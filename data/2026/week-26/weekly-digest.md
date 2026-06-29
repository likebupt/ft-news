## Hugging Face / NVIDIA
- Hugging Face published a guide on using NVIDIA NeMo AutoModel to accelerate transformer fine-tuning, highlighting a more optimized path for training and adapting models on NVIDIA hardware. For finetuning teams, this matters because faster, more efficient post-training lowers iteration time and infrastructure cost for SFT, domain adaptation, and continual training. [Read more](https://huggingface.co/blog/nvidia/accelerating-fine-tuning-nvidia-nemo-automodel)

## Apple
- Apple studied how many annotations are actually needed when training on label distributions, showing that annotator disagreement is useful signal and that “enough” labels depends on the evaluation metric. For finetuning, this suggests soft-label training and metric-aware data collection can improve quality on ambiguous tasks while reducing annotation spend. [Read more](https://machinelearning.apple.com/research/metric-dependent-annotation-saturation)

## OpenAI
- OpenAI said it is helping develop shared standards for advanced AI, including evaluation frameworks, safety practices, and coordination through the Appia Foundation. For post-training, that matters because standard evals and safety criteria increasingly shape how labs design alignment fine-tuning, reward modeling, and release gates. [Read more](https://openai.com/index/helping-build-shared-standards-for-advanced-ai)