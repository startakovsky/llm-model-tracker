# Open-Source LLM Model Tracker

Daily-updated knowledge base of trending open-source LLMs for self-hosting and API use.

Reference model: **GLM-5.2** (daily driver, $0.63+$1.98/M on OpenRouter, 82.8% SWE-bench, 81.0 Terminal-Bench)

Last scan: 2026-07-09

## Index

Sorted by capability tiers. Every model links to its detail file and one third-party validation source.

| Model | Org | Params | Active | Context | OR Price | Self-Host? | Quality | Agentic? (vs GLM-5.2) | Validation |
|---|---|---|---|---|---|---|---|---|---|
| [GLM-5.2](glm-5.2.md) | Z.ai | 753B | 40B | 1M | $0.63+$1.98/M | Q2: 254GB | Frontier coding (82.8% SWE-bench) | **Reference** — best-in-class agentic (81.0 Terminal-Bench) | [HN](https://news.ycombinator.com/item?id=48639840) |
| [DeepSeek V4 Pro](deepseek-v4-pro.md) | DeepSeek | 1.6T | 49B | 1M | $0.43+$0.87/M | IQ2: 465GB | Frontier reasoning, largest open weights | Strong — comparable reasoning, less tool-call tested | [HF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |
| [Nex-N2-Pro](nex-n2-pro.md) | Nex AGI | 397B | 17B | 262K | $0.25+$1.00/M | FP8: ~397GB | Frontier agentic (80.8 SWE-bench, 75.3 Terminal-Bench) | **Near GLM-5.2** — 93% Terminal-Bench, 98% SWE-bench, 2.5x cheaper | [HF](https://huggingface.co/nex-agi/Nex-N2-Pro) |
| [LongCat-2.0](longcat-2.0.md) | Meituan | 1.6T | 48B | 1M | Not on OR | FP8: 1.6TB | Frontier agentic coding (59.5 SWE-bench Pro, 70.8 Terminal-Bench) | Promising — 70.8 Terminal-Bench (~87% of GLM-5.2), 1M ctx, MIT license, not yet on OR | [AIWeekly](https://aiweekly.co/alerts/meituan-open-sources-16t-parameter-longcat-20-moe-model) |
| [Kimi K2.7 Code](kimi-k2.7-code.md) | Moonshot | ~1T | ~32B | 256K | $0.74+$3.50/M | IQ1: 135GB | Frontier coding specialist | Likely strong — coding agent lineage, not yet benchmarked vs GLM-5.2 | [HF](https://huggingface.co/moonshotai/Kimi-K2.7-Code) |
| [MiniMax M3](minimax-m3.md) | MiniMax | 428B | 23B | 1M | $0.30+$1.20/M | FP8: ~428GB | Frontier multimodal (59.0 SWE-bench Pro, beats GPT-5.5) | Promising — multimodal + 1M ctx, Terminal-Bench not reported | [Digg](https://digg.com/tech/aqmz169n) |
| [Nemotron 3 Ultra](nemotron-3-ultra.md) | NVIDIA | 550B | 55B | 1M | $0.50+$2.20/M | NVFP4: 345GB | Top US open-weight (AA idx 48, SWE-bench 65-70%) | Decent — SWE-bench 65-70% vs GLM-5.2's 82.8%, cheaper but trails on coding | [AIWeekly](https://aiweekly.co/alerts/nvidia-ships-nemotron-3-ultra-a-550b-open-moe-for-agents) |
| [Qwen3.5-397B](qwen3.5-397b.md) | Alibaba | 397B | 17B | 256K | $0.39+$2.45/M | MXFP4: 225GB | Frontier multimodal/reasoning | Promising — multimodal + reasoning, agentic untested | [HF](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) |
| [Ring-2.6-1T](ring-2.6-1t.md) | inclusionAI | 1T | 63B | 262K | $0.07+$0.62/M | Pre-quant: ~625GB | Strong agentic (92% Tau²-Bench, 74 SWE-bench) | Cost-alt — Tau²-Bench 92% excellent, SWE-bench 74 trails GLM-5.2, 9x cheaper | [Modelgrep](https://modelgrep.com/models/inclusionai/ring-2.6-1t) |
| [Tencent Hy3](tencent-hy3.md) | Tencent | 295B | 21B | 256K | $0.14+$0.58/M | FP8: 295GB | ~88% of GLM-5.2 agentic (71.7 Terminal-Bench) | Viable cost alt — 71.7 Terminal-Bench, stable across scaffoldings, ~1/4th GLM-5.2 cost | [NVIDIA Forum](https://forums.developer.nvidia.com/t/new-2x-spark-king-tencent-hy3-just-released/375718) |
| [DeepSeek V4 Flash](deepseek-v4-flash.md) | DeepSeek | 284B | 13B | 1M | $0.09+$0.18/M | Q4: 155GB | 85-90% of GLM-5.2 coding at 1/10th cost | Weaker — 55.4 agentic score, good for cost but not GLM-5.2 replacement | [benchlm.ai](https://benchlm.ai/compare/claude-sonnet-4-6-vs-deepseek-v4-flash) |
| [Qwen3-235B](qwen3-235b.md) | Alibaba | 234B | 7B | 262K | $0.09+$0.10/M | Q4: 143GB | ~80% of GLM-5.2 quality, cheapest capable | Moderate — tool-calling supported, untested on long agentic chains | [HF](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) |
| [Qwen3.5-122B](qwen3.5-122b.md) | Alibaba | 122B | 10B | 256K | $0.26+$2.08/M | Q4: 73GB | ~95% of Qwen3.5-397B, best self-host MoE | Moderate — tool-calling supported, untested on long agentic chains | [HF](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) |
| [Qwen3.6-27B](qwen3.6-27b.md) | Alibaba | 27B | 27B | 256K | $0.29+$2.40/M | Q4: 18GB | 77.2% SWE-bench dense, runs on 18GB RAM | Local fallback — 59.3 Terminal-Bench (73% of GLM-5.2), best local coding model for size | [Unsloth](https://unsloth.ai/docs/models/qwen3.6) |
| [Qwen3.6-35B-A3B](qwen3.6-35b-a3b.md) | Alibaba | 35B | 3B | 256K | $0.14+$1.00/M | Q4: 22GB | 73.4% SWE-bench, 3B active, fast local MoE | Local coding only — 51.5 Terminal-Bench (64% of GLM-5.2), fast on consumer HW | [Unsloth](https://unsloth.ai/docs/models/qwen3.6) |
| [Laguna XS 2.1](laguna-xs-2.1.md) | Poolside | 33B | 3B | 262K | $0.06+$0.12/M | Q4: 18GB | 70.9% SWE-bench Verified, runs on 36GB RAM | Local coding only — Terminal-Bench 37.5% far below GLM-5.2's 81.0 | [HF](https://huggingface.co/poolside/Laguna-XS-2.1) |
| [North Mini Code](north-mini-code.md) | Cohere | 30B | 3B | 256K | Free on OR | FP8: 1×H100 | 67.6% SWE-bench, Apache 2.0, sovereign | Local coding only — Terminal-Bench 36.0%, too small for full agentic | [Cohere Blog](https://cohere.com/blog/north-mini-code) |
| [GPT-OSS-120B](gpt-oss-120b.md) | OpenAI | 120B | 5B | 128K | $0.03+$0.15/M | Q4: 92GB | Solid reasoning, cheapest API | Unknown — OpenAI lineage suggests decent tool-use, untested | [HF](https://huggingface.co/openai/gpt-oss-120b) |
| [GLM-4.5-Air](glm-4.5-air.md) | Z.ai | 106B | 7B | 131K | $0.13+$0.85/M | Q4: 68GB | Good coding/agentic, designed for self-host | Good — same lineage as GLM-5.2, tool-calling native, weaker reasoning | [HF](https://huggingface.co/zai-org/GLM-4.5-Air) |
| [Llama 4 Scout](llama-4-scout.md) | Meta | 109B | 17B | 10M | $0.10+$0.30/M | Q4: ~66GB | Decent reasoning, unique 10M ctx | Moderate — tool-calling supported, 10M ctx is advantage for long sessions | [HF](https://huggingface.co/meta-llama/Llama-4-Scout) |
| [Gemma 4 31B-IT](gemma-4-31b.md) | Google | 31B | 31B | 256K | $0.12+$0.35/M | Q4: 18GB | Solid dense, multimodal | Limited — dense model, weaker on multi-step tool chains | [HF](https://huggingface.co/google/gemma-4-31b-it) |
| [Qwen3.5-27B](qwen3.5-27b.md) | Alibaba | 27B | 27B | 256K | $0.20+$1.56/M | Q4: 16GB | Best dense 27B (superseded by Qwen3.6-27B) | Limited — too small for serious agentic work, good for local vision tasks | [HF](https://huggingface.co/Qwen/Qwen3.5-27B) |
| [Qwen3-Coder-30B](qwen3-coder-30b.md) | Alibaba | 30B | 3B | 160K | $0.07+$0.27/M | Q4: ~18GB | Coding specialist, very cheap | Not suitable — coding-only, not a general agent | [HF](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) |
| [GPT-OSS-20B](gpt-oss-20b.md) | OpenAI | 20B | 3B | 128K | $0.03+$0.14/M | Q4: 11GB | Strong for size, edge deployment | Not suitable — too small for serious agentic work | [HF](https://huggingface.co/openai/gpt-oss-20b) |
| [Qwen3.5-9B](qwen3.5-9b.md) | Alibaba | 9B | 9B | 262K | $0.10+$0.15/M | Q4: ~5GB | Lightweight, edge/always-on | Not suitable — too small for serious agentic work | [HF](https://huggingface.co/Qwen/Qwen3.5-9B) |
