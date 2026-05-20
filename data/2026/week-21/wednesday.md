## Weekly Digest — Fine-Tuning & Post-Training
*Filtered for fine-tuning/post-training relevance. No company affiliations were provided in the source summaries, so everything is grouped under **Academic / arXiv Research**.*

### Academic / arXiv Research

#### PEFT, Fine-Tuning, and Continual Learning
- [**HELLoRA**](https://arxiv.org/abs/2605.18795) — MoE-specific LoRA that prioritizes frequently activated experts.
- [**Hybrid-LoRA**](https://arxiv.org/abs/2605.18822) — Aims to narrow the quality gap between LoRA and full fine-tuning in post-training.
- [**LoRA vs. Full Fine-Tuning: A Theoretical Perspective**](https://arxiv.org/abs/2605.19018) — Analyzes when low-rank adapters can and cannot match full FT.
- [**Learning When to Adapt**](https://arxiv.org/abs/2605.19028) — Makes adaptation input-dependent instead of always-on.
- [**AR1-ZO**](https://arxiv.org/abs/2605.19767) — Topology-aware rank-1 zeroth-order queries for high-rank LoRA.
- [**Learning Rate Matters: Vanilla LoRA May Suffice for LLM Fine-tuning**](https://arxiv.org/abs/2602.04998) — Shows tuned vanilla LoRA can be stronger than many reported baselines suggest.
- [**Skill Neologisms: Towards Skill-based Continual Learning**](https://arxiv.org/abs/2605.04970) — Adds new skills with less catastrophic forgetting.
- [**Fine-tuning Large Language Model for Automated Algorithm Design**](https://arxiv.org/abs/2507.10614) — Studies domain FT for LLMs used in algorithm-search loops.
- [**EmbGen: Teaching with Reassembled Corpora**](https://arxiv.org/abs/2605.19394) — Builds synthetic instruction data from reassembled domain corpora for cheaper adaptation.
- [**Are Rationales Necessary and Sufficient?**](https://arxiv.org/abs/2605.19285) — Tests whether rationale supervision improves explainable misinformation detection.
- [**Self-Filtered Distillation with LLMs-generated Trust Indicators**](https://arxiv.org/abs/2510.05431) — Filters noisy synthetic rationales before distillation for patent classification.
- [**Investigating Cross-Modal Skill Injection**](https://arxiv.org/abs/2605.19523) — Maps efficient skill injection methods for VLM continual adaptation.
- [**Where Does Authorship Signal Emerge in Encoder-Based Language Models?**](https://arxiv.org/abs/2605.19908) — Shows scoring-head choice can strongly affect encoder FT outcomes.

#### RLHF, RLVR, and Reasoning Post-Training
- [**Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients**](https://arxiv.org/abs/2510.18924) — Corrects reward-noise bias in GRPO updates.
- [**Transformation-Augmented GRPO**](https://arxiv.org/abs/2601.22478) — Expands reasoning exploration with correctness-preserving transformations.
- [**LambdaPO**](https://arxiv.org/abs/2605.19416) — Replaces coarse group baselines with finer-grained credit assignment.
- [**Learning-Zone Energy**](https://arxiv.org/abs/2605.17003) — Selects RL prompts in the model’s learnable zone to save rollout budget.
- [**CEPO**](https://arxiv.org/abs/2605.19436) — RLVR self-distillation that emphasizes evidence-bearing reasoning tokens.
- [**Rethinking Muon Beyond Pretraining**](https://arxiv.org/abs/2605.19282) — Finds Muon can hurt RLVR/VLA post-training and proposes a high-pass fix.
- [**Critique-Guided Distillation for Robust Reasoning via Refinement**](https://arxiv.org/abs/2505.11628) — Distills critique/refinement ability without requiring critique output at inference.
- [**Backtracking When It Strays**](https://arxiv.org/abs/2605.19433) — Mitigates reasoning-distillation failures when intermediate steps drift off track.
- [**Taming the Thinker**](https://arxiv.org/abs/2605.19358) — Adapts reasoning depth with conditional entropy shaping.
- [**GoLongRL**](https://arxiv.org/abs/2605.19577) — Open long-context RLVR recipe focused on capability coverage and multitask alignment.
- [**Text-to-SPARQL Generation with Reinforcement Learning**](https://arxiv.org/abs/2605.20066) — Uses GRPO-style RL to learn executable SPARQL without gold queries.
- [**ZeroSearch**](https://arxiv.org/abs/2505.04588) — Trains search behavior without live search-engine interaction.

#### Alignment, Reward Modeling, and Internal Training Signals
- [**Eliminating Inductive Bias in Reward Models with Information-Theoretic Guidance**](https://arxiv.org/abs/2512.23461) — Reduces shortcut learning in reward models.
- [**Contrastive Reasoning Alignment (CRAFT)**](https://arxiv.org/abs/2603.17305) — Aligns hidden representations and reasoning traces for stronger jailbreak robustness.
- [**Lying Is Just a Phase**](https://arxiv.org/abs/2605.18838) — Reports a scaling threshold where reasoning and truthfulness begin to align.

#### Multimodal, Tool Use, and Specialized Post-Training
- [**From Seeing to Thinking**](https://arxiv.org/abs/2605.20177) — Improves VLM post-training by decoupling perception from reasoning.
- [**Are Tools Always Beneficial?**](https://arxiv.org/abs/2605.19852) — Trains multimodal LLMs to invoke tools selectively, not by default.
- [**ReacTOD**](https://arxiv.org/abs/2605.19077) — Bounded neuro-symbolic zero-shot dialogue state tracking for more predictable task behavior.

#### Agents, Evaluation, and Data Reliability
- [**Rewriting History**](https://arxiv.org/abs/2510.14261) — Practical recipe for causal data-intervention studies on model behavior.
- [**Towards Consistent Detection of Cognitive Distortions**](https://arxiv.org/abs/2511.01482) — Uses repeated LLM annotation and dataset-agnostic evaluation to improve label consistency.
- [**Can Deep Research Agents Retrieve and Organize?**](https://arxiv.org/abs/2601.12369) — Evaluates whether research agents can build expert-like taxonomies, not just retrieve papers.
- [**Agent Meltdowns**](https://arxiv.org/abs/2605.19149) — Defines agent failure cascades where “helpful” actions compound errors.
- [**Time to REFLECT**](https://arxiv.org/abs/2605.19196) — Tests whether LLM judges are reliable for evidence-based research agents.
- [**SciCustom**](https://arxiv.org/abs/2605.19357) — Framework for custom scientific-capability evaluations.

## Key Takeaways
- **PEFT is getting more architecture-aware and input-aware, but simple baselines still matter.** Representative work: [HELLoRA](https://arxiv.org/abs/2605.18795), [Learning When to Adapt](https://arxiv.org/abs/2605.19028), [Learning Rate Matters](https://arxiv.org/abs/2602.04998).
- **Reasoning RL is moving beyond vanilla GRPO toward better credit assignment, exploration, noise robustness, and prompt selection.** See [Noise-corrected GRPO](https://arxiv.org/abs/2510.18924), [LambdaPO](https://arxiv.org/abs/2605.19416), [Learning-Zone Energy](https://arxiv.org/abs/2605.17003).
- **Distillation and synthetic supervision are becoming more selective.** Researchers are filtering noisy rationales, distilling critique behavior, and correcting off-trajectory reasoning with methods like [Self-Filtered Distillation](https://arxiv.org/abs/2510.05431), [Critique-Guided Distillation](https://arxiv.org/abs/2505.11628), and [Backtracking When It Strays](https://arxiv.org/abs/2605.19433).
- **Multimodal and agent post-training is shifting toward adaptive control.** Reasoning depth, tool invocation, perception bottlenecks, and recovery behavior are now key levers: [Taming the Thinker](https://arxiv.org/abs/2605.19358), [Are Tools Always Beneficial?](https://arxiv.org/abs/2605.19852), [From Seeing to Thinking](https://arxiv.org/abs/2605.20177), [Agent Meltdowns](https://arxiv.org/abs/2605.19149).
- **Evaluation remains a major bottleneck.** New work focuses on causal data analysis, domain-specific evals, research synthesis quality, and validating LLM judges: [Rewriting History](https://arxiv.org/abs/2510.14261), [SciCustom](https://arxiv.org/abs/2605.19357), [Can Deep Research Agents Retrieve and Organize?](https://arxiv.org/abs/2601.12369), [Time to REFLECT](https://arxiv.org/abs/2605.19196).
- **Alignment research is probing deeper internal signals and scaling effects.** Notable examples are [CRAFT](https://arxiv.org/abs/2603.17305) and [Lying Is Just a Phase](https://arxiv.org/abs/2605.18838).