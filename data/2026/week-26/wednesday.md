## Weekly Digest

### NVIDIA
- **Cosmos 3** introduces *omnimodal* world models that jointly process and generate **language, image, video, audio, and action** in a unified mixture-of-transformers architecture, reinforcing NVIDIA’s push into **physical AI and robotics**. [Read more](https://arxiv.org/abs/2606.02800)

### Alibaba / Qwen
- **Qwen-AgentWorld** explores **language world models** for general agents, treating world modeling as prediction of environment dynamics from observations and actions to improve **reasoning and planning**. This is notable for post-training because rollout/simulation becomes a learned model capability rather than a separate system layer. [Read more](https://arxiv.org/abs/2606.24597)

### Academic / Open Research
- **Towards Spec Learning: Inference-Time Alignment from Preference Pairs** proposes steering models at **inference time** using preference pairs, offering a lighter-weight alignment complement to prompt engineering and fine-tuning. [Read more](https://arxiv.org/abs/2606.24004)
- **Reinforcement Learning Towards Broadly and Persistently Beneficial Models** argues alignment RL should generalize beyond training tasks and remain **beneficial across diverse, high-stakes deployments**. [Read more](https://arxiv.org/abs/2606.24014)
- **KLip-PPO: A per-sample KL perspective on PPO-Clip** reinterprets PPO through **per-sample KL control**, with implications for RLHF and other PPO-based post-training pipelines. [Read more](https://arxiv.org/abs/2606.23932)
- **EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games** proposes EMA regularization to stabilize PPO-style self-play, relevant to RL-based post-training where policy oscillation remains a common issue. [Search paper](https://arxiv.org/search/?query=EMAgnet%3A+Parameter-Space+EMA+Regularization+for+Policy+Gradient+Self-Play+in+Large+Games&searchtype=all)
- **Variational Model Merging for Pareto Front Estimation in Multitask Finetuning** uses variational model merging to estimate **Pareto fronts** more cheaply, helping teams balance multiple post-training objectives without exhaustive retraining. [Read more](https://arxiv.org/abs/2412.08147)
- **Tuning without Peeking: Provable Generalization Bounds and Robust LLM Post-Training** studies privacy-preserving post-training settings where gradients can leak sensitive information, offering a more secure framework with provable guarantees. [Read more](https://arxiv.org/abs/2507.01752)
- **Removing Noise, not Finding Gold: Quality Filtering for Large-Scale Pretraining** argues data filtering helps mainly by **removing noisy documents**, not by identifying rare “gold” samples—an important takeaway for training-data curation. [Read more](https://arxiv.org/abs/2510.00866)

## Key Takeaways
- **World models are gaining momentum** across both **robotics/physical AI** (NVIDIA) and **general agent planning** (Qwen).
- **Post-training is broadening beyond standard fine-tuning**, with new work on **inference-time alignment**, **privacy-preserving tuning**, and **checkpoint/model merging**.
- **RL fundamentals still matter**: PPO behavior, KL control, and update stability remain active areas for improving RLHF-style systems.
- **Data quality work is becoming more practical**, with evidence that **noise removal** may matter more than increasingly elaborate data scoring.