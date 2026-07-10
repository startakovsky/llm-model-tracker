---
model: Ring-2.6-1T
organization: inclusionAI
license: MIT
release_date: 2026-05-14
last_updated: 2026-07-08
sources:
  - https://huggingface.co/inclusionAI/Ring-2.6-1T
  - https://openrouter.ai/inclusionai/ring-2.6-1t
---

# Ring-2.6-1T

## Architecture
- **Total params:** ~1T (MoE, BailingMoeV2_5 hybrid architecture)
- **Active params per token:** 63B
- **Context length:** 262,144 (131,072 max position embeddings, 66K max output)
- **Model type:** bailing_hybrid
- **Layers:** 80, hidden_size=8192, 256 experts, top-8 routing
- **Quantization:** shipped in compressed-tensors format (pre-quantized)

## Self-Hosting

### GGUF (llama.cpp)
- No GGUF quants available yet
- Model ships pre-quantized in compressed-tensors format

### FP8/FP4 (vLLM on GPU)
- Full BF16: ~2TB (not practical)
- Shipped format (compressed-tensors): ~625GB+ estimated
- Supports vLLM and SGLang natively

### Other engines
- vLLM: `vllm serve "inclusionAI/Ring-2.6-1T"`
- SGLang supported
- Docker Model Runner supported

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (inclusionai/ring-2.6-1t) | $0.075 | $0.625 | 262,144 | 12x cheaper prompt than GLM-5.2 |
| Novita | $0.075 | $0.625 | 262K | 100% uptime |

## Quality Benchmarks
- Artificial Analysis Intelligence Index: 30.6 (56th of 151)
- Artificial Analysis Coding Index: 42.8
- GPQA Diamond: 86% (88.27 xhigh)
- AIME 2026: 95.83 (xhigh)
- SWE-bench Verified: 74
- Tau²-Bench (agentic): 92%
- PinchBench: 87.60 (high config)
- ClawEval: 63.82
- ARC-AGI-V2: 66.18 (xhigh)

## Quality Assessment
Ring-2.6-1T is a trillion-parameter reasoning model purpose-built for agentic workflows. Its standout: Tau²-Bench at 92% (agentic) is exceptional, and PinchBench at 87.60 beats GPT-5.4 xHigh. However, SWE-bench Verified at 74 is notably below GLM-5.2's 82.8 (~89% as good). GPQA Diamond at 86% and AIME 2026 at 95.83 show strong reasoning. The Intelligence Index of 30.6 ranks 56th — mid-tier overall, but the agentic-specific benchmarks are much stronger than the general index suggests.

**Agentic verdict:** Promising but not yet a GLM-5.2 replacement. Tau²-Bench 92% is outstanding for agentic tool-use, but SWE-bench Verified 74 vs GLM-5.2's 82.8 means coding agent performance trails. At $0.075+$0.625/M (12x cheaper prompt, 4.6x cheaper completion), it's a compelling cost/quality option for agentic workflows that emphasize tool-calling over heavy coding. The configurable reasoning effort (high/xhigh) is a nice production feature.

## Notes
- 826 downloads, 104 likes on HuggingFace (low traction — niche model)
- Trained with Async RL + IcePop algorithm for trillion-parameter stability
- Two reasoning effort levels: "high" (fast, production) and "xhigh" (deep reasoning)
- Companion model Ling-2.6-1T also available
