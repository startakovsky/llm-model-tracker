# LLM Model Tracker

Daily-updated tracker of top LLMs. Open and closed source. Last updated: 2026-08-01

## Top 10 Open-Source Models

| # | Model | Org | Category | Context | OR Price | Released | Score | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | [Kimi K3](open/kimi-k3.md) | Moonshot AI | Frontier | 1M | $3.00+$15.00/M | 2026-07 | 93 | 2.8T MoE. Largest open model ever. 93.5% GPQA, 56% HLE. Beats GLM-5.2 on all coding benchmarks. 91.2 agentic score. Weights LIVE on HuggingFace (moonshotai/Kimi-K3, ~594GB). 1M ctx |
| 2 | [GLM-5.2](open/glm-5.2.md) | Z.ai | Frontier | 1M | $0.76+$2.39/M | 2026-06 | 90 | Reference model. 753B/40B MoE. 82.8% SWE-bench. Price -21%/-21% to $0.76/$2.39 on Aug 1 (reverses Jul 30 hike; now cheapest since tracking began) |
| 3 | [DeepSeek V4 Pro](open/deepseek-v4-pro.md) | DeepSeek | Frontier | 1M | $0.43+$0.87/M | 2026-06 | 89 | 1.6T/49B MoE. V4 GA Jul 24. Competes with GPT-5.5 and Claude Opus 4.8 on reasoning |
| 4 | [Z.ai: GLM 5](open/glm-5.md) | z-ai | Frontier | 204K | $0.95+$2.55/M | 2026-03 | 87 | GLM-5 base. 744B/40B MoE. Completion -19% to $2.55 on Jul 20. ctx 202752->204800 on Jul 29 |
| 5 | [Qwen3.8 Max Preview](open/qwen3.8-max-preview.md) | Alibaba | Frontier | 1M | $0.00+$0.00/M | 2026-07 | 86 | 2.4T param multimodal MoE. First Qwen >1T multimodal (text+image+video+doc). Qwen says "second only to Fable 5". Outperforms Qwen3.7-Max in coding. Open weights promised by Jul 27. Preview via Token Plan/Qoder at 10% price. Not yet on OpenRouter. Benchmarks pending |
| 6 | [GLM-5.1](open/glm-5.1.md) | Z.ai | Frontier | 204K | $0.97+$3.04/M | 2026-05 | 86 | 744B/40B MoE. ctx 202752->204800 on Jul 29 |
| 7 | [Inkling](open/inkling.md) | Thinking Machines | Frontier | 1M | $1.00+$4.05/M | 2026-07 | 85 | First open model from Thinking Machines (Mira Murati). 975B/41B MoE multimodal (text+image+audio). 1M ctx. 45T tokens. 97.1% AIME, 87.2% GPQA, 77.6% SWE-bench. Now live on OpenRouter at $1.00/$4.05 |
| 8 | [Kimi K2.7 Code](open/kimi-k2.7-code.md) | Moonshot AI | Frontier | 262K | $0.73+$3.50/M | 2026-06 | 85 | 1T/32B MoE coding model. Native multimodal. Prompt -3% to $0.73 on Jul 27 (completion steady at $3.50) |
| 9 | [LongCat-2.0](open/longcat-2.0.md) | Meituan | Frontier | 1M | $0.30+$1.20/M | 2026-07 | 84 | 1.6T/48B MoE. LongCat Sparse Attention. ~1M ctx. Trained on AI ASIC superpods. 35T tokens. MIT license. LIVE on OpenRouter at $0.30/$1.20 |
| 10 | [Qwen: Qwen3 VL 235B A22B Thinking](open/qwen3-vl-235b-a22b-thinking.md) | qwen | Frontier | 131K | $0.40+$4.00/M | 2026-05 | 84 | Qwen3 VL 235B thinking. Price +54% to $0.40/$4.00 on Jul 29 |

## Top 10 Closed-Source Models

| # | Model | Org | Context | OR Price | Released | Score | Notes |
|---|---|---|---|---|---|---|---|
| 1 | [GPT-5.5 Pro](closed/gpt-5.5-pro.md) | OpenAI | 1M | $30.00+$180.00/M | 2026-06 | 98 | Pro reasoning |
| 2 | [Claude Opus 5](closed/claude-opus-5.md) | Anthropic | 1M | $5.00+$25.00/M | 2026-07 | 96 | New Anthropic flagship (Jul 24). Approaches Fable 5 capability at half the price ($5/$25, same as Opus 4.8). Default for Claude Max. Effort dial. Most-aligned Opus. 1M ctx. 4th Claude 5 model in <2 months |
| 3 | [Claude Opus 4.8 Fast](closed/claude-opus-4.8-fast.md) | Anthropic | 1M | $10.00+$50.00/M | 2026-06 | 96 | Fast Opus |
| 4 | [Claude Opus 5 Fast](closed/claude-opus-5-fast.md) | Anthropic | 1M | $10.00+$50.00/M | 2026-07 | 95 | Fast-mode variant of Opus 5 (Jul 24). Identical capabilities, higher output speed at 2x pricing. 1M ctx |
| 5 | [GPT-5.5](closed/gpt-5.5.md) | OpenAI | 1M | $5.00+$30.00/M | 2026-06 | 95 | Flagship |
| 6 | [Claude Opus 4.8](closed/claude-opus-4.8.md) | Anthropic | 1M | $5.00+$25.00/M | 2026-06 | 95 | Flagship Opus |
| 7 | [GPT-5.4 Pro](closed/gpt-5.4-pro.md) | OpenAI | 1M | $30.00+$180.00/M | 2026-05 | 94 | Pro reasoning |
| 8 | [Claude Opus 4.7 Fast](closed/claude-opus-4.7-fast.md) | Anthropic | 1M | $30.00+$150.00/M | 2026-05 | 94 | Fast Opus |
| 9 | [Fugu Ultra](closed/fugu-ultra.md) | Sakana AI | 1M | $5.00+$30.00/M | 2026-06 | 93 | Multi-agent orchestration engine. Dynamically routes to frontier models. 93.2 LiveCodeBench, 95.5 GPQA, 73.7 SWE-bench Pro. Matches Fable 5 without it in pool |
| 10 | [GPT-5.6 Sol Pro](closed/gpt-5.6-sol-pro.md) | OpenAI | 1M | $5.00+$30.00/M | 2026-06 | 93 | Solid reasoning |

## Full Index

- [Open-source models (94)](INDEX-OPEN.md)
- [Closed-source models (71)](INDEX-CLOSED.md)
- [Raw CSV data](models.csv)
