---
model: DeepSeek V4 Flash
organization: DeepSeek AI
license: MIT
release_date: 2026-06
last_updated: 2026-07-04
---

# DeepSeek V4 Flash

## Architecture
- **Total params:** ~290B (MoE)
- **Active params per token:** ~13.5B (6 of 256 experts)
- **Context length:** 1,048,576
- **Layers:** 43, hidden_size=4096, 256 routed experts, moe_intermediate_size=2048
- **Model type:** deepseek_v4 (DeepseekV4ForCausalLM)

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4 experts (antirez mixed) | 164.6GB | 192GB+ | antirez/deepseek-v4-gguf |
| IQ2XXS mixed (antirez) | 86.7GB | 128GB+ | Attention at Q8, experts at Q2 |
| MXFP4 (bartowski) | 156GB | 192GB+ | bartowski/DeepSeek-V4-Flash-GGUF |

Source: https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash

### DwarfStar (antirez engine)
- Mac Studio M3 Ultra 512GB: DeepSeek V4 Pro at 150 t/s prefill, 10-13 t/s decode
- M5 Max 128GB: DeepSeek V4 Flash at 500 t/s prefill, 35-40 t/s decode
- Selective mixed-precision: 568GB model compressed to 81GB

### llama.cpp support
- WIP as of late June 2026 (PR #24162)
- Not yet merged into mainline

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4-flash) | $0.09 | $0.18 | 1,048,576 | 10x cheaper than GLM-5.2 |

## Quality Benchmarks
- Coding average: 72.2 (benchlm.ai)
- Agentic: 55.4 (benchlm.ai)
- Strong competitor to GLM-5.2 at fraction of cost

## Notes
- 2.1M downloads — extremely popular
- DeepSeek V4 Pro also exists (1.6T total, 49B active, IQ2: 465GB)
- llama.cpp PR in progress — will become a local option when merged
