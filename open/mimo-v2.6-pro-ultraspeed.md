---
model: MiMo-V2.6-Pro UltraSpeed
organization: Xiaomi
license: MIT
release_date: 2026-09-21
last_updated: 2026-09-22
openrouter_id: xiaomi/mimo-v2.6-pro-ultraspeed
category: Frontier
---

# MiMo-V2.6-Pro UltraSpeed

UltraSpeed tier of Xiaomi's MiMo-V2.6-Pro flagship, released Sep 21, 2026.

## Architecture
- **Context length:** 1,048,576 (1M)
- **Modality:** Omni-modal (multi-modality reasoning)
- **Architecture type:** Flagship reasoning model, UltraSpeed (speculative-decoding) serving

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (xiaomi/mimo-v2.6-pro-ultraspeed) | $4.35 | $8.70 | 1,048,576 |

## Self-Hosting
- Same open MIT weights as the MiMo-V2.6 series; UltraSpeed refers to the accelerated serving mode rather than a separate weight set.

## Quality Assessment
The premium low-latency serving of MiMo-V2.6-Pro, delivering up to ~20× faster generation via speculative decoding. Carries a ~10× price premium over the base Pro tier ($4.35/$8.70 vs $0.435/$0.87) for the latency/capacity boost. Aimed at interactive and latency-sensitive agentic workloads that tolerate the higher per-token cost.

## Notes
- Open-sourced MIT (HF).
- Use base MiMo-V2.6-Pro for cost-efficient throughput; UltraSpeed only when latency justifies the ~10× premium.