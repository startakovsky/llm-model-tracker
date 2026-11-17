---
model: K2-Horizon-375B-A23B
organization: IFM
license: Apache-2.0
release_date: 2026-09-01
last_updated: 2026-11-17
sources:
  - https://huggingface.co/IFM/K2-Horizon-375B-A23B
  - https://huggingface.co/papers/2611.21003
---

# K2-Horizon-375B-A23B

Flagship of the K2-Horizon family from IFM (ifm-ai): a sparse MoE storing 375B params, running 23B per token, with a native 512K context window. Released open with checkpoints, training data, and training code (Apache-2.0). The K2-Horizon paper (Nov 16-17, 2026) documents the full fleet (0.9B dense → 375B-A23B MoE) and brings fresh community attention.

## Architecture
- **Total params:** 375B (sparse MoE), ~23B active per token
- **Experts:** 192 total, 8 active per token
- **Layers:** 61, hidden 6144, 48 attention heads / 8 KV heads
- **Context length:** 524,288 (512K, native from midtraining onward)
- **Modality:** text in / text out
- **License:** Apache-2.0 — weights + training data + training code all public

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter | — | — | — | Not listed (self-host / HF) |

## Quality Assessment
Self-reported results position it as frontier-class on agentic tool use, terminal, and long-horizon workflow benchmarks — matching or beating open-weight MoE models up to 2.6× its size and competitive with closed frontier models. A 375B/23B MoE at 512K context is self-hostable on multi-GPU rigs (FP8 ~200GB class), making it a serious open alternative for agentic workloads without API pricing. Traction is still modest (10-27K HF downloads per member at Nov 17; the 7B member leads with ~27K) — the Nov paper is the main buzz driver. Treat vendor benchmark claims with caution until third-party confirmation.

## Notes
- Fully open: training data (`IFM/K2-Horizon-Pretrain-Data`, `K2-Horizon-Midtrain-Data`) and training code (`ifm-ai/xllm`) public.
- Intermediate checkpoints released to study capability change across training.
- GGUF quants available for the smaller fleet members (3.7B, 7B).
- Not on OpenRouter as of Nov 17, 2026 — self-host only.
