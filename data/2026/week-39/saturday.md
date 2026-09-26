# Weekly Digest

_No notable company announcements emerged from these batches; the week was dominated by academic research._

## Academic Research / arXiv

- **[Wiring Beats Blending: Structure-Aware Compensation for Transformer Downscaling](https://arxiv.org/abs/2608.02829)** — Finds that converting a pretrained 1.4B model toward 410M works better when structural wiring is preserved, suggesting architecture-aware downscaling may outperform training small models from scratch.
- **[Beyond Forgetting: Diagnosing and Harnessing Shared Reasoning in Continual RLVR](https://arxiv.org/abs/2608.18574)** — Argues continual RLVR is not just about forgetting; some capabilities transfer as shared reasoning, which could reduce the cost of adding new tasks.
- **[Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning](https://arxiv.org/abs/2609.28581)** — Proposes treating RL auditability as multi-dimensional, since similar policies can score alike while relying on different learned rules.
- **[LastOPD: Taming Collapse in Latent On-Policy Distillation](https://arxiv.org/abs/2609.28845)** — Addresses OPD collapse by supervising latent reasoning signals, improving transfer of RL-refined behavior beyond next-token imitation.
- **[Let Training Guide Selection: Online Synthetic Data Filtering via Real-Anchored Utility](https://arxiv.org/abs/2609.29988)** — Filters synthetic data by training utility relative to a small real-data anchor set, rather than by realism alone.
- **[Forecast-Dojo: Replayable Environments for Benchmarking and Training LLM Forecasting Agents](https://arxiv.org/abs/2609.28876)** — Introduces replayable historical forecasting environments built from resolved markets and time-stamped news for leakage-resistant benchmarking.
- **[TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement](https://arxiv.org/abs/2609.29099)** — Targets stealthy poisoned image-text pairs that evade standard filters, with clear relevance for multimodal fine-tuning pipelines.
- **[Post-Training Leaves Behavioral Shadows on Unrelated Decisions](https://arxiv.org/abs/2609.29233)** — Shows post-training can shift behavior on unrelated tasks, highlighting hidden side effects that standard evals may miss.
- **[Transcript-Supervised Post-Training of Generative Speech Enhancement on Real Recordings via Reinforce Adjoint Matching](https://arxiv.org/abs/2609.29405)** — Uses transcript-based rewards to improve speech enhancement on real noisy recordings without requiring clean paired labels.
- **[TTLab at AlexandriaX-2026: A Fine-Tuned Surface Tagger for Arabic Machine-Translation Error-Span Detection and Classification](https://arxiv.org/abs/2609.29633)** — A more incremental result, but a useful example of targeted fine-tuning still working well on narrow structured NLP tasks.

## Key Takeaways

- **Post-training is becoming more about control than raw gains**: data filtering, poisoning defense, auditability, and behavioral spillover detection were recurring themes.
- **Structure-aware transfer is gaining traction**: both transformer downscaling and latent distillation papers suggest preserving internal structure matters more than naive output matching.
- **Weak supervision is increasingly practical**: small real-data anchors, transcript rewards, and replayable historical environments offer useful alternatives when gold labels are scarce.
- **Evaluation needs to get broader**: several papers warn that standard task metrics can miss hidden behavior changes, auditability gaps, or poisoning risks.
- **Continual adaptation remains a major opportunity**: work on continual RLVR suggests future systems may add capabilities more efficiently without full retraining.