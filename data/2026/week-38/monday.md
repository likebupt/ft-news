# Weekly Digest

## Open Research / Academia
*(The source notes only identified arXiv/open-research items, so all updates are grouped here.)*

- **[SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141)** — Post-training attention sparsification that learns to rank the most useful context tokens/blocks end-to-end, aiming to reduce Transformer inference cost.
- **[Chopthin-Consensus Power Sampling: A Diversity-Preserving Approach to LLM Decoding](https://arxiv.org/abs/2609.12243)** — Inference-time decoding via SMC power sampling designed to improve reasoning while preserving trajectory diversity, without post-training.
- **[SteerDuplex: Steerable Duplex Speech Dialogue Models](https://arxiv.org/abs/2609.12623)** — Adds steerability to full-duplex spoken dialogue systems, targeting controllable real-time behavior beyond latency, interruption handling, and backchanneling.
- **[EAR: Entity-Aware Partitioning for RAG](https://arxiv.org/abs/2609.12268)** — Replaces naive chunking with entity-aware corpus partitioning to better preserve semantic boundaries and improve retrieval grounding.
- **[CueMem: Cue-Guided Context Reconstruction](https://arxiv.org/abs/2609.12354)** — Long-term memory approach for conversational agents that stores compact cues and reconstructs richer context on demand to cut token cost and improve recall.
- **[ORQA: Occupation-Realistic QA for Professional Knowledge](https://arxiv.org/abs/2609.12366)** — Evaluation framework for testing LLM knowledge using more realistic occupation-level professional questions rather than synthetic skill proxies.
- **[GraphProfiler: Sensitive Attribute Inference via Personal Knowledge Graphs](https://arxiv.org/abs/2609.12448)** — Shows how LLM profiling can infer sensitive traits by aggregating weak signals across many posts and linking them into a personal knowledge graph.
- **[Meddies-PII: Multilingual Clinical De-identification](https://arxiv.org/abs/2609.12544)** — Multilingual framework for extracting PII from clinical text, aimed at improving de-identification where labeled data is scarce and expensive.
- **[Cognition on Graph: Graph-Text Synergy for RAG](https://arxiv.org/abs/2609.12791)** — Graph-centric RAG with bidirectional graph-text interaction and “cognitive cycles” for better navigation of large heterogeneous knowledge spaces.

## Key Takeaways
- **Inference optimization is a major theme:** SAS and Chopthin-Consensus both target better efficiency/quality at inference time without changing pretraining.
- **RAG architecture is moving beyond basic chunking:** EAR and Cognition on Graph highlight that retrieval unit design and graph structure can materially improve grounding and multi-hop reasoning.
- **Memory and voice agents are getting more product-oriented:** CueMem and SteerDuplex focus on persistent context, controllability, and real-time behavior.
- **Evaluation and safety are broadening:** ORQA, GraphProfiler, and Meddies-PII point to stronger emphasis on domain realism, privacy risks, and compliance-sensitive workflows.

*Note: A few source entries appeared truncated in the partial summaries, so this digest includes the items with enough detail and links to merge cleanly.*