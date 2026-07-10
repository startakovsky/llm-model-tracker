---
model: GPT-OSS-120B
organization: OpenAI
license: Apache 2.0
release_date: 2025-08
last_updated: 2026-07-08
---

# GPT-OSS-120B

OpenAI's first open-weight model release, part of the GPT-OSS family. Native MoE with MXFP4 weights and 128 experts. Apache 2.0 licensed. Designed to be efficient for self-hosting despite 120B total params.

## Architecture
- Total params: ~120B (128 experts × ~0.9B each + shared)
- Active params per token: ~5B (4 experts active per token)
- Architecture: MoE (128 local experts, top-4 routing)
- Layers: 36
- Hidden size: 2880
- Attention heads: 64, KV heads: 8 (GQA)
- Vocab: 201,088
- Context length: 131,072 (128K)
- Sliding window: 128 (local attention)
- Native weight dtype: MXFP4 (8-bit with microscaling)
- Sliding window attention for long-context efficiency

## Self-Hosting
### GGUF (llama.cpp via unsloth/gpt-oss-120b-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | ~92 GB (2 shards) | ~110 GB | Best quality/size balance |
| Q3_K_M | ~75 GB | ~90 GB | Lower quality |
| Q2_K | ~58 GB | ~70 GB | Aggressive, quality loss |
| Q5_K_M | ~105 GB | ~120 GB | Higher quality |
| Q6_K | ~120 GB | ~140 GB | Near-lossless |

### FP8/FP4 (vLLM on GPU)
- Native MXFP4 weights: ~63 GB model size
- Runs on a single H100 80GB (tight) or 2× A100 80GB
- vLLM supports gpt_oss model type natively
- Fast inference: ~60-80 tok/s on H100

### Other engines
- MLX supported on Apple Silicon (Mac Studio M2 Ultra can run Q4)
- KTransformers: works with GGUF MoE offload

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (openai/gpt-oss-120b) | $0.03 | $0.15 | 128K | Very cheap |
| OpenRouter (free) | $0 | $0 | 128K | Rate-limited free tier |

## Quality Benchmarks
- Competitive with GPT-4.1-mini class on reasoning
- Strong on coding (HumanEval, MBPP)
- MMLU: ~78
- Designed for agentic/tool-use workflows

## Notes
- HuggingFace: https://huggingface.co/openai/gpt-oss-120b
- 4.18M downloads, 4946 likes
- OpenAI's first true open-weight release (Apache 2.0)
- MXFP4 native quantization is a breakthrough — minimal quality loss vs FP16
- Best value open model for sub-$0.20/M token pricing
- OpenRouter free tier makes it accessible for testing
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
