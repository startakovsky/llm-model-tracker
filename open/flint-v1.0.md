---
model: Recursive Flint
organization: Recursive
license: Apache-2.0
release_date: 2026-10-21
last_updated: 2026-10-22
sources:
  - https://huggingface.co/RecursiveSI/flint
  - https://www.recursive.com/updates/introducing-recursive-flint
  - https://github.com/recursive-oss/rec
  - https://openrouter.ai/recursive/flint-v1.0:free
---

# Recursive Flint

Coding-agent-focused mixture-of-experts model from Recursive (RecursiveSI), released Oct 21, 2026. Strong early community traction (434 likes, 420 downloads on HF in day one; front-page r/LocalLLaMA).

## Architecture
- **Type:** 39.8B total / ~2.5B active MoE (designated "40B-A2.5B")
- **Context length:** 262,144 tokens (prompt + generated)
- **Structure:** 49 layers (2 dense + 47 MoE); 35 sliding-window + 14 full-attention layers; 256 routed experts with 6 selected per token plus an always-active shared expert
- **Attention:** 32 query heads / 4 KV heads (head dim 128); per-head QK RMSNorm with learned attention sinks; RoPE on sliding-window layers only
- **Positioning:** built for investigating codebases, fixing bugs, implementing features, writing tests; text I/O, reasoning, multi-turn tool use

## Benchmarks (developer-reported, temperature 1.0)
- **Terminal-Bench 2.1:** 54.9%
- **SWE-bench Pro v2:** 89.7%
- **SWE-bench Verified:** 74.2%

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (recursive/flint-v1.0:free) | $0 | $0 | 262,144 | Free endpoint at launch; paid pricing TBA |

## Self-Hosting
- BF16 checkpoint ~80GB; runs on one B300 or H200 per replica with the bundled SGLang kit (serving scripts for both)
- Quantized variants prepared separately for NVIDIA (NVFP4) and Apple Silicon runtimes
- Local engine at github.com/recursive-oss/rec
- Knowledge cutoff June 2026

## Quality Assessment
A strong open-weights coding-agent candidate at the 40B class: 74.2% SWE-bench Verified and 89.7% SWE-bench Pro v2 are competitive with much larger local MoEs (e.g., Qwen3.5-122B-A10B), and the Terminal-Bench 2.1 score (54.9%, with web-retrieval-solved tasks counted as failures) is solid for its size. Apache-2.0, single-GPU serveable (B300/H200 class), and an explicit agent/tool-use design make it a credible self-hosted alternative to API coding agents. Quality score 74 provisional — benchmarks still being independently verified.

## Notes
- Only the `:free` OpenRouter endpoint is live; paid pricing TBA
- No GGUF yet in the main repo (quantized variants hosted separately)
- Added to tracker Oct 22, 2026
