---
model: Particle-1
organization: Particle AI
license: Proprietary
release_date: 2026-10-28
last_updated: 2026-10-29
---

# Particle-1

First model from Particle AI, a new San Francisco startup founded by Suhail Doshi (Mighty, Mixpanel co-founder), launched Oct 28, 2026. A token-efficient agentic coding model post-trained on DeepSeek V4.1 Flash — positioned for terminal workflows, codebase changes, and data work where output-token cost dominates.

## Availability
- Closed API only. `particle-ai/particle-1` on OpenRouter at **$0.25/$1.00 per M**, 1M ctx, 131K max output.
- Cached input **$0.03/M** (88% below list prompt price). Reasoning is configurable (default `high`, up to `max`).
- Text+image input, text output. Structured outputs, tools, and seed supported.
- Launch claim: ~34% lower cost per coding task vs comparable models (token-efficient design).

## Classification
`closed` (Proprietary, API only). No weights on HuggingFace (HF search returns nothing for Particle-1 as of Oct 29). Quality score 74 — promising cheap agentic-coder niche play, unproven against established benchmarks; DeepSeek V4.1 Flash base means solid floor.

## Benchmarks
- No independent third-party benchmarks published yet (launch week). Company claims focus on cost-per-task efficiency for agentic coding rather than raw capability.
- Base model (DeepSeek V4.1 Flash) itself scores ~86 on this tracker, so Particle-1 inherits a strong foundation for terminal/agent work.

## Notes
- Founding team pedigree (Suhail Doshi) + "cheaper agentic coding" angle gives it startup buzz; worth watching for benchmark results and weight release.
- Distinct from the similarly-named "particle" physics models — this is a coding agent model.
