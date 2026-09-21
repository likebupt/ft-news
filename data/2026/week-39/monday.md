# Weekly Digest

## Company Updates
- No major company announcements surfaced in these summaries; the most relevant items were from **academic / open-source research**.

## Academic / Open-Source Research
- **[When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation](https://arxiv.org/abs/2609.20942)** — Studies how AI-generated peer reviews can contaminate future reviewer-model training and degrade evaluation quality over time.
- **[FairLMs: A Turnkey Library for Fairness in Language Models](https://arxiv.org/abs/2609.21296)** — End-to-end fairness toolkit for bias measurement, mitigation, and evidence inspection in LM workflows.
- **[IncentRL: The Trade-Off Between Preference Guidance and Task Performance](https://arxiv.org/abs/2609.21525)** — Explores RLHF-style reward design that balances preference alignment with original task performance.
- **[Reading Anxiety or Reading the Label? Comparing Fine-Tuned and Frontier Models for Anxiety Detection on Social Media](https://arxiv.org/abs/2609.20847)** — Compares smaller fine-tuned models vs. prompted frontier models, with focus on real signal detection vs. annotation shortcuts.
- **[Scaling Forced Alignment to End-User Devices](https://arxiv.org/abs/2609.21145)** — More efficient audio-text forced alignment aimed at on-device use, relevant for speech data curation and post-training pipelines.
- **[PRISM-BN: A Controlled Corpus and Benchmark for Text-to-Parameterized Bayesian Network Extraction](https://arxiv.org/abs/2609.21673)** — Adds a benchmark for extracting Bayesian-network structure and parameters from text, useful for structured prediction evals.
- **[Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](https://arxiv.org/abs/2608.17605)** — Survey of persistent multimodal assistants covering datasets, architectures, evaluation gaps, memory, grounding, and turn control.
- **[Dynamic Lagging using Stable-Prefix Training for Simultaneous Translation](https://arxiv.org/abs/2609.05799)** — Improves latency/quality tradeoffs in streaming translation, relevant for real-time multilingual assistants.
- **The Role of Fine-grained Harm Signals in LLM Safety** — Examines whether category-specific harm labels outperform a single generic harmfulness label for safety supervision and post-training control. *(Link not included in source notes.)*

## Key Takeaways
- **Synthetic-data feedback loops matter more**: AI-generated outputs reused in training can degrade evaluator and preference-model quality without strong provenance and filtering.
- **Post-training tooling is broadening**: Focus is expanding from optimization alone to fairness, safety, and evaluator governance.
- **Evaluation quality remains a bottleneck**: Several papers highlight shortcut learning, label leakage, and weak supervision as persistent risks.
- **Speech and real-time systems are getting more practical**: On-device alignment and lower-latency translation methods could improve deployment efficiency.
- **Structured and multimodal benchmarks are maturing**: New benchmarks and surveys point to growing interest in rigorous evaluation for symbolic extraction and multi-turn multimodal assistants.