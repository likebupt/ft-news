# Weekly Digest

*No company-specific releases surfaced in these batches, so the week is grouped under **Open Research / Academia**.*

## Open Research / Academia

### Alignment, safety, and preference optimization
- [**Quantization Undoes Alignment: Bias Emergence in Compressed LLMs Across Models and Precision Levels**](https://arxiv.org/abs/2605.15208) — Post-training quantization can reintroduce bias, so safety/fairness checks need to be rerun on each quantized deployment.
- [**Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent Bias in LLMs for High-Stakes Decisions**](https://arxiv.org/abs/2605.15217) — Surface-level fairness may hide biased internal representations that still matter causally.
- [**Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation**](https://arxiv.org/abs/2605.15239) — Uses on-policy self-distillation to preserve reasoning performance while maintaining safety robustness.
- [**ActiveDPO: Active Direct Preference Optimization for Sample-Efficient Alignment**](https://arxiv.org/abs/2505.19241) — Adds active learning to DPO to cut human preference-labeling cost.
- [**What Is Preference Optimization Doing, and Why?**](https://arxiv.org/abs/2512.00778) — Provides theory for what preference-optimization methods are actually optimizing.
- [**Learning Where It Matters: Geometric Anchoring for Robust Preference Alignment**](https://arxiv.org/abs/2602.04909) — Addresses DPO reference drift with geometric anchoring for better robustness under noisy preferences and shift.
- [**Provably avoiding over-optimization in Direct Preference Optimization without knowing the data distribution**](https://arxiv.org/abs/2602.06239) — Introduces PEPO, a pessimistic-ensemble approach to reduce over-optimization without a reward model.
- [**ODRPO: Ordinal Decompositions of Discrete Rewards for Robust Policy Optimization**](https://arxiv.org/abs/2605.12667) — Recasts noisy multi-level auto-rater scores as ordinal subproblems to stabilize RLAIF training.
- [**Reward Auditor: Inference on Reward Modeling Suitability in Real-World Perturbed Scenarios**](https://arxiv.org/abs/2512.00920) — Evaluates reward models under perturbed, more deployment-like conditions rather than static accuracy alone.
- [**Mechanisms of Introspective Awareness**](https://arxiv.org/abs/2603.21396) — Studies why some open models can detect injected steering vectors, shedding light on model self-monitoring.
- [**Rethinking Output Alignment For 1-bit Post-Training Quantization of Large Language Models**](https://arxiv.org/abs/2512.21651) — Revisits output alignment for extreme 1-bit PTQ to retain more quality under very low-cost deployment.

### RL and post-training recipes
- [**GRLO: Towards Generalizable Reinforcement Learning in Open-Ended Environments from Zero**](https://arxiv.org/abs/2605.15464) — Proposes a broader RL post-training setup aimed at generalization beyond fixed feedback sources.
- [**Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking**](https://arxiv.org/abs/2605.16154) — Focuses optimization on rollout segments where trajectories diverge to reduce wasted VLA RL compute.
- [**Blending Supervised and Reinforcement Fine-Tuning with Prefix Sampling**](https://arxiv.org/abs/2507.01679) — Mixes SFT and RL fine-tuning to combine stability with better generalization.
- [**Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training**](https://arxiv.org/abs/2605.12483) — Proposes a four-stage sparse-to-dense reward pipeline for more label-efficient reasoning-model training.
- [**TemplateRL: Structured Template-Guided Reinforcement Learning for LLM Reasoning**](https://arxiv.org/abs/2505.15692) — Uses template-guided rollouts to teach reusable reasoning patterns instead of only fitting scalar rewards.
- [**Reference-Free Reinforcement Learning Fine-Tuning for MT: A Seq2Seq Perspective**](https://arxiv.org/abs/2605.15976) — Extends GRPO-style RLFT to encoder-decoder MT models with reference-free rewards.
- [**Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR**](https://arxiv.org/abs/2605.15726) — Targets RLVR exploration bottlenecks with strategy-guided exploration rather than brute-force rollout scaling.
- [**Stabilizing Knowledge, Promoting Reasoning: Dual-Token Constraints for RLVR**](https://arxiv.org/abs/2507.15778) — Applies different constraints to different token roles to preserve knowledge while improving reasoning.
- [**When Importance Sampling Misallocates Credit: Asymmetric Ratios for Outcome-Supervised RL**](https://arxiv.org/abs/2510.06062) — Introduces asymmetric importance ratios to improve token-level credit assignment in GRPO-style training.
- [**TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination**](https://arxiv.org/abs/2605.15207) — Uses trust-region updates to stabilize sequential fine-tuning in shared-context multi-agent systems.
- [**CLARE: Continual Learning for Vision-Language-Action Models via Autonomous Adapter Routing and Expansion**](https://arxiv.org/abs/2601.09512) — Uses modular adapter routing/expansion to add VLA skills while reducing forgetting.

### Efficiency, compression, and adaptation
- [**LoCO: Low-rank Compositional Rotation Fine-tuning**](https://arxiv.org/abs/2605.15916) — A PEFT method that aims to preserve pretrained weight geometry better than standard low-rank updates.
- [**Always Learning, Always Mixing: Efficient and Simple Data Mixing All The Time**](https://arxiv.org/abs/2605.15220) — Proposes one unified data-mixing strategy across pretraining, continual learning, and adaptation.
- [**Decouple Searching from Training: Scaling Data Mixing via Model Merging for Large Language Model Pre-training**](https://arxiv.org/abs/2602.00747) — Uses model merging to search for better pretraining mixtures without retraining every candidate.
- [**Towards Efficient Large Language Reasoning Models via Extreme-Ratio Chain-of-Thought Compression**](https://arxiv.org/abs/2602.08324) — Compresses CoT traces aggressively while trying to preserve logical fidelity and reduce inference cost.
- [**Painless Activation Steering: An Automated, Lightweight Approach for Post-Training Large Language Models**](https://arxiv.org/abs/2509.22739) — Automates activation steering as a cheaper, faster alternative to weight updates for some behaviors.
- [**DimMem**](https://arxiv.org/abs/2605.15759) — A lightweight long-term memory design for agents that preserves more structure than flat summaries.
- [**CompactQE**](https://arxiv.org/abs/2605.15763) — Argues sub-30B open models can perform interpretable translation quality estimation in a single pass.
- [**From Flat Language Labels to Typological Priors**](https://arxiv.org/abs/2605.16026) — Replaces simple language-ID conditioning with typological priors for multilingual speech-to-speech transfer.

### Agents, deployment, and real-world workflows
- [**FinReporting**](https://arxiv.org/abs/2604.05966) — An agentic workflow for localized reporting of financial disclosures across differing filing systems and taxonomies.
- [**Capability Conditioned Scaffolding for Professional Human LLM Collaboration**](https://arxiv.org/abs/2605.15404) — Adapts scaffolding to a user’s ability to verify outputs, aiming to reduce overreliance in professional settings.
- [**Fully Open Meditron: An Auditable Pipeline for Clinical LLMs**](https://arxiv.org/abs/2605.16215) — Emphasizes full auditability across data provenance, curation, and generation for clinical LLMs.
- [**Improve Large Language Model Systems with User Logs**](https://arxiv.org/abs/2602.06470) — Positions user logs as a key post-launch signal for continual improvement as scaling returns diminish.

### Evaluation, multilingual coverage, and detection
- [**Do Chinese models speak Chinese languages?**](https://arxiv.org/abs/2504.00289) — Tests whether Chinese open-weight models really cover the diverse languages spoken in China.
- [**IndicSafe: A Benchmark for Evaluating Multilingual LLM Safety in South Asia**](https://arxiv.org/abs/2603.17915) — Adds multilingual safety evaluation across 12 Indic languages.
- [**FINESSE-Bench**](https://arxiv.org/abs/2605.15482) — A hierarchical benchmark for financial-domain knowledge and technical analysis.
- [**MHGraphBench**](https://arxiv.org/abs/2605.15589) — A knowledge-graph-grounded benchmark for mental-health entity, relation, and judgment tasks.
- [**Evaluating Chinese Ambiguity Understanding in Large Language Models**](https://arxiv.org/abs/2605.15635) — Introduces a scalable benchmark for Chinese ambiguity understanding.
- [**DetectRL-X**](https://arxiv.org/abs/2605.15518) — A multilingual benchmark/framework for LLM-generated text detection under real-world conditions.
- [**Multi-Level Contextual Token Relation Modeling for Machine-Generated Text Detection**](https://arxiv.org/abs/2605.16107) — Proposes a token-relation-based detector aimed at more robust machine-text detection.
- [**MELI: the Mandarin-English Language Interview Corpus**](https://arxiv.org/abs/2603.27043) — Releases a 29.8-hour bilingual speech corpus for multilingual speech fine-tuning and evaluation.

## Key Takeaways
- **Efficiency remains the dominant engineering theme.** Work this week focused on cheaper post-training and deployment via [1-bit PTQ alignment](https://arxiv.org/abs/2512.21651), [CoT compression](https://arxiv.org/abs/2602.08324), [LoCO](https://arxiv.org/abs/2605.15916), [activation steering](https://arxiv.org/abs/2509.22739), and [chunk-masked RL](https://arxiv.org/abs/2605.16154).
- **Alignment is increasingly treated as fragile and deployment-specific.** Papers showed that [quantization can undo alignment](https://arxiv.org/abs/2605.15208), [latent bias can survive “fair” outputs](https://arxiv.org/abs/2605.15217), and [reward models need perturbation-based auditing](https://arxiv.org/abs/2512.00920).
- **Post-training is getting more structured and stability-focused.** Instead of brute-force rollout scaling, authors proposed [sparse-to-dense reward pipelines](https://arxiv.org/abs/2605.12483), [template-guided RL](https://arxiv.org/abs/2505.15692), [dual-token RL constraints](https://arxiv.org/abs/2507.15778), and [trust-region multi-agent tuning](https://arxiv.org/abs/2605.15207).
- **Evaluation is moving closer to real deployment.** New work emphasized [clinical auditability](https://arxiv.org/abs/2605.16215), [financial and mental-health benchmarks](https://arxiv.org/abs/2605.15482), [multilingual safety](https://arxiv.org/abs/2603.17915), and [real-world text detection](https://arxiv.org/abs/2605.15518).
- **Real-world feedback loops are becoming central.** Papers on [user-log learning](https://arxiv.org/abs/2602.06470), [continual VLA adaptation](https://arxiv.org/abs/2601.09512), [agent memory](https://arxiv.org/abs/2605.15759), and [data-mixture search](https://arxiv.org/abs/2602.00747) all point toward more iterative improvement after initial pretraining.

If you want, I can also turn this into a **shorter exec-summary version** or a **table format by theme/paper/link**.