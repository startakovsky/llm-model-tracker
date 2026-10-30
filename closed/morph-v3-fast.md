---
model: Morph V3 Fast
organization: Morph (YC S23)
license: Proprietary
release_date: 2026-07-15
last_updated: 2026-10-30
sources:
  - https://www.morphllm.com/
  - https://openrouter.ai/morph/morph-v3-fast
---

# Morph V3 Fast

Fast-Apply tier of Morph's V3 code-edit family (V3 generation, ~Jul 2026), sibling of the tracked Morph V3 Large. Morph (YC S23) builds fast inference for coding agents — applying AI-suggested code edits directly into source files instead of generating reasoning-heavy completions.

## Availability
- **OpenRouter:** LIVE at **$0.80/$1.20 per M tokens** (prompt/completion), 262K ctx. ~10,500+ tok/s per Morph.
- Also exposed via LiteLLM, Vercel AI Gateway, and Netlify AI Gateway.

## Classification
`closed` (proprietary API — a routing/inference product, not downloadable weights). Category: Specialized (code-application). Quality score 70.

## Notes
- Cheaper, faster tier than Morph V3 Large ($0.90/$1.90, ~2500+ tok/s); same code-edit application niche.
- Positions as a cheap, fast "pair" to a frontier planner model: frontier model writes the edit, Morph applies it.

## Sources
- Morph: https://www.morphllm.com/
- OpenRouter: https://openrouter.ai/morph/morph-v3-fast
- LiteLLM provider docs: https://docs.litellm.ai/blog/morph-provider