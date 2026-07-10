---
model: MiniMax M3
organization: MiniMax AI
license: other (custom)
release_date: 2026-05-31
last_updated: 2026-07-08
sources:
  - https://huggingface.co/MiniMaxAI/Minimax-M3
  - https://openrouter.ai/minimax/minimax-m3
---

# MiniMax M3

## Architecture
- **Total params:** ~428B (MoE, MiniMaxM3SparseForConditionalGeneration)
- **Active params per token:** ~23B
- **Context length:** 1,048,576 (1M native)
- **Model type:** minimax_m3_vl (multimodal)
- **Modality:** text+image+video→text (native multimodal from first training step)
- **Architecture:** MiniMax Sparse Attention (MSA) — 9× prefill and 15× decode speedups vs M2 at 1M context

## Self-Hosting

### GGUF (llama.cpp)
- No GGUF quants available yet (0 GGUF files on HuggingFace)

### FP8/FP4 (vLLM on GPU)
- Full BF16: ~856GB (not practical)
- FP8: ~428GB (requires multi-GPU cluster)
- Supports vLLM, SGLang natively

### Other engines
- vLLM: `vllm serve "MiniMaxAI/Minimax-M3"`
- SGLang supported
- Docker Model Runner supported

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (minimax/minimax-m3) | $0.30 | $1.20 | 1,048,576 | 3x cheaper prompt than GLM-5.2 |

## Quality Benchmarks
- SWE-bench Pro: 59.0 (beats GPT-5.5's 58.6)
- SWE-bench Verified: (available on leaderboard, not extracted)
- AgentBrowseComp: 83.5 (from Nex-N2 comparison table)
- GDPval: ~1535-1554 (from Nex-N2 comparison table)
- ClawEval: available (on HF leaderboard)
- Apex Agents: available (on HF leaderboard)

## Quality Assessment
MiniMax M3 is a frontier-tier multimodal model with a 1M context window. Its SWE-bench Pro score of 59.0 narrowly beats GPT-5.5's 58.6, placing it in the frontier coding tier. However, GPT-5.5 outperforms M3 on terminal/command-line tasks per community reports. The MiniMax Sparse Attention (MSA) is a genuine architectural breakthrough — 9× prefill and 15× decode speedups at 1M context make it one of the most efficient long-context models available. At $0.30+$1.20/M, it's 3x cheaper on prompt and 2.4x cheaper on completion vs GLM-5.2.

**Agentic verdict:** Strong on coding benchmarks but not a direct GLM-5.2 replacement for agentic work. SWE-bench Pro 59.0 is competitive, but GLM-5.2's Terminal-Bench 81.0 is the agentic gold standard and M3 hasn't been benchmarked on Terminal-Bench. Native multimodality (text+image+video) is an advantage for multi-modal agentic workflows. The 1M context + MSA efficiency makes it excellent for long-context production deployments. Cost-effective at ~3x cheaper than GLM-5.2.

## Notes
- 233,589 downloads, 1,307 likes on HuggingFace — very popular
- Technical report: arXiv:2606.13392
- Native multimodality from first training step (not bolted on)
- Custom license (not MIT/Apache) — check terms for commercial use
- Used as a comparison baseline in Nex-N2-Pro benchmarks
