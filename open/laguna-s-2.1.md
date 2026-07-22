---
model: Laguna S 2.1
organization: Poolside
license: OpenMDW-1.1
release_date: 2026-07-21
last_updated: 2026-07-22
---

# Laguna S 2.1

## Architecture
- **Total params:** 118B (MoE)
- **Active params per token:** 8B
- **Context length:** 1,048,576 (1M)
- **Architecture type:** Sparse Mixture-of-Experts
- **Modality:** Text → Text

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (poolside/laguna-s-2.1) | $0.10 | $0.20 | 1,048,576 |

## Benchmarks
- **Terminal-Bench 2.1:** 70.2%
- **DeepSWE:** 40.4%
- One of the strongest coding models in the 118B parameter category

## Self-Hosting
- Weights available on HuggingFace: `poolside/Laguna-S-2.1` (OpenMDW-1.1 license)
- 3,056 downloads and 327 likes within 24 hours of release
- Quantized variants already available:
  - GGUF (`poolside/Laguna-S-2.1-GGUF`, `unsloth/Laguna-S-2.1-GGUF`)
  - FP8 (`poolside/Laguna-S-2.1-FP8`) — 10,176 downloads
  - INT4 (`poolside/Laguna-S-2.1-INT4`) — 9,834 downloads
  - NVFP4 (`poolside/Laguna-S-2.1-NVFP4`) — 1,953 downloads
  - DFlash (`poolside/Laguna-S-2.1-DFlash`)
- Unsloth quantization released same day (community adoption signal)

## Quality Assessment
Poolside Laguna S 2.1 is the most capable open coding agent model from a Western lab in the 118B parameter class. With 70.2% Terminal-Bench 2.1 and 40.4% DeepSWE, it beats American and Chinese open-source competition in its weight class — with the notable exception of Moonshot's Kimi K3 (2.8T params, 20x larger). At $0.10/$0.20 per M tokens, it is exceptionally cheap for a coding agent — roughly 1/10th the cost of GLM-5.2 ($0.81/$2.55) while being purpose-built for software engineering. Forbes (Jul 21, 2026) featured it as a significant American open-source response to Chinese model dominance. Poolside CEO Jason Warner claims an industrial model-building process with new iterations every five weeks. Too new for comprehensive benchmark comparison, but the rapid community adoption (GGUF/FP8/INT4 within 24h) signals strong developer interest.

## Notes
- Featured in Forbes (Jul 21, 2026): "most capable open model in the West" in 118B class
- OpenMDW-1.1 license (open weights with use policy restrictions)
- Poolside co-founded by Jason Warner (former GitHub CTO) and Eiso Kant
- Industrial model-building process — new iterations planned every 5 weeks
- Sister model to Laguna XS 2.1 (33B/3B, already tracked)
- Significantly smaller than Kimi K3 (118B vs 2.8T) but competitive in coding
