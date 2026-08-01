# Inkling Small — Thinking Machines

| Field | Value |
|---|---|
| **Org** | Thinking Machines (Mira Murati) |
| **OpenRouter ID** | `thinkingmachines/inkling-small` (live as of ~Jul 30 2026) |
| **HuggingFace** | [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling) (family) |
| **License** | Apache 2.0 |
| **Release date** | 2026-07-30 |
| **Pricing** | OpenRouter $0.50 prompt / $1.20 completion per M tokens; open weights self-hostable |
| **Context** | 524,288 (512K) |
| **Category** | Frontier (open) |

## Overview

Inkling Small is the **cost-efficient tier of the Inkling family** from Thinking Machines, the lab founded by former OpenAI CTO Mira Murati. It joins the flagship 975B/41B MoE `thinkingmachines/inkling` (Jul 15 2026) as a lighter, cheaper variant on OpenRouter.

- Same **Apache 2.0 open-weight** philosophy as the flagship.
- **512K context** — half the flagship's 1M, still ample for long-horizon agent and retrieval workloads.
- **$0.50/$1.20 per M** on OpenRouter — roughly **half the flagship's $1.00/$4.05**, making it the most affordable way to reach the Inkling family's multimodal reasoning stack via API.
- Shares the family's **native multimodal** design (text + image + audio in a single decoder, no bolted-on encoders).

## Quality Assessment

Inkling Small is positioned as a **price-tier variant**, not a separate architecture line. Expect it to sit a few points below the flagship Inkling (quality 85) on raw benchmarks while retaining the family's multimodal breadth and the same 45T-token training pedigree. Without published per-variant benchmark numbers, a provisional **quality score of 80** reflects "frontier-class but clearly the smaller sibling."

**Cost/quality framing:** At ~1/3 the blended cost of the flagship Inkling and ~1/5 of GLM-5.2's new $0.76/$2.39 (Aug 1), Inkling Small is attractive for **high-volume multimodal agent workloads** where the full 1M context and last-few-points of reasoning quality aren't worth a 2–3× premium. For pure text reasoning/coding, GLM-5.2 (quality 90) and DeepSeek V4 Pro (89) remain stronger per-token; Inkling Small's edge is **native image+audio at frontier-open pricing**.

**Verdict:** A sensible "Inkling-lite" for cost-sensitive multimodal pipelines. Not a frontier leader on text, but the cheapest open-weight multimodal frontier-class option currently on OpenRouter. Now live at $0.50/$1.20 per M (added ~Jul 30 2026).
