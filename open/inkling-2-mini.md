---
model: Inkling 2 Mini
organization: Thinking Machines
license: Apache 2.0
release_date: 2026-11-20
last_updated: 2026-11-21
sources:
  - https://huggingface.co/thinkingmachines/inkling-2-mini
  - https://thinkingmachines.ai/news/inkling-2-mini
  - https://openrouter.ai/thinkingmachines/inkling-2-mini
---

# Inkling 2 Mini — Thinking Machines Lab

| Field | Value |
|---|---|
| **Org** | Thinking Machines Lab (Mira Murati) |
| **OpenRouter ID** | `thinkingmachines/inkling-2-mini` |
| **HuggingFace** | [thinkingmachines/inkling-2-mini](https://huggingface.co/thinkingmachines/inkling-2-mini) |
| **License** | Apache 2.0 (open weights) |
| **Release date** | 2026-11-20 |
| **Pricing** | $0.10/$0.40 per M |
| **Context** | 1,048,576 (1M) |
| **Category** | Lightweight (open) |

## Architecture

- **26.4B total / 3.4B active** looped-transformer MoE — the smallest model in the second Inkling generation (after Inkling 2 Small). Middle layers run three times with shared weights, adding reasoning depth per token.
- Multimodal (text+image), ~20GB checkpoint in bf16 — fits on a laptop-class machine.
- Open weights on HuggingFace (Apache 2.0): ~8K downloads / ~1.5K likes at tracking time; unsloth GGUF + llama.cpp support landed the same week (llama.cpp b12600).

## Benchmarks

- Ties Qwen3.8 27B on Artificial Analysis (open-weight local-coding leader at its size).
- Early writeups position it as the local agentic-coding pick: looped reasoning helps on tasks that benefit from iterative re-reading (DeepSWE-style coding); dethrones Qwen3.8 27B for local coding per community tests.
- NVIDIA-family note: not a frontier model — it is a laptop-runnable efficiency play.

## Quality Assessment

~90% of Qwen3.8 27B-class capability at a fraction of the footprint (3.4B active vs 27B dense) — the value is local runnability plus looped reasoning, not raw frontier score. At $0.10/$0.40 it is also the cheapest paid entry point in the Inkling line (~1/3 of Inkling 2 Small's $0.30/$1.00). Score 68: strong Lightweight-tier local coding, not a frontier contender.
