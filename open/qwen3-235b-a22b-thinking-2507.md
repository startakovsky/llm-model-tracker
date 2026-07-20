---
model: Qwen3-235B-A22B-Thinking-2507
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026-07
last_updated: 2026-07-20
sources:
  - https://openrouter.ai/qwen/qwen3-235b-a22b-thinking-2507
  - https://huggingface.co/Qwen
---

# Qwen3-235B-A22B-Thinking (2507)

The **thinking** variant of the Qwen3-235B-A22B July 2026 release. Same 235B/22B Mixture-of-Experts backbone as the Instruct model, but tuned for extended chain-of-thought reasoning before answering. Open weights (Apache 2.0).

## Architecture
- **Total params:** ~234B (MoE)
- **Active params per token:** ~22B
- **Context length:** 262,144
- Same expert config as the Instruct sibling (128 experts), with reasoning-mode training

## Self-Hosting
Same footprint as the Instruct variant:
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| Q4_K_M | ~142GB | 160GB+ | bartowski GGUF |
| IQ4_XS | ~126GB | 144GB+ | Smaller 4-bit |
| Q3_K_M | ~108GB | 128GB+ | |
| Q2_K | ~73GB | 96GB+ | |

FP8 (~235GB) needs 4x H100 or 3x RTX PRO 6000.

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3-235b-a22b-thinking-2507) | $0.30 | $3.00 | 262,144 | Price doubled from $0.15/$1.495 on Jul 20, 2026 |

## Quality Benchmarks
- Optimized for complex multi-step reasoning; stronger than the Instruct variant on math/STEM and agentic planning
- Open weights enable local reasoning control (budget tuning)

## Quality Assessment
The Thinking variant trades higher latency and output cost for materially better reasoning. At $0.30/$3.00/M it is now ~3x the blended cost of the Instruct sibling ($0.09/$0.10) — use it when the reasoning uplift justifies the price, otherwise prefer the Instruct model. Roughly 82% of GLM-5.2 quality on reasoning tasks at a fraction of GLM-5.2's (post-hike) cost.

## Notes
- Companion to Qwen3-235B-A22B-Instruct-2507 (cheapest capable model at $0.09/$0.10)
- Price doubled to $0.30/$3.00 on July 20, 2026 (was $0.15/$1.495)
