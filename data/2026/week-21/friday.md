# Weekly Digest

*Most items in this batch don’t list clear company affiliations, so they’re grouped under **arXiv / Open Research**.*

## Meta
- **[torchtune: PyTorch native post-training library](https://arxiv.org/abs/2605.21442)** — PyTorch-native toolkit for open-weight LLM fine-tuning and post-training.

## arXiv / Open Research

### Post-training, RL & Preference Optimization
- **[GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents](https://arxiv.org/abs/2605.20246)** — GRPO-style RL for open-world VLM agents with explicit state/action trajectory modeling.
- **[FBOS-RL: Feedback-Driven Bi-Objective Synergistic Reinforcement Learning](https://arxiv.org/abs/2605.20256)** — Bi-objective RL that better couples rollout sampling with policy updates.
- **[Spectral Souping: A Unified Framework for Online Preference Alignment](https://arxiv.org/abs/2605.20408)** — Online preference alignment aimed at more personalized user preference handling.
- **[Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs](https://arxiv.org/abs/2605.20555)** — Blends frozen SFT behavior with trainable RL via logit averaging.
- **[Distributed Direct Preference Optimization](https://arxiv.org/abs/2605.20696)** — Extends DPO to distributed, heterogeneous-user preference data.
- **[AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback](https://arxiv.org/abs/2605.20722)** — Critic-free GRPO variant with adaptive clipping and decoding temperature.
- **[PREFINE: Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment](https://arxiv.org/abs/2605.21225)** — Adds safety constraints to reward-optimized policies using preference comparisons over lower-cost trajectories.
- **[How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR](https://arxiv.org/abs/2605.21266)** — Uses smaller sets of informative rollouts to reduce online RL cost.
- **[Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment](https://arxiv.org/abs/2605.20834)** — Argues DPO ≈ RLHF only under specific hidden assumptions.
- **[Linear-DPO: Linear Direct Preference Optimization for Diffusion and Flow-Matching Generative Models](https://arxiv.org/abs/2605.21123)** — Adapts DPO-style alignment to diffusion and flow-matching generators.
- **[Bayesian Preference Learning for Test-Time Steerable Reward Models](https://arxiv.org/abs/2602.08819)** — Uncertainty-aware reward models for test-time preference steering.
- **[Token-weighted Direct Preference Optimization with Attention](https://arxiv.org/abs/2605.21883)** — Weights DPO loss by token importance instead of treating all tokens equally.
- **[Value-Gradient Hypothesis of RL for LLMs](https://arxiv.org/abs/2605.21654)** — Theoretical view of why critic-free RL can work for LLM post-training.
- **[Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization](https://arxiv.org/abs/2605.21801)** — Proposes better uncertainty signals for filtering noisy rollouts.
- **[From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning](https://arxiv.org/abs/2605.22074)** — Breaks reasoning into verifiable subproblems for denser RL credit assignment.
- **[Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework](https://arxiv.org/abs/2605.22620)** — Multi-reward RLIF setup designed to reduce training collapse.
- **[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](https://arxiv.org/abs/2605.22817)** — Optimizes for diverse behaviors to strengthen search-based inference.
- **[LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance](https://arxiv.org/abs/2605.22567)** — Improves multilingual reasoning while preserving the user’s input language.

### Fine-tuning, Distillation & Data Selection
- **[Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages](https://arxiv.org/abs/2605.20285)** — Pushes post-training feedback upstream into pretraining and SFT.
- **[Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining](https://arxiv.org/abs/2605.20296)** — Recovers forgotten capabilities from base and fine-tuned checkpoints without full retraining.
- **[Consistently Informative Soft-Label Temperature for Knowledge Distillation](https://arxiv.org/abs/2605.20357)** — Adaptive KD temperature design for richer teacher signal transfer.
- **[SMoA: Spectrum Modulation Adapter for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2605.21147)** — PEFT adapter aimed at outperforming LoRA under very low-rank budgets.
- **[Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning](https://arxiv.org/abs/2605.21422)** — Selects fine-tuning data by expected preference impact.
- **[Federated LoRA Fine-Tuning for LLMs via Collaborative Alignment](https://arxiv.org/abs/2605.21217)** — Collaborative PEFT for highly heterogeneous client data.
- **[Unified Data Selection for LLM Reasoning](https://arxiv.org/abs/2605.22389)** — Uses HES to filter high-quality long-CoT data without extra training.
- **[From Parameters to Data: A Task-Parameter-Guided Fine-Tuning Pipeline for Efficient LLM Alignment](https://arxiv.org/abs/2605.21558)** — Connects PEFT choices with smarter alignment-data selection.
- **[X-Token: Projection-Guided Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2605.21699)** — Transfers richer teacher logits across incompatible tokenizers.
- **[LightReasoner: Can Small Language Models Teach Large Language Models Reasoning?](https://arxiv.org/abs/2510.07962)** — Tests whether smaller models can provide cheap reasoning supervision.
- **[MixSD: Mixed Contextual Self-Distillation for Knowledge Injection](https://arxiv.org/abs/2605.16865)** — Updates factual knowledge while trying to preserve reasoning and general capabilities.
- **[Beyond Temperature: Hyperfitting as a Late-Stage Geometric Expansion](https://arxiv.org/abs/2605.22579)** — Geometric account of why near-zero-loss fine-tuning can still improve generation.

### Reasoning, Agents & Long Context
- **[Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning](https://arxiv.org/abs/2605.20201)** — Trains on smaller proxy contexts to improve full long-context reasoning.
- **[ACC: Compiling Agent Trajectories for Long-Context Training](https://arxiv.org/abs/2605.21850)** — Uses agent-generated trajectories as scalable long-context training data.
- **[Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning](https://arxiv.org/abs/2605.22511)** — Self-distillation recipe for search-augmented reasoning.
- **[FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing](https://arxiv.org/abs/2605.22057)** — Continuously updates agent routing from production traffic.
- **[DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA](https://arxiv.org/abs/2605.22411)** — Query-time memory retrieval/distillation for long-history QA.
- **[SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations](https://arxiv.org/abs/2605.22564)** — Measures whether synthetic tool-calling traces are good enough for evals.

### Safety, Robustness & Failure Modes
- **[It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs](https://arxiv.org/abs/2605.20258)** — Self-distillation approach for privacy and contextual-integrity judgments.
- **[REFLECTOR: Internalizing Step-wise Reflection against Indirect Jailbreak](https://arxiv.org/abs/2605.20654)** — Step-wise reflection defense against indirect multi-turn jailbreaks.
- **[Optimus: A Robust Defense Framework for Mitigating Toxicity while Fine-Tuning Conversational AI](https://arxiv.org/abs/2507.05660)** — Protects fine-tuning on untrusted chat data from toxicity injection.
- **[Discovering Implicit Large Language Model Alignment Objectives](https://arxiv.org/abs/2602.15338)** — Infers latent behaviors actually incentivized by alignment rewards.
- **[Diagnosis Is Not Prescription: Linguistic Co-Adaptation Explains Patching Hazards in LLM Pipelines](https://arxiv.org/abs/2605.21958)** — Shows why patching the apparent failing module can worsen pipeline behavior.
- **[Hallucination as Commitment Failure: Larger LLMs Misfire Despite Knowing the Answer](https://arxiv.org/abs/2605.22007)** — Reframes some hallucinations as calibration/answer-selection failures, not knowledge gaps.

### Applications & Benchmarks
- **[Comparing LLM and Fine-Tuned Model Performance on NVDRS Circumstance Extraction with Varying Prompt Complexity](https://arxiv.org/abs/2605.21845)** — Uses task complexity buckets to compare prompt-based LLMs vs domain fine-tuning.
- **[Polite on the Surface, Wrong in Practice: A Curated Dataset for Fixing Honorific Failures in Multilingual Bangla Generation](https://arxiv.org/abs/2605.22487)** — Dataset targeting Bangla honorific and register failures.

## Key Takeaways
- **RL post-training is branching beyond vanilla GRPO/DPO** — New work emphasizes informative rollouts, token-level weighting, verifiable subproblems, multi-reward setups, and diversity-aware objectives. [AGPO](https://arxiv.org/abs/2605.20722)
- **Retention and efficiency are now first-class goals** — Post-hoc unforgetting, mixed self-distillation, smarter data selection, low-rank adapters, and cross-tokenizer KD all aim to cut cost without sacrificing capability. [Spectral Unforgetting](https://arxiv.org/abs/2605.20296)
- **Agent infrastructure is becoming its own post-training stack** — Trajectory compilation, live routing flywheels, query-time memory, and synthetic eval quality checks are emerging as core building blocks. [ACC](https://arxiv.org/abs/2605.21850)
- **Alignment is broadening well beyond generic helpfulness** — Privacy, multilingual behavior, hidden reward objectives, indirect jailbreaks, toxicity injection, and commitment-failure hallucinations are all active focus areas. [REFLECTOR](https://arxiv.org/abs/2605.20654)
- **Theory and tooling are catching up to practice** — PyTorch-native tooling, tighter DPO/RLHF assumptions, value-gradient explanations, and better uncertainty calibration are making post-training more interpretable and reproducible. [torchtune](https://arxiv.org/abs/2605.21442)