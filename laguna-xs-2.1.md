---
model: Laguna XS 2.1
organization: Poolside
license: OpenMDW-1.1
release_date: 2026-07-02
last_updated: 2026-07-08
sources:
  - https://huggingface.co/poolside/Laguna-XS-2.1
  - https://openrouter.ai/poolside/laguna-xs-2.1
---

# Laguna XS 2.1

## Architecture
- **Total params:** 33B (MoE)
- **Active params per token:** 3B (8 of 256 experts)
- **Context length:** 262,144
- **Model type:** laguna (LagunaForCausalLM)
- **Layers:** 40, hidden_size=2048, vocab_size=100,352
- **Architecture:** Mixed SWA (Sliding Window Attention) and global attention in 3:1 ratio, sigmoid gating with per-layer rotary scales, FP8 KV cache
- **Native reasoning:** Interleaved thinking between tool calls (toggleable per-request)

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M (imatrix) | ~18GB | 24GB+ | Official: poolside/Laguna-XS-2.1-GGUF |
| Q8_0 | ~33GB | 48GB+ | Higher precision |
| BF16 | ~66GB | 72GB+ | Full precision |

Source: https://huggingface.co/poolside/Laguna-XS-2.1-GGUF

**Note:** Requires building llama.cpp from PR #25165 (not yet merged to mainline as of July 8, 2026)

### Ollama (easiest local option)
```bash
ollama run laguna-xs-2.1          # default — Q4_K_M (imatrix)
ollama run laguna-xs-2.1:q8_0     # higher precision
ollama run laguna-xs-2.1:bf16     # full precision
```
Runs on Mac with 36 GB RAM. MLX support available.

### FP8/NVFP4 (vLLM, SGLang, TRT-LLM)
- vLLM 0.21.0+ supported
- SGLang supported (sgl-project/sglang#24204)
- TRT-LLM v1.3.0rc16+ supported
- FP8, NVFP4, and INT4 quantized variants available in collection

### Speculative decoding (DFlash)
- DFlash speculator: 5-layer Llama-style draft model, proposes 7 tokens/step at ~70% acceptance on coding tasks
- vLLM support in progress (vllm-project/vllm#46853)
- SGLang support added (sgl-project/sglang#29446)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (poolside/laguna-xs-2.1) | $0.06 | $0.12 | 262,144 | 15x cheaper prompt than GLM-5.2 |
| OpenRouter (free tier) | $0.00 | $0.00 | 262,144 | Free inference for limited time |

## Quality Benchmarks
- SWE-bench Verified: 70.9%
- SWE-bench Multilingual: 63.1%
- SWE-bench Pro: 47.6%
- Terminal-Bench 2.0: 37.5%
- Artificial Analysis Coding Index: N/A (33.4 for comparison model North Mini Code)

## Quality Assessment
Laguna XS 2.1 is a remarkably efficient coding agent for its size. At only 33B total / 3B active, it achieves 70.9% SWE-bench Verified — ~86% of GLM-5.2's 82.8% — while being small enough to run on a Mac with 36GB RAM. Terminal-Bench 2.0 at 37.5% is well below GLM-5.2's 81.0, reflecting the size limitation for complex agentic terminal tasks. The model excels at coding-focused workflows with native reasoning, interleaved thinking, and excellent local deployment story (Ollama, llama.cpp, MLX).

**Agentic verdict:** Not a GLM-5.2 replacement for full agentic workflows. Terminal-Bench 37.5% is less than half of GLM-5.2's 81.0. However, for coding-specific tasks (SWE-bench Verified 70.9% vs 82.8%), it delivers ~86% of GLM-5.2's quality at 15x lower API cost ($0.06+$0.12/M vs $0.90+$2.86/M) and can run locally on 36GB RAM. Best suited as a local coding assistant or cost-effective coding API, not a general-purpose agent.

## Notes
- 3,385 downloads, 74 likes on HuggingFace (new release, growing)
- Upgraded from Laguna XS.2 with +5.4% on SWE-bench Multilingual
- Launch-day support in vLLM, SGLang, Transformers, llama.cpp, TRT-LLM
- Companion model: Laguna M.1 (225B, larger)
- Poolside also provides `pool` — a terminal-based coding agent
- Free inference available on OpenRouter for limited time
