# Nemotron 3 Super (120B-A12B)

**Org:** NVIDIA  
**License:** OpenMDW-1.1  
**OpenRouter ID:** `nvidia/nemotron-3-super-120b-a12b`  
**Release Date:** June 10, 2026  
**Category:** Self-hostable  
**Context:** 1,000,000 tokens  

## Pricing (per million tokens)

| | Prompt | Completion |
|---|---|---|
| OpenRouter | $0.08 | $0.45 |

## Architecture

- **Total params:** 120B
- **Active params:** 12B
- **Architecture:** Hybrid Mamba-Transformer Mixture-of-Experts
- **Context:** 1M tokens
- **Weights:** Fully open (weights, datasets, recipes) on HuggingFace (`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8`)

## Quality Assessment

Nemotron 3 Super is NVIDIA's efficient open MoE model, activating only 12B of 120B parameters. It achieves up to 2.2x higher inference throughput than GPT-OSS-120B and 7.5x higher than Qwen3.5-122B on 8k token input. Excels in agentic reasoning, coding, planning, and tool calling.

On Artificial Analysis Intelligence Index, it scores 25 (reasoning mode). NVIDIA reports strong function-calling benchmarks (retail 62.6, telecom 95.0, airline 66.0). Output speed ranges from 145-499 t/s.

**Cost/quality tradeoff:** At $0.08/$0.45 per million, Nemotron 3 Super is extremely cost-efficient — roughly 10x cheaper than GLM-5.2 ($0.93/$3.00) while offering competitive agentic and coding performance for its size class. The hybrid Mamba-Transformer architecture gives it a throughput advantage over pure Transformer MoEs of similar size. Available in FP8 on HuggingFace for efficient deployment.

## Links

- [OpenRouter](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b)
- [HuggingFace](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8)
- [NVIDIA Model Card](https://build.nvidia.com/nvidia/nemotron-3-super-120b-a12b/modelcard)
- [NVIDIA Research](https://research.nvidia.com/labs/nemotron/Nemotron-3-Super/)
