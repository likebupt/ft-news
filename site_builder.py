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
    """Convert digest markdown to HTML content (inner, no full page).

    Used for daily summaries.  Weekly digests use _digest_to_html().
    """
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
# Inline markdown helpers
# ---------------------------------------------------------------------------

def _inline_md(text: str) -> str:
    """Convert inline markdown (links, bold, italic) to HTML."""
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2">\1</a>',
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


# ---------------------------------------------------------------------------
# Digest-aware rich renderer (weekly digest pages only)
# ---------------------------------------------------------------------------

def _parse_digest_sections(md: str) -> list[dict]:
    """Split weekly digest markdown into sections by ## headings."""
    lines = md.strip().split("\n")
    sections: list[dict] = []
    current: dict = {"title": "", "id": "intro", "lines": []}

    for line in lines:
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            continue  # skip main title
        if s.startswith("## "):
            if current["lines"] or current["title"]:
                sections.append(current)
            title = s[3:].strip()
            sid = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            current = {"title": title, "id": sid, "lines": []}
        else:
            current["lines"].append(line)

    if current["lines"] or current["title"]:
        sections.append(current)
    return sections


def _extract_tldr(sections: list[dict]) -> str:
    """Extract TL;DR text from parsed sections."""
    # Case 1: TL;DR as its own ## section
    for s in sections:
        if s["id"] == "tl-dr" or s["title"].upper().startswith("TL;DR"):
            text = "\n".join(l.strip() for l in s["lines"] if l.strip())
            return text

    # Case 2: Bold **TL;DR** in intro section
    intro = next((s for s in sections if s["id"] == "intro"), None)
    if intro:
        for line in intro["lines"]:
            stripped = line.strip()
            if "TL;DR" in stripped.upper():
                return re.sub(r"^\*?\*?TL;DR\*?\*?\s*[—–\-:]*\s*", "", stripped, flags=re.IGNORECASE)
    return ""


def _extract_companies(sections: list[dict]) -> list[str]:
    """Extract company names from 'By Company' section.

    Handles multiple markdown formats:
    - **Company** (standalone bold line)
    - ### Company (sub-heading)
    - - **Company** — description (bold at start of bullet)
    Skips regional headers like ### North America.
    """
    _REGION_NAMES = {"north america", "asia", "europe", "latin america", "middle east"}
    companies: list[str] = []
    by_company = next((s for s in sections if "company" in s["title"].lower()), None)
    if not by_company:
        return companies
    for line in by_company["lines"]:
        s = line.strip()
        # Format: **Company** (standalone)
        m = re.match(r"^\*\*(.+?)\*\*\s*$", s)
        if m:
            companies.append(m.group(1))
            continue
        # Format: ### Company (heading)
        m = re.match(r"^###\s+(.+)$", s)
        if m and m.group(1).strip().lower() not in _REGION_NAMES:
            companies.append(m.group(1).strip())
            continue
        # Format: - **Company** — description
        m = re.match(r"^-\s+\*\*(.+?)\*\*\s*[—–\-:]", s)
        if m:
            companies.append(m.group(1))
    return companies


def _count_digest_stats(lines: list[str], sections: list[dict]) -> dict:
    """Count items, companies, papers from the digest markdown."""
    total_items = sum(1 for l in lines if l.strip().startswith("- "))
    paper_sec = next((s for s in sections if "paper" in s["title"].lower()), None)
    paper_count = 0
    if paper_sec:
        paper_count = sum(1 for l in paper_sec["lines"] if l.strip().startswith("- "))
    companies = _extract_companies(sections)
    return {"items": total_items, "companies": len(companies), "papers": paper_count}


def _render_top_stories_html(lines: list[str]) -> str:
    """Render Top Stories section as styled cards."""
    cards: list[str] = []
    for line in lines:
        s = line.strip()
        if not s.startswith("- "):
            continue
        bullet = s[2:]
        # Try to extract a tag from **Bold**: rest
        tag_html = ""
        m = re.match(r"\*\*(.+?)\*\*\s*[:：]\s*(.*)", bullet)
        if m:
            tag_html = f'<span class="story-tag">{m.group(1)}</span>'
            rest = m.group(2)
        else:
            rest = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", bullet)
        rest_html = _inline_md(rest)
        cards.append(
            f'<div class="story-card">{tag_html}<p>{rest_html}</p></div>'
        )
    return "\n".join(cards)


def _render_implications_html(lines: list[str]) -> str:
    """Render 'What This Means for Us' section as amber callout items."""
    items = [f"<li>{_inline_md(l.strip()[2:])}</li>" for l in lines if l.strip().startswith("- ")]
    return "<ul>" + "\n".join(items) + "</ul>" if items else ""


def _render_company_section_html(lines: list[str]) -> str:
    """Render 'By Company' section with anchor IDs on each company heading.

    Handles:
    - **Company** (standalone) → h3 heading
    - ### Region or ### Company → h3 heading (regions get a different style)
    - - **Company** — desc → individual company card
    - - bullet → list item under current heading
    """
    _REGION_NAMES = {"north america", "asia", "europe", "latin america", "middle east"}
    html_parts: list[str] = []
    current_heading = ""
    current_items: list[str] = []

    def _flush() -> None:
        if current_heading and current_items:
            cid = re.sub(r"[^a-z0-9]+", "-", current_heading.lower()).strip("-")
            html_parts.append(f'<h3 class="section-anchor" id="{cid}">{current_heading}</h3>')
            html_parts.append("<ul>" + "\n".join(current_items) + "</ul>")
        elif current_items:  # items without heading
            html_parts.append("<ul>" + "\n".join(current_items) + "</ul>")

    for line in lines:
        s = line.strip()
        if not s:
            continue
        # ### Heading
        m = re.match(r"^###\s+(.+)$", s)
        if m:
            _flush()
            current_heading = m.group(1).strip()
            current_items = []
            continue
        # **Company** standalone
        m = re.match(r"^\*\*(.+?)\*\*\s*$", s)
        if m:
            _flush()
            current_heading = m.group(1)
            current_items = []
            continue
        # Bullet item (including - **Company** — desc format)
        if s.startswith("- "):
            current_items.append(f"<li>{_inline_md(s[2:])}</li>")

    _flush()
    return "\n".join(html_parts)


def _render_generic_section_html(lines: list[str]) -> str:
    """Render a section with sub-headings and bullet lists."""
    html: list[str] = []
    in_list = False
    for line in lines:
        s = line.strip()
        if not s:
            if in_list:
                html.append("</ul>")
                in_list = False
            continue
        m = re.match(r"^\*\*(.+?)\*\*\s*$", s)
        if m:
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<h3>{m.group(1)}</h3>")
        elif s.startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{_inline_md(s[2:])}</li>")
        else:
            if in_list:
                html.append("</ul>")
                in_list = False
            html.append(f"<p>{_inline_md(s)}</p>")
    if in_list:
        html.append("</ul>")
    return "\n".join(html)


def _digest_to_html(md: str) -> str:
    """Convert weekly digest markdown to enhanced HTML with rich UX components.

    Produces: stats bar, company tag bar, TOC, hero TL;DR,
    top-stories cards, company sections with anchors,
    and amber implications callout.
    """
    lines = md.strip().split("\n")
    sections = _parse_digest_sections(md)
    tldr_text = _extract_tldr(sections)
    companies = _extract_companies(sections)
    stats = _count_digest_stats(lines, sections)

    parts: list[str] = []

    # ── Stats bar ──
    parts.append(
        f'<div class="stats-bar">'
        f'<div class="stat"><span class="stat-num">{stats["items"]}</span> items covered</div>'
        f'<div class="stat"><span class="stat-num">{stats["companies"]}</span> companies</div>'
        f'<div class="stat"><span class="stat-num">{stats["papers"]}</span> papers</div>'
        f"</div>"
    )

    # ── Company tag bar ──
    if companies:
        pills = "".join(
            f'<a class="company-pill" href="#{re.sub(r"[^a-z0-9]+", "-", c.lower()).strip("-")}">{c}</a>'
            for c in companies
        )
        parts.append(f'<div class="company-bar">{pills}</div>')

    # ── Table of contents ──
    toc_entries: list[tuple[str, str]] = []
    if tldr_text:
        toc_entries.append(("tldr", "TL;DR"))
    for s in sections:
        if s["id"] not in ("intro", "tl-dr") and s["title"]:
            toc_entries.append((s["id"], s["title"]))
    if toc_entries:
        links = '<span class="toc-sep">·</span>'.join(
            f'<a href="#{tid}">{label}</a>' for tid, label in toc_entries
        )
        parts.append(f'<nav class="toc"><span class="toc-label">In This Issue</span>{links}</nav>')

    # ── Hero TL;DR ──
    if tldr_text:
        parts.append(
            f'<div class="hero-tldr" id="tldr"><div class="hero-icon">\U0001f4cc</div>'
            f'<div class="hero-text"><div class="hero-label">TL;DR</div>'
            f"<p>{_inline_md(tldr_text)}</p></div></div>"
        )

    # ── Content sections ──
    for section in sections:
        if section["id"] in ("intro", "tl-dr"):
            continue
        title = section["title"]
        sid = section["id"]
        slines = section["lines"]

        if "top stories" in title.lower():
            cards_html = _render_top_stories_html(slines)
            parts.append(
                f'<div class="section-anchor" id="{sid}">'
                f'<h2>\U0001f525 Top Stories</h2>'
                f'<div class="stories-grid">{cards_html}</div></div>'
            )
        elif "what this means" in title.lower():
            items_html = _render_implications_html(slines)
            parts.append(
                f'<div class="implications section-anchor" id="{sid}">'
                f'<h2>\U0001f4a1 {title}</h2>{items_html}</div>'
            )
        elif "company" in title.lower():
            company_html = _render_company_section_html(slines)
            parts.append(
                f'<div class="card section-anchor" id="{sid}">'
                f"<h2>{title}</h2>{company_html}</div>"
            )
        else:
            content_html = _render_generic_section_html(slines)
            parts.append(
                f'<div class="card section-anchor" id="{sid}">'
                f"<h2>{title}</h2>{content_html}</div>"
            )

    return "\n".join(parts)


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
        digest_html = _digest_to_html(digest_md)
    else:
        digest_html = (
            '<div class="card"><div class="tldr"><strong>No weekly digest yet.</strong> '
            "Daily summaries are being collected. Check back on Monday.</div></div>"
        )

    content = f"""
    <div class="week-header">
        <h1>{week['label']}: Weekly Digest</h1>
        <div class="date-range">{week['date_range']}</div>
        {nav_html}
    </div>
    {day_tabs}
    {digest_html}
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
