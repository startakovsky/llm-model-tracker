---
model: Ling 3.0 Tiny
organization: inclusionAI
license: MIT
release_date: 2026-08-08
last_updated: 2026-11-13
sources:
  - https://huggingface.co/inclusionAI/Ling-3.0-Tiny
  - https://openrouter.ai/inclusionai/ling-3.0-tiny
---

# Ling 3.0 Tiny — inclusionAI

| Field | Value |
|---|---|
| **Org** | inclusionAI (Ant Group) |
| **OpenRouter ID** | `inclusionai/ling-3.0-tiny` |
| **HuggingFace** | [inclusionAI/Ling-3.0-Tiny](https://huggingface.co/inclusionAI/Ling-3.0-Tiny) |
| **License** | MIT |
| **Release date** | ~Aug 2026 (listed on OpenRouter Aug 8) |
| **Pricing** | $0.015/$0.045 per M tokens (cheapest tracked listing) |
| **Context** | 262,144 (262K) on OpenRouter (128K native per HF config) |
| **Category** | Lightweight (open) |

## Architecture

- **BailingMoeV3** hybrid MoE (`bailing_hybrid` model type) — 24 layers, hidden size 1536, 16 attention heads, vocab 157,184.
- Smallest member of the Ling 3.0 family (vs Ling 3.0 Flash at 124B/5.1B MoE).
- Open weights on HuggingFace: 13.7K downloads, 583 likes, 32 safetensors shards.
- MIT license, matching the rest of the Ling 3.0 open line.

## Quality Assessment

Entry-level tier of the Ling family: ~1-2% of the price of Ling 3.0 Flash ($0.015/$0.045 vs $0.021/$0.063 is actually comparable per-token — the value is the smaller footprint). Quality score 52. Not a frontier or even mid-tier competitor; suited to high-volume, low-complexity tasks where the marginal cost matters most. Cheapest model in the tracker by completion price.

**Verdict:** A curiosity-tier addition to the Ling family — notable mainly as the cheapest tracked listing and for the open MIT weights. Tracked Nov 13.
