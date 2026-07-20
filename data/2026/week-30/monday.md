# Weekly Digest

*All items provided this week were from **Open Research / Academia**, so they’re grouped together below.*

## Open Research / Academia

- **Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation for Compressed Reasoning** — Proposes iterative self-reasoning distillation to compress long reasoning chains into shorter, more efficient reasoning traces. *(Link not provided in source.)*

- [**When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis**](https://arxiv.org/abs/2607.16062) — Analyzes when separately trained RL policies can be merged successfully, and when parameter-space interference makes joint multi-task RL the better option.

- [**Rate-Utility Frontiers for Language Encodings: Comparing Tokens, Bytes, and Pixels Under Controlled Linguistic Content**](https://arxiv.org/abs/2607.16117) — Compares token-, byte-, and pixel-based encodings under controlled information exposure to clarify efficiency trade-offs for tokenizer-free and multimodal language modeling.

- [**What Models Express, Suppress, and Resist: Auditing Open-Weight LLMs with Persona Vectors**](https://arxiv.org/abs/2607.13162) — Introduces persona vectors to probe which behavioral tendencies post-trained models express, hide, or resist, offering a deeper audit tool for alignment and safety.

- **SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents** — Consolidates and evaluates reusable agent “skills” for real-world LLM systems, helping structure and benchmark the emerging open skill ecosystem. *(Link not provided in source.)*

- [**Analysing Moral Bias in Finetuned LLMs through Mechanistic Interpretability**](https://arxiv.org/abs/2510.12229) — Studies how fine-tuning changes moral bias inside model internals, pointing toward component-level diagnosis and mitigation rather than output-only bias testing.

- [**From Articles to Premises: Building PrimeFacts, an Extraction Methodology and Resource for Fact-Checking Evidence**](https://arxiv.org/abs/2605.06006) — Builds a method and dataset for converting long fact-checking articles into premise-level evidence that automated verification systems can use more directly.

## Key Takeaways

- **Post-training is getting more inspectable:** persona vectors and mechanistic bias analysis both push evaluation beyond surface outputs and into model internals.
- **Efficiency remains a core theme:** compressed reasoning and encoding-rate trade-offs both target lower-cost, higher-utility inference and training.
- **Composition vs joint training is a live question:** model merging work suggests modular post-training can be competitive, but only under the right geometric conditions.
- **Agent infrastructure is maturing:** SkillCorpus reflects growing interest in reusable, benchmarkable agent skills rather than one-off agent pipelines.
- **Verification pipelines are becoming more structured:** PrimeFacts shows continued movement toward premise-level evidence extraction for fact-checking systems.