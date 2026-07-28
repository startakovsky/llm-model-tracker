# Qwen3.7 Flash

| Field | Value |
|-------|-------|
| **OpenRouter ID** | `qwen/qwen3.7-flash` |
| **Org** | Alibaba (Qwen Team) |
| **License** | Apache 2.0 (weights pending) |
| **Access** | Closed (API only on OpenRouter) |
| **Context** | 1,000,000 tokens |
| **Pricing** | $0.03/M prompt, $0.13/M completion |
| **Released** | 2026-07-27 |
| **Quality Score** | 75/100 |

## Overview

Qwen3.7 Flash is a vision-language reasoning model from Alibaba's Qwen team, released July 27, 2026. It is the Flash tier of the Qwen3.7 series, positioned below Qwen3.7 Max and Qwen3.7 Plus. At $0.03/$0.13 per million tokens, it is one of the cheapest 1M-context models available, undercutting Qwen3.6 Flash ($0.19/$1.13) by roughly 6x on prompt pricing.

## Key Features

- **Vision-language**: Supports text + image input (multimodal reasoning)
- **1M context window**: Full million-token context
- **Ultra-cheap**: $0.03 prompt / $0.13 completion per million tokens — among the cheapest frontier-tier models
- **Closed-weight API**: Weights not yet released; open weights reportedly pending (evidence of open-weight release circulating on r/LocalLLaMA)

## Benchmarks

No published benchmark scores yet (0/369 on BenchLM as of Jul 27, 2026). Benchmarks expected in coming weeks.

## Cost/Quality Tradeoff

At $0.03/$0.13 per million tokens, Qwen3.7 Flash is ~25x cheaper than GLM-5.2 ($0.77/$2.42) and ~100x cheaper than Claude Opus 5 ($5/$25). If benchmarks land in the 70-78 range (consistent with Qwen3.6 Flash at 78), it would be an exceptional value for multimodal agentic workflows, subagents, and high-volume coding tasks.

## Links

- [OpenRouter](https://openrouter.ai/qwen/qwen3.7-flash)
- [BenchLM](https://benchlm.ai/models/qwen3-7-flash)
