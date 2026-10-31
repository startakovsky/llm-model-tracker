---
model: Ternary Bonsai 2 (9B)
organization: prism-ml
license: Apache-2.0
release_date: 2026-10-16
last_updated: 2026-10-31
sources:
  - https://openrouter.ai/prism-ml/ternary-bonsai-2-9b
  - https://huggingface.co/prism-ml/Ternary-Bonsai-2-9B-gguf
---

# Ternary Bonsai 2 (9B)

Released Oct 16, 2026 — the smaller sibling of the tracked Ternary Bonsai 2 27B, from prism-ml's ternary-weight compression line. Focused on aggressive size/weight compression while retaining usable quality.

## Architecture
- **Total params:** ~9B
- **Context length:** 262,144 (256K)
- **Architecture:** ternary-weight compression (family line)
- **Modality:** text in / text out

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (prism-ml/ternary-bonsai-2-9b) | $0.08 | $0.13 | 262,144 | Oct 16: live on OpenRouter |

## Quality Assessment
Ultra-cheap self-host candidate in the ternary-quantization niche (the 27B sibling logged ~1.5M downloads on HF). At $0.08/$0.13 on OpenRouter it's one of the cheapest listed options, aimed at resource-constrained local inference. Benchmark coverage is thinner than the 27B; treat it as a lightweight utility model rather than a frontier contender.

## Notes
- Apache-2.0; GGUF on HuggingFace (`prism-ml/Ternary-Bonsai-2-9B-gguf`).
- Same family as `prism-ml/ternary-bonsai-2-27b` (tracked Sep 18).
