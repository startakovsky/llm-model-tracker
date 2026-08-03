# Open-Source LLM Index

95 models. Sorted by quality score.

| Model | Org | Category | Context | OR Price | Released | Score | Self-Host? | Notes |
|---|---|---|---|---|---|---|---|---|
| [Kimi K3](open/kimi-k3.md) | Moonshot AI | Frontier | 1M | $3.00+$15.00/M | 2026-07 | 93 | Large | 2.8T MoE. Largest open model ever. 93.5% GPQA, 56% HLE. Beats GLM-5.2 on all coding benchmarks. 91.2 agentic score. Weights LIVE on HuggingFace (moonshotai/Kimi-K3, ~594GB). 1M ctx |
| [GLM-5.2](open/glm-5.2.md) | Z.ai | Frontier | 1M | $0.63+$1.98/M | 2026-06 | 90 | Large | Reference model. 753B/40B MoE. 82.8% SWE-bench. Price +121%/+121% to $0.63/$1.98 on Aug 3 (rebounds from Aug 2 crash; back near Jul 30 levels) |
| [DeepSeek V4 Pro](open/deepseek-v4-pro.md) | DeepSeek | Frontier | 1M | $0.43+$0.87/M | 2026-06 | 89 | Large | 1.6T/49B MoE. V4 GA Jul 24. Competes with GPT-5.5 and Claude Opus 4.8 on reasoning |
| [Z.ai: GLM 5](open/glm-5.md) | z-ai | Frontier | 204K | $0.95+$2.55/M | 2026-03 | 87 | Large | GLM-5 base. 744B/40B MoE. Completion -19% to $2.55 on Jul 20. ctx 202752->204800 on Jul 29 |
| [GLM-5.1](open/glm-5.1.md) | Z.ai | Frontier | 204K | $0.97+$3.04/M | 2026-05 | 86 | Large | 744B/40B MoE. ctx 202752->204800 on Jul 29 |
| [Inkling](open/inkling.md) | Thinking Machines | Frontier | 1M | $1.00+$4.05/M | 2026-07 | 85 | Large | First open model from Thinking Machines (Mira Murati). 975B/41B MoE multimodal (text+image+audio). 1M ctx. 45T tokens. 97.1% AIME, 87.2% GPQA, 77.6% SWE-bench. Now live on OpenRouter at $1.00/$4.05 |
| [Kimi K2.7 Code](open/kimi-k2.7-code.md) | Moonshot AI | Frontier | 262K | $0.73+$3.50/M | 2026-06 | 85 | Large | 1T/32B MoE coding model. Native multimodal. Prompt -3% to $0.73 on Jul 27 (completion steady at $3.50) |
| [Qwen3.8 Max](open/qwen3.8-max-preview.md) | Alibaba | Frontier | 1M | $2.00+$6.00/M | 2026-08 | 84 | Large | 2.4T param multimodal MoE. First Qwen >1T multimodal (text+image+video+doc). Officially launched Aug 2 (preview Jul 19). Nikkei: falls short of 'second only to Fable 5' claim in benchmarks. Priced $2/$6 (below Kimi K3 $3/$15). Open weights promised next week. Not yet on OpenRouter |
| [LongCat-2.0](open/longcat-2.0.md) | Meituan | Frontier | 1M | $0.30+$1.20/M | 2026-07 | 84 | Large | 1.6T/48B MoE. LongCat Sparse Attention. ~1M ctx. Trained on AI ASIC superpods. 35T tokens. MIT license. LIVE on OpenRouter at $0.30/$1.20 |
| [Qwen: Qwen3 VL 235B A22B Thinking](open/qwen3-vl-235b-a22b-thinking.md) | qwen | Frontier | 131K | $0.98+$3.95/M | 2026-05 | 84 | Large | Qwen3 VL 235B thinking. Prompt +145% to $0.98 on Aug 3 (completion steady $3.95) |
| [GLM-5 Turbo](open/glm-5-turbo.md) | Z.ai | Frontier | 202K | $1.20+$4.00/M | 2026-04 | 84 | Large | Turbo variant |
| [DeepSeek R1](open/deepseek-r1.md) | DeepSeek | Frontier | 163K | $0.70+$2.50/M | 2026-01 | 84 | Large | Reasoning model |
| [Qwen3.5-397B-A17B](open/qwen3.5-397b-a17b.md) | Alibaba | Frontier | 262K | $0.39+$2.34/M | 2026-05 | 83 | Large | 397B/17B MoE. Price drop: prompt -13%, completion -22% |
| [Kimi K2.6](open/kimi-k2.6.md) | Moonshot AI | Frontier | 262K | $0.60+$3.41/M | 2026-04 | 83 | Large | 1T/32B MoE multimodal coding model. Next-gen from K2.7. Native coding in Python/Rust/Go. Price: prompt -7% to $0.60, completion +25% to $3.41 on Aug 1 |
| [GLM-5V Turbo](open/glm-5v-turbo.md) | Z.ai | Frontier | 202K | $1.20+$4.00/M | 2026-04 | 83 | Large | Vision variant |
| [DeepSeek V4 Flash 0731](open/deepseek-v4-flash-0731.md) | DeepSeek | Self-hostable | 1M | $0.09+$0.18/M | 2026-07 | 82 | Yes | 284B/13B MoE re-post-trained revision. 1M ctx. Non-surge pricing ($0.09/$0.18 vs base $0.14/$0.28). Coding/reasoning/agent workflows. ~10x cheaper than GLM-5.2 |
| [Laguna S 2.1](open/laguna-s-2.1.md) | Poolside | Frontier | 1M | $0.09+$0.18/M | 2026-07 | 82 | Large | 118B/8B MoE coding agent. 70.2% Terminal-Bench 2.1. 40.4% DeepSWE. Open weights (OpenMDW-1.1). 1M ctx. Forbes: most capable open model in the West in 118B class. GGUF/FP8/INT4 on HF. 327 likes in 1 day. Price -10%/-10% to $0.09/$0.18 on Aug 1 |
| [Qwen: Qwen3 235B A22B Thinking 2507](open/qwen3-235b-a22b-thinking-2507.md) | qwen | Frontier | 262K | $0.23+$2.30/M | 2026-07 | 82 | Large | Qwen3 235B thinking July 2026. Price -23%/-23% to $0.23/$2.30 on Aug 1 (reverses Jul 20 doubling) |
| [DeepSeek V4 Flash](open/deepseek-v4-flash.md) | DeepSeek | Self-hostable | 1M | $0.14+$0.28/M | 2026-06 | 82 | Yes | 284B/13B MoE. 1M ctx. V4 GA Jul 24. Base ID still at surge pricing $0.14/$0.28; cheaper 0731 snapshot ($0.09/$0.18) now live |
| [MoonshotAI: Kimi K2 Thinking](open/kimi-k2-thinking.md) | moonshotai | Frontier | 262K | $0.60+$2.50/M | 2026-05 | 82 | Large | Thinking variant of Kimi K2 |
| [Mistral: Mistral Large 3 2512](open/mistral-large-2512.md) | mistralai | Frontier | 262K | $0.50+$1.50/M | 2026-05 | 82 | Large | Mistral Large Dec 2026 |
| [Qwen: Qwen3 VL 235B A22B Instruct](open/qwen3-vl-235b-a22b-instruct.md) | qwen | Frontier | 262K | $0.21+$1.90/M | 2026-05 | 82 | Large | Qwen3 VL 235B. Vision-language. ctx 131K->262K on Jul 29 |
| [DeepSeek: DeepSeek V3.2 Exp](open/deepseek-v3.2-exp.md) | deepseek | Self-hostable | 163K | $0.27+$0.41/M | 2026-05 | 81 | Yes | V3.2 experimental |
| [Ornith-1.0-397B](open/ornith-1.0-397b.md) | Unsloth | Self-hostable | 262K | $0.00+$0.00/M | 2026-07 | 80 | Yes | 397B/17B MoE agentic coding. Self-improving RL (joint scaffold+solution optimization). Post-trained on Gemma 4 + Qwen3.5. MIT license. Terminal-Bench 2.1 77.5-78.2 (near GLM-5.2's 81). SWE-bench/NL2Repo/OpenClaw SOTA among open models of comparable size. Not on OpenRouter. GGUF quants on HF |
| [Inkling Small](open/inkling-small.md) | Thinking Machines | Frontier | 524K | $0.50+$1.20/M | 2026-07 | 80 | Large | Smaller Inkling variant from Thinking Machines (Mira Murati). 524K ctx (half of flagship 1M). Apache 2.0 open weights. Cost-efficient tier of the 975B/41B MoE family. Now live on OpenRouter at $0.50/$1.20 |
| [Nemotron 3 Ultra](open/nemotron-3-ultra-550b-a55b.md) | NVIDIA | Self-hostable | 512K | $0.60+$3.60/M | 2026-06 | 80 | Yes | 550B/55B hybrid Mamba-Transformer MoE. Price +20%/+64% to $0.60/$3.60 on Aug 2 (reverses Aug 1 drop) |
| [Nous: Hermes 4 405B](open/hermes-4-405b.md) | nousresearch | Frontier | 131K | $1.00+$3.00/M | 2026-06 | 80 | Large | Hermes 4 405B. Fine-tuned Llama 405B |
| [DeepSeek: DeepSeek V3.2](open/deepseek-v3.2.md) | deepseek | Self-hostable | 163K | $0.27+$0.40/M | 2026-05 | 80 | Yes | V3.2 update. 671B/37B MoE |
| [Amazon: Nova Premier 1.0](open/nova-premier-v1.md) | amazon | Frontier | 1M | $2.50+$12.50/M | 2026-05 | 80 | Large | Nova Premier. 1M ctx |
| [MoonshotAI: Kimi K2.5](open/kimi-k2.5.md) | moonshotai | Frontier | 262K | $0.57+$2.85/M | 2026-03 | 80 | Large | 1T/32B MoE. Predecessor to K2.6 |
| [Qwen3-235B-A22B-Instruct](open/qwen3-235b-a22b-2507.md) | Alibaba | Self-hostable | 262K | $0.15+$0.60/M | 2026-07 | 78 | Yes | 234B/7B MoE. Price +66%/+9% to $0.15/$0.60 on Aug 3 (reverses prior low) |
| [Nex-N2-Pro](open/nex-n2-pro.md) | Nex AGI | Frontier | 262K | $0.25+$1.00/M | 2026-06 | 78 | Large | 397B/17B MoE multimodal. Built on Qwen3.5 |
| [Z.ai: GLM 4.7](open/glm-4.7.md) | z-ai | Self-hostable | 204K | $0.40+$1.75/M | 2026-05 | 78 | Yes | GLM-4.7. Mid-tier Z.ai. ctx 202752->204800 on Jul 29 |
| [Qwen: Qwen3 Coder 480B A35B](open/qwen3-coder.md) | qwen | Self-hostable | 262K | $0.30+$1.00/M | 2026-05 | 78 | Yes | Qwen3 Coder base. OpenRouter ctx 1M->262K on Jul 29 |
| [DeepSeek: DeepSeek V3.1](open/deepseek-chat-v3.1.md) | deepseek | Self-hostable | 163K | $0.25+$0.95/M | 2026-03 | 78 | Yes | V3.1 chat |
| [Hy3](open/hy3.md) | Tencent | Self-hostable | 262K | $0.13+$0.53/M | 2026-07 | 77 | Yes | 295B/21B MoE. 192 experts. Configurable reasoning. Price down -30%/-27.5% on Jul 21, further -6%/-9% on Jul 24 |
| [DeepSeek: DeepSeek V3.1 Terminus](open/deepseek-v3.1-terminus.md) | deepseek | Self-hostable | 163K | $0.27+$1.00/M | 2026-03 | 77 | Yes | V3.1 Terminus. ctx 131K->163K on Jul 29 |
| [MiniMax M3](open/minimax-m3.md) | MiniMax AI | Frontier | 1M | $0.30+$1.20/M | 2026-05 | 76 | Large | 428B MoE multimodal. 1M ctx |
| [Laguna M.1](open/laguna-m.1.md) | Poolside | Frontier | 262K | $0.20+$0.40/M | 2026-04 | 76 | Large | Flagship coding agent model. Complex SWE tasks. 256K ctx |
| [Baidu: ERNIE 4.5 VL 424B A47B ](open/ernie-4.5-vl-424b-a47b.md) | baidu | Frontier | 123K | $0.42+$1.25/M | 2026-04 | 76 | Large | Ernie 4.5 VL. 424B/47B MoE multimodal. ctx 131K->123K on Jul 30 |
| [Z.ai: GLM 4.6](open/glm-4.6.md) | z-ai | Self-hostable | 204K | $0.50+$2.00/M | 2026-02 | 76 | Yes | GLM-4.6. ctx 202752->204800 on Jul 29 |
| [Qwen3.5-122B-A10B](open/qwen3.5-122b-a10b.md) | Alibaba | Self-hostable | 262K | $0.40+$3.20/M | 2026-03 | 75 | Yes | 122B/10B MoE. Single 96GB GPU feasible. Price +54%/+54% to $0.40/$3.20 on Aug 3 |
| [Tencent: Hy3 preview](open/hy3-preview.md) | tencent | Self-hostable | 262K | $0.06+$0.21/M | 2026-07 | 74 | Yes | Hy3 preview. 295B/21B MoE |
| [Qwen: Qwen3 Next 80B A3B Thinking](open/qwen3-next-80b-a3b-thinking.md) | qwen | Self-hostable | 262K | $0.15+$1.20/M | 2026-06 | 74 | Yes | Qwen3 Next 80B thinking. Price +54% to $0.15/$1.20 on Jul 29 (reverses Jul 25 drop) |
| [Meta: Llama 4 Maverick](open/llama-4-maverick.md) | meta-llama | Self-hostable | 1M | $0.20+$0.80/M | 2026-04 | 74 | Yes | Llama 4 Maverick. 400B/17B MoE. 1M ctx |
| [Z.ai: GLM 4.6V](open/glm-4.6v.md) | z-ai | Self-hostable | 131K | $0.30+$0.90/M | 2026-02 | 74 | Yes | Vision variant of GLM-4.6 |
| [Qwen: Qwen3 Coder Flash](open/qwen3-coder-flash.md) | qwen | Frontier | 1M | $0.20+$0.97/M | 2026-06 | 73 | Large | Qwen3 Coder Flash. 1M ctx. Closed-weight API |
| [Z.ai: GLM 4.5](open/glm-4.5.md) | z-ai | Self-hostable | 131K | $0.60+$2.20/M | 2025-11 | 73 | Yes | GLM-4.5 base |
| [Qwen: Qwen3 Next 80B A3B Instruct](open/qwen3-next-80b-a3b-instruct.md) | qwen | Self-hostable | 262K | $0.10+$1.10/M | 2026-06 | 72 | Yes | Qwen3 Next 80B/3B. Price -33%/-8% to $0.10/$1.10 on Jul 25 |
| [ByteDance Seed: Seed-2.0-Lite](open/seed-2.0-lite.md) | bytedance-seed | Frontier | 262K | $0.25+$2.00/M | 2026-06 | 72 | Large | Seed 2.0 Lite. 262K ctx |
| [Ring-2.6-1T](open/ring-2.6-1t.md) | inclusionAI | Self-hostable | 262K | $0.07+$0.62/M | 2026-05 | 72 | Yes | 1T/63B MoE. Coding agent. 262K ctx |
| [Mistral: Devstral 2 2512](open/devstral-2512.md) | mistralai | Self-hostable | 262K | $0.40+$2.00/M | 2026-05 | 72 | Yes | Devstral coding model |
| [Ling-2.6-1T](open/ling-2.6-1t.md) | inclusionAI | Self-hostable | 262K | $0.07+$0.62/M | 2026-04 | 72 | Yes | 1T/63B MoE instant model. Fast execution for agents. Sister to Ring-2.6-1T |
| [Llama 4 Scout](open/llama-4-scout.md) | Meta | Self-hostable | 1M | $0.10+$0.30/M | 2026-04 | 72 | Yes | 109B/17B MoE. OpenRouter ctx corrected 10M->1.31M on Jul 29 |
| [Step 3.5 Flash](open/step-3.5-flash.md) | StepFun | Self-hostable | 262K | $0.10+$0.30/M | 2026-01 | 72 | Yes | 196B/11B MoE. StepFun most capable open-source model. Apache 2.0. 828 HF likes. 123K downloads. 262K ctx. Predecessor to closed Step 3.7 Flash |
| [Nemotron 3 Super](open/nemotron-3-super-120b-a12b.md) | NVIDIA | Self-hostable | 1M | $0.09+$0.40/M | 2026-06 | 70 | Yes | 120B/12B hybrid Mamba-Transformer MoE. 1M ctx. Fully open weights/datasets/recipes. Price to $0.085/$0.40 on Jul 25 (p +6%, c -11%) |
| [Mistral: Codestral 2508](open/codestral-2508.md) | mistralai | Lightweight | 256K | $0.30+$0.90/M | 2026-04 | 70 | Yes | Codestral coding model |
| [Qwen3 Coder Next](open/qwen3-coder-next.md) | Alibaba | Self-hostable | 262K | $0.12+$0.80/M | 2026-02 | 70 | Yes | 80B/3B MoE coding model. Open weights for local dev workflows. 262K ctx. Price -33%/-11% to $0.12/$0.80 on Jul 29 (reverses Jul 28 jump) |
| [GLM-4.5-Air](open/glm-4.5-air.md) | Z.ai | Self-hostable | 131K | $0.13+$0.85/M | 2025-08 | 70 | Yes | 106B/7B MoE. Designed for local |
| [Ling 3.0 Flash](open/ling-3.0-flash.md) | inclusionAI | Self-hostable | 262K | $0.00+$0.00/M | 2026-07 | 68 | Yes | 124B/5.1B MoE. Hybrid-reasoning. Production-scale agents. Free on OpenRouter. Open weights on HF/ModelScope |
| [ByteDance Seed: Seed-2.0-Mini](open/seed-2.0-mini.md) | bytedance-seed | Lightweight | 262K | $0.10+$0.40/M | 2026-06 | 68 | Yes | Seed 2.0 Mini. 262K ctx |
| [Z.ai: GLM 4.7 Flash](open/glm-4.7-flash.md) | z-ai | Lightweight | 202K | $0.06+$0.40/M | 2026-05 | 68 | Yes | Flash variant of GLM-4.7. Prompt -0.8% to $0.06 on Jul 28. ctx 200000->202752 on Jul 29 |
| [Qwen: Qwen3 VL 32B Instruct](open/qwen3-vl-32b-instruct.md) | qwen | Lightweight | 131K | $0.10+$0.42/M | 2026-05 | 68 | Yes | Qwen3 VL 32B. ctx 262K->131K on Jul 29 |
| [Tencent: Hunyuan A13B Instruct](open/hunyuan-a13b-instruct.md) | tencent | Self-hostable | 131K | $0.14+$0.57/M | 2026-03 | 68 | Yes | Hunyuan A13B. MoE |
| [GPT-OSS-120B](open/gpt-oss-120b.md) | OpenAI | Self-hostable | 131K | $0.04+$0.17/M | 2026-05 | 65 | Yes | 120B/5B MoE. Price dropped to $0.03/$0.15. Cheapest API |
| [Amazon: Nova 2 Lite](open/nova-2-lite-v1.md) | amazon | Self-hostable | 1M | $0.30+$2.50/M | 2026-05 | 65 | Yes | Nova 2 Lite. 1M ctx |
| [Trinity Large Thinking](open/trinity-large-thinking.md) | Arcee AI | Self-hostable | 262K | $0.22+$0.85/M | 2026-04 | 65 | Yes | Open reasoning model. Strong PinchBench and agentic workload scores. Price to $0.22/$0.85 on Jul 25 (p -12%, c +6%) |
| [Mistral Small 4](open/mistral-small-2603.md) | Mistral AI | Lightweight | 262K | $0.15+$0.60/M | 2026-03 | 65 | Yes | Mistral Small 4. Unifies flagship capabilities into efficient model. 262K ctx. Open weights |
| [Qwen: Qwen3 32B](open/qwen3-32b.md) | qwen | Lightweight | 131K | $0.08+$0.28/M | 2025-12 | 65 | Yes | Qwen3 32B dense |
| [Qwen: Qwen3 30B A3B Thinking 2507](open/qwen3-30b-a3b-thinking-2507.md) | qwen | Lightweight | 81K | $0.20+$2.40/M | 2026-07 | 64 | Yes | Qwen3 30B thinking July 2026. Price +54% to $0.20/$2.40 on Jul 29. Context cut 131K->82K |
| [Qwen3.6-35B-A3B](open/qwen3.6-35b-a3b.md) | Alibaba | Lightweight | 262K | $0.14+$1.00/M | 2026-06 | 64 | Yes | 35B/3B MoE |
| [Qwen: Qwen3 30B A3B Instruct 2507](open/qwen3-30b-a3b-instruct-2507.md) | qwen | Lightweight | 262K | $0.05+$0.19/M | 2026-07 | 62 | Yes | Qwen3 30B A3B July 2026. Price -52%/-36% to $0.048/$0.193 on Jul 26 |
| [North Mini Code](open/north-mini-code.md) | Cohere | Self-hostable | 256K | $0.00+$0.00/M | 2026-06 | 62 | Yes | 30B/3B MoE agentic coding. First Cohere North model. SWE-bench Verified 67.6%. Free on OpenRouter. Apache 2.0. 37K HF downloads |
| [Nous: Hermes 4 70B](open/hermes-4-70b.md) | nousresearch | Lightweight | 131K | $0.13+$0.40/M | 2026-06 | 62 | Yes | Hermes 4 70B. Fine-tuned Llama |
| [Qwen3.5-35B-A3B](open/qwen3.5-35b-a3b.md) | Alibaba | Lightweight | 262K | $0.14+$1.00/M | 2026-03 | 62 | Yes | 35B/3B MoE |
| [Qwen3.6-27B](open/qwen3.6-27b.md) | Alibaba | Lightweight | 262K | $0.29+$2.40/M | 2026-06 | 60 | Yes | 27B dense. Price: prompt -4% to $0.29 |
| [Qwen3-Coder-30B-A3B](open/qwen3-coder-30b-a3b-instruct.md) | Alibaba | Lightweight | 262K | $0.07+$0.28/M | 2026-04 | 60 | Yes | 30B/3B MoE coding. Completion +0.01 to $0.28 on Aug 1. ctx 160K->262K on Jul 29 |
| [Laguna XS 2.1](open/laguna-xs-2.1.md) | Poolside | Lightweight | 262K | $0.06+$0.12/M | 2026-07 | 58 | Yes | 33B/3B MoE coding agent |
| [Mistral: Ministral 3 14B 2512](open/ministral-14b-2512.md) | mistralai | Lightweight | 262K | $0.20+$0.20/M | 2026-05 | 58 | Yes | Ministral 14B |
| [Qwen3.5-27B](open/qwen3.5-27b.md) | Alibaba | Lightweight | 262K | $0.20+$1.56/M | 2026-03 | 58 | Yes | 27B dense. Price reverses: prompt -25%, completion -40% to $0.20/$1.56 on Jul 24 |
| [Llama 3.3 70B](open/llama-3.3-70b-instruct.md) | Meta | Lightweight | 131K | $0.13+$0.40/M | 2025-12 | 58 | Yes | 70B dense |
| [Gemma 4 31B-IT](open/gemma-4-31b-it.md) | Google | Lightweight | 262K | $0.10+$0.34/M | 2026-04 | 56 | Yes | 31B dense multimodal. Price -29%/-15% to $0.10/$0.34 on Jul 30 |
| [Olmo 3 32B Think](open/olmo-3-32b-think.md) | AllenAI | Lightweight | 65K | $0.15+$0.50/M | 2025-11 | 56 | Yes | 32B dense reasoning model. Fully-open (data+recipe+weights). 173 HF likes. 11K downloads |
| [Agents-A1](open/agents-a1.md) | InternScience | Self-hostable | 262K | $0.00+$0.00/M | 2026-06 | 55 | Yes | 35B MoE agentic VLM. Vision+text. Built on Qwen3.5 MoE. 262K ctx. 502 HF likes. Not on OpenRouter |
| [NVIDIA: Nemotron 3 Nano 30B A3B](open/nemotron-3-nano-30b-a3b.md) | nvidia | Lightweight | 262K | $0.05+$0.20/M | 2026-06 | 55 | Yes | 30B/3B hybrid Mamba-Transformer. Nano tier |
| [GPT-OSS-20B](open/gpt-oss-20b.md) | OpenAI | Lightweight | 131K | $0.03+$0.13/M | 2026-05 | 55 | Yes | 20B/3B MoE. Completion -7% to $0.13 on Jul 29 (prompt steady at $0.03) |
| [Qwen: Qwen3 14B](open/qwen3-14b.md) | qwen | Lightweight | 131K | $0.23+$0.91/M | 2025-12 | 55 | Yes | Qwen3 14B dense. Price reversed: prompt +90%, completion +279% to $0.23/$0.91 on Jul 23 (was Jul 22 drop) |
| [Gemma 4 26B A4B](open/gemma-4-26b-a4b-it.md) | Google | Lightweight | 262K | $0.07+$0.34/M | 2026-04 | 54 | Yes | 25.2B/3.8B MoE. Near-31B quality at fraction of cost. 14M HF downloads. Price cut -53%/-24% to $0.07/$0.34 on Jul 29 |
| [Google: Gemma 3 27B](open/gemma-3-27b-it.md) | google | Lightweight | 262K | $0.08+$0.45/M | 2025-06 | 52 | Yes | Gemma 3 27B. Older gen. Prompt -20%, completion +50% to $0.08/$0.45 on Jul 24. ctx 131K->262K on Jul 29 |
| [Nex-N2-Mini](open/nex-n2-mini.md) | Nex AGI | Lightweight | 262K | $0.03+$0.10/M | 2026-06 | 50 | Yes | Open agentic MoE. Text+image input. Coding and tool use. Ultra-cheap |
| [Qwen3.5-9B](open/qwen3.5-9b.md) | Alibaba | Lightweight | 262K | $0.10+$0.15/M | 2026-03 | 50 | Yes | 9B dense |
| [Qwen: Qwen3 8B](open/qwen3-8b.md) | qwen | Lightweight | 131K | $0.12+$0.46/M | 2025-12 | 50 | Yes | Qwen3 8B dense |
| [Ling-2.6-Flash](open/ling-2.6-flash.md) | inclusionAI | Lightweight | 262K | $0.01+$0.03/M | 2026-04 | 48 | Yes | 104B/7.4B MoE. Ultra-cheap at $0.01/$0.03/M. Fast agent responses |
| [Granite 4.1 8B](open/granite-4.1-8b.md) | IBM | Lightweight | 131K | $0.05+$0.10/M | 2026-04 | 45 | Yes | 8B dense. Enterprise tasks. 131K ctx. 1M HF downloads |
| [Meta: Llama Guard 4 12B](open/llama-guard-4-12b.md) | meta-llama | Specialized | 1M | $0.18+$0.18/M | 2026-04 | 40 | Large | Llama Guard 4 safety model. ctx 164K->1M on Jul 29 |