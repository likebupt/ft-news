# Weekly Digest — Fine-Tuning & Post-Training

*Most papers in this batch did not include clear affiliations, so they’re grouped under **Open Research / arXiv**. Only clearly branded work is grouped under a named company.*

## Baidu
- **ERNIE-Image Technical Report** — Open-source **8B single-stream DiT** text-to-image model; emphasizes large-scale data mining and higher-quality supervision to narrow the open/closed image-model gap. [Read more](https://arxiv.org/abs/2605.25347)

## Open Research / arXiv

### Efficient adaptation, PEFT, and distributed tuning
- **Signs Beat Floats: Low-Rank Double-Binary Adaptation for On-Device Fine-Tuning** — Binary/sign-based low-rank adapters remove the extra floating-point LoRA branch for on-device tuning of quantized LLMs. [Read more](https://arxiv.org/abs/2605.24058)
- **RotMoLE: Enhancing Mixture of Low-Rank Experts through Rotational Gating Mechanism** — Adds rotational gating to mixture-of-low-rank-experts PEFT for better domain routing. [Read more](https://arxiv.org/abs/2605.25565)
- **TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks** — Reduces memory and uplink costs for privacy-preserving split fine-tuning on edge devices. [Read more](https://arxiv.org/abs/2605.23988)
- **SLAP: Stratified Loss-based Pruning for On-Policy Data-Efficient Instruction Tuning** — Prunes instruction-tuning data by loss to cut training cost while preserving useful diversity. [Read more](https://arxiv.org/abs/2605.23969)
- **Federated Sketching LoRA** — Sketching-based LoRA makes federated fine-tuning more flexible across heterogeneous clients. [Read more](https://arxiv.org/abs/2501.19389)
- **FLoRIST** — Uses singular value thresholding to improve the communication/compute/accuracy trade-off in federated LoRA. [Read more](https://arxiv.org/abs/2506.09199)
- **Prism** — Reproducible infrastructure for scalable multimodal continual instruction tuning. [Read more](https://arxiv.org/abs/2605.26110)
- **Llamion Technical Report** — Converts Orion-14B into Llama-family 14B models with a knowledge-preserving transformation recipe. [Read more](https://arxiv.org/abs/2605.25676)
- **On the Limits of Model Merging for Multilinguality in Pre-Training** — Tests how far post-hoc merging can substitute for multilingual pre-training. [Read more](https://arxiv.org/abs/2605.25846)
- **Can LoRA Fusion Support Cross-Domain Tasks in Cloud-Edge Collaboration?** — Studies whether private edge-trained LoRAs can be fused into a cloud model without centralizing sensitive data. [Read more](https://arxiv.org/abs/2605.23913)
- **MAGIC: Multimodal Alignment & Grounding-aware Instruction Coreset** — Coreset selection for LVLM instruction tuning that favors grounding, alignment, and balanced reasoning-behavior coverage. [Read more](https://arxiv.org/abs/2605.26004)
- **Fine-Tuning Causal LLMs for Text Classification** — Compares embedding-head vs instruction-style fine-tuning for resource-constrained classification. [Read more](https://arxiv.org/abs/2512.12677)

### Preference optimization, RL, and reasoning
- **Learning to Reason Efficiently with A* Post-Training** — Recasts reasoning as search and rewards valid, efficient proof steps. [Read more](https://arxiv.org/abs/2605.24597)
- **TIAR: Trajectory-Informed Advantage Reweighting for LLM Abstention Learning** — Replaces static abstention rewards with trajectory-aware reweighting in GRPO-style training. [Read more](https://arxiv.org/abs/2605.25850)
- **Uni-DPO** — Dynamic preference optimization that weights examples by quality and learning difficulty. [Read more](https://arxiv.org/abs/2506.10054)
- **InfiFPO** — Moves model fusion into the preference-alignment stage instead of limiting fusion to SFT. [Read more](https://arxiv.org/abs/2505.13878)
- **Adaptive Preference Optimization with Uncertainty-aware Utility Anchor** — Adds uncertainty-aware anchoring to improve offline preference alignment. [Read more](https://arxiv.org/abs/2509.10515)
- **STAPO** — Stabilizes RL post-training by suppressing rare spurious tokens that trigger collapse. [Read more](https://arxiv.org/abs/2602.15620)
- **Better, Faster: Harnessing Self-Improvement in Large Reasoning Models** — Examines when self-generated reasoning traces help and when they fail. [Read more](https://arxiv.org/abs/2605.24998)
- **Harmony in Diversity** — Contrastive policy optimization reduces cross-domain interference in multi-domain reasoning RL. [Read more](https://arxiv.org/abs/2605.25443)
- **CRPO** — Character-centric GRPO improves role fidelity in role-playing agents. [Read more](https://arxiv.org/abs/2605.25511)
- **MATO** — Uses test-time optimization for multi-objective personalized alignment without retraining separate reward models. [Read more](https://arxiv.org/abs/2605.25342)
- **From Reasoning to Code** — Applies GRPO to improve code generation for underrepresented languages like Prolog and Lisp. [Read more](https://arxiv.org/abs/2506.11027)
- **PageLLM** — Multi-grained reward framework for whole-page optimization in search/recommendation. [Read more](https://arxiv.org/abs/2506.09084)
- **Which Reasoning Trajectories Teach Students to Reason Better?** — Proposes an “informative alignment” metric for selecting better CoT traces for distillation. [Read more](https://arxiv.org/abs/2601.14249)

### Speech, audio, and multimodal grounding
- **Raon-Speech Technical Report** — Transforms a pretrained LLM into a **9B English/Korean SpeechLM** plus a full-duplex speech chat model. [Read more](https://arxiv.org/abs/2605.23912)
- **EchoDistill** — Noisy-to-clean self-distillation for more robust Audio LLMs under real-world noise. [Read more](https://arxiv.org/abs/2605.23954)
- **Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition** — Applies DPO to reduce omission, translation, and hallucination errors in code-switching ASR. [Read more](https://arxiv.org/abs/2605.23975)
- **Language Bias in LVLMs** — Analyzes text-prior overreliance and proposes a simple mitigation for stronger visual grounding. [Read more](https://arxiv.org/abs/2605.25036)
- **Mitigating Object Hallucinations in Vision-Language Models through Region-Aware Attention Recalibration** — Lightweight recalibration reduces object hallucinations without heavy fine-tuning. [Read more](https://arxiv.org/abs/2605.24957)
- **GeoSVG-RL** — Geometry-aware RL improves layout-constrained text-to-SVG diagram generation. [Read more](https://arxiv.org/abs/2605.25447)

### Safety, evaluation, and theory
- **Causal methods for LLM development and evaluation** — Argues that data, routing, annotation, and eval choices should be treated explicitly as causal questions. [Read more](https://arxiv.org/abs/2605.25998)
- **Security in the Fine-Tuning Lifecycle of Large Language Models** — Surveys attack surfaces across data, weights, reusable components, agents, and interfaces. [Read more](https://arxiv.org/abs/2605.25073)
- **When In-Distribution Gains Fail** — Shows weak-to-strong reward models can break under zero-shot preference shift despite good in-distribution results. [Read more](https://arxiv.org/abs/2605.25629)
- **Jailbreak to Protect** — Studies temporary jailbreaking during training as a defense against malicious fine-tuning in FaaS setups. [Read more](https://arxiv.org/abs/2605.24550)
- **DRInQ** — Controlled evaluation of conversational implicature under context variation for dialog models. [Read more](https://arxiv.org/abs/2605.24267)
- **Clarification Is Not Enough** — Finds that answering after clarification, not asking clarifying questions, remains the main multi-turn QA bottleneck. [Read more](https://arxiv.org/abs/2605.25204)
- **Autoregressive Language Models are Secretly Energy-Based Models** — Theoretical bridge with implications for alignment objectives and decoding. [Read more](https://arxiv.org/abs/2512.15605)

### Domain-specific and applied post-training
- **Context-Instrumental Data Distillation for Kubernetes Manifest Generation** — Synthetic data plus tool feedback specializes small models for Kubernetes DSL generation. [Read more](https://arxiv.org/abs/2605.25835)
- **Multimodal Alignment and Preference Optimization for Zero-Shot Conditional RNA Generation** — Applies alignment and preference optimization to scientific sequence generation. [Read more](https://arxiv.org/abs/2605.23961)
- **Creative Quality Alignment** — Transfers expert tacit knowledge about creativity via low-data chain-of-thought fine-tuning. [Read more](https://arxiv.org/abs/2605.25977)
- **Fine-Tuning Over Architectural Complexity: Broad-Coverage PII Detection on PIIBench** — Shows strong multi-source fine-tuning can beat extra model complexity for 82-type PII detection. [Read more](https://arxiv.org/abs/2605.25816)
- **Geo-Expert** — Uses PEFT on curated geology corpora to improve expert-style subsurface and deep-time reasoning. [Read more](https://arxiv.org/abs/2605.24844)
- **Mitigating Hallucinations in Healthcare LLMs with Granular Fact-Checking and Domain-Specific Adaptation** — Pairs fine-grained verification with healthcare adaptation for safer outputs. [Read more](https://arxiv.org/abs/2512.16189)
- **Knowledge Graph-Driven Expert-Level Reasoning for Neuroscience** — Uses corpus-derived knowledge graphs for structured neuroscience domain adaptation. [Read more](https://arxiv.org/abs/2605.25183)
- **QUEST** — Trains deep-research agents on fully synthetic tasks to improve workflow generalization. [Read more](https://arxiv.org/abs/2605.24218)

## Key Takeaways
- **Efficiency is still the center of gravity** — Binary adapters, low-rank experts, pruning, LoRA fusion, federated tuning, and model conversion/merging all target cheaper post-training. [Signs Beat Floats](https://arxiv.org/abs/2605.24058) · [FLoRIST](https://arxiv.org/abs/2506.09199) · [Llamion](https://arxiv.org/abs/2605.25676)
- **Preference optimization is getting more dynamic and specialized** — This week’s work moves beyond static DPO toward adaptive weighting, abstention-aware rewards, fusion, stabilization, and search-aware objectives. [Uni-DPO](https://arxiv.org/abs/2506.10054) · [TIAR](https://arxiv.org/abs/2605.25850) · [A* Post-Training](https://arxiv.org/abs/2605.24597)
- **Multimodal and speech post-training is accelerating** — Strong activity spans text-to-image, speech LMs, audio robustness, code-switching ASR, and LVLM grounding/hallucination fixes. [ERNIE-Image](https://arxiv.org/abs/2605.25347) · [Raon-Speech](https://arxiv.org/abs/2605.23912) · [MAGIC](https://arxiv.org/abs/2605.26004)
- **Robustness, safety, and evaluation under shift are now first-class** — Reward-model fragility, full-lifecycle fine-tuning security, causal eval design, and safer adaptation pipelines are recurring concerns. [Security Lifecycle](https://arxiv.org/abs/2605.25073) · [Preference Shift](https://arxiv.org/abs/2605.25629) · [Causal Methods](https://arxiv.org/abs/2605.25998)
- **Domain-specific post-training keeps expanding** — Kubernetes, healthcare, geology, neuroscience, RNA generation, creative alignment, and research agents all point to more verticalized adaptation pipelines. [Kubernetes Distillation](https://arxiv.org/abs/2605.25835) · [Healthcare Hallucinations](https://arxiv.org/abs/2512.16189) · [QUEST](https://arxiv.org/abs/2605.24218)