---
model: Qwen3-Next-80B-A3B-Thinking
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026-06
last_updated: 2026-07-20
sources:
  - https://openrouter.ai/qwen/qwen3-next-80b-a3b-thinking
---

# Qwen3-Next-80B-A3B-Thinking

The **thinking** variant of Qwen3-Next-80B-A3B — an 80B-total / 3B-active MoE from the Qwen3-Next line, tuned for extended reasoning. Open weights (Apache 2.0). A good self-hostable reasoning model that fits on a single high-memory GPU.

## Architecture
- **Total params:** ~80B (MoE)
- **Active params per token:** ~3B
- **Context length:** 262,144
- Reasoning-optimized training (chain-of-thought before answer)

## Self-Hosting
MoE means large total weight but low per-token compute; quantized, the active-expert throughput is high.
| Quant | Est. Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | ~45GB | 64GB+ | Reasonable on a 48-64GB GPU + RAM |
| Q3_K_M | ~35GB | 48GB+ | |
| Q2_K | ~24GB | 32GB+ | Budget |

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3-next-80b-a3b-thinking) | $0.0975 | $0.78 | 262,144 | Negligible prompt tick from $0.098 on Jul 20 (rounding) |

## Quality Assessment
A capable mid-tier reasoning model at low cost (~$0.10/$0.78). The 80B/3B MoE keeps inference cheap while thinking mode lifts reasoning quality above the non-thinking Instruct sibling. Roughly 74% of GLM-5.2 quality — best value when you need extended reasoning without frontier pricing.

## Notes
- Companion to Qwen3-Next-80B-A3B-Instruct ($0.10/$1.10)
- Prompt price effectively unchanged ($0.098 → $0.0975) on Jul 20, 2026
