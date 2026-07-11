---
model: Nex-N2-Mini
organization: Nex AGI
license: Apache 2.0
release_date: 2026-06-24
last_updated: 2026-07-11
---

# Nex-N2-Mini

## Architecture
- **Context length:** 262,144
- **Modality:** Text + Image → Text
- **Architecture type:** Agentic Mixture-of-Experts

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (nex-agi/nex-n2-mini) | $0.025 | $0.10 | 262,144 |

## Quality Assessment
Nex-N2-Mini is the smaller sibling in Nex AGI's Nex-N2 series (which includes the Nex-N2-Pro, already tracked). Open-source agentic MoE accepting text and image input, built for coding and tool use. At $0.025/$0.10/M, it's one of the cheapest models in the tracker — viable for high-volume, cost-sensitive pipelines. Apache 2.0, ~14K HF downloads, 279 likes. Good for lightweight agentic tasks where cost-per-token matters more than frontier quality.

## Notes
- Smaller sibling of Nex-N2-Pro (397B/17B MoE)
- Ultra-cheap at $0.025/$0.10/M
- Apache 2.0, open weights
- Built for coding, tool use, and agentic workflows
