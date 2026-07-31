# Final Weekly Digest

## Academic / Open Research
- [**SDO: Structure-Aware Data Organization for Efficient LLM Post-Training**](https://arxiv.org/abs/2607.27273) — Frames data organization itself as a post-training efficiency lever, beyond sample selection and scheduling.
- [**Subtract or Replay? Exact Deletion from Language-Model Memory**](https://arxiv.org/abs/2607.27539) — Examines when exact deletion from persistent LM memory is possible via subtraction versus requiring replay; relevant to privacy and unlearning.
- [**Compliance2LoRA: On-Demand Safety Alignment on Arbitrary Policy Subsets via Hypernetwork-Generated LoRA Adapters**](https://arxiv.org/abs/2607.27594) — Uses a hypernetwork to generate policy-specific LoRA adapters on demand for modular, personalized safety alignment.
- [**Constitutional Midtraining: Content Presence Drives Alignment Gains**](https://arxiv.org/abs/2607.26654) — Suggests alignment durability may depend more on aligned content in the training mix than on the intervention label itself.
- [**HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs**](https://arxiv.org/abs/2607.27379) — Explores synthetic data generation for underrepresented humanities/social-science domains where high-quality supervision is scarce.
- [**Training Skills Like Parameters via Self-Supervised Semantic Diffusion**](https://arxiv.org/abs/2607.27557) — Proposes learning specialized open-ended skills through self-supervised semantic diffusion rather than standard instruction tuning alone.
- [**Lightning OPD 2.0: Mitigating Style Bias in Cross-Teacher On-Policy Distillation for Large Reasoning Models**](https://arxiv.org/abs/2607.28449) — Targets style bias in multi-teacher reasoning distillation to make on-policy post-training more robust.
- [**OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models**](https://arxiv.org/abs/2607.28609) — Introduces standardized evaluation for reward models used in computer-use agents across environments.
- [**Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection**](https://arxiv.org/abs/2604.18248) — Moves beyond regex/classifier-only defenses with seven broader techniques for more robust prompt-injection detection.

## Key Takeaways
- **Alignment is moving earlier in the stack**: midtraining and training-data composition look increasingly important for durable behavior changes.
- **Post-training is becoming more modular and data-centric**: structure-aware data organization, synthetic data, skill injection, and policy-specific LoRA adapters all push in that direction.
- **Reasoning and agent stacks are maturing operationally**: cross-teacher distillation and reward-model benchmarking address practical bottlenecks in deployment.
- **Security, privacy, and compliance are rising priorities**: prompt-injection detection, exact memory deletion, and modular safety alignment all point to stronger post-deployment controls.

*Note: one partial item on LoRA sample complexity was truncated in the source summaries and lacked a usable link, so it was not included above.*