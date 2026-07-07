---
model: Qwen3.5-397B-A17B
organization: Alibaba (Qwen Team)
license: Apache 2.0
release_date: 2026-02
last_updated: 2026-07-07
---

# Qwen3.5-397B-A17B

Frontier MoE from Qwen's 3.5 series. 512 experts with 10 active per token — the largest open-weights Qwen to date. Multimodal (image-text-to-text). Competes with GPT-5.5, Claude, Gemini at the frontier.

## Architecture
- Total params: ~397B (512 experts)
- Active params per token: ~17B (10 experts active)
- Architecture: Qwen3_5MoE (MoE, 512 experts, top-10 routing)
- Layers: 60
- Hidden size: 4096
- Attention heads: 32, KV heads: 2 (extreme GQA)
- Context length: 262,144 (256K)
- Multimodal: image-text-to-text, conversational
- Native dtype: BF16

## Self-Hosting
### GGUF (llama.cpp via unsloth/Qwen3.5-397B-A17B-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~795 GB (17 shards) | ~850 GB | Full precision, impractical |
| MXFP4_MOE | ~225 GB (6 shards) | ~250 GB | MoE-only MXFP4, best for self-host |
| Q4_K_M | ~240 GB (est.) | ~270 GB | Standard GGUF quant |

### FP8/FP4 (vLLM on GPU)
- FP8 weights: ~400 GB
- Requires 5× H100 80GB or 6× A100 80GB
- MXFP4 MoE offload via KTransformers possible on CPU+GPU hybrid

### Other engines
- KTransformers: MoE expert offload to CPU, ~30 tok/s on dual Xeon + single H100
- SGLang: supports Qwen3.5 MoE

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.5-397b-a17b) | $0.385 | $2.45 | 256K | |
| Qwen API (direct) | varies | varies | 256K | |

## Quality Benchmarks
- Frontier-class on MMLU, GPQA, AIME
- Strong multilingual (Qwen's traditional strength)
- Multimodal: strong vision understanding

## Notes
- HuggingFace: https://huggingface.co/Qwen/Qwen3.5-397B-A17B
- 415K downloads, 1526 likes
- Apache 2.0 — fully open
- MXFP4_MOE GGUF format is notable: MoE-only quantization keeps shared layers in higher precision
- Best frontier open-weight alternative to GLM-5.2 and DeepSeek V4 Pro
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
