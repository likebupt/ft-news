# Final Weekly Digest

## Academic Research / arXiv

- **Demystifying Reinforcement Learning Post-Training of Language Models** — Overview of why RL post-training boosts reasoning, math, and coding, and which design choices matter most in modern RLHF/RLAIF pipelines. [Read more](https://arxiv.org/abs/2608.24949)

- **Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach** — Proposes an RL fine-tuning method to reduce sycophancy and push models toward truthfulness over user-pleasing answers. [Read more](https://arxiv.org/abs/2608.25267)

- **Beyond Pairwise Feedback: Listwise Vision-Language Supervision for Preference-Based Reward Learning** — Replaces pairwise preference labels with listwise vision-language supervision for richer reward modeling. [Read more](https://arxiv.org/abs/2608.25350)

- **TailSFT: Filtered Fine-Tuning Improves Post-Training Performance** — Shows that stronger, filtered SFT can materially improve the model before RL post-training. [Read more](https://arxiv.org/abs/2608.25756)

- **Does Fine-Tuning Undo Activation Steering? Behavioural Recovery Without Weight-Edit Reversal** — Finds that behaviors introduced via steering can re-emerge after fine-tuning even when the underlying weight edits are not fully reversed. [Read more](https://arxiv.org/abs/2608.24988)

- **From Memorization to Absorption: Mixed-Policy RL for Continual Knowledge Injection** — Explores mixed-policy RL as an alternative to SFT for integrating new knowledge more durably. [Read more](https://arxiv.org/abs/2608.25243)

- **Learning New Facts with QLoRA: An Acquisition-Retention Frontier** — Shows adapter capacity strongly affects the tradeoff between learning new facts and preserving prior capabilities. [Read more](https://arxiv.org/abs/2608.25677)

- **Unfolding Scientific Papers into Multi-Turn Generation Trajectories for Continued Pre-Training** — Turns scientific papers into synthetic multi-turn generation trajectories to support continued pre-training beyond short-form web text. [Search on arXiv](https://arxiv.org/search/?query=Unfolding+Scientific+Papers+into+Multi-Turn+Generation+Trajectories+for+Continued+Pre-Training&searchtype=all)

## Key Takeaways

- **RL post-training remained the core theme**, especially for truthfulness, reward learning quality, and continual knowledge updating.
- **Setup before RL matters a lot**: filtered SFT, richer supervision, and adapter design all materially shape post-training outcomes.
- **Knowledge updates are still fragile**: fine-tuning, steering, and parameter-efficient updates can shift behavior in non-obvious ways.
- **Synthetic training data is expanding upstream**: multi-turn trajectories extracted from scientific papers point to new continued pre-training pipelines.