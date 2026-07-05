---
model: Qwen3.5-122B-A10B
organization: Alibaba (Qwen Team)
license: Apache 2.0
release_date: 2026-02
last_updated: 2026-07-05
---

# Qwen3.5-122B-A10B

Mid-tier Qwen3.5 MoE. 256 experts with 8 active. Multimodal. The sweet spot for self-hosting a frontier-class model on a single high-end GPU or dual-GPU rig.

## Architecture
- Total params: ~122B (256 experts)
- Active params per token: ~10B (8 experts active)
- Architecture: Qwen3_5MoE (MoE, 256 experts, top-8 routing)
- Layers: 48
- Hidden size: 3072
- Attention heads: 32, KV heads: 2 (GQA)
- Context length: 262,144 (256K)
- Multimodal: image-text-to-text

## Self-Hosting
### GGUF (llama.cpp via unsloth/Qwen3.5-122B-A10B-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~245 GB (5 shards) | ~270 GB | Full precision |
| MXFP4_MOE | ~70 GB (3 shards) | ~80 GB | Best for self-host |
| Q4_K_M | ~73 GB (3 shards) | ~85 GB | Standard quant, fits 96GB |
| Q3_K_M | ~60 GB | ~70 GB | Lower quality |
| Q4_K_S | ~68 GB | ~78 GB | Slightly smaller |

### FP8/FP4 (vLLM on GPU)
- FP8: ~125 GB, needs 2× H100 80GB
- MXFP4 MoE: ~70 GB, single H100 80GB feasible

### Other engines
- KTransformers: CPU MoE offload, ~40 tok/s on dual Xeon + RTX 4090
- MLX: not yet supported for Qwen3.5 MoE

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.5-122b-a10b) | $0.26 | $2.08 | 256K | |

## Quality Benchmarks
- Approaches Qwen3.5-397B on most benchmarks (within 3-5 points)
- Strong coding, math, reasoning
- Multimodal vision understanding

## Notes
- HuggingFace: https://huggingface.co/Qwen/Qwen3.5-122B-A10B
- 770K downloads, 582 likes
- Best Qwen3.5 model for self-hosting on a single 96GB machine
- MXFP4_MOE GGUF is the recommended format
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
