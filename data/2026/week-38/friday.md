# Weekly Digest

*No company affiliations were provided in the source summaries, so items are grouped under **Open Research / Academia**.*

## Open Research / Academia

### RL, Distillation, and Agent Training
- **Improving Online Reinforcement Learning via Bidirectional Behavior Prior Distillation** — proposes bidirectional behavior prior distillation to improve online RL sample efficiency and stabilize learning under critic error; relevant to LLM/agent post-training as a regularizer for on-policy updates. [Read more](https://arxiv.org/abs/2609.20268)
- **When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation** — finds that teacher/student EOS mismatch can cause length inflation in on-policy distillation, making EOS alignment a key training lever rather than a decoding detail. [Read more](https://arxiv.org/abs/2609.20511)
- **Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL** — argues that supervising observation tokens, not just action tokens, changes learned representations and downstream exploration behavior, making trajectory formatting an important post-training choice. [Read more](https://arxiv.org/abs/2609.20715)
- **Compositional Reasoning in Language Models under Reinforcement Learning Post-Training** — examines whether RL post-training improves true compositional generalization rather than only lifting benchmark performance. [Read more](https://arxiv.org/abs/2609.19465)
- **OPTED: On-Policy Fine-Tuning for End-to-End Driving using a Render-Free Teacher** —