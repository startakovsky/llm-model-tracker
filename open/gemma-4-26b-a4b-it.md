---
model: Gemma 4 26B A4B
organization: Google DeepMind
license: Apache 2.0
release_date: 2026-04-03
last_updated: 2026-07-11
---

# Gemma 4 26B A4B

## Architecture
- **Total params:** 25.2B (MoE)
- **Active params per token:** ~3.8B
- **Context length:** 262,144
- **Modality:** Text + Image + Video → Text
- **Architecture type:** Instruction-tuned Mixture-of-Experts

## Self-Hosting
Despite 25.2B total params, only 3.8B activate per token — delivering near-31B dense quality at a fraction of inference cost. Fits comfortably in 16-24GB VRAM with quantization.

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (google/gemma-4-26b-a4b-it) | $0.06 | $0.33 | 262,144 |

## Quality Assessment
One of the best quality-per-dollar open models available. 14M+ HuggingFace downloads and 1254 likes indicate massive community adoption. At $0.06/$0.33/M via API, it's ~5x cheaper than GLM-5.2 while delivering near-31B dense quality. Excellent for lightweight agentic tasks, chat, and multimodal understanding. The MoE design means local inference is fast — only 3.8B active params.

## Notes
- Massive adoption (14M HF downloads) — one of the most popular open models
- Multimodal: supports text, image, and video input
- Apache 2.0 license — fully open for commercial use
- Excellent for self-hosting on consumer hardware
