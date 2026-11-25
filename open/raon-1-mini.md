---
model: Raon 1 Mini
organization: KRAFTON
license: Apache 2.0
release_date: 2026-11-24
last_updated: 2026-11-25
sources:
  - https://huggingface.co/KRAFTON/Raon-1-mini
---

# Raon 1 Mini — KRAFTON

| Field | Value |
|---|---|
| **Org** | KRAFTON (PUBG maker; first in-house LLM) |
| **HuggingFace** | [KRAFTON/Raon-1-mini](https://huggingface.co/KRAFTON/Raon-1-mini) (264 DL / 85 likes day-1; GGUF + NVFP4 variants) |
| **License** | Apache 2.0 (open weights) |
| **Release date** | 2026-11-24 |
| **Pricing** | Not on OpenRouter (self-host) |
| **Context** | 262,144 |
| **Category** | Lightweight (open) |

## Architecture

- Dense causal LM, ~4.3B params (est. from config: hidden 2,560, 25 layers, 40 heads, intermediate 12,032, vocab 259,840, untied embeddings).
- 256K max position embeddings; `raon1_mini` model type.

## Quality Assessment

Game studio (KRAFTON) entering the LLM race with a small Apache-2.0 model — notable mostly as an industry signal (PUBG maker's in-house stack, Korean coverage). Small dense class; not a frontier contender. Score 55.

## Sources
- https://huggingface.co/KRAFTON/Raon-1-mini
