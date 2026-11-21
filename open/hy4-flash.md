---
model: Tencent Hy4 Flash
organization: Tencent
license: Hy License (custom) — weights released Nov 18, 2026 (tencent/Hy4-flash + Hy4-flash-FP8 + Hy4-flash-base)
release_date: 2026-11-16
last_updated: 2026-11-21
sources:
  - https://huggingface.co/tencent/Hy4-flash
  - https://news.sulat.com/2026/11/16/tencent-hy4-flash
  - https://superpowerdaily.com/posts/tencent-releases-hy4-flash-with-ai-input-priced-at-0-07-per-million-tokens
  - https://aichatdaily.com/ai-models/tencent-launches-hy4-flash-cutting-task-costs-one-twentieth
---

# Tencent Hy4 Flash

Cost-efficient everyday-workhorse variant of Tencent's Hy4 line, launched Nov 16, 2026. Positioned as "the cheapest model for everyday productivity," matching Claude Haiku 5.5 on daily work in Tencent's internal blind tests at ~18x lower cost/task.

## Availability
- OpenRouter id `tencent/hy4-flash` at $0.04375/$0.175625 per M, 1M ctx, live Nov 16 (~38% under Tencent's official list).
- Tencent official API: $0.070 input / $0.281 output / $0.003 cached per M (TokenHub). WorkBuddy free + TokenHub 50% off until Nov 30.
- Deployed across Tencent Cloud TokenHub, WorkBuddy, Yuanbao, WeCom, QQ, ima, Marvis.
- **Weights released Nov 18** on HuggingFace/ModelScope/GitCode (`tencent/Hy4-flash`, `Hy4-flash-FP8`, `Hy4-flash-base`) — 220B-total/12B-active with 1M ctx; reclassified **open from closed** (Nov 21 tracking). Tencent Hy License: free below $50M annual MaaS revenue / 100M MAU, separate commercial agreement above.

## Specs
- 224B total params, 12B active per token; 64B of the total counted as Engram parameters.
- Hybrid attention + LatentMoE + Engram architecture; KV cache cut to 1/24 of Hy3's size and 1/6 of Hy4's.
- Post-training: self-distillation from Hy4, then RL — average end-to-end output tokens cut 50%.
- Serving: megakernels, DFly, 4-bit quantization; decoding past 150 tokens/sec.
- 1M ctx, multimodal.

## Blind test (85 internal WorkBuddy users, 259 tasks, 27 categories; external models at high tier)
| Model | Satisfaction (4-pt) | Median time | Cost/task (yuan) |
|---|---|---|---|
| DeepSeek-V4.1-Flash-1017 | 3.09 | 10.3 min | 1.20 |
| Hy4 Flash | 2.79 | 6.7 min | 0.26 |
| Claude Haiku 5.5 | 2.81 | 6.8 min | 4.73 |
| GLM-5.3-Flash | 2.53 | 7.6 min | 0.81 |

## Quality assessment
Excellent cost/quality for everyday productivity: ~Haiku-5.5-level satisfaction at ~1/18th the cost/task, fastest median completion in Tencent's test. 12B-active MoE with weights now public (Nov 18) means real self-hosting headroom — free commercial use below the $50M MaaS / 100M MAU Hy License threshold. Note the blind test is Tencent's own, small-n (85 users), and satisfaction trails DeepSeek-V4.1-Flash-1017. Score 74: cheap, fast, good-enough — a Lightweight-tier value play, not a frontier contender.
