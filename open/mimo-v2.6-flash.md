---
model: MiMo-V2.6-Flash
organization: Xiaomi
license: MIT
release_date: 2026-09-21
last_updated: 2026-09-22
openrouter_id: xiaomi/mimo-v2.6-flash
category: Frontier
---

# MiMo-V2.6-Flash

Efficiency-balanced checkpoint of the MiMo-V2.6 series from Xiaomi, released Sep 21, 2026.

## Architecture
- **Context length:** 1,048,576 (1M)
- **Modality:** Omni-modal (multi-modality reasoning)
- **Architecture type:** Efficiency checkpoint (open weights)

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (xiaomi/mimo-v2.6-flash) | $0.14 | $0.28 | 1,048,576 |

## Self-Hosting
- Open weights on HuggingFace: `XiaomiMiMo/MiMo-V2.6-Flash-RL` (MIT, ~336 likes, ~2.6K downloads).
- The Flash-RL checkpoint is built to scale reinforcement-learning pre-training for agentic efficiency.

## Quality Assessment
The cost-efficient tier of the MiMo-V2.6 family. At $0.14/$0.28 with 1M context, it undercuts most comparable low-latency reasoning APIs while offering open weights. Best suited to high-volume agentic and RL-heavy workloads where cost-per-call dominates.

## Notes
- MIT open weights (HF).
- Sibling tiers: MiMo-V2.6-Pro (flagship) and MiMo-V2.6-Pro-UltraSpeed (up to 20× faster).