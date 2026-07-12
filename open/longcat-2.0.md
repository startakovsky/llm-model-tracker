---
model: LongCat-2.0
organization: Meituan
license: MIT
release_date: 2026-07-05
last_updated: 2026-07-12
---

# LongCat-2.0

## Architecture
- **Total params:** 1.6T (MoE)
- **Active params per token:** ~48B
- **Context length:** 1,048,576 (1M native)
- **Pre-training data:** 35T+ tokens
- **Architecture type:** LongCat MoE with LongCat Sparse Attention (LSA)
- **Experts:** 768 routed experts, top-12 routing
- **N-gram Embedding:** 135B parameters (orthogonal sparse dimension)
- **Vocab size:** 163,840
- **Hardware:** Trained entirely on AI ASIC superpods (not GPUs)

## Key Innovations

### LongCat Sparse Attention (LSA)
Three orthogonal improvements over standard sparse attention:
1. **Streaming-aware Indexing (SI):** Reshapes token selection budget for coalesced HBM access
2. **Cross-Layer Indexing (CLI):** Single indexing pass serves multiple consecutive layers (2-layer sharing)
3. **Hierarchical Indexing (HI):** Coarse-to-fine two-stage scoring scheme

All strategies extend to Multi-Token Prediction (MTP) for speculative decoding.

### N-gram Embedding
Expands parameters in sparse dimensions orthogonal to MoE. 135B embedding parameters constrained within optimal range for robust superiority vs equivalent pure MoE.

## Self-Hosting
- Weights available on HuggingFace: `meituan-longcat/LongCat-2.0` (MIT license)
- Quantized variants: FP8, INT8, 3-bit (MLX)
- Config: `max_position_embeddings: 262144`, extended to 1M via DeepSeek YaRN rope scaling
- Architecture: `LongcatCausalLM` (custom architecture, requires LongCat library)
- 1,767 downloads, 179 likes on HuggingFace

## API Providers
Not yet available on OpenRouter. No public API pricing as of July 12, 2026.

## Quality Assessment
LongCat-2.0 is a frontier-scale open-weight model from Meituan, notable for being trained entirely on AI ASIC superpods rather than GPUs — demonstrating alternative hardware viability for frontier training. With 1.6T params and ~48B active, it competes with DeepSeek V4 Pro (1.6T/49B). Its LongCat Sparse Attention and N-gram Embedding innovations are architecturally distinct from standard MoE approaches. Benchmarks reportedly compare against Gemini 3.1 Pro, GPT-5.5, and Claude Opus 4.6-4.8, though specific scores were truncated. Integrated with Claude Code, OpenClaw, and Hermes harnesses for agentic workflows. Too early for definitive quality ranking but the scale and MIT license make it a significant addition to the open-weight frontier.

## Notes
- Deeply integrated with mainstream harnesses (Claude Code, OpenClaw, Hermes)
- Custom architecture (`LongcatCausalLM`) — not a standard Llama/Qwen derivative
- FP8 and INT8 variants available
- 3-bit MLX quantization available for Apple Silicon
