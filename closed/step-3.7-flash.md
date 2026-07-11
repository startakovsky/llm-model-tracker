---
model: Step 3.7 Flash
organization: StepFun
license: Proprietary
release_date: 2026-05-28
last_updated: 2026-07-11
---

# Step 3.7 Flash

## Architecture
- **Total params:** 196B (MoE)
- **Active params per token:** ~11B
- **Context length:** 256,000
- **Modality:** Text + Image + Video → Text
- **Architecture type:** Multimodal Mixture-of-Experts

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (stepfun/step-3.7-flash) | $0.20 | $1.15 | 256,000 |

## Quality Assessment
Step 3.7 Flash is StepFun's latest high-efficiency multimodal MoE model. Pairs a 196B-parameter language backbone with a vision encoder for native image and video understanding. At $0.20/$1.15/M, it's competitively priced — cheaper than most frontier models while offering native multimodal (including video). StepFun is a rising Chinese AI company. The 196B/11B MoE design is efficient, with only ~11B params active per token. Good for cost-sensitive multimodal applications where video understanding is needed.

## Notes
- 196B/11B MoE — efficient inference
- Native image + video understanding
- StepFun is an emerging Chinese AI lab
- 256K context
