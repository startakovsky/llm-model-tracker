---
model: Mi:dm K 3.0 Pro
organization: KT (Korea Telecom)
license: Proprietary
release_date: 2026-11-05
last_updated: 2026-11-11
sources:
  - https://openrouter.ai/kt/midm-k-3.0-pro
  - https://anyrouter.dev/model/kt/midm-k-3.0-pro
  - https://bothub.chat/midm-k-3.0-pro
---

# Mi:dm K 3.0 Pro

KT's (Korea Telecom) Mixture-of-Experts reasoning model: 120B total / 12B active parameters, hybrid architecture mixing Mamba, MoE, and attention layers; text-in.

## Availability
- OpenRouter id `kt/midm-k-3.0-pro` at $0.20/$0.80 per M, ~262K ctx (261,795).
- Surfaced Nov 10 when KT became an OpenRouter provider — 7 models served from Korean data centers; K 3.0 Pro is one of two models new to OpenRouter from that onboarding.

## Specs
- 120B total / 12B active MoE reasoning model; hybrid Mamba + MoE + attention.
- Text-only input.

## Quality assessment
Mid-tier reasoning model from a major Korean telecom, cheapest Korean option on OpenRouter. No weights found on HF yet (KT's Mi:dm 2.0 line was open previously) — classified closed pending weights. Quality score 72.
