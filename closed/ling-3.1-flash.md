# Ling 3.1 Flash — inclusionAI

| Field | Value |
|---|---|
| **Org** | inclusionAI (Ant Group) |
| **OpenRouter ID** | `inclusionai/ling-3.1-flash` (live Oct 2 2026) |
| **HuggingFace** | Weights NOT yet published (open-sourcing planned after trial) |
| **License** | Not published yet (predecessor Ling-3.0-flash is MIT) |
| **Release date** | 2026-09-30 |
| **Pricing** | Free intro on OpenRouter ($0/$0 per M); reported list $0.075/$0.22 |
| **Context** | 262,144 on OpenRouter (1M design, capped during free trial) |
| **Category** | Frontier (closed for now — announced, not open release) |

## Architecture

Ling 3.1 Flash is inclusionAI's latest **hybrid-reasoning Mixture-of-Experts** model, positioning for agent tasks, search, office software and specialist applications:

- **560B total / 25B active** parameters — a major jump from Ling-3.0-Flash (124B/5.1B).
- **Hybrid reasoning**: fast mode + deep reasoning in one model; thinking on by default, can be toggled off.
- **1M-token context window** by design; the free-trial tier caps at ~256K (262,144 on OpenRouter), full window via paid tier after Oct 13.
- Optimized for coding, multi-step analysis, tool-using agents, long documents and extended task histories.

## Quality Assessment

Ling 3.1 Flash is a **frontier-class 560B/25B MoE** from a Chinese lab with a strong release cadence (Ling-2.6 → 3.0 → 3.1 in ~4 months). But as of release there are **no published external benchmarks** — only self-reported CyberGym 87.9%, and BenchLM lists just 8 of 495 benchmarks covered, all self-reported, unranked overall. Weights are not yet published (the Sep 30 AI Weekly coverage explicitly calls it "an announced one, not an open release"), so on the tracker it classifies **closed** until a repo + license appear.

**Cost/quality framing:** At $0.075/$0.22 reported list (free intro on OpenRouter), it lands well below frontier API pricing. If its capability holds up in independent evals, it would be a strong cost/quality play for coding and agent workflows — ~80-85% of GLM-5.3-class capability at a fraction of the price. But that is unverified: no external benchmark exists yet, and the "open weights after trial" promise is unfulfilled.

**Community signal:** Live on Vercel AI Gateway the same day as announcement — unusual for a pre-pricing release. Moderate interest on r/LocalLLaMA; the open-source commitment is treated with caution until a repo appears (same pattern as Ling-3.0-Flash's two-week gap).

**Verdict:** A genuinely new frontier-class open-pending model worth tracking. Treat benchmark claims as unverified; classify closed until weights drop. The free OpenRouter intro makes it worth a hands-on look for agentic coding workloads.
