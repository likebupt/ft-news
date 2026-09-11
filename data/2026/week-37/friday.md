## Weekly Digest

*No company-specific releases appeared in these partials; the notable items this week were academic research papers on pretraining, post-training, and deployment efficiency.*

## Academic Research / arXiv

- **Characterizing Narrative Content in Web-scale LLM Pretraining Data** — Fine-grained analysis of narrative content in web-scale pretraining corpora, relevant for dataset auditing, mixture design, and continued pretraining. [Search](https://arxiv.org/search/?query=Characterizing+Narrative+Content+in+Web-scale+LLM+Pretraining+Data&searchtype=all&abstracts=show&order=-announced_date_first&size=50)
- **The information geometry of large language models is shared, learned, and controllable** — Uses Fisher–Rao geometry of next-token distributions to study why independently trained LLMs converge on similar behaviors, with implications for more selective post-training edits and alignment. [Read more](https://arxiv.org/abs/2609.11063)
- **LILA: Calibration-Free Structured Pruning of Large Language Models via Latent Spectral Geometry** — Proposes structured pruning without calibration data, gradients, or large auxiliary policy networks, making compression cheaper and more practical for real hardware speedups. [Read more](https://arxiv.org/abs/2609.11163)
- **Why Does Post-Training Quantization Work?** — Offers theoretical grounding for why quantization noise does not explode across layers, helping practitioners reason more confidently about lower-bit PTQ. [Read more](https://arxiv.org/abs/2609.11716)
- **When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents** — In a 34,396-skill router setting, shows synthetic data can degrade retrieval quality via catastrophic forgetting instead of improving coverage. [Read more](https://arxiv.org/abs/2609.10750)
- **Your Model Already Knows Don’t Teach It, Learn to Ask It: Soft Prompting for Few-Shot Adaptation of Vision-Language Models** — Finds that soft prompting can adapt VLMs to out-of-domain tasks with as few as 10 labeled images, often avoiding heavier fine-tuning. [Read more](https://arxiv.org/abs/2609.11310)

## Key Takeaways

- **Post-training efficiency was a major theme**: pruning and quantization research focused on lowering deployment cost without full retraining.
- **Selective control is gaining importance**: geometry-based behavior editing and soft prompting both point to lighter-touch adaptation methods.
- **Data decisions remain high leverage**: both pretraining corpus composition and synthetic-data augmentation can strongly shape downstream behavior.
- **Agent pipelines need caution with synthetic data**: augmentation can hurt tool/skill retrieval if it overwrites existing routing behavior.