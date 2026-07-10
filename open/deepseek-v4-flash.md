---
model: DeepSeek V4 Flash
organization: DeepSeek AI
license: MIT
release_date: 2026-06
last_updated: 2026-07-08
sources:
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash
  - https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF
---

# DeepSeek V4 Flash

## Architecture
- **Total params:** 284B (MoE) — corrected from DeepSeek V4 official model card
- **Active params per token:** 13B (corrected)
- **Context length:** 1,048,576
- **Layers:** 43, hidden_size=4096, 256 routed experts, moe_intermediate_size=2048
- **Model type:** deepseek_v4 (DeepseekV4ForCausalLM)
- **Architecture:** DeepSeek V4 with Compressed Sparse Attention (CSA) & Heavily Compressed Attention (HCA) — compresses KV cache for efficient long-context

## Self-Hosting

### GGUF (llama.cpp / Unsloth)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| UD-Q4_K_XL | ~155GB | 192GB+ | Unsloth Dynamic 2.0, near-lossless |
| UD-Q8_K_XL | 162GB | 192GB+ | Full precision lossless, only 7GB bigger than Q4 |
| UD-IQ1_M | ~86GB | 128GB+ | 1-bit dynamic, multi-file |
| Q4 experts (antirez mixed) | 164.6GB | 192GB+ | antirez/deepseek-v4-gguf |
| IQ2XXS mixed (antirez) | 86.7GB | 128GB+ | Attention at Q8, experts at Q2 |
| MXFP4 (bartowski) | 156GB | 192GB+ | bartowski/DeepSeek-V4-Flash-GGUF |

Source: https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF

**llama.cpp now supported!** Unsloth confirmed DeepSeek-V4 is ready to run as of July 7, 2026. Chat template tested over 4000 conversations. Run via:
```bash
llama serve -hf unsloth/DeepSeek-V4-Flash-GGUF:UD-Q4_K_XL
```

### DwarfStar (antirez engine)
- Mac Studio M3 Ultra 512GB: DeepSeek V4 Pro at 150 t/s prefill, 10-13 t/s decode
- M5 Max 128GB: DeepSeek V4 Flash at 500 t/s prefill, 35-40 t/s decode
- Selective mixed-precision: 568GB model compressed to 81GB

### Unsloth Studio
- Full GUI support with High and Max thinking toggles
- `curl -fsSL https://unsloth.ai/install.sh | sh && unsloth studio -H 0.0.0.0 -p 8888`

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4-flash) | $0.09 | $0.18 | 1,048,576 | 10x cheaper than GLM-5.2 |

## Quality Benchmarks
- Coding average: 72.2 (benchlm.ai)
- Agentic: 55.4 (benchlm.ai)
- Strong competitor to GLM-5.2 at fraction of cost

## Quality Assessment
DeepSeek V4 Flash scores 72.2 coding average (benchlm.ai) — roughly 85-90% of GLM-5.2's coding quality at 1/10th the API cost ($0.09+$0.18/M vs $0.91+$2.86/M). Strong on logical reasoning and coding. Weaker on agentic tasks (55.4 vs GLM-5.2's higher scores). For cost-conscious workflows, this is the best value frontier-tier model available. The 1M context window matches GLM-5.2.

## Notes
- 6.4M downloads (antirez GGUF) + 2.1M+ (official) — extremely popular
- Unsloth confirmed llama.cpp support ready as of July 7, 2026
- DeepSeek V4 Pro also exists (1.6T total, 49B active, IQ2: 465GB)
- DeepSeek V4 architecture uses CSA + HCA for KV cache compression
- Unsloth Dynamic 2.0 quants achieve superior accuracy vs other quants
