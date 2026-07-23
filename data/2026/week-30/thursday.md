# Weekly Digest

## Company Updates
- No company-specific releases were included in these partial summaries.

## Academic / arXiv
- **LAARA: Layer-Aware Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning** — Assigns different LoRA ranks to different transformer layers instead of using one uniform rank, aiming for better quality-per-parameter and less manual rank tuning. [Read more](https://arxiv.org/abs/2607.19391)
- **From Trajectories to Prefixes: Reusing Teacher Trajectories via Replayed Prefixes and Online Continuation** — Proposes a distillation method for small agentic LMs that reuses teacher trajectories as replayed prefixes and continues generation online to transfer agent behavior more efficiently. [Search on arXiv](https://arxiv.org/search/?query=From+Trajectories+to+Prefixes%3A+Reusing+Teacher+Trajectories+via+Replayed+Prefixes+and+Online+Continuation&searchtype=title)
- **How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF** — Treats reward-model scoring as a core RLHF systems bottleneck and benchmarks C++ vs. PyTorch inference paths to measure training-loop speedups. [Read more](https://arxiv.org/abs/2607.19712)
- **Post-Training in Time Series Foundation Models: A Unifying Framework** — Argues that pretraining alone is insufficient for reliable deployment and organizes the post-training adaptations needed for time-series foundation models. [Read more](https://arxiv.org/abs/2607.20002)
- **Co-Evolving LLM Evaluators and Policies via DynamicRubric** — Targets evaluator saturation during post-training by evolving the rubric alongside the policy so feedback remains discriminative as outputs improve. [Read more](https://arxiv.org/abs/2607.20083)
- **Knowledge-Centric Self-Improvement** — Shifts self-improvement from prompts/workflows/agents toward the underlying knowledge base, with the goal of making iteration more reusable, auditable, and stable. [Read more](https://arxiv.org/abs/2607.19592)

## Key Takeaways
- RLHF optimization is increasingly a **systems problem as well as a modeling problem**; reward-model inference speed can directly limit training throughput.
- Post-training research is focusing on **stronger, longer-lasting feedback loops**, especially evaluators that stay useful as policies improve.
- Fine-tuning is moving toward **more structured adaptation**, from layer-aware PEFT methods to unified post-training frameworks.
- There is growing interest in **reusable improvement mechanisms**, including distillation from teacher trajectories and knowledge-base-centric self-improvement.