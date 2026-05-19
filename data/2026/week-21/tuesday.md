# Final Weekly Digest: Fine-Tuning & Post-Training

*Most items had no stated company affiliation, so they’re grouped under **Academic / Open Research**.*

## Academic / Open Research

### Adaptation, PEFT & knowledge injection
- **Goal-Conditioned Supervised Learning for LLM Fine-Tuning** — Offline fine-tuning conditioned on desired outcomes to capture some RL-style alignment benefits without reward models or online rollouts. [Paper](https://arxiv.org/abs/2605.16345)
- **Strategic Over-Parameterization for Generalizable Low-Rank Adaptation** — Adds targeted capacity inside LoRA-style PEFT to recover expressivity and generalization at low rank. [Paper](https://arxiv.org/abs/2605.16470)
- **FIM-LoRA** — Uses calibration-time gradient variance to allocate LoRA rank where the task appears to need it most. [Paper](https://arxiv.org/abs/2605.16800)
- **DP-SelFT** — Differentially private selective fine-tuning to improve the privacy/utility trade-off on sensitive data. [Paper](https://arxiv.org/abs/2605.17432)
- **MixSD** — Mixed contextual self-distillation for knowledge injection with less reasoning/generalization regression. [Paper](https://arxiv.org/abs/2605.16865)
- **Internalizing Tool Knowledge in Small Language Models via QLoRA Fine-Tuning** — Fine-tunes tool schemas into small models to reduce prompt overhead in agent settings. [Paper](https://arxiv.org/abs/2605.17774)
- **Beyond LoRA vs. Full Fine-Tuning: Gradient-Guided Optimizer Routing for LLM Adaptation** — Routes updates between low-rank and full optimization instead of choosing one globally. [Paper](https://arxiv.org/abs/2605.07111)
- **Learning Faster with Better Tokens** — Parameter-efficient vocabulary adaptation to address tokenization mismatch in specialized summarization. [Paper](https://arxiv.org/abs/2605.17379)
- **A Data-Efficient Path to Multilingual LLMs** — Expands languages via post-training parameter deltas integrated into upcycled MoE models, avoiding costly continued pretraining. [Paper](https://arxiv.org/abs/2605.18083)

### Alignment, RL & distillation
- **Decoupling KL and Trajectories** — Separates prefix source and KL direction to unify SFT, DAgger, offline RL, and on-policy distillation. [Paper](https://arxiv.org/abs/2605.16826)
- **Learning-Zone Energy** — Dynamically selects prompts during RL post-training so compute is spent on examples the model is ready to learn from. [Paper](https://arxiv.org/abs/2605.17003)
- **DISA** — Uses offline importance sampling for distribution-matching RL to avoid mode collapse and preserve multiple valid reasoning paths. [Paper](https://arxiv.org/abs/2605.17295)
- **ClaHF** — Applies human-feedback-style RL to classification, aiming for better decision boundaries and calibration than plain labels. [Paper](https://arxiv.org/abs/2605.17458)
- **Beyond Inference-Time Search** — Uses RL to synthesize reusable solvers so reasoning cost shifts from decoding into model weights. [Paper](https://arxiv.org/abs/2605.18374)
- **General Preference Reinforcement Learning** — Unifies verifier-based RL and preference optimization into a broader post-training framework. [Paper](https://arxiv.org/abs/2605.18721)
- **CPMobius** — Data-free coach-player RL loop for reasoning improvement without curated SFT/RL datasets. [Paper](https://arxiv.org/abs/2602.02979)
- **Weak-to-Strong Elicitation via Mismatched Wrong Drafts** — Shows even incorrect drafts from weaker models can help stronger learners improve. [Paper](https://arxiv.org/abs/2605.17314)
- **Transitivity Meets Cyclicity** — Decomposes transitive and cyclic preferences to model richer human alignment signals than scalar rewards alone. [Paper](https://arxiv.org/abs/2605.17342)
- **Reinforcement Learning for LLM Post-Training: A Survey** — Broad survey of RLHF, DPO, GRPO, safety, reasoning, math, and coding post-training. [Paper](https://arxiv.org/abs/2407.16216)

### Multimodal, multilingual & task-specific systems
- **HPC-LLM** — Combines domain adaptation and RAG for HPC support across clusters, schedulers, GPUs, and parallel frameworks. [Paper](https://arxiv.org/abs/2605.16347)
- **Multilingual OCR-Aware Fine-Tuning and Prompt-Guided CoT for Multimodal LLMs** — OCR-aware multilingual post-training for cluttered, blurry, real-world text understanding. [Paper](https://arxiv.org/abs/2605.16409)
- **AutoRubric-T2I** — Rule-based reward model for text-to-image alignment as a cheaper alternative to large preference models. [Paper](https://arxiv.org/abs/2605.17602)
- **OProver** — Unified framework for agentic Lean 4 theorem proving that iteratively improves failed proof attempts. [Paper](https://arxiv.org/abs/2605.17283)
- **AMATA** — Multi-agent trajectory alignment to reduce hallucinations in knowledge-intensive QA. [Paper](https://arxiv.org/abs/2605.17352)
- **HEED** — Density-weighted residual alignment for distilling a VLM into a Mamba/attention hybrid while better handling hard examples. [Paper](https://arxiv.org/abs/2605.17093)
- **Toward Robust Multilingual Adaptation of LLMs for Low-Resource Languages** — LiRA targets low-resource adaptation under data scarcity, translation noise, and unstable cross-lingual alignment. [Paper](https://arxiv.org/abs/2510.14466)
- **PEGRL** — Post-editing-guided RL for machine translation to improve stability versus noisy GRPO-style training. [Paper](https://arxiv.org/abs/2602.03352)

### Robustness, evaluation & deployment
- **Where Pretraining writes and Alignment reads** — Finds alignment may act more through readout directions than broad representation rewrites. [Paper](https://arxiv.org/abs/2605.16600)
- **Why Do Reasoning Models Lose Coverage?** — Explains why reasoning fine-tuning can improve pass@1 while hurting pass@k by reducing answer diversity. [Paper](https://arxiv.org/abs/2605.17026)
- **FedSDR** — Federated self-distillation with rectification to handle client heterogeneity in federated LLM fine-tuning. [Paper](https://arxiv.org/abs/2605.18028)
- **Alignment Dynamics in LLM Fine-Tuning** — Studies why alignment gained through SFT/RLHF often degrades during later fine-tuning. [Paper](https://arxiv.org/abs/2605.18309)
- **Evaluation Drift in LLM Personality Induction** — Argues some reported gains may reflect shifting evaluation criteria rather than stable behavior changes. [Paper](https://arxiv.org/abs/2605.16996)
- **Red-Bandit** — Test-time red-teaming with bandit-guided LoRA experts to adapt attacks to model-specific failure modes. [Paper](https://arxiv.org/abs/2510.07239)
- **Self-Distilled Trajectory-Aware Boltzmann Modeling** — Aligns diffusion language model training with actual inference trajectories. [Paper](https://arxiv.org/abs/2605.11854)
- **E-PMQ** — Post-merge quantization with merged-weight anchoring to preserve quality after expert/model merging. [Paper](https://arxiv.org/abs/2605.16882)

## Google ecosystem
- **CRAC 2026 multilingual coreference on Gemma-3-27B** — Two-stage fine-tuning ranked **1st in the LLM track** and **3rd overall** with **74.32 average CoNLL F1**. [Paper](https://arxiv.org/abs/2605.16984)

## Alibaba / NVIDIA ecosystem
- **Mixture of Experts for Low-Resource LLMs** — Analyzes expert routing in **Qwen3-30B-A3B** and **Nemotron-3-Nano-30B-A3B** for Hebrew, with implications for low-resource multilingual MoE adaptation. [Paper](https://arxiv.org/abs/2605.17598)

## Key Takeaways
- **Adaptive post-training is accelerating**: rank allocation, routed optimizers, selective/private tuning, tokenization fixes, and parameter-delta integration all aim to beat one-size-fits-all PEFT.
- **RL work is shifting toward reusable capability**: many papers try to internalize reasoning into weights, reduce rollout waste, and preserve answer diversity rather than only optimizing pass@1.
- **Alignment fragility is now a core research problem**: continued fine-tuning, federated setups, cyclic preferences, and evaluation drift all show how easily aligned behavior can degrade.
- **Deployment practicality broadened this week**: post-merge quantization, domain RAG, tool-schema internalization, OCR-aware tuning, and cheaper reward models all target production constraints.
- **Multilingual and multimodal adaptation remain major frontiers**: low-resource languages, OCR-heavy inputs, multilingual coreference, MoE routing, and MT continue to get specialized post-training recipes.