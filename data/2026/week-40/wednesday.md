# Weekly Digest

## Open Research / arXiv
*No company-specific announcements were included in the source summaries; all notable items were open research.*

- **[MaD-RL: Matching Distributions for Calibrating LLMs with Reinforcement Learning](https://arxiv.org/abs/2609.31644)** — RL post-training for **distribution-level calibration**, aiming to improve confidence quality rather than just verifier/reward scores.
- **[DOHF: Online Diffusion Fine-tuning with Doob's h-transform Guidance](https://arxiv.org/abs/2609.31882)** — Online **reward-based diffusion fine-tuning** for settings where good samples are rare or rewards are expensive.
- **[Understanding the Synergy between SFT, RLVR, and OPD in LLM Post-Training](https://arxiv.org/abs/2609.31900)** — Analyzes how **SFT, RL with verifiable rewards, and on-policy distillation** interact in multi-stage post-training pipelines.
- **[On-Policy Attention Linearization](https://arxiv.org/abs/2609.31947)** — Uses post-training to push pretrained transformers toward **linear-attention-heavy hybrids** without retraining from scratch.
- **[SAMBAR: Selective Anchoring via Method of Multipliers for Balanced Knowledge Acquisition and Retention in Vision-Language-Action Models](https://arxiv.org/abs/2609.32108)** — Addresses **continual fine-tuning** in VLA models by balancing new-task learning with retention.
- **[Certification Frontiers for Gaussian LoRA: Independent Priors, Posterior Risk, and Prediction-Preserving Balancing](https://arxiv.org/abs/2609.32271)** — Studies when **Bayesian LoRA fine-tuning** can and cannot deliver useful generalization certificates.
- **[When the Merge Coefficient Stops Mattering: Proximity Regularized Merging for Continual LoRA Adaptation](https://arxiv.org/abs/2609.32332)** — Proposes a **rehearsal-free continual LoRA** method that reduces sensitivity to merge coefficients across tasks.
- **[Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation](https://arxiv.org/abs/2609.32361)** — Introduces a **black-box auditing** lens for checking epistemic reliability in debate-distilled verifiers.
- **[Attribution Without a Second Pass: Inline Per-Sample Gradient Provenance at ~1% Overhead](https://arxiv.org/abs/2609.32380)** — Captures per-sample gradient provenance **during training**, potentially making attribution practical at routine fine-tuning scale.
- **[On the Pitfalls of Verbalized Confidence Priors for Calibrating Large Reasoning Models](https://arxiv.org/abs/2609.32470)** — Warns that **verbalized confidence priors** can hurt rather than help calibration in reasoning-heavy