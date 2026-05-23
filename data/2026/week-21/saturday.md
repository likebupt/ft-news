## Final Weekly Digest — Fine-Tuning & Post-Training

*No company-specific announcements surfaced in these batches; all relevant items are grouped under **Research / Academia**.*

### Research / Academia

#### RL, alignment, and credit assignment
- **[Value-Gradient Hypothesis of RL for LLMs](https://arxiv.org/abs/2605.21654)** — Recasts LLM RL post-training through value gradients to explain why PPO/GRPO-style methods can work with limited critic machinery.
- **[OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2605.21851)** — Targets token-level credit assignment in RLVR, addressing GRPO’s flat trajectory-level rewards.
- **[From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning](https://arxiv.org/abs/2605.22074)** — Breaks hard reasoning traces into verifiable subproblems so failed rollouts still provide useful learning signal.
- **[Vector Policy Optimization: Training for Diversity Improves Test-Time Search](https://arxiv.org/abs/2605.22817)** — Optimizes vector-valued rewards to explicitly train rollout diversity for stronger test-time search.
- **[General Preference Reinforcement Learning](https://arxiv.org/abs/2605.18721)** — Seeks to unify verifiable-reward online RL with preference optimization for broader alignment tasks.
- **[GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents](https://arxiv.org/abs/2605.20246)** — Extends GRPO-style training to open-world vision-language agents via state-action modeling.
- **[Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation](https://arxiv.org/abs/2605.22731)** — Argues post-training outcomes depend more on supervised state distributions than token losses alone.
- **[TIP: Token Importance in On-Policy Distillation](https://arxiv.org/abs/2604.14084)** — Analyzes which token positions carry the highest-value learning signal in on-policy distillation.

#### Reward modeling, safety, and objective auditing
- **[Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization](https://arxiv.org/abs/2605.21801)** — Replaces semantic-entropy heuristics with geometry-aware, calibrated uncertainty estimates for better policy optimization signals.
- **[On-Policy Consistency Training Improves LLM Safety with Minimal Capability Degradation](https://arxiv.org/abs/2605.21834)** — Moves consistency training on-policy to improve safety against jailbreaks and related failures with limited capability loss.
- **[Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework](https://arxiv.org/abs/2605.22620)** — Uses multi-reward RLIF to reduce collapse when training from internal feedback instead of external labels.
- **[VRPRM: Process Reward Modeling via Visual Reasoning](https://arxiv.org/abs/2508.03556)** — Proposes a visual-reasoning-based PRM for stronger step-level evaluation on long-horizon reasoning tasks.
- **[Discovering Implicit Large Language Model Alignment Objectives](https://arxiv.org/abs/2602.15338)** — Attempts to recover the latent objectives actually optimized in alignment pipelines.
- **[DecepChain: Inducing Deceptive Reasoning in Large Language Models](https://arxiv.org/abs/2510.00319)** — Examines how models can produce plausible but incorrect chains of thought, weakening CoT as a trust signal.
- **[AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment](https://arxiv.org/abs/2605.17602)** — Proposes a rule-based reward model for text-to-image alignment with an emphasis on robustness and interpretability.

#### Efficiency, adaptation, and distillation
- **[From Parameters to Data: A Task-Parameter-Guided Fine-Tuning Pipeline for Efficient LLM Alignment](https://arxiv.org/abs/2605.21558)** — Links PEFT parameter selection to data selection to cut alignment cost.
- **[X-Token: Projection-Guided Cross-Tokenizer Knowledge Distillation](https://arxiv.org/abs/2605.21699)** — Introduces cross-tokenizer distillation for teacher/student pairs with incompatible vocabularies.
- **[Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.22263)** — Adapts self-distillation to the model’s current reasoning ability to avoid suppressing complex reasoning.
- **[Little by Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts](https://arxiv.org/abs/2506.21035)** — Adds rank-1 associative memory experts incrementally to reduce catastrophic forgetting during continual adaptation.
- **[SeqLoRA: Bilevel Orthogonal Adaptation for Continual Multi-Concept Generation](https://arxiv.org/abs/2605.22743)** — Uses orthogonal bilevel LoRA adaptation to reduce interference in continual multi-concept generation.

#### Multimodal / diffusion
- **[Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators](https://arxiv.org/abs/2605.22717)** — Explores efficient post-training for interactive, streaming diffusion-based music generation.

## Key Takeaways
- **Credit assignment is the clearest throughline** — papers like [OPPO](https://arxiv.org/abs/2605.21851), [SCRL](https://arxiv.org/abs/2605.22074), [TIP](https://arxiv.org/abs/2604.14084), and [Post-Training is About States, Not Tokens](https://arxiv.org/abs/2605.22731) all push beyond coarse trajectory-level or token-uniform supervision.
- **Reward quality and auditability are becoming central bottlenecks** — work on [VRPRM](https://arxiv.org/abs/2508.03556), [Why Semantic Entropy Fails](https://arxiv.org/abs/2605.21801), [Discovering Implicit Alignment Objectives](https://arxiv.org/abs/2602.15338), [DecepChain](https://arxiv.org/abs/2510.00319), and [AutoRubric-T2I](https://arxiv.org/abs/2605.17602) points to stronger interest in inspecting and hardening post-training signals.
- **On-policy methods are gaining ground across both safety and capability** — see [On-Policy Consistency Training](https://arxiv.org/abs/2605.21834), [Tailoring Teaching to Aptitude](https://arxiv.org/abs/2605.22263), [General Preference RL](https://arxiv.org/abs/2605.18721), and [GROW](https://arxiv.org/abs/2605.20246).
- **Efficiency and continual adaptation remain persistent priorities** — [From Parameters to Data](https://arxiv.org/abs/2605.21558), [X-Token](https://arxiv.org/abs/2605.21699), [Little by Little](https://arxiv.org/abs/2506.21035), [SeqLoRA](https://arxiv.org/abs/2605.22743), and [Live Music Diffusion Models](https://arxiv.org/abs/2605.22717) all target lower-cost adaptation without large capability tradeoffs.