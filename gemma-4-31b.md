---
model: Gemma-4-31B-IT
organization: Google DeepMind
license: Apache 2.0
release_date: 2026-04
last_updated: 2026-07-08
---

# Gemma 4 31B-IT

Google's Gemma 4 series. Dense 31B model with multimodal (image-text-to-text) capability. Apache 2.0. Strong general-purpose model with excellent GGUF support and a MTP (multi-token prediction) variant for faster inference.

## Architecture
- Total params: ~31B (dense, all active)
- Architecture: Gemma4 (dense transformer)
- Layers: 60
- Hidden size: 5376
- Attention heads: 32, KV heads: 16 (GQA)
- Intermediate size: 21,504
- Context length: 262,144 (256K)
- Multimodal: image-text-to-text
- Sliding window attention supported

## Self-Hosting
### GGUF (llama.cpp via unsloth/gemma-4-31b-it-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | ~18 GB | 21 GB | Sweet spot, RTX 4090 friendly |
| Q3_K_M | ~15 GB | 17 GB | |
| Q5_K_M | ~21 GB | 24 GB | |
| Q6_K | ~24 GB | 27 GB | |
| Q8_0 | ~31 GB | 34 GB | |
| UD-IQ2_M | ~8 GB | 10 GB | Aggressive, 12GB cards |
| BF16 | ~62 GB (2 shards) | 66 GB | Full precision |
| MTP variants | varies | varies | Multi-token prediction, faster |

### FP8/FP4 (vLLM on GPU)
- FP8: ~31 GB, single RTX 4090 (24GB tight)
- BF16: ~62 GB, 2× 4090 or A100

### Other engines
- MLX on Apple Silicon: Q4 works well on M2/M3 with 32GB
- MTP (multi-token prediction) GGUF variants available for ~2× speedup

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (google/gemma-4-31b-it) | $0.12 | $0.35 | 256K | |

## Quality Benchmarks
- Strong general performance, competitive with Llama-4-Scout
- Good multimodal/vision capability
- MTP variant enables faster inference

## Notes
- HuggingFace: https://huggingface.co/google/gemma-4-31b-it
- 11.2M downloads, 3127 likes — extremely popular
- MTP (Multi-Token Prediction) GGUF variants are notable: speculative-decoding-style speedup
- Best Google open model for self-hosting as of mid-2026
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
