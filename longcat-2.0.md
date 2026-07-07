---
model: Meituan LongCat-2.0
organization: Meituan
license: MIT
release_date: 2026-06-30
last_updated: 2026-07-07
sources:
  - https://huggingface.co/meituan-longcat/LongCat-2.0
  - https://openrouter.ai/api/v1/models
  - https://longcat.ai/blog/longcat-2.0/
---

# Meituan LongCat-2.0

## Architecture
- **Total params:** 1.6T (MoE) + 135B N-gram Embedding module
- **Active params per token:** ~48B (dynamic 33B–56B via zero-computation experts)
- **Context length:** 1,000,000 (native, via LongCat Sparse Attention)
- **Architecture:** ScMoE (shortcut-connected MoE) with zero-computation experts, LongCat Sparse Attention (LSA), N-gram Embedding
- **Attention:** LongCat Sparse Attention — streaming-aware, cross-layer, and hierarchical indexing; evolves DeepSeek Sparse Attention to near-linear complexity
- **Pre-training:** 35T+ tokens on domestic AI ASIC superpods (no NVIDIA chips)
- **Post-training:** MOPD pipeline with multi-teacher online distillation (Agent, Reasoning, Interaction expert groups)
- **Training hardware:** 50,000-card domestic (Chinese) computing cluster — first trillion-parameter model fully trained and served on non-NVIDIA silicon

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~3.2TB | 3.2TB+ | Not practical |
| FP8 (official) | ~1.6TB | 1.7TB+ | Available on HuggingFace |
| Q4_K_M (est) | ~900GB | 1TB+ | Not yet available — expect community GGUFs |

No community GGUF quants available yet (released June 30). Expect unsloth/unsloth-community GGUFs within weeks given MIT license.

### FP8 (vLLM/SGLang on GPU)
- Official FP8 weights available
- Recommended hardware: 16x H20 GPUs (per model card)
- 6D parallelism scheme with prefill-decode disaggregated architecture
- Super kernels and L2-cache weight prefetching for I/O latency hiding

### Other engines
- **KTransformers / hybrid CPU-GPU:** Not yet confirmed, but 48B active params makes it a candidate for KTransformers-style offloading once supported
- **DGX Spark:** Not viable at 1.6T total params without extreme quantization

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter | — | — | — | Not yet listed (was running as codename "Owl Alpha" for 2 months before reveal) |
| Meituan direct | TBD | TBD | 1M | Check longcat.ai for API access |

## Quality Assessment

LongCat-2.0 is Meituan's frontier-scale agentic coding model. Key benchmarks (self-reported by Meituan):

- **SWE-bench Pro:** 59.5 (beats GPT-5.5 at 58.6, Gemini 3.1 Pro at 54.2, Claude Opus 4.6 at 57.3; but trails Claude Opus reference at 69.2)
- **Terminal-Bench 2.1:** 70.8 (vs GLM-5.2's 81.0 — ~87% of GLM-5.2's agentic score)
- **SWE-bench Multilingual:** 77.3 (on par with Claude Opus 4.6 at 77.8)
- **IFEval:** 90.0 (beats Claude Opus reference at 86.0)
- **IMO-AnswerBench:** 81.8 (beats Claude Opus at 75.3)
- **RWSearch:** 78.8 (search agent benchmark)
- **BrowseComp:** 79.9
- **FORTE:** 73.2 (productivity scenario)

**Verdict:** LongCat-2.0 is a strong frontier-tier agentic coding model that edges out GPT-5.5 and Gemini 3.1 Pro on SWE-bench Pro, but trails Claude Opus on hard agentic coding (69.2 vs 59.5 on SWE-bench Pro). Against GLM-5.2, it sits at ~87% of Terminal-Bench performance (70.8 vs 81.0). The 1M native context and MIT license are major advantages. The zero-NVIDIA-chip training is geopolitically significant but doesn't affect model quality. Independent benchmark confirmation is still pending — treat as self-reported.

**Agentic verdict:** LongCat-2.0 is a promising but not yet proven GLM-5.2 replacement for agentic workflows. At 70.8 Terminal-Bench (vs 81.0 for GLM-5.2), it handles tool-calling and agentic coding well, and the 1M context is advantageous for long sessions. However, it's not yet on OpenRouter, so cost comparison is pending. The model was specifically designed for agentic coding (MOPD post-training with Agent expert group), suggesting strong tool-use intent. Best use case: agentic coding workflows where 1M context matters and you can self-host on 16x H20. Watch for OpenRouter listing and independent benchmarks.

## Sources
- Primary: https://huggingface.co/meituan-longcat/LongCat-2.0
- Validation: https://www.marktechpost.com/2026/07/05/meituan-releases-longcat-2-0-a-1-6t-parameter-open-moe-model-with-native-1m-context-and-longcat-sparse-attention/
- Blog: https://longcat.ai/blog/longcat-2.0/
- AIWeekly: https://aiweekly.co/alerts/meituan-open-sources-16t-parameter-longcat-20-moe-model
