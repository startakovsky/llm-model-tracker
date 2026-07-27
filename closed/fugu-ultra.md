# Fugu Ultra — Sakana AI

| Field | Value |
|---|---|
| **Org** | Sakana AI (Tokyo, Japan) |
| **OpenRouter ID** | `sakana/fugu-ultra` (live as of ~Jun 24 2026) |
| **License** | Proprietary (orchestration service, no weights) |
| **Release date** | 2026-06-24 (v1.0), v1.1 upgrade ~Jul 2026 |
| **Pricing** | OpenRouter $5.00 prompt / $30.00 completion per M tokens |
| **Context** | 1,000,000 (1M) |
| **Category** | Frontier (closed) |

## Architecture

Fugu Ultra is **not a traditional LLM** — it is a **multi-agent orchestration engine** that dynamically coordinates a pool of frontier models to solve complex tasks:

- Instead of relying on a single model, Fugu **runs a team of AIs** and picks the best one for each part of the task.
- Dynamically orchestrates the latest frontier models, routing subtasks to the model best suited for each.
- Upgraded to v1.1 with incorporation of the latest frontier models, pushing performance up by as much as 7.9 points over v1.0.
- Available on OpenRouter, Vercel, and via Claude Code-compatible endpoints.
- **Closed**: no downloadable weights — it is an orchestration service that calls other (closed and open) models internally.

The key insight: intelligence doesn't require training a bigger model. By combining the strengths of multiple frontier models, Fugu Ultra matches or beats individual frontier models without needing to train its own mega-model.

## Benchmarks (Sakana-reported, v1.1)

| Benchmark | Fugu Ultra | Notes |
|---|---|---|
| LiveCodeBench | 93.2 | Leads several coding tests |
| GPQA | 95.5 | Top-tier science reasoning |
| SWE-bench Pro | 73.7 | vs 69.2 for strongest individual worker baseline |
| Terminal Bench 2.1 | 82.1 | Agentic coding |

Fugu Ultra matches Claude Opus 4.8 and GPT-5.5 on several benchmarks — **without either model in its agent pool** (both are subject to export controls in Japan). It also beats Fable 5 in complex coding and reasoning tasks without Fable in the pool.

## Quality Assessment

Fugu Ultra achieves **frontier-level performance** through orchestration rather than scale. Its benchmark scores (93.2 LiveCodeBench, 95.5 GPQA) are competitive with the very best closed models. The SWE-bench Pro score of 73.7 exceeds the strongest individual worker model (69.2), demonstrating that the multi-agent approach genuinely adds value beyond simply calling the best single model.

**Cost/quality framing:** At $5/$30 per M tokens, Fugu Ultra is priced at the same tier as GPT-5.5 ($5/$30) and cheaper than GPT-5.5 Pro ($30/$180) or Claude Opus 4.8 Fast ($10/$50). For complex multi-step coding and reasoning tasks where quality matters more than latency, it offers frontier-level output at standard frontier pricing. For simpler tasks, a single frontier model may be more cost-effective since Fugu's orchestration adds overhead.

**Community signal:** Significant buzz on social media — "Japanese lab matched frontier AI without training a bigger model." Covered by major outlets. The Claude Code interface launch expanded developer adoption.

**Verdict:** A novel approach to frontier AI — orchestration over training. Not a self-hostable model, but a compelling option for complex agentic workflows where the best single model isn't enough. The fact that it matches Fable 5 and Claude Opus 4.8 without either in its pool suggests the orchestration layer adds genuine intelligence, not just routing. Worth tracking as the orchestration paradigm evolves.
