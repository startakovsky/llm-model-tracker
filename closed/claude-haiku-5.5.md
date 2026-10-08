---
model: Claude Haiku 5.5
organization: Anthropic
license: Proprietary
release_date: 2026-10-07
last_updated: 2026-10-08
---

# Claude Haiku 5.5

Anthropic's small, fast model for high-volume, cost-sensitive work, released Oct 7, 2026. Succeeds Claude Haiku 4.5 with stronger coding, computer use, and knowledge work. Text + image input, 1M-token context.

## Availability
- Closed API only. `anthropic/claude-haiku-5.5` on OpenRouter at $0.10/$0.50 per M (matches GPT-6 Luna pricing), 1M ctx.
- **Pricing caveat:** $0.10/$0.50 up to 100K tokens; beyond that the price increases 5x to $0.50/$2.50. GPT-6 Luna's long-context bump is milder ($0.20/$0.75 past 272K), so Luna is the better deal above ~100K tokens.
- New, less generous tokenizer: same prompt uses ~1.25x as many tokens as Haiku 4.5 (hidden price increase).
- ~75% cheaper to run than Haiku 4.5 on average.

## Classification
`closed` (Proprietary). Quality score 75 — positioned as Anthropic's lightweight tier: fastest, most capable small model, built for classification, routing, extraction, summarization, subagents, and browser use.

## Notes
- First Haiku with adjustable effort settings. Thinking is adaptive and on by default; effort is the main lever (low/medium/high) trading off depth, latency, and cost. Reasoning cannot be fully disabled.
- 1M ctx, 128K max output (per Anthropic docs), text+image input.
- Reports higher benchmark scores than GPT-6 Luna at equal price for workloads fitting in 100K tokens.
- On OpenRouter from Oct 8 at $0.10/$0.50 (standard routing), 1M ctx.
