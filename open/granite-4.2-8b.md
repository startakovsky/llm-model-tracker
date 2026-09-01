---
model: Granite 4.2 8B
organization: IBM
license: Apache 2.0
release_date: 2026-08-25
last_updated: 2026-09-01
sources:
  - https://huggingface.co/ibm-granite/granite-4.2-8b
  - https://openrouter.ai/ibm-granite/granite-4.2-8b
---

# Granite 4.2 8B

IBM's Granite 4.2 lightweight 8.8B dense model, the mid-2026 refresh of the Granite enterprise 8B line (family built on the Granite 4.1 base). Apache 2.0 open weights, uploaded to HuggingFace Aug 25, 2026.

## Architecture
- **Total params:** 8.79B (dense, decoder-only)
- **Context length:** 131,072
- **Modality:** Text → Text
- **Architecture type:** Dense, instruction-tuned enterprise LLM

## Self-Hosting
8.8B dense — trivial to self-host on consumer/edge hardware (~8GB VRAM with Q4, 16GB for Q8). One of the lightest frontier-lab-adjacent models with open weights and a 131K context.

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (ibm-granite/granite-4.2-8b) | $0.10 | $0.15 | 131,072 |

## Quality Assessment
Entry point to IBM's enterprise Granite family. ~8.8B dense, Apache 2.0, cheap ($0.10/$0.15/M). Not frontier — below Granite 4.1-class enterprise tuning on complex reasoning but solid for document classification, summarization, extraction, and cost-sensitive enterprise tasks. Value proposition is license simplicity and negligible cost, not raw capability. ~50% of GLM-5.2-class quality at ~1/40th the price.

## Notes
- Apache 2.0, fully open for commercial use
- 8.8B dense — trivial to self-host
- Successor to Granite 4.1 8B (already tracked in this repo)
- ~10.4k HF downloads in first week