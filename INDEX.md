# Open-Source LLM Model Tracker

Daily-updated knowledge base of trending open-source LLMs for self-hosting and API use.

Reference model: **GLM-5.2** (daily driver, $0.91+$2.86/M on OpenRouter, 82.8% SWE-bench, 81.0 Terminal-Bench)

Last scan: 2026-07-05

## Index

Sorted by capability tier. Every model links to its detail file and one third-party validation source.

| Model | Org | Params | Active | Context | OR Price | Self-Host? | Quality | Agentic? (vs GLM-5.2) | Validation |
|---|---|---|---|---|---|---|---|---|---|
| [GLM-5.2](glm-5.2.md) | Z.ai | 753B | 40B | 1M | $0.91+$2.86/M | Q2: 254GB | Frontier coding (82.8% SWE-bench) | **Reference** — best-in-class agentic (81.0 Terminal-Bench) | [HN](https://news.ycombinator.com/item?id=48639840) |
| [DeepSeek V4 Pro](deepseek-v4-pro.md) | DeepSeek | 1.6T | 49B | 1M | $0.43+$0.87/M | IQ2: 465GB | Frontier reasoning, largest open weights | Strong — comparable reasoning, less tool-call tested | [HF](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) |
| [Kimi K2.7 Code](kimi-k2.7-code.md) | Moonshot | ~1T | ~32B | 256K | $0.74+$3.50/M | IQ1: 135GB | Frontier coding specialist | Likely strong — coding agent lineage, not yet benchmarked vs GLM-5.2 | [HF](https://huggingface.co/moonshotai/Kimi-K2.7-Code) |
| [Qwen3.5-397B](qwen3.5-397b.md) | Alibaba | 397B | 17B | 256K | $0.39+$2.45/M | MXFP4: 225GB | Frontier multimodal/reasoning | Promising — multimodal + reasoning, agentic untested | [HF](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) |
| [DeepSeek V4 Flash](deepseek-v4-flash.md) | DeepSeek | 290B | 13.5B | 1M | $0.09+$0.18/M | Q4: 165GB | 85-90% of GLM-5.2 coding at 1/10th cost | Weaker — 55.4 agentic score, good for cost but not GLM-5.2 replacement | [benchlm.ai](https://benchlm.ai/compare/claude-sonnet-4-6-vs-deepseek-v4-flash) |
| [Qwen3-235B](qwen3-235b.md) | Alibaba | 234B | 7B | 262K | $0.09+$0.10/M | Q4: 143GB | ~80% of GLM-5.2 quality, cheapest capable | Moderate — tool-calling supported, untested on long agentic chains | [HF](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) |
| [GPT-OSS-120B](gpt-oss-120b.md) | OpenAI | 120B | 5B | 128K | $0.03+$0.15/M | Q4: 92GB | Solid reasoning, cheapest API | Unknown — OpenAI lineage suggests decent tool-use, untested | [HF](https://huggingface.co/openai/gpt-oss-120b) |
| [GLM-4.5-Air](glm-4.5-air.md) | Z.ai | 106B | 7B | 131K | $0.13+$0.85/M | Q4: 68GB | Good coding/agentic, designed for self-host | Good — same lineage as GLM-5.2, tool-calling native, weaker reasoning | [HF](https://huggingface.co/zai-org/GLM-4.5-Air) |
| [Llama 4 Scout](llama-4-scout.md) | Meta | 109B | 17B | 10M | $0.10+$0.30/M | Q4: ~66GB | Decent reasoning, unique 10M ctx | Moderate — tool-calling supported, 10M ctx is advantage for long sessions | [HF](https://huggingface.co/meta-llama/Llama-4-Scout) |
| [Gemma 4 31B-IT](gemma-4-31b.md) | Google | 31B | 31B | 256K | $0.12+$0.35/M | Q4: 18GB | Solid dense, multimodal | Limited — dense model, weaker on multi-step tool chains | [HF](https://huggingface.co/google/gemma-4-31b-it) |
| [Qwen3-Coder-30B](qwen3-coder-30b.md) | Alibaba | 30B | 3B | 160K | $0.07+$0.27/M | Q4: ~18GB | Coding specialist, very cheap | Not suitable — coding-only, not a general agent | [HF](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) |
| [Qwen3.5-9B](qwen3.5-9b.md) | Alibaba | 9B | 9B | 262K | $0.10+$0.15/M | Q4: ~5GB | Lightweight, edge/always-on | Not suitable — too small for serious agentic work | [HF](https://huggingface.co/Qwen/Qwen3.5-9B) |
