---
model: Moondream 3 Preview
organization: Moondream
license: Moondream Model License 1.0
release_date: 2026-10-15
last_updated: 2026-10-21
sources:
  - https://huggingface.co/moondream/moondream3-preview
  - https://openrouter.ai/moondream/moondream3-preview
---

# Moondream 3 Preview

Preview of the Moondream 3 vision-language line from Moondream (the tiny-VLM startup known for query/detect/caption models that run locally). Serves as the preview gate for the 3.x family, superseded by **Moondream 3.1** (9B/2B MoE, tracked separately) which keeps the same $0.30/$2.50 OpenRouter pricing.

## Architecture
- **Modality:** image + text -> text (vision-language: query, detect, point, caption)
- **Context length:** 32,000 (32K) on OpenRouter
- **Family:** Moondream 3 -> Moondream 3.1 9B/2B MoE (SOTA visual reasoning/detection for its size)
- **Traction:** 82K HF downloads, 692 likes; local-first via the Photon engine

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (moondream/moondream3-preview) | $0.30 | $2.50 | 32,000 | Live since ~Oct 15, 2026 |

## Quality Assessment
Moondream's niche is on-device/local vision: fast query/detect/caption in a small footprint rather than frontier general reasoning. At $0.30/$2.50 through OpenRouter it is not the cheap vision option (nano-tier models undercut it), but it is a reliable, well-tested local-friendly VLM with strong detection for its size. For embedded/local vision tasks it competes well; for heavy multimodal reasoning the frontier closed VLMs win on quality.

## Notes
- Preview channel: expect weight/config churn until the stable 3.1 release; pricing steady across the preview -> 3.1 transition.
- Classified `open` (Lightweight).