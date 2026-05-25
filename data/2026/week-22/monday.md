# Weekly Digest

_No company-specific announcements were included in these batches, so everything is grouped under **Academia / Open Research**._

## Academia / Open Research

### Fine-tuning, post-training & optimization
- **[FuRA: Full-Rank Parameter-Efficient Fine-Tuning with Spectral Preconditioning](https://arxiv.org/abs/2605.22869)** — Full-rank PEFT that uses spectral preconditioning to better preserve pretrained structure.
- **[Convex Optimization for Alignment and Preference Learning on a Single GPU](https://arxiv.org/abs/2605.23244)** — Recasts alignment/preference learning as a convex problem that can run on one GPU.
- **[Learnability-Informed Fine-Tuning of Diffusion Language Models](https://arxiv.org/abs/2605.22939)** — Shows vanilla SFT can hurt DLMs and proposes a learnability-aware tuning recipe.
- **[Beyond Log Likelihood: Probability-Based Objectives for Supervised Fine-Tuning across the Model Capability Continuum](https://arxiv.org/abs/2510.00526)** — Argues NLL is a weak default for capable models and proposes probability-based SFT objectives.
- **[Anytime Training with Schedule-Free Spectral Optimization](https://arxiv.org/abs/2605.23061)** — Schedule-free spectral optimizer aimed at changing token budgets and training horizons.
- **[Understanding and Improving Noisy Embedding Techniques in Instruction Finetuning](https://arxiv.org/abs/2605.23171)** — Analyzes why uniform embedding noise can outperform Gaussian noise in instruction tuning.
- **[Freeze Deep, Train Shallow: Interpretable Layer Allocation for Continued Pre-Training](https://arxiv.org/abs/2605.11416)** — Introduces LayerTracer to choose which layers to freeze or train during continued pretraining.
- **[Fine-Tuning Causal LLMs for Text Classification: Embedding-Based vs. Instruction-Based Approaches](https://arxiv.org/abs/2512.12677)** — Compares classification-head tuning versus instruction-style tuning under tight compute budgets.
- **[Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation](https://arxiv.org/abs/2605.15913)** — Uses segmentation plus distillation to make block attention more practical for long-context and RAG.
- **[Long-Context Reasoning Through Proxy-Based Chain-of-Thought Tuning](https://arxiv.org/abs/2605.20201)** — Trains on compact proxy contexts to transfer reasoning to much longer inputs.

### Alignment, RL & distillation
- **[OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2605.21851)** — Improves reasoning RL by assigning credit at the token level instead of across whole trajectories.
- **[LambdaPO: A Lambda Style Policy Optimization for Reasoning Language Models](https://arxiv.org/abs/2605.19416)** — Alternative to GRPO-style RL that aims to preserve more trajectory-level signal.
- **[Precise: SDE-Consistent Stochastic Sampling for RL Post-Training of Flow-Matching Models](https://arxiv.org/abs/2605.23522)** — Fixes the deterministic-to-stochastic mismatch in RL post-training for flow-matching generators.
- **[Learning Kernel-Based MDPs from Episodic Preferential Feedback](https://arxiv.org/abs/2605.23650)** — Theory-focused RLHF work on learning from pairwise preferences instead of scalar rewards.
- **[From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning](https://arxiv.org/abs/2605.23382)** — Pushes agentic RL toward user-specific preference rewards rather than generic correctness.
- **[Entropy-Aware On-Policy Distillation of Language Models](https://arxiv.org/abs/2603.07079)** — Distillation objective designed to better preserve teacher uncertainty on student-generated trajectories.
- **[Strong Teacher Not Needed? On Distillation in LLM Pretraining](https://arxiv.org/abs/2605.23857)** — Challenges the assumption that stronger teachers always produce better distilled students.
- **[Knowledge Distillation for Low-Resource Open-source Text-to-SQL Model](https://arxiv.org/abs/2605.22843)** — Uses distillation to improve open Text-to-SQL models when labeled data is scarce.
- **[InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion](https://arxiv.org/abs/2505.13893)** — Structure-aware logit distillation for fusing heterogeneous models without extra inference cost.
- **[What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA](https://arxiv.org/abs/2605.23067)** — Shows curriculum design strongly shapes the skills learned by RL memory agents.

### Training-free systems, steering & mechanistic studies
- **[Training-Free Looped Transformers](https://arxiv.org/abs/2605.23872)** — Adds recurrence-like behavior by looping a mid-stack block at inference time.
- **[Training-Free Multimodal Large Language Model Orchestration](https://arxiv.org/abs/2508.10016)** — Orchestrates off-the-shelf multimodal components without end-to-end retraining.
- **[Multilingual Steering by Design: Multilingual Sparse Autoencoders and Principled Layer Selection](https://arxiv.org/abs/2605.23036)** — Extends SAE-based steering beyond English with principled layer selection.
- **[As X, Do Y: How Persona and Task Combine in Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23147)** — Finds persona and task prompts act like partially orthogonal directions in instruction-tuned models.

### Safety, security & bias
- **[Test-Time Training Undermines Safety Guardrails](https://arxiv.org/abs/2605.22984)** — Shows inference-time adaptation can open a new jailbreak surface.
- **[PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23168)** — Demonstrates that a small poison set can implant attacker-chosen task behavior.
- **[The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems](https://arxiv.org/abs/2605.22842)** — Memory poisoning can look like model misalignment, confusing diagnosis in agent stacks.
- **[How Far Will They Go? Red-Teaming Online Influence with Large Language Models](https://arxiv.org/abs/2605.22880)** — Studies how open-source LLMs could support political influence operations.
- **[It’s the humans, not the data: Geopolitical bias in LLMs originates in post-training, amplified by the language of the prompt](https://arxiv.org/abs/2605.23825)** — Argues geopolitical bias is introduced mainly in post-training and amplified by prompt language.
- **[When AI Takes Sides on Questions of Faith: Persistent Asymmetries in AI-Mediated Faith Guidance](https://arxiv.org/abs/2605.22975)** — Finds asymmetric responses to mirrored religion-conversion prompts.
- **[Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs](https://arxiv.org/abs/2605.23157)** — Jailbreak vulnerability varies significantly by language and modality.

### Evaluation, grounding & benchmarks
- **[CapTrack: Multifaceted Evaluation of Forgetting in LLM Post-Training](https://arxiv.org/abs/2603.06610)** — Broader framework for measuring capability erosion after post-training.
- **[Graph Alignment Topology as an Inductive Bias for Grounding Detection](https://arxiv.org/abs/2605.22963)** — Detects whether generated propositions are actually grounded in source documents.
- **[BURMESE-SAN: Burmese NLP Benchmark for Evaluating Large Language Models](https://arxiv.org/abs/2602.18788)** — Adds a broad low-resource benchmark spanning seven Burmese NLP subtasks.
- **[Evaluating Large Language Models in a Complex Hidden Role Game](https://arxiv.org/abs/2605.22826)** — Uses *Secret Hitler* to test strategic reasoning, persuasion, and deception.
- **[Convergence Without Understanding: When Language Models Agree on Representations but Disagree on Reasoning](https://arxiv.org/abs/2605.23315)** — Similar representations do not guarantee similar reasoning processes.

## Key Takeaways
- Post-training work is moving past generic SFT/LoRA toward more structure-aware and stage-aware methods, including **[FuRA](https://arxiv.org/abs/2605.22869)**, **[Convex Optimization for Alignment](https://arxiv.org/abs/2605.23244)**, **[Beyond Log Likelihood](https://arxiv.org/abs/2510.00526)**, and **[LayerTracer](https://arxiv.org/abs/2605.11416)**.
- Alignment research is increasingly focused on better credit assignment and richer preference signals, with **[OPPO](https://arxiv.org/abs/2605.21851)**, **[LambdaPO](https://arxiv.org/abs/2605.19416)**, **[Learning from Preferential Feedback](https://arxiv.org/abs/2605.23650)**, and **[Personalized Agentic RL](https://arxiv.org/abs/2605.23382)** standing out.
- Safety risks are showing up in the adaptation and system stack, not just the base model: see **[Test-Time Training Undermines Safety Guardrails](https://arxiv.org/abs/2605.22984)**, **[PoisonForge](https://arxiv.org/abs/2605.23168)**, **[The Misattribution Gap](https://arxiv.org/abs/2605.22842)**, and **[Same Model, Different Weakness](https://arxiv.org/abs/2605.23157)**.
- Evaluation is broadening beyond benchmark accuracy to include forgetting, grounding, multilingual coverage, strategic behavior, and reasoning-process mismatch via **[CapTrack](https://arxiv.org/abs/2603.06610)**, **[Graph Alignment Topology](https://arxiv.org/abs/2605.22963)**, **[BURMESE-SAN](https://arxiv.org/abs/2602.18788)**, and **[Convergence Without Understanding](https://arxiv.org/abs/2605.23315)**.
- Low-cost capability upgrades remain a major theme, from **[Training-Free Looped Transformers](https://arxiv.org/abs/2605.23872)** and **[Training-Free Multimodal Orchestration](https://arxiv.org/abs/2508.10016)** to cheaper distillation and fusion approaches like **[Strong Teacher Not Needed?](https://arxiv.org/abs/2605.23857)** and **[InfiGFusion](https://arxiv.org/abs/2505.13893)**.