"""FT News Weekly - CLI entry point.

Architecture (v2 — decoupled pipeline):

  OFFLINE (background / cron):
    ingest   → async fetch all RSS feeds → store in SQLite
    migrate  → import legacy JSON files into the DB

  ONLINE (fast query path):
    digest   → map-reduce summarisation from DB (cached)
    daily    → daily summary from DB (cached)

  SITE:
    build    → static site from data/ markdown files

  LEGACY (still available):
    fetch       → old sync fetch + single-pass LLM
    fetch-only  → old sync fetch, no LLM
"""

from __future__ import annotations

import logging
import sys
from datetime import datetime, timedelta, timezone

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


# ===================================================================
# NEW PIPELINE commands
# ===================================================================

@cli.command()
def ingest() -> None:
    """Fetch all RSS feeds asynchronously and store in the database."""
    from ingestion import run_ingestion

    click.echo("Starting async ingestion...")
    stats = run_ingestion()
    click.echo(f"Done!  batch={stats['batch_id']}")
    click.echo(f"  Sources OK : {stats['sources_ok']}/{stats['sources_total']}")
    click.echo(f"  Relevant   : {stats['relevant_found']}")
    click.echo(f"  New articles: {stats['inserted']}")
    click.echo(f"  Duplicates : {stats['duplicates_skipped']}")
    if stats["errors"]:
        click.echo(f"  Errors ({len(stats['errors'])}):")
        for e in stats["errors"]:
            click.echo(f"    - {e}")


@cli.command()
def migrate() -> None:
    """Import all legacy *-raw.json files into the SQLite database."""
    from storage import migrate_all_json

    click.echo("Migrating JSON data to SQLite...")
    total = migrate_all_json()
    click.echo(f"Migrated {total} new articles into the database.")


@cli.command("db-stats")
def db_stats() -> None:
    """Show database statistics."""
    from query import stats as get_stats

    s = get_stats()
    click.echo("Database statistics:")
    click.echo(f"  Articles       : {s['total_articles']}")
    click.echo(f"  Weekly digests : {s['weekly_digests']}")
    click.echo(f"  Daily digests  : {s['daily_digests']}")
    click.echo(f"  Cached chunks  : {s['cached_chunks']}")


@cli.command()
@click.option("--week", default=None, type=int, help="ISO week number (default: previous week)")
@click.option("--year", default=None, type=int, help="ISO year (default: current)")
@click.option("--force", is_flag=True, help="Ignore cache and re-summarise")
@click.option("--max-articles", default=200, type=int, help="Max articles for summarisation")
@click.option("--chunk-size", default=15, type=int, help="Articles per map chunk")
def digest(week: int | None, year: int | None, force: bool, max_articles: int, chunk_size: int) -> None:
    """Generate the weekly digest using map-reduce summarisation."""
    from query import weekly_digest

    click.echo("Generating weekly digest (map-reduce)...")
    text = weekly_digest(
        year=year, week=week, force=force,
        max_articles=max_articles, chunk_size=chunk_size,
    )
    click.echo("\n" + "=" * 60)
    click.echo(text[:3000] if len(text) > 3000 else text)
    if len(text) > 3000:
        click.echo(f"\n... ({len(text)} chars total, see data/ for full output)")


@cli.command()
@click.option("--date", default=None, help="Date in YYYY-MM-DD format (default: today)")
@click.option("--force", is_flag=True, help="Ignore cache and re-summarise")
def daily(date: str | None, force: bool) -> None:
    """Generate a daily summary using map-reduce summarisation."""
    from query import daily_digest

    click.echo("Generating daily digest (map-reduce)...")
    text = daily_digest(date_str=date, force=force)
    click.echo("\n" + "=" * 60)
    click.echo(text[:3000] if len(text) > 3000 else text)


@cli.command()
def pipeline() -> None:
    """Run the full daily pipeline: ingest → daily summary → build site."""
    from ingestion import run_ingestion
    from query import daily_digest
    from site_builder import build_site

    # Step 1: Ingest
    click.echo("[1/3] Ingesting articles...")
    stats = run_ingestion()
    click.echo(f"  → {stats['inserted']} new articles from {stats['sources_ok']} sources")

    # Step 2: Summarise today
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    click.echo(f"[2/3] Summarising {today}...")
    text = daily_digest(date_str=today)
    click.echo(f"  → {len(text)} chars generated")

    # Step 3: Build site
    click.echo("[3/3] Building site...")
    out = build_site()
    click.echo(f"  → {out}")
    click.echo("Pipeline complete!")


@cli.command("weekly-pipeline")
def weekly_pipeline() -> None:
    """Run the full weekly pipeline: digest → build site."""
    from query import weekly_digest
    from site_builder import build_site

    click.echo("[1/2] Generating weekly digest (map-reduce)...")
    text = weekly_digest()
    click.echo(f"  → {len(text)} chars generated")

    click.echo("[2/2] Building site...")
    out = build_site()
    click.echo(f"  → {out}")
    click.echo("Weekly pipeline complete!")


# ===================================================================
# LEGACY commands (kept for backward compatibility)
# ===================================================================

@cli.command("legacy-fetch")
def legacy_fetch() -> None:
    """[Legacy] Sync fetch + single-pass LLM summarise."""
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


@cli.command("legacy-fetch-only")
def legacy_fetch_only() -> None:
    """[Legacy] Fetch articles without LLM summarization."""
    from fetcher import fetch_daily, save_daily_result

    click.echo("Fetching finetuning news (no summarization)...")
    result = fetch_daily()
    raw_path = save_daily_result(result)
    click.echo(f"Found {len(result.articles)} relevant articles.")
    click.echo(f"Raw data saved to: {raw_path}")

    for a in result.articles:
        click.echo(f"  [{a.source_name}] {a.title}")
        click.echo(f"    {a.url}")


# ===================================================================
# SHARED commands
# ===================================================================

@cli.command()
@click.option(
    "--date",
    default=None,
    help="Reference date to find the digest (ISO format). Defaults to today.",
)
def push(date: str | None) -> None:
    """Send the latest weekly digest via email."""
    from config import DATA_DIR
    from publisher import send_email

    ref = datetime.fromisoformat(date).replace(tzinfo=timezone.utc) if date else datetime.now(timezone.utc)

    last_week = ref - timedelta(weeks=1)
    iso_year, iso_week, _ = last_week.isocalendar()
    digest_path = DATA_DIR / str(iso_year) / f"week-{iso_week:02d}" / "weekly-digest.md"

    if not digest_path.exists():
        click.echo(f"No digest found at {digest_path}. Run 'digest' first.")
        sys.exit(1)

    digest_text = digest_path.read_text(encoding="utf-8")
    click.echo("Sending weekly digest email...")
    success = send_email(digest_text)

    if success:
        click.echo("Email sent successfully!")
    else:
        click.echo("Failed to send email. Check logs for details.")
        sys.exit(1)


@cli.command()
def build() -> None:
    """Build the static website from collected data."""
    from site_builder import build_site

    click.echo("Building static site...")
    out = build_site()
    click.echo(f"Site built → {out}")


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
