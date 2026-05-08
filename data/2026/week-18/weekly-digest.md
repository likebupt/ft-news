# Weekly Finetuning & Post-Training Update

## TL;DR
This week’s clearest signals were around safer agentic systems, privacy-hardening for customized models, tighter data→tune→eval workflows, and a wave of papers aimed at making RL/post-training cheaper, more controllable, and easier to evaluate.

## Top Stories
- Microsoft Research showed that networks of individually “safe” agents can still produce unsafe behavior when composed, reinforcing the need for multi-agent evals and post-training targets beyond single-agent alignment [Read more](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/)
- Amazon Science recreated training-data extraction attacks and outlined cryptographic defenses, making privacy testing feel increasingly mandatory for enterprise finetuning on sensitive data [Read more](https://www.amazon.science/blog/preserving-the-privacy-of-ai-training-data)
- Together AI and Adaption integrated data optimization, finetuning, evaluation, and deployment, signaling market demand for tighter closed-loop post-training workflows rather than siloed tools [Read more](https://www.together.ai/blog/announcing-together-ai-and-adaption-partnership)
- DORA introduced asynchronous RL for LLM post-training that overlaps rollouts and optimization, directly targeting one of the biggest cost centers in RLHF/RLAIF pipelines [Read more](https://arxiv.org/abs/2604.26256)
- EvoSelect proposed an evolutionary synthetic-data selection loop for targeted adaptation, pointing to a practical route for improving task performance with much less labeled data [Read more](https://arxiv.org/abs/2604.26170)

## By Company

**OpenAI / Microsoft**
- OpenAI and Microsoft announced amended partnership terms aimed at longer-term clarity, which should reduce platform uncertainty for enterprises building custom models on the Azure/OpenAI stack [Source](https://openai.com/index/next-phase-of-microsoft-partnership)

**Apple**
- Apple’s LaDiR combines LLMs with latent diffusion for more holistic reasoning refinement, hinting at post-training alternatives to standard left-to-right chain-of-thought optimization [Source](https://machinelearning.apple.com/research/ladir)

**Tilde**
- TildeOpen LLM launched as a 30B open model for 34 European languages using curriculum learning, a useful signal for multilingual finetuning recipes and data balancing [Source](https://arxiv.org/abs/2603.08182)

## Notable Papers

**Data, Adaptation, and Efficiency**
- CAPT adapts new general LLMs using legacy clinical specialists without retraining, offering a cheaper path than re-finetuning every new base model for regulated domains [Paper](https://arxiv.org/abs/2601.03423)
- Adaptive module-wise expert pruning for LoRA-MoE cuts experts differently across transformer blocks, potentially lowering PEFT memory/compute without giving up much adaptation capacity [Paper](https://arxiv.org/abs/2604.26340)
- TinyR1-32B-Preview uses branch-merge distillation to compress reasoning models more effectively than standard recipes, improving the path from expensive teachers to deployable students [Paper](https://arxiv.org/abs/2503.04872)
- SplitFT proposes federated split learning for privacy-sensitive, resource-constrained LLM finetuning, relevant for customers that cannot centralize data or host full training stacks [Paper](https://arxiv.org/abs/2604.26388)
- Decoupling knowledge and task subspaces in composable PRAG suggests modular adapter training where knowledge updates and task behavior can be maintained independently [Paper](https://arxiv.org/abs/2604.26768)
- Faithfulness-QA forces RAG models to prefer retrieved evidence over parametric memory via counterfactual entity substitution, giving a sharper target for context-faithful post-training [Paper](https://arxiv.org/abs/2604.25313)

**RL, Reward, and Agent Training**
- ClawGym provides a scalable way to generate verifiable trajectories and diagnose failures in persistent tool/file environments, improving training data quality for agent finetuning [Paper](https://arxiv.org/abs/2604.26904)
- Verified Critical Step Optimization improves long-horizon agent credit assignment by optimizing verifiable intermediate steps instead of relying only on noisy outcome rewards [Paper](https://arxiv.org/abs/2602.03412)
- reward-lens adds mechanistic interpretability for scalar reward models, which could help catch spurious reward proxies before policy optimization amplifies them [Paper](https://arxiv.org/abs/2604.26130)
- PAINT blends token-level supervision with partial-solution trajectories closer to test-time behavior, offering a middle ground between SFT and sparse-reward RL for reasoning [Paper](https://arxiv.org/abs/2604.26573)
- TLPO applies token-level policy optimization to reduce multilingual “language confusion,” showing finer-grained RL can better enforce output constraints like target language [Paper](https://arxiv.org/abs/2604.26553)
- Failure Modes of Maximum Entropy RLHF shows preference objectives that look elegant offline can become unstable online, a useful caution for interactive RLHF designs [Paper](https://arxiv.org/abs/2509.20265)
- System-Integrated Speculative Decoding accelerates rollout generation for RL post-training without changing the optimizer, a directly practical systems win for large-scale runs [Paper](https://arxiv.org/abs/2604.26779)
- Entropy Centroids proposes using model entropy instead of a trained reward model to pick the best sample in test-time scaling, which could simplify best-of-N stacks [Paper](https://arxiv.org/abs/2604.26173)
- SWE-Edit restructures code editing into inspection, planning, and execution, producing cleaner trajectories and action spaces for code-agent post-training [Paper](https://arxiv.org/abs/2604.26102)

**Evaluation, Safety, and Multimodal**
- MINOS introduces a learned evaluator for image↔text generation, strengthening the judge-model stack for multimodal alignment and preference optimization [Paper](https://arxiv.org/abs/2506.02494)
- Safety Is Not Universal argues aggregate safety scores can mask subgroup failures, pushing finetuning teams toward subgroup-aware objectives and evals [Paper](https://arxiv.org/abs/2601.04389)
- Anchored Confabulation finds that partially grounded reasoning can temporarily increase confident hallucinations, suggesting calibration should be tested under incomplete evidence, not just fully grounded settings [Paper](https://arxiv.org/abs/2604.25931)
- Teaching LLM to be Persuasive uses heterogeneous rewards to train negotiation agents that must meet business goals while following SOPs and safety guardrails over long dialogues [Paper](https://arxiv.org/abs/2510.04214)

## What This Means for Us
- Foundry should keep investing in a closed-loop workflow spanning data curation, synthetic-data selection, finetuning, evaluation, and deployment, because the competitive stack is moving toward faster iteration on data quality rather than just model knobs [Source](https://www.together.ai/blog/announcing-together-ai-and-adaption-partnership)
- We should expand post-training evals beyond single-model quality to include privacy leakage, multi-agent interactions, subgroup safety, and partial-grounding hallucination checks before customer finetunes ship [Source](https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/)
- RL/post-training efficiency is becoming a product differentiator, so rollout acceleration, token-level control, and reward-model observability are worth prioritizing in the Foundry roadmap [Source](https://arxiv.org/abs/2604.26256)