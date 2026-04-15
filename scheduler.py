"""Scheduler - runs daily fetch and weekly digest on a cron schedule."""

from __future__ import annotations

import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from config import (
    DAILY_FETCH_HOUR,
    DAILY_FETCH_MINUTE,
    LOG_LEVEL,
    WEEKLY_PUSH_HOUR,
    WEEKLY_PUSH_MINUTE,
)

logger = logging.getLogger(__name__)


def _run_daily_job() -> None:
    """Fetch news and create daily summary."""
    from fetcher import fetch_daily, save_daily_result
    from summarizer import save_daily_summary, summarize_daily

    logger.info("=== Starting daily fetch job ===")
    result = fetch_daily()
    save_daily_result(result)

    if result.articles:
        summary = summarize_daily(result)
        save_daily_summary(summary, result.date)
    else:
        logger.info("No relevant articles found today, skipping summarization.")

    logger.info("=== Daily fetch job complete ===")


def _run_weekly_job() -> None:
    """Generate weekly digest and push to Teams."""
    from digest import generate_weekly_digest
    from publisher import send_to_teams

    logger.info("=== Starting weekly digest job ===")
    digest, path = generate_weekly_digest()

    if digest.strip():
        success = send_to_teams(digest)
        if success:
            logger.info("Weekly digest sent to Teams successfully.")
        else:
            logger.error("Failed to send weekly digest to Teams.")
    else:
        logger.warning("Empty digest, skipping Teams push.")

    logger.info("=== Weekly digest job complete ===")


def start_scheduler() -> None:
    """Start the APScheduler with daily and weekly jobs."""
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    scheduler = BlockingScheduler(timezone="US/Pacific")

    # Daily job: fetch + summarize (every day at configured time, PST)
    scheduler.add_job(
        _run_daily_job,
        CronTrigger(
            hour=DAILY_FETCH_HOUR,
            minute=DAILY_FETCH_MINUTE,
            timezone="US/Pacific",
        ),
        id="daily_fetch",
        name="Daily Finetuning News Fetch",
        misfire_grace_time=3600,
    )

    # Weekly job: digest + push (every Monday at configured time, PST)
    scheduler.add_job(
        _run_weekly_job,
        CronTrigger(
            day_of_week="mon",
            hour=WEEKLY_PUSH_HOUR,
            minute=WEEKLY_PUSH_MINUTE,
            timezone="US/Pacific",
        ),
        id="weekly_digest",
        name="Weekly Digest & Teams Push",
        misfire_grace_time=3600,
    )

    logger.info(
        "Scheduler started. Daily fetch at %02d:%02d PST, "
        "Weekly digest at Monday %02d:%02d PST.",
        DAILY_FETCH_HOUR, DAILY_FETCH_MINUTE,
        WEEKLY_PUSH_HOUR, WEEKLY_PUSH_MINUTE,
    )
    logger.info("Press Ctrl+C to stop.")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")
