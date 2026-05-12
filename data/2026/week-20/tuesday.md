# Final Weekly Digest

*No company-specific announcements appeared across these five partial summaries, so everything is grouped under **Academic / arXiv**.*

## Academic / arXiv

### PEFT / Fine-Tuning / Adaptation
- **[BaLoRA](https://arxiv.org/abs/2605.08110)** — Bayesian LoRA adds uncertainty-aware low-rank updates to narrow the gap to full fine-tuning.
- **[CERSA](https://arxiv.org/abs/2605.08174)** — Retains more update “energy” than standard low-rank PEFT to better match full fine-tuning.
- **[Echo-LoRA](https://arxiv.org/abs/2605.08177)** — Extends PEFT into cross-layer activation-space adaptation, not just per-layer weight updates.
- **[Queryable LoRA](https://arxiv.org/abs/2605.08423)** — Makes adapters input-adaptive by routing over shared low-rank “atoms.”
- **[Beyond LoRA vs. Full Fine-Tuning](https://arxiv.org/abs/2605.07111)** — Uses gradient-guided optimizer routing to blend LoRA efficiency with full-FT plasticity.
- **[Gradient-Based LoRA Rank Allocation Under GRPO](https://arxiv.org/abs/2605.07366)** — Tests whether adaptive rank allocation transfers from SFT to RL post-training.
- **[AdaPaD](https://arxiv.org/abs/2605.10741)** — Learns effective adapter rank during training instead of fixing it up front.
- **[MatryoshkaLoRA](https://arxiv.org/abs/2605.07850)** — Trains hierarchical low-rank adapters so one run supports multiple effective ranks.
- **[Locking Pretrained Weights via Deep Low-Rank Residual Distillation](https://arxiv.org/abs/2605.10777)** — Freezes base weights and shifts adaptability into low-rank residuals.
- **[Can Muon Fine-tune Adam-Pretrained Models?](https://arxiv.org/abs/2605.10468)** — Analyzes optimizer mismatch when switching from Adam-pretrained checkpoints to Muon.
- **[When More Parameters Hurt](https://arxiv.org/abs/2605.08992)** — Shows larger pretrained priors can worsen worst-client outcomes in highly heterogeneous federated fine-tuning.

### Alignment / RL / Distillation
- **[The Extrapolation Cliff in On-Policy Distillation](https://arxiv.org/abs/2605.08737)** — Finds reward extrapolation can help until it abruptly breaks structured-output constraints.
- **[CoDistill-GRPO](https://arxiv.org/abs/2605.08873)** — Uses co-distillation to make GRPO work better for smaller reasoning models.
- **[Exploration-Driven Optimization for Test-Time LLM Reasoning](https://arxiv.org/abs/2605.09853)** — Tries to preserve exploration needed for inference-time search despite RL sharpening.
- **[G-Zero](https://arxiv.org/abs/2605.09959)** — Replaces external judges with intrinsic rewards for zero-data, verifier-free self-play.
- **[Rebellious Student](https://arxiv.org/abs/2605.10781)** — Reverses teacher signals on successful student rollouts to maintain reasoning diversity.
- **[MASS-DPO](https://arxiv.org/abs/2605.10784)** — Actively selects informative negatives to make multi-negative DPO more efficient.
- **[KL for a KL / vOPD](https://arxiv.org/abs/2605.07865)** — Adds a control-variate baseline to cut gradient variance in on-policy distillation.
- **[UFT](https://arxiv.org/abs/2410.21438)** — Unifies SFT and RLHF/DPO/UNA under a generalized implicit reward view.
- **[Enhanced LLM Reasoning via Search-Driven RL](https://arxiv.org/abs/2605.02073)** — Uses search to improve reward design for reasoning-heavy RL post-training.
- **[UNA](https://arxiv.org/abs/2408.15339)** — A supervised alignment framework that combines pairwise and scalar feedback.
- **[MaPPO](https://arxiv.org/abs/2507.21183)** — Adds prior reward knowledge to preference optimization through a MAP objective.
- **[Theoretical Limits of Language Model Alignment](https://arxiv.org/abs/2605.07105)** — Studies capability-preservation tradeoffs under KL-constrained RL and best-of-N selection.
- **[Experience Sharing in Mutual RL for Heterogeneous LMs](https://arxiv.org/abs/2605.07244)** — Lets different models share typed experience while training separately.
- **[Topology-Enhanced Alignment](https://arxiv.org/abs/2605.07172)** — Aligns hidden-state trajectory geometry, not just token-level outputs.
- **[Reinforce Adjoint Matching](https://arxiv.org/abs/2605.10759)** — Scales RL post-training for diffusion and flow-matching generators.
- **[Trajectory as the Teacher](https://arxiv.org/abs/2605.07924)** — Uses the full generation trajectory to distill few-step discrete flow models.
- **[Chain-based Distillation](https://arxiv.org/abs/2605.07783)** — Initializes multiple small-model sizes without repeatedly using a large teacher.

### Continual Learning / Retention / Unlearning / Reliability
- **[Revitalizing the Beginning](https://arxiv.org/abs/2605.08311)** — Model merging for storage-constrained continual learning without retaining prior task data.
- **[Self-Consolidating Language Models](https://arxiv.org/abs/2605.07076)** — Writes useful context into weights for later reuse while minimizing interference.
- **[Geometry Conflict](https://arxiv.org/abs/2605.09608)** — Frames catastrophic forgetting as geometric interference between new updates and old capability subspaces.
- **[Memorize Theorems, Not Instances](https://arxiv.org/abs/2605.09270)** — Argues SFT hurts math generalization when it memorizes examples instead of theorem-level abstractions.
- **[Unlearners Can Lie](https://arxiv.org/abs/2605.08765)** — Reports unlearning can increase hallucinations, abnormal tokens, and inconsistency.
- **[Anatomy of Unlearning](https://arxiv.org/abs/2602.19612)** — Shows unlearning difficulty depends on fact salience and whether knowledge came from pretraining or SFT.
- **[Optimizing Language Models for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)** — Uses RL-style optimization to reduce answer inconsistency across languages.

### Reasoning / Inference-Time Optimization
- **[LLMs for Sequential Decision-Making](https://arxiv.org/abs/2605.09009)** — Finds supervised fine-tuning improves MDP/POMDP-style in-context decision tasks.
- **[LaTER](https://arxiv.org/abs/2605.07315)** — Combines latent-space exploration with explicit verification to cut token-heavy reasoning cost.
- **[Can David Beat Goliath?](https://arxiv.org/abs/2601.21699)** — Examines multi-hop reasoning under tight rollout and batch budgets.
- **[Rethinking Dense Sequential Chains](https://arxiv.org/abs/2605.07307)** — Suggests reasoning models can often recover answers from sparse or shuffled CoT traces.

### Data / Federated / Safety / Structured Outputs
- **[Learning Multi-Indicator Weights for Data Selection](https://arxiv.org/abs/2605.09665)** — Learns task/model-specific mixtures of data-quality signals for instruction-tuning selection.
- **[Concordia](https://arxiv.org/abs/2605.09855)** — Uses self-improving synthetic tables for privacy-preserving federated adaptation under non-IID data.
- **[MIPIAD](https://arxiv.org/abs/2605.07269)** — Multilingual prompt-injection defense using Qwen, TF-IDF, and a meta-ensemble.
- **[InvThink](https://arxiv.org/abs/2510.01569)** — Premortem reasoning that enumerates likely failures before answering.
- **[ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189)** — A 100k-example dataset for schema-constrained JSON / structured generation.

## Key Takeaways
- **PEFT is moving beyond static LoRA** toward adaptive routing, dynamic rank discovery, hierarchical adapters, and uncertainty-aware updates — see **[BaLoRA](https://arxiv.org/abs/2605.08110)**, **[Queryable LoRA](https://arxiv.org/abs/2605.08423)**, **[AdaPaD](https://arxiv.org/abs/2605.10741)**, **[MatryoshkaLoRA](https://arxiv.org/abs/2605.07850)**.
- **Post-training work is increasingly about stability, not just reward gains** — variance reduction, capability preservation, and exploration control show up across **[vOPD](https://arxiv.org/abs/2605.07865)**, **[Extrapolation Cliff](https://arxiv.org/abs/2605.08737)**, **[UFT](https://arxiv.org/abs/2410.21438)**, **[Theoretical Limits](https://arxiv.org/abs/2605.07105)**.
- **Continual learning and unlearning are getting more diagnostic** — interference geometry, memory consolidation, salience-aware unlearning, and honesty regressions are all active themes in **[Geometry Conflict](https://arxiv.org/abs/2605.09608)**, **[Self-Consolidating LMs](https://arxiv.org/abs/2605.07076)**, **[Unlearners Can Lie](https://arxiv.org/abs/2605.08765)**, **[Anatomy of Unlearning](https://arxiv.org/abs/2602.19612)**.
- **Reasoning optimization is spreading into inference-time compute shaping** — latent reasoning, explicit verification, exploration-preserving decoding, and budget-aware training matter alongside fine-tuning; see **[LaTER](https://arxiv.org/abs/2605.07315)**, **[Exploration-Driven Optimization](https://arxiv.org/abs/2605.09853)**, **[Can David Beat Goliath?](https://arxiv.org/abs/2601.21699)**.
- **Synthetic, privacy-preserving, and structured signals are becoming core training infrastructure** — especially in **[Concordia](https://arxiv.org/abs/2605.09855)**, **[G-Zero](https://arxiv.org/abs/2605.09959)**, **[ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189)**, and **[MIPIAD](https://arxiv.org/abs/2605.07269)**.