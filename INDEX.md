# Open-Source LLM Model Tracker

Daily-updated knowledge base of open-source LLMs for self-hosting and API use.

## Structure

Each model has a markdown file: `<model-name>.md`

Fields tracked per model:
- Name, org, license, release date
- Architecture (params, active params, MoE/dense, context length)
- Self-hosting: GGUF sizes, FP8/FP4 sizes, min RAM/VRAM
- API providers: OpenRouter pricing, direct API, other providers
- Quality: benchmark scores (coding, reasoning, agentic, math)
- Speed: tokens/sec on various hardware configs
- Last updated date
- Sources (URLs)

## Index

| Model | Org | Params | Active | Context | License | Self-Host? | OR? |
|---|---|---|---|---|---|---|---|
| GLM-5.2 | Z.ai | 753B | 40B | 1M | MIT | Yes (Q2: 254GB) | Yes ($0.91+$2.86/M) |
| GLM-4.5-Air | Z.ai | 106B | 7B | 131K | MIT | Yes (Q4: 68GB) | Yes ($0.13+$0.85/M) |
| DeepSeek V4 Flash | DeepSeek | 290B | 13.5B | 1M | MIT | Yes (Q4: 165GB) | Yes ($0.09+$0.18/M) |
| DeepSeek V4 Pro | DeepSeek | 1.6T | 49B | 1M | MIT | Yes (IQ2: 465GB) | Yes |
| Qwen3-235B-A22B-Instruct | Alibaba | 234B | 7B | 262K | Apache 2.0 | Yes (Q4: 143GB) | Yes ($0.09+$0.10/M) |
| Qwen3-Coder-30B-A3B | Alibaba | 30B | 3B | 160K | Apache 2.0 | Yes (Q4: ~18GB) | Yes ($0.07+$0.27/M) |
| Qwen3.5-9B | Alibaba | 9B | 9B | 262K | Apache 2.0 | Yes (Q4: ~5GB) | Yes ($0.10+$0.15/M) |
| Llama 4 Scout | Meta | 109B | 17B | 10M | Llama 4 license | Yes (Q4: ~66GB) | Yes ($0.10+$0.30/M) |
