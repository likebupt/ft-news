# Final Weekly Digest

*No company affiliations were provided in the source summaries, so items are grouped under academic research.*

## Research / Academia (arXiv)

- **When to Write and When to Suppress: Route-Specialized Dual Adapters for Memory-Assisted Knowledge Editing** — Separates “write” vs. “suppress” routes in memory-assisted editing to update target facts while reducing collateral behavior changes, especially when retrieved memories are noisy or only partially relevant. [Link](https://arxiv.org/abs/2606.14668)

- **Weak-to-Strong Elicitation via Mismatched Wrong Drafts** — Shows that weaker-model off-policy traces, including wrong drafts, can help stronger models learn capabilities that standard on-policy RL fine-tuning may miss. [Link](https://arxiv.org/abs/2605.17314)

- **Metaphors are a Source of Cross-Domain Misalignment of Large Reasoning Models** — Finds that metaphorical framing can systematically alter reasoning across domains, highlighting a subtle misalignment channel that eval suites should test for explicitly. [Search link](https://arxiv.org/search/?query=Metaphors+are+a+Source+of+Cross-Domain+Misalignment+of+Large+Reasoning+Models&searchtype=all)

- **Know2Guess: A Contamination-Aware Multi-Zone Benchmark for Knowledge-Boundary Evaluation in Large Language Models** — Introduces a benchmark designed to separate genuine knowledge from unsupported guessing while controlling for contamination, prompt quirks, and refusal behavior. [Link](https://arxiv.org/abs/2606.26101)

- **From Lexicon to AI: A Structured-Data Pipeline for Specialized Conversational Systems in Low-Resource Languages** — Proposes a structured-data pipeline for building specialized conversational systems in low-resource languages without relying heavily on large text corpora. [Link](https://arxiv.org/abs/2606.26112)

- **Soft Token Alignment for Cross-Lingual Reasoning** — Targets inconsistent reasoning across semantically equivalent prompts in different languages by aligning representations beyond prompt-only fixes. [Link](https://arxiv.org/abs/2606.26466)

- **DiARC: Distinguishing Positive and Negative Samples Helps Improving ARC-like Reasoning Ability of Large Language Models** — Uses explicit positive/negative sample distinctions to improve ARC-style reasoning performance in LLMs. [Search link](https://arxiv.org/search/?query=DiARC%3A+Distinguishing+Positive+and+Negative+Samples+Helps+Improving+ARC-like+Reasoning+Ability+of+Large+Language+Models&searchtype=all)

## Key Takeaways

- **Post-training is getting more data-efficient and indirect:** wrong drafts, memory routing, and positive/negative sample design all point to richer supervision beyond standard RL or SFT.
- **Evaluation quality remains a major theme:** contamination-aware knowledge benchmarks and framing-sensitive misalignment tests both push toward more realistic, harder-to-game evals.
- **Robust multilingual performance is still an open frontier:** cross-lingual reasoning alignment and low-resource conversational pipelines show continued focus on extending capability beyond English-heavy settings.
- **Safety and reliability concerns are becoming more subtle:** metaphor-driven reasoning shifts suggest that prompt framing itself can be a meaningful source of model misalignment.