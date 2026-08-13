---
model: Qwen3.8 2.4T A95B
organization: Alibaba (Qwen Team)
license: qwen3.8-max
release_date: 2026-08
last_updated: 2026-08-13
sources:
  - https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - https://openrouter.ai/qwen/qwen3.8-2.4t-a95b
  - https://vllm.ai/blog/2026-08-12-qwen3.8
---

# Qwen3.8 2.4T A95B

Qwen's largest-ever open-weight release and the first time a Qwen-Max-class model has been pushed to open weights. Built on the Qwen3.5 architectural foundation with substantial gains across coding, professional work, research, and long-horizon agentic tasks. 2.4T total params / 95B active — the largest open MoE on HF.

## Architecture
- Total params: 2.4T (MoE)
- Active params per token: 95B
- Architecture: Qwen3_5 MoeForCausalLM (hybrid linear/full attention, attn_output_gate)
- Config: head_dim 256, hidden_size 8192, full-attention layer every 4th layer
- Context length: 1,000,000 (1M) on OpenRouter
- Training: pre-trained + post-trained (post-trained transformers weights published)
- License: `qwen3.8-max` (permissive-looking Qwen custom license; see LICENSE)
- Downloads: 1,012 | Likes: 712 on HF as of Aug 13

Note: Qwen3.8-2.4T-A95B here is the open-weight post-trained model (thinking mode). **Qwen3.8-Max** is Alibaba's closed cloud version built on these weights, adding vision input, non-thinking support, 1M ctx default, and official built-in tools.

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.8-2.4t-a95b) | $2.00 | $6.00 | 1M | New endpoint, aligns with Qwen3.8 Max pricing |

## Quality Assessment
Qwen3.8 is a Qwen-Max-class model brought to open release, so it targets the frontier rather than cost-efficient local deployment. On agentic evaluations it lands near the top tier — Artificial Analysis puts Qwen3.8 Max in competition with Grok 4.6 and Claude Fable 5 on GDPval-style agentic work, and it scored τ³-Banking 51.3% (top score alongside Grok 4.6). Terminal-Bench v2.1 and SWE-bench are frontier-class for an open model. Cost: at $2/$6 it undercuts the cloud frontier (Opus 5 $5/$25, GPT-5.6 Sol $5/$30) while remaining a closed-price Amazon for open-weight fans — you can fully self-host the 2.4T MoE (needs a datacenter-grade cluster, not consumer hardware).

**Agentic verdict:** Qwen3.8-2.4T-A95B is the most capable open-weight agentic model available, effectively "Qwen3.8 Max at open weights." ~95% of GLM-5.2's capability class but at ~4x the price-tag for self-hosting (2.4T params demand 2× GB200-class nodes). Best choice when you want a frontier-class open stack on managed GPU.

## Sources
- Primary: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B (weights, license, download stats)
- Validation: https://vllm.ai/blog/2026-08-12-qwen3.8 (Day-0 vLLM support)
- Hardware: https://forums.developer.nvidia.com (GB300 NVL72 serving guide)
- Benchmarks: Artificial Analysis, QwenWebBench (Qwen3.8 family)