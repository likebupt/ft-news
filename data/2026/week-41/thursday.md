# Final Weekly Digest

## Research / Academia

### Post-training / RL
- **BehaviorTrace** — Introduces a method to link online RL rollouts to newly learned behaviors, while warning that attribution can look causal without being reliable. [Read more](https://arxiv.org/abs/2610.10422)
- **Multi-Teacher On-Policy Distillation (MOPD)** — Uses **teacher-relative shifts** to better combine heterogeneous teacher policies across domains. [Read more](https://arxiv.org/abs/2610.10460)
- **Decoupling Exploration from Optimization in RLVR** — Argues reasoning-focused RL with verifiable rewards should separate exploration from optimization to improve strategy discovery. [Read more](https://arxiv.org/abs/2610.10536)
- **LoGRA** — Proposes **low-rank gradient sketches** to reduce memory costs in RL-based LLM post-training, relevant for scaling RLHF/RLAIF pipelines. [Read more](https://arxiv.org/abs/2610.06647)
- **SeOPD** — Explores online self-distillation from a model’s own chain-of-thought as a cheaper path to continual self-improvement. [Read more](https://arxiv.org/abs/2609.33181)
- **Many Ways to Succeed** — Shows that preserving behavioral diversity during RL fine-tuning can improve VLA generalization beyond narrow policy optimization. [Read more](https://arxiv.org/abs/2610.09943)

### Alignment / Planning / Generalization
- **CM-DPO** — Extends DPO for planning by weighting the **severity** of constraint violations and reducing common length/style bias. [Read more](https://arxiv.org/abs/2610.09219)
- **Persona Hierarchy Model** — Studies when fine-tuned behaviors remain tied to a specific prompt/persona versus generalize across contexts. [Read more](https://arxiv.org/abs/2610.09384)

### Agent Evaluation / Simulation
- **Beyond Cooperative Simulators** — Pushes for more realistic user personas in agent evals, including ambiguous, impatient, or reluctant users. [Read more](https://arxiv.org/abs/2605.12894)
- **ToolRACER** — Presents a resource for training and evaluating task-oriented agents under harder, less cooperative conversational conditions. *(Link not included in source summary.)*

## Key Takeaways
- **Credit assignment is a major theme:** researchers are probing which rollouts, teachers, and rewards actually drive behavior change.
- **Post-training is getting more structured:** work this week emphasizes better exploration, multi-teacher composition, constraint-aware objectives, and diversity-preserving RL.
- **Efficiency is improving:** methods like **LoGRA** and **SeOPD** aim to make iterative RL-style post-training cheaper and less dependent on stronger external teachers.
- **Evaluation is becoming more realistic:** new persona and conversation-emulation work reflects a shift toward testing agents in messy, non-cooperative real-world settings.