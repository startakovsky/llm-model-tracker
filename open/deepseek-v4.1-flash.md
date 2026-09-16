---
model: DeepSeek V4.1 Flash
organization: DeepSeek AI
license: MIT
release_date: 2026-09-10
last_updated: 2026-09-16
sources:
  - https://openrouter.ai/deepseek/deepseek-v4.1-flash
  - https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
---

# DeepSeek V4.1 Flash

Released Sep 10, 2026 — DeepSeek's Flash-tier refresh with a new **Causal Encoder-Decoder (CED)** architecture built around KV-cache compression. Multimodal (image + text), strong agentic performance, and notably cheap for input-heavy workloads.

## Architecture
- **Total params:** 552B backbone (sparse MoE)
- **Active params per token:** ~8B prefill / ~16B decode
- **Context length:** 1,048,576 (1M)
- **Architecture:** CED — 20-layer causal encoder + 20-layer decoder (40 layers total). Decoder's global KV cache is projected from the final encoder hidden states rather than recomputed per layer, sharply cutting prefill KV cost.
- **Multimodal:** native image + text; 32-layer vision encoder (1024 hidden, patch_size 14)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4.1-flash) | $0.15 | $0.60 | 1,048,576 | Live Sep 10 |

## Quality Assessment
Positioned ~Fable-tier on autonomous SWE with 1/15th the cost (Fireworks: "Astra-level DeepSWE at 1/15th"). Hacker News commenters call it the best hacking/infra model; strong r/LocalLLaMA reception. Priced above base V4 Flash ($0.065/$0.18) — smarter and faster, with a commensurate bump — but still a fraction of GLM-5.2 / frontier-closed costs. Standout value for input-heavy long-context agentic work thanks to the 8B-active prefill design.

## Notes
- MIT license; weights on HuggingFace (deepseek-ai/DeepSeek-V4.1-Flash, ~2.8K likes).
- GGUF quants and FP8 packs surfaced within days (antirez GGUF 336K downloads).
- KV-cache compression is the headline feature ("Pushing the Limits of KV Cache Compression").