"""LLM-based summarizer - uses Azure AI Foundry Responses API."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

import httpx

from config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_OPENAI_ENDPOINT,
    DATA_DIR,
)
from fetcher import Article, DailyFetchResult

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Responses API helper
# ---------------------------------------------------------------------------

_TIMEOUT = httpx.Timeout(connect=30.0, read=300.0, write=30.0, pool=30.0)


def _call_responses_api(system_prompt: str, user_msg: str) -> str:
    """Call the Azure AI Foundry Responses API and return the text output."""
    url = f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/responses"
    headers = {
        "api-key": AZURE_OPENAI_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "model": AZURE_OPENAI_DEPLOYMENT,
        "instructions": system_prompt,
        "input": user_msg,
        "max_output_tokens": 16384,
        "truncation": "auto",
    }

    resp = httpx.post(url, headers=headers, json=payload, timeout=_TIMEOUT)
    if resp.status_code != 200:
        logger.error("Responses API error %d: %s", resp.status_code, resp.text[:500])
    resp.raise_for_status()
    data = resp.json()

    # Extract text from response output
    for item in data.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    return content.get("text", "")
    logger.warning("No text found in API response: %s", str(data)[:500])
    return ""


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

_DAILY_SYSTEM_PROMPT = """\
You are an AI research analyst specializing in fine-tuning and post-training \
for large language models. Your audience is a product team at Microsoft working \
on fine-tuning infrastructure (Foundry Finetuning).

Your job is to summarize a batch of collected articles into a concise daily \
briefing. Follow these rules:
1. Group articles by COMPANY / ORGANIZATION.
2. Under each company heading, write 1-3 bullet points per article.
3. Each bullet should capture: what was announced/released, why it matters \
   for finetuning/post-training, and any key technical details.
4. If an article is not actually relevant to finetuning/post-training, skip it.
5. At the end, add a "Key Takeaways" section with 2-3 bullets summarizing \
   the most important developments of the day.
6. Write in clear, professional English.
7. Every bullet MUST end with a clickable markdown link to the original \
   source, e.g. [Read more](URL). This is critical for the weekly rollup.
"""

_WEEKLY_SYSTEM_PROMPT = """\
You are an AI research analyst creating a weekly digest for the Microsoft \
Foundry Finetuning product team. You will receive daily summaries from the \
past week.

Create a polished "Weekly Finetuning & Post-Training Update" that is \
HIGHLY READABLE and CONCISE. A busy PM should be able to scan it in \
5-10 minutes and walk away knowing what happened.

Format rules:
1. Start with a one-sentence "TL;DR" of the week.
2. **Top Stories** — 3-5 bullet points, ranked by impact. Each bullet is \
   ONE concise sentence describing what happened and why it matters. \
   End each bullet with a markdown link: [Read more](URL)
3. **By Company** — Group remaining noteworthy items by company. Use \
   sub-bullets, each ONE sentence max. Include [Source](URL) at the end.
4. **Notable Papers** — Only if significant. One bullet per paper with \
   [Paper](URL).
5. **What This Means for Us** — 2-3 bullets on implications for our \
   Foundry Finetuning product.

Style guidelines:
- Be ruthlessly concise. Prefer short, punchy bullets over paragraphs.
- Every bullet MUST end with a clickable markdown link to the original source.
- Use format: "[Read more](https://...)" or "[Source](https://...)" or \
  "[Paper](https://...)".
- Do NOT repeat the same news across sections.
- Skip anything that is only tangentially relevant to finetuning.
- Write in clear, professional English.
- Total length should be ~30-50 bullet points maximum.
"""


# ---------------------------------------------------------------------------
# Summarization functions
# ---------------------------------------------------------------------------

def _format_articles_for_prompt(articles: list[Article]) -> str:
    """Format articles into a text block for the LLM."""
    lines: list[str] = []
    for i, a in enumerate(articles, 1):
        lines.append(f"--- Article {i} ---")
        lines.append(f"Source: {a.source_name} ({a.category})")
        lines.append(f"Title: {a.title}")
        lines.append(f"URL: {a.url}")
        lines.append(f"Published: {a.published}")
        lines.append(f"Excerpt: {a.summary[:500]}")
        lines.append("")
    return "\n".join(lines)


def summarize_daily(result: DailyFetchResult) -> str:
    """Summarize the day's articles using Azure AI Foundry, return markdown."""
    if not result.articles:
        return f"# Daily Finetuning News - {result.date}\n\nNo relevant articles found today.\n"

    # Limit to top 20 articles by relevance to stay within token limits
    articles = sorted(result.articles, key=lambda a: a.relevance_score, reverse=True)[:20]
    articles_text = _format_articles_for_prompt(articles)
    user_msg = (
        f"Today is {result.date}. Here are {len(articles)} articles "
        f"collected from official AI company blogs and research feeds. "
        f"Please create the daily briefing.\n\n{articles_text}"
    )

    logger.info("Sending %d articles to LLM for daily summary...", len(articles))
    summary = _call_responses_api(_DAILY_SYSTEM_PROMPT, user_msg)
    logger.info("Daily summary generated (%d chars)", len(summary))
    return summary


def save_daily_summary(summary: str, date_str: str) -> Path:
    """Save the daily summary markdown in the weekly folder."""
    dt = datetime.fromisoformat(date_str)
    week_num = dt.isocalendar()[1]
    year = dt.isocalendar()[0]
    week_dir = DATA_DIR / str(year) / f"week-{week_num:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)

    day_name = dt.strftime("%A").lower()
    out_file = week_dir / f"{day_name}.md"
    out_file.write_text(summary, encoding="utf-8")
    logger.info("Saved daily summary to %s", out_file)
    return out_file


def summarize_weekly(daily_summaries: list[str], week_label: str) -> str:
    """Create a weekly digest from daily summaries using Azure AI Foundry."""
    if not daily_summaries:
        return f"# Weekly Finetuning Update - {week_label}\n\nNo news collected this week.\n"

    combined = "\n\n---\n\n".join(daily_summaries)
    user_msg = (
        f"Here are the daily finetuning/post-training briefings from {week_label}. "
        f"Please create the weekly digest.\n\n{combined}"
    )

    logger.info("Sending %d daily summaries to LLM for weekly digest...", len(daily_summaries))
    digest = _call_responses_api(_WEEKLY_SYSTEM_PROMPT, user_msg)
    logger.info("Weekly digest generated (%d chars)", len(digest))
    return digest


def save_weekly_digest(digest: str, year: int, week_num: int) -> Path:
    """Save the weekly digest markdown."""
    week_dir = DATA_DIR / str(year) / f"week-{week_num:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)
    out_file = week_dir / "weekly-digest.md"
    out_file.write_text(digest, encoding="utf-8")
    logger.info("Saved weekly digest to %s", out_file)
    return out_file
