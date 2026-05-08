"""FT News Weekly - Configuration."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(override=True)

# Paths
ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / os.getenv("DATA_DIR", "data")
SEEN_URLS_FILE = DATA_DIR / ".seen_urls.json"

# Azure OpenAI
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-5.4-pro")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-04-01-preview")

# Email via Microsoft Graph API
GRAPH_TENANT_ID = os.getenv("GRAPH_TENANT_ID", "")
GRAPH_CLIENT_ID = os.getenv("GRAPH_CLIENT_ID", "")
GRAPH_CLIENT_SECRET = os.getenv("GRAPH_CLIENT_SECRET", "")
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "")  # e.g. you@microsoft.com
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS", "")  # semicolon-separated

# Site
SITE_BASE_PATH = os.getenv("SITE_BASE_PATH", "/ft-news")  # GitHub Pages subpath

# Schedule (PST)
DAILY_FETCH_HOUR = int(os.getenv("DAILY_FETCH_HOUR", "18"))
DAILY_FETCH_MINUTE = int(os.getenv("DAILY_FETCH_MINUTE", "0"))
WEEKLY_PUSH_HOUR = int(os.getenv("WEEKLY_PUSH_HOUR", "9"))
WEEKLY_PUSH_MINUTE = int(os.getenv("WEEKLY_PUSH_MINUTE", "0"))

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Finetuning-related keywords for relevance filtering
RELEVANCE_KEYWORDS = [
    "fine-tun", "finetun", "fine tun",
    "post-train", "post train",
    "instruction tun", "instruction-tun",
    "rlhf", "reinforcement learning from human",
    "dpo", "direct preference optimization",
    "grpo", "group relative policy optimization",
    "ppo", "proximal policy optimization",
    "lora", "qlora", "low-rank adaptation",
    "peft", "parameter-efficient",
    "adapter", "adaptor",
    "alignment", "model alignment",
    "reward model", "preference learning",
    "supervised fine", "sft",
    "distillation", "knowledge distillation",
    "model customization", "custom model",
    "training data", "training pipeline",
    "checkpoint", "model merging",
    "continued pretraining", "continual learning",
    "domain adaptation",
    "synthetic data generation",
    "data curation", "data quality",
    "evaluation benchmark",
    "unsloth", "axolotl", "trl",
]
