# LLM Model Tracker

Daily-updated tracker of top LLMs. Open and closed source. Last updated: 2026-08-14

## Top 10 Open-Source Models

| # | Model | Org | Category | Context | OR Price | Released | Score | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 | [Kimi K3](open/kimi-k3.md) | Moonshot AI | Frontier | 1M | $3.00+$15.00/M | 2026-07 | 93 | 2.8T MoE. Largest open model ever. 93.5% GPQA, 56% HLE. Beats GLM-5.2 on all coding benchmarks. 91.2 agentic score. Weights LIVE on HuggingFace (moonshotai/Kimi-K3, ~594GB). 1M ctx |
| 2 | [GLM-5.3](open/glm-5.3.md) | Z.ai | Frontier | 1M | $0.00+$0.00/M | 2026-08 | 91 | Same 743B base as GLM-5.2, all gains from post-training. Strongest open-weights coding claim. Terminal-Bench 3.0 4.6->28.3, DeepSWE v1.1 46.2->66.9, CyberGym 84.5%, GDPval-AA v2 1769. Weights ~2 weeks post-security-review; API-only now. Not yet on OpenRouter. |
| 3 | [GLM-5.2](open/glm-5.2.md) | Z.ai | Frontier | 1M | $1.19+$3.74/M | 2026-06 | 90 | Reference model. 753B/40B MoE. 82.8% SWE-bench. Price up +29%/+29% to $0.63/$1.98 on Aug 13 (still extremely volatile week) Price up +89%/+89% to $1.19/$3.74 on Aug 14 (fourth double-digit swing this week; GLM-5.3 same base launched today) |
| 4 | [DeepSeek V4 Pro 0813](open/deepseek-v4-pro-0813.md) | DeepSeek | Frontier | 1M | $0.43+$0.87/M | 2026-08 | 89 | Official GA 0813 build of V4 Pro. 1.6T/49B MoE, MIT open weights. Equal-or-better results than prior V4 Pro at far lower cost ($0.435/$0.87 vs old $1.168/$2.336). Reportedly ahead of Claude Opus 4.8 on Terminal-Bench 2.1 & CyberGym |
| 5 | [DeepSeek V4 Pro](open/deepseek-v4-pro.md) | DeepSeek | Frontier | 1M | $1.17+$2.34/M | 2026-06 | 89 | 1.6T/49B MoE. V4 GA Jul 24. Competes with GPT-5.5 and Claude Opus 4.8 on reasoning. Price up +85%/+85% to $1.17/$2.34 on Aug 12 (second consecutive major hike; DeepSeek price rise underway) |
| 6 | [Z.ai: GLM 5](open/glm-5.md) | z-ai | Frontier | 204K | $0.95+$2.55/M | 2026-03 | 87 | GLM-5 base. 744B/40B MoE. Completion -19% to $2.55 on Jul 20. ctx 202752->204800 on Jul 29 |
| 7 | [Qwen3.8 2.4T A95B](open/qwen3.8-2.4t-a95b.md) | Alibaba | Frontier | 1M | $2.00+$6.00/M | 2026-08 | 86 | 2.4T/95B MoE. First Qwen-Max-class model to open release; post-trained weights on HF (Qwen/Qwen3.8-2.4T-A95B, 712 likes). Built on Qwen3.5 arch. Strong agentic/terminal/long-horizon. qwen3.8-max license. OpenRouter $2/$6. Qwen3.8-Max (cloud, closed) adds vision + non-thinking |
| 8 | [GLM-5.1](open/glm-5.1.md) | Z.ai | Frontier | 204K | $1.40+$4.40/M | 2026-05 | 86 | 744B/40B MoE. ctx 202752->204800 on Jul 29. Price down -32%/-32% to $0.95/$2.99 on Aug 13 (reverses Aug 12 +47% hike) Price up +47%/+47% to $1.40/$4.40 on Aug 14 (follows GLM-5.2's jump; reverses the Aug 13 cut) |
| 9 | [Inkling](open/inkling.md) | Thinking Machines | Frontier | 1M | $0.95+$4.05/M | 2026-07 | 85 | First open model from Thinking Machines (Mira Murati). 975B/41B MoE multimodal (text+image+audio). 1M ctx. 45T tokens. 97.1% AIME, 87.2% GPQA, 77.6% SWE-bench. Now live on OpenRouter at $0.95/$4.05 on Aug 8 (prompt -5%) |
| 10 | [Kimi K2.7 Code](open/kimi-k2.7-code.md) | Moonshot AI | Frontier | 262K | $0.71+$3.50/M | 2026-06 | 85 | 1T/32B MoE coding model. Native multimodal. Price down -4%/-3% to $0.67/$3.40 on Aug 13 Price up +6%/+3% to $0.71/$3.50 on Aug 14 |

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

- [Open-source models (101)](INDEX-OPEN.md)
- [Closed-source models (75)](INDEX-CLOSED.md)
- [Raw CSV data](models.csv)
