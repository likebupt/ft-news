# FT News Weekly

> Automated finetuning & post-training news aggregator for the Microsoft Foundry Finetuning team.

This agent fetches daily news from official AI company blogs and research feeds, filters for finetuning/post-training relevance, summarizes them using Azure OpenAI, and delivers a polished weekly digest to Microsoft Teams every Monday at 9:00 AM PST.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  RSS Feeds  │────▶│   Fetcher    │────▶│  Summarizer  │────▶│  Publisher   │
│  (20+ src)  │     │  + Filter    │     │  (Azure OAI) │     │  (Teams)     │
└─────────────┘     └──────┬───────┘     └──────┬───────┘     └──────────────┘
                           │                     │
                    ┌──────▼───────┐     ┌───────▼──────┐
                    │  daily-raw   │     │  daily .md   │
                    │  .json       │     │  weekly .md  │
                    └──────────────┘     └──────────────┘
```

**Data Flow:**

1. **Daily (6 PM PST):** Fetcher pulls RSS feeds → filters by finetuning keywords → deduplicates → LLM summarizes → saves to `data/YYYY/week-NN/day.md`
2. **Weekly (Mon 9 AM PST):** Digest generator reads all daily summaries → LLM creates weekly digest → Publisher sends Adaptive Card to Teams

## Monitored Sources

| Category | Sources |
|----------|---------|
| **Big Tech** | OpenAI, Google AI, DeepMind, Meta AI, Microsoft Research, NVIDIA, Amazon Science, Apple ML |
| **AI Unicorns** | Anthropic, Mistral AI, Cohere, Together AI, xAI, Databricks |
| **Open Source** | Hugging Face, Unsloth |
| **Research** | arXiv cs.LG, arXiv cs.CL |

## Setup

### 1. Clone & Install

```bash
git clone <repo-url>
cd ft-news-weekly
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your values
```

Required settings:

| Variable | Description |
|----------|-------------|
| `AZURE_OPENAI_ENDPOINT` | Your Azure OpenAI resource endpoint |
| `AZURE_OPENAI_API_KEY` | API key for Azure OpenAI |
| `AZURE_OPENAI_DEPLOYMENT` | Deployment name (e.g., `gpt-4o`) |
| `TEAMS_WEBHOOK_URL` | Teams Incoming Webhook URL |

### 3. Set Up Teams Webhook

1. Open your Teams channel
2. Click **⋯** → **Connectors** (or **Manage channel** → **Connectors**)
3. Find **Incoming Webhook** → **Configure**
4. Name it "FT News Weekly", optionally add an icon
5. Copy the webhook URL to your `.env` file

## Usage

### CLI Commands

```bash
# Start the automated scheduler (daily fetch + weekly digest)
python main.py run

# Manually fetch today's news + summarize
python main.py fetch

# Fetch only (no LLM summarization, for testing)
python main.py fetch-only

# Generate weekly digest for the previous week
python main.py digest

# Generate digest for a specific week (by reference date)
python main.py digest --date 2026-04-20

# Push the latest digest to Teams
python main.py push

# List all configured sources
python main.py sources
```

### Running as a Service

For production, run the scheduler as a background service:

**Option A: systemd (Linux)**
```ini
# /etc/systemd/system/ft-news-weekly.service
[Unit]
Description=FT News Weekly Agent
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/ft-news-weekly
ExecStart=/path/to/python main.py run
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
```

**Option B: Task Scheduler (Windows)**
1. Open Task Scheduler
2. Create a new task
3. Set trigger: Daily at your preferred time
4. Set action: `python main.py fetch` (for daily) or `python main.py run` (for continuous)

**Option C: Azure Container Instance / Azure Functions**
Deploy as a containerized service for zero-maintenance operation.

## Data Structure

```
data/
└── 2026/
    └── week-16/
        ├── monday-raw.json      # Raw fetched articles
        ├── monday.md            # LLM-generated daily summary
        ├── tuesday-raw.json
        ├── tuesday.md
        ├── ...
        └── weekly-digest.md     # Weekly rollup (sent to Teams)
```

## Customization

### Adding New Sources

Edit `sources.py` to add new RSS feeds:

```python
NewsSource(
    name="New Company",
    feed_url="https://company.com/blog/rss.xml",
    source_type="rss",
    category="unicorn",  # bigtech | unicorn | opensource | research
)
```

### Adjusting Relevance Keywords

Edit `RELEVANCE_KEYWORDS` in `config.py` to tune what articles are considered relevant.

### Changing Summary Style

Edit the system prompts in `summarizer.py` (`_DAILY_SYSTEM_PROMPT` and `_WEEKLY_SYSTEM_PROMPT`) to adjust tone, format, or focus areas.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No articles found | Check if RSS feed URLs are accessible; run `python main.py fetch-only` to debug |
| LLM errors | Verify Azure OpenAI credentials in `.env` |
| Teams push fails | Check webhook URL; ensure it's not expired |
| Duplicate articles | Delete `data/.seen_urls.json` to reset dedup tracking |

## License

Internal Microsoft use.
