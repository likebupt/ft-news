"""Generate daily summaries and weekly digests directly from raw JSON data.

This module is a fallback when Azure OpenAI is not available. It formats
the raw article data into structured markdown without LLM summarization.
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from config import DATA_DIR

logger = logging.getLogger(__name__)


def _load_raw_articles(json_path: Path) -> list[dict]:
    """Load articles from a raw JSON file."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    return data.get("articles", [])


def _format_daily_md(articles: list[dict], date_str: str) -> str:
    """Format articles into a markdown daily summary grouped by source."""
    if not articles:
        return f"# Daily Finetuning News - {date_str}\n\nNo relevant articles found today.\n"

    # Group by source/company
    by_source: dict[str, list[dict]] = defaultdict(list)
    for a in articles:
        by_source[a.get("source_name", "Unknown")].append(a)

    lines: list[str] = [f"# Daily Finetuning News - {date_str}\n"]

    # Sort sources: bigtech first, then tools, then research
    category_order = {"bigtech": 0, "tools": 1, "research": 2}
    sorted_sources = sorted(
        by_source.items(),
        key=lambda x: (
            category_order.get(x[1][0].get("category", ""), 9),
            x[0],
        ),
    )

    for source_name, source_articles in sorted_sources:
        lines.append(f"\n## {source_name}\n")
        # Limit to top 10 per source by relevance
        top = sorted(source_articles, key=lambda a: a.get("relevance_score", 0), reverse=True)[:10]
        for a in top:
            title = a.get("title", "Untitled")
            url = a.get("url", "")
            summary = a.get("summary", "")
            # Truncate summary
            if len(summary) > 150:
                summary = summary[:147] + "..."
            lines.append(f"- **{title}**")
            if summary:
                lines.append(f"  {summary}")
            lines.append(f"  [Read more]({url})")
            lines.append("")

    lines.append(f"\n---\n*{len(articles)} articles collected from {len(by_source)} sources.*\n")
    return "\n".join(lines)


def _format_weekly_digest_md(
    all_articles: list[dict], week_label: str
) -> str:
    """Format a weekly digest from all articles across the week."""
    if not all_articles:
        return f"# Weekly Finetuning Update - {week_label}\n\nNo news collected this week.\n"

    # Group by source
    by_source: dict[str, list[dict]] = defaultdict(list)
    for a in all_articles:
        by_source[a.get("source_name", "Unknown")].append(a)

    # Pick top articles overall by relevance
    top_all = sorted(all_articles, key=lambda a: a.get("relevance_score", 0), reverse=True)[:30]

    lines: list[str] = [
        f"# Weekly Finetuning & Post-Training Update - {week_label}\n",
        f"**TL;DR**: {len(all_articles)} finetuning-related articles collected "
        f"from {len(by_source)} sources this week.\n",
        "\n## Top Stories\n",
    ]

    # Top 5 articles
    seen_titles: set[str] = set()
    count = 0
    for a in top_all:
        title = a.get("title", "")
        if title in seen_titles:
            continue
        seen_titles.add(title)
        url = a.get("url", "")
        source = a.get("source_name", "")
        summary = a.get("summary", "")
        if len(summary) > 120:
            summary = summary[:117] + "..."
        lines.append(f"- **{title}** ({source}) — {summary} [Read more]({url})")
        lines.append("")
        count += 1
        if count >= 5:
            break

    lines.append("\n## By Company\n")

    category_order = {"bigtech": 0, "tools": 1, "research": 2}
    sorted_sources = sorted(
        by_source.items(),
        key=lambda x: (
            category_order.get(x[1][0].get("category", ""), 9),
            x[0],
        ),
    )

    for source_name, source_articles in sorted_sources:
        # Top 5 per source for weekly
        top = sorted(source_articles, key=lambda a: a.get("relevance_score", 0), reverse=True)[:5]
        lines.append(f"\n### {source_name}\n")
        for a in top:
            title = a.get("title", "")
            if title in seen_titles:
                continue
            seen_titles.add(title)
            url = a.get("url", "")
            lines.append(f"- {title} [Source]({url})")
        lines.append("")

    lines.append(
        f"\n---\n*Generated from raw article data. "
        f"Full LLM-powered analysis will be available when Azure OpenAI is configured.*\n"
    )
    return "\n".join(lines)


def generate_from_raw(year: int, week_num: int) -> tuple[Path | None, Path | None]:
    """Generate daily summary and weekly digest from raw JSON files.

    Returns (daily_path, digest_path) or (None, None) if no data found.
    """
    week_dir = DATA_DIR / str(year) / f"week-{week_num:02d}"
    if not week_dir.exists():
        logger.warning("Week directory not found: %s", week_dir)
        return None, None

    # Find all raw JSON files
    raw_files = sorted(week_dir.glob("*-raw.json"))
    if not raw_files:
        logger.warning("No raw JSON files in %s", week_dir)
        return None, None

    all_articles: list[dict] = []
    daily_path: Path | None = None

    for raw_file in raw_files:
        articles = _load_raw_articles(raw_file)
        if not articles:
            continue

        all_articles.extend(articles)

        # Generate daily summary for each raw file
        # Extract date from JSON content
        data = json.loads(raw_file.read_text(encoding="utf-8"))
        date_str = data.get("date", "unknown")
        daily_md = _format_daily_md(articles, date_str)

        # Determine day name from the filename (e.g., "thursday-raw.json")
        day_name = raw_file.stem.replace("-raw", "")
        daily_out = week_dir / f"{day_name}.md"
        daily_out.write_text(daily_md, encoding="utf-8")
        daily_path = daily_out
        logger.info("Generated daily summary: %s (%d articles)", daily_out, len(articles))

    # Generate weekly digest from all articles
    if all_articles:
        monday = datetime.fromisocalendar(year, week_num, 1)
        sunday = monday + __import__("datetime").timedelta(days=6)
        label = f"Week {week_num}: {monday.strftime('%b %d')} - {sunday.strftime('%b %d, %Y')}"
        digest_md = _format_weekly_digest_md(all_articles, label)
        digest_path = week_dir / "weekly-digest.md"
        digest_path.write_text(digest_md, encoding="utf-8")
        logger.info("Generated weekly digest: %s (%d total articles)", digest_path, len(all_articles))
        return daily_path, digest_path

    return daily_path, None
