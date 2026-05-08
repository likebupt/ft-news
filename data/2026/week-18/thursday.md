# Weekly AI Digest
*Items without clear company affiliation are grouped under **Open Research / arXiv**.*

## Together AI
- **[Together AI × Adaption partnership](https://www.together.ai/blog/announcing-together-ai-and-adaption-partnership)** — Brings Together Fine-Tuning into Adaptive Data, aiming for a more unified data optimization → fine-tuning → evaluation → deployment workflow.

## Microsoft
- **[Red-teaming a network of agents](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/)** — Argues that safety does not compose cleanly across multi-agent systems; teams need network-level red-teaming, not just single-agent evals.

## Tilde
- **[TildeOpen LLM](https://arxiv.org/abs/2603.08182)** — A 30B open model for 34 European languages that uses curriculum learning to improve representation and downstream quality for underrepresented languages.

## Open Research / arXiv

### Post-training, RL, and alignment
- **[EvoSelect](https://arxiv.org/abs/2604.26170)** — Data-efficient task adaptation via iterative synthetic-data selection and generation.
- **[TinyR1-32B-Preview](https://arxiv.org/abs/2503.04872)** — Uses Branch-Merge distillation to shrink models while retaining more accuracy.
- **[Teaching LLM to be Persuasive](https://arxiv.org/abs/2510.04214)** — Heterogeneous-reward policy optimization for safer, more controllable negotiation agents.
- **[Verified Critical Step Optimization](https://arxiv.org/abs/2602.03412)** — Optimizes verified intermediate steps for long-horizon agent post-training.
- **[PAINT](https://arxiv.org/abs/2604.26573)** — Combines partial-solution supervision with adaptive interpolation for denser reasoning signals.
- **[TLPO](https://arxiv.org/abs/2604.26553)** — Token-level policy optimization to reduce multilingual language confusion.
- **[A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)** — Reviews step-level/process supervision as an alternative to outcome-only rewards.
- **[Failure Modes of Maximum Entropy RLHF](https://arxiv.org/abs/2509.20265)** — Identifies important online RLHF failure modes for maximum-entropy/SimPO-style objectives.
- **[Affective Flow Language Model](https://arxiv.org/abs/2602.08826)** — Adds intermediate affective and strategy supervision for emotional support chat.
- **[Entropy Centroids as Intrinsic Rewards](https://arxiv.org/abs/2604.26173)** — Proposes best-of-N response selection without a separate reward model.
- **[DORA](https://arxiv.org/abs/2604.26256)** — Asynchronous RL system that overlaps rollout generation and optimization.
- **[Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2604.26779)** — Speeds RL post-training rollouts with system-integrated speculative decoding.
- **[reward-lens](https://arxiv.org/abs/2604.26130)** — Mechanistic interpretability toolkit built for scalar-head reward models.

### Agents, code, and reasoning infrastructure
- **[ClawGym](https://arxiv.org/abs/2604.26904)** — Framework for verifiable synthetic training and evaluation of persistent tool-using agents.
- **[SWE-Edit](https://arxiv.org/abs/2604.26102)** — Separates inspection, planning, and execution for more efficient code-editing agents.
- **[WebAggregator](https://arxiv.org/abs/2510.14438)** — Targets multi-source aggregation as a core capability for deep-research agents.
- **[Breaking the Autoregressive Chain](https://arxiv.org/abs/2604.26209)** — Hyper-parallel decoding for extraction tasks with conditionally independent outputs.

### RAG, grounding, and multimodal
- **[MINOS](https://arxiv.org/abs/2506.02494)** — Multimodal evaluator for both image→text and text→image generation.
- **[Faithfulness-QA](https://arxiv.org/abs/2604.25313)** — Counterfactual entity substitutions to train and evaluate context-faithful RAG.
- **[SciMDR](https://arxiv.org/abs/2603.12249)** — “Synthesize-and-reground” pipeline for multimodal scientific document reasoning data.
- **[Composable PRAG adapters](https://arxiv.org/abs/2604.26768)** — Separates document knowledge from task behavior for more reusable parametric retrieval modules.
- **[Anchored Confabulation](https://arxiv.org/abs/2604.25931)** — Shows that partial evidence can amplify confident hallucinations before fuller evidence helps.
- **[BioGraphletQA](https://arxiv.org/abs/2604.26048)** — Uses knowledge-graph “graphlets” to generate fact-grounded, complexity-controlled QA data.

### Efficiency, adaptation, and deployment
- **[Training-Free Adaptation via CAPT](https://arxiv.org/abs/2601.03423)** — Adapts newer general LLMs to clinical tasks using legacy clinical models without fresh continued pretraining.
- **[Module-wise Expert Pruning for LoRA-MoE](https://arxiv.org/abs/2604.26340)** — Prunes experts per module to make LoRA-MoE fine-tuning cheaper.
- **[SplitFT](https://arxiv.org/abs/2604.26388)** — Federated split-learning for privacy-preserving LLM fine-tuning.
- **[Unified Multi-task EEG with LoRA](https://arxiv.org/abs/2604.25131)** — Uses low-rank adaptation to share a self-supervised EEG backbone across tasks.
- **[Lightweight LLMs for Biomedical NER](https://arxiv.org/abs/2604.25920)** — Highlights output-format choice as a key variable for small-model extraction quality.
- **[Edge AI for Automotive VRU Safety](https://arxiv.org/abs/2604.26857)** — Applies distillation to preserve detection quality under edge deployment constraints.

### Domain, multilingual, and healthcare
- **[Domain-Adapted SLMs for Clinical Triage](https://arxiv.org/abs/2604.26766)** — Evaluates domain-adapted small models for reliable emergency triage support.
- **[Translating Under Pressure](https://arxiv.org/abs/2604.26597)** — Data-efficient crisis translation via retrieval and filtering from broader corpora.
- **[Cross-lingual ABSA](https://arxiv.org/abs/2604.26619)** — Benchmarks aspect-based sentiment transfer from zero-shot to full-resource settings.

### Safety, evaluation, and interpretability
- **[Safety Is Not Universal](https://arxiv.org/abs/2601.04389)** — Warns that aggregate safety scores can hide subgroup-specific failures.
- **[MoRFI](https://arxiv.org/abs/2604.26866)** — Uses monotonic sparse autoencoders to identify factual features shaped by post-training.
- **[Silicon Philosophers](https://arxiv.org/abs/2604.23575)** — Synthetic panels can match average human opinions while collapsing diversity of views.
- **[When Annotators Disagree, Topology Explains](https://arxiv.org/abs/2510.17548)** — Uses Mapper to analyze ambiguity and annotator disagreement in embedding space.
- **[Evaluation Revisited](https://arxiv.org/abs/2604.25923)** — Offers a taxonomy for structuring eval concerns more systematically.

## Key Takeaways
- **Fine-grained post-training is accelerating**: token-level, step-level, partial-solution, and heterogeneous-reward methods are replacing coarse sequence- or outcome-only optimization.
- **Efficiency is now a systems problem**: async RL, speculative rollout decoding, hyper-parallel decoding, distillation, expert pruning, and federated/split tuning all target the cost of deployment-scale post-training.
- **Grounding and faithfulness are getting sharper treatment**: new work focuses on counterfactual RAG data, multimodal regrounding, composable retrieval adapters, and failure modes where partial evidence worsens hallucination.
- **Evaluation is broadening beyond average-case metrics**: researchers are probing subgroup safety, preference-diversity collapse, ambiguity geometry, and agent-network failure modes.
- **Domain-specific and multilingual deployment remains a major frontier**: healthcare, crisis translation, EEG, biomedical extraction, and multilingual foundation modeling all point to more targeted adaptation strategies.
- **Commercial platforms are converging on full-stack workflows**: Together AI’s partnership reflects a broader push toward bundled data, tuning, eval, and deployment products.