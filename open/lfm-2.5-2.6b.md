---
model: LFM2.5-2.6B
organization: Liquid AI
license: other
release_date: 2026-07-28
last_updated: 2026-10-30
sources:
  - https://openrouter.ai/liquid/lfm-2.5-2.6b
  - https://huggingface.co/LiquidAI/LFM2.5-2.6B
---

# LFM2.5-2.6B

Smallest member of Liquid AI's LFM2.5 family (released Jul 28, 2026), a 2.6B reasoning model built for tool-calling agents; Liquid pairs it with retrieval/search for knowledge-heavy tasks (same design as the larger LFM2.5-24B-A2B sibling already tracked).

## Availability
- OpenRouter id `liquid/lfm-2.5-2.6b` at $0.35/$0.50 per M, 128K ctx (a `:free` endpoint also live).
- Open weights on HuggingFace (`LiquidAI/LFM2.5-2.6B`, Liquid custom license; 91K downloads, 859 likes).

## Key signals
- New OpenRouter listing (Oct 2026) of an open model with real HF traction (91K downloads).
- Same always-reasons + tool-calling design as the family flagship, at edge scale.

## Quality assessment
A competent edge/on-device reasoning agent model, not a frontier contender. At $0.35/$0.50 it costs more per token than larger open models (LFM2.5-24B-A2B is $0.05/$0.70), so its value is local deployment, not API cost/quality. Quality score 50.