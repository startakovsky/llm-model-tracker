---
model: Tencent Hy3
organization: Tencent (Hy Team / Hunyuan)
license: Apache-2.0
release_date: 2026-07-06
last_updated: 2026-07-08
sources:
  - https://huggingface.co/tencent/Hy3
  - https://openrouter.ai/api/v1/models
  - https://github.com/Tencent-Hunyuan/Hy3
---

# Tencent Hy3

## Architecture
- **Total params:** 295B (MoE) + 3.8B MTP layer
- **Active params per token:** 21B
- **Context length:** 256K
- **Architecture:** MoE with 192 experts, top-8 activated, 1 shared expert
- **Attention:** GQA (64 heads, 8 KV heads, head dim 128), 80 layers
- **MTP (Multi-Token Prediction):** 1 layer, speculative decoding via EAGLE/vLLM
- **Supported precisions:** BF16 (native), FP8 (official quantized release available)
- **Reasoning mode:** Configurable `reasoning_effort` — `no_think` (direct), `low`, `high` (chain-of-thought)

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~590GB | 600GB+ | Not practical |
| Q4_K_M (est) | ~170GB | 192GB+ | Not yet available — no GGUF releases as of 2026-07-06 |
| FP8 (official) | ~295GB | 320GB+ | `tencent/Hy3-FP8` on HuggingFace, for vLLM/SGLang |

No community GGUF quants available yet (model released today). Expect unsloth/unsloth-community GGUFs within days.

### FP8 (vLLM/SGLang on GPU)
- Official FP8 weights: `tencent/Hy3-FP8`
- Recommended hardware: 8x H20-3e or equivalent (vLLM TP=8)
- MTP speculative decoding supported (2 speculative tokens) for ~2x throughput
- vLLM recipe: `vllm serve tencent/Hy3 --tensor-parallel-size 8 --speculative-config.method mtp --tool-call-parser hy_v3 --reasoning-parser hy_v3 --enable-auto-tool-choice`
- SGLang recipe also available with EAGLE speculative decoding

### Other engines
- **DGX Spark (2x GB10):** NVIDIA forum users note 295B-A21B is a good fit for 2x Spark configs (288GB unified memory). No NVFP4 release yet — watch for community NVFP4 quants.
- **KTransformers / hybrid CPU-GPU:** Not yet confirmed, but 21B active params makes it a strong candidate for KTransformers-style offloading once supported.

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (tencent/hy3) | $0.20 | $0.80 | 256K | Cheapest frontier-tier agent model (price updated 2026-07-07, was $0.14+$0.58/M) |
| OpenRouter (tencent/hy3:free) | $0 | $0 | 256K | Free tier available |
| OpenRouter (tencent/hy3-preview) | $0.063 | $0.21 | 256K | Older preview, cheaper but weaker |

## Quality Assessment

Hy3 is a strong mid-tier frontier model that sits between GLM-5.1 and GLM-5.2 in capability, at roughly 1/6th the cost of GLM-5.2. Key benchmarks:

- **Terminal-Bench 2.1:** 71.7 (vs GLM-5.2's 81.0 — ~88% of GLM-5.2's agentic score)
- **DeepSWE:** 28.0 (real-world agentic coding, vs GLM-5.2 leading)
- **SWE-bench Verified:** Accuracy variance <4% across scaffoldings (CodeBuddy, Cline, KiloCode) — strong tool-use stability
- **Blind expert eval:** 2.67/4 vs GLM-5.1's 2.51/4 (270 experts, real work tasks)
- **Hallucination rate:** 5.4% (down from 12.5% in preview) — strong anti-hallucination
- **Multi-turn coherence:** Issue rate 7.9% (down from 17.4%) — good long-conversation retention

**Verdict:** Hy3 delivers ~85-88% of GLM-5.2's coding and agentic capability at ~1/6th the API cost ($0.14+$0.58/M vs $0.91+$2.86/M). For cost-sensitive agentic workflows where you don't need the absolute frontier, Hy3 is the best value proposition in the tracker. It is the cheapest model with a Terminal-Bench score above 70.

**Agentic verdict:** Hy3 is a viable cost-saving alternative to GLM-5.2 for agentic tool-use workflows, but not a full replacement. At 71.7 Terminal-Bench (vs 81.0 for GLM-5.2), it handles tool-calling, multi-step reasoning, and agent scaffolding well, with notably stable performance across different frameworks (<4% variance). For Hermes Agent workloads, it would handle most tasks but may struggle on the most complex 10+ tool-call chains where GLM-5.2 maintains coherence. Best use case: high-volume agentic work where 88% of frontier quality at 1/6th cost is the right tradeoff.

## Sources
- Primary: https://huggingface.co/tencent/Hy3
- Validation: https://forums.developer.nvidia.com/t/new-2x-spark-king-tencent-hy3-just-released/375718
- OpenRouter: https://openrouter.ai/tencent/hy3
- GitHub: https://github.com/Tencent-Hunyuan/Hy3
