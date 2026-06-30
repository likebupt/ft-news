## Weekly Digest

*Note: the provided partials only contained academic / independent research items, so the digest is grouped accordingly.*

### Academic / Independent Research

- **A Gravitational Interpretation of Fine-Tuning Reversion** — Proposes a theory for why later, seemingly benign fine-tuning can partially undo prior alignment, safety tuning, or unlearning. [Read more](https://arxiv.org/abs/2606.28525)

- **Invariant Reasoning Directions in Latent Trajectories of Language Models** — Identifies invariant hidden-state directions that may underlie multi-step reasoning, with implications for latent-space steering and reasoning control. [Read more](https://arxiv.org/abs/2606.29164)

- **Symbolic Mechanistic Data Attribution: Tracing Training Influence to Learned Behavioral Policies** — Extends data attribution toward explaining how specific examples shape higher-level model behaviors, useful for auditing SFT/RLHF datasets. [Read more](https://arxiv.org/abs/2606.29171)

- **BaRA: Bayesian Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning** — Introduces adaptive LoRA rank allocation instead of fixed-rank tuning, aiming to improve PEFT efficiency across uneven tasks. [Read more](https://arxiv.org/abs/2606.29184)

- **On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse** — Re-examines GRPO through a policy-gradient lens, focusing on credit assignment and optimization pathologies relevant to RL post-training. *(Link not included in source notes.)*

- **Neural Subspace Reallocation: Continual Learning as Retrieval-Based Subspace Memory Management** — Treats LoRA adapters as reusable parameter subspaces, framing continual learning as retrieval and reallocation to reduce forgetting. [Read more](https://arxiv.org/abs/2606.30067)

- **Online Data Selection for Instruction Tuning via Gaussian Processes** — Proposes GP-based online selection for instruction-tuning data, targeting the growing bottleneck of data quality over raw volume. [Read more](https://arxiv.org/abs/2606.30077)

- **Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation** — Explores PEFT for incrementally updating motion-language agents without full retraining, extending continual adaptation into multimodal settings. [Read more](https://arxiv.org/abs/2606.30266)

- **DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training** — Introduces a self-improvement framework for reasoning models that combines difficulty-aware routing, periodic exploration, and replay-like success buffers. *(Link not included in source notes.)*

### Key Takeaways

- **Post-training stability is a major theme**: new work focuses on why fine-tuning can reverse alignment or cause forgetting.
- **PEFT is getting more dynamic**: LoRA is evolving toward adaptive rank allocation, reusable subspaces, and continual multimodal updates.
- **Data quality is now a first-class bottleneck**: both attribution and online data selection are becoming more central to tuning pipelines.
- **Reasoning optimization is diversifying**: researchers are probing latent reasoning structure, RL training dynamics, and self-distillation methods in parallel.