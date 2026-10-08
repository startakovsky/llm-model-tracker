---
model: Step 5 Preview
organization: StepFun
license: Proprietary (weights pending)
release_date: 2026-10-06
last_updated: 2026-10-08
---

# Step 5 Preview

StepFun's flagship model for agentic work, released as a preview ~Oct 6-7, 2026. Built on a sparse Mixture-of-Experts architecture (27B active / 600B total parameters). Strong in software engineering and professional knowledge work, with particular strength in finance. Designed for extended tasks spanning large codebases and documents — using tools and refining results over multiple steps.

## Availability
- Closed API for now. `stepfun/step-5-preview` on OpenRouter at $1.00/$2.70 per M, 1M ctx.
- Weights scheduled to drop Oct 15, 2026 (per MindStudio); until then the model is API-only and treated as closed.
- $0.05/M cached-input pricing on OpenRouter.

## Classification
`closed` (Proprietary, weights pending). Quality score 80 — flagships-tier agentic coding and professional knowledge; 83.75% on the 8 Kingbench coding tasks (MindStudio test).

## Notes
- 600B total / 27B active sparse MoE — efficient inference for a frontier-class model.
- Multi-step tool use for long-horizon agentic and professional work; finance is a particular strength.
- Follows StepFun's pattern of shipping a closed preview before an open-weights release (Step 3.5 Flash was open-sourced Apache 2.0; Step 3.7 Flash remains closed). Watch the Oct 15 weight drop — if Apache 2.0, it reclassifies to `open` (Self-hostable).
