---
model: Qwen3.6-27B
organization: Alibaba (Qwen Team)
license: Apache-2.0
release_date: 2026-04
last_updated: 2026-07-09
sources:
  - https://huggingface.co/Qwen/Qwen3.6-27B
  - https://openrouter.ai/qwen/qwen3.6-27b
  - https://unsloth.ai/docs/models/qwen3.6
---

# Qwen3.6-27B

Dense (non-MoE) Qwen3.6 model with hybrid linear+full attention, multi-token prediction (MTP), and multimodal (image, video) support. A major jump over Qwen3.5-27B in coding and agentic tasks. Runs on as little as 18GB RAM quantized.

## Architecture
- Total params: 27B (dense, all active)
- Architecture: Qwen3_5 (dense transformer, hybrid linear/full attention)
- Layers: 64 (every 4th layer is full attention, rest linear attention)
- Hidden size: 5120
- Attention heads: 24, KV heads: 4 (GQA), head dim 256
- Linear attention: 16 key heads, 48 value heads, key/value dim 128, conv kernel 4
- Intermediate size: 17,408
- Context length: 262,144 (256K native, extendable to 1M via YaRN)
- MTP: 1 layer, multi-token prediction for 1.4-2.2x faster inference
- Multimodal: image-text-to-text, video support
- Vocab: 248,320

## Self-Hosting
### GGUF (llama.cpp via unsloth/Qwen3.6-27B-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q3_K_M | ~12 GB | 14 GB | Budget option |
| IQ4_XS | ~14 GB | 15 GB | Dynamic 2.0, popular choice |
| Q4_K_M | ~16 GB | 18 GB | Sweet spot |
| Q5_K_M | ~18 GB | 21 GB | |
| Q6_K | ~21 GB | 24 GB | Near-lossless |
| Q8_0 | ~27 GB | 30 GB | |
| BF16 | ~55 GB | 58 GB | Full precision |

Unsloth Dynamic 2.0 quants — calibrated on real-world use-case datasets, important layers upcasted. Developer role support for Codex, OpenCode.

### FP8/FP4 (vLLM on GPU)
- FP8: ~27 GB, single RTX 4090 (tight, works with offload)
- BF16: ~55 GB, 2× 4090 or A100
- MTP support in Unsloth Studio for 1.4-2.2x faster inference

### Other engines
- MLX on Apple Silicon: Q4 runs great on M2 Pro+ with 32GB
- One of the best dense models for local Mac deployment

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.6-27b) | $0.29 | $2.40 | 256K | Created 2026-04-27 |

## Quality Assessment
Qwen3.6-27B is a standout dense model — it achieves 77.2% SWE-bench Verified (vs GLM-5.2's 82.8%), 59.3 Terminal-Bench 2.0 (vs GLM-5.2's 81.0), and 48.2 on SkillsBench (beating Claude 4.5 Opus's 45.3). At 93% of GLM-5.2's SWE-bench score while being a 27B dense model that runs on 18GB RAM, it is the best local self-hostable coding model in its weight class.

The hybrid linear/full attention architecture (every 4th layer is full attention, rest is linear) gives it efficient long-context handling. MTP support nearly doubles inference speed without accuracy loss. The `preserve_thinking` parameter maintains reasoning state across agent loop iterations, making it practical for iterative agentic coding workflows.

**Agentic verdict:** Qwen3.6-27B is a strong local-only option for agentic tool-use when you can't run GLM-5.2. At 59.3 Terminal-Bench (73% of GLM-5.2's 81.0), it handles multi-step tool-calling and coding agent workflows well for its size, but will struggle on the most complex 10+ tool-call chains. Best use case: local coding agent on consumer hardware (single GPU, 18-24GB RAM) where cloud API costs are prohibitive. It does NOT replace GLM-5.2 for serious agentic work — it's a capable local fallback.

## Sources
- Primary: https://huggingface.co/Qwen/Qwen3.6-27B (4.84M downloads, 1,930 likes)
- Validation: https://unsloth.ai/docs/models/qwen3.6 (self-hosting guide, hardware requirements)
- Benchmarks: https://qwenchat.online/qwen-code (SWE-bench, Terminal-Bench, SkillsBench scores)
- Community: https://blog.alexellis.io/local-ai-is-not-opus/ (real-world deployment report)
- GGUF: https://huggingface.co/unsloth/Qwen3.6-27B-GGUF
