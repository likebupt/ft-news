# Weekly Digest

Most items this week were research papers rather than product launches; only a few were clearly company-affiliated.

## Alibaba / Qwen

- [Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models](https://arxiv.org/abs/2605.11887) — Turns sparse autoencoder features into developer tooling for inspecting, controlling, and debugging LLM behavior.

## NVIDIA-linked Research

- [HEBATRON: A Hebrew-Specialized Open-Weight Mixture-of-Experts Language Model](https://arxiv.org/abs/2605.11255) — Builds a Hebrew-focused open-weight MoE on Nemotron-3 with curriculum training, anti-forgetting anchoring, and bilingual SFT.

## Research / Academia

### Post-training optimization, RLHF, and reward modeling

- [ξ-DPO: Direct Preference Optimization via Ratio Reward Margin](https://arxiv.org/abs/2605.10981) — Proposes a reference-free preference objective aimed at reducing SimPO-style hyperparameter brittleness.
- [Spurious Correlation Learning in Preference Optimization](https://arxiv.org/abs/2605.11134) — Explains why DPO-like methods pick up sycophancy/length bias and proposes tie training as a fix.
- [fg-expo](https://arxiv.org/abs/2605.11403) — Improves GRPO/RLVR for math reasoning with adaptive KL control and a Gaussian difficulty curriculum.
- [Evolutionary Task Discovery](https://arxiv.org/abs/2605.11666) — Synthesizes harder, more diverse reasoning tasks to reduce the RLVR data bottleneck.
- [GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation](https://arxiv.org/abs/2605.11853) — Uses self-distillation to create finer-grained rewards for agent RL credit assignment.
- [Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training](https://arxiv.org/abs/2605.12483) — Argues scarce verifiable data is often best used to induce denser rewards, not just supervise the final student directly.
- [Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting](https://arxiv.org/abs/2605.11538) — Targets GRPO instability from extreme tokens and poor exploration/exploitation balance.
- [Variance-aware Reward Modeling with Anchor Guidance](https://arxiv.org/abs/2605.11865) — Models reward mean plus variance to better handle disagreement and pluralistic preferences.
- [Understanding the Performance Gap in Preference Learning: A Dichotomy of RLHF and DPO](https://arxiv.org/abs/2505.19770) — Breaks the RLHF-vs-DPO gap into representation effects and finite-sample effects.
- [Learning Agentic Policy from Action Guidance](https://arxiv.org/abs/2605.12004) — Adds action guidance to help agentic RL explore tasks where the base model cannot reach reward states unaided.
- [Combining On-Policy Optimization and Distillation for Long-Context Reasoning in Large Language Models](https://arxiv.org/abs/2605.12227) — Mixes on-policy learning with distillation to improve long-context reasoning more stably than pure RL.
- [TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching](https://arxiv.org/abs/2605.12288) — Recasts preference learning at the token level instead of relying only on sequence-level objectives.
- [STAPO: Stabilizing Reinforcement Learning for LLMs by Silencing Rare Spurious Tokens](https://arxiv.org/abs/2602.15620) — Suppresses rare spurious tokens to reduce late-stage RL collapse.
- [RLearner-LLM: Balancing Logical Grounding and Fluency in Large Language Models via Hybrid Direct Preference Optimization](https://arxiv.org/abs/2605.04539) — Uses a hybrid preference setup to reduce verbosity bias and better reward correctness.
- [Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation](https://arxiv.org/abs/2605.11739) — Studies why on-policy distillation works so well, pointing to parameter-level learning dynamics rather than just denser supervision.
- [YFPO: A Preliminary Study of Yoked Feature Preference Optimization with Neuron-Guided Rewards for Mathematical Reasoning](https://arxiv.org/abs/2605.11906) — Injects neuron-guided internal signals into preference optimization for math reasoning.

### Fine-tuning, distillation, PEFT, and adaptation efficiency

- [Rotation-Preserving Supervised Fine-Tuning](https://arxiv.org/abs/2605.10973) — Frames OOD loss after SFT as singular-subspace rotation and proposes a cheaper rotation-preserving update.
- [Curriculum Learning-Guided Progressive Distillation in Large Language Models](https://arxiv.org/abs/2605.11260) — Combines curriculum learning with progressive distillation to better handle teacher–student capacity mismatch.
- [LOFT: Low-Rank Orthogonal Fine-Tuning via Task-Aware Support Selection](https://arxiv.org/abs/2605.11872) — Introduces an orthogonal PEFT method that separates where adaptation happens from how it is applied.
- [Not How Many, But Which: Parameter Placement in Low-Rank Adaptation](https://arxiv.org/abs/2605.12207) — Shows LoRA parameter placement matters much more under GRPO than under standard SFT.
- [Learning Adapter Rank via Symmetry Breaking](https://arxiv.org/abs/2506.22809) — Learns adapter rank via variational symmetry breaking instead of hand-picking LoRA rank.
- [Self-Distilled Trajectory-Aware Boltzmann Modeling: Bridging the Training-Inference Discrepancy in Diffusion Language Models](https://arxiv.org/abs/2605.11854) — Self-distills denoising trajectories to better match diffusion-LM training and inference.
- [Output Composability of QLoRA PEFT Modules for Plug-and-Play Attribute-Controlled Text Generation](https://arxiv.org/abs/2605.12345) — Tests whether separate QLoRA adapters can be composed instead of retraining for each attribute mix.
- [Freeze Deep, Train Shallow: Interpretable Layer Allocation for Continued Pre-Training](https://arxiv.org/abs/2605.11416) — Introduces LayerTracer and argues many CPT gains can come from updating shallower layers while freezing deeper ones.
- [A Study on Hidden Layer Distillation for Large Language Model Pre-Training](https://arxiv.org/abs/2605.11513) — Explores hidden-state distillation as a stronger transfer target than logits alone.
- [Probabilistic Calibration Is a Trainable Capability in Language Models](https://arxiv.org/abs/2605.11845) — Shows calibration can be directly improved through fine-tuning with synthetic randomness-aware prompts.
- [ReAD: Reinforcement-Guided Capability Distillation for Large Language Models](https://arxiv.org/abs/2605.11290) — Distills capabilities with reinforcement signals while modeling interactions across capabilities.

### Safety, interpretability, privacy, and evaluation

- [Persona-Conditioned Adversarial Prompting](https://arxiv.org/abs/2605.11730) — Broadens automated red-teaming by generating attacks from diverse personas and strategies.
- [Overtrained, Not Misaligned](https://arxiv.org/abs/2605.12199) — Argues many “emergent misalignment” results are better explained by overtraining dynamics.
- [Targeted Neuron Modulation via Contrastive Pair Search](https://arxiv.org/abs/2605.12290) — Uses contrastive neuron attribution to identify and modulate refusal-related neurons more cleanly than residual-stream steering.
- [Controllable User Simulation](https://arxiv.org/abs/2605.11519) — Formalizes controllable user simulators for conversational-agent evaluation in rare or counterfactual scenarios.
- [Reconstruction of Personally Identifiable Information from Supervised Finetuned Models](https://arxiv.org/abs/2605.12264) — Shows PII can be reconstructable from SFT models, highlighting privacy risk in instruction-tuning pipelines.
- [Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection](https://arxiv.org/abs/2602.07892) — Treats safety tuning as continual learning and uses orthogonal gradients to reduce utility loss.
- [SAGE: Scalable Automated Robustness Augmentation for LLM Knowledge Evaluation](https://arxiv.org/abs/2605.12022) — Automatically generates robustness variants for knowledge benchmarks to expose brittle performance.
- [How far can bias go? Tracing bias from pretraining data to alignment](https://arxiv.org/abs/2411.19240) — Tracks how gender-occupation bias survives from pretraining into aligned models.
- [One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue](https://arxiv.org/abs/2605.05630) — Targets attacks where malicious intent is distributed across otherwise benign dialogue turns.

### Multimodal, multilingual, speech, video, and specialized model training

- [OmniThoughtVis: A Scalable Distillation Pipeline for Deployable Multimodal Reasoning Models](https://arxiv.org/abs/2605.11629) — Distills multimodal chain-of-thought from large MLLMs into smaller deployable models.
- [Enhancing Multilingual Counterfactual Generation through Alignment-as-Preference Optimization](https://arxiv.org/abs/2605.11632) — Applies preference-style alignment to improve multilingual counterfactual explanations.
- [AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in UMMs via Decompositional Verifiable Reward](https://arxiv.org/abs/2605.12495) — Extends GRPO-style post-training to unified multimodal models without a separate cold-start stage.
- [Mind the Pause: Disfluency-Aware Objective Tuning for Multilingual Speech Correction with LLMs](https://arxiv.org/abs/2605.12242) — Tunes LLMs to better clean ASR transcripts with fillers, repetitions, and false starts.
- [READ: Recurrent Adapter with Partial Video-Language Alignment for Parameter-Efficient Transfer Learning in Low-Resource Video-Language Modeling](https://arxiv.org/abs/2312.06950) — Introduces recurrent adapters plus partial alignment for cheaper video-language transfer in low-resource settings.

## Key Takeaways

- Reward-efficient post-training dominated the week, with cleaner objectives and richer training signals emerging across [ξ-DPO](https://arxiv.org/abs/2605.10981), [sparse-to-dense rewards](https://arxiv.org/abs/2605.12483), [TokenRatio](https://arxiv.org/abs/2605.12288), and multiple GRPO variants.
- Fine-tuning is getting more surgical: [rotation-preserving SFT](https://arxiv.org/abs/2605.10973), [LOFT](https://arxiv.org/abs/2605.11872), [layer allocation for CPT](https://arxiv.org/abs/2605.11416), and [LoRA parameter placement](https://arxiv.org/abs/2605.12207) all focus on *where* and *how* to adapt, not just how much.
- Safety work is shifting from blunt alignment toward targeted control and better measurement, seen in [persona-conditioned red teaming](https://arxiv.org/abs/2605.11730), [neuron-level modulation](https://arxiv.org/abs/2605.12290), [continual-learning-aware safety tuning](https://arxiv.org/abs/2602.07892), and [PII reconstruction audits](https://arxiv.org/abs/2605.12264).
- Tooling and evaluation are maturing alongside optimization, with [Qwen-Scope](https://arxiv.org/abs/2605.11887), [controllable user simulation](https://arxiv.org/abs/2605.11519), and [SAGE](https://arxiv.org/abs/2605.12022) pushing toward more operational post-training workflows.
- Multimodal and deployment-oriented training is broadening fast, from [OmniThoughtVis](https://arxiv.org/abs/2605.11629) and [AlphaGRPO](https://arxiv.org/abs/2605.12495) to [READ](https://arxiv.org/abs/2312.06950) and [HEBATRON](https://arxiv.org/abs/2605.11255).
- Researchers are also treating behaviors once seen as emergent as directly trainable capabilities, including [probabilistic calibration](https://arxiv.org/abs/2605.11845), [multilingual counterfactual quality](https://arxiv.org/abs/2605.11632), and [speech disfluency handling](https://arxiv.org/abs/2605.12242).