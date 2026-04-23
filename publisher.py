"""Email publisher - sends weekly digest via Microsoft Graph API."""

from __future__ import annotations

import logging
import re

import httpx
import msal

from config import (
    EMAIL_RECIPIENTS,
    EMAIL_SENDER,
    GRAPH_CLIENT_ID,
    GRAPH_CLIENT_SECRET,
    GRAPH_TENANT_ID,
)

logger = logging.getLogger(__name__)

_TIMEOUT = httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0)
_GRAPH_SCOPE = ["https://graph.microsoft.com/.default"]
_GRAPH_SEND_URL = "https://graph.microsoft.com/v1.0/users/{sender}/sendMail"


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


def _get_graph_token() -> str:
    """Acquire an access token for Microsoft Graph using client credentials."""
    app = msal.ConfidentialClientApplication(
        GRAPH_CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{GRAPH_TENANT_ID}",
        client_credential=GRAPH_CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=_GRAPH_SCOPE)
    if "access_token" not in result:
        raise RuntimeError(
            f"Failed to acquire Graph token: {result.get('error_description', result)}"
        )
    return result["access_token"]


def _build_graph_payload(
    digest: str,
    subject: str,
    recipients: str,
) -> dict:
    """Build the Graph API sendMail payload with HTML body."""
    html_body = _markdown_to_html(digest)

    to_recipients = [
        {"emailAddress": {"address": addr.strip()}}
        for addr in recipients.split(";")
        if addr.strip()
    ]

    return {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": html_body,
            },
            "toRecipients": to_recipients,
        },
        "saveToSentItems": "false",
    }


def send_email(
    digest: str,
    subject: str = "Weekly Finetuning & Post-Training Update",
) -> bool:
    """Send the weekly digest as an email via Microsoft Graph API.

    Returns True on success, False on failure.
    """
    if not all([GRAPH_TENANT_ID, GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET, EMAIL_SENDER]):
        logger.error(
            "Graph API not configured. "
            "Set GRAPH_TENANT_ID, GRAPH_CLIENT_ID, GRAPH_CLIENT_SECRET, "
            "and EMAIL_SENDER in .env."
        )
        return False

    recipients = EMAIL_RECIPIENTS
    if not recipients:
        logger.error("No email recipients configured. Set EMAIL_RECIPIENTS in .env.")
        return False

    try:
        token = _get_graph_token()
    except RuntimeError as exc:
        logger.error("Graph auth failed: %s", exc)
        return False

    payload = _build_graph_payload(digest, subject, recipients)
    url = _GRAPH_SEND_URL.format(sender=EMAIL_SENDER)

    try:
        with httpx.Client(timeout=_TIMEOUT) as client:
            resp = client.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {token}"},
            )
            resp.raise_for_status()

        logger.info("Email sent successfully (status %d)", resp.status_code)
        return True

    except httpx.HTTPStatusError as exc:
        logger.error(
            "Graph API returned HTTP %d: %s",
            exc.response.status_code,
            exc.response.text[:500],
        )
        return False
    except httpx.HTTPError as exc:
        logger.error("Failed to reach Graph API: %s", exc)
        return False
