"""Teams webhook publisher - sends weekly digest to a Teams channel via Incoming Webhook."""

from __future__ import annotations

import logging
import re

import httpx

from config import TEAMS_WEBHOOK_URL

logger = logging.getLogger(__name__)

_TIMEOUT = httpx.Timeout(connect=10.0, read=30.0, write=10.0, pool=10.0)


def _markdown_to_adaptive_card_body(markdown: str) -> list[dict]:
    """Convert markdown text to Adaptive Card body elements.

    This is a lightweight conversion that handles headings, bullets, and text.
    """
    body: list[dict] = []
    lines = markdown.strip().split("\n")

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        # Heading 1
        if stripped.startswith("# "):
            body.append({
                "type": "TextBlock",
                "text": stripped[2:],
                "size": "Large",
                "weight": "Bolder",
                "wrap": True,
            })
        # Heading 2
        elif stripped.startswith("## "):
            body.append({
                "type": "TextBlock",
                "text": stripped[3:],
                "size": "Medium",
                "weight": "Bolder",
                "wrap": True,
                "spacing": "Medium",
            })
        # Heading 3
        elif stripped.startswith("### "):
            body.append({
                "type": "TextBlock",
                "text": stripped[4:],
                "size": "Default",
                "weight": "Bolder",
                "wrap": True,
                "spacing": "Small",
            })
        # Horizontal rule
        elif stripped in ("---", "***", "___"):
            body.append({
                "type": "TextBlock",
                "text": "─" * 40,
                "size": "Small",
                "color": "Light",
                "spacing": "Small",
            })
        # Bullet point
        elif stripped.startswith(("- ", "* ", "• ")):
            bullet_text = stripped[2:]
            body.append({
                "type": "TextBlock",
                "text": f"• {bullet_text}",
                "wrap": True,
                "spacing": "Small",
            })
        # Numbered list
        elif re.match(r"^\d+\.\s", stripped):
            body.append({
                "type": "TextBlock",
                "text": stripped,
                "wrap": True,
                "spacing": "Small",
            })
        # Bold text block
        elif stripped.startswith("**") and stripped.endswith("**"):
            body.append({
                "type": "TextBlock",
                "text": stripped,
                "weight": "Bolder",
                "wrap": True,
            })
        # Regular text
        else:
            body.append({
                "type": "TextBlock",
                "text": stripped,
                "wrap": True,
                "spacing": "Small",
            })

    return body


def _build_adaptive_card(digest: str) -> dict:
    """Build a Teams-compatible Adaptive Card payload from the digest markdown."""
    body = _markdown_to_adaptive_card_body(digest)

    # Truncate body if it's extremely long (Teams has payload limits)
    if len(body) > 150:
        body = body[:150]
        body.append({
            "type": "TextBlock",
            "text": "_(Digest truncated — see full version in the shared folder)_",
            "isSubtle": True,
            "wrap": True,
        })

    return {
        "type": "message",
        "attachments": [
            {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "contentUrl": None,
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.5",
                    "msteams": {"width": "Full"},
                    "body": body,
                },
            }
        ],
    }


def send_to_teams(
    digest: str,
    webhook_url: str | None = None,
) -> bool:
    """Send the weekly digest to a Teams channel via Incoming Webhook.

    Returns True on success, False on failure.
    """
    url = webhook_url or TEAMS_WEBHOOK_URL
    if not url:
        logger.error(
            "No Teams webhook URL configured. "
            "Set TEAMS_WEBHOOK_URL in .env or pass it explicitly."
        )
        return False

    payload = _build_adaptive_card(digest)

    try:
        with httpx.Client(timeout=_TIMEOUT) as client:
            resp = client.post(url, json=payload)
            resp.raise_for_status()

        logger.info("Successfully posted weekly digest to Teams (status %d)", resp.status_code)
        return True

    except httpx.HTTPStatusError as exc:
        logger.error(
            "Teams webhook returned HTTP %d: %s",
            exc.response.status_code,
            exc.response.text[:500],
        )
        return False
    except httpx.HTTPError as exc:
        logger.error("Failed to reach Teams webhook: %s", exc)
        return False
