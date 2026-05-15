# Final Weekly Digest

No company affiliations were provided in the source summaries, so all items are grouped under **Open Research / arXiv (multiple institutions)**.

## Open Research / arXiv

### Fine-Tuning, PEFT & Adaptation
- [**Towards the Next Frontier of LLMs, Training on Private Data: A Cross-Domain Benchmark for Federated Fine-Tuning**](https://arxiv.org/abs/2605.13936) — Benchmark for federated fine-tuning on private, decentralized data in regulated domains.
- [**PreFT: Prefill-only finetuning for efficient inference**](https://arxiv.org/abs/2605.14217) — Personalization method that shifts adaptation into prefill to reduce decode-time serving cost.
- [**GPart: End-to-End Isometric Fine-Tuning via Global Parameter Partitioning**](https://arxiv.org/abs/2605.14841) — Geometry-aware PEFT alternative to LoRA aimed at preserving optimization structure.
- [**ScaLoRA: Optimally Scaled Low-Rank Adaptation for Efficient High-Rank Fine-Tuning**](https://arxiv.org/abs/2510.23818) — Improves LoRA scaling so higher-rank adapters train more effectively.
- [**PEML: Parameter-efficient Multi-Task Learning with Optimized Continuous Prompts**](https://arxiv.org/abs/2605.14055) — Multi-task PEFT using shared continuous prompts.
- [**TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA**](https://arxiv.org/abs/2510.04682) — Tries to make LoRA adapters transferable across backbone models.
- [**TRIM: Token-wise Attention-Derived Saliency for Data-Efficient Instruction Tuning**](https://arxiv.org/abs/2510.07118) — Uses token-level saliency to select higher-value instruction data.
- [**Query-Conditioned Test-Time Self-Training for Large Language Models**](https://arxiv.org/abs/2605.13369) — Explores per-query adaptation at inference time via self-training.
- [**EndPrompt: Efficient Long-Context Extension via Terminal Anchoring**](https://arxiv.org/abs/2605.14589) — Extends context length without training on full target-length sequences.
- [**How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining**](https://arxiv.org/abs/2511.18903) — Shows curriculum order and LR schedule must be co-designed.

### Distillation, Quantization & Efficiency
- [**Towards Resource-Efficient LLMs: End-to-End Energy Accounting of Distillation Pipelines**](https://arxiv.org/abs/2605.13981) — Measures full teacher–student energy cost rather than only deployed model efficiency.
- [**AMiD: Knowledge Distillation for LLMs with α-mixture Assistant Distribution**](https://arxiv.org/abs/2510.15982) — Mixes teacher and student outputs during KD to reduce mismatch.
- [**Distribution Corrected Offline Data Distillation for Large Language Models**](https://arxiv.org/abs/2605.14071) — Corrects distribution drift in offline teacher-trace distillation.
- [**Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Generation via Multi-Stage In-Flight Rejection**](https://arxiv.org/abs/2605.14062) — Rejects low-quality synthetic samples mid-generation to save tokens.
- [**Rethinking Output Alignment For 1-bit Post-Training Quantization of Large Language Models**](https://arxiv.org/abs/2512.21651) — Revisits alignment objectives for extreme 1-bit PTQ.
- [**DiffusionOPD: A Unified Perspective of On-Policy Distillation in Diffusion Models**](https://arxiv.org/abs/2605.15055) — Unifies on-policy distillation for RL-tuned diffusion models.
- [**OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework**](https://arxiv.org/abs/2603.24422) — Applies self-distillation and latent reasoning to generative search.

### RL, Preference Optimization & Post-Training
- [**Self-Distilled Agentic Reinforcement Learning**](https://arxiv.org/abs/2605.15155) — Adds denser token-level guidance to sparse-reward agent RL.
- [**Reinforcement Learning with Semantic Rewards Enables Low-Resource Language Expansion without Alignment Tax**](https://arxiv.org/abs/2605.14366) — Uses semantic-reward RL to improve low-resource language ability while limiting forgetting.
- [**GIFT: Group-Relative Implicit Fine-Tuning Integrates GRPO with DPO and UNA**](https://arxiv.org/abs/2510.23868) — Combines grouped rollouts, implicit rewards, and advantage matching.
- [**GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation**](https://arxiv.org/abs/2605.11853) — Improves credit assignment for long-horizon agent tasks.
- [**Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training**](https://arxiv.org/abs/2605.12483) — Argues sparse rewards are best used to train a strong teacher, then distilled.
- [**It Takes Two: Your GRPO Is Secretly DPO**](https://arxiv.org/abs/2510.00977) — Suggests GRPO behaves much like DPO in key regimes.
- [**TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching**](https://arxiv.org/abs/2605.12288) — Moves preference optimization from sequence level to token level.
- [**Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards**](https://arxiv.org/abs/2605.14117) — Applies RLVR to structured, constraint-heavy design generation.

### Safety, Reliability & Evaluation
- [**GradShield: Alignment Preserving Finetuning**](https://arxiv.org/abs/2605.14194) — Filters finetuning data to reduce safety/alignment drift.
- [**Functional-level Uncertainty Quantification for Calibrated Fine-tuning on LLMs**](https://arxiv.org/abs/2410.06431) — Integrates uncertainty estimation directly into PEFT for better calibration.
- [**Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning**](https://arxiv.org/abs/2602.19612) — Studies how salience and training source affect unlearning difficulty.
- [**DocScope: Benchmarking Verifiable Reasoning for Trustworthy Long-Document Understanding**](https://arxiv.org/abs/2605.08888) — Benchmark for verifiable reasoning over long multimodal documents.
- [**Dimension-Level Intent Fidelity Evaluation for Large Language Models**](https://arxiv.org/abs/2605.14517) — Separates prompt-form adherence from true user-intent preservation.
- [**When Evidence Conflicts: Uncertainty and Order Effects in Retrieval-Augmented Biomedical Question Answering**](https://arxiv.org/abs/2605.14115) — Evaluates biomedical RAG under incomplete, misleading, and contradictory evidence.

### Long-Context, Memory, Multimodal & Specialized Applications
- [**Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture**](https://arxiv.org/abs/2605.14448) — Adds selective reasoning to multimodal embedding models with Dual-LoRA.
- [**ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both**](https://arxiv.org/abs/2605.15198) — Explores lighter control mechanisms for visual reasoning.
- [**BOOKMARKS: Efficient Active Storyline Memory for Role-playing**](https://arxiv.org/abs/2605.14169) — Search-based memory system for long-horizon consistency.
- [**Teaching and Evaluating LLMs to Reason About Polymer Design Related Tasks**](https://arxiv.org/abs/2601.16312) — Case for domain-specialized post-training in polymer science.

## Key Takeaways
- **Post-training is becoming deployment-first** — privacy, serving latency, calibration, and full-pipeline energy are now central concerns, not side metrics ([Federated Fine-Tuning](https://arxiv.org/abs/2605.13936), [PreFT](https://arxiv.org/abs/2605.14217), [Energy Accounting](https://arxiv.org/abs/2605.13981)).
- **RL, distillation, and preference optimization are converging** — many papers use sparse-to-dense supervision, self-distillation, or token-level objectives instead of plain GRPO/DPO recipes ([Self-Distilled Agentic RL](https://arxiv.org/abs/2605.15155), [Sparse-to-Dense Reward Principle](https://arxiv.org/abs/2605.12483), [TokenRatio](https://arxiv.org/abs/2605.12288)).
- **PEFT research is broadening beyond vanilla LoRA** — new work targets scaling, adapter portability, multi-task prompting, and geometry-aware optimization ([ScaLoRA](https://arxiv.org/abs/2510.23818), [TiTok](https://arxiv.org/abs/2510.04682), [GPart](https://arxiv.org/abs/2605.14841)).
- **Evaluation is shifting toward reliability and traceability** — verifiable reasoning, intent fidelity, uncertainty under conflicting evidence, and realistic unlearning are gaining weight ([DocScope](https://arxiv.org/abs/2605.08888), [Intent Fidelity](https://arxiv.org/abs/2605.14517), [HealthContradict study](https://arxiv.org/abs/2605.14115), [Anatomy of Unlearning](https://arxiv.org/abs/2602.19612)).
- **Post-training methods are spreading into new stacks** — search, multimodal retrieval, agent memory, structured design, and scientific reasoning all show up in this week’s papers ([OneSearch-V2](https://arxiv.org/abs/2603.24422), [BOOKMARKS](https://arxiv.org/abs/2605.14169), [Floor Plan RLVR](https://arxiv.org/abs/2605.14117), [Polymer Design](https://arxiv.org/abs/2601.16312)).