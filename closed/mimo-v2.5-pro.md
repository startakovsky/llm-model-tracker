---
model: MiMo-V2.5-Pro
organization: Xiaomi
license: Proprietary
release_date: 2026-04-22
last_updated: 2026-07-11
---

# MiMo-V2.5-Pro

## Architecture
- **Context length:** 1,048,576
- **Modality:** Text → Text
- **Architecture type:** Flagship reasoning model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (xiaomi/mimo-v2.5-pro) | $0.435 | $0.87 | 1,048,576 |

## Quality Assessment
MiMo-V2.5-Pro is Xiaomi's flagship model, delivering strong performance in general agentic capabilities, complex software engineering, and long-horizon tasks. Top rankings on benchmarks such as ClawEval, GDPVal, and SWE-bench Pro. At $0.435/$0.87/M with 1M context, it's one of the best value propositions in the tracker — comparable to GLM-5.2 ($0.35/$1.10) on prompt pricing and cheaper on completion. The fact that Xiaomi (primarily a hardware company) is producing frontier-quality models is notable. Closed-weight (no HF weights found).

## Notes
- Xiaomi's first entry in the tracker — significant frontier push from a hardware company
- Top rankings on ClawEval, GDPVal, SWE-bench Pro
- 1M context at $0.435/$0.87/M — excellent value
- A non-overlapping variant (MiMo-V2.5) exists at half the price with omnimodal capabilities
