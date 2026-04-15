"""FT News Weekly - CLI entry point.

Usage:
    python main.py run          # Start the scheduler (daily + weekly jobs)
    python main.py fetch        # Manually run a daily fetch + summarize
    python main.py digest       # Manually generate this week's digest
    python main.py push         # Manually push the latest digest to Teams
    python main.py fetch-only   # Fetch without summarizing (for testing)
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime, timezone

import click

from config import LOG_LEVEL


def _setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


@click.group()
def cli() -> None:
    """FT News Weekly - Finetuning & Post-Training News Agent."""
    _setup_logging()


@cli.command()
def run() -> None:
    """Start the scheduler (runs daily fetch + weekly digest automatically)."""
    from scheduler import start_scheduler

    click.echo("Starting FT News Weekly scheduler...")
    start_scheduler()


@cli.command()
def fetch() -> None:
    """Manually run a daily fetch + summarize."""
    from fetcher import fetch_daily, save_daily_result
    from summarizer import save_daily_summary, summarize_daily

    click.echo("Fetching finetuning news from all sources...")
    result = fetch_daily()
    raw_path = save_daily_result(result)
    click.echo(f"Found {len(result.articles)} relevant articles.")
    click.echo(f"Raw data saved to: {raw_path}")

    if result.errors:
        click.echo(f"Errors: {len(result.errors)}")
        for err in result.errors:
            click.echo(f"  - {err}")

    if result.articles:
        click.echo("Generating daily summary with LLM...")
        summary = summarize_daily(result)
        summary_path = save_daily_summary(summary, result.date)
        click.echo(f"Summary saved to: {summary_path}")
        click.echo("\n" + "=" * 60)
        click.echo(summary)
    else:
        click.echo("No relevant articles found.")


@cli.command("fetch-only")
def fetch_only() -> None:
    """Fetch articles without LLM summarization (for testing)."""
    from fetcher import fetch_daily, save_daily_result

    click.echo("Fetching finetuning news (no summarization)...")
    result = fetch_daily()
    raw_path = save_daily_result(result)
    click.echo(f"Found {len(result.articles)} relevant articles.")
    click.echo(f"Raw data saved to: {raw_path}")

    for a in result.articles:
        click.echo(f"  [{a.source_name}] {a.title}")
        click.echo(f"    {a.url}")


@cli.command()
@click.option(
    "--date",
    default=None,
    help="Reference date (ISO format, e.g. 2026-04-20). Defaults to today.",
)
def digest(date: str | None) -> None:
    """Generate the weekly digest for the previous week."""
    from digest import generate_weekly_digest

    ref = datetime.fromisoformat(date).replace(tzinfo=timezone.utc) if date else None
    click.echo("Generating weekly digest...")
    digest_text, path = generate_weekly_digest(ref)
    click.echo(f"Digest saved to: {path}")
    click.echo("\n" + "=" * 60)
    click.echo(digest_text)


@cli.command()
@click.option(
    "--date",
    default=None,
    help="Reference date to find the digest (ISO format). Defaults to today.",
)
def push(date: str | None) -> None:
    """Push the latest weekly digest to Teams."""
    from config import DATA_DIR
    from publisher import send_to_teams

    ref = datetime.fromisoformat(date).replace(tzinfo=timezone.utc) if date else datetime.now(timezone.utc)
    from datetime import timedelta

    last_week = ref - timedelta(weeks=1)
    iso_year, iso_week, _ = last_week.isocalendar()
    digest_path = DATA_DIR / str(iso_year) / f"week-{iso_week:02d}" / "weekly-digest.md"

    if not digest_path.exists():
        click.echo(f"No digest found at {digest_path}. Run 'digest' first.")
        sys.exit(1)

    digest_text = digest_path.read_text(encoding="utf-8")
    click.echo("Pushing weekly digest to Teams...")
    success = send_to_teams(digest_text)

    if success:
        click.echo("Successfully sent to Teams!")
    else:
        click.echo("Failed to send to Teams. Check logs for details.")
        sys.exit(1)


@cli.command()
def sources() -> None:
    """List all configured news sources."""
    from sources import SOURCES

    click.echo(f"Configured news sources ({len(SOURCES)}):\n")
    for s in SOURCES:
        click.echo(f"  [{s.category:>10}] {s.name}")
        click.echo(f"              {s.feed_url}")


if __name__ == "__main__":
    cli()
