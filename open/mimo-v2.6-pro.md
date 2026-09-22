---
model: MiMo-V2.6-Pro
organization: Xiaomi
license: MIT
release_date: 2026-09-21
last_updated: 2026-09-22
openrouter_id: xiaomi/mimo-v2.6-pro
category: Frontier
---

# MiMo-V2.6-Pro

Xiaomi's flagship omni-modal reasoning model in the MiMo-V2.6 series, released and open-sourced Sep 21, 2026. Supersedes the closed-weight MiMo-V2.5 line.

## Architecture
- **Context length:** 1,048,576 (1M)
- **Modality:** Omni-modal (multi-modality reasoning)
- **Architecture type:** Flagship reasoning model (open weights)

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (xiaomi/mimo-v2.6-pro) | $0.435 | $0.87 | 1,048,576 |

## Self-Hosting
- Open weights on HuggingFace (MiMo-V2.6 series), MIT license.
- Notable shift: Xiaomi moved the flagship V2.6 line open (MIT) after shipping closed MiMo-V2.5 via API.

## Quality Assessment
Xiaomi's strongest reasoning model to date, aimed at agentic digital-work and complex reasoning. At $0.435/$0.87 with 1M context and open weights, it's a strong cost-per-dollar self-host candidate versus closed frontier reasoning APIs. Xiaomi highlights productivity gains in domains like new-materials R&D.

## Notes
- Open-sourced under MIT (HF).
- Low-latency sibling: MiMo-V2.6-Flash; UltraSpeed variant up to 20× faster generation.