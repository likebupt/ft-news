"""Daily news fetcher - pulls RSS feeds and filters for finetuning relevance."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import httpx

from config import DATA_DIR, RELEVANCE_KEYWORDS, SEEN_URLS_FILE
from sources import SOURCES, NewsSource

logger = logging.getLogger(__name__)

# Compile a single regex for fast keyword matching
_KW_PATTERN = re.compile(
    "|".join(re.escape(kw) for kw in RELEVANCE_KEYWORDS),
    re.IGNORECASE,
)

# httpx timeout settings
_TIMEOUT = httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0)
_HEADERS = {
    "User-Agent": (
        "FTNewsWeekly/1.0 (Microsoft Foundry Finetuning; "
        "+https://github.com/microsoft/ft-news-weekly)"
    )
}


@dataclass
class Article:
    """A single fetched article."""

    title: str
    url: str
    source_name: str
    category: str
    published: str  # ISO-8601 string
    summary: str  # Raw excerpt / description from feed
    relevance_score: float = 0.0  # 0-1, set during filtering

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class DailyFetchResult:
    """Result of a daily fetch run."""

    date: str
    articles: list[Article] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Seen-URL tracking (simple JSON file)
# ---------------------------------------------------------------------------

def _load_seen_urls() -> set[str]:
    if SEEN_URLS_FILE.exists():
        return set(json.loads(SEEN_URLS_FILE.read_text(encoding="utf-8")))
    return set()


def _save_seen_urls(urls: set[str]) -> None:
    SEEN_URLS_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Keep only the most recent 10 000 URLs to avoid unbounded growth
    trimmed = sorted(urls)[-10_000:]
    SEEN_URLS_FILE.write_text(
        json.dumps(trimmed, indent=0), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Feed parsing
# ---------------------------------------------------------------------------

def _parse_published(entry: dict) -> str:
    """Extract a published date string from a feed entry."""
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


def _entry_text(entry: dict) -> str:
    """Get the best available text for relevance matching."""
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
    """Return a relevance score (0-1) based on keyword hits."""
    matches = _KW_PATTERN.findall(text.lower())
    if not matches:
        return 0.0
    unique = len(set(m.lower() for m in matches))
    # More unique keyword hits → higher score, cap at 1.0
    return min(unique / 3.0, 1.0)


def _fetch_feed(source: NewsSource, client: httpx.Client) -> list[Article]:
    """Fetch and parse a single RSS/Atom feed."""
    try:
        resp = client.get(source.feed_url)
        resp.raise_for_status()
    except httpx.HTTPError as exc:
        logger.warning("Failed to fetch %s: %s", source.name, exc)
        return []

    feed = feedparser.parse(resp.text)
    articles: list[Article] = []

    for entry in feed.entries:
        url = entry.get("link", "")
        if not url:
            continue

        text = _entry_text(entry)
        score = _is_relevant(text)
        if score <= 0:
            continue

        articles.append(
            Article(
                title=entry.get("title", "(no title)"),
                url=url,
                source_name=source.name,
                category=source.category,
                published=_parse_published(entry),
                summary=entry.get("summary", "")[:1000],
                relevance_score=score,
            )
        )

    logger.info(
        "Fetched %s: %d entries, %d relevant",
        source.name,
        len(feed.entries),
        len(articles),
    )
    return articles


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def fetch_daily(sources: list[NewsSource] | None = None) -> DailyFetchResult:
    """Fetch all sources, filter for relevance, deduplicate, return results."""
    sources = sources or SOURCES
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    result = DailyFetchResult(date=today)
    seen = _load_seen_urls()

    with httpx.Client(timeout=_TIMEOUT, headers=_HEADERS, follow_redirects=True) as client:
        for source in sources:
            try:
                articles = _fetch_feed(source, client)
                for article in articles:
                    if article.url in seen:
                        continue
                    seen.add(article.url)
                    result.articles.append(article)
            except Exception as exc:
                msg = f"Error processing {source.name}: {exc}"
                logger.error(msg)
                result.errors.append(msg)

    # Sort by relevance (highest first), then by source
    result.articles.sort(key=lambda a: (-a.relevance_score, a.source_name))

    _save_seen_urls(seen)

    logger.info(
        "Daily fetch complete: %d articles from %d sources, %d errors",
        len(result.articles),
        len(sources),
        len(result.errors),
    )
    return result


def save_daily_result(result: DailyFetchResult) -> Path:
    """Save daily fetch result as a JSON file in the weekly folder."""
    dt = datetime.fromisoformat(result.date)
    week_num = dt.isocalendar()[1]
    year = dt.isocalendar()[0]
    week_dir = DATA_DIR / str(year) / f"week-{week_num:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)

    day_name = dt.strftime("%A").lower()
    out_file = week_dir / f"{day_name}-raw.json"
    out_file.write_text(
        json.dumps(
            {
                "date": result.date,
                "article_count": len(result.articles),
                "articles": [a.to_dict() for a in result.articles],
                "errors": result.errors,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    logger.info("Saved daily raw data to %s", out_file)
    return out_file
