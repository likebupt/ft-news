**Note:** The feed is entirely academic/arXiv research with no clear company affiliations provided, so relevant items are grouped under **Research / Academia**.

## Research / Academia

### Inverse Reasoning Models for Efficient Post-Training and Verification from Answer-Only Data
- Proposes **Inverse Reasoning Models (IRMs)** to post-train reasoning LLMs using **answer-only supervision**, targeting a cheaper alternative to chain-of-thought annotated data. [Read more](https://arxiv.org/abs/2610.18878)
- Positions the same framework as a **verification tool**, suggesting a two-for-one benefit: lower-cost reasoning post-training plus answer checking. [Read more](https://arxiv.org/abs/2610.18878)

### How Many Ranks Does a Token Need? A Noise-Floor Squelch for Rank-One LoRA Experts
- Examines a core LoRA inefficiency: applying every rank-one component to every token, even when many components may contribute mostly noise. [Read more](https://arxiv.org/abs/2610.19033)
- Introduces a **noise-floor “squelch”** mechanism for **rank-one LoRA experts**, aiming to activate only the useful low-rank components per token instead of relying on a fixed routing budget. [Read more](https://arxiv.org/abs/2610.19033)

### DTDD: Divergence-Triggered Dynamic Distillation for Reliable On-Policy Supervision
- Tackles a known failure mode in **on-policy distillation**: teacher token-level supervision becomes unreliable once student and teacher trajectories drift too far apart. [Read more](https://arxiv.org/abs/2610.19302)
- Proposes **divergence-triggered dynamic distillation**, which appears to adapt supervision based on teacher-student mismatch to keep on-policy training stable. [Read more](https://arxiv.org/abs/2610.19302)

### Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents
- Studies **curriculum design under GRPO** for long-horizon agent tasks, highlighting that GRPO provides little learning signal when all sampled rollouts receive the same reward. [Read more](https://arxiv.org/abs/2610.19349)
- Focuses on the practical post-training question of **how to stage task difficulty and exploration** so reward-relative optimization remains informative in multi-step settings. [Read more](https://arxiv.org/abs/2610.19349)

### ReGRA: Residual-Gradient Adaptation for Complementary Low-Rank Fine-Tuning
- Targets a common PEFT issue: raising LoRA rank adds capacity, but not all learned directions are actually complementary or useful. [Read more](https://arxiv.org/abs/2610.19700)
- Proposes **Residual-Gradient Adaptation (ReGRA)** to encourage **complementary low-rank updates**, potentially improving parameter efficiency over simply increasing rank. [Read more](https://arxiv.org/abs/2610.19700)

### RM-OPD: On-Policy Distillation for Generative Reward Models
- Focuses on **Generative Reward Models (GRMs)**, arguing that today’s **Mix-RL** training pipeline has important drawbacks for general-purpose reward modeling. [Read more](https://arxiv.org/abs/2610.20174)
- Introduces **on-policy distillation for GRMs**, pointing to a potentially more stable and scalable route for training reward models used in alignment and post-training stacks. [Read more](https://arxiv.org/abs/2610.20174)

### Decoupled Marginal Sharpening for Training-Free Inference-Time Scaling
- Proposes a way to improve LLM reasoning **at inference time only**, without weight updates and without external reward models. [Read more](https://arxiv.org/abs/2610.20483)
- Builds on **reward-free power-sampling** and introduces **Decoupled Marginal Sharpening**, aiming to make test-time compute scaling more practical than sequence-level sampling schemes. [Read more](https://arxiv.org/abs/2610.20483)

## Key Takeaways
- **Cheaper post-training is a major theme