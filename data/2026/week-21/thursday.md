# Final Weekly Digest

*Most items this week are arXiv papers without clear company attribution in the source metadata, so they’re grouped under **Academic / Open Research**. The only clearly attributable org in this batch is **Meta**.*

## Meta

- [**torchtune: PyTorch native post-training library**](https://arxiv.org/abs/2605.21442) — PyTorch-native toolkit for open-weight LLM post-training, covering efficient fine-tuning, experimentation, and deployment.

## Academic / Open Research

### Alignment, RLHF, and Preference Optimization
- [**GROW: Aligning GRPO with State-Action Modeling for Open-World VLM Agents**](https://arxiv.org/abs/2605.20246) — Adapts GRPO to open-world VLM agents by modeling state-action trajectories, reducing reliance on expert SFT demos.
- [**FBOS-RL: Feedback-Driven Bi-Objective Synergistic Reinforcement Learning**](https://arxiv.org/abs/2605.20256) — Bi-objective RL framework aimed at making GRPO-style alignment more stable when supervised targets are sparse.
- [**Spectral Souping: A Unified Framework for Online Preference Alignment**](https://arxiv.org/abs/2605.20408) — Online preference alignment framework for diverse and conflicting user preferences.
- [**Complementing reinforcement learning with SFT through logit averaging in the post training of LLMs**](https://arxiv.org/abs/2605.20555) — Hybrid RL+SFT recipe that blends frozen SFT/reference logits with a trainable policy.
- [**Distributed Direct Preference Optimization**](https://arxiv.org/abs/2605.20696) — Extends DPO to decentralized settings with fragmented user preference data.
- [**AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback**](https://arxiv.org/abs/2605.20722) — Replaces fixed GRPO clipping and temperature with adaptive controls to reduce brittleness in reasoning RL.
- [**PREFINE: Preference-Based Implicit Reward and Cost Fine-Tuning for Safety Alignment**](https://arxiv.org/abs/2605.21225) — Adds safety-aware cost preferences to reward-optimized policies without numeric cost labels or full retraining.
- [**How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR**](https://arxiv.org/abs/2605.21266) — Uses a limited set of informative online rollouts to bootstrap cheaper offline preference optimization.
- [**Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment**](https://arxiv.org/abs/2605.20834) — Argues DPO is only conditionally equivalent to RLHF and maps failure modes.
- [**Bayesian Preference Learning for Test-Time Steerable Reward Models**](https://arxiv.org/abs/2602.08819) — Makes reward models steerable at inference time as objectives change.
- [**Linear-DPO: Linear Direct Preference Optimization for Diffusion and Flow-Matching Generative Models**](https://arxiv.org/abs/2605.21123) — Extends DPO-style alignment to diffusion and flow-matching generative systems.
- [**LamPO: A Lambda Style Policy Optimization for Reasoning Language Models**](https://arxiv.org/abs/2605.21235) — RLVR objective that preserves finer-grained signal than GRPO for reasoning-heavy tasks.

### Safety, Robustness, and Evaluation
- [**It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs**](https://arxiv.org/abs/2605.20258) — Uses self-distillation to improve privacy-norm adherence under contextual integrity.
- [**REFLECTOR: Internalizing Step-wise Reflection against Indirect Jailbreak**](https://arxiv.org/abs/2605.20654) — Two-stage training that teaches internal stepwise reflection to resist indirect jailbreaks.
- [**Towards Context-Invariant Safety Alignment for Large Language Models**](https://arxiv.org/abs/2605.20994) — Pushes safety tuning toward underlying harmful intent rather than prompt wording.
- [**Do No Harm? Hallucination and Actor-Level Abuse in Web-Deployed Medical Large Language Models**](https://arxiv.org/abs/2605.20591) — Audit of medical LLM deployments finds hallucination, policy, and abuse risks in practice.
- [**EvalMORAAL: Interpretable Chain-of-Thought and LLM-as-Judge Evaluation for Moral Alignment in Large Language Models**](https://arxiv.org/abs/2510.05942) — Moral-alignment evaluation stack combining interpretable CoT, log-probs, direct ratings, and LLM judges.
- [**When Reasoning Supervision Hurts**](https://arxiv.org/abs/2605.20364) — Finds explicit reasoning supervision can degrade creativity-oriented generation quality.
- [**Do as I Say, Not as I Do**](https://arxiv.org/abs/2605.20382) — Shows repeated in-context patterns can override explicit user instructions.
- [**Stage-Audit**](https://arxiv.org/abs/2605.20478) — Makes source-frontier discovery more auditable for grounded tables, citation quality, and RAG trust.
- [**MTR-Suite**](https://arxiv.org/abs/2605.20729) — Framework to audit and synthesize conversational retrieval benchmarks more realistically.

### Fine-Tuning, PEFT, Distillation, and Capability Retention
- [**Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages**](https://arxiv.org/abs/2605.20285) — Feeds later-stage training signals back into earlier stages to improve pipeline efficiency.
- [**Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining**](https://arxiv.org/abs/2605.20296) — Post-hoc repair method for catastrophic forgetting using only base and fine-tuned checkpoints.
- [**Consistently Informative Soft-Label Temperature for Knowledge Distillation**](https://arxiv.org/abs/2605.20357) — Revisits KD temperature scaling to improve teacher-to-student transfer.
- [**SMoA: Spectrum Modulation Adapter for Parameter-Efficient Fine-Tuning**](https://arxiv.org/abs/2605.21147) — PEFT adapter designed to overcome low-rank bottlenecks in LoRA-style tuning.
- [**Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning**](https://arxiv.org/abs/2605.21422) — Uses influence functions plus preference-aware weighting to select higher-value training data.
- [**Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning**](https://arxiv.org/abs/2605.20201) — Trains on shorter proxy contexts that preserve reasoning structure, reducing long-context training cost.
- [**Federated LoRA Fine-Tuning for LLMs via Collaborative Alignment**](https://arxiv.org/abs/2605.21217) — Parameter-efficient collaborative fine-tuning across heterogeneous clients without full-model sharing.
- [**SHINE: A Scalable In-Context Hypernetwork for Mapping Context to LoRA in a Single Pass**](https://arxiv.org/abs/2602.06358) — Generates LoRA adapters from context in one pass for faster specialization.
- [**Distributional Alignment as a Criterion for Designing Task Vectors in In-Context Learning**](https://arxiv.org/abs/2605.20730) — Uses compact task vectors as a lower-cost alternative to long in-context demonstrations.
- [**DiM³: Bridging Multilingual and Multimodal Models via Direction- and Magnitude-Aware Merging**](https://arxiv.org/abs/2605.12960) — Training-free merge method for extending multimodal models to new languages.

### Agents, Systems, and Memory
- [**Frontier: Towards Comprehensive and Accurate LLM Inference Simulation**](https://arxiv.org/abs/2605.21312) — Serving simulator covering disaggregation, parallelism, optimizations, and stateful workloads like reasoning/RL rollouts.
- [**MemGym: a Long-Horizon Memory Environment for LLM Agents**](https://arxiv.org/abs/2605.20833) — Benchmark focused on dynamic memory formation during long agent runs.
- [**Terminal-World: Scaling Terminal-Agent Environments via Agent Skills**](https://arxiv.org/abs/2605.20876) — Skill-based environment to expand higher-quality terminal-agent training data.
- [**Auto-Dreamer**](https://arxiv.org/abs/2605.20616) — Offline memory consolidation for language agents via later “dreaming” over prior experience.

### Multimodal, Speech, Voice, and Specialized Domains
- [**Enhancing Speech Large Language Models through Reinforced Behavior Alignment**](https://arxiv.org/abs/2509.03526) — RL-based alignment to reduce speech/text modality mismatch in SpeechLMs.
- [**FlowLM: Few-Step Language Modeling via Diffusion-to-Flow Adaptation**](https://arxiv.org/abs/2605.20199) — Converts diffusion LMs into flow-matching models for few-step generation with efficient fine-tuning.
- [**AFD-INSTRUCTION: A Comprehensive Antibody Instruction Dataset with Functional Annotations for LLM-Based Understanding and Design**](https://arxiv.org/abs/2602.04916) — Instruction-tuning dataset for antibody understanding and design.
- [**The Silent Thought**](https://arxiv.org/abs/2603.17837) — Adds latent reasoning to full-duplex spoken dialogue systems so they can “think while listening.”

## Key Takeaways
- **Preference optimization is fragmenting into many variants**: adaptive GRPO replacements, hybrid RL+SFT recipes, decentralized/federated alignment, offline-online mixes, and steerable reward models.
- **Efficiency is the clearest cross-cutting theme**: proxy-context tuning, smarter data selection, PEFT beyond vanilla LoRA, model merging, compact task vectors, and post-hoc capability recovery all aim to cut retraining cost.
- **Safety work is shifting from surface refusals to robustness**: context-invariant safety, indirect jailbreak defenses, privacy norms, medical deployment audits, and better moral/RAG evaluation all reflect deeper failure-mode coverage.
- **Agents are now bottlenecked by systems and memory tooling as much as model quality**: serving simulators, long-horizon memory benchmarks, terminal environments, and offline memory consolidation are becoming core infrastructure.
- **Post-training is broadening beyond text-only chat**: VLM agents, speech models, full-duplex voice systems, multilingual multimodal merging, and biotech datasets show where adaptation work is expanding next.