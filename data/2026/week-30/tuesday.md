Since all three partials are academic research, I merged them under a single **Academia / arXiv** section and organized by theme.

# Final Weekly Digest

## Academia / arXiv

### Alignment, Safety, and Preference Optimization
- **[LLM Unlearning for Cyber Defense: A Survey on Methods, Challenges, and Emerging Threats](https://arxiv.org/abs/2607.16227)** — Survey of LLM unlearning for removing sensitive, harmful, or regulated knowledge in security-critical deployments.
- **[Normalized Rewards for Preference Optimization](https://arxiv.org/abs/2607.16240)** — Proposes reward normalization to stabilize DPO-style preference optimization and reduce over-optimization.
- **[TRACE: Trajectory-Based Safety Patch Learning for LLM Post-Training Realignment](https://arxiv.org/abs/2607.16242)** — Safety patching method to restore alignment after user fine-tuning degrades guardrails.
- **[Abliteration Is Not a Scalpel: Off-Target Effects of Refusal Removal on Decision Disposition Across Model Families](https://arxiv.org/abs/2607.17427)** — Shows that removing refusal behavior can shift broader decision tendencies, not just censorship behavior.
- **[A Geometric Perspective on Stabilizing Value Conflict Resolution](https://arxiv.org/abs/2607.17946)** — Uses a geometric framing to make RLHF-style value conflict resolution more stable.
- **[Metadata-Free Meta-Reweighted Direct Preference Optimization under Noisy Preference Labels](https://arxiv.org/abs/2607.09796)** — DPO variant that meta-reweights noisy preference pairs without requiring extra metadata.

### RL, Distillation, and Post-Training
- **[Let the Data Decide: Supervision Analysis, Capability Trade-offs, and Adaptive Objective Routing in Continued Pre-Training via Off-Policy Distillation](https://arxiv.org/abs/2607.16246)** — Explores adaptive routing of supervision signals instead of using a fixed distillation objective.
- **[Distilled Reinforcement Learning for LLM Post-training](https://arxiv.org/abs/2607.17247)** — Combines RL with on-policy distillation to improve reasoning, adaptation, and alignment.
- **[Trace-Based On-Policy Distillation for Masked Diffusion Language Models](https://arxiv.org/abs/2607.16872)** — Distillation-based post-training method tailored to diffusion LMs, with a focus on reasoning.
- **[Token-Level Off-Policy Learning for Faithful Generation Under Distribution Shift](https://arxiv.org/abs/2607.17524)** — Introduces token-level off-policy labeling to improve faithfulness under distribution shift.
- **[GradAlign: Gradient-Aligned Data Selection for LLM Reinforcement Learning](https://arxiv.org/abs/2602.21492)** — Selects RL training problems by gradient alignment to improve sample efficiency and data quality.
- **[OR Else: A Differentiable Trust Region for Policy Optimization](https://arxiv.org/abs/2607.18163)** — Differentiable trust-region alternative to PPO/GRPO clipping aimed at smoother optimization.
- **[MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient Reasoning in Compact Models](https://arxiv.org/abs/2607.18006)** — Uses debate-aware RL to improve reasoning in compact models while keeping training efficient.

### Diffusion Model Training
- **[AGG: Jacobian-Aggregated Group Gradient for Efficient GRPO Training of Diffusion Models](https://arxiv.org/abs/2607.17572)** — Efficiency-focused GRPO variant for diffusion models using grouped/Jacobian-based gradient aggregation.

### PEFT, LoRA, and Fine-Tuning Efficiency
- **[SOS-LoRA: Static Orthogonal-Subspace Low-Rank Adaptation with Fixed Multi-Scale Scaling](https://arxiv.org/abs/2607.16252)** — PEFT method that splits adaptation across