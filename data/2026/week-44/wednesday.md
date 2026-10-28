# Weekly Digest — Fine-Tuning, Post-Training & PEFT

## Company Updates
- No clear company blog/news items were included in this batch.

## Open Research / arXiv

- **Beyond Update Counts: A Control Map for Evaluating Test-Time Model Updates** — Proposes a more structured framework for evaluating persistent test-time updates to model state (e.g., weights/adapters). *(Link not provided in source.)*

- **[Dr. Post-Training](https://arxiv.org/abs/2605.07063)** — Reframes post-training data selection as a data-regularization problem, helping teams reason about when scarce high-fidelity data should be mixed with broader noisier corpora.

- **[Lost in the bf16 Cast](https://arxiv.org/abs/2610.07853)** — Shows that export/casting pipelines for ternary LMs can wipe out small fine-tuning gains; practical implication: audit quantization/export end to end.

- **First-Order LoRA Training with Phone NPUs** — Explores on-device LoRA fine-tuning on smartphone NPUs for private, local personalization. *(Link not provided in source.)*

- **[Hierarchical Low-Rank Reparameterization for Parameter-Efficient…](https://arxiv.org/abs/2610.37068)** — Introduces hierarchical low-rank reparameterization for PEFT, aiming to shrink adaptation-state size further for customized deployment.

- **[Aligning Large Language Models for Safety in African Languages: A Case Study of Hausa](https://arxiv.org/abs/2610.37245)** — Examines how safety alignment transfers to a low-resource language setting, highlighting limits of English-centric assumptions.

- **[Teach reality, not ethics](https://arxiv.org/abs/2610.37484)** — Argues that continued-pretraining corpus design itself can be a meaningful alignment lever, not just instruction tuning or preference optimization.

- **[Uncovering Shortcut Amplification in Video RLVR through the Lens of Perceptual Uncertainty Collapse](https://arxiv.org/abs/2610.37211)** — Identifies a failure mode in video RL with verifiable rewards where post-training amplifies brittle shortcut cues.

## Key Takeaways

- **Post-training is becoming more data- and pipeline-aware:** both dataset mixing and export/quantization details can materially change outcomes.
- **PEFT research is pushing in two directions at once:** smaller adaptation state for deployment and more feasible on-device personalization.
- **Alignment work is broadening beyond English defaults:** multilingual safety transfer and corpus design are emerging as important levers.
- **Evaluation is getting more nuanced:** simple update counts are not enough, and RLVR setups still need robustness checks for shortcut behavior.