"""News source registry - official blogs and feeds from major AI companies."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NewsSource:
    """A single news source to monitor."""

    name: str  # Company / org name
    feed_url: str  # RSS / Atom feed URL
    source_type: str  # "rss" | "atom" | "blog"
    category: str  # "bigtech" | "unicorn" | "research" | "opensource"


# ---------------------------------------------------------------------------
# Official RSS/Atom feeds from major AI companies and research labs.
# Each URL points to the company's own blog or research feed.
# ---------------------------------------------------------------------------
SOURCES: list[NewsSource] = [
    # ---- Big Tech ----
    NewsSource(
        name="OpenAI",
        feed_url="https://openai.com/blog/rss.xml",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Google AI Blog",
        feed_url="https://blog.google/technology/ai/rss/",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Google DeepMind",
        feed_url="https://deepmind.google/blog/rss.xml",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Meta AI",
        feed_url="https://ai.meta.com/blog/rss/",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Microsoft Research",
        feed_url="https://www.microsoft.com/en-us/research/feed/",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Microsoft AI Blog",
        feed_url="https://blogs.microsoft.com/ai/feed/",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="NVIDIA AI Blog",
        feed_url="https://blogs.nvidia.com/ai/feed/",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Amazon Science",
        feed_url="https://www.amazon.science/index.rss",
        source_type="rss",
        category="bigtech",
    ),
    NewsSource(
        name="Apple Machine Learning",
        feed_url="https://machinelearning.apple.com/rss.xml",
        source_type="rss",
        category="bigtech",
    ),

    # ---- AI Unicorns / Startups ----
    NewsSource(
        name="Anthropic",
        feed_url="https://www.anthropic.com/rss.xml",
        source_type="rss",
        category="unicorn",
    ),
    NewsSource(
        name="Mistral AI",
        feed_url="https://mistral.ai/feed.xml",
        source_type="rss",
        category="unicorn",
    ),
    NewsSource(
        name="Cohere",
        feed_url="https://cohere.com/blog/rss.xml",
        source_type="rss",
        category="unicorn",
    ),
    NewsSource(
        name="Together AI",
        feed_url="https://www.together.ai/blog/rss.xml",
        source_type="rss",
        category="unicorn",
    ),
    NewsSource(
        name="xAI",
        feed_url="https://x.ai/blog/rss.xml",
        source_type="rss",
        category="unicorn",
    ),
    NewsSource(
        name="Databricks (Mosaic)",
        feed_url="https://www.databricks.com/feed",
        source_type="rss",
        category="unicorn",
    ),

    # ---- Open Source / Community ----
    NewsSource(
        name="Hugging Face",
        feed_url="https://huggingface.co/blog/feed.xml",
        source_type="rss",
        category="opensource",
    ),
    NewsSource(
        name="Unsloth",
        feed_url="https://unsloth.ai/blog/rss.xml",
        source_type="rss",
        category="opensource",
    ),

    # ---- Research (arXiv) ----
    # arXiv RSS for cs.LG (Machine Learning) - filtered by keywords later
    NewsSource(
        name="arXiv cs.LG",
        feed_url="https://rss.arxiv.org/rss/cs.LG",
        source_type="rss",
        category="research",
    ),
    # arXiv RSS for cs.CL (Computation and Language)
    NewsSource(
        name="arXiv cs.CL",
        feed_url="https://rss.arxiv.org/rss/cs.CL",
        source_type="rss",
        category="research",
    ),
]


def get_sources(category: str | None = None) -> list[NewsSource]:
    """Return sources, optionally filtered by category."""
    if category is None:
        return SOURCES
    return [s for s in SOURCES if s.category == category]
