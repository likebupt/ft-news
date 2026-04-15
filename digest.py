"""Weekly digest generator - collects daily summaries and produces a weekly report."""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

from config import DATA_DIR
from summarizer import save_weekly_digest, summarize_weekly

logger = logging.getLogger(__name__)


def _get_previous_week_info(
    reference_date: datetime | None = None,
) -> tuple[int, int, str]:
    """Return (iso_year, iso_week, label) for the previous week."""
    ref = reference_date or datetime.now(timezone.utc)
    last_week = ref - timedelta(weeks=1)
    iso_year, iso_week, _ = last_week.isocalendar()
    # Label like "Apr 7 - Apr 13, 2026"
    # Monday of that week
    monday = datetime.fromisocalendar(iso_year, iso_week, 1)
    sunday = monday + timedelta(days=6)
    label = f"Week {iso_week}: {monday.strftime('%b %d')} - {sunday.strftime('%b %d, %Y')}"
    return iso_year, iso_week, label


def collect_daily_summaries(year: int, week_num: int) -> list[str]:
    """Read all daily summary markdown files for a given week."""
    week_dir = DATA_DIR / str(year) / f"week-{week_num:02d}"
    if not week_dir.exists():
        logger.warning("Week directory not found: %s", week_dir)
        return []

    summaries: list[str] = []
    day_order = [
        "monday", "tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday",
    ]

    for day in day_order:
        day_file = week_dir / f"{day}.md"
        if day_file.exists():
            content = day_file.read_text(encoding="utf-8").strip()
            if content:
                summaries.append(content)
                logger.info("Loaded %s summary (%d chars)", day, len(content))

    logger.info(
        "Collected %d daily summaries for week %d of %d",
        len(summaries), week_num, year,
    )
    return summaries


def generate_weekly_digest(
    reference_date: datetime | None = None,
) -> tuple[str, Path]:
    """Generate the weekly digest for the previous week.

    Returns the digest text and the path where it was saved.
    """
    year, week_num, label = _get_previous_week_info(reference_date)
    logger.info("Generating weekly digest for %s", label)

    daily_summaries = collect_daily_summaries(year, week_num)
    digest = summarize_weekly(daily_summaries, label)
    out_path = save_weekly_digest(digest, year, week_num)

    return digest, out_path
