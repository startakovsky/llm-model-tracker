---
model: Grok 4.6
organization: xAI (SpaceXAI)
license: Proprietary
release_date: 2026-08
last_updated: 2026-08-13
sources:
  - https://x.ai/news/grok-4-6
  - https://openrouter.ai/x-ai/grok-4.6
  - https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis
---

# Grok 4.6

xAI's latest frontier flagship, released 2026-08-12/13 and available via the SpaceXAI API, Cursor, Grok Build, and OpenRouter. Returns SpaceXAI to the intelligence frontier: **AA Intelligence Index 61**, in line with GPT-5.6 Sol, ahead of Kimi K3, behind only Anthropic (Claude Opus 5 at 63, Claude Fable 5 at 62).

## Architecture / Specs
- Context window: 500,000 (500K)
- Pricing: $2.00 in / $6.00 out per 1M tokens (flat vs Grok 4.5)
- Cache hits: $0.50/M (up from Grok 4.5's $0.30/M)
- Availability: SpaceXAI API, OpenRouter, Vercel, Cloudflare, Cursor, Grok Build (2x included usage first week)
- License: Proprietary (API/cloud only)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (x-ai/grok-4.6) | $2.00 | $6.00 | 500K | New endpoint, matches Grok 4.5 pricing |

## Quality Assessment
Grok 4.6 is an agentic-first frontier model. Artificial Analysis headline figures:
- **AA Intelligence Index: 61** (GPT-5.6 Sol tier; Fable 5 = 62, Opus 5 = 63)
- **GDPval-AA v2: Elo 1753** — behind only Claude Opus 5, statistically tied with Fable 5 and Qwen3.8 Max
- **Terminal-Bench v2.1: 88.4%** — level with the leading models
- **τ³-Banking: 50.7%** — top-2 score (alongside Qwen3.8 Max at 51.3%)
- **AA-Briefcase (long-horizon agentic): Elo 1577** — Fable 5-tier, notably turn-efficient (~53 turns / ~0.5B input tokens vs ~103 turns / ~2.0B for Opus 5)

**Agentic verdict:** Grok 4.6 is now a top-3 frontier agentic model with the best price/performance of the frontier tier — ~95% of Claude Opus 5's agentic quality at 40% of the price ($6 vs $25 out), and on the Intelligence-vs-cost Pareto frontier. For heavy reasoning/agentic workloads it dominates GPT-5.6 Sol ($30 out). Closed-source; no open weights.

## Sources
- Primary: https://x.ai/news/grok-4-6 (announcement), https://cursor.com/blog/grok-4-6
- Benchmarks: https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis
- Coverage: https://venturebeat.com/technology/spacexai-debuts-grok-4-6-...