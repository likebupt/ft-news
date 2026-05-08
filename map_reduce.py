"""Map-reduce summarisation — handles large article sets without timeouts.

Strategy
--------
1. **Map**: Summarise each chunk of ~15 articles independently (parallel-safe).
2. **Reduce**: Merge all chunk summaries into one final digest.

Each step is a separate LLM call with bounded input size, so:
- No context-window overflow
- No extreme latency
- Individual retries on failure

Summary results are cached in the DB so re-runs skip already-done chunks.
"""

from __future__ import annotations

import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import httpx

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT,
    DATA_DIR,
)
from storage import get_summary, save_summary

logger = logging.getLogger(__name__)

_TIMEOUT = httpx.Timeout(connect=30.0, read=600.0, write=30.0, pool=30.0)
_MAX_RETRIES = 2


# ---------------------------------------------------------------------------
# LLM call (Azure Responses API)
# ---------------------------------------------------------------------------

def _call_llm(instructions: str, user_input: str, max_tokens: int = 8192) -> str:
    """Call Azure AI Foundry Responses API with retry."""
    url = f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/responses"
    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "model": AZURE_OPENAI_DEPLOYMENT,
        "instructions": instructions,
        "input": user_input,
        "max_output_tokens": max_tokens,
        "truncation": "auto",
    }

    for attempt in range(1, _MAX_RETRIES + 1):
        t0 = time.monotonic()
        try:
            resp = httpx.post(url, headers=headers, json=payload, timeout=_TIMEOUT)
            elapsed = time.monotonic() - t0
            if resp.status_code != 200:
                logger.warning(
                    "LLM call attempt %d failed: HTTP %d (%.1fs) — %s",
                    attempt, resp.status_code, elapsed, resp.text[:300],
                )
                if attempt < _MAX_RETRIES:
                    time.sleep(2.0 * attempt)
                    continue
                resp.raise_for_status()

            data = resp.json()
            for item in data.get("output", []):
                if item.get("type") == "message":
                    for c in item.get("content", []):
                        if c.get("type") == "output_text":
                            text = c.get("text", "")
                            logger.info("LLM response: %d chars in %.1fs", len(text), elapsed)
                            return text

            logger.warning("No output_text in LLM response (%.1fs)", elapsed)
            return ""

        except httpx.TimeoutException:
            elapsed = time.monotonic() - t0
            logger.warning("LLM timeout attempt %d (%.1fs)", attempt, elapsed)
            if attempt < _MAX_RETRIES:
                time.sleep(2.0 * attempt)
            else:
                raise

    return ""


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

_MAP_PROMPT = """\
You are an AI research analyst specialising in fine-tuning and post-training \
for large language models.

Summarise the following batch of articles into concise bullet points grouped \
by COMPANY / ORGANISATION:
- 1-2 sentences per article: what happened and why it matters for finetuning.
- Skip clearly irrelevant articles.
- Every bullet MUST end with a markdown link: [Read more](URL)
- Be concise — this output will be merged with other batches later.
"""

_REDUCE_PROMPT = """\
You are an AI research analyst creating a weekly digest for the Microsoft \
Foundry Finetuning product team.  You will receive several partial summaries \
from different batches of articles from the same week.

Merge them into ONE polished "Weekly Finetuning & Post-Training Update":

1. **TL;DR** — one sentence overview of the week.
2. **Top Stories** — 3-5 most impactful items. One sentence each with [Read more](URL).
3. **By Company** — remaining noteworthy items grouped by company. \
   One sentence sub-bullets with [Source](URL).
4. **Notable Papers** — significant research only. [Paper](URL).
5. **What This Means for Us** — 2-3 bullets on implications for Foundry Finetuning.

Rules:
- Be ruthlessly concise.  A busy PM should scan this in 5-10 minutes.
- Every bullet MUST end with a clickable markdown link.
- Do NOT repeat the same news across sections.
- Skip tangentially relevant items.
- Total: ~30-50 bullet points max.
"""

_DAILY_MAP_PROMPT = """\
You are an AI research analyst specialising in fine-tuning and post-training.

Summarise these articles into a concise daily briefing grouped by company:
- 1-3 bullet points per article with key details.
- Skip irrelevant articles.
- End each bullet with [Read more](URL).
- Add a "Key Takeaways" section (2-3 bullets) at the end.
"""


# ---------------------------------------------------------------------------
# Format helpers
# ---------------------------------------------------------------------------

def _format_chunk(articles: list[dict]) -> str:
    lines: list[str] = []
    for i, a in enumerate(articles, 1):
        lines.append(f"--- Article {i} ---")
        lines.append(f"Source: {a.get('source_name', '')} ({a.get('category', '')})")
        lines.append(f"Title: {a.get('title', '')}")
        lines.append(f"URL: {a.get('url', '')}")
        lines.append(f"Published: {a.get('published', '')}")
        excerpt = a.get("summary", "")[:400]
        lines.append(f"Excerpt: {excerpt}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Map step
# ---------------------------------------------------------------------------

def summarise_chunk(
    chunk: list[dict],
    chunk_index: int,
    scope_prefix: str,
    *,
    prompt: str = _MAP_PROMPT,
    kind: str = "daily_chunk",
) -> str:
    """Summarise a single chunk. Uses DB cache if available."""
    scope_key = f"{scope_prefix}-chunk-{chunk_index}"

    cached = get_summary(kind, scope_key)
    if cached:
        logger.info("Cache hit: %s/%s", kind, scope_key)
        return cached

    user_input = (
        f"Batch {chunk_index + 1}: {len(chunk)} articles.\n\n"
        + _format_chunk(chunk)
    )

    text = _call_llm(prompt, user_input)
    if text:
        article_ids = [a.get("id") for a in chunk if a.get("id")]
        save_summary(kind, scope_key, text, article_ids)
    return text


# ---------------------------------------------------------------------------
# Parallel map
# ---------------------------------------------------------------------------

def _map_chunks_parallel(
    chunks: list[list[dict]],
    scope_prefix: str,
    *,
    prompt: str = _MAP_PROMPT,
    kind: str = "daily_chunk",
    max_workers: int = 3,
) -> list[str]:
    """Map step: summarise all chunks in parallel using threads."""
    results: list[str | None] = [None] * len(chunks)

    def _do_chunk(idx: int, chunk: list[dict]) -> tuple[int, str]:
        return idx, summarise_chunk(chunk, idx, scope_prefix, prompt=prompt, kind=kind)

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_do_chunk, i, c): i for i, c in enumerate(chunks)}
        for future in as_completed(futures):
            idx, text = future.result()
            results[idx] = text
            logger.info("Chunk %d/%d done", idx + 1, len(chunks))

    return [r for r in results if r]


# ---------------------------------------------------------------------------
# Reduce step
# ---------------------------------------------------------------------------

def merge_summaries(
    partial_summaries: list[str],
    scope_key: str,
    *,
    prompt: str = _REDUCE_PROMPT,
    kind: str = "weekly",
) -> str:
    """Merge partial summaries into a final digest. Uses DB cache."""
    cached = get_summary(kind, scope_key)
    if cached:
        logger.info("Cache hit: %s/%s", kind, scope_key)
        return cached

    combined = "\n\n---\n\n".join(
        f"## Partial Summary {i+1}\n\n{s}" for i, s in enumerate(partial_summaries) if s
    )
    if not combined.strip():
        return ""

    user_input = (
        f"Here are {len(partial_summaries)} partial summaries from this week. "
        f"Please merge into the final weekly digest.\n\n{combined}"
    )

    text = _call_llm(prompt, user_input, max_tokens=16384)
    if text:
        save_summary(kind, scope_key, text)
    return text


# ---------------------------------------------------------------------------
# High-level orchestrators
# ---------------------------------------------------------------------------

def map_reduce_weekly(
    chunks: list[list[dict]],
    year: int,
    week: int,
) -> str:
    """Full map-reduce pipeline for a weekly digest.

    1.  Map each chunk → partial summary  (sequential to respect rate limits)
    2.  Reduce all partials → final digest
    3.  Save final digest as markdown file + DB cache
    """
    scope_prefix = f"{year}-W{week:02d}"

    if not chunks:
        return f"# Weekly Finetuning Update — {year} Week {week}\n\nNo relevant articles this week.\n"

    # --- Map (parallel) ---
    logger.info("Map step: %d chunks for %s (parallel)", len(chunks), scope_prefix)
    partials = _map_chunks_parallel(chunks, scope_prefix)

    if not partials:
        return f"# Weekly Finetuning Update — {year} Week {week}\n\nSummarisation produced no output.\n"

    # --- Reduce ---
    logger.info("Reduce step: merging %d partial summaries…", len(partials))
    digest = merge_summaries(partials, scope_prefix)

    # --- Persist as markdown file (for site builder compatibility) ---
    if digest:
        week_dir = DATA_DIR / str(year) / f"week-{week:02d}"
        week_dir.mkdir(parents=True, exist_ok=True)
        out = week_dir / "weekly-digest.md"
        out.write_text(digest, encoding="utf-8")
        logger.info("Weekly digest written to %s (%d chars)", out, len(digest))

    return digest


def map_reduce_daily(
    chunks: list[list[dict]],
    date_str: str,
) -> str:
    """Map-reduce pipeline for a daily summary."""
    scope_prefix = f"daily-{date_str}"

    if not chunks:
        return f"# Daily Finetuning News — {date_str}\n\nNo relevant articles today.\n"

    partials = _map_chunks_parallel(
        chunks, scope_prefix,
        prompt=_DAILY_MAP_PROMPT,
        kind="daily_chunk",
    )

    if not partials:
        return f"# Daily Finetuning News — {date_str}\n\nSummarisation produced no output.\n"

    # For daily, if only one chunk, skip reduce
    if len(partials) == 1:
        digest = partials[0]
    else:
        daily_reduce = (
            "Merge these partial daily summaries into one cohesive daily briefing. "
            "Group by company, keep bullets concise with links. "
            "Add Key Takeaways at the end."
        )
        digest = merge_summaries(
            partials, scope_prefix, prompt=daily_reduce, kind="daily_merged"
        )

    # Persist
    if digest:
        dt = datetime.fromisoformat(date_str)
        iso_year, iso_week, _ = dt.isocalendar()
        week_dir = DATA_DIR / str(iso_year) / f"week-{iso_week:02d}"
        week_dir.mkdir(parents=True, exist_ok=True)
        day_name = dt.strftime("%A").lower()
        out = week_dir / f"{day_name}.md"
        out.write_text(digest, encoding="utf-8")
        logger.info("Daily summary written to %s", out)

    return digest
