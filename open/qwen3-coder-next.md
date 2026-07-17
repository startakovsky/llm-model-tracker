# Qwen3 Coder Next — Alibaba

| Field | Value |
|---|---|
| **Org** | Alibaba (Qwen) |
| **OpenRouter ID** | `qwen/qwen3-coder-next` |
| **License** | Apache 2.0 |
| **Release date** | 2026-02-02 |
| **Pricing** | $0.11 / $0.80 per M tokens (OpenRouter) |
| **Context** | 262,144 (256K) |
| **Category** | Self-hostable (open) |
| **Quality score** | 70 |

## Architecture

Qwen3-Coder-Next is an open-weight causal language model optimized for coding agents and local development workflows:

- **80B total / 3B active** parameters — sparse Mixture-of-Experts (MoE) design
- Only 3B parameters activated per forward pass — highly efficient inference
- 262K token context window
- Apache 2.0 licensed — fully open weights
- Designed for interactive development sessions and autonomous coding workflows

## Quality Assessment

Qwen3-Coder-Next targets the sweet spot between capability and self-hostability. With only 3B active parameters out of 80B, it can run on modest hardware (single consumer GPU at quantized precision) while leveraging the full 80B knowledge base through MoE routing.

**Cost/quality framing:** At $0.11/$0.80 per million tokens via OpenRouter, it is cheaper than Qwen3-Coder-30B-A3B ($0.07/$0.27) on prompt but more expensive on completion. The larger 80B total parameter count gives it broader knowledge coverage. Comparable to GPT-OSS-120B ($0.037/$0.17) on capability but at higher cost — the trade-off is better coding-specific optimization.

**Self-hosting:** At 80B/3B MoE, quantized GGUF versions should fit in ~40-50GB, making it accessible on a single 48GB GPU (e.g., RTX 6000 Ada) or 64GB RAM with CPU offload via KTransformers.

**Verdict:** A strong open coding model for self-hosting. The MoE design makes it efficient enough for local development workflows while maintaining coding-specific optimization. Good alternative to GPT-OSS-120B for users who want more coding focus.
