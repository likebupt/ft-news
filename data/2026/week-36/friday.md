# Weekly Digest — Fine-Tuning / Post-Training

## Academic / arXiv

- **Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation** — Proposes prompt-level teacher gating so students only get dense token-level supervision when the frozen teacher appears reliable, aiming to reduce harmful guidance and improve OPD stability/efficiency. [Read more](https://arxiv.org/abs/2609.02998)

- **Routing Is Not Enough: Diagnosing Intra-Adapter Subspace Contention in MoE+LoRA Fine-Tuning** — Argues MoE routing alone does not fully isolate multi-domain updates when paired with LoRA; identifies intra-adapter subspace contention as a likely interference source and points toward stronger parameter-isolation schemes. [Read more](https://arxiv.org/abs/2609.03150)

- **Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Reasoning with Gradient-Aligned Rewards** — Tackles a core RLVR issue where binary outcome rewards fail to distinguish among correct reasoning paths; introduces gradient-aligned rewards to provide a more informative training signal. [Read more](https://arxiv.org/abs/2609.03342)

- **EmoDistill: Offline Emotion Skill Distillation for Language Model Agents in Adversarial Negotiation** — Presents an offline distillation method for teaching emotionally robust negotiation behavior, with a post-training focus on specialization without online RL. [Read more](https://arxiv.org/abs/2605.26785)

- **Skill-Conditioned Gated Self-Distillation for LLM Reasoning** — Introduces a self-distillation approach for reasoning that combines skill conditioning with gating to make supervision more selective and targeted. *(Link was not included in the source notes.)*

## Key Takeaways

- **Selective supervision is a major theme**: teacher gating and gated self-distillation both aim to improve post-training by deciding when supervision is actually trustworthy.
- **Reward design is getting more nuanced**: gradient-aligned rewards reflect a broader push beyond coarse binary outcomes toward signals that better differentiate reasoning quality.
- **Offline specialization remains attractive**: EmoDistill highlights continued interest in avoiding costly or unstable online RL while still teaching domain-specific behaviors.
- **Parameter isolation still matters**: the MoE+LoRA paper suggests routing alone may not prevent cross-domain interference during fine-tuning.
- **Overall trend**: this week’s papers skew toward making post-training more **efficient, robust, and selective** rather than simply scaling more data or compute.