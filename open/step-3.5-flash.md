---
model: Step 3.5 Flash
organization: StepFun
license: Apache 2.0
release_date: 2026-01-29
last_updated: 2026-07-22
---

# Step 3.5 Flash

## Architecture
- **Total params:** 196B (MoE)
- **Active params per token:** 11B
- **Context length:** 262,144 (256K)
- **Architecture type:** Sparse Mixture-of-Experts
- **Modality:** Text → Text

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (stepfun/step-3.5-flash) | $0.10 | $0.30 | 262,144 |

## Self-Hosting
- Weights available on HuggingFace: `stepfun-ai/Step-3.5-Flash` (Apache 2.0)
- 123,753 downloads, 828 likes on HuggingFace
- Strong community adoption and traction

## Quality Assessment
Step 3.5 Flash is StepFun's most capable open-source foundation model. Built on a sparse MoE architecture with 196B total params and 11B active, it delivers high efficiency at very low cost ($0.10/$0.30 per M tokens). At this price point, it competes with OpenAI GPT-OSS-120B ($0.037/$0.17) and Qwen3-235B ($0.09/$0.55) while offering strong agentic and reasoning capabilities. The predecessor to the closed Step 3.7 Flash (also tracked). With 828 HuggingFace likes and 123K downloads, it has demonstrated sustained community traction over 6 months. Supports reasoning, tool use, and structured parameters. Good self-hosting option for teams wanting a mid-size MoE with Apache 2.0 licensing.

## Notes
- Open weights under Apache 2.0 (verified on HuggingFace)
- 828 HF likes, 123K downloads — strong sustained traction
- Predecessor to closed Step 3.7 Flash (tracked separately)
- 196B/11B MoE — mid-size, self-hostable on multi-GPU setups
- $0.10/$0.30 per M tokens — very cost-effective
- Supports reasoning, tool_choice, structured outputs
- Catch-up addition: on OpenRouter since Jan 2026, discovered during Jul 22 scan
