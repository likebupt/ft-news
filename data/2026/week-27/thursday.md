# Final Weekly Digest
*No company affiliations were included in the source snippets, so items are grouped under Research / Academia.*

## Research / Academia

- **[EPC: A Standardized Protocol for Measuring Evaluator Preference Dynamics in LLM Agent Systems](https://arxiv.org/abs/2607.00297)** — Introduces a protocol for measuring evaluator-preference coupling in iterative agent training loops; useful for RLHF, judge-model, and agent-eval pipelines.

- **[Prototype Language Models](https://arxiv.org/abs/2607.00510)** — Uses explicit prototypes to make it easier to trace which training examples drive outputs, improving auditability and correction in post-training workflows.

- **[Staleness-Learning Rate Scaling Laws for Asynchronous RLHF](https://arxiv.org/abs/2607.01083)** — Studies how rollout staleness affects async RLHF and proposes learning-rate scaling guidance to maintain stability at higher throughput.

- **[ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces](https://arxiv.org/abs/2607.01125)** — Proposes a more efficient zeroth-order fine-tuning method by selecting low-rank update subspaces from activation signals, reducing the cost of backprop-free tuning.

- **[Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search](https://arxiv.org/abs/2607.01144)** — Presents an online, feedback-driven search approach for training-free reward alignment, framing alignment as inference/search rather than weight updates.

- **Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training** — Suggests that much of RL adaptation may be captured by updating a single transformer layer, pointing to cheaper parameter-efficient RL post-training. *(No link provided in the source snippets.)*

- **ADAPT: Attention Dynamics Alignment with Preference Tuning for Faithful MLLMs** — Uses attention-dynamics alignment as an internal hallucination signal during multimodal preference tuning to improve faithfulness in MLLMs. *(No link provided in the source snippets.)*

## Key Takeaways

- **Efficiency is the dominant theme:** several papers aim to cut post-training cost via zeroth-order tuning, single-layer RL updates, or training-free search.
- **Feedback quality is under scrutiny:** EPC and async RLHF staleness work both focus on making iterative feedback loops more reliable and measurable.
- **Interpretability is moving into model design:** Prototype Language Models and ADAPT both use internal structure/signals to improve auditability or faithfulness.
- **Alignment is broadening beyond standard RLHF:** search-based alignment and multimodal faithfulness methods suggest a wider post-training toolkit is emerging.