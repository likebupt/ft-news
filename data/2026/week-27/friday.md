# Weekly Digest

*No company affiliations were provided in the source summaries, so items are grouped under a single academic/research bucket.*

## Research / Academia (arXiv / unspecified teams)

- **[Spectral Imbalance Causes Forgetting in Low-Rank Continual Adaptation](https://arxiv.org/search/?query=Spectral+Imbalance+Causes+Forgetting+in+Low-Rank+Continual+Adaptation&searchtype=all)** — Argues catastrophic forgetting in parameter-efficient continual learning is driven by **spectral imbalance**, pointing to spectrum/rank control as a lever for better retention.

- **[Clinically Structured Rank-Gated LoRA for Cross-Benchmark Medical Question Answering](https://arxiv.org/abs/2606.31432)** — Proposes **clinically structured, rank-gated LoRA** for medical QA, suggesting **task-structured dynamic rank allocation** can outperform uniform adapters in specialized domains.

- **[The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning](https://arxiv.org/abs/2607.01415)** — Makes the case that coding-agent RL performance depends heavily on **execution environments, sandboxing, orchestration, and rollout throughput**, not just the policy update loop.

- **[Token Geometry](https://arxiv.org/abs/2607.01455)** — Studies the gradient geometry of the **token embedding table and LM head**, highlighting the token read/write interface as an important factor in training and fine-tuning behavior.

- **[Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis](https://arxiv.org/abs/2607.01918)** — Introduces a **tuning-free time-series foundation model** aimed at handling multiple tasks without per-task fine-tuning, potentially reducing adaptation and deployment overhead.

- **[kNNGuard: Turning LLM Hidden Activations into a Training-Free Configurable Guardrail](https://arxiv.org/abs/2607.02072)** — Proposes a **training-free safety guardrail** using hidden activations plus **kNN-style retrieval**, enabling configurable moderation without retraining a separate classifier.

## Key Takeaways

- **PEFT research is getting more adaptive:** both **rank-gated LoRA** and **spectrum-aware continual adaptation** point toward smarter, less uniform fine-tuning.
- **Infrastructure is now a core RL variable:** for coding agents, **rollout systems and execution environments** can be as important as reward design or policy optimization.
- **Training-free / low-tuning methods are gaining traction:** from **time-series foundation models** to **guardrails**, teams are looking to cut iteration and deployment cost.
- **Core model interfaces still matter:** work on **token geometry** suggests improvements may come not only from higher-level training recipes, but also from better understanding embedding/output-layer optimization.