# Weekly Digest — Fine-Tuning & Post-Training

*No company-specific updates were included in the provided excerpts, so items are grouped under **Open Research / Academic**.*

## Open Research / Academic

- **[Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation](https://arxiv.org/abs/2610.02324)** — Proposes a multi-teacher, on-policy distillation setup for multimodal LLMs aimed at improving specialization without eroding broad capabilities.
- **[Are you Synthesizing or Recalling? Evaluating LLMs on Algorithmic Code Retrieval](https://arxiv.org/abs/2610.02438)** — Introduces an eval framework to separate true code synthesis from memorized algorithm recall, helping teams interpret post-training gains more accurately.
- **[Capability Scaling-Down Laws for LLM Compression](https://arxiv.org/abs/2610.02462)** — Explores more predictable capability–efficiency trade-offs for compression, moving model downsizing beyond heuristic tuning.
- **Post-Training Quantization of Autoregressive Weather Models** — Examines post-training quantization for autoregressive weather models, highlighting deployment trade-offs for scientific forecasting systems. *(Link not included in the provided partials.)*
- **[Context-Tower Conversion Preserves Generation While Freezing Retains Knowledge: Low-Budget AR-to-Diffusion Conversion of MoE LLMs](https://arxiv.org/abs/2610.02657)** — Presents a lower-cost path to convert pretrained autoregressive MoE LLMs into diffusion LMs while preserving generation quality and retained knowledge.
- **[Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps](https://arxiv.org/abs/2610.02740)** — Uses the gap between predicted and observed outcomes as a self-calibration signal for RL, with potential benefits for long-horizon planning and agent post-training.
- **[CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking](https://arxiv.org/abs/2610.02460)** — Proposes calibrated user embeddings to make multi-turn user simulation more realistic and useful for evaluating interactive assistants.
- **[Text-Centric Post-Training for Omni-Modal Reasoning](https://arxiv.org/abs/2610.02819)** — Argues that text-centric post-training can cheaply improve multimodal reasoning without requiring large new audio-visual datasets.
- **[Evaluating LLM-as-a-Judge Beyond Score Alignment: A Psychometric Analysis of Residual Judging Difficulty](https://arxiv.org/abs/2610.02877)** — Looks beyond average score agreement to test whether LLM judges fail on the same hard examples as humans, which matters for reward modeling and eval automation.
- **Enhancing Biomedical Named Entity Recognition via Multiple Programming Languages Instruction Tuning and Ensemble Method** — Explores BioNER instruction tuning using prompts framed through multiple programming languages plus ensembling, pointing to a niche but practical adaptation strategy. *(Link not included in the provided partials.)*

## Key Takeaways

- **Capability preservation is becoming a core post-training theme**, especially in distillation, multimodal tuning, and conversion pipelines.
- **Evaluation is getting more diagnostic**, with new work focused on disentangling recall vs. reasoning, improving user simulation, and stress-testing LLM judges beyond top-line agreement.
- **Efficiency work is maturing**, with papers on compression laws, quantization, and AR-to-diffusion conversion aiming to make deployment trade-offs more predictable.
- **Cheaper post-training paths are gaining traction**, particularly text-centric methods for multimodal systems and low-budget model conversion techniques.
- **Domain-specific post-training remains active**, with examples spanning weather forecasting and biomedical NER.