# Final Weekly Digest

*Most papers in the source feed did not include clear company metadata, so they’re grouped under **Research / Academic**.*

## OpenAI
- **[Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely)** — Outlines the deployment safety stack for coding agents: sandboxing, approval controls, network restrictions, and agent-native telemetry.

## Together AI
- **[Serving DeepSeek-V4: why million-token context is an inference systems problem](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)** — Frames million-token context as a serving challenge driven by KV-cache compression, prefix caching, kernel maturity, and endpoint design.

## Zyphra
- **[ZAYA1-8B Technical Report](https://arxiv.org/abs/2605.05365)** — Introduces a reasoning-focused MoE with **8B total / 700M active parameters** on **MoE++**, trained on a full AMD stack.

## Olava
- **[A Few Good Clauses: Comparing LLMs vs Domain-Trained Small Language Models on Structured Contract Extraction](https://arxiv.org/abs/2605.05532)** — Reports that **Olava Extract**, a legal-domain MoE SLM, beat several frontier LLMs on structured contract extraction at lower cost.

## Research / Academic

### RL, alignment, and post-training
- **[Rethinking Data Curation in LLM Training](https://arxiv.org/abs/2605.05227)** — Replaces static data mixing with **online reweighting** during training; reports stronger generalization under shifts.
- **[RVPO: Risk-Sensitive Alignment via Variance Regularization](https://arxiv.org/abs/2605.05750)** — Adds variance-based regularization so weak safety/formatting objectives are not washed out by average reward.
- **[Near-Policy: Accelerating On-Policy Distillation](https://arxiv.org/abs/2605.05940)** — Uses asynchronous **near-on-policy distillation** to reduce teacher-student mismatch without full RL-style cost.
- **[Optimal Transport for LLM Reward Modeling from Noisy Preference](https://arxiv.org/abs/2605.06036)** — Applies optimal transport to make reward models more robust to corrupted or heterogeneous preference labels.
- **[A Unified Pair-GRPO Family](https://arxiv.org/abs/2605.06375)** — Unifies pairwise preference-based RL alignment methods to improve stability and interpretability.
- **[On the Implicit Reward Overfitting and the Low-rank Dynamics in RLVR](https://arxiv.org/abs/2605.06523)** — Argues RLVR gains often concentrate in low-rank directions that may also encode implicit reward overfitting.
- **[Nonsense Helps: Prompt Space Perturbation Broadens Reasoning Exploration](https://arxiv.org/abs/2605.05566)** — Perturbs prompts, including nonsensical variants, to recover learning signal when all rollouts initially fail.
- **[Sample-efficient LLM Optimization with Reset Replay](https://arxiv.org/abs/2508.06412)** — Introduces **Reset Replay** to improve sample efficiency and reduce primacy bias in long RL/preference runs.
- **[P²O: Joint Policy and Prompt Optimization](https://arxiv.org/abs/2603.21877)** — Jointly optimizes the policy and the prompt to address advantage collapse on hard reasoning samples.
- **[How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum](https://arxiv.org/abs/2604.25907)** — Proposes a unified loss family between SFT and RLVR, explaining why **SFT→RLVR** often beats RLVR from scratch.
- **[Knowledge-Level Consistency Reinforcement Learning: Dual-Fact Alignment for Long-Form Factuality](https://arxiv.org/abs/2509.23765)** — Uses knowledge-consistency RL to reduce long-form hallucinations beyond standard preference rewards.
- **[Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text](https://arxiv.org/abs/2604.20051)** — Turns pretraining corpora into synthetic supervision and reward signals via rubric-based self-play.
- **[Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients](https://arxiv.org/abs/2605.06650)** — Proposes a positive-only RLVR update that approximates negative feedback implicitly.
- **[OPSD Compresses What RLVR Teaches: A Post-RL Compaction Stage for Reasoning Models](https://arxiv.org/abs/2605.06188)** — Uses post-RL self-distillation to compact reasoning behavior and shorten outputs while keeping RL gains.
- **[Reinforced Informativeness Optimization for Long-Form RAG](https://arxiv.org/abs/2505.20825)** — Optimizes for informative, evidence-grounded long-form answers instead of brittle single-answer rewards.
- **[Correct Is Not Enough](https://arxiv.org/abs/2605.03862)** — Introduces executor-grounded rewards so planners learn reasoning traces that downstream systems can actually use.

### Fine-tuning, continual learning, and adaptation
- **[CRAFT: Forgetting-Aware Intervention-Based Adaptation for Continual Learning](https://arxiv.org/abs/2605.05732)** — Keeps base weights fixed and learns low-rank hidden-state interventions to add capabilities with less forgetting.
- **[Optimizer-Model Consistency](https://arxiv.org/abs/2605.06654)** — Finds that full finetuning with the **same optimizer as pretraining** can improve the learning/forgetting tradeoff.
- **[Rethinking Adapter Placement](https://arxiv.org/abs/2605.06183)** — Suggests PEFT performance depends heavily on **where** adapters are placed, not just how many parameters are updated.
- **[Generalizing the Geometry of Model Merging Through Fréchet Averages](https://arxiv.org/abs/2604.27155)** — Extends checkpoint merging with symmetry-aware Fréchet averages.
- **[Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training](https://arxiv.org/abs/2605.06076)** — Argues static “locate-then-update” maps can go stale during finetuning and may need dynamic re-localization.
- **[Attribution-Guided Continual Learning for Large Language Models](https://arxiv.org/abs/2605.05285)** — Uses attribution signals to track where knowledge lives, aiming to reduce catastrophic forgetting during sequential updates.
- **[KORE](https://arxiv.org/abs/2510.19316)** — Focuses on knowledge injection for multimodal models while preserving existing capabilities.

### Agents, tools, and interaction
- **[MemReranker: Reasoning-Aware Reranking for Agent Memory Retrieval](https://arxiv.org/abs/2605.06132)** — Replaces similarity-heavy memory reranking with reasoning-aware retrieval for agents.
- **[Teaching Thinking Models to Reason with Tools: A Full-Pipeline Recipe for Tool-Integrated Reasoning](https://arxiv.org/abs/2605.06326)** — Finds eval-time tool enablement alone can hurt reasoning; proposes training tool use end to end.
- **[StraTA: Incentivizing Agentic Reinforcement Learning with Strategic Trajectory Abstraction](https://arxiv.org/abs/2605.06642)** — Uses higher-level trajectory abstractions to improve long-horizon exploration and credit assignment.
- **[When2Speak](https://arxiv.org/abs/2605.05626)** — Introduces a dataset for temporal participation and turn-taking in multi-party conversations.
- **[One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue](https://arxiv.org/abs/2605.05630)** — Targets attacks that spread harmful intent across benign-looking dialogue turns.

### Safety, evaluation, and behavior
- **[Measuring Evaluation-Context Divergence in Open-Weight LLMs](https://arxiv.org/abs/2605.06327)** — Proposes paired prompts to test whether models behave differently in “eval-like” vs normal contexts.
- **[Priming, Path-dependence, and Plasticity](https://arxiv.org/abs/2605.05767)** — Uses 140K chatbot sessions to show early interactions can shape later user prompting behavior.
- **[Safety Anchor](https://arxiv.org/abs/2605.05995)** — Proposes geometric bottlenecks as a defense against harmful finetuning under persistent attack.
- **[Precise Debugging Benchmark](https://arxiv.org/abs/2604.17338)** — Measures whether coding models make localized, minimal edits instead of regenerating whole solutions.

### Data, domain, and application-focused post-training
- **[DialectLLM](https://arxiv.org/abs/2601.22888)** — Uses synthetic dialogue data to improve multi-dialect handling and reduce stereotyped responses.
- **[From Documents to Spans](https://arxiv.org/abs/2603.15270)** — Converts document-level supervision into span-level evidence for auditable ICD coding.
- **[Generating Query-Focused Summarization Datasets from Query-Free Summarization Datasets](https://arxiv.org/abs/2605.05392)** — Auto-generates evidence-based queries from standard summarization datasets to bootstrap QFS training data.

## Key Takeaways
- **RL post-training is moving beyond raw reward maximization** toward better signal recovery, bottleneck-aware objectives, noisy-preference robustness, and process-grounded rewards ([RVPO](https://arxiv.org/abs/2605.05750), [Reset Replay](https://arxiv.org/abs/2508.06412), [P²O](https://arxiv.org/abs/2603.21877), [Correct Is Not Enough](https://arxiv.org/abs/2605.03862)).
- **Efficient adaptation is increasingly about structure, not just fewer updated parameters**—online data reweighting, hidden-state interventions, selective adapter placement, optimizer consistency, and symmetry-aware merging all stood out ([Rethinking Data Curation](https://arxiv.org/abs/2605.05227), [CRAFT](https://arxiv.org/abs/2605.05732), [Rethinking Adapter Placement](https://arxiv.org/abs/2605.06183), [Optimizer-Model Consistency](https://arxiv.org/abs/2605.06654), [Fréchet Averages](https://arxiv.org/abs/2604.27155)).
- **Synthetic and weakly supervised data pipelines remain a major lever** for expanding post-training coverage ([Rubric Self-play](https://arxiv.org/abs/2604.20051), [DialectLLM](https://arxiv.org/abs/2601.22888), [QFS Dataset Generation](https://arxiv.org/abs/2605.05392), [From Documents to Spans](https://arxiv.org/abs/2603.15270)).
- **Agent quality is becoming end-to-end**: memory retrieval, tool use, long-horizon planning, dialogue timing, and runtime controls all matter—not just base-model strength ([MemReranker](https://arxiv.org/abs/2605.06132), [Tool-Integrated Reasoning](https://arxiv.org/abs/2605.06326), [StraTA](https://arxiv.org/abs/2605.06642), [Codex safety stack](https://openai.com/index/running-codex-safely)).
- **Safety work is broadening across both training and deployment**—from harmful-finetuning defenses and multi-turn intent detection to evaluation-context probes and production agent safeguards ([Safety Anchor](https://arxiv.org/abs/2605.05995), [One Turn Too Late](https://arxiv.org/abs/2605.05630), [Evaluation-Context Divergence](https://arxiv.org/abs/2605.06327), [Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely)).
- **Differentiation is shifting toward specialization and systems engineering**: efficient MoEs, domain SLMs, and long-context serving stacks are becoming durable advantages ([ZAYA1-8B](https://arxiv.org/abs/2605.05365), [Olava Extract](https://arxiv.org/abs/2605.05532), [Serving DeepSeek-V4](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)).