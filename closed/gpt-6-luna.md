---
model: GPT-6 Luna
organization: OpenAI
license: Proprietary
release_date: 2026-09-22
last_updated: 2026-09-24
---

# GPT-6 Luna

Cheap, high-volume, fast tier of GPT-6 (~140 tok/s), optimized for extraction and summarization at scale. Less reasoning than Sol. Per VentureBeat this "slashes API costs 50%+" versus prior tiers.

## Availability
- Closed API only. `openai/gpt-6-luna` on OpenRouter at $0.1/$0.5 per M, 1.05M ctx.

## Classification
`closed` (Proprietary). Quality score 84 — budget fast tier.

## Notes
- 1.05M ctx, priced at a budget $0.1/$0.5.
- The `-pro` variant (GPT-6 Luna Pro) is the same model served with `reasoning.mode=pro` at identical pricing.