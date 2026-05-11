No company-specific announcements appeared in these source summaries, so this week’s digest is grouped under **Academic / arXiv**.

## Academic / arXiv

### PEFT, fine-tuning, and model adaptation
- **[Beyond Factor Aggregation](https://arxiv.org/abs/2605.06733)** — Proposes gauge-aware server representations so federated LoRA aggregation is consistent at the update level, not the factor level.
- **[SR²-LoRA](https://arxiv.org/abs/2605.07420)** — Reduces class-incremental PEFT forgetting by preserving inter-layer relations with a self-rectifying LoRA scheme.
- **[Bayesian Fine-tuning in Projected Subspaces](https://arxiv.org/abs/2605.07706)** — Brings Bayesian uncertainty estimation to LoRA-style tuning in a cheaper projected space.
- **[MatryoshkaLoRA](https://arxiv.org/abs/2605.07850)** — Learns nested low-rank adapters so one fine-tuned model can run at multiple ranks.
- **[Beyond LoRA vs. Full Fine-Tuning](https://arxiv.org/abs/2605.07111)** — Uses gradient signals to route updates between full fine-tuning and LoRA instead of picking one globally.
- **[Gradient-Based LoRA Rank Allocation Under GRPO](https://arxiv.org/abs/2605.07366)** — Tests whether adaptive rank allocation still helps under GRPO-style RL tuning.
- **[Don’t Retrain, Align](https://arxiv.org/abs/2605.06885)** — Adapts autoregressive LMs into diffusion LMs via representation alignment rather than retraining from scratch.
- **[Dr. Post-Training](https://arxiv.org/abs/2605.07063)** — Recasts post-training data mixing as regularization: scarce target data drives learning, broader data stabilizes it.
- **[Self-Consolidating Language Models](https://arxiv.org/abs/2605.07076)** — Explores writing useful context back into model weights while limiting interference.

### Alignment, RLHF/RLVR, and preference optimization
- **[How to Compress KV Cache in RL Post-Training?](https://arxiv.org/abs/2605.06850)** — Shadow Mask Distillation targets rollout KV-cache memory costs in online alignment.
- **[f-Divergence Regularized RLHF](https://arxiv.org/abs/2605.06977)** — Unifies RLHF analyses beyond reverse KL and studies how divergence choice interacts with sampling.
- **[Response Time Enhances Alignment with Heterogeneous Preferences](https://arxiv.org/abs/2605.06987)** — Uses annotator response time as extra signal when preferences differ across raters.
- **[Theoretical Limits of Language Model Alignment](https://arxiv.org/abs/2605.07105)** — Analyzes when KL-constrained RL and best-of-N can improve reward without damaging base capabilities.
- **[Experience Sharing in Mutual Reinforcement Learning](https://arxiv.org/abs/2605.07244)** — Lets heterogeneous LMs share typed experience while keeping separate weights, objectives, and tokenizers.
- **[Rethinking Importance Sampling in LLM Policy Optimization](https://arxiv.org/abs/2605.07331)** — Proposes a cumulative-token view of off-policy importance sampling for better bias/variance trade-offs.
- **[POETS](https://arxiv.org/abs/2605.07775)** — Compute-efficient policy ensembles for uncertainty-aware exploration in LLM optimization.
- **[KL for a KL (vOPD)](https://arxiv.org/abs/2605.07865)** — Introduces a control-variate baseline to reduce variance in on-policy distillation’s KL estimates.
- **[Beyond Pairs](https://arxiv.org/abs/2605.08037)** — Argues preference data forms a graph, not isolated pairs, and proposes graph-aware alignment objectives.
- **[Structured Role-Aware Policy Optimization](https://arxiv.org/abs/2605.07274)** — Improves multimodal RLVR credit assignment with role-specific rewards across reasoning traces.
- **[UNA](https://arxiv.org/abs/2408.15339)** — Unified supervised alignment that combines pairwise preferences and scalar feedback in one framework.
- **[Topology-Enhanced Alignment](https://arxiv.org/abs/2605.07172)** — Regularizes hidden-state trajectory topology rather than optimizing only token likelihood or scalar preferences.
- **[Optimizing LMs for Crosslingual Knowledge Consistency](https://arxiv.org/abs/2603.04678)** — Uses RL to reduce multilingual answer inconsistency.
- **[Enhanced LLM Reasoning with Search-Driven RL](https://arxiv.org/abs/2605.02073)** — Uses search to optimize reward functions for stronger reasoning post-training.
- **[InvThink](https://arxiv.org/abs/2510.01569)** — Premortem-style safety method where models first enumerate likely harms before answering.

### Distillation, reasoning efficiency, and small-model deployment
- **[Star Elastic](https://arxiv.org/abs/2605.07182)** — Builds nested submodels inside one reasoning checkpoint to support multiple latency/compute budgets.
- **[Trajectory as the Teacher](https://arxiv.org/abs/2605.07924)** — Distills flow-matching text generators into few-step students using full generation trajectories.
- **[Chain-based Distillation for Variable-Sized SLMs](https://arxiv.org/abs/2605.07783)** — Initializes several small-model sizes efficiently without repeatedly depending on a large teacher.
- **[LiteGUI](https://arxiv.org/abs/2605.07505)** — Uses RL-based distillation to improve compact on-device GUI agents.
- **[Can David Beat Goliath?](https://arxiv.org/abs/2601.21699)** — Studies multi-hop reasoning when rollout counts, batch sizes, and RL budgets are tightly constrained.
- **[Rethinking Dense Sequential Chains](https://arxiv.org/abs/2605.07307)** — Finds models can often recover answers from sparse, masked, or shuffled chain-of-thought traces.
- **[LaTER](https://arxiv.org/abs/2605.07315)** — Cuts test-time reasoning cost via latent exploration followed by explicit verification.
- **[SOD](https://arxiv.org/abs/2605.07725)** — Step-wise on-policy distillation stabilizes small tool-using agents under sparse rewards.

### Mechanistic diagnostics, evaluation, and robustness
- **[The Convergence Gap](https://arxiv.org/abs/2605.07282)** — Shows instruction-tuned models stabilize their next-token decisions later in the forward pass.
- **[Instruction Tuning Changes How Upstream State Conditions Late Readout](https://arxiv.org/abs/2605.07284)** — Cross-patching suggests instruction tuning changes internal dependency structure, not just output style.
- **[Not All Tokens Learn Alike](https://arxiv.org/abs/2605.07660)** — Attention entropy reveals token-level heterogeneity in RL reasoning updates.
- **[How Value Induction Reshapes LLM Behaviour](https://arxiv.org/abs/2605.07925)** — Examines how training on value-laden language shifts broader model behavior.
- **[Anatomy of Unlearning](https://arxiv.org/abs/2602.19612)** — DUAL benchmark studies how fact salience and training source affect unlearning difficulty.
- **[Quality-Conditioned Agreement in Short Answer Scoring](https://arxiv.org/abs/2605.07647)** — Shows generic few-shot LLM grading struggles most on partially correct mid-range answers.
- **[ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189)** — Releases a large dataset for schema-constrained, web-grounded structured generation.

### Applied, safety, and domain-specific post-training
- **[Emergent Symbolic Structure in Health Foundation Models](https://arxiv.org/abs/2605.07407)** — Decomposes frozen health-model embeddings into interpretable symbols for concept alignment and multimodal transfer.
- **[MIPIAD](https://arxiv.org/abs/2605.07269)** — Multilingual indirect prompt-injection defense using a LoRA-tuned classifier, TF-IDF features, and a meta-ensemble.
- **[BITS Pilani at SemEval-2026 Task 9](https://arxiv.org/abs/2604.11121)** — Practical recipe combining structured SFT with DPO refinement for multilingual polarization detection.
- **[WeatherSyn](https://arxiv.org/abs/2605.07522)** — Instruction-tuned multimodal model for weather forecasting report generation.
- **[Uncertainty-Aware Structured Data Extraction from Full CMR Reports](https://arxiv.org/abs/2605.08045)** — Distilled clinical extraction pipeline with per-field confidence for more auditable deployment.

## Key Takeaways
- **Post-training is getting more modular and adaptive** — from gauge-aware federated LoRA and gradient-routed FT/LoRA hybrids to nested-rank adapters and many-in-one reasoning checkpoints. Relevant: **[Beyond Factor Aggregation](https://arxiv.org/abs/2605.06733)**, **[Beyond LoRA vs. Full Fine-Tuning](https://arxiv.org/abs/2605.07111)**, **[MatryoshkaLoRA](https://arxiv.org/abs/2605.07850)**, **[Star Elastic](https://arxiv.org/abs/2605.07182)**.
- **Alignment research is becoming more theory-heavy and structurally richer** — with work on divergence choices, theoretical limits, importance sampling, graph-structured preferences, topology-aware objectives, and side-channel signals like response time. Relevant: **[f-Divergence RLHF](https://arxiv.org/abs/2605.06977)**, **[Theoretical Limits](https://arxiv.org/abs/2605.07105)**, **[Rethinking Importance Sampling](https://arxiv.org/abs/2605.07331)**, **[Beyond Pairs](https://arxiv.org/abs/2605.08037)**, **[Topology-Enhanced Alignment](https://arxiv.org/abs/2605.07172)**.
- **Efficiency remains the dominant systems theme** — spanning RL rollout memory reduction, distillation for smaller models, lighter GUI/tool agents, and cheaper reasoning at inference time. Relevant: **[KV Cache Compression](https://arxiv.org/abs/2605.06850)**, **[Trajectory as the Teacher](https://arxiv.org/abs/2605.07924)**, **[LiteGUI](https://arxiv.org/abs/2605.07505)**, **[LaTER](https://arxiv.org/abs/2605.07315)**.
- **Researchers are probing post-training more mechanistically** — instruction tuning, RL, and value induction are increasingly being studied via forward-pass diagnostics, token-level signals, and behavioral analysis rather than only downstream benchmarks. Relevant: **[The Convergence Gap](https://arxiv.org/abs/2605.07282)**, **[Cross-Patching Diagnostic](https://arxiv.org/abs/2605.07284)**, **[Not All Tokens Learn Alike](https://arxiv.org/abs/2605.07660)**, **[How Value Induction Reshapes Behaviour](https://arxiv.org/abs/2605.07925)**.
- **Domain-specific adaptation still matters** — health, weather, clinical extraction, multilingual safety, and structured-output tasks continue to benefit from targeted post-training or distillation rather than generic prompting alone. Relevant: **[Health Symbols](https://arxiv.org/abs/2605.07407)**, **[WeatherSyn](https://arxiv.org/abs/2605.07522)**, **[CMR Extraction](https://arxiv.org/abs/2605.08045)**, **[MIPIAD](https://arxiv.org/abs/2605.07269)**, **[ScrapeGraphAI-100k](https://arxiv.org/abs/2602.15189)**.

If you want, I can also turn this into a **shorter exec-only version** or a **table with columns for area / contribution / likely practical impact**.