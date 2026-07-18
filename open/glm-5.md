---
model: GLM-5
organization: Z.ai
license: Apache 2.0
release_date: 2026-03-01
last_updated: 2026-07-18
---

# GLM-5

## Architecture
- **Total params:** 744B (MoE)
- **Active params per token:** ~40B
- **Context length:** 202,752
- **Architecture type:** GLM MoE

## Pricing
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (`z-ai/glm-5`) | $0.95 | $3.15 | 202,752 |

## Quality Assessment
GLM-5 is the March 2026 base release of Z.ai's GLM-5 family — a 744B/40B MoE that established the open-weight frontier tier before being superseded by GLM-5.1 (May) and the GLM-5.2 reference model (June). It remains a strong, widely-available open model at a mid-tier price.

**Cost/quality framing:** Roughly comparable to GLM-5.1 but a step below GLM-5.2 (quality 87 vs 90). Useful as a cheaper fallback when the 1M-context GLM-5.2 isn't required.

## Notes
- Predecessor to GLM-5.1 and GLM-5.2 in the same MoE family.
- Open weights on HuggingFace under Apache 2.0.
