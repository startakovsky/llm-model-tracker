---
model: DeepSeek V4 Flash Vision Exp
organization: DeepSeek
license: MIT
release_date: 2026-08-21
last_updated: 2026-08-21
sources:
  - https://api-docs.deepseek.com/guides/vision/
  - https://openrouter.ai/deepseek/deepseek-v4-flash-vision-exp
  - https://www.bloomberg.com/news/articles/2026-08-21/deepseek-unveils-test-model-to-rival-anthropic-s-opus-4-8
---

# DeepSeek V4 Flash Vision Exp

Experimental vision-enabled variant of DeepSeek V4 Flash, built on the 0731 revision. Adds image understanding while matching the base model on text capabilities including agents, reasoning, and world knowledge. Released Aug 21, 2026.

## Key signals
- **Vision added:** accepts images alongside text — describe pictures, read text from screenshots, analyze charts.
- **Text parity:** matches DeepSeek-V4-Flash on text benchmarks (agents, reasoning, world knowledge) per DeepSeek.
- **Positioning:** Bloomberg coverage frames it as DeepSeek testing a multimodal model that approaches an advanced Anthropic rival (Opus 4.8) — a deliberate Opus-4.8-competitor signal.

## Availability
- **OpenRouter:** Live Aug 21 at **$0.22/$0.66 per M** (prompt/completion), 1M ctx.
- **Weights:** MIT, on HuggingFace under DeepSeek org (deepseek-ai), consistent with the open V4 Flash line.

## Classification
`open` (MIT weights on HF). Quality score 80 — a capable multimodal workhorse at roughly 1/6th the cost of DeepSeek V4 Pro; strong self-hosting value on the 284B/13B MoE architecture. Vision is experimental, so below the flagship frontier mark.

## Sources
- DeepSeek vision API docs: https://api-docs.deepseek.com/guides/vision/
- OpenRouter: https://openrouter.ai/deepseek/deepseek-v4-flash-vision-exp
- Bloomberg: https://www.bloomberg.com/news/articles/2026-08-21/deepseek-unveils-test-model-to-rival-anthropic-s-opus-4-8
