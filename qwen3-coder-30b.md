---
model: Qwen3-Coder-30B-A3B-Instruct
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026
last_updated: 2026-07-04
---

# Qwen3-Coder-30B-A3B-Instruct

## Architecture
- **Total params:** 30B (MoE)
- **Active params per token:** 3B
- **Context length:** 160,000

## Self-Hosting
- GGUF (unsloth): Q4 ~18GB — fits any 24GB GPU or 24GB+ RAM
- MLX 4-bit and 5-bit available
- Very lightweight — can run alongside other services

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3-coder-30b-a3b-instruct) | $0.07 | $0.27 | 160,000 | Coding specialist |

## Notes
- Coding specialist — designed for code generation
- Extremely cheap to self-host (fits in 24GB)
- Good candidate for a coding-focused Tier 1 model
