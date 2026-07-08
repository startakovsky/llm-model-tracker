---
model: Nex-N2-Pro
organization: Nex AGI
license: Apache 2.0
release_date: 2026-06-08
last_updated: 2026-07-08
sources:
  - https://huggingface.co/nex-agi/Nex-N2-Pro
  - https://openrouter.ai/qwen/qwen3.7-max
---

# Nex-N2-Pro

## Architecture
- **Total params:** 397B (MoE, built on Qwen3.5 architecture)
- **Active params per token:** 17B
- **Context length:** 262,144
- **Model type:** qwen3_5_moe (Qwen3_5MoeForConditionalGeneration)
- **Modality:** text+image→text (multimodal)
- **Architecture:** Qwen3.5-based MoE with Agentic Thinking framework (Adaptive Thinking + Coherent Thinking)

## Self-Hosting

### GGUF (llama.cpp)
- No official GGUF quants available yet
- Model has 0 GGUF files on HuggingFace

### FP8/FP4 (vLLM on GPU)
- Full BF16: ~794GB (not practical)
- FP8: ~397GB (fits 1x H100 80GB with offloading, or 8x H100)
- Supports vLLM, SGLang out of the box
- NVFP4 quantization expected possible

### Other engines
- vLLM and SGLang supported natively (HuggingFace model card)
- Docker Model Runner: `docker model run hf.co/nex-agi/Nex-N2-Pro`

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nex-agi/nex-n2-pro) | $0.25 | $1.00 | 262,144 | 3.6x cheaper prompt than GLM-5.2 |

## Quality Benchmarks
- Terminal-Bench 2.1: 75.3
- SWE-bench Verified: 80.8
- SWE-bench Pro: 58.8
- GPQA Diamond: 90.7
- GDPval: 1585
- AgentBrowseComp: 83.7
- Toolathlon: 51.9
- WildClawBench: 53.5
- WideSearch: 75.6
- TAU: 71.1

## Quality Assessment
Nex-N2-Pro is a serious frontier-tier agentic model that rivals GPT-5.5 and Opus 4.7 on multiple benchmarks. With Terminal-Bench 2.1 at 75.3 (vs GLM-5.2's 81.0, ~93% as good) and SWE-bench Verified at 80.8 (vs GLM-5.2's 82.8, ~98% as good), it comes within striking distance of GLM-5.2 on coding and agentic tasks. GPQA Diamond at 90.7 is exceptional reasoning. At $0.25+$1.00/M on OpenRouter, it's ~3.6x cheaper on prompt tokens and ~2.9x cheaper on completion tokens compared to GLM-5.2 ($0.90+$2.86/M). Built on Qwen3.5 architecture with multimodal support.

**Agentic verdict:** Nearly viable as a GLM-5.2 replacement for agentic workflows. Terminal-Bench 75.3 is ~93% of GLM-5.2's 81.0, and SWE-bench Verified 80.8 is ~98% of GLM-5.2's 82.8. The model's "Agentic Thinking" framework (Adaptive Thinking + Coherent Thinking) is purpose-built for multi-step tool-calling. At ~3x cheaper, this is a strong cost/quality tradeoff for agentic workloads. Community reports on Reddit confirm strong real-world agentic performance.

## Notes
- Post-trained on Qwen3.5 series
- 7,846 downloads, 364 likes on HuggingFace
- Nex-N2-Mini also available (35B total, smaller sibling)
- Reddit r/LocalLLaMA: positive reception, "Nex N2 Pro IS GREAT"
