# Weekly Digest

*No company metadata was provided in the source summaries, so everything is grouped under **Academic / arXiv**.*

## Academic / arXiv

### Training Signals, RL, and Reasoning
- **[ODRPO](https://arxiv.org/abs/2605.12667)** — Treats noisy multi-level judge scores as ordinal signals to make RLAIF-style optimization more robust.
- **[Reflection-Enhanced Self-Distillation](https://arxiv.org/abs/2605.12741)** — Uses reflection to turn rich environment feedback into stronger learning signals when successful trajectories are rare.
- **[Sharpness-Guided GRPO](https://arxiv.org/abs/2511.00066)** — Adds probability shaping to GRPO to improve robustness and generalization under verifiable rewards.
- **[PEPO](https://arxiv.org/abs/2602.06239)** — A pessimistic, single-step DPO-style method aimed at reducing preference over-optimization.
- **[Verifiable Process Supervision](https://arxiv.org/abs/2605.12519)** — Rewards intermediate reasoning quality instead of only final answers.
- **[STOP](https://arxiv.org/abs/2605.13165)** — Prunes low-yield long-form reasoning during on-policy training to cut “overthinking” cost.
- **[Olympiad Reasoning via Unified Scaling](https://arxiv.org/abs/2605.13301)** — Shows strong math/science reasoning can come from a streamlined scaling and post-training recipe.
- **[CPMobius](https://arxiv.org/abs/2602.02979)** — Uses an iterative coach-player setup to improve reasoning without labeled task data.
- **[Table-R1](https://arxiv.org/abs/2505.12415)** — Applies region-based RL to table understanding instead of relying only on linearized text.

### Fine-Tuning, PEFT, and Continual Learning
- **[Early Data Exposure Improves Robustness to Subsequent Fine-Tuning](https://arxiv.org/abs/2605.12705)** — Suggests when a capability is learned affects how well it survives later tuning.
- **[Gradient-Surgery LoRA Initialization](https://arxiv.org/abs/2605.12752)** — Reduces interference in continual LoRA tuning through better adapter initialization.
- **[Data Difficulty and the Generalization–Extrapolation Tradeoff](https://arxiv.org/abs/2605.12906)** — Finds SFT data difficulty can shift models between standard generalization and harder extrapolation.
- **[Program Memory for Continual Fine-Tuning](https://arxiv.org/abs/2605.13162)** — Adds an explicit memory mechanism for sequential PEFT updates.
- **[Catastrophic Forgetting in LoRA via Mean-Field Attention Dynamics](https://arxiv.org/abs/2402.15415)** — Provides a mechanistic explanation for forgetting in LoRA.
- **[LoRA-Mixer](https://arxiv.org/abs/2507.00029)** — Routes through modular low-rank experts to improve multi-task specialization.
- **[PEFT-Bench](https://arxiv.org/abs/2511.21285)** — Benchmarks PEFT methods across quality, efficiency, and cost.
- **[PEFT-Factory](https://arxiv.org/abs/2512.02764)** — Unifies implementation and deployment across multiple PEFT methods.
- **[MinT](https://arxiv.org/abs/2605.13779)** — Infrastructure for training/serving millions of LoRA-adapted models without materializing full checkpoints.

### Test-Time Adaptation, Merging, and Compression
- **[Query-Conditioned Test-Time Self-Training](https://arxiv.org/abs/2605.13369)** — Adapts model parameters at inference time based on the specific query.
- **[Many-Shot CoT-ICL](https://arxiv.org/abs/2605.13511)** — Studies long-context, many-shot chain-of-thought prompting as a stronger adaptation regime than classic few-shot ICL.
- **[Entropy-Aware Reward Guidance for Diffusion LMs](https://arxiv.org/abs/2602.05000)** — Makes reward-guided alignment more practical for discrete diffusion language models.
- **[Adaptive Steering and Remasking](https://arxiv.org/abs/2605.13043)** — Adds decoding-time controls to suppress harmful intermediate generations in diffusion LMs.
- **[Preserve-Then-Quantize](https://arxiv.org/abs/2602.02001)** — Balances low-rank correction between preserving important structure and fixing quantization error.
- **[TokAlign++](https://arxiv.org/abs/2605.13429)** — Improves vocabulary/token alignment across models with different tokenizers.
- **[DiM3](https://arxiv.org/abs/2605.12960)** — A training-free merge method for adding multilingual capability to multimodal models.
- **[LLM as Token Compressor and Decompressor](https://arxiv.org/abs/2603.25340)** — Uses lightweight LoRA fine-tuning to compress long-context inputs into variable-length token representations.

### Data Generation, Evaluation, Safety, and Personalization
- **[ToolWeave](https://arxiv.org/abs/2605.12521)** — Generates more realistic multi-turn tool-use dialogues by aligning goals, dialogue state, and tool affordances.
- **[Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution](https://arxiv.org/abs/2605.13411)** — Keeps safety tuning fresh with an externalized red-team / defense loop.
- **[RTLC](https://arxiv.org/abs/2605.13695)** — Improves LLM-as-a-judge performance with a prompt-only research/teach/critique scaffold.
- **[Automated Rubrics for Medical Dialogue Evaluation](https://arxiv.org/abs/2601.15161)** — Uses fine-grained rubrics to catch subtle clinical hallucinations and unsafe advice.
- **[Data-Mediated Transfer and Emergent Misalignment](https://arxiv.org/abs/2605.12798)** — Frames harmful fine-tuning effects as transfer through existing model representations.
- **[Backdoor Collapse](https://arxiv.org/abs/2510.10265)** — Defends against unknown backdoors in public checkpoints by aggregating known backdoor patterns.
- **[Alignment Reduces Expressed but Not Encoded Gender Bias](https://arxiv.org/abs/2603.24125)** — Finds alignment can clean up outputs while leaving latent bias in representations.
- **[PRISM-X](https://arxiv.org/abs/2605.13307)** — Examines personalized fine-tuning with both real and simulated users.

### Domain, Multilingual, and Low-Resource Adaptation
- **[Continual Pre-training for Tibetan LLMs](https://arxiv.org/abs/2507.09205)** — Details a low-resource scaling pipeline for Tibetan across dense and MoE models.
- **[Polymer-Composite Additive Manufacturing Adaptation](https://arxiv.org/abs/2605.12516)** — Compares RAG and fine-tuning for domain adaptation in a specialized engineering workflow.
- **[Vividh-ASR](https://arxiv.org/abs/2605.13087)** — Introduces a Hindi/Malayalam ASR benchmark highlighting “studio-bias” in speech fine-tuning.
- **[WARDEN](https://arxiv.org/abs/2605.13846)** — Shows endangered-language transcription/translation for Wardaman→English with only 6 hours of training data.

## Key Takeaways
- **Richer supervision is a major trend** — papers are moving beyond brittle scalar rewards toward ordinal rewards, process supervision, reflection, and rubric-based evaluation. See **[ODRPO](https://arxiv.org/abs/2605.12667)**, **[Verifiable Process Supervision](https://arxiv.org/abs/2605.12519)**, and **[Automated Rubrics](https://arxiv.org/abs/2601.15161)**.
- **Continual tuning and PEFT remain core bottlenecks** — research is attacking forgetting through training order, adapter initialization, explicit memory, mechanistic theory, and better infra/benchmarks. See **[Early Data Exposure](https://arxiv.org/abs/2605.12705)**, **[Program Memory](https://arxiv.org/abs/2605.13162)**, **[PEFT-Bench](https://arxiv.org/abs/2511.21285)**, and **[MinT](https://arxiv.org/abs/2605.13779)**.
- **Cheaper adaptation is expanding beyond full retraining** — test-time self-training, many-shot ICL, model merging, tokenizer alignment, and compression are all pushing capability transfer into lighter-weight regimes. See **[Query-Conditioned Test-Time Self-Training](https://arxiv.org/abs/2605.13369)**, **[Many-Shot CoT-ICL](https://arxiv.org/abs/2605.13511)**, **[DiM3](https://arxiv.org/abs/2605.12960)**, and **[TokAlign++](https://arxiv.org/abs/2605.13429)**.
- **Safety work is getting more nuanced** — newer papers focus on hidden failure modes like transfer-induced misalignment, backdoors, unsafe diffusion trajectories, and latent bias that survives alignment. See **[Data-Mediated Transfer](https://arxiv.org/abs/2605.12798)**, **[Backdoor Collapse](https://arxiv.org/abs/2510.10265)**, **[Adaptive Steering and Remasking](https://arxiv.org/abs/2605.13043)**, and **[Encoded Gender Bias](https://arxiv.org/abs/2603.24125)**.
- **Low-resource and domain-specific adaptation remains active** — speech, endangered languages, industrial domains, tables, and Tibetan modeling show post-training is spreading well beyond generic English chat. See **[WARDEN](https://arxiv.org/abs/2605.13846)**, **[Vividh-ASR](https://arxiv.org/abs/2605.13087)**, **[Polymer-Composite Adaptation](https://arxiv.org/abs/2605.12516)**, and **[Tibetan Continual Pre-training](https://arxiv.org/abs/2507.09205)**.