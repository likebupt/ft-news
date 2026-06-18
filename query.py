"""Query-time module — fast path for generating digests from pre-collected data.

This module NEVER touches the network.  It reads from the SQLite database
(populated by the ingestion layer) and uses cached summaries when available.
If no cached summary exists, it runs map-reduce summarisation.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

from map_reduce import map_reduce_daily, map_reduce_weekly
from preprocessing import chunk_articles, deduplicate, rank_and_select
from storage import get_summary, init_db, query_articles

logger = logging.getLogger(__name__)


def weekly_digest(
    year: int | None = None,
    week: int | None = None,
    *,
    force: bool = False,
    max_articles: int = 200,
    chunk_size: int = 10,
) -> str:
    """Generate (or retrieve cached) weekly digest.

    Fast path: returns cached digest if already computed.
    Slow path: runs map-reduce summarisation on DB articles.

    Parameters
    ----------
    year, week : target ISO week.  Defaults to the *previous* week.
    force : if True, ignore cache and re-summarise.
    max_articles : max articles to feed into summarisation.
    chunk_size : articles per map chunk.

    Returns
    -------
    Markdown digest string.
    """
    init_db()

    if year is None or week is None:
        ref = datetime.now(timezone.utc) - timedelta(weeks=1)
        year, week, _ = ref.isocalendar()

    scope_key = f"{year}-W{week:02d}"

    # Fast path 1: DB cache
    if not force:
        cached = get_summary("weekly", scope_key)
        if cached:
            logger.info("Returning cached weekly digest for %s", scope_key)
            return cached

    # Fast path 2: existing markdown file on disk (e.g. committed to git)
    from config import DATA_DIR
    digest_file = DATA_DIR / str(year) / f"week-{week:02d}" / "weekly-digest.md"
    if not force and digest_file.exists():
        content = digest_file.read_text(encoding="utf-8").strip()
        if content and "No news collected" not in content and "No articles found" not in content:
            logger.info("Returning existing digest file for %s", scope_key)
            return content

    # Slow path: query → preprocess → map-reduce
    logger.info("Building weekly digest for %s from DB…", scope_key)
    monday = datetime.fromisocalendar(year, week, 1).replace(tzinfo=timezone.utc)
    sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)

    articles = query_articles(since=monday.isoformat(), until=sunday.isoformat())
    if not articles:
        # Don't overwrite an existing digest with "no articles"
        if digest_file.exists():
            logger.warning("DB has no articles for %s but digest file exists — keeping it", scope_key)
            return digest_file.read_text(encoding="utf-8")
        return f"# Weekly Finetuning Update — {year} Week {week}\n\nNo articles found for this week.\n"

    articles = deduplicate(articles)
    articles = rank_and_select(articles, max_total=max_articles)
    chunks = chunk_articles(articles, chunk_size=chunk_size)

    return map_reduce_weekly(chunks, year, week)


def daily_digest(
    date_str: str | None = None,
    *,
    force: bool = False,
    max_articles: int = 100,
    chunk_size: int = 10,
) -> str:
    """Generate (or retrieve cached) daily digest.

    Parameters
    ----------
    date_str : ISO date string (e.g. "2026-05-08").  Defaults to today.
    force : if True, ignore cache and re-summarise.
    """
    init_db()

    if not date_str:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    scope_key = f"daily-{date_str}"

    if not force:
        cached = get_summary("daily_merged", scope_key)
        if cached:
            logger.info("Returning cached daily digest for %s", scope_key)
            return cached

    # Query today's articles
    day_start = f"{date_str}T00:00:00+00:00"
    day_end = f"{date_str}T23:59:59+00:00"
    articles = query_articles(since=day_start, until=day_end)

    if not articles:
        return f"# Daily Finetuning News — {date_str}\n\nNo articles found for today.\n"

    articles = deduplicate(articles)
    articles = rank_and_select(articles, max_total=max_articles)
    chunks = chunk_articles(articles, chunk_size=chunk_size)

    return map_reduce_daily(chunks, date_str)


def stats() -> dict:
    """Return quick stats about the database."""
    init_db()
    from storage import article_count, list_summaries

    return {
        "total_articles": article_count(),
        "weekly_digests": len(list_summaries("weekly")),
        "daily_digests": len(list_summaries("daily_merged")),
        "cached_chunks": len(list_summaries("daily_chunk")),
    }
