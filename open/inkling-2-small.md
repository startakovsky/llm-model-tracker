---
model: Inkling 2 Small
organization: Thinking Machines
license: Apache 2.0
release_date: 2026-11-05
last_updated: 2026-11-13
sources:
  - https://huggingface.co/thinkingmachines/Inkling-2-Small
  - https://openrouter.ai/thinkingmachines/inkling-2-small
---

# Inkling 2 Small — Thinking Machines Lab

| Field | Value |
|---|---|
| **Org** | Thinking Machines Lab (Mira Murati) |
| **OpenRouter ID** | `thinkingmachines/inkling-2-small` (paid) and `:free` variant |
| **HuggingFace** | [thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) |
| **License** | Apache 2.0 (weights public Nov 2026) |
| **Release date** | 2026-11-05 |
| **Pricing** | $0.30/$1.00 per M (paid base listing live Nov 13; free endpoint remains) |
| **Context** | 1,048,576 (1M) |
| **Category** | Frontier (open) |

## Architecture

- **594B total / 17B active** MoE, multimodal (text+image), trained from scratch on 12.6T tokens with RL on long coding tasks.
- First model of Thinking Machines Lab's second Inkling generation (after Inkling and Inkling Small).
- Weights published to HuggingFace as Apache 2.0 (24 safetensors shards; ~1K downloads / 193 likes at tracking time) — the previously "promised after external safety testing" release is now live.

## Benchmarks

- AA Intelligence Index 31 (level with Gemini 3.8 Flash high; +18 over Inkling Small).
- Vision/docs best-in-class among open weights: MMMU Pro 81.6%, ScreenSpot Pro 83.8%, Vals Finance 61.5%, Vals Legal 73.9%.
- DeepSWE v1.1 72.1% (behind DeepSeek V4.1 Flash 77.0); AutomationBench 5% -> 46%; Terminal-Bench 4.0 only 13%.
- Chatty: ~150K output tokens/task (~$1.18/task at $0.30/$1.00).

## Quality Assessment

Strong open-weight vision/docs and long-coding model; weaker terminal-agent skills. At $0.30/$1.00 it undercuts most frontier open models (GLM-5.2 ~$0.007/$6.80 prompt-heavy pricing is not directly comparable; vs DeepSeek V4.1 Flash 1017 at $0.038/$0.50 it is ~8x the price with a lower DeepSWE score). Reclassified open from closed on Nov 13 when weights went public; quality score 78.
