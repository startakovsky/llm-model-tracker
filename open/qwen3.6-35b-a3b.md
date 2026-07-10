---
model: Qwen3.6-35B-A3B
organization: Alibaba (Qwen Team)
license: Apache-2.0
release_date: 2026-04
last_updated: 2026-07-09
sources:
  - https://huggingface.co/Qwen/Qwen3.6-35B-A3B
  - https://openrouter.ai/qwen/qwen3.6-35b-a3b
  - https://unsloth.ai/docs/models/qwen3.6
---

# Qwen3.6-35B-A3B

MoE variant of Qwen3.6 — 35B total params but only 3B active per token. Uses the same hybrid linear/full attention architecture and MTP as the 27B dense model, with 256 experts (top-8) and a shared expert. Multimodal (image, video). Runs on 22GB RAM quantized.

## Architecture
- Total params: 35B (MoE)
- Active params per token: 3B
- Architecture: Qwen3_5 MoE (hybrid linear/full attention)
- Layers: 40 (every 4th layer is full attention, rest linear attention)
- Hidden size: 2048
- Experts: 256 total, 8 activated per token, 1 shared expert
- MoE intermediate size: 512
- Attention heads: 16, KV heads: 2 (GQA), head dim 256
- Linear attention: 16 key heads, 32 value heads, key/value dim 128, conv kernel 4
- Context length: 262,144 (256K native)
- MTP: 1 layer, multi-token prediction for 1.4-2.2x faster inference
- Multimodal: image-text-to-text, video support
- Vocab: 248,320

## Self-Hosting
### GGUF (llama.cpp via unsloth/Qwen3.6-35B-A3B-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q3_K_M | ~13 GB | 15 GB | Budget |
| Q4_K_M | ~16 GB | 22 GB | Sweet spot |
| Q5_K_M | ~19 GB | 24 GB | |
| Q6_K | ~22 GB | 28 GB | Near-lossless |
| Q8_0 | ~28 GB | 34 GB | |
| BF16 | ~70 GB | 74 GB | Full precision |

Unsloth Dynamic 2.0 quants with calibrated important-layer upcasting. Developer role support for Codex, OpenCode.

### FP8/FP4 (vLLM on GPU)
- FP8: ~35 GB, single RTX 4090 with offload or A100
- BF16: ~70 GB, 2× 4090 or A100
- MTP support in Unsloth Studio

### Other engines
- With only 3B active params, this model is extremely fast on consumer hardware
- MLX on Apple Silicon: Q4 runs well on M2 Pro+ with 24GB

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.6-35b-a3b) | $0.14 | $1.00 | 256K | Created 2026-04-27 |

## Quality Assessment
Qwen3.6-35B-A3B achieves 73.4% SWE-bench Verified (vs GLM-5.2's 82.8%) and 51.5 Terminal-Bench 2.0 (vs GLM-5.2's 81.0). At only 3B active params, it delivers 88% of GLM-5.2's SWE-bench performance with extreme inference efficiency. It scores 1397 on QwenWebBench for frontend code generation. The `preserve_thinking` parameter supports iterative agentic coding.

The MoE design with 256 experts means only 3B params are active per token, making this one of the fastest models in its quality class on consumer hardware. The tradeoff is slightly lower Terminal-Bench (51.5 vs 59.3 for the 27B dense) despite higher SWE-bench, suggesting it's better at code generation than complex terminal workflows.

**Agentic verdict:** Qwen3.6-35B-A3B is a good local option for coding tasks but weaker for full agentic workflows. At 51.5 Terminal-Bench (64% of GLM-5.2's 81.0), it handles tool-calling and multi-step reasoning but will struggle on complex agent chains. Best use case: fast local coding assistant on consumer hardware where the 3B active params give excellent speed/quality ratio. Does NOT replace GLM-5.2 for agentic work.

## Sources
- Primary: https://huggingface.co/Qwen/Qwen3.6-35B-A3B (6.59M downloads, 2,354 likes)
- Validation: https://unsloth.ai/docs/models/qwen3.6 (self-hosting guide, hardware requirements)
- Benchmarks: https://qwenchat.online/qwen-code (SWE-bench, Terminal-Bench scores)
- GGUF: https://huggingface.co/unsloth/Qwen3.6-27B-GGUF (sibling model, same quants available)
