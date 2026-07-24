# Ling 3.0 Flash — inclusionAI

| Field | Value |
|---|---|
| **Org** | inclusionAI (Ant Group) |
| **OpenRouter ID** | `inclusionai/ling-3.0-flash:free` (live as of Jul 23 2026) |
| **HuggingFace** | [inclusionAI/Ling-3.0-flash](https://huggingface.co/inclusionAI/Ling-3.0-flash) |
| **License** | MIT |
| **Release date** | 2026-07-23 |
| **Pricing** | Free on OpenRouter ($0/$0 per M tokens); open weights also self-hostable |
| **Context** | 262,144 (262K) |
| **Category** | Self-hostable (open) |

## Architecture

Ling 3.0 Flash is inclusionAI's latest **hybrid-reasoning Mixture-of-Experts** model, built for production-scale agentic inference:

- **124B total / 5.1B active** parameters — extremely efficient per-token computation.
- **Hybrid reasoning**: combines fast mode and deep reasoning mode in a single model.
- Designed with **token efficiency** as a key priority — developers can complete more useful work within constrained token, latency, and serving-cost budgets.
- **Production-scale agents**: optimized for agentic workflows at inference time.
- Open weights available on HuggingFace and ModelScope upon release.

This is a major version bump from the Ling-2.6 series (Ling-2.6-1T at 1T/63B and Ling-2.6-Flash at 104B/7.4B). Ling 3.0 Flash shifts to a more efficient architecture: more total parameters than 2.6-Flash (124B vs 104B) but far fewer active (5.1B vs 7.4B), targeting the sweet spot between capability and serving cost.

## Quality Assessment

Ling 3.0 Flash is a **mid-tier open model** designed for cost-efficient agentic inference rather than frontier benchmarks. With only 5.1B active parameters, it cannot match GLM-5.2 (753B/40B, quality 90) or Kimi K3 (2.8T MoE, quality 93) on raw reasoning. However, its value proposition is **extreme efficiency**: at 5.1B active params, it can serve production agents at a fraction of the cost of frontier models.

**Cost/quality framing:** Free on OpenRouter during launch. At 5.1B active params, self-hosting is feasible on a single consumer GPU. Relative to GLM-5.2 (the open reference at quality 90), Ling 3.0 Flash is ~70% as capable on text reasoning/coding but at ~0% API cost and dramatically lower self-hosting cost. The hybrid-reasoning design means it can switch to deep reasoning when needed without a separate model.

**Community signal:** 249 upvotes on r/LocalLLaMA within hours of launch. Strong interest from the local LLM community due to the 5.1B active param count.

**Verdict:** A solid mid-tier open model for cost-sensitive agentic workloads. Not a frontier competitor, but an excellent choice for production agents where token efficiency and serving cost matter more than peak benchmark scores. The free OpenRouter tier makes it accessible to everyone.
