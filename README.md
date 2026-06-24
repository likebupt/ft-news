# FT News Weekly

> Automated finetuning & post-training news aggregator for the Microsoft Foundry Finetuning team.

**Live site: [https://likebupt.github.io/ft-news/](https://likebupt.github.io/ft-news/)**

A zero-maintenance static website deployed on GitHub Pages that automatically collects, filters, and summarizes AI finetuning news from 20+ official sources every day, and produces a polished weekly digest every Monday.

## How It Works

```text
             ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  20 RSS  ──▶│  Async       │────▶│  Map-Reduce  │────▶│  Static Site │
  Feeds      │  Ingestion   │     │  Summarizer  │     │  Builder     │
             │  (aiohttp)   │     │  (Azure AI)  │     │  (HTML/CSS)  │
             └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
                    │                    │                     │
             ┌──────▼───────┐     ┌──────▼───────┐     ┌──────▼───────┐
             │   SQLite DB  │     │  Cached      │     │   GitHub     │
             │  (dedup,     │     │  Summaries   │     │   Pages      │
             │   articles)  │     │  (DB + .md)  │     │   Deploy     │
             └──────────────┘     └──────────────┘     └──────────────┘
```

**Daily (01:00 UTC / 6 PM PST):** GitHub Actions → async RSS fetch → SQLite dedup → map-reduce LLM summary → build site → deploy to GitHub Pages

**Weekly (Mon 17:00 UTC / 9 AM PST):** GitHub Actions → ingest latest → map-reduce weekly digest → build site → deploy

## Features

- **Async ingestion** — 8 concurrent RSS feeds via aiohttp with retry and rate limiting
- **Map-reduce summarization** — articles chunked (10/batch), summarized in parallel (2 threads), then merged into a final digest
- **SQLite storage** — full dedup by URL, time-window queries, summary caching
- **Rich weekly digest** — TL;DR hero card, Top Stories cards, company tag bar, table of contents, implications callout
- **Zero maintenance** — runs entirely on GitHub Actions, deploys to GitHub Pages

## Monitored Sources

| Category | Sources |
| ---------- | --------- |
| **Big Tech** | OpenAI, Google AI, DeepMind, Meta AI, Microsoft Research, Microsoft AI Blog, NVIDIA, Amazon Science, Apple ML |
| **AI Unicorns** | Anthropic, Mistral AI, Cohere, Together AI, xAI, Databricks |
| **Open Source** | Hugging Face, Unsloth |
| **Research** | arXiv cs.LG, arXiv cs.CL |

## Setup

### 1. Clone & Install

```bash
git clone https://github.com/likebupt/ft-news.git
cd ft-news
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your values
```

| Variable | Description |
| ---------- | ------------- |
| `AZURE_OPENAI_ENDPOINT` | Azure AI Foundry endpoint (e.g. `https://your-resource.services.ai.azure.com/api/projects/your-project/openai/v1`) |
| `AZURE_OPENAI_API_KEY` | API key |
| `AZURE_OPENAI_DEPLOYMENT` | Deployment name (e.g. `gpt-5.4-pro`) |
| `AZURE_OPENAI_API_VERSION` | API version (e.g. `2025-04-01-preview`) |
| `LOGIC_APP_URL` | Optional Logic App HTTP trigger URL for email publishing |
| `EMAIL_RECIPIENTS` | Optional semicolon-separated email recipients |
| `EMAIL_SENDER` | Optional sender metadata if your Logic App workflow expects it |

### 3. GitHub Actions Secrets

Go to **Settings → Secrets and variables → Actions** and add the Azure OpenAI variables above. Add the email variables only if a workflow or scheduled process sends email.

## CLI Commands

```bash
# ── Pipeline (recommended) ──
python main.py pipeline          # Daily: ingest → summarize → build
python main.py weekly-pipeline   # Weekly: digest → build

# ── Individual steps ──
python main.py ingest            # Fetch all RSS feeds → SQLite
python main.py migrate           # Import legacy JSON files into DB
python main.py digest            # Generate weekly digest (map-reduce)
python main.py digest --week 19  # Specific week
python main.py digest --force    # Ignore cache, re-summarize
python main.py daily             # Generate today's summary
python main.py daily --date 2026-05-08
python main.py db-stats          # Show DB statistics
python main.py build             # Build static site from data/
python main.py sources           # List all configured sources
```

## Data Structure

```text
data/
├── ft_news.db          # SQLite (gitignored, rebuilt from JSON in CI)
└── 2026/
    └── week-19/
        ├── weekly-digest.md   # LLM-generated weekly digest
        ├── friday.md          # Daily summary
        └── friday-raw.json    # Raw article metadata
```

## Customization

### Adding Sources

Edit `sources.py`:

```python
NewsSource(
    name="New Company",
    feed_url="https://company.com/blog/rss.xml",
    source_type="rss",
    category="unicorn",  # bigtech | unicorn | opensource | research
)
```

### Tuning Relevance

Edit `RELEVANCE_KEYWORDS` in `config.py` to adjust which articles pass the filter.

### Adjusting Summary Style

Edit `_REDUCE_PROMPT` in `map_reduce.py` to change the weekly digest format, tone, or sections.

## Troubleshooting

| Issue | Solution |
| ------- | ---------- |
| No articles found | Check RSS URLs; run `python main.py ingest` to debug |
| LLM errors | Verify Azure OpenAI credentials; check endpoint uses Responses API path |
| Cached stale digest | Run `python main.py digest --force` to regenerate |
| GitHub Actions fails | Check Secrets are set; manually trigger workflow to test |

## License

Internal Microsoft use.
