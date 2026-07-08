# Weekly Digest

*No company-affiliated announcements were included in these two batches, so the relevant items are grouped under open research.*

## Academia / Open Research

- **[A Coin Flip Per Token: Bernoulli Sparse Steering of Large Language Models](https://arxiv.org/abs/2607.05615)** — Proposes per-token Bernoulli SAE steering, making inference-time behavior control lighter and more selective than steering every token.
- **[Auditing of Unlearning Algorithms](https://arxiv.org/abs/2607.05898)** — Introduces an auditor that estimates lower bounds on the residual influence of removed training data, aimed at verifying whether unlearning actually worked.
- **[Performance Optimization and Comparative Analysis of Generative AI Models on Advanced Accelerators](https://arxiv.org/abs/2607.05400)** — Analyzes LLM and diffusion model performance on advanced accelerator hardware, with a focus on deployment efficiency and serving trade-offs.
- **[Fine-Tuning Regimes Define Distinct Continual Learning Problems](https://arxiv.org/abs/2604.21927)** — Argues that different fine-tuning setups create different forgetting/retention dynamics, so continual-learning results should be evaluated by regime rather than treated as directly comparable.

## Key Takeaways

- **Post-training control is getting more targeted:** inference-time steering methods are shifting toward sparse, selective interventions instead of always-on control.
- **Verification is becoming a first-class concern:** unlearning work is moving beyond methods to auditing and compliance-oriented validation.
- **Deployment efficiency remains critical:** accelerator-aware optimization is still a major practical bottleneck for production GenAI systems.
- **Fine-tuning results are highly regime-dependent:** teams doing sequential SFT, domain adaptation, or instruction tuning should be cautious about generalizing continual-learning claims across setups.