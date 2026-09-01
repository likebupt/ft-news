# Weekly Digest

## Academia / Open Research
- [Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models](https://arxiv.org/abs/2601.14758) — Examines whether AR→masked-diffusion post-training creates a real generation-mechanism shift or mostly preserves autoregressive behavior.
- [Least but not Last: Fine-tuning Intermediate Principal Components for Better Performance-Forgetting Trade-Offs](https://arxiv.org/abs/2602.03493) — Argues LoRA-style adaptation should target intermediate principal components to improve downstream gains while reducing forgetting.
- [Constrained Group Relative Policy Optimization](https://arxiv.org/abs/2602.05863) — Extends GRPO to settings with explicit safety or operational constraints, aiming to keep critic-free simplicity with better controllability.
- [Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment](https://arxiv.org/abs/2603.10009) — Adapts GRPO for heterogeneous user preferences, pointing toward segment-specific or personalized alignment.
- [OISD: On-Policy Internal Self-Distillation of Language Models](https://arxiv.org/abs/2605.29089) — Uses the model’s own internal predictive signals during RL post-training to provide richer, more sample-efficient learning signals.
- [Bayesian Sparse Low-Rank Adaptation for Large Language Model Uncertainty Estimation](https://arxiv.org/abs/2607.02182) — Combines Bayesian uncertainty modeling with sparse low-rank adaptation to improve calibration after fine-tuning.
- **Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space** — Finds RL with verifiable rewards can improve pass@1 while shrinking the reachable solution space, potentially reducing gains from test-time scaling and diverse sampling. *(Source link was incomplete.)*
- **A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training** — Suggests limited teacher intervention during on-policy rollouts can produce better agent-training data than relying only on static demonstrations. *(Source link was incomplete.)*
- **XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals** — Proposes an explainable metric for data-to-text alignment designed to produce more actionable feedback signals for evaluation and debugging. *(Source link was not included in the source.)*

## Key Takeaways
- Post-training research is heavily focused on RL-based methods, with new work on constraints, personalization, self-distillation, and teacher-assisted data generation.
- Several papers highlight a trade-off between raw performance gains and other goals such as diversity, controllability, calibration, and forgetting.
- Parameter-efficient adaptation remains active, especially for preserving base-model capabilities and improving uncertainty estimation.
- Evaluation and interpretability are also getting attention, from mechanism-level analyses of diffusion post-training to more actionable data-to-text alignment metrics.