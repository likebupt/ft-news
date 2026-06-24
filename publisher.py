"""Email publisher - sends weekly digest via Azure Logic App HTTP trigger."""

from __future__ import annotations

import logging
import re

import httpx

from config import (
    EMAIL_RECIPIENTS,
    EMAIL_SENDER,
    LOGIC_APP_URL,
)

logger = logging.getLogger(__name__)

_TIMEOUT = httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0)


def _markdown_to_html(markdown: str) -> str:
    """Convert digest markdown to clean HTML for email."""
    lines = markdown.strip().split("\n")
    html_parts: list[str] = []

    html_parts.append(
        '<div style="font-family: Segoe UI, Arial, sans-serif; '
        'max-width: 720px; margin: 0 auto; color: #333;">'
    )

    for line in lines:
        stripped = line.strip()
        if not stripped:
            html_parts.append("<br>")
            continue

        # Convert markdown links [text](url) to HTML <a> tags
        stripped = re.sub(
            r"\[([^\]]+)\]\((https?://[^)]+)\)",
            r'<a href="\2" style="color: #0078D4;">\1</a>',
            stripped,
        )

        # Convert **bold** to <strong>
        stripped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", stripped)

        # Heading 1
        if stripped.startswith("# "):
            text = stripped[2:]
            html_parts.append(
                f'<h1 style="color: #0078D4; border-bottom: 2px solid #0078D4; '
                f'padding-bottom: 6px; margin-top: 24px;">{text}</h1>'
            )
        # Heading 2
        elif stripped.startswith("## "):
            text = stripped[3:]
            html_parts.append(
                f'<h2 style="color: #333; margin-top: 20px; '
                f'margin-bottom: 8px;">{text}</h2>'
            )
        # Heading 3
        elif stripped.startswith("### "):
            text = stripped[4:]
            html_parts.append(
                f'<h3 style="color: #555; margin-top: 16px; '
                f'margin-bottom: 6px;">{text}</h3>'
            )
        # Horizontal rule
        elif stripped in ("---", "***", "___"):
            html_parts.append(
                '<hr style="border: none; border-top: 1px solid #ddd; margin: 16px 0;">'
            )
        # Bullet point
        elif stripped.startswith(("- ", "* ", "• ")):
            bullet_text = stripped[2:]
            html_parts.append(
                f'<div style="padding-left: 16px; margin: 4px 0;">'
                f'&bull; {bullet_text}</div>'
            )
        # Numbered list
        elif re.match(r"^\d+\.\s", stripped):
            html_parts.append(
                f'<div style="padding-left: 16px; margin: 4px 0;">{stripped}</div>'
            )
        # Regular text
        else:
            html_parts.append(f"<p style=\"margin: 6px 0;\">{stripped}</p>")

    html_parts.append("</div>")
    return "\n".join(html_parts)


def send_email(
    digest: str,
    subject: str = "Weekly Finetuning & Post-Training Update",
) -> bool:
    """Send the weekly digest via Azure Logic App HTTP trigger.

    The Logic App should be configured with:
      - HTTP Request trigger (accepts JSON)
      - Send Email (Office 365 Outlook) action

    Expected JSON payload:
            { "subject": "...", "body": "<html>...", "to": "a@b.com;c@d.com" }
            Optional: { "from": "sender@example.com" }

    Returns True on success, False on failure.
    """
    if not LOGIC_APP_URL:
        logger.error(
            "Logic App not configured. Set LOGIC_APP_URL in .env "
            "(the HTTP trigger URL with SAS token)."
        )
        return False

    recipients = EMAIL_RECIPIENTS
    if not recipients:
        logger.error("No email recipients configured. Set EMAIL_RECIPIENTS in .env.")
        return False

    html_body = _markdown_to_html(digest)

    payload = {
        "subject": subject,
        "body": html_body,
        "to": recipients,
    }
    if EMAIL_SENDER:
        payload["from"] = EMAIL_SENDER

    try:
        with httpx.Client(timeout=_TIMEOUT) as client:
            resp = client.post(
                LOGIC_APP_URL,
                json=payload,
                headers={"Content-Type": "application/json"},
            )
            resp.raise_for_status()

        logger.info("Logic App triggered successfully (status %d)", resp.status_code)
        return True

    except httpx.HTTPStatusError as exc:
        logger.error(
            "Logic App returned HTTP %d: %s",
            exc.response.status_code,
            exc.response.text[:500],
        )
        return False
    except httpx.HTTPError as exc:
        logger.error("Failed to reach Logic App: %s", exc)
        return False
