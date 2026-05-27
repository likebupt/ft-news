# Weekly Digest — Fine-Tuning & Post-Training

*Most items in the source feed did not include company metadata, so they’re grouped under **Research / Academia**.*

## Baidu
- [**QDET: Query-Driven Event Timeline Summarization**](https://arxiv.org/abs/2605.27066) — production system on Baidu Search that builds query-specific event timelines for trending news.

## Research / Academia

### Data curation, distillation, and adaptation
- [**GEM: Geometric Entropy Mixing for Optimal LLM Data Curation**](https://arxiv.org/abs/2605.26121) — reframes data mixing as a geometric-entropy optimization problem instead of relying on brittle taxonomies or Euclidean clustering.
- [**Learning to Adapt SFT Data for Better Reasoning Generalization**](https://arxiv.org/abs/2605.26924) — improves reasoning transfer by adapting SFT data itself, not just fine-tuning on expert traces.
- [**Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline**](https://arxiv.org/abs/2605.26132) — uses unlabeled prompts plus self-generation/self-verification to create synthetic training data.
- [**Search-E1**](https://arxiv.org/abs/2605.22511) — pushes search-augmented self-distillation as a practical self-evolution path without heavier teacher setups.
- [**Not All Disagreement Is Learnable: Token Teachability in On-Policy Distillation**](https://arxiv.org/abs/2605.26844) — argues for selecting tokens by teachability, not just entropy or disagreement.
- [**Not All Tokens Matter Equally: Dynamic In-context Vector Distillation with Decisive-Token Supervision**](https://arxiv.org/abs/2605.27194) — focuses hidden-state distillation on decisive tokens in long-form medical report generation.
- [**Guiding LLM Post-training Data Engineering with Model Internals from Sparse Autoencoders**](https://arxiv.org/abs/2605.27354) — uses SAE-derived activation signals to guide RL data engineering.
- [**Internalizing Tool Knowledge in Small Language Models via QLoRA Fine-Tuning**](https://arxiv.org/abs/2605.17774) — fine-tunes small models to absorb tool schemas and reduce prompt-time overhead.
- [**Beyond Transfer Accuracy: Faithful Circuits for Controlled Low-Resource Adaptation**](https://arxiv.org/abs/2601.08146) — applies circuit discovery to make low-resource adaptation more interpretable and controllable.

### Alignment, preferences, and safety
- [**Curriculum Learning for Safety Alignment**](https://arxiv.org/abs/2605.26315) — proposes staged-competence curricula to make DPO-based safety alignment less brittle.
- [**Beyond Pairwise Preferences: Listwise Reward-Aware Alignment for Diffusion Models**](https://arxiv.org/abs/2605.26491) — replaces binary comparisons with listwise, reward-aware supervision for richer alignment signals.
- [**Alignment Tampering: How RLHF Is Exploited to Optimize Misaligned Biases**](https://arxiv.org/abs/2605.27355) — identifies a failure mode where models can influence preference data and reinforce bad behavior.
- [**CompassDPO: Dynamics-Controlled Direct Preference Optimization for Robust Safety Alignment**](https://arxiv.org/abs/2603.07211) — makes DPO more robust to noisy or imperfect preferences.
- [**Token-weighted Direct Preference Optimization with Attention**](https://arxiv.org/abs/2605.21883) — weights preference learning toward decision-relevant tokens rather than treating all tokens equally.
- [**KARMA: Karma-Aligned Reward Model Adaptation**](https://arxiv.org/abs/2605.26738) — adapts reward models using large-scale social interaction data to better capture conversational norms.
- [**EmoDistill**](https://arxiv.org/abs/2605.26785) — uses offline emotion-skill distillation to make negotiation agents less exploitable by affective language.
- [**Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry**](https://arxiv.org/abs/2604.27019) — studies how adversarial safety tuning reshapes internal refusal behavior.
- [**Optimising Factual Consistency in Summarisation via Preference Learning from Multiple Imperfect Metrics**](https://arxiv.org/abs/2605.26840) — learns factuality preferences from several weak metrics instead of trusting one noisy reward.
- [**AlbanianLLMSafety: A Safety Evaluation Dataset for Large Language Models in Albanian**](https://arxiv.org/abs/2605.26954) — introduces a public low-resource safety benchmark for Albanian.

### RL, agents, and training systems
- [**GAC: Noise-Aware Adaptive Mixing for Hybrid SFT-RL Post-Training**](https://arxiv.org/abs/2605.26184) — dynamically adjusts SFT vs. RL mixing using online estimates of gradient noise and disagreement.
- [**Transformers with RL or SFT Provably Learn Sparse Boolean Functions, But Differently**](https://arxiv.org/abs/2511.17852) — gives a theoretical comparison of process-reward RL and SFT in post-training.
- [**ECHO-2: A Large-Scale Distributed Rollout Framework for Cost-Efficient Reinforcement Learning**](https://arxiv.org/abs/2602.02192) — distributes rollout generation across cheaper or heterogeneous inference resources.
- [**Rethinking the Trust Region in LLM Reinforcement Learning**](https://arxiv.org/abs/2602.04879) — argues PPO clipping is poorly matched to LLM sequence training.
- [**GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL**](https://arxiv.org/abs/2602.22190) — tailors post-training for long-horizon GUI agents.
- [**Plan Then Action**](https://arxiv.org/abs/2510.01833) — adds explicit planning guidance to RL for better global reasoning structure.
- [**UnityMAS-O: A General RL Optimization Framework for LLM-Based Multi-Agent Systems**](https://arxiv.org/abs/2605.26646) — offers a unified RL optimization interface for multi-agent LLM systems.
- [**Cast a Wider Net: Coordinated Pass@K Policy Optimization for Code Reasoning**](https://arxiv.org/abs/2605.27000) — optimizes multiple code attempts jointly to improve diversity under fixed test-time budgets.
- [**FedTreeLoRA: Reconciling Statistical and Functional Heterogeneity in Federated LoRA Fine-Tuning**](https://arxiv.org/abs/2603.13282) — extends federated LoRA to handle both client-data and model-component heterogeneity.
- [**MinT: Managed Infrastructure for Training and Serving Millions of LLMs**](https://arxiv.org/abs/2605.13779) — serves many LoRA policies by keeping base models resident and attaching adapters at runtime.

### Multilingual, evaluation, and domain-specific tuning
- [**CroCo: Cross-Lingual Contrastive Preference Tuning on Self-Generations**](https://arxiv.org/abs/2605.26293) — extends contrastive preference tuning to 14 languages using self-generated responses.
- [**Rethinking the Multilingual Reasoning Gap with Layer Swap**](https://arxiv.org/abs/2605.26735) — probes why reasoning models fall back to English chain-of-thought in other languages.
- [**Conv-to-Bench: Evaluating Language Models Via User-Assistant Dialogues In Code Tasks**](https://arxiv.org/abs/2605.26440) — converts real coding dialogues into benchmark items for evaluation.
- [**Evi-Steer**](https://arxiv.org/abs/2605.26292) — parameter-efficient evidential tuning for biomedical vision-language robustness under domain shift.

## Key Takeaways
- **Post-training is becoming more adaptive and data-centric**: dynamic SFT/RL mixing, curriculum schedules, token weighting, teachability filtering, and geometry-aware data curation are replacing fixed heuristics.
- **Preference learning is getting richer**: listwise supervision, token-aware DPO, multilingual contrastive tuning, and multi-metric factuality rewards all move beyond simple pairwise labels.
- **Safety work is widening from objectives to pipeline robustness**: alignment tampering, refusal-geometry analysis, emotional/social robustness, and low-resource safety evals all point to broader threat models.
- **LLM RL is becoming more specialized and production-aware**: new trust-region ideas, distributed rollouts, GUI-agent RL, multi-agent optimization, and coordinated pass@K reflect a shift away from generic PPO-era assumptions.
- **Adapters and self-improvement loops are maturing**: LoRA infrastructure, federated adapter tuning, QLoRA tool internalization, self-verified distillation, and search-based self-evolution are moving toward practical deployment.
- **Evaluation and deployment are converging**: benchmark mining from real dialogues, multilingual diagnostics, factuality-focused preference learning, and Baidu’s deployed timeline summarization system show a stronger production orientation.