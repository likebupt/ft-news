# Weekly Digest

*No company-specific announcements were captured in these batches; all identifiable items fell under academic/open research.*

## Academia / Open Research

- **What Should SFT Learn? Conditional Information Gain for Generalizable Post-Training** — Proposes **Conditional Information Gain (CIG)** as a criterion for what supervised fine-tuning should teach, aiming for **generalization beyond demonstration imitation**. [Read more](https://arxiv.org/abs/2610.12995)
- **EmoGavel: Grounding-Aware Reinforcement Learning with Verifiable Rewards for Multimodal Emotion Preference Learning** — Introduces **grounding-aware RL** with **verifiable rewards** so multimodal preference learning is tied more closely to input evidence, not just human preference signals. [Read more](https://arxiv.org/abs/2610.13353)
- **PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents** — Uses **privileged traces during post-training** to improve **multi-turn tool use, long-horizon reasoning, and cross-turn adaptation**, positioned as a more stable alternative to pure RL-heavy setups. [Read more](https://arxiv.org/abs/2606.16215)

## Notes on partially captured items
Some source entries were truncated and couldn’t be merged reliably with full links/titles, including references to:
- **Evo²**
- **Sample-Adaptive Zeroth...**
- **Unsupervised Multimodal Reward Modeling**

## Key Takeaways

- **Post-training remains the center of gravity**: this week’s research focused more on **how models should be trained after pretraining** than on base-model scaling.
- **Generalization over imitation** is a recurring theme, especially in work on **SFT objectives** and **data/skill selection**.
- **Reward modeling is getting more grounded**: papers are pushing toward **verifiable, evidence-linked rewards** rather than purely preference-based supervision.
- **Agent training is shifting toward hybrid methods**: approaches like **PACT** suggest teams are looking for ways to improve tool-use agents **without relying solely on brittle RL pipelines**.
- **Multimodal alignment is broadening** beyond captioning or VLM benchmarks into **emotion, preference learning, and reward construction**.