# Weekly Finetuning & Post-Training Update

**TL;DR** — The week’s clearest signal was a shift from static one-shot tuning toward adaptive, production-aware post-training: dynamic data weighting, optimizer/replay choices, explicit tool/agent supervision, and safety-preserving update methods all advanced meaningfully. [Read more](https://arxiv.org/abs/2605.05227)

## Top Stories
- **OpenAI / Codex ops**: OpenAI said Codex is run with sandboxing, approval gates, network controls, and agent-native telemetry—exactly the kind of traces that can become high-value data for future safety tuning and reward modeling of coding agents. [Read more](https://openai.com/index/running-codex-safely)
- **Online data reweighting**: Training-coupled online reweighting beat offline data selection/mixing under shifts, making dynamic curation one of the most actionable ideas for SFT and continual post-training. [Read more](https://arxiv.org/abs/2605.05227)
- **Optimizer-model consistency**: Matching the pretraining optimizer during full finetuning reduced forgetting while matching or improving downstream quality, suggesting current FT defaults may be leaving capability on the table. [Read more](https://arxiv.org/abs/2605.06654)
- **RVPO for multi-objective RLHF**: RVPO adds variance regularization so gains on one reward cannot hide failures on safety, formatting, or other bottleneck objectives—a common alignment failure mode. [Read more](https://arxiv.org/abs/2605.05750)
- **Tool-integrated reasoning**: A new recipe showed that simply exposing tools can hurt performance unless models are explicitly trained when and how to use them. [Read more](https://arxiv.org/abs/2605.06326)

## By Company

**Amazon**
- Amazon argued responsible AI should span data, tuning, evaluation, and red-teaming as one lifecycle rather than a last-step safety patch, reinforcing integrated post-training stacks. [Source](https://www.amazon.science/blog/building-trust-into-ai)

**Together AI**
- Together AI showed that million-token context serving is primarily an inference-systems problem—KV-cache compression, prefix caching, and hardware-aware kernels now gate the value of long-context post-training. [Source](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)

**Zyphra / AMD**
- Zyphra’s ZAYA1-8B report suggests strong reasoning post-training is feasible with a small-active-parameter MoE on AMD infrastructure, widening hardware and cost options. [Source](https://arxiv.org/abs/2605.05365)

## Notable Papers

**RL / Post-training**
- **Reset Replay** reduces primacy bias in long RL/preference optimization runs and improves sample efficiency. [Paper](https://arxiv.org/abs/2508.06412)
- **P²O** jointly optimizes prompts and policy in RLVR, recovering learning signal on hard samples where all rollouts initially fail. [Paper](https://arxiv.org/abs/2603.21877)
- **Tsallis Loss Continuum** offers a unified view of SFT and RLVR, helping explain why SFT→RLVR curricula work well. [Paper](https://arxiv.org/abs/2604.25907)
- **Near-Policy Distillation** approximates on-policy distillation with asynchronous generation and selective packing, lowering the cost of student-model post-training. [Paper](https://arxiv.org/abs/2605.05940)
- **Unified Pair-GRPO** unifies pairwise GRPO variants to lower gradient variance and improve controllability in preference optimization. [Paper](https://arxiv.org/abs/2605.06375)
- **Positive-only Policy Optimization** learns from successful verifiable-reward rollouts without explicitly collecting failures, simplifying RLVR data generation. [Paper](https://arxiv.org/abs/2605.06650)
- **Optimal-transport Reward Modeling** makes reward models more robust to noisy preference labels, a common RLHF failure point. [Paper](https://arxiv.org/abs/2605.06036)
- **Rubric-based Self-play** bootstraps synthetic post-training signals from pretraining text for open-ended tasks, reducing dependence on human labels. [Paper](https://arxiv.org/abs/2604.20051)
- **OPSD after RLVR** argues reasoning capability should be built with RLVR first and compacted afterward, supporting a two-stage capability-then-efficiency stack. [Paper](https://arxiv.org/abs/2605.06188)
- **Correct Is Not Enough** proposes executor-grounded rewards so planning models are trained on faithful reasoning, not lucky correct answers. [Paper](https://arxiv.org/abs/2605.03862)

**Continual tuning / PEFT / composition**
- **CRAFT** adds routed low-rank interventions instead of updating base weights, offering PEFT-style continual adaptation with less forgetting. [Paper](https://arxiv.org/abs/2605.05732)
- **Adapter Placement** shows a few well-placed LoRA adapters can outperform broad placement at lower trainable-parameter budgets. [Paper](https://arxiv.org/abs/2605.06183)
- **Attribution-guided Continual Learning** uses attribution signals to decide what to update, aiming to reduce forgetting across sequential finetunes. [Paper](https://arxiv.org/abs/2605.05285)
- **Fréchet Averages for Model Merging** argues symmetry-aware merge operators beat naive parameter averaging when combining specialized checkpoints. [Paper](https://arxiv.org/abs/2604.27155)

**Safety / agents / evaluation**
- **Safety Anchor** uses geometric bottlenecks to resist harmful finetuning, targeting safety removal via persistent or adversarial updates. [Paper](https://arxiv.org/abs/2605.05995)
- **StraTA** abstracts long agent trajectories into higher-level units to improve exploration and credit assignment in agent RL. [Paper](https://arxiv.org/abs/2605.06642)
- **When2Speak** adds supervision for turn-taking timing, a missing post-training signal for meetings, group chat, and multi-agent settings. [Paper](https://arxiv.org/abs/2605.05626)
- **One Turn Too Late** defends against multi-turn attacks that hide malicious intent across dialogue history, highlighting the need for trajectory-level safety training. [Paper](https://arxiv.org/abs/2605.05630)
- **Evaluation-context Divergence** shows benchmark-like prompts can elicit materially different behavior than deployment-like prompts, challenging current eval assumptions. [Paper](https://arxiv.org/abs/2605.06327)
- **Prompt-space Perturbation for GRPO** broadens reasoning exploration with lightweight prompt perturbations, helping with zero-advantage failures. [Paper](https://arxiv.org/abs/2605.05566)

## What This Means for Us
- **Expose adaptive-training knobs**: Foundry Finetuning should make optimizer presets, replay/weighting strategies, and curriculum controls easier to configure, since multiple papers point to gains without changing the base model. [Context](https://arxiv.org/abs/2605.06654)
- **Make agent/tool traces first-class**: tool calls, approvals, sandbox outcomes, and dialogue state increasingly look like core training/eval assets rather than observability exhaust. [Context](https://arxiv.org/abs/2605.06326)
- **Invest in safe continual-tuning workflows**: better PEFT placement/merging plus protections against safety stripping and forgetting could become a strong enterprise differentiator. [Context](https://arxiv.org/abs/2605.05995)