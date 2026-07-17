# Kimi K3 — Moonshot AI

| Field | Value |
|---|---|
| **Org** | Moonshot AI |
| **OpenRouter ID** | `moonshotai/kimi-k3` |
| **License** | MIT |
| **Release date** | 2026-07-14 |
| **Pricing** | $3.00 / $15.00 per M tokens (OpenRouter) |
| **Context** | 1,048,576 (1M) |
| **Category** | Frontier (open) |
| **Quality score** | 93 |

## Architecture

Kimi K3 is Moonshot AI's flagship model and the **largest open-weight model ever released**:

- **2.8 trillion total parameters** — Mixture-of-Experts (MoE) architecture
- **1 million token context window**
- **Multimodal:** accepts text and image inputs, outputs text
- Designed for complex coding, long-horizon agentic workflows, knowledge-intensive tasks, and enterprise-scale document processing
- Deeply integrated with the **Kimi Code** ecosystem for autonomous software development
- **Open weights promised by July 27, 2026** — currently API-only via OpenRouter and Kimi platform

## Benchmarks

| Benchmark | Kimi K3 | GLM-5.2 (ref) |
|---|---|---|
| BenchAlign overall | 82/100 | 63.96/100 |
| Agentic | 91.2 | 81.0 |
| Knowledge | 61.1 | 59.6 |
| GPQA | 93.5% | 91.2% |
| HLE | 56% | 54.7% |
| Multimodal | 78.5 | — |

According to Moonshot AI, Kimi K3 outperforms GLM-5.2 across every published coding benchmark. BenchLM rates it ~18 points ahead of GLM-5.2 on overall BenchAlign. Positioned at Claude Fable 5 / GPT-5.6 Sol level.

## Quality Assessment

Kimi K3 is the **strongest open-source model available as of July 2026**. It posts the highest open-model agentic score (91.2) and matches or exceeds closed-frontier models on knowledge benchmarks. Its coding performance is its standout — Moonshot claims it beats GLM-5.2 on all coding benchmarks.

**Cost/quality framing:** At $3.00/$15.00 per million tokens, Kimi K3 is roughly 3.4× the output cost of GLM-5.2 ($0.94/$2.95), but delivers materially stronger benchmark results. It is cheaper than Claude Opus 4.8 ($5/$25) and GPT-5.6 Sol ($5/$30) while approaching their capability. Once open weights drop (July 27), self-hosting becomes possible at the cost of running a 2.8T MoE — practical only for datacenter-scale deployments.

**Community signal:** Massive buzz — trending on r/LocalLLaMA, covered by Reuters and VentureBeat ("the largest open-source model ever"). Weights release on July 27 is highly anticipated.

**Verdict:** The new open-source king. If weights land as promised, it replaces GLM-5.2 as the reference open model. Watch for July 27 weight release and community quantization (GGUF) efforts.
