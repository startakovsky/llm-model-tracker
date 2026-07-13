---
model: Qwen3-235B-A22B-Instruct-2507
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026-07
last_updated: 2026-07-08
---

# Qwen3-235B-A22B-Instruct

## Architecture
- **Total params:** ~234B (MoE)
- **Active params per token:** ~7B (8 of 128 experts)
- **Context length:** 262,144
- **Layers:** 94, hidden_size=4096, 128 experts, moe_intermediate_size=1536

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | 142.6GB | 160GB+ | bartowski GGUF |
| IQ4_XS | 125.9GB | 144GB+ | Smaller 4-bit |
| Q3_K_M | ~108GB | 128GB+ | |
| Q2_K | ~73GB | 96GB+ | |

Source: https://huggingface.co/bartowski/Qwen_Qwen3-235B-A22B-Instruct-2507-GGUF

### FP8 (vLLM on GPU)
- ~235GB at FP8, needs 4x H100 or 3x RTX PRO 6000
- DynaExq (dynamic expert quantization) can cut to 2x RTX PRO 6000

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3-235b-a22b-instruct-2507) | $0.09 | $0.10 | 262,144 | Cheapest capable model |

## Quality Benchmarks
- Strong reasoning and coding (per community reports)
- 916K downloads on HuggingFace

## Quality Assessment
Qwen3-235B is the cheapest capable model on OpenRouter ($0.09+$0.10/M). Strong reasoning and coding at roughly 80% of GLM-5.2 quality. Good for personal-assistant tasks and tool-calling. The 262K context is sufficient for most coding sessions (not full 1M like GLM-5.2). At this price, it's the best "good enough" daily driver — if it handles your workload, there's no reason to pay 10x more for GLM-5.2.

## Notes
- Qwen3-Coder-30B-A3B-Instruct also available (30B/3B, Q4 ~18GB, $0.07+$0.27/M)
- Qwen3.5-9B available (9B dense, Q4 ~5GB, $0.10+$0.15/M)
- Qwen3-235B has Thinking variant (2507) with extended reasoning
