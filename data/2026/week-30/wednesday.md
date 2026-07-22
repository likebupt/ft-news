# Weekly Digest

*No company-specific announcements were included in these partials; this week’s digest is research-heavy.*

## Research / Academia

- **[NexForge: Scaling Agent Capabilities through Requirement-Driven Task Synthesis for LLMs](https://arxiv.org/abs/2607.14186)** — Proposes requirement-driven synthesis of executable agent-training tasks, aiming to scale post-training data generation beyond fixed tools, repos, or skill graphs.

- **[Rationale-Guided Knowledge Distillation for Cross-Lingual Stance Detection](https://arxiv.org/abs/2607.18693)** — Uses teacher rationales during distillation to improve cross-lingual stance detection, suggesting a more efficient way to transfer multilingual capabilities into smaller models.

- **[Guard Vector: Beyond English LLM Guardrails with Task-Vector Composition and Streaming-Aware Prefix SFT](https://arxiv.org/abs/2509.23381)** — Introduces a reusable “Guard Vector” that composes safety behavior into other same-architecture models, with a focus on multilingual guardrailing and streaming-aware serving.

- **[Lower-Resource, Higher Scores: Language Bias in LLM Evaluators](https://arxiv.org/abs/2607.14480)** — Examines bias in reward models and LLM-as-a-Judge systems, arguing that strong aggregate accuracy can still hide unfair scoring across languages.

- **[Reasoning Fine-Tuning Induces Persistent Latent Policy States](https://arxiv.org/abs/2607.18532)** — Suggests reasoning fine-tuning may create durable internal policy shifts rather than only transient inference-time strategies, with implications for interpretability and safety evaluation.

- **[Disentangling Curriculum Learning in NLP: Towards a Unifying Taxonomy](https://arxiv.org/abs/2607.18984)** — Proposes a unifying taxonomy for curriculum learning, offering clearer guidance on difficulty metrics and schedules that affect fine-tuning efficiency and stability.

## Key Takeaways

- **Post-training is getting more modular:** requirement-driven task synthesis, task-vector-style safety composition, and curriculum design all point to more targeted alternatives to monolithic fine-tuning.
- **Multilingual alignment is a major theme:** cross-lingual distillation, non-English guardrailing, and evaluator bias all highlight gaps in current multilingual deployment stacks.
- **Evaluation remains a weak point:** reward models and LLM judges may appear strong while still introducing systematic language bias.
- **Reasoning and safety tuning are increasingly viewed as policy-shaping:** new work is focusing on how fine-tuning changes internal model states, not just outputs.

*Note: one source item (“Find Before You Fine-Tune: …”) appeared truncated in the input, so it was omitted to avoid adding unsupported details.*