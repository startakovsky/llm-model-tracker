---
model: ERNIE-5.5-Flash-Preview
organization: Baidu
license: Apache 2.0 (base)
release_date: 2026-11-10
last_updated: 2026-11-11
sources:
  - https://ernie.baidu.com/release/ernie-5-5-flash-preview/
  - https://ernie.baidu.com/release/ernie-5-5-flash-base/
  - https://openrouter.ai/baidu/ernie-5.5-flash-preview:free
---

# ERNIE-5.5-Flash-Preview

First post-trained model built on ERNIE-5.5-Flash-Base (280B total / 14B active sparse MoE, base released Nov 5, 2026). New Baidu architecture; r/LocalLLaMA reports it suitable for 32GB VRAM + 128GB RAM systems.

## Availability
- Free preview on OpenRouter (`baidu/ernie-5.5-flash-preview:free`), live Nov 10, 1.024M ctx. **[Nov 12] Base id dropped from OpenRouter; only the `:free` variant remains.**
- Base weights open on HuggingFace: `baidu/ERNIE-5.5-Flash-Base` (BF16 variant too).
- Preview weights not yet published; full ERNIE 5.5 Flash release expected by Nov 25.

## Specs
- Sparse MoE: 280B total, 14B active per token.
- Text model; long-context + agentic positioning.

## Quality assessment
No independent benchmarks published at launch. Tracker classifies closed pending preview weights (base family is open). Free endpoint makes it a zero-cost trial candidate for agentic workloads until the full release. Quality score 72.
