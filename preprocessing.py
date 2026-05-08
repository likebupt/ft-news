"""Preprocessing layer — dedup, time-window filtering, topic grouping.

Runs offline after ingestion.  Reads from SQLite, produces a clean set
of articles ready for summarisation.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from storage import query_articles

logger = logging.getLogger(__name__)


def get_week_range(year: int, week: int) -> tuple[str, str]:
    """Return (monday_iso, sunday_iso) for the given ISO year/week."""
    monday = datetime.fromisocalendar(year, week, 1).replace(tzinfo=timezone.utc)
    sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
    return monday.isoformat(), sunday.isoformat()


def get_recent_articles(days: int = 7, min_relevance: float = 0.0) -> list[dict]:
    """Return articles from the last *days* days."""
    since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    return query_articles(since=since, min_relevance=min_relevance)


def get_week_articles(year: int, week: int, min_relevance: float = 0.0) -> list[dict]:
    """Return articles for a specific ISO week."""
    since, until = get_week_range(year, week)
    return query_articles(since=since, until=until, min_relevance=min_relevance)


def deduplicate(articles: list[dict]) -> list[dict]:
    """Remove articles with the same URL (DB enforces uniqueness but JSON
    imports might have near-duplicates with similar titles)."""
    seen_urls: set[str] = set()
    seen_titles: set[str] = set()
    out: list[dict] = []
    for a in articles:
        url = a.get("url", "")
        title_key = a.get("title", "").lower().strip()
        if url in seen_urls or title_key in seen_titles:
            continue
        seen_urls.add(url)
        seen_titles.add(title_key)
        out.append(a)
    logger.info("Dedup: %d → %d articles", len(articles), len(out))
    return out


def group_by_source(articles: list[dict]) -> dict[str, list[dict]]:
    """Group articles by source_name."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for a in articles:
        groups[a.get("source_name", "Unknown")].append(a)
    return dict(groups)


def rank_and_select(
    articles: list[dict],
    max_total: int = 200,
    max_per_source: int = 30,
) -> list[dict]:
    """Rank by relevance, cap per-source, return top articles."""
    # Sort globally by relevance
    sorted_all = sorted(articles, key=lambda a: a.get("relevance_score", 0), reverse=True)

    source_counts: dict[str, int] = defaultdict(int)
    selected: list[dict] = []
    for a in sorted_all:
        src = a.get("source_name", "")
        if source_counts[src] >= max_per_source:
            continue
        source_counts[src] += 1
        selected.append(a)
        if len(selected) >= max_total:
            break

    logger.info(
        "Selected %d articles (from %d) across %d sources",
        len(selected), len(articles), len(source_counts),
    )
    return selected


def chunk_articles(articles: list[dict], chunk_size: int = 15) -> list[list[dict]]:
    """Split articles into chunks for map-reduce summarisation."""
    chunks = [articles[i:i + chunk_size] for i in range(0, len(articles), chunk_size)]
    logger.info("Split %d articles into %d chunks of ≤%d", len(articles), len(chunks), chunk_size)
    return chunks


def prepare_for_summarisation(
    year: int,
    week: int,
    *,
    max_total: int = 200,
    max_per_source: int = 30,
    chunk_size: int = 15,
) -> list[list[dict]]:
    """Full preprocessing pipeline: fetch from DB → dedup → rank → chunk.

    Returns a list of article chunks ready for the map step.
    """
    raw = get_week_articles(year, week)
    if not raw:
        logger.warning("No articles found for %d-W%02d", year, week)
        return []

    deduped = deduplicate(raw)
    selected = rank_and_select(deduped, max_total=max_total, max_per_source=max_per_source)
    return chunk_articles(selected, chunk_size=chunk_size)
