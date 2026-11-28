---
model: AliceAI Foundation 80B-A3B Base
organization: Yandex
license: Apache 2.0
release_date: 2026-11-27
last_updated: 2026-11-28
sources:
  - https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base
  - https://habr.com/ru/companies/yandex/articles/1083300/
  - https://huggingface.co/datasets/yandex/WikiWebFacts
---

# AliceAI Foundation 80B-A3B Base — Yandex

| Field | Value |
|---|---|
| **Org** | Yandex |
| **OpenRouter ID** | not listed (self-host / base weights) |
| **HuggingFace** | [yandex/AliceAI-Foundation-80B-A3B-Base](https://huggingface.co/yandex/AliceAI-Foundation-80B-A3B-Base) |
| **License** | Apache 2.0 (open weights) |
| **Release date** | 2026-11-27 |
| **Pricing** | n/a (no OpenRouter listing yet) |
| **Context** | 262,144 |
| **Category** | Self-hostable (open) |

## Architecture

- **80B total / ~3B active per token** hybrid MoE — first fully-scratch Yandex Alice foundation model.
- Layer scheme `12 × (3 × (KDA → MoE) → 1 × (Gated Attention → MoE))`, 48 layers, hidden 2,048, vocab 129,024.
- MoE: 512 experts, top-10 + 1 shared expert, expert intermediate 512.
- KDA (key-decay attention) blocks + gated attention; 1 MTP layer (multi-token prediction).
- ~163 GB BF16 safetensors, `transformers` + vLLM support, custom `alice_ai` model type.

## Benchmarks

- Yandex reports parity with much larger open models on math/coding/reasoning, and strength in **Russian-language factual knowledge** — published alongside two RU-focused benchmark datasets: [WikiWebFacts](https://huggingface.co/datasets/yandex/WikiWebFacts) and HardMultiQA.
- Claims to outperform larger models — including DeepSeek V4 Flash and Nemotron 3 Super — on several benchmarks (table in the HF model card; mostly RU-context evaluation).

## Quality Assessment

A serious US/EU-parity open base model from Yandex's Alice team — significant for the RU-language market (where most frontier models are weak) and for the trend of Western/European labs shipping open weights. As a **base (pretrain) model with no instruct/chat release yet**, it is not directly usable for agentic or assistant workloads today; treat it as a foundation-model play. Self-hostable on multi-GPU (163GB BF16 → ~160GB VRAM class); expect instruct + quantization follows. Score 66.

- Note: RU/EN bilingual, ~1.9K HF downloads / 427 likes on day 1 — modest traction so far.
