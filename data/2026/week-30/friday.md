# Weekly Digest

## Academic / Open Research (affiliations not specified)

- **Preference Tuning as Spectral Update Reorganization** — Recasts RLHF and related preference optimization through the *structure of the learned update*, using a spectral lens to explain what preference tuning changes and why it may improve some behaviors while degrading others. [arXiv](https://arxiv.org/abs/2607.20438)

- **Domyn-Small: A European 10B Reasoning Language Model** — Introduces **Domyn-Small**, a **10B open-weight reasoning model** released under the **MIT license**; notable for its permissive licensing, **9T-token** pretraining, and reasoning-focused post-training recipe. [arXiv](https://arxiv.org/abs/2607.20448)

- **MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems** — Proposes a **multi-objective** version of GRPO to reduce reward hacking, especially when reward models are unreliable and objectives cannot be safely collapsed into a single scalar reward. [arXiv](https://arxiv.org/abs/2509.22047)

- **Simple Policy Gradients for Reasoning with Diffusion Language Models** — Explores simple policy-gradient methods for improving reasoning in **diffusion language models**, highlighting post-training options beyond standard autoregressive setups. [Search](https://arxiv.org/search/?query=Simple+Policy+Gradients+for+Reasoning+with+Diffusion+Language+Models&searchtype=all)

- **From Evaluation to Optimisation: Hierarchy-Aware Training Signals for CWE Prediction in Python** — Extends taxonomy-aware **CWE** scoring from evaluation into training, so Python vulnerability models can learn from hierarchical “near-miss” predictions instead of treating all mistakes equally. [Search](https://arxiv.org/search/?query=From+Evaluation+to+Optimisation%3A+Hierarchy-Aware+Training+Signals+for+CWE+Prediction+in+Python&searchtype=all)

## Key Takeaways

- **Post-training is getting more interpretable:** spectral views of preference tuning could help teams understand why RLHF-style methods help some capabilities while harming others.
- **Open reasoning models remain active at mid-scale:** Domyn-Small stands out as a permissively licensed **10B** model with a substantial pretraining and reasoning post-training stack.
- **RLHF robustness is still a major theme:** MO-GRPO reflects continued work on reducing reward hacking by optimizing across multiple objectives rather than a single fragile reward.
- **Training recipes are broadening beyond standard LLMs:** new work is targeting both **diffusion language models** and **hierarchy-aware security modeling**, suggesting more task-specific and architecture-specific post-training methods.

*Note: search links were used where the partial summaries did not include a direct paper URL.*