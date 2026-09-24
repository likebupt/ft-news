# Weekly Digest

*No company affiliations were included in the source notes, so all items are grouped under **Open Research / Academic**.*

## Open Research / Academic (arXiv)

### Fine-Tuning, Continual Learning & PEFT
- [**Parameter Importance-Driven Continual Learning for Foundation Models**](https://arxiv.org/abs/2511.15375) — Continual post-training method that uses parameter-importance estimates to reduce catastrophic forgetting during domain adaptation while preserving general reasoning.
- [**LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights**](https://arxiv.org/abs/2602.17510) — PEFT approach that shares structure across layers with a frozen Tucker decomposition, aiming to improve efficiency over standard per-layer LoRA.
- [**Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs**](https://arxiv.org/abs/2609.27262) — Evaluates when a single multitask-adapted model can replace multiple task-specific fine-tunes across customer-support tasks like intent classification, QA, summarization, and tool-use decisions.

### RL / Agent Post-Training
- [**Reinforcement Learning with Decomposed Subtasks**](https://arxiv.org/abs/2609.27035) — Proposes breaking multi-turn agent rollouts into subtasks for finer-grained credit assignment, a potential improvement over single scalar trajectory rewards in GRPO-style post-training; especially relevant for tool use, planning, and long-horizon workflows.

### Evaluation / Verification
- **What Changes When Fact-Verification Scores Improve? Evidence and Answer Accounting Across Trained Verifiers and LLMs** — Examines whether fact-verification gains come from better answers, better evidence retrieval, or both, using FEVEROUS and comparisons across trained verifiers and LLMs. *(Link was not included in the source notes.)*

## Key Takeaways
- Post-training research is pushing toward **more targeted adaptation**: reducing forgetting, sharing adapter structure across layers, and improving RL credit assignment.
- PEFT work is moving beyond vanilla LoRA toward **cross-layer and structured factorization methods** to get more from limited trainable parameters.
- Applied fine-tuning decisions are becoming more operational: teams are asking whether **one multitask model or many specialized models** is the better production strategy.
- Evaluation research is probing whether benchmark gains reflect **real evidence-grounded improvement**, not just higher aggregate scores.