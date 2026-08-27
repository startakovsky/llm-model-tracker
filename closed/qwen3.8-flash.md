---
model: Qwen3.8 Flash
organization: Alibaba
license: qwen3.8-max
release_date: 2026-08-26
last_updated: 2026-08-27
sources:
  - https://openrouter.ai/qwen/qwen3.8-flash
---

# Qwen3.8 Flash

## Overview
- **Org:** Alibaba (Qwen)
- **License:** Qwen3.8 Community License (qwen3.8-max)
- **Category:** Frontier
- **Context length:** 1,000,000 (1M)
- **Released:** 2026-08-26
- **OpenRouter ID:** `qwen/qwen3.8-flash`

## Architecture
- Production **managed** tier of the Qwen3.8 line, built on the **Qwen4 architecture**
- 1M context by default, built-in tools
- Closed API (managed); the open-weight research sibling is **Qwen3.8-Flash-Next**

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (qwen/qwen3.8-flash) | $0.15 | $0.47 | 1,000,000 |

Undercuts Kimi K3 ($3/$15) and most frontier closed APIs by a wide margin at this capability tier.

## Benchmarks
- Production counterpart to Qwen3.8-Flash-Next, whose open pre/post-training scores landed strong agentic results (Agentic #13/138, ~91st pct; Inst-Following #10/42; SWE-bench Pro 62.5, GPQA-D 91.7 on the Next weights).
- Positioned as a low-cost, high-efficiency agentic/long-horizon model.

## Self-Hosting
- Not self-hostable — closed managed API only.
- Open alternative: **Qwen3.8-Flash-Next** (research preview weights on HuggingFace, Qwen Community License).

## Quality Assessment
Qwen3.8 Flash is the cheap production API on the Qwen4 architecture. At $0.15/$0.47/M it is one of the least expensive large-context (1M) agentic models available through OpenRouter, carrying the same architecture family as the open Flash-Next preview. Quality score 74 reflects a low-cost workhorse class rather than top-frontier capability.