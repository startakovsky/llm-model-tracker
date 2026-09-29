---
model: Claude Sonnet 5.5
organization: Anthropic
license: Proprietary
release_date: 2026-09-28
last_updated: 2026-09-29
---

# Claude Sonnet 5.5

New Anthropic Sonnet-class flagship (Sep 28, 2026), second model in the Claude 5.5 family. Positioned as faster, lower-cost complement to Opus 5.5 for well-scoped everyday work, bug-fixing, and polished document creation.

## Availability
- Closed API only. `anthropic/claude-sonnet-5.5` on OpenRouter at $2/$10 per M, 1M ctx (same price as Sonnet 5, matches GPT-6 Sol).
- Also on Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry.
- Batch API at 50% discount. 5m cache write $2.50, 1h cache write $4, cache read $0.20.

## Classification
`closed` (Proprietary). Quality score 92 — AA Intelligence Index 56 (#2 overall, just 2 pts behind Opus 5.5 max); Terminal-Bench 4.0 64% beats Opus 5.5 and GPT-6 Astra (both 60%).

## Notes
- 1M ctx, 128K max output, text+image input. Adaptive thinking on by default, default effort `high`, five effort levels (low→max).
- Runs 30%+ faster than Sonnet 5 (per Anthropic).
- Heaviest token use measured by Artificial Analysis: ~193K output tokens/task at max effort (~60% higher than Opus 5.5 max, ~7x GPT-6 Astra max), driving cost/task ~50% above Sonnet 5 — sits off the Intelligence vs Cost-per-Task Pareto frontier at most effort settings.
- Parity with Opus 5.5 on Terminal-Bench 4.0, AA-Briefcase, GDPval-AA, AutomationBench-AA.
- Lags Opus 5.5 on factual knowledge (AA-Omniscience 54% vs 66%) but lower hallucination rate (47% vs 59%).
- Released Sep 28, 2026; retirement no sooner than Sep 28, 2027.
