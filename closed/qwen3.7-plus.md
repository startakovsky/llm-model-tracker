---
model: Qwen3.7 Plus
organization: Alibaba
license: Apache 2.0
release_date: 2026-06-03
last_updated: 2026-07-11
---

# Qwen3.7 Plus

## Architecture
- **Context length:** 1,000,000
- **Modality:** Text + Image → Text
- **Architecture type:** Closed-weight API model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (qwen/qwen3.7-plus) | $0.32 | $1.28 | 1,000,000 |

## Quality Assessment
Qwen3.7 Plus is a cost-effective model in Alibaba's Qwen3.7 series (which also includes the closed-weight Qwen3.7 Max, already tracked). Supports text and image input with text output. At $0.32/$1.28/M, it's competitively priced — comparable to GLM-5.2 ($0.35/$1.10) on prompt tokens but cheaper on completion. Closed-weight API (no HuggingFace weights). Good mid-tier option for multimodal tasks requiring 1M context at a reasonable price.

## Notes
- Part of the Qwen3.7 series alongside Qwen3.7 Max (closed-weight)
- Closed-weight API — no open weights despite Apache 2.0 license tag
- 1M context, multimodal (text + image)
- Cost-effective mid-tier for multimodal + long context
