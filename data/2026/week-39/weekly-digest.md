### Amazon
- Amazon Bio Discovery published three papers on AI for antibody engineering, covering better benchmarking for binding prediction and experimental validation of de novo designs. For finetuning, this matters because stronger task-specific benchmarks and wet-lab labels can improve supervised adaptation of foundation models for biology. [Read more](https://www.amazon.science/blog/advancing-ai-for-biology-teaching-models-to-design-and-characterize-antibodies)
- Amazon and Reactor described kernel-level optimizations on Trainium for real-time autoregressive diffusion video generation, addressing dynamic shapes, memory access, and cache behavior. For finetuning, this could lower the cost and latency of post-training and serving video models on AWS hardware. [Read more](https://www.amazon.science/blog/a-kernel-centric-path-to-real-time-video-generation-on-trainium)
- Amazon launched a joint research initiative with Stanford focused on AI and science. It is broad, but could yield new datasets, benchmarks, and domain workflows that support scientific model finetuning. [Read more](https://www.amazon.science/news/amazon-launches-research-initiative-with-stanford-university-to-advance-ai-and-science)

### Microsoft
- Microsoft highlighted RetroChimera, a model for improving small-molecule synthesis prediction at scale. For finetuning, it reinforces that large domain datasets plus task-specific adaptation can materially improve scientific model performance. [Read more](https://www.microsoft.com/en-us/research/blog/improving-synthesis-prediction-of-small-molecules-at-scale-with-retrochimera/)
- Microsoft Research showed that offloading inference from robots to external compute can improve task success and efficiency for physical AI. For finetuning, this expands the practical envelope for deploying larger post-trained robotics models and suggests training should account for split-compute serving setups. [Read more](https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/)

### Apple
- Apple introduced latent-space distillation to compress streaming neural audio encoders used in on-device dictation. For finetuning, this is a useful post-training pattern for shrinking multimodal front ends while preserving compatibility with downstream foundation models. [Read more](https://machinelearning.apple.com/research/latent-space-distillation)

### Together AI
- Together AI published a walkthrough for training a Jev-like classifier on top of Qwen3.5 4B for about $17 and released an experimental model. This is directly relevant to finetuning because it demonstrates a low-cost, practical recipe for classifier tuning on open models via serverless infrastructure. [Read more](https://www.together.ai/blog/how-to-train-your-own-jev)

### Hugging Face
- Hugging Face hired oMLX creator Jun Kim to support the MLX community. For finetuning, stronger MLX support could improve Apple-silicon-native tooling for local LoRA, lightweight training, and on-device adaptation workflows. [Read more](https://huggingface.co/blog/omlx)