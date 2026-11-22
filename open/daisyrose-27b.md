---
model: DaisyRose-27B
organization: RadixArk
license: Apache 2.0
release_date: 2026-11-18
last_updated: 2026-11-22
sources:
  - https://huggingface.co/RadixArk/DaisyRose-27B
  - https://radixark.com/blog/daisyrose-27b
  - https://openrouter.ai/radixark/daisyrose-27b
---

# DaisyRose-27B — RadixArk

| Field | Value |
|---|---|
| **Org** | RadixArk (SGLang / Miles RL framework team, CEO Ying Sheng) |
| **OpenRouter ID** | `radixark/daisyrose-27b` |
| **HuggingFace** | [RadixArk/DaisyRose-27B](https://huggingface.co/RadixArk/DaisyRose-27B) |
| **License** | Apache 2.0 (open weights) |
| **Release date** | 2026-11-18 |
| **Pricing** | $0.15/$1.875 per M |
| **Context** | 262,144 |
| **Category** | Lightweight (open) |

## Architecture

- **27.8B dense** (incl. 0.46B vision encoder + 0.42B multi-token-prediction head) — RL-only post-train of Qwen3.8-27B, no SFT/distillation.
- Qwen3.8 arch: 64 decoder layers in a 3:1 Gated DeltaNet linear-attention / full-attention pattern; hidden 5,120.
- Text+image in, text out; thinking model (reasoning in `reasoning_content`).
- Apache 2.0 weights in BF16 (~52 GB), FP8 (~29 GB), NVFP4 (~23 GB, Blackwell), plus GGUF — runs on a single GPU (H200, B200, GB300, RTX 5090, DGX Spark).
- DSpark draft model for speculative decoding with SGLang.

## Benchmarks

Self-reported (BF16/FP8 best runs), vs Qwen3.8-27B base:

| Benchmark | DaisyRose-27B | Qwen3.8-27B |
|---|---|---|
| Terminal-Bench 4.1 | 12.0 | 5.6 |
| Terminal-Bench 2.1 | 75.5 | 73.0 |
| DeepSWE v1.1 | 46.2 | 42.2 |
| SWE Bench Pro v2 | 94.7 | 91.3 |
| IFBench | 82.4 | 79.5 |
| GPQA Diamond | 90.7 | 89.2 |
| HLE (text) | 34.3 | 33.9 |

- Beats base on all 7; Terminal-Bench 4.1 more than doubles. IFBench 82.4 tops RadixArk's 9-model table.
- Trails much larger MoE models on hard agentic tasks (Inkling 2 Small 72.1 DeepSWE; MiMo V2.6 Flash 16.1 TB4.1).

## Quality Assessment

~same-size upgrade over Qwen3.8-27B for long-horizon agentic coding — the RL-only recipe double-clicked terminal-agent skill in 18 days / 63K GPU-hrs (144 H200s). Value play: ~85% of Inkling 2 Small's DeepSWE at ~1/5 the price, runs on one GPU, fully Apache-2.0. At 27B dense it is a strong Lightweight-tier agent pick, not a frontier contender. Score 64.

- Training data note: 1,200 curated tasks (Eigent AI), sandbox attempts up to 1.5h / 100+ tool calls / 256K+ output tokens; ~944K sandboxes run total.
