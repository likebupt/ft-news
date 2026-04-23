# Weekly Finetuning & Post-Training Update

**TL;DR:** Big week for finetuning — OpenAI ships cheaper fine-tuning API, Meta open-sources a new RLHF toolkit, and Google publishes a breakthrough paper on parameter-efficient training.

## Top Stories

- **OpenAI slashes fine-tuning costs by 50%** and adds support for GPT-5 fine-tuning with vision inputs. This directly impacts our competitive positioning. [Read more](https://openai.com/blog/fine-tuning-updates)
- **Meta releases RLHF-Toolkit v2**, a fully open-source framework for reward model training and PPO/DPO alignment. Supports distributed training out of the box. [Read more](https://ai.meta.com/blog/rlhf-toolkit-v2)
- **Google DeepMind publishes "LoRA-XL"** — a new parameter-efficient method that matches full fine-tuning quality at 1/10th the compute. [Paper](https://arxiv.org/abs/2026.12345)

## By Company

### OpenAI
- Fine-tuning API now supports GPT-5 and multimodal inputs (text + images). [Source](https://openai.com/blog/fine-tuning-updates)
- New evaluation dashboard for fine-tuned models with automated benchmarking. [Source](https://openai.com/blog/eval-dashboard)

### Meta
- RLHF-Toolkit v2 includes pre-built reward models for code, math, and instruction following. [Source](https://ai.meta.com/blog/rlhf-toolkit-v2)

### Google DeepMind
- LoRA-XL paper demonstrates scaling parameter-efficient methods to 400B+ parameter models. [Paper](https://arxiv.org/abs/2026.12345)

### Anthropic
- Published research on "Constitutional AI" fine-tuning with synthetic preference data. [Source](https://www.anthropic.com/research/constitutional-ft)

### NVIDIA
- NeMo Framework adds native DPO and KTO support for custom LLM alignment. [Source](https://blogs.nvidia.com/nemo-dpo-kto)

## Notable Papers

- **LoRA-XL: Scaling Parameter-Efficient Fine-Tuning** (Google DeepMind) — Key insight: using block-diagonal adapters enables LoRA to scale without quality loss. [Paper](https://arxiv.org/abs/2026.12345)
- **Synthetic Preference Optimization** (Anthropic) — Generates training preferences from constitutional principles, reducing need for human labelers. [Paper](https://arxiv.org/abs/2026.67890)

## What This Means for Us

- OpenAI's price cut and multimodal fine-tuning raise the bar — we need competitive pricing and vision fine-tuning in Foundry
- Meta's open-source RLHF toolkit could become the de facto standard; consider integration or compatibility
- LoRA-XL's efficiency gains suggest we should evaluate it for our managed fine-tuning infrastructure
