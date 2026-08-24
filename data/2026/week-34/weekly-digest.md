## Apple

- Apple studies GRPO/RLVR for non-English and multilingual settings, extending a post-training recipe that has mostly been validated in English. It matters because multilingual reasoning fine-tuning likely needs language-aware reward design, data balance, and evaluation rather than assuming English RL results transfer cleanly. [Read more](https://machinelearning.apple.com/research/grpo-beyond-english)

- Apple proposes “lexical interventions” to improve multilingual knowledge transfer when target-language data is scarce. It matters because this points to a data-efficient fine-tuning strategy for low-resource languages, especially where key task knowledge is locked in high-resource-language corpora. [Read more](https://machinelearning.apple.com/research/multilingual-knowledge-transfer-lexical-interventions)

- Apple introduces an iterative pseudo-labeling approach for Mandarin-English code-switching ASR, targeting a setting with limited supervised code-switching data. It matters for post-training because it reinforces self-training/pseudo-labeling as a practical way to adapt models to mixed-language or low-resource domains. [Read more](https://machinelearning.apple.com/research/progressive-refinement-pseudo-labeling)

## OpenAI

- OpenAI says it is tightening monitoring, alignment, and security as models approach cyber-critical capability thresholds. For fine-tuning teams, this signals that frontier post-training may increasingly be gated by capability evals and safety controls, not just benchmark gains. [Read more](https://openai.com/index/pacing-model-development-cyber-capabilities)

## Together AI

- Together AI recommends endpoint-level A/B testing to compare models in production, rather than relying only on shadow traffic or app-side routing. It matters because online experimentation is becoming a core post-training loop for validating whether a newly fine-tuned model actually improves user outcomes before full rollout. [Read more](https://www.together.ai/blog/a-b-test-models-in-production)