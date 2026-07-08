---
model: GPT-OSS-20B
organization: OpenAI
license: Apache 2.0
release_date: 2025-08
last_updated: 2026-07-08
---

# GPT-OSS-20B

Smaller sibling of GPT-OSS-120B. 32-expert MoE with only 3B active params. Designed for edge/local deployment — runs on consumer hardware. Apache 2.0 licensed.

## Architecture
- Total params: ~20B (32 experts)
- Active params per token: ~3B (4 experts active per token)
- Architecture: MoE (32 local experts, top-4 routing)
- Layers: 24
- Hidden size: 2880
- Attention heads: 64, KV heads: 8 (GQA)
- Vocab: 201,088
- Context length: 131,072 (128K)
- Sliding window: 128
- Native weight dtype: MXFP4

## Self-Hosting
### GGUF (llama.cpp via unsloth/gpt-oss-20b-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | 10.83 GB | 13 GB | Sweet spot, runs on 16GB GPU/Mac |
| Q3_K_M | ~9 GB | 11 GB | |
| Q5_K_M | ~12 GB | 15 GB | |
| Q6_K | ~14 GB | 17 GB | Near-lossless |
| Q8_0 | ~18 GB | 21 GB | |
| F16 | ~37 GB | 40 GB | Full precision |

### FP8/FP4 (vLLM on GPU)
- Native MXFP4: ~11 GB model size
- Runs on single RTX 4090 (24GB) or RTX 3090
- vLLM native support

### Other engines
- MLX on Apple Silicon: Q4 runs on M2/M3 with 16GB+ unified memory
- Extremely fast on consumer hardware

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (openai/gpt-oss-20b) | $0.029 | $0.14 | 128K | |
| OpenRouter (free) | $0 | $0 | 128K | Rate-limited |

## Quality Benchmarks
- Approaches GPT-4.1-mini on many tasks
- MMLU: ~74
- Strong coding for its size
- Good agentic/tool-use capability

## Notes
- HuggingFace: https://huggingface.co/openai/gpt-oss-20b
- 6.92M downloads, 4765 likes — one of the most downloaded open models ever
- Best small open model for self-hosting as of mid-2026
- Pairs well with gpt-oss-120b for cost-tiered routing
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
