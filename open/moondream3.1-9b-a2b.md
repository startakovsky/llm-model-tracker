---
model: Moondream 3.1
organization: Moondream
license: Moondream Model License 1.0
release_date: 2026-10-15
last_updated: 2026-10-19
sources:
  - https://huggingface.co/moondream/moondream3.1-9B-A2B
  - https://moondream.ai/blog/moondream-3-1-beyond-benchmarks
  - https://openrouter.ai/moondream/moondream3.1-9b-a2b
---

# Moondream 3.1

Vision-language model with mixture-of-experts architecture (9B total / 2B active), released Oct 15, 2026. SOTA-tier visual reasoning and detection for its size class, designed to run locally on commodity GPUs (Ampere+) and Apple Silicon.

## Architecture
- **Type:** 9B total / 2B active MoE vision-language model
- **Context length:** 32,000
- **Capabilities:** native `query`, `detect`, `point`, `caption` skills, all structured output
- **Runtime:** Moondream "Photon" inference engine; `pip install moondream` for local use; Moondream Cloud with free tier

## API Providers
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (moondream/moondream3.1-9b-a2b) | $0.30 | $2.50 | 32,000 |

## Quality Assessment
The strongest open small-VL option for local visual reasoning: 2B-active MoE keeps it fast and cheap, benchmarks position it well above prior Moondream generations for detection and visual QA. At $0.30/$2.50 via API it's a budget VL pick versus Gemini Nano Banana-style offerings. Note the Moondream Model License (not Apache). Quality score 74.

## Notes
- Moondream 3 preview also live on HF (85K downloads, 692 likes) — 3.1 is the refined successor
- Weights on HuggingFace (`moondream/moondream3.1-9B-A2B`, 12.6K downloads)