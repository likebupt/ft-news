"""Static site generator - builds HTML pages from markdown digests."""

from __future__ import annotations

import json
import logging
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring

from config import DATA_DIR, SITE_BASE_PATH

logger = logging.getLogger(__name__)

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
SITE_DIR = Path(__file__).resolve().parent / "_site"
SITE_TITLE = "FT News Weekly"


# ---------------------------------------------------------------------------
# Template engine (minimal, no dependencies)
# ---------------------------------------------------------------------------

def _render(template_name: str, **kwargs: str) -> str:
    """Render a template with simple {{ var }} substitution."""
    tmpl = (TEMPLATES_DIR / template_name).read_text(encoding="utf-8")
    # Inject base path into all absolute href/src paths
    base = SITE_BASE_PATH.rstrip("/")
    tmpl = tmpl.replace('href="/', f'href="{base}/')
    tmpl = tmpl.replace('src="/', f'src="{base}/')
    for key, value in kwargs.items():
        tmpl = tmpl.replace("{{ " + key + " }}", value)
        # Handle Jinja-style conditionals simply via class replacement
        tmpl = tmpl.replace(
            "{{ 'active' if page == '" + key + "' else '' }}",
            "active" if kwargs.get("page") == key else "",
        )
    # Clean up any remaining conditional templates
    tmpl = re.sub(r"\{\{[^}]+\}\}", "", tmpl)
    return tmpl


# ---------------------------------------------------------------------------
# Markdown to HTML conversion
# ---------------------------------------------------------------------------

def _md_to_html(md: str) -> str:
    """Convert digest markdown to HTML content (inner, no full page)."""
    lines = md.strip().split("\n")
    html: list[str] = []
    in_list = False

    for line in lines:
        s = line.strip()
        if not s:
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append("<br>")
            continue

        # Convert markdown links
        s = re.sub(
            r"\[([^\]]+)\]\((https?://[^)]+)\)",
            r'<a href="\2">\1</a>',
            s,
        )
        # Convert **bold**
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        # Convert *italic*
        s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)

        if s.startswith("# "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h2>{s[2:]}</h2>")
        elif s.startswith("## "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h2>{s[3:]}</h2>")
        elif s.startswith("### "):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h3>{s[4:]}</h3>")
        elif s in ("---", "***", "___"):
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append("<hr>")
        elif s.startswith(("- ", "* ", "• ")):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{s[2:]}</li>")
        elif re.match(r"^\d+\.\s", s):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{s}</li>")
        else:
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<p>{s}</p>")

    if in_list:
        html.append("</ul>")

    return "\n".join(html)


# ---------------------------------------------------------------------------
# Week discovery
# ---------------------------------------------------------------------------

def _discover_weeks() -> list[dict]:
    """Find all weeks with data, return sorted list (newest first)."""
    weeks: list[dict] = []
    if not DATA_DIR.exists():
        return weeks

    for year_dir in sorted(DATA_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for week_dir in sorted(year_dir.iterdir(), reverse=True):
            if not week_dir.is_dir() or not week_dir.name.startswith("week-"):
                continue
            week_num = int(week_dir.name.split("-")[1])
            year = int(year_dir.name)

            # Calculate date range
            monday = datetime.fromisocalendar(year, week_num, 1)
            sunday = monday + timedelta(days=6)

            digest_file = week_dir / "weekly-digest.md"
            daily_files = sorted(week_dir.glob("*.md"))
            daily_files = [f for f in daily_files if f.name != "weekly-digest.md"]

            weeks.append({
                "year": year,
                "week_num": week_num,
                "label": f"Week {week_num}",
                "date_range": f"{monday.strftime('%b %d')} – {sunday.strftime('%b %d, %Y')}",
                "dir": week_dir,
                "has_digest": digest_file.exists(),
                "digest_file": digest_file,
                "daily_files": daily_files,
                "slug": f"{year}/week-{week_num:02d}",
            })

    return weeks


def _discover_daily(week: dict) -> list[dict]:
    """Get daily summaries for a week."""
    days = []
    day_order = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for day_name in day_order:
        md_file = week["dir"] / f"{day_name}.md"
        raw_file = week["dir"] / f"{day_name}-raw.json"
        if md_file.exists():
            article_count = 0
            if raw_file.exists():
                try:
                    raw = json.loads(raw_file.read_text(encoding="utf-8"))
                    article_count = raw.get("article_count", 0)
                except Exception:
                    pass
            days.append({
                "name": day_name,
                "label": day_name.capitalize(),
                "file": md_file,
                "article_count": article_count,
            })
    return days


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------

def _build_week_page(week: dict, prev_week: dict | None, next_week: dict | None) -> str:
    """Build the HTML page for a single week."""
    # Week navigation
    base = SITE_BASE_PATH.rstrip("/")
    nav_html = '<div class="week-nav">'
    if next_week:
        nav_html += f'<a href="{base}/{next_week["slug"]}/index.html">← {next_week["label"]}</a>'
    nav_html += f'<a href="{base}/archive.html">All Weeks</a>'
    if prev_week:
        nav_html += f'<a href="{base}/{prev_week["slug"]}/index.html">{prev_week["label"]} →</a>'
    nav_html += "</div>"

    # Day tabs
    days = _discover_daily(week)
    day_tabs = ""
    if days:
        day_tabs = '<div class="day-tabs">'
        for d in days:
            count_badge = f" ({d['article_count']})" if d["article_count"] else ""
            day_tabs += (
                f'<a class="day-tab" href="{base}/{week["slug"]}/{d["name"]}.html">'
                f'{d["label"]}{count_badge}</a>'
            )
        day_tabs += "</div>"

    # Digest content
    if week["has_digest"]:
        digest_md = week["digest_file"].read_text(encoding="utf-8")
        digest_html = _md_to_html(digest_md)
    else:
        digest_html = (
            '<div class="tldr"><strong>No weekly digest yet.</strong> '
            "Daily summaries are being collected. Check back on Monday.</div>"
        )

    content = f"""
    <div class="week-header">
        <h1>{week['label']}: Weekly Digest</h1>
        <div class="date-range">{week['date_range']}</div>
        {nav_html}
    </div>
    {day_tabs}
    <div class="card">
        {digest_html}
    </div>
    """

    return _render("base.html", title=week["label"], page="home", content=content)


def _build_day_page(week: dict, day: dict) -> str:
    """Build the HTML page for a single day."""
    md = day["file"].read_text(encoding="utf-8")
    html_content = _md_to_html(md)

    # Other day tabs
    base = SITE_BASE_PATH.rstrip("/")
    days = _discover_daily(week)
    day_tabs = '<div class="day-tabs">'
    for d in days:
        active = "active" if d["name"] == day["name"] else ""
        day_tabs += (
            f'<a class="day-tab {active}" href="{base}/{week["slug"]}/{d["name"]}.html">'
            f'{d["label"]}</a>'
        )
    day_tabs += "</div>"

    content = f"""
    <div class="week-header">
        <h1>{day['label']}'s Finetuning News</h1>
        <div class="date-range">{week['label']} \u00b7 {week['date_range']}</div>
        <div class="week-nav">
            <a href="{base}/{week['slug']}/index.html">\u2190 Back to Weekly Digest</a>
        </div>
    </div>
    {day_tabs}
    <div class="card">
        {html_content}
    </div>
    """

    title = f"{day['label']} - {week['label']}"
    return _render("base.html", title=title, page="daily", content=content)


def _build_archive_page(weeks: list[dict]) -> str:
    """Build the archive listing page."""
    items = ""
    base = SITE_BASE_PATH.rstrip("/")
    for w in weeks:
        status = "\U0001f4ca Digest available" if w["has_digest"] else "\U0001f4dd In progress"
        daily_count = len(w["daily_files"])
        items += (
            f'<li><a href="{base}/{w["slug"]}/index.html">{w["label"]}: '
            f'{w["date_range"]}</a>'
            f'<div class="date">{status} · {daily_count} daily summaries</div></li>'
        )

    content = f"""
    <div class="week-header">
        <h1>Archive</h1>
        <div class="date-range">All weekly digests</div>
    </div>
    <div class="card">
        <ul class="archive-list">
            {items if items else '<li>No digests yet. Data will appear after the first daily fetch.</li>'}
        </ul>
    </div>
    """

    return _render("base.html", title="Archive", page="archive", content=content)


def _build_rss(weeks: list[dict]) -> str:
    """Build an RSS 2.0 feed XML string."""
    base = SITE_BASE_PATH.rstrip("/")
    rss = Element("rss", version="2.0")
    channel = SubElement(rss, "channel")
    SubElement(channel, "title").text = SITE_TITLE
    SubElement(channel, "link").text = base or "/"
    SubElement(channel, "description").text = (
        "Weekly finetuning & post-training news for the Microsoft Foundry team."
    )

    for w in weeks[:20]:  # Last 20 weeks
        if not w["has_digest"]:
            continue
        item = SubElement(channel, "item")
        SubElement(item, "title").text = f"{w['label']}: {w['date_range']}"
        link = f"{base}/{w['slug']}/index.html"
        SubElement(item, "link").text = link
        SubElement(item, "guid").text = link

        digest_text = w["digest_file"].read_text(encoding="utf-8")
        SubElement(item, "description").text = digest_text[:2000]

    xml_bytes = tostring(rss, encoding="unicode", xml_declaration=False)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_bytes


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def build_site() -> Path:
    """Generate the full static site into _site/."""
    logger.info("Building static site...")

    # Clean output
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    weeks = _discover_weeks()

    if not weeks:
        # Build a placeholder homepage
        content = """
        <div class="week-header">
            <h1>Welcome to FT News Weekly</h1>
            <div class="date-range">Finetuning & Post-Training Intelligence</div>
        </div>
        <div class="card">
            <p>No data yet. The first daily fetch will populate this site.</p>
            <p>Run <code>python main.py fetch</code> to get started.</p>
        </div>
        """
        index_html = _render("base.html", title="Home", page="home", content=content)
        (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")
        logger.info("Built placeholder site (no data yet)")
        return SITE_DIR

    # Homepage = latest week
    latest = weeks[0]

    for i, week in enumerate(weeks):
        prev_week = weeks[i - 1] if i > 0 else None
        next_week = weeks[i + 1] if i < len(weeks) - 1 else None

        week_out = SITE_DIR / week["slug"]
        week_out.mkdir(parents=True, exist_ok=True)

        # Week index page
        page_html = _build_week_page(week, prev_week, next_week)
        (week_out / "index.html").write_text(page_html, encoding="utf-8")

        # Daily pages
        for day in _discover_daily(week):
            day_html = _build_day_page(week, day)
            (week_out / f"{day['name']}.html").write_text(day_html, encoding="utf-8")

    # Homepage redirect to latest week
    index_html = _build_week_page(latest, None, weeks[1] if len(weeks) > 1 else None)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Archive page
    archive_html = _build_archive_page(weeks)
    (SITE_DIR / "archive.html").write_text(archive_html, encoding="utf-8")

    # RSS feed
    rss_xml = _build_rss(weeks)
    (SITE_DIR / "feed.xml").write_text(rss_xml, encoding="utf-8")

    # .nojekyll for GitHub Pages
    (SITE_DIR / ".nojekyll").write_text("", encoding="utf-8")

    total_pages = sum(2 + len(_discover_daily(w)) for w in weeks)
    logger.info("Built %d pages for %d weeks → %s", total_pages, len(weeks), SITE_DIR)
    return SITE_DIR
