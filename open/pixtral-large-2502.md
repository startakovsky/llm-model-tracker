---
model: Pixtral Large 2502
organization: Mistral AI
license: Apache 2.0
release_date: 2026-11-20
last_updated: 2026-11-22
sources:
  - https://openrouter.ai/mistralai/pixtral-large-2502
---

# Pixtral Large 2502 — Mistral AI

| Field | Value |
|---|---|
| **Org** | Mistral AI |
| **OpenRouter ID** | `mistralai/pixtral-large-2502` |
| **License** | Apache 2.0 (open weights) |
| **OpenRouter listing** | 2026-11-20 |
| **Pricing** | $2.00/$6.00 per M |
| **Context** | 128,000 |
| **Category** | Self-hostable (open) |

## Architecture

- Mistral's large multimodal model: text+image input → text output; handles documents, charts, natural images.
- New OpenRouter listing Nov 20, 2026 (model is the Feb 2025 Pixtral Large 2502 generation); 128K ctx, max completion 102,400 (~100K).

## Quality Assessment

Large-scale open multimodal from Mistral, newly available on OpenRouter at $2.00/$6.00 — mid-tier pricing for a 124B-class multimodal model. Relevant where open-weights document/chart understanding at scale is the job; not a frontier text-reasoning contender. Score 66 (assessed at listing; no fresh independent benchmarks surfaced in the current release cycle).

- HF repo gated/unavailable at tracking time — weights assumed Apache 2.0 per Mistral's Pixtral line; verify before self-hosting.
