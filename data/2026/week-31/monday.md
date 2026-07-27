# Final Weekly Digest

## Academia / arXiv

- **On the Convergence of Stochastic Low-Rank Adaptation** — A theory paper on when stochastic optimization of LoRA’s bilinear factors converges, helping clarify PEFT stability and optimization behavior. [Read more](https://arxiv.org/abs/2607.21975)
- **IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning** — Allocates a fixed LoRA rank budget across Transformer layers based on topology instead of uniform rank, aiming for better quality at the same parameter budget. [Read more](https://arxiv.org/abs/2607.22251)
- **κ-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating** — Uses condition-number signals to decide which LoRA matrices are worth training, with the goal of cutting unnecessary compute while preserving performance. [Read more](https://arxiv.org/abs/2607.22489)
- **Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step Procedures** — Argues LoRA is effective for style/factual adaptation but struggles to internalize multi-step procedural knowledge, suggesting a structural limitation of low-rank adaptation. [Search arXiv](https://arxiv.org/search/?query=Procedural+Knowledge+Is+Not+Low-Rank%3A+Why+LoRA+Fails+to+Internalize+Multi-Step+Procedures&searchtype=all&abstracts=show&order=-announced_date_first&size=50)
- **What Matters When Building Universal Multilingual Named Entity Recognition Models?** — Studies which factors actually drive universal multilingual NER performance, comparing multilingual backbones, task architectures, loss design, and large-scale training choices. [Read more](https://arxiv.org/abs/2601.06347)

## Key Takeaways

- **LoRA/PEFT was the dominant research theme**, with new work spanning theory, rank allocation, and selective parameter updates.
- **Efficiency is becoming more targeted**: multiple papers focus on where low-rank capacity should go and which matrices are worth updating at all.
- **LoRA’s limits are getting clearer**: one paper argues low-rank adaptation may be structurally weak for multi-step procedural knowledge.
- **For multilingual NER, system-level choices matter**: backbone selection, training setup, and scaling decisions may matter as much as architecture tweaks.