---
model: Ling-2.6-1T
organization: inclusionAI
license: MIT
release_date: 2026-04-23
last_updated: 2026-07-11
---

# Ling-2.6-1T

## Architecture
- **Total params:** ~1T (MoE)
- **Active params per token:** ~63B
- **Context length:** 262,144
- **Modality:** Text → Text
- **Architecture type:** MoE, instant (instruct) model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (inclusionai/ling-2.6-1t) | $0.075 | $0.625 | 262,144 |

## Quality Assessment
Ling-2.6-1T is inclusionAI's trillion-parameter flagship instant (instruct) model, designed for real-world agents requiring fast execution and high efficiency at scale. Uses a "fast thinking" mode for optimized inference. Sister model to Ring-2.6-1T (already tracked), which is the thinking/reasoning variant. At $0.075/$0.625/M, it's extremely cost-competitive for a 1T model — far cheaper than GLM-5.2. MIT license, 383 HF downloads, 475 likes.

## Notes
- Sister to Ring-2.6-1T (thinking model); Ling is the instant/instruct variant
- Same 1T/63B MoE architecture as Ring-2.6-1T
- MIT license — fully open
- Ultra-cheap for a 1T-class model
