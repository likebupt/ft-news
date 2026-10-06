# Weekly Digest

*No company names were provided in the source notes, so items are grouped under **Research / arXiv**.*

## Research / arXiv
- **Learning without Overwriting: A Theory of Self-Distillation and Supervised Fine-Tuning in Continual Reasoning** — Explains why on-policy self-distillation can improve reasoning while preserving prior capabilities better than standard SFT in continual-learning settings. [Read more](https://arxiv.org/abs/2610.05200)
- **Robust Parameter-Efficient LLM Adaptation on Analog Hardware** — Introduces PEFT methods designed for analog in-memory compute, improving resilience to hardware noise and analog non-idealities. [Read more](https://arxiv.org/abs/2610.05318)
- **Distributed Subliminal Learning: Replacing Model Updates with Random-Carrier Outputs** — Proposes collaborative adaptation via output-based communication over random carriers instead of sharing weights or adapters. [Read more](https://arxiv.org/search/?query=Distributed+Subliminal+Learning%3A+Replacing+Model+Updates+with+Random-Carrier+Outputs&searchtype=all&source=header)
- **PB-GRPO: Learning Socially Adaptive LLM Agents from Persona-Driven Simulation with Preference-Batched GRPO** — Uses persona-driven simulation and preference-batched GRPO to train more socially adaptive agents. [Read more](https://arxiv.org/abs/2610.04132)
- **Boundaries Agree, Labels Do Not: Intra-Annotator Dynamics as a Kind of Training Data** — Shows annotator disagreement patterns can be useful training signal, especially for interpretive labeling tasks. [Read more](https://arxiv.org/abs/2610.04370)
- **GlitchPatch: Repairing Glitch Tokens in Frozen Language Models via Local Retokenization** — Repairs anomalous “glitch tokens” in frozen models through local retokenization, without full retraining. [Read more](https://arxiv.org/abs/2610.04399)
- **From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents** — Evaluates whether strong offline probe metrics actually translate into useful deployment-time alarm policies. [Read more](https://arxiv.org/abs/2610.04575)
- **Scaling Verifiable Environments for Long-horizon Work Agents** — Builds scalable training and evaluation environments for workplace-style agents with verifiable outcomes. [Read more](https://arxiv.org/abs/2610.04906)
- **TrajLong: Co-Designing Agentic and Long-Context Supervision for Mid-Training** — Proposes mid-training that jointly improves agent trajectories and long-context reasoning. [Read more](https://arxiv.org/abs/2610.04973)
- **IREA: Intermediate Representation-based Embedding Alignment for Normative RAG** — Improves retrieval for ethical or judgment-heavy queries using intermediate-representation alignment. [Read more](https://arxiv.org/abs/2610.04974)
- **Small Agents with Semantic Search: Efficient Multilingual Code Localization** — Suggests compact specialized models can handle codebase file localization efficiently in multilingual settings. [Read more](https://arxiv.org/abs/2610.05099)
- **Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination** — Explores multi-agent coordination to improve long-horizon evidence gathering and synthesis. [Read more](https://arxiv.org/abs/2610.05382)

## Key Takeaways
- **Agent post-training is a major theme**: social adaptation, long-context supervision, long-horizon search, and work-agent evaluation all featured prominently.
- **Retention and efficient adaptation matter more**: self-distillation for continual reasoning, PEFT for analog hardware, and output-based distributed learning all target lower-cost model improvement.
- **Practical reliability is getting attention**: glitch-token repair, activation-monitor deployment validity, and better use of annotator disagreement aim to improve real-world robustness.
- **Modular and retrieval-centric systems keep gaining traction**: normative RAG, semantic code search, and coordinated small-agent setups point toward more composable AI stacks.