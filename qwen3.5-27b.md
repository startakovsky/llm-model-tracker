---
model: Qwen3.5-27B
organization: Alibaba (Qwen Team)
license: Apache 2.0
release_date: 2026-02
last_updated: 2026-07-05
---

# Qwen3.5-27B

Dense (non-MoE) Qwen3.5 model. All 27B params active per token. Multimodal (image-text-to-text). Strong general-purpose model that runs comfortably on consumer hardware.

## Architecture
- Total params: 27B (dense, all active)
- Architecture: Qwen3_5 (dense transformer)
- Layers: 64
- Hidden size: 5120
- Attention heads: 24, KV heads: 4 (GQA)
- Intermediate size: 17,408
- Context length: 262,144 (256K)
- Multimodal: image-text-to-text, video support

## Self-Hosting
### GGUF (llama.cpp via unsloth/Qwen3.5-27B-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | 15.59 GB | 18 GB | Sweet spot |
| Q3_K_M | ~12 GB | 14 GB | |
| Q5_K_M | ~18 GB | 21 GB | |
| Q6_K | ~21 GB | 24 GB | Near-lossless |
| Q8_0 | ~27 GB | 30 GB | |
| UD-IQ2_M | ~9 GB | 11 GB | Aggressive, runs on 12GB |
| BF16 | ~54 GB (2 shards) | 58 GB | Full precision |

### FP8/FP4 (vLLM on GPU)
- FP8: ~27 GB, single RTX 4090 (24GB tight, 3090/4090 work with offload)
- BF16: ~54 GB, needs 2× 4090 or A100

### Other engines
- MLX on Apple Silicon: Q4 runs great on M2 Pro+ with 32GB
- One of the best dense models for local Mac deployment

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.5-27b) | $0.195 | $1.56 | 256K | |

## Quality Benchmarks
- Strong general-purpose performance
- Best-in-class for 27B dense models
- Good multimodal/vision capability
- Solid coding and reasoning

## Notes
- HuggingFace: https://huggingface.co/Qwen/Qwen3.5-27B
- 2.57M downloads, 996 likes
- Best dense alternative to Llama-4-Scout for local deployment
- Video understanding support (video_preprocessor_config.json)
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
