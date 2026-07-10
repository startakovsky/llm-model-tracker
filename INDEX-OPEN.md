# Open-Source LLM Index

30 models. Sorted by API cost (proxy for capability tier).

| Model | Org | Category | Context | OR Price | Released | Self-Host? | Notes |
|---|---|---|---|---|---|---|---|
| [GLM-5 Turbo](open/glm-5-turbo.md) | Z.ai | Frontier | 262K | $1.20+$4.00/M | 2026-04 | Large | Turbo variant |
| [GLM-5V Turbo](open/glm-5v-turbo.md) | Z.ai | Frontier | 202K | $1.20+$4.00/M | 2026-04 | Large | Vision variant |
| [Kimi K2.7 Code](open/kimi-k2.7-code.md) | Moonshot AI | Frontier | 262K | $0.72+$3.49/M | 2026-06 | Large | 1T/32B MoE coding model. Native multimodal |
| [GLM-5.1](open/glm-5.1.md) | Z.ai | Frontier | 202K | $0.97+$3.04/M | 2026-05 | Large | 744B/40B MoE |
| [DeepSeek R1](open/deepseek-r1.md) | DeepSeek | Frontier | 163K | $0.70+$2.50/M | 2026-01 | Large | Reasoning model |
| [Qwen3.5-397B-A17B](open/qwen3.5-397b-a17b.md) | Alibaba | Frontier | 256K | $0.39+$2.45/M | 2026-05 | Large | 397B/17B MoE |
| [Nemotron 3 Ultra](open/nemotron-3-ultra-550b-a55b.md) | NVIDIA | Self-hostable | 1M | $0.50+$2.20/M | 2026-06 | Yes | 550B/55B hybrid Mamba-Transformer MoE. 1M ctx |
| [Qwen3.6-27B](open/qwen3.6-27b.md) | Alibaba | Lightweight | 262K | $0.29+$2.40/M | 2026-06 | Yes | 27B dense |
| [Qwen3.5-122B-A10B](open/qwen3.5-122b-a10b.md) | Alibaba | Self-hostable | 262K | $0.26+$2.08/M | 2026-03 | Yes | 122B/10B MoE. Single 96GB GPU feasible |
| [GLM-5.2](open/glm-5.2.md) | Z.ai | Frontier | 1M | $0.49+$1.54/M | 2026-06 | Large | Reference model. 753B/40B MoE. 82.8% SWE-bench. Price dropped 46% |
| [Qwen3.5-27B](open/qwen3.5-27b.md) | Alibaba | Lightweight | 262K | $0.20+$1.56/M | 2026-03 | Yes | 27B dense |
| [MiniMax M3](open/minimax-m3.md) | MiniMax AI | Frontier | 1M | $0.30+$1.20/M | 2026-05 | Large | 428B MoE multimodal. 1M ctx |
| [DeepSeek V4 Pro](open/deepseek-v4-pro.md) | DeepSeek | Frontier | 1M | $0.43+$0.87/M | 2026-06 | Large | 1.6T/49B MoE |
| [Nex-N2-Pro](open/nex-n2-pro.md) | Nex AGI | Frontier | 262K | $0.25+$1.00/M | 2026-06 | Large | 397B/17B MoE multimodal. Built on Qwen3.5 |
| [Qwen3.6-35B-A3B](open/qwen3.6-35b-a3b.md) | Alibaba | Lightweight | 262K | $0.14+$1.00/M | 2026-06 | Yes | 35B/3B MoE |
| [Qwen3.5-35B-A3B](open/qwen3.5-35b-a3b.md) | Alibaba | Lightweight | 262K | $0.14+$1.00/M | 2026-03 | Yes | 35B/3B MoE |
| [GLM-4.5-Air](open/glm-4.5-air.md) | Z.ai | Self-hostable | 131K | $0.13+$0.85/M | 2025-08 | Yes | 106B/7B MoE. Designed for local |
| [Hy3](open/hy3.md) | Tencent | Self-hostable | 262K | $0.14+$0.58/M | 2026-07 | Yes | 295B/21B MoE. 192 experts. Configurable reasoning |
| [Ring-2.6-1T](open/ring-2.6-1t.md) | inclusionAI | Self-hostable | 262K | $0.07+$0.62/M | 2026-05 | Yes | 1T/63B MoE. Coding agent. 262K ctx |
| [Gemma 4 31B-IT](open/gemma-4-31b-it.md) | Google | Lightweight | 256K | $0.12+$0.35/M | 2026-04 | Yes | 31B dense multimodal |
| [Llama 3.3 70B](open/llama-3.3-70b-instruct.md) | Meta | Lightweight | 131K | $0.10+$0.32/M | 2025-12 | Yes | 70B dense |
| [Nemotron 70B](open/llama-3.1-nemotron-70b-instruct.md) | NVIDIA | Lightweight | 131K | $0.12+$0.30/M | 2025-10 | Yes | 70B dense |
| [Llama 4 Scout](open/llama-4-scout.md) | Meta | Self-hostable | 10M | $0.10+$0.30/M | 2026-04 | Yes | 109B/17B MoE. 10M ctx |
| [Qwen3-Coder-30B-A3B](open/qwen3-coder-30b-a3b-instruct.md) | Alibaba | Lightweight | 160K | $0.07+$0.27/M | 2026-04 | Yes | 30B/3B MoE coding |
| [DeepSeek V4 Flash](open/deepseek-v4-flash.md) | DeepSeek | Self-hostable | 1M | $0.09+$0.18/M | 2026-06 | Yes | 290B/13.5B MoE. 1M ctx |
| [Qwen3.5-9B](open/qwen3.5-9b.md) | Alibaba | Lightweight | 262K | $0.10+$0.15/M | 2026-03 | Yes | 9B dense |
| [GPT-OSS-120B](open/gpt-oss-120b.md) | OpenAI | Self-hostable | 128K | $0.04+$0.18/M | 2026-05 | Yes | 120B/5B MoE. Cheapest API |
| [Qwen3-235B-A22B-Instruct](open/qwen3-235b-a22b-instruct-2507.md) | Alibaba | Self-hostable | 262K | $0.09+$0.10/M | 2026-07 | Yes | 234B/7B MoE. Cheapest capable |
| [Laguna XS 2.1](open/laguna-xs-2.1.md) | Poolside | Lightweight | 262K | $0.06+$0.12/M | 2026-07 | Yes | 33B/3B MoE coding agent |
| [GPT-OSS-20B](open/gpt-oss-20b.md) | OpenAI | Lightweight | 128K | $0.03+$0.14/M | 2026-05 | Yes | 20B/3B MoE |