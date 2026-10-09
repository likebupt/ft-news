# Weekly Digest

## Open Research / Academic
*No company affiliations were provided in the source summaries, so all items are grouped under open research.*

- **MoE router telemetry can leak membership information** — Monitoring/debugging data from MoE routing may reveal whether specific examples were in training, suggesting router logs need privacy protections similar to outputs and activations. [Read more](https://arxiv.org/abs/2610.10616)

- **On-policy distillation for looped language models** — Proposes dynamic cross-loop self-improvement for LoopLMs to strengthen multi-step reasoning while preserving parameter efficiency. [Read more](https://arxiv.org/abs/2610.10623)

- **Subliminal learning can transfer backdoors** — Distillation on semantically unrelated data may still pass along latent capabilities and hidden backdoors, raising supply-chain risks for student models. [Read more](https://arxiv.org/abs/2610.10657)

- **KDFP for principled LLM distillation** — Introduces a first-principles framework for knowledge distillation aimed at making student quality and compression trade-offs more predictable. [Read more](https://arxiv.org/abs/2610.10854)

- **RH-Detect standardizes reward-hacking detection** — A unified benchmark for reward-hacking detection that could make alignment and eval workflows more comparable across setups. [Read more](https://arxiv.org/abs/2610.10947)

- **Multilingual fine-tuning for pluralistic value alignment** — Shows a practical recipe for region-specific alignment/moderation across China, Indonesia, and Sri Lanka using multilingual fine-tuning plus threshold calibration. [Read more](https://arxiv.org/abs/2609.32382)

- **Latent-space reward modeling** — Compresses generative reward modeling into a semantics-preserving latent representation to reduce token-level inference costs while keeping evaluation quality high. [Read more](https://arxiv.org/abs/2610.09788)

- **Fine-tuned small models can beat prompted frontier models** — Reports that deployed fine-tuned small LMs outperform prompted frontier models on grammar concept annotation, reinforcing the quality/latency/cost case for task-specific tuning. [Read more](https://arxiv.org/abs/2610.10827)

## Key Takeaways
- **Distillation is a major theme**: multiple papers target cheaper or more reliable capability transfer, from LoopLM self-improvement to first-principles KD and latent-space reward modeling.
- **Safety risks are shifting toward infrastructure and transfer effects**: MoE telemetry leakage, subliminal backdoor transfer, and reward-hacking detection all point to post-training and deployment pipelines as active risk surfaces.
- **Practical post-training continues to matter**: multilingual alignment methods and fine-tuned small-model wins suggest targeted tuning can still outperform larger prompted systems in production settings.

*Note: one additional item in the provided source (“Stochastic teacher intervention for on-policy distillation”) was truncated before the summary/link, so it is not included here.*