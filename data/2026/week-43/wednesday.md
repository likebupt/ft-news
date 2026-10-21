# Weekly Digest

## Academic / Open Research

- [**EG-GRPO: Evidence-Guided Step-level Credit Assignment for Deep Search Agents**](https://arxiv.org/abs/2610.25269) — RL post-training method for LLM search agents that uses evidence-based **step-level credit assignment**, improving learning on **long-horizon search/reasoning** tasks.
- [**Where Groups Split: A Probe Prior for Nonzero Within-Group Variance in RL Post-Training**](https://arxiv.org/abs/2610.25325) — Identifies a **GRPO failure mode** with binary verifiers (zero within-group variance) and introduces a **probe prior** to recover learning signal when reward disagreement is sparse.
- [**Safety Offset Learning: When Benign Fine-Tuning Misaligns LLMs**](https://arxiv.org/abs/2610.25611) — Shows that even **benign fine-tuning** can weaken safety alignment, highlighting risk for teams doing domain adaptation or instruction tuning.
- [**OPDArena: Understanding Learning and Forgetting in On-Policy Distillation**](https://arxiv.org/abs/2610.25651) — Framework for studying **on-policy distillation**, with a focus on the trade-off between **learning gains and forgetting** during post-training.
- **NADS: Navigator-Guided Data Selection for Mitigating Catastrophic Forgetting in Fine-Tuning** — Proposes **navigator-guided synthetic data selection** to reduce catastrophic forgetting during fine-tuning. *(Link/details were cut off in the source excerpt.)*
- [**Residual-Guided Adaptive Tucker Rank Allocation for Parameter-Efficient MCI Conversion Prediction**](https://arxiv.org/abs/2610.25873) — PEFT method for 3D CNNs that allocates Tucker ranks **adaptively by residual signal** rather than uniformly, reinforcing the value of smarter **layer-wise adaptation budgets**.
- **Correctness-Dependent Asymmetric Target Distributions for Self-Distillation Policy Optimization** — Post-training/self-distillation approach that changes token-level targets based on **correctness**. *(Link/details were cut off in the source excerpt.)*

## Key Takeaways

- **Finer-grained post-training signals are a major theme**: step-level credit assignment, variance recovery in GRPO, and correctness-aware targets all aim to improve learning efficiency over coarse rewards.
- **Forgetting is now a first-class concern**: OPDArena and NADS both focus on retaining capabilities while adapting models.
- **Safety can drift during ordinary fine-tuning**: “benign” adaptation is not automatically safe and needs explicit evaluation.
- **Selective adaptation is gaining traction**: from data selection to adaptive rank allocation, newer methods try to spend limited tuning capacity where it matters most.

If you want, I can also turn this into a tighter **exec-style newsletter** or a **table format**.