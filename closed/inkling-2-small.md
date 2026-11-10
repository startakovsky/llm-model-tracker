---
model: Inkling 2 Small
organization: Thinking Machines
license: other
release_date: 2026-11-05
last_updated: 2026-11-10
sources:
  - https://www.edenai.co/post/inkling-2-small-benchmarks-pricing-cost-per-task
  - https://openrouter.ai/thinkingmachines/inkling-2-small
  - https://x.com/thinkymachines/status/2119896225315188993
---

# Inkling 2 Small

First model of **Thinking Machines Lab's second Inkling generation** (Nov 5, 2026, Mira Murati's lab) — trained from scratch, not an update of the first generation. 594B total / 17B active per token mixture-of-experts, multimodal (text + image), built for long-horizon autonomous work, agentic coding, and knowledge work.

## Key Facts

- **Pricing:** $0/$0 free OpenRouter endpoint (`thinkingmachines/inkling-2-small:free`, limited-time). Tinker platform list: $0.30 input / $0.03 cached / $1.00 output per M. Full paid base listing not yet live on OpenRouter.
- **Context:** 1M ctx; adjustable reasoning effort with a length penalty.
- **AA Intelligence Index 31** (+18 over Inkling Small, level with Gemini 3.8 Flash high).
- **Weights:** Apache 2.0 announced for the week after launch, after external safety testing — **not yet on HuggingFace** (as of Nov 10). Tinker-only for now (Playground, API, fine-tuning).

## Benchmarks (Thinking Machines + Artificial Analysis, Nov 5)

| Benchmark | Inkling 2 Small | DeepSeek V4.1 Flash | Kimi K3 | GLM-5.3-Flash |
|---|---|---|---|---|
| DeepSWE v1.1 | 72.1% | **77.0%** | 68.5% | 63.4% |
| Vibe Code Bench v1.1 | 81.6% | **87.7%** | 85.0% | 30.8% |
| MMMU Pro (vision) | **81.6%** | 80.6% | 80.5% | 79.0% |
| ScreenSpot Pro | **83.8%** | n/r | 73.8% | n/r |
| Vals Finance Index | **61.5%** | 60.9% | 58.0% | 55.8% |
| Vals Legal Index | **73.9%** | 71.9% | 71.7% | 71.1% |
| AA-Briefcase v1.1 (Elo) | 1527 | **1570** | 1497 | 1451 |
| HLE-Diamond | **28.7%** | n/r | 26.9% | 18.2% |

AutomationBench: 5% → 46% (RL trained on long coding tasks, graded on process — how it works — not just passing tests). Vision encoder is 292M-param; designed to read screenshots/charts/docs and check its own visual output (website/3D building). Independent note: hallucination drop 61%→27% mostly from declining to answer more often (accuracy 32%→34%).

## Cost-per-Task Reality Check

Very chatty: ~150K output tokens per AA task (4x Inkling Small) → **~$1.18/task** at Tinker pricing. That's ~6.6x cheaper than Gemini 3.8 Flash high for the same score, ~8.5x cheaper than Claude Sonnet 5.5 medium, but ~6x more expensive per task than its own predecessor Inkling Small ($0.20). Lower the effort setting for simple requests.

## Quality Assessment

The strongest open-weight-class vision/document model of its size tier (best MMMU Pro, ScreenSpot Pro, Vals Finance/Legal among the open field), with coding that is good but not best-in-class (DeepSeek V4.1 Flash 1017 stays ahead on DeepSWE/Vibe Code; Terminal-Bench 4.0 only 13% vs Sonnet 5.5's 30%). Artificial Analysis expects it to become the highest-scoring open-weight model developed outside China once weights drop. Training was notably frugal: 12.6T tokens, main RL run 9 days on 2,048 GPUs (GENCI CTO flagged the low compute/data vs competitors).

## Notes

- The full Inkling 2 family presumably follows this Small variant.
- Classified `closed` (Frontier) pending the Apache-2.0 weights release — flip to `open` when the repo appears.
