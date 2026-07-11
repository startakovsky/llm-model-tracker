---
model: Ling-2.6-Flash
organization: inclusionAI
license: MIT
release_date: 2026-04-21
last_updated: 2026-07-11
---

# Ling-2.6-Flash

## Architecture
- **Total params:** 104B (MoE)
- **Active params per token:** 7.4B
- **Context length:** 262,144
- **Modality:** Text → Text
- **Architecture type:** MoE, instant (instruct) model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (inclusionai/ling-2.6-flash) | $0.01 | $0.03 | 262,144 |

## Quality Assessment
Ling-2.6-Flash is inclusionAI's lightweight instant model with 104B total / 7.4B active params, designed for fast responses and high token efficiency. At $0.01/$0.03/M, it is the **cheapest model in the entire tracker** — 35x cheaper than GLM-5.2 on prompt tokens. Ideal for high-volume agent workflows where cost-per-token is critical. MIT license, 2,798 HF downloads, 498 likes (high like ratio suggests quality).

## Notes
- **Cheapest model in tracker** at $0.01/$0.03/M
- 104B/7.4B MoE — only 7.4B active per token
- MIT license
- Part of the Ling-2.6 family alongside Ling-2.6-1T and Ring-2.6-1T
