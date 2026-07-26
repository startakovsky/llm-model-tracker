---
model: North Mini Code
organization: Cohere / Cohere Labs
license: Apache 2.0
release_date: 2026-06-17
last_updated: 2026-07-08
sources:
  - https://huggingface.co/CohereLabs/North-Mini-Code-1.0
  - https://cohere.com/blog/north-mini-code
---

# North Mini Code

## Architecture
- **Total params:** 30B (MoE)
- **Active params per token:** 3B (8 of 128 experts)
- **Context length:** 256,000 (64K max output)
- **Model type:** cohere2_moe (Cohere2MoeForCausalLM)
- **Layers:** 49 (1 dense + 48 sparse), hidden_size=2048, vocab_size=262,144
- **Architecture:** Decoder-only, interleaved sliding-window attention (RoPE) and global attention (no positional embeddings) in 3:1 ratio, SwiGLU activation, sigmoid router
- **Training:** Two-stage cascaded SFT followed by RLVR (reinforcement learning with verifiable rewards) focused on agentic coding

## Self-Hosting

### GGUF (llama.cpp)
- No GGUF quants available yet (0 GGUF files)

### FP8/FP4 (vLLM on GPU)
- Available in BF16, FP8, and W4A16 on HuggingFace
- Minimum: 1× H100 @ FP8, or 1× H100 @ FP4
- vLLM requires main branch (not yet in stable release)
- Also requires Cohere's `melody` library for accurate response parsing

### Other engines
- OpenCode integration (recommended coding agent)
- Cohere Model Vault (managed inference)
- HuggingFace Space (try before download)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (cohere/north-mini-code:free) | $0.00 | $0.00 | 256,000 | Free tier available |
| Cohere API | TBD | TBD | 256K | Official hosting |

## Quality Benchmarks
- SWE-bench Verified: 67.6%
- SWE-bench Pro: 40.2%
- Terminal-Bench v2: 36.0%
- Terminal-Bench Hard: (benchmarked, using Terminus-2 harness)
- SciCode: (benchmarked)
- LiveCodeBench v6: (benchmarked)
- Artificial Analysis Coding Index: 33.4

## Quality Assessment
North Mini Code is Cohere's first agentic coding model, purpose-built for software engineering with terminal and tool-use capabilities. At 30B/3B active, it's in the same weight class as Laguna XS 2.1 and Qwen3-Coder-30B. SWE-bench Verified at 67.6% is ~82% of GLM-5.2's 82.8%. Terminal-Bench v2 at 36.0% is well below GLM-5.2's 81.0. The model shines in its size-to-capability ratio — it's specifically trained with RLVR for agentic coding, supports interleaved thinking, and is designed for sovereign/local deployment under Apache 2.0.

**Agentic verdict:** Not a GLM-5.2 replacement. Terminal-Bench 36.0% is less than half of GLM-5.2's 81.0, and SWE-bench Verified 67.6% is ~82% of GLM-5.2's 82.8%. However, as a local coding agent that runs on a single H100, it's a strong sovereign option. The Apache 2.0 license and Cohere's sovereign AI mission make it attractive for on-premise deployments. Best for: local coding assistant, code review, sub-agent orchestration. Not suitable for: complex multi-step agentic workflows requiring GLM-5.2-level reasoning.

## Notes
- 37,216 downloads, 514 likes on HuggingFace
- First model in Cohere's "North" family
- Apache 2.0 license — fully open, including commercial use
- Supports interleaved thinking (preserve thinking in message history for best results)
- 2.8x higher output throughput than Devstral Small 2 in internal tests
- 30% advantage in inter-token latency vs Devstral Small 2
- Recommended sampling: temperature=1.0, top_p=0.95
