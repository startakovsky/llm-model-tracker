---
model: Mistral Medium 3.5
organization: Mistral AI
license: Proprietary
release_date: 2026-04-30
last_updated: 2026-07-11
---

# Mistral Medium 3.5

## Architecture
- **Total params:** ~128B (dense)
- **Context length:** 262,144
- **Modality:** Text + Image + File → Text
- **Architecture type:** Dense instruction-following model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (mistralai/mistral-medium-3-5) | $1.50 | $7.50 | 262,144 |

## Quality Assessment
Mistral Medium 3.5 is a dense 128B instruction-following model from Mistral AI. Designed for agentic workflows, coding, and complex reasoning. Supports text and image inputs. At $1.50/$7.50/M, it's priced similarly to Gemini 3.5 Flash but with half the context (262K vs 1M) and fewer modalities. Dense architecture means consistent quality across all params. Mistral's first tracked medium-tier with multimodal support — a solid mid-range option for European enterprises needing data sovereignty.

## Notes
- Dense 128B — no MoE routing variance
- Multimodal: text + image input
- 262K context
- European-based provider (data sovereignty advantage)
