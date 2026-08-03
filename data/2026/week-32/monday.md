## Daily Briefing

### Academic / arXiv Research
- **MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification** — Proposes a PEFT-style mixture-of-experts approach for medical image classification, aiming to better handle clinical heterogeneity while avoiding the overfitting risks of full end-to-end fine-tuning. Relevant for multimodal/domain-specialized adaptation where data is fragmented or highly variable. [Read more](https://arxiv.org/abs/2607.29462)

- **GeoRA: Geometry-Aware Low-Rank Adaptation for RLVR** — Introduces a geometry-aware LoRA variant for reinforcement learning with verifiable rewards (RLVR), based on the premise that RLVR has different optimization dynamics than standard supervised fine-tuning. This is directly relevant to post-training for reasoning models. [Read more](https://arxiv.org/abs/2601.09361)

- **LightningRL: Breaking the Accuracy-Parallelism Trade-off of Block-wise dLLMs via Reinforcement Learning** — Applies reinforcement learning to block-wise diffusion LLMs, targeting the key trade-off between fast parallel generation and output quality. Notable as a post-training approach for alternative LLM architectures beyond autoregressive models. [Read more](https://arxiv.org/abs/2603.13319)

- **OpsLLM: Construction of Large Language Model for Software Operations with Multi-stage Learning** — Describes a domain-specific LLM for software operations built with a multi-stage learning pipeline, suggesting a practical recipe for verticalized post-training in enterprise/DevOps settings. Relevant for teams building specialized assistants from general base models. [Read more](https://arxiv.org/abs/2605.02906)

- **DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training** — Presents a self-improvement framework for reasoning LLMs that combines self-distillation with exploration and success-buffer training. The focus is stable post-training without external expert labels, which is highly relevant to scalable reasoning model improvement. [Read more](https://arxiv.org/abs/2606.30345)

- **TriShield: Zero-Utility-Loss Defense Against Privacy Backdoors in Federated Language Model Fine-Tuning via Orthogonal Gradient Projection and Optimizer State Entanglement** — Proposes a defense against privacy backdoors in federated LLM fine-tuning, using orthogonal gradient projection plus optimizer-state entanglement. Important for organizations exploring collaborative fine-tuning without centralizing sensitive data. [Read more](https