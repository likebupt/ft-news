# Final Weekly Digest

*No company attributions were included in the source summaries, so items are grouped under **Academic Research (arXiv)**.*

## Academic Research (arXiv)

- **Auditability Is Not One Property: Rule Overlap, Behavioural Agreement, and Composition in Reinforcement Learning** — Argues RL auditability should be decomposed into **rule overlap**, **behavioral agreement**, and **composition**, warning that logs/checkpoints alone may not reveal the learned policy. [Read more](https://arxiv.org/abs/2609.28581)

- **LastOPD: Taming Collapse in Latent On-Policy Distillation** — Proposes latent-level on-policy distillation to better preserve post-RL behavior and reduce collapse versus next-token-only matching. [Read more](https://arxiv.org/abs/2609.28845)

- **Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD** — Improves Direct-OPD by supervising only the most informative tokens, aiming to transfer RL gains between models more sample-efficiently. *(Link not provided in source)*

- **TraceGuard: Adaptive Multimodal Poison Filtering through Cross-Feature Rank Agreement** — Introduces an adaptive filter for image-text poisoning that uses cross-feature rank agreement to catch stealthy but plausible poisoned pairs. [Read more](https://arxiv.org/abs/2609.29099)

- **Post-Training Leaves Behavioral Shadows on Unrelated Decisions** — Finds that post-training can alter behavior in unrelated settings, suggesting SFT/RLHF effects may extend beyond target benchmarks. [Read more](https://arxiv.org/abs/2609.29233)

- **Transcript-Supervised Post-Training of Generative Speech Enhancement on Real Recordings via Reinforce Adjoint Matching** — Explores transcript-supervised post-training for generative speech enhancement on real recordings using Reinforce Adjoint Matching. *(Link not provided in source)*

## Key Takeaways

- **Post-training is the dominant theme:** several papers focus on how RL/SFT updates are transferred, audited, or preserved.
- **Behavioral evaluation needs to broaden:** post-training may affect unrelated decisions, not just benchmarked tasks.
- **Distillation is getting more selective and structured:** latent supervision and token selection both aim to preserve RL improvements more faithfully.
- **Data quality remains a core risk:** multimodal poisoning defenses are advancing as training pipelines become more complex.
- **Post-training techniques are spreading beyond text:** speech enhancement is emerging as another active application area.