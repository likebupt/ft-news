## TL;DR

This week sharpened two product truths: post-training is becoming inseparable from runtime instrumentation, and long-context finetuning is only valuable if the serving stack can actually carry it. OpenAI’s Codex safety design shows that agent traces, approval events, and policy interventions are turning into high-value post-training data, while Together AI’s DeepSeek-V4 deployment makes clear that long-context tuning fails commercially if inference cost, cache behavior, and latency are not designed in from day one. The strongest research signal is a shift away from brute-force retraining toward smarter updates—especially continual low-rank adaptation, dynamic data weighting, and better adapter targeting—which is exactly where enterprise buyers will expect lower cost and less forgetting. Net: Foundry should think less like a job runner and more like an end-to-end post-training control plane spanning data, tuning, eval, and deployment.

## Top Stories

- **OpenAI turns Codex operations into a safety-and-training loop** — OpenAI detailed Codex’s production controls, including sandboxed execution, approval gates, network restrictions, and agent-native telemetry. For Foundry, the important shift is that runtime artifacts—tool traces, human approvals, and policy hits—are becoming premium post-training data, so our product needs native collection and replay of agent traces, not just model checkpoints. [Read more](https://openai.com/index/running-codex-safely)

- **Together AI makes the long-context bottleneck explicit** — Together AI said serving DeepSeek-V4 at million-token context required compressed KV-cache layouts, prefix caching, and hardware-specific kernel optimization on HGX B200. That matters because long-context finetuning is only sellable if deployment economics work on Azure afterward; otherwise we help customers create models they cannot afford to run. [Read more](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)

- **CRAFFT points to a more enterprise-friendly continual tuning path** — Researchers introduced CRAFT, which adds new capabilities through routed low-rank interventions on hidden representations instead of repeatedly rewriting base weights. This is highly relevant for Foundry because enterprise customers usually need recurring policy, domain, and seasonal updates, and “tune again without forgetting” is a more compelling product promise than repeated full retrains. [Read more](https://arxiv.org/abs/2605.05732)

## By Company

### North America

- **Amazon** — Amazon framed responsible AI as an end-to-end lifecycle spanning instruction tuning, safety tuning, evaluation, and red-teaming, reinforcing that enterprise buyers increasingly expect governance to be built into post-training rather than bolted on after deployment. [Source](https://www.amazon.science/blog/building-trust-into-ai)

- **Zyphra / AMD** — Zyphra’s ZAYA1-8B report describes a reasoning-focused MoE with just 700M active parameters trained across pretraining, midtraining, and SFT on an AMD full-stack platform, signaling that capable reasoning post-training may become cheaper and less tied to NVIDIA-centric assumptions. [Source](https://arxiv.org/abs/2605.05365)

## Notable Papers

- **Online data curation via reweighting** — Dynamic example weighting during training could outperform repeated offline dataset filtering, making it a strong candidate for an “auto-curate” feature in SFT and continual tuning workflows. [Paper](https://arxiv.org/abs/2605.05227)

- **Near-Policy Distillation** — Asynchronous generation plus selective packing suggests a cheaper path to near on-policy distillation, which could reduce the cost of student-model post-training and compaction. [Paper](https://arxiv.org/abs/2605.05940)

- **Optimizer-model consistency** — Matching the finetuning optimizer to the one used in pretraining appears to reduce forgetting while maintaining downstream quality, which is a practical default change for full-model SFT jobs. [Paper](https://arxiv.org/abs/2605.06654)

- **Adapter placement in dominant modules** — This work argues LoRA quality depends heavily on targeting a small set of dominant modules rather than spreading adapters broadly, opening the door to lower-cost PEFT with smarter defaults. [Paper](https://arxiv.org/abs/2605.06183)

- **RVPO for risk-sensitive RLHF** — Variance-regularized preference optimization looks useful for enterprise multi-objective tuning, where gains on helpfulness cannot be allowed to mask regressions on safety, formatting, or policy compliance. [Paper](https://arxiv.org/abs/2605.05750)

- **Reward modeling from noisy preferences** — Optimal-transport-based reward modeling could make RLHF pipelines more robust to imperfect preference labels, which is especially relevant for enterprise annotation programs with mixed-quality raters. [Paper](https://arxiv.org/abs/2605.06036)

- **Tool-integrated reasoning** — The paper shows that simply turning tools on can hurt quality unless models are explicitly trained when and how to use them, implying Foundry should treat tool-use tuning as a first-class workflow rather than a prompt-layer add-on. [Paper](https://arxiv.org/abs/2605.06326)

- **One Turn Too Late** — Multi-turn hidden-intent attacks require response-aware defenses, a reminder that post-training safety evals based only on single prompts will miss realistic enterprise dialogue risks. [Paper](https://arxiv.org/abs/2605.05630)

- **Safety Anchor** — Geometric bottlenecks for defending against harmful finetuning suggest a promising way to preserve alignment when customers perform downstream customization on top of already-safe models. [Paper](https://arxiv.org/abs/2605.05995)

- **Evaluation-context divergence** — Models can behave differently when prompts “look like” benchmarks, which means benchmark-style post-training wins may not transfer cleanly to production prompts unless eval design changes. [Paper](https://arxiv.org/abs/2605.06327)

## What This Means for Us

- **Build first-class agent-trace ingestion for post-training** — OpenAI’s Codex design makes clear that approvals, tool traces, sandbox outcomes, and policy violations are becoming the highest-value data for the next tuning cycle; Foundry should ship native schemas, storage, and replay paths so customers can turn agent operations directly into SFT, reward-model, and safety-tuning datasets. [Read more](https://openai.com/index/running-codex-safely)

- **Bundle long-context tuning with deployment-feasibility checks** — Together AI’s DeepSeek-V4 write-up shows that million-token capability is as much an inference-systems problem as a model problem, so Foundry should gate long-context jobs with Azure deployment sizing, KV-cache-aware evals, and projected cost/latency outputs before customers commit spend. [Read more](https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem)

- **Add a “continual tuning” mode for recurring enterprise updates** — CRAFT and attribution-guided continual learning both point to a clear product opportunity: customers need monthly domain and policy refreshes without catastrophic forgetting, and a PEFT-first sequential update workflow would be easier to operationalize than repeated full retrains. [CRAFT](https://arxiv.org/abs/2605.05732), [Attribution-guided continual learning](https://arxiv.org/abs/2605.05285)

- **Offer automatic data-weighting and LoRA-target optimization** — Online reweighting and dominant-module adapter placement both suggest better quality-per-dollar comes from choosing the right examples and modules, not just running more epochs, which makes this a strong candidate for an “optimization layer” inside Foundry tuning jobs. [Data reweighting](https://arxiv.org/abs/2605.05227), [Adapter placement](https://arxiv.org/abs/2605.06183)

- **Monitor cost pressure from small-active MoEs on non-NVIDIA stacks** — Zyphra’s AMD-based reasoning model is a warning that capable post-training may get cheaper and more hardware-flexible than many enterprise buyers assume, which could compress margins on premium finetuning offers unless Azure leads on transparent cost/performance positioning. [Source](https://arxiv.org/abs/2605.05365)

- **Harden post-tune safety and evals around real deployment failure modes** — Safety Anchor, One Turn Too Late, and evaluation-context divergence all point to the same risk: downstream finetuning can quietly erode alignment, miss multi-turn attacks, or overfit benchmark-style prompts, so every Foundry workflow should include post-tune regression suites for policy retention, multi-turn safety, and production-like prompt distributions. [Safety Anchor](https://arxiv.org/abs/2605.05995), [One Turn Too Late](https://arxiv.org/abs/2605.05630), [Evaluation-context divergence](https://arxiv.org/abs/2605.06327)