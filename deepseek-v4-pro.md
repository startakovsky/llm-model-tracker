---
model: DeepSeek V4 Pro
organization: DeepSeek AI
license: MIT
release_date: 2026-06
last_updated: 2026-07-05
---

# DeepSeek V4 Pro

## Architecture
- **Total params:** ~1.6T (MoE)
- **Active params per token:** ~49B
- **Context length:** 1,048,576

## Self-Hosting

### GGUF (llama.cpp / antirez)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| IQ2XXS mixed (antirez) | 464.6GB | 512GB+ | antirez/deepseek-v4-gguf |
| Q4K (antirez, 2-part) | ~900GB | 1TB+ | Full Q4, not practical for most |

Source: https://huggingface.co/antirez/deepseek-v4-gguf

### DwarfStar (antirez engine)
- Mac Studio M3 Ultra 512GB: 150 t/s prefill, 10-13 t/s decode

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4-pro) | $0.43 | $0.87 | 1,048,576 | Half the cost of GLM-5.2 |

## Quality Assessment
DeepSeek V4 Pro is the largest open-weights model available (1.6T params, 49B active). It competes directly with GLM-5.2 on reasoning and coding quality. Self-hosting requires 512GB+ RAM even at 2-bit quant — only feasible on high-memory servers or Mac Studio Ultra. For most users, DeepSeek V4 Flash (290B, 1/10th the API cost) is the better practical choice. V4 Pro is for when you need maximum quality and have the hardware to run it.

## Sources
- Primary: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
- Validation: https://huggingface.co/antirez/deepseek-v4-gguf
