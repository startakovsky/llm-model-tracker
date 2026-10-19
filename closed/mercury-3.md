---
model: Mercury 3
organization: Inception (Inception Labs)
license: Proprietary
release_date: 2026-10-16
last_updated: 2026-10-19
sources:
  - https://openrouter.ai/inception/mercury-3
  - https://www.inceptionlabs.ai/
---

# Mercury 3

Released Oct 16, 2026 — third generation of Inception's diffusion-based LLM line (after Mercury 2.5, Sep 2026). Keeps the ultra-fast non-autoregressive architecture with a big context jump to 1M tokens.

## Architecture
- **Type:** Diffusion-based language model (not autoregressive); iterative denoising
- **Context length:** 1,048,576 (1M)
- **Positioning:** ultra-low-latency reasoning for real-time agents, voice, subagent routing/compaction

## API Providers
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (inception/mercury-3) | $0.10 | $0.35 | 1,048,576 |

## Quality Assessment
Same niche as Mercury 2.5: not a frontier-reasoning competitor on raw benchmarks, but the latency/quality tradeoff for real-time or high-volume routing workloads. At $0.10/$0.35 it is cheap enough to sit in front of pricier frontier models as a compaction/routing layer. Quality score 78 — modest bump over Mercury 2.5 (72), reflecting 1M ctx and a generation of diffusion training gains.

## Notes
- Diffusion LLMs remain an active research area; Google's DiffusionGemma is the main open competing approach
- No downloadable weights (proprietary, API only)
- API launched at roughly half the price of Mercury 2's original $0.25/$0.75, but above the promo-level $0.04/$0.15 Mercury 2.5 pricing