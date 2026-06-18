## Weekly Digest

*Note: one source item was truncated in the partials, so only fully recoverable entries are included below.*

## NVIDIA
- **Cosmos 3: Omnimodal World Models for Physical AI** — NVIDIA introduced an **omnimodal world-model family** spanning **language, image, video, audio, and action** in one setup, pointing toward foundation models for **physical AI and robotics**. [Read more](https://arxiv.org/abs/2606.02800)

## Academic / Unspecified Research Teams
- **DRIFT: Refining Instruction Data via On-Policy Data Attribution** — Uses **on-policy data attribution** to improve the **distribution quality** of SFT instruction data, treating upstream data curation as a capability lever. [Read more](https://arxiv.org/abs/2606.18307)

- **LLMZero: Discovering Adaptive Training Strategies for RL Post-Training via LLM Agents** — Explores using **LLM agents** to discover **dataset-specific RL post-training strategies**, with implications for automating RLHF/RLVR recipe design. [Read more](https://arxiv.org/abs/2606.18388)

- **Reliable Neural-Codec Text-to-Speech by ASR Self-Verification and Distillation** — Tackles **catastrophic TTS failures** like silence and repetition using **ASR-based self-verification** plus **distillation**, aiming for near-zero failure rates. [Read more](https://arxiv.org/abs/2606.18323)

- **Beyond Safe Data: Pretraining-Stage Alignment with Regular Safety Reflection** — Argues safety should begin during **pretraining**, not only via data filtering or later post-training, by adding **regular safety reflection** earlier in the stack. [Read more](https://arxiv.org/abs/2606.19168)

- **From Memorization to Parameter Interference: How Overtraining Experts Harms Model Merging** — Finds that aggressive expert fine-tuning hurts merging not just through memorization, but through **parameter interference**, suggesting the need for **merge-aware tuning**. [Read more](https://arxiv.org/abs/2506.14126)

- **Task-Adaptive Parameter-Efficient Fine-Tuning for Weather Foundation Models** — Extends **PEFT** into **weather foundation models**, aiming to preserve performance while lowering adaptation cost in scientific modeling. [Read more](https://arxiv.org/abs/2509.22020)

- **Trust Region On-Policy Distillation** — Proposes a **trust-region formulation** for **on-policy distillation**, targeting more stable policy updates in post-training, agent learning, and compression. [Read more](https://arxiv.org/abs/2606.01249)

- **TLA-Prover: Verifiable TLA+ Specification Synthesis via Preference-Optimized Low-Rank Adaptation** — Applies **preference-optimized LoRA** to generate TLA+ specs that are more likely to pass **TLC verification**, highlighting post-training optimized for **formal correctness**. *(Link not included in the partial summaries.)*

- **ScholarSum** — Introduces a **student-teacher abstractive summarization** framework for scientific literature that combines **knowledge-graph reasoning** with **reflective refinement** to improve faithfulness. [Read more](https://arxiv.org/abs/2606.18850)

## Key Takeaways
- **Data curation and recipe discovery are becoming core training levers**: DRIFT focuses on better SFT data distributions, while LLMZero automates RL post-training strategy selection.
- **Reliability and verification are a major theme**: from TTS self-checking, to formally verifiable TLA+ synthesis, to faithfulness-focused scientific summarization.
- **Safety is shifting earlier in the pipeline**: alignment work is moving from post-training toward **pretraining-stage safety priors**.
- **Post-training is getting more stability-aware**: trust-region distillation and merge-interference analysis both point to more controlled optimization regimes.
- **Foundation-model methods are broadening beyond text**: PE