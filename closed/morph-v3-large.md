---
model: Morph V3 Large
organization: Morph (YC S23)
license: Proprietary
release_date: 2026-07-15
last_updated: 2026-08-17
sources:
  - https://www.morphllm.com/
  - https://vercel.com/ai-gateway/models/morph-v3-large
  - https://news.ycombinator.com/item?id=44490863
---

# Morph V3 Large

Released ~July 2026 (V3 generation). Morph (YC S23) builds fast inference specifically for coding agents — applying AI-suggested code edits directly into source files rather than generating reasoning-heavy completions. V3 Large is the flagship tier.

## Availability
- **OpenRouter:** LIVE at **$0.90/$1.90 per M tokens** (prompt/completion). 262K ctx (81.9K input / 16K output tokens per request).
- Also exposed via Vercel AI Gateway and LiteLLM.

## Classification
`closed` (proprietary API — a routing/inference product, not downloadable weights). Category: Specialized (code-application). Quality score 72 for its narrow agentic-coding niche.

## Notes
- Applies code edits with ~90% merge accuracy on complex multi-scope edits, ~2500+ tok/s (about 30% faster baseline).
- Positions as a cheap, fast "pair" to a frontier planner model: frontier model writes the edit, Morph applies it.
- Real community traction (HN Show, YC S23) though it is a tool model rather than a frontier LLM.

## Sources
- Morph: https://www.morphllm.com/
- Vercel AI Gateway: https://vercel.com/ai-gateway/models/morph-v3-large
- HN: https://news.ycombinator.com/item?id=44490863