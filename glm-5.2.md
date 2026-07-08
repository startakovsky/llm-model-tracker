---
model: GLM-5.2
organization: Z.ai
license: MIT
release_date: 2026-06-13
last_updated: 2026-07-08
---

# GLM-5.2

## Architecture
- **Total params:** 753B (MoE)
- **Active params per token:** ~40B
- **Context length:** 1,000,000 (native), 131,072 max output
- **Pre-training data:** 28.5T tokens
- **Architecture type:** GLM MoE with DeepSeek Sparse Attention

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Accuracy | Min RAM | Notes |
|---|---|---|---|---|
| BF16 | ~1.5TB | 100% | 1.5TB+ | Not practical |
| UD-Q4_K_XL | 467GB | ~97% | 512GB+ | Near-lossless, needs big server |
| UD-Q2_K_XL | 254GB | ~82% | 256GB+ | Fits 256GB Mac or 352GB EPYC |
| UD-IQ1_M | ~188GB | ~76% | 192GB+ | 1-bit dynamic |

Source: https://huggingface.co/unsloth/GLM-5.2-GGUF

### NVFP4 (vLLM, Blackwell GPUs)
| Variant | Size | GPQA | Notes |
|---|---|---|---|
| nvidia/GLM-5.2-NVFP4 | 465GB | 89.39 | Full model, near-lossless (FP8=89.52) |
| 0xSero/GLM-5.2-NVFP4-REAP-469B | 313GB | ~87 | REAP-pruned 37%, 60 t/s on 4x RTX PRO 6000 |
| madeby561/GLM-5.2-Int8Mix-NVFP4-REAP-594B | ~370GB | 86.87 | 22% prune, 97% retained |

### KTransformers (hybrid CPU/GPU)
- Supported in KTransformers v0.5.12+ via KT-Kernel + SGLang
- Config: TP8, 96 CPU threads, 30 GPU experts (FP8), NSA attention, FP8 KV cache
- Tutorial: ktransformers/doc/en/kt-kernel/GLM-5.2-Tutorial.md

### Real-world speed benchmarks
| Hardware | Quant | Speed | Source |
|---|---|---|---|
| 4x RTX PRO 6000 (b12x vLLM) | NVFP4 REAP-469B | 60 t/s @ 250K ctx | github.com/0xSero/glm-5.2-sm120 |
| 4x DGX Spark GB10 | NVFP4 (Mapika, no REAP) | 15 t/s @ 128K ctx | NVIDIA forums |
| Mac Studio M3 Ultra 256GB | UD-Q2_K_XL | 3-9 t/s | Reddit r/LocalLLaMA |
| 4x3090 + 192GB RAM | UD-Q2_K_XL | 7.3 t/s | Reddit r/LocalLLaMA |
| EPYC 9454P 352GB (est) | UD-Q2_K_XL | 8-15 t/s (est) | DDR5-4800 bandwidth calc |
| 8x B200 (Baseten) | NVFP4 | 280+ t/s | Baseten blog |

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (z-ai/glm-5.2) | $0.93 | $3.00 | 1,048,576 | Daily driver |
| Z.ai direct (Coding Plan) | Subscription | Subscription | 1M | $1,344/yr Max tier |

## Quality Benchmarks
- Terminal-Bench 2.1: 81.0
- SWE-bench Pro: 62.1
- SWE-bench Verified: 82.8%
- DesignArena: #1
- Code Arena Frontend: #2
- No official benchmarks at launch (DataCamp confirmed)

## Quality Assessment
GLM-5.2 is the current reference point for open-weight frontier quality. It excels at coding (82.8% SWE-bench Verified), agentic tool use (81.0 Terminal-Bench), and long-context reasoning (1M native context). Community reports rate it on par with or above Claude Opus 4.6 for coding. This is the benchmark other models in this tracker are compared against.

## Notes
- GLM-5.2-Air does NOT exist as of July 4, 2026
- GLM 5.5 rumored for August 2026
- b12x is Luke Alonso's SM120 CuTe DSL kernel library, bundled in voipmonitor/vllm Docker images
- DCP (Decode Context Parallelism) shards KV cache across GPUs: DCP4 = 250K ctx on 4 GPUs
