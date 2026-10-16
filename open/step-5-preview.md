---
model: Step 5 Preview
organization: StepFun
license: StepFun Model License 1.0
release_date: 2026-10-06
last_updated: 2026-10-16
sources:
  - https://huggingface.co/stepfun-ai/Step-5-Preview
  - https://pandaily.com/stepfun-step-5-preview-open-weights-technical-blog-92-layer-sparse-gqa/
---

# Step 5 Preview

StepFun's flagship model for agentic work, released as a preview ~Oct 6-7, 2026, with **weights released Oct 15, 2026** (on schedule). Sparse MoE: 27B active / 600B total parameters, up to 1M context (1.048M on OpenRouter). Strong in software engineering and professional knowledge work, with particular strength in finance. Built for long-horizon agentic tasks spanning large codebases and documents — tool use with iterative verification and refinement over many steps.

## Key signals
- 600B/27B active sparse MoE; 92-layer sparse GQA architecture; FP8 and BF16 checkpoints.
- Input: text + image (specs say text/image/video in capability docs; model card lists text+image). Output: text.
- Multi-step tool use for long-horizon agentic and professional work; finance is a particular strength.
- 83.75% on the 8 Kingbench coding tasks (MindStudio test). Strong SWE + professional knowledge.
- NVIDIA congratulated StepFun on "their largest open weights release" — designed for agent tasks lasting up to 24 hours.

## Availability
- **OpenRouter:** **$1.00/$2.70 per M**, 1M ctx (was 1M, now 1.048M). $0.05/M cached-input.
- **Weights:** HuggingFace `stepfun-ai/Step-5-Preview` (82 likes, ~600 downloads day one; FP8/BF16).
- **License:** StepFun Model License 1.0 — Apache-2.0-style with additional attribution and commercial-license conditions for model use/modification/distribution. Not pure Apache 2.0.

## Classification
`open` (weights on HF as of Oct 15; license is Apache-2.0-style with conditions). Quality score **80** — frontier-class agentic coding and professional knowledge at a bargain $1.00/$2.70; now self-hostable (FP8 on 4× B300 / 8× H200).

## Notes
- Follows StepFun's pattern of shipping a closed preview before an open-weights release (Step 3.5 Flash is open Apache 2.0; Step 3.7 Flash remains closed). Step 5 Preview has now reclassified to open.
- Step 5 vs Step 5 Preview: this is the preview snapshot; the production Step 5 may differ.
