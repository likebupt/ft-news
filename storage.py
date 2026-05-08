"""Persistent storage layer using SQLite.

Stores articles in a local database with full deduplication, time-window
queries, and summary caching.  Replaces the old JSON-file-per-day approach
for the hot path while keeping JSON exports for the static site builder.
"""

from __future__ import annotations

import json
import logging
import sqlite3
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

from config import DATA_DIR

logger = logging.getLogger(__name__)

DB_PATH = DATA_DIR / "ft_news.db"

# ---------------------------------------------------------------------------
# Data models (kept compatible with the old Article for migration ease)
# ---------------------------------------------------------------------------

@dataclass
class ArticleRow:
    """A single article stored in the database."""

    id: int | None  # auto-increment PK
    url: str
    title: str
    source_name: str
    category: str
    published: str  # ISO-8601
    summary: str  # feed excerpt
    relevance_score: float
    fetched_at: str  # ISO-8601 when we first saw it
    batch_id: str  # groups articles from the same ingestion run

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class SummaryRow:
    """A cached LLM summary (daily chunk or weekly digest)."""

    id: int | None
    kind: str  # "daily_chunk", "daily_merged", "weekly"
    scope_key: str  # e.g. "2026-W18" or "2026-W18-chunk-0"
    content: str  # markdown
    article_ids: str  # JSON list of article IDs summarised
    created_at: str


# ---------------------------------------------------------------------------
# Database lifecycle
# ---------------------------------------------------------------------------

@contextmanager
def _connect() -> Iterator[sqlite3.Connection]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), timeout=30)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db() -> None:
    """Create tables if they don't exist."""
    with _connect() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS articles (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            url           TEXT    NOT NULL UNIQUE,
            title         TEXT    NOT NULL,
            source_name   TEXT    NOT NULL,
            category      TEXT    NOT NULL DEFAULT '',
            published     TEXT    NOT NULL,
            summary       TEXT    NOT NULL DEFAULT '',
            relevance_score REAL  NOT NULL DEFAULT 0.0,
            fetched_at    TEXT    NOT NULL,
            batch_id      TEXT    NOT NULL DEFAULT ''
        );

        CREATE INDEX IF NOT EXISTS idx_articles_published
            ON articles(published);
        CREATE INDEX IF NOT EXISTS idx_articles_source
            ON articles(source_name);
        CREATE INDEX IF NOT EXISTS idx_articles_batch
            ON articles(batch_id);

        CREATE TABLE IF NOT EXISTS summaries (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            kind        TEXT    NOT NULL,
            scope_key   TEXT    NOT NULL,
            content     TEXT    NOT NULL,
            article_ids TEXT    NOT NULL DEFAULT '[]',
            created_at  TEXT    NOT NULL,
            UNIQUE(kind, scope_key)
        );
        """)
    logger.info("Database initialised at %s", DB_PATH)


# ---------------------------------------------------------------------------
# Article operations
# ---------------------------------------------------------------------------

def insert_articles(articles: list[dict], batch_id: str) -> int:
    """Bulk-insert articles, skipping duplicates by URL. Returns count inserted."""
    now = datetime.now(timezone.utc).isoformat()
    inserted = 0
    with _connect() as conn:
        for a in articles:
            try:
                conn.execute(
                    """INSERT OR IGNORE INTO articles
                       (url, title, source_name, category, published,
                        summary, relevance_score, fetched_at, batch_id)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        a["url"],
                        a.get("title", ""),
                        a.get("source_name", ""),
                        a.get("category", ""),
                        a.get("published", now),
                        a.get("summary", "")[:2000],
                        a.get("relevance_score", 0.0),
                        now,
                        batch_id,
                    ),
                )
                if conn.total_changes:
                    inserted += 1
            except sqlite3.IntegrityError:
                pass  # duplicate URL
    logger.info("Inserted %d/%d articles (batch %s)", inserted, len(articles), batch_id)
    return inserted


def query_articles(
    *,
    since: str | None = None,
    until: str | None = None,
    min_relevance: float = 0.0,
    source: str | None = None,
    limit: int = 5000,
) -> list[dict]:
    """Query articles with filters. Returns list of dicts."""
    clauses: list[str] = []
    params: list = []
    if since:
        clauses.append("published >= ?")
        params.append(since)
    if until:
        clauses.append("published <= ?")
        params.append(until)
    if min_relevance > 0:
        clauses.append("relevance_score >= ?")
        params.append(min_relevance)
    if source:
        clauses.append("source_name = ?")
        params.append(source)

    where = (" WHERE " + " AND ".join(clauses)) if clauses else ""
    sql = f"SELECT * FROM articles{where} ORDER BY relevance_score DESC, published DESC LIMIT ?"
    params.append(limit)

    with _connect() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


def article_count() -> int:
    with _connect() as conn:
        return conn.execute("SELECT COUNT(*) FROM articles").fetchone()[0]


def url_exists(url: str) -> bool:
    with _connect() as conn:
        row = conn.execute("SELECT 1 FROM articles WHERE url = ?", (url,)).fetchone()
        return row is not None


def get_existing_urls(urls: list[str]) -> set[str]:
    """Return the subset of *urls* that already exist in the DB."""
    if not urls:
        return set()
    with _connect() as conn:
        placeholders = ",".join("?" for _ in urls)
        rows = conn.execute(
            f"SELECT url FROM articles WHERE url IN ({placeholders})", urls
        ).fetchall()
    return {r["url"] for r in rows}


# ---------------------------------------------------------------------------
# Summary cache operations
# ---------------------------------------------------------------------------

def save_summary(kind: str, scope_key: str, content: str, article_ids: list[int] | None = None) -> None:
    """Upsert a summary."""
    now = datetime.now(timezone.utc).isoformat()
    ids_json = json.dumps(article_ids or [])
    with _connect() as conn:
        conn.execute(
            """INSERT INTO summaries (kind, scope_key, content, article_ids, created_at)
               VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(kind, scope_key) DO UPDATE SET
                   content = excluded.content,
                   article_ids = excluded.article_ids,
                   created_at = excluded.created_at""",
            (kind, scope_key, content, ids_json, now),
        )
    logger.info("Saved summary kind=%s scope=%s (%d chars)", kind, scope_key, len(content))


def get_summary(kind: str, scope_key: str) -> str | None:
    """Return cached summary content or None."""
    with _connect() as conn:
        row = conn.execute(
            "SELECT content FROM summaries WHERE kind = ? AND scope_key = ?",
            (kind, scope_key),
        ).fetchone()
    return row["content"] if row else None


def list_summaries(kind: str) -> list[dict]:
    """List all summaries of a given kind."""
    with _connect() as conn:
        rows = conn.execute(
            "SELECT * FROM summaries WHERE kind = ? ORDER BY created_at DESC", (kind,)
        ).fetchall()
    return [dict(r) for r in rows]


# ---------------------------------------------------------------------------
# Migration helpers
# ---------------------------------------------------------------------------

def import_from_json(json_path: Path, batch_id: str | None = None) -> int:
    """Import articles from a legacy *-raw.json file into the DB."""
    data = json.loads(json_path.read_text(encoding="utf-8"))
    articles = data.get("articles", [])
    bid = batch_id or json_path.stem
    return insert_articles(articles, bid)


def migrate_all_json() -> int:
    """Scan data/ for all *-raw.json files and import them."""
    init_db()
    total = 0
    for jf in sorted(DATA_DIR.rglob("*-raw.json")):
        n = import_from_json(jf)
        total += n
        logger.info("Migrated %s → %d new articles", jf.name, n)
    logger.info("Migration complete: %d total new articles", total)
    return total
