# Ling 3.0 Tiny — inclusionAI

| Field | Value |
|---|---|
| **Org** | inclusionAI (Ant Group) |
| **OpenRouter ID** | `inclusionai/ling-3.0-tiny` (free tier as of Aug 11 2026) |
| **HuggingFace** | [inclusionAI/Ling-3.0-tiny](https://huggingface.co/inclusionAI/Ling-3.0-tiny) |
| **License** | MIT |
| **Release date** | 2026-08-10 |
| **Pricing** | Free on OpenRouter ($0/$0 per M tokens); open weights also self-hostable |
| **Context** | 262,144 (262K) |
| **Category** | Lightweight (open) |

## Architecture

Ling 3.0 Tiny is the lightweight sibling of inclusionAI's **Ling-3.0** family, alongside Ling 3.0 Flash (124B/5.1B MoE):

- **~8B total / 1.3B active parameters** — a small Mixture-of-Experts model (~7.9B total params confirmed on HF safetensors).
- Distilled/local-oriented variant of the Ling 3.0 platform, geared toward on-device and low-cost local inference.
- **MIT license** — fully permissive, no usage restrictions.
- Open weights on HuggingFace (`inclusionAI/Ling-3.0-tiny`) and ModelScope.

This lands at the small end of the Ling family: Ling-2.6-1T (1T/63B), Ling-2.6-Flash (104B/7.4B), Ling-3.0-Flash (124B/5.1B) → Ling-3.0-Tiny (~8B/1.3B).

## Quality Assessment

Ling 3.0 Tiny is a **lightweight open model** for edge/local use rather than a frontier competitor. With only ~1.3B active parameters, it will not approach GLM-5.2 (753B/40B, quality 90) or Kimi K3 (2.8T MoE, quality 93) on raw reasoning — or even Ling-3.0-Flash (quality 68). Its value is **portability and cost**: ~7.9B total params run comfortably on a consumer GPU, making it an accessible entry point into the Ling 3.0 platform for on-device agentic workloads.

**Cost/quality framing:** Free on OpenRouter and trivially self-hostable. Relative to GLM-5.2 (open reference at quality 90), Ling 3.0 Tiny is ~55% as capable on simple reasoning/coding but at ~0% API cost and minimal hardware footprint. Choose the Flash variant for production agents (5.1B active) and Tiny for edge/local prototyping.

**Community signal:** 122 HF likes within a day of release; discussed on r/LocalLLaMA. Decent early traction for a small model.

**Verdict:** A new, actively-tracked lightweight addition to the Ling family. Not a frontier player — useful as a low-cost local/edge option and a sign of inclusionAI rounding out its product line downward. Quality scored 50 (comparable to Qwen3.5-9B and Llama 3.3 8B-class small models).
