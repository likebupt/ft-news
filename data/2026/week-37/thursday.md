# Weekly Digest

## Academic / Open Research
*No company affiliations were provided in the source material, so all items are grouped here.*

- **RL + SFT logit averaging for LLM post-training** — Proposes averaging logits from a frozen SFT/reference model with a trainable RL policy inside GRPO to preserve supervised capabilities while still optimizing reward. [Read more](https://arxiv.org/abs/2605.20555)
- **Reward uncertainty for diverse RL behavior** — Uses uncertainty over rewards to encourage multiple valid behaviors instead of collapsing to a single policy, with clear relevance to LLM tasks that have many acceptable outputs. [Read more](https://arxiv.org/abs/2606.03962)
- **FiberTune for VLA fine-tuning** — Preserves “action-fiber” visual residuals during vision-language-action fine-tuning so models retain richer visual structure and generalize better. [Read more](https://arxiv.org/abs/2606.08653)
- **SalamandraTA on terminology-aware translation** — Finds that harder terminology examples are better teachers than standard fine-tuning data, highlighting data selection as a lever for glossary/constraint-following. [Read more](https://arxiv.org/abs/2609.09999)
- **Data-centric post-training for financial reasoning** — Combines data mining, distillation, and verifiable learning to turn noisy financial corpora into higher-quality reasoning supervision. [Read more](https://arxiv.org/abs/2609.10113)
- **Ling 2.0 / “Every Activation Boosted”** — Introduces a reasoning-oriented open foundation model family with an explicit scaling path up to 1T parameters, positioning reasoning as the central scaling target. [Read more](https://arxiv.org/abs/2510.22115)
- **Proof-Carrying Cognition** — Argues RL gains are concentrated in math/code because they have cheap verifiers, and proposes **reality-settled reward** to address the broader verification gap. [Read more](https://arxiv.org/abs/2609.09776)
- **Preventative Steering under adversarial fine-tuning** — Studies malicious fine-tuning and finds static defenses are not enough; steering-based defenses likely need to adapt over time. [Read more](https://arxiv.org/abs/2609.10142)
- **TRACE for causal exploration** — Trains reasoning agents for causal exploration using synthesized rewards, pointing to reward construction as a path beyond naturally verifiable domains. [Read more](https://arxiv.org/abs/2609.10315)
- **NOPE-HYPE for robust speech-to-text** — Presents a structured simulation workflow to improve speech-to-text robustness across diverse acoustic environments. *(No link provided in source.)*

## Key Takeaways
- **Hybrid post-training is gaining traction:** several papers aim to keep SFT-era capabilities intact while still benefiting from RL or domain-specific optimization.
- **Verification and reward design remain the bottleneck:** reward uncertainty, synthesized rewards, and reality-settled reward all target the same core challenge—how to scale post-training beyond easy-to-verify tasks.
- **Data curation matters as much as model size:** hard-example mining, distillation, and verification pipelines appear especially valuable for specialized domains like finance and terminology-constrained translation.
- **Robustness is broadening beyond text-only LLMs:** new work spans VLA fine-tuning, adversarial fine-tuning defenses, and speech-to-text evaluation in diverse real-world conditions.