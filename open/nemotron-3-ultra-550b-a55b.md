---
model: NVIDIA Nemotron 3 Ultra
organization: NVIDIA
license: OpenMDW-1.1 (commercial use allowed)
release_date: 2026-06-04
last_updated: 2026-07-08
sources:
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4
  - https://openrouter.ai/api/v1/models
---

# NVIDIA Nemotron 3 Ultra

## Architecture
- **Total params:** 550B (MoE)
- **Active params per token:** ~55B
- **Sparsity:** ~90%
- **Context length:** 1,000,000
- **Architecture:** Hybrid Mamba-Transformer MoE (Nemotron-H) — interleaves Mamba-2 state-space layers, MoE layers, and attention layers
- **Multi-Token Prediction (MTP):** Yes — drafts multiple tokens per forward pass
- **LatentMoE:** Hardware-aware expert design
- **Training precision:** NVFP4 pre-training recipe (native 4-bit floating point)
- **Pre-training data cutoff:** September 2025; post-training cutoff May 2026
- **Reasoning controls:** Granular reasoning-budget (operators can dial "thinking" up/down at inference time)

## Self-Hosting

### NVFP4 (vLLM on Blackwell GPUs)
- Ships pre-quantized to NVFP4 (native 4-bit for Blackwell)
- 5.03 bits-per-element: NVFP4 routed experts + FP8 shared experts + FP8 Mamba linears + BF16 attention
- On Hopper (H100/H200): falls back to W4A16 (no FP4 tensor cores)
- ~5x higher inference throughput than GLM-5.1, Kimi-K2.6, Qwen-3.5 (NVIDIA-reported, 8K input / 64K output shape)

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~1.1TB | 1.1TB+ | Not practical |
| NVFP4 (official) | ~345GB | 384GB+ | Native on Blackwell, W4A16 fallback on Hopper |

No community GGUF quants yet. The NVFP4 format is NVIDIA-specific; community Q4_K_M GGUFs may emerge.

### Other engines
- **build.nvidia.com:** NVIDIA's own hosted inference
- **vLLM:** Officially supported with NVFP4 on Blackwell
- **KTransformers:** Not yet confirmed

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nvidia/nemotron-3-ultra-550b-a55b) | $0.50 | $2.20 | 1,000,000 | Competitive with GLM-5.2 |
| OpenRouter (free tier) | $0.00 | $0.00 | 1,000,000 | Free tier available |
| build.nvidia.com | TBD | TBD | 1M | NVIDIA's hosted endpoint |

## Quality Assessment

Nemotron 3 Ultra is the largest and most capable open-weight model from a U.S. lab. Key benchmarks:

- **Artificial Analysis Intelligence Index:** 47.7 (NVFP4) / 48.2 (BF16) — top U.S. open-weight, but 6 points behind Kimi K2.6 (53.9)
- **SWE-bench Verified:** 65–70.4% (across several scaffolds)
- **PinchBench:** 90.0
- **ProfBench Search:** 56.0
- **Throughput:** 5.9x / 4.8x / 1.6x vs GLM-5.1 / Kimi-K2.6 / Qwen-3.5 (NVIDIA-reported)

**Verdict:** Nemotron 3 Ultra is a solid frontier-tier model that wins on U.S. open-weight quality and inference throughput (on Blackwell), but trails Chinese leaders on raw intelligence (AA index 48 vs 54 for Kimi K2.6). Against GLM-5.2, it's roughly comparable in SWE-bench (65-70% vs 82.8%) — meaning GLM-5.2 is notably ahead on coding. The NVFP4 native quantization is the key differentiator: if you have Blackwell GPUs, this is the cheapest frontier model to serve. The OpenMDW-1.1 license is clean for commercial use. The hybrid Mamba-Transformer architecture is technically interesting for long-context efficiency.

**Agentic verdict:** Nemotron 3 Ultra is a decent but not top-tier agentic model. With SWE-bench Verified at 65-70% (vs GLM-5.2's 82.8%) and no Terminal-Bench score published, it trails GLM-5.2 meaningfully on agentic coding. The 1M context and reasoning-budget controls are useful for agent workflows, and NVIDIA's agentic positioning (PinchBench 90.0) suggests competent tool-use. At $0.50+$2.20/M on OpenRouter, it's cheaper than GLM-5.2 ($0.90+$2.86/M) but not enough cheaper to justify the quality gap for serious agentic work. Best use case: Blackwell-equipped self-hosting where NVFP4 throughput is the priority, or as a cheaper alternative for less demanding agent tasks.

## Sources
- Primary: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4
- Validation: https://aiweekly.co/alerts/nvidia-ships-nemotron-3-ultra-a-550b-open-moe-for-agents
- Analysis: https://tech-insider.org/ca/nvidia-nemotron-3-ultra-2026/
