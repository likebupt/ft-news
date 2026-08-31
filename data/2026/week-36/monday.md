## Academic / arXiv Research

- **Large Reasoning Models Struggle to Transfer Parametric Knowledge Across Scripts** — Argues that cross-lingual knowledge transfer failures in modern reasoning LLMs are driven largely by a **script barrier**, suggesting multilingual post-training may need explicit cross-script alignment rather than assuming language transfer will generalize automatically. [Read more](https://arxiv.org/abs/2603.17070)

- **Human Label Variation as Stable Signal: Learning Annotator-Specific Explanation Behavior via Cross-Annotator Preference Optimization** — Treats annotator disagreement and free-text explanations as useful signal, proposing **cross-annotator preference optimization** to learn annotator-specific explanation behavior instead of collapsing variation into a single “gold” preference. [Read more](https://arxiv.org/abs/2605.28802)

- **Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation** — Benchmarks the reliability of **LLM-as-a-judge** setups for long-form generations, a timely issue for teams using automated evaluation to iterate on SFT, preference tuning, and reasoning models. [Read more](https://arxiv.org/abs/2606.01629)

- **Does Finetuning with Scientific Data Increase Hallucinations? A Multi-domain Factuality Evaluation of LLMs** — Examines whether **scientific-domain fine-tuning** changes hallucination behavior, using a multi-domain factuality evaluation that is directly relevant for domain adaptation in high-stakes assistant workflows. [Read more](https://arxiv.org/abs/2606.21359)

- **Self-Generated Text Recognition: Quality Heuristics, Cross-Task Transfer, and Downstream Bias in LLM Evaluation** — Studies **self-generated text recognition (SGTR)**, where models can detect their own outputs, highlighting a potential source of bias in evaluator, monitor, and safeguard pipelines that reuse related model families. [Read more](https://arxiv.org/abs/2608.26159)

- **PRISM: Self-Pruning Intrinsic Selection Method for Training-Free Multimodal Data Selection** — Introduces a **training-free multimodal data selection** method for visual instruction tuning, aiming to prune redundant/low-value examples and reduce post-training cost without full retraining-based selection loops. [Read more](https://arxiv.org/abs/2502.12119)

## Key Takeaways

- Post-training quality is increasingly constrained by **data and evaluator design**: annotator variation, judge reliability, and example selection are emerging as core levers alongside model scale.
- Two persistent