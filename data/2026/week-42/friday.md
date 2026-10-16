# Final Weekly Digest

*No company-attributed items were provided in the source summaries, so all items are grouped under **Open Research / Academic**.*

## Open Research / Academic

- [**Towards Continual Learning: Mitigating Forgetting With Subspace Tuning**](https://arxiv.org/abs/2610.22293) — Proposes **subspace tuning** to reduce catastrophic forgetting during sequential LLM fine-tuning, aiming to preserve existing skills while adding new ones.

- [**CoTranslator: Reverse to Forward Chain-of-Thought Translator for Reasoning Distillation**](https://arxiv.org/abs/2610.20828) — Reframes reasoning distillation around **reverse-to-forward CoT translation**, with the goal of producing cheaper, higher-quality reasoning traces.

- [**Athanor: An Agent-Native System for Autonomous Post-Training Research**](https://arxiv.org/abs/2610.21055) — Presents an **agent-native system** for autonomous post-training research, relevant to teams tracking AI-assisted model improvement.

- [**Clean Data Can Still Carry Backdoors: Support-Persistent Backdoors for Model Reuse**](https://arxiv.org/abs/2610.21208) — Argues that **clean downstream data does not eliminate inherited backdoor risk**, underscoring the need for model provenance checks and post-training security evaluation.

- [**MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering**](https://arxiv.org/abs/2610.22344) — Explores a **generalist agentic model** for autonomous ML engineering, pointing toward end-to-end automation of experimentation, tuning, and model improvement.

- [**Stabilizing the Modality Gap: Null-Space Projected Continual Learning for Vision-Language Models**](https://arxiv.org/abs/2507.19839) — Uses **null-space projected updates** to support continual learning in VLMs without degrading image-text alignment.

- [**Wolof-Adapted Industry-Ready Open-Weight Language Models**](https://arxiv.org/abs/2610.20824) — Focuses on adapting open-weight LLMs for **Wolof**, highlighting practical low-resource deployment issues such as cost, governance, and language sovereignty.

- [**Data Strategies for Large Language Models: A Unified Perspective on the Training Lifecycle**](https://arxiv.org/abs/2610.21681) — Frames **data selection, weighting, and scheduling** as core levers across the full LLM lifecycle, not just initial pretraining.

- [**Translation Circuit Discovery and Targeted Optimization for Low-Resource Multilingual Translation**](https://arxiv.org/abs/2610.21456) — Studies internal **translation circuits** in multilingual LLMs and proposes targeted optimization as a more efficient alternative to broad fine-tuning for low-resource translation.

- [**OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents**](https://arxiv.org/abs/2610.21496) — Targets long-horizon coding-agent failures by reinforcing adherence to constraints and tool feedback through **on-policy reminder distillation**.

## Key Takeaways

- **Continual learning is a major theme**: multiple papers focus on preserving capabilities during sequential post-training for both text and multimodal models.
- **AI-for-AI is advancing**: systems like **Athanor** and **MLExpert** suggest growing momentum toward automating research, tuning, and ML engineering workflows.
- **Data remains a primary control surface**: from lifecycle data strategy to cheaper reasoning-distillation pipelines, post-training quality is increasingly framed as a data problem.
- **Security risks persist across reuse**: inherited backdoors remain a meaningful concern even when downstream fine-tuning data appears clean.
- **Low-resource and multilingual adaptation is getting more targeted**: work on Wolof and translation circuits points to more efficient methods than blanket fine-tuning.
- **Agent reliability over long horizons is becoming its own post-training category**, especially for coding and tool-using systems.

*Note: Two source entries appeared truncated in the provided summaries and were omitted to avoid adding unsupported details.*