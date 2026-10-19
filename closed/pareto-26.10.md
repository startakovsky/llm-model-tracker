---
model: Pareto 26.10
organization: Unbiased
license: Proprietary
release_date: 2026-10-15
last_updated: 2026-10-19
sources:
  - https://openrouter.ai/unbiased/pareto-26.10
---

# Pareto 26.10

GA snapshot of Unbiased's blended Pareto composite (follows Pareto 26.9, Sep 17). Replaces the 26.10 Preview on OpenRouter as of Oct 15, 2026, at the same $0.80/$3.20 price and 1M context.

## API Providers
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (unbiased/pareto-26.10) | $0.80 | $3.20 | 1,048,576 |

## How it works
Like Pareto 26.9: engages multiple LLMs in parallel per request and synthesizes a single answer (text + vision). The blended stealth-composite pattern continues across Pareto snapshots.

## Quality Assessment
A routing/mixture composite — a proxy for "best blend of frontier models at a given price" rather than a single architecture. Value depends on how well Unbiased's routing weights track the underlying model mix. Quality score 87 held from 26.9/26.10-preview.

## Notes
- Closed API (Proprietary)
- 26.10 Preview listing dropped from OpenRouter; GA replaced it at the same price