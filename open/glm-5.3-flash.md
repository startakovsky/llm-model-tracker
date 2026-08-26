---
model: GLM-5.3-Flash
organization: Z.ai
license: MIT
release_date: 2026-08-26
last_updated: 2026-08-26
---

# GLM-5.3-Flash

## Architecture
- **Context length:** 1,048,576 (1M)
- **Architecture type:** Hybrid sparse + linear attention
- **Modality:** Text + Image (native multimodal, image-text-to-text)

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (z-ai/glm-5.3-flash) | $0.075 | $0.25 | 1,048,576 |

## Benchmarks
- Brand new (released Aug 26, 2026) — limited independent benchmarks yet
- Part of GLM-5.3 family (strongest open-weights coding claim)
- Positioned for efficient coding and long-horizon agent tasks

## Self-Hosting
- Open weights on HuggingFace: `zai-org/GLM-5.3-Flash` (MIT license, 317 likes on day one)
- Quantized variants available same day:
  - GGUF (`unsloth/GLM-5.3-Flash-GGUF`, `AtomicChat/GLM-5.3-Flash-GGUF`)
  - BF16 (`zai-org/GLM-5.3-Flash-BF16`)
  - FP8 (`unsloth/GLM-5.3-Flash-FP8`)
- Fast community adoption signals (GGUF/BF16/FP8 day one)

## Quality Assessment
GLM-5.3-Flash is the cost-efficient Flash tier of Z.ai's GLM-5.3 line, launched the day after GLM-5.3's API debut went live on OpenRouter. It inherits the hybrid sparse/linear attention architecture that makes large MoEs tractable for long-context agent work while adding native multimodal (image + text) input. At $0.075/$0.25 per M tokens it undercuts nearly every other 1M-context model by ~10x, making it an attractive self-hostable agent backbone. Still too new for reliable benchmark comparison, but GLM-5.3's frontier coding results (Terminal-Bench 3.0, DeepSWE) suggest the Flash tier is worth tracking for cost-sensitive agent deployments. MIT weights + day-one GGUF/FP8 quants reinforce strong community signal.