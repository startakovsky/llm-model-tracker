---
model: DeepSeek V4 Flash 0731
organization: DeepSeek AI
license: MIT
release_date: 2026-07-31
last_updated: 2026-08-02
sources:
  - https://openrouter.ai/deepseek/deepseek-v4-flash-0731
---

# DeepSeek V4 Flash 0731

A re-post-trained revision of DeepSeek V4 Flash, dated July 31, 2026. Same architecture as the base V4 Flash but offered at the original (non-surge) price point.

## Architecture
- **Total params:** 284B (MoE)
- **Active params per token:** 13B
- **Context length:** 1,048,576
- **Architecture:** DeepSeek V4 with Compressed Sparse Attention (CSA) & Heavily Compressed Attention (HCA) — compresses KV cache for efficient long-context
- **Description (OpenRouter):** sparse mixture-of-experts model suited for coding, reasoning, and agent workflows

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4-flash-0731) | $0.09 | $0.18 | 1,048,576 | Non-surge pricing; cheaper than base ID ($0.14/$0.28) |
| OpenRouter (~deepseek/deepseek-v4-flash-latest) | $0.09 | $0.18 | 1,048,576 | Alias that redirects to the latest V4 Flash (currently 0731) |

## Quality Assessment
Same model family as DeepSeek V4 Flash. Coding average ~72.2 (benchlm.ai); roughly 85-90% of GLM-5.2's coding quality at ~1/3 the API cost ($0.09+$0.18/M vs GLM-5.2's $0.28+$0.89/M). Strong on logical reasoning and coding; weaker on agentic tasks. For cost-conscious workflows this remains the best value frontier-tier model available. The 1M context window matches GLM-5.2.

## Notes
- The base ID `deepseek/deepseek-v4-flash` remains on OpenRouter at surge pricing ($0.14/$0.28) since Jul 26.
- The 0731 snapshot restores the original $0.09/$0.18 pricing.
- Weights on HuggingFace: deepseek-ai/DeepSeek-V4-Flash (same family). Unsloth GGUF quants available.
