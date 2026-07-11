---
model: Granite 4.1 8B
organization: IBM
license: Apache 2.0
release_date: 2026-04-30
last_updated: 2026-07-11
---

# Granite 4.1 8B

## Architecture
- **Total params:** 8B (dense, decoder-only)
- **Context length:** 131,072
- **Modality:** Text → Text
- **Architecture type:** Dense language model

## Self-Hosting
8B dense model — easily self-hostable on consumer hardware (8GB VRAM with Q4 quantization, 16GB for Q8). Fast inference on CPU as well.

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (ibm-granite/granite-4.1-8b) | $0.05 | $0.10 | 131,072 |

## Quality Assessment
Granite 4.1 8B is part of IBM's Granite 4.1 family, designed for enterprise tasks. Dense 8B architecture with 131K context window. At $0.05/$0.10/M via API, it's ultra-cheap. Over 1M HF downloads and 214 likes indicate strong enterprise adoption. Best suited for lightweight enterprise tasks — document processing, classification, summarization. Not frontier quality, but excellent value for cost-sensitive enterprise deployments.

## Notes
- Apache 2.0, fully open for commercial use
- Dense 8B — trivial to self-host
- Strong enterprise adoption (1M+ HF downloads)
- Part of the Granite 4.1 family
