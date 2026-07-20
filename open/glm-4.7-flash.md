---
model: GLM-4.7-Flash
organization: Z.ai
license: Apache 2.0
release_date: 2026-05
last_updated: 2026-07-20
sources:
  - https://openrouter.ai/z-ai/glm-4.7-flash
---

# GLM-4.7-Flash

The **Flash** (fast, lightweight) tier of Z.ai's GLM-4.7 line. Open weights (Apache 2.0). Optimized for low-latency, high-throughput serving — the cheap, snappy sibling of the mid-tier GLM-4.7.

## Architecture
- **Family:** GLM-4.7 (Z.ai)
- **Tier:** Flash (efficiency-optimized)
- **Context length:** 200,000

## Self-Hosting
Flash tiers are typically smaller-dense or lightly-gated MoE; quantizes well for local use. Confirm exact param count on the HuggingFace model card before speccing hardware.

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (z-ai/glm-4.7-flash) | $0.0605 | $0.40 | 200,000 | Negligible prompt tick from $0.06 on Jul 20 (rounding) |

## Quality Assessment
A cheap, fast Z.ai model for lightweight agentic and assistant tasks where you don't need frontier reasoning. At ~$0.06/$0.40 it's well under GLM-4.7 ($0.40/$1.75) — roughly 68% of GLM-5.2 quality for a fraction of the cost. Good fit for high-volume routing and quick-turnaround tool use.

## Notes
- Part of the GLM-4.7 family (base GLM-4.7 at $0.40/$1.75, 202K ctx)
- Prompt price effectively unchanged ($0.06 → $0.0605) on Jul 20, 2026
