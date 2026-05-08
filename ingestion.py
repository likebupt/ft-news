"""Async ingestion layer — fetches RSS feeds concurrently with rate limiting.

Runs as a background / scheduled job.  All fetched articles go straight into
the SQLite database via the storage module.  Network I/O is fully async
(aiohttp) with a semaphore to cap concurrent connections.
"""

from __future__ import annotations

import asyncio
import logging
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone

import aiohttp
import feedparser

from config import RELEVANCE_KEYWORDS
from sources import SOURCES, NewsSource
from storage import get_existing_urls, init_db, insert_articles

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Relevance filter (shared with old fetcher, kept in sync)
# ---------------------------------------------------------------------------

_KW_PATTERN = re.compile(
    "|".join(re.escape(kw) for kw in RELEVANCE_KEYWORDS),
    re.IGNORECASE,
)

_HEADERS = {
    "User-Agent": (
        "FTNewsWeekly/2.0 (Microsoft Foundry Finetuning; "
        "+https://github.com/microsoft/ft-news-weekly)"
    )
}

# Concurrency knobs
MAX_CONCURRENT = 8          # at most 8 feeds in flight at once
CONNECT_TIMEOUT = 15        # seconds
READ_TIMEOUT = 30           # seconds
MAX_RETRIES = 2             # retry failed feeds once


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _entry_text(entry: dict) -> str:
    parts: list[str] = []
    if entry.get("title"):
        parts.append(entry["title"])
    if entry.get("summary"):
        parts.append(entry["summary"])
    for content in entry.get("content", []):
        if content.get("value"):
            parts.append(content["value"])
    return " ".join(parts)


def _is_relevant(text: str) -> float:
    matches = _KW_PATTERN.findall(text.lower())
    if not matches:
        return 0.0
    unique = len(set(m.lower() for m in matches))
    return min(unique / 3.0, 1.0)


def _parse_published(entry: dict) -> str:
    for key in ("published_parsed", "updated_parsed"):
        tp = entry.get(key)
        if tp:
            try:
                return datetime(*tp[:6], tzinfo=timezone.utc).isoformat()
            except Exception:
                pass
    for key in ("published", "updated"):
        val = entry.get(key)
        if val:
            return val
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Async feed fetcher
# ---------------------------------------------------------------------------

@dataclass
class _FeedResult:
    source: str
    total_entries: int = 0
    relevant: int = 0
    articles: list[dict] | None = None
    error: str | None = None


async def _fetch_one(
    source: NewsSource,
    session: aiohttp.ClientSession,
    sem: asyncio.Semaphore,
) -> _FeedResult:
    """Fetch a single RSS feed with retry + semaphore."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with sem:
                async with session.get(
                    source.feed_url,
                    timeout=aiohttp.ClientTimeout(
                        sock_connect=CONNECT_TIMEOUT,
                        sock_read=READ_TIMEOUT,
                    ),
                    allow_redirects=True,
                ) as resp:
                    if resp.status >= 400:
                        return _FeedResult(source=source.name, error=f"HTTP {resp.status}")
                    body = await resp.text()
        except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
            if attempt < MAX_RETRIES:
                await asyncio.sleep(1.0 * attempt)
                continue
            return _FeedResult(source=source.name, error=str(exc))

        # Parse (CPU-bound but fast enough in-process)
        feed = feedparser.parse(body)
        articles: list[dict] = []
        for entry in feed.entries:
            url = entry.get("link", "")
            if not url:
                continue
            text = _entry_text(entry)
            score = _is_relevant(text)
            if score <= 0:
                continue
            articles.append({
                "url": url,
                "title": entry.get("title", "(no title)"),
                "source_name": source.name,
                "category": source.category,
                "published": _parse_published(entry),
                "summary": entry.get("summary", "")[:2000],
                "relevance_score": score,
            })

        logger.info(
            "Fetched %s: %d entries, %d relevant",
            source.name, len(feed.entries), len(articles),
        )
        return _FeedResult(
            source=source.name,
            total_entries=len(feed.entries),
            relevant=len(articles),
            articles=articles,
        )

    return _FeedResult(source=source.name, error="max retries exceeded")


async def _ingest_all(sources: list[NewsSource]) -> dict:
    """Fetch all sources concurrently, deduplicate, store in DB."""
    init_db()
    batch_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-") + uuid.uuid4().hex[:6]
    sem = asyncio.Semaphore(MAX_CONCURRENT)

    async with aiohttp.ClientSession(headers=_HEADERS) as session:
        tasks = [_fetch_one(src, session, sem) for src in sources]
        results: list[_FeedResult] = await asyncio.gather(*tasks)

    # Collect all candidate articles
    all_articles: list[dict] = []
    errors: list[str] = []
    for r in results:
        if r.error:
            errors.append(f"{r.source}: {r.error}")
        if r.articles:
            all_articles.extend(r.articles)

    # Deduplicate against DB in one query
    candidate_urls = [a["url"] for a in all_articles]
    existing = get_existing_urls(candidate_urls)
    new_articles = [a for a in all_articles if a["url"] not in existing]

    # Insert
    inserted = insert_articles(new_articles, batch_id) if new_articles else 0

    stats = {
        "batch_id": batch_id,
        "sources_total": len(sources),
        "sources_ok": sum(1 for r in results if r.error is None),
        "total_entries": sum(r.total_entries for r in results),
        "relevant_found": len(all_articles),
        "duplicates_skipped": len(all_articles) - len(new_articles),
        "inserted": inserted,
        "errors": errors,
    }
    logger.info(
        "Ingestion batch %s: %d sources, %d relevant, %d new, %d dupes, %d errors",
        batch_id,
        stats["sources_total"],
        stats["relevant_found"],
        stats["inserted"],
        stats["duplicates_skipped"],
        len(errors),
    )
    return stats


# ---------------------------------------------------------------------------
# Public sync wrapper (called from CLI / scheduler)
# ---------------------------------------------------------------------------

def run_ingestion(sources: list[NewsSource] | None = None) -> dict:
    """Synchronous entry point — runs the async ingestion loop."""
    src = sources or SOURCES
    # Avoid "Event loop is closed" RuntimeError on Windows / Python 3.9
    import sys
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return asyncio.run(_ingest_all(src))
