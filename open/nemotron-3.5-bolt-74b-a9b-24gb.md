---
model: Nemotron 3.5 Bolt 74B-A9B (24GB)
organization: NVIDIA
license: OpenMDW-1.1
release_date: 2026-10-15
last_updated: 2026-10-20
sources:
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB
  - https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Bolt-24GB/
---

# Nemotron 3.5 Bolt 74B-A9B (24GB)

NVIDIA's local-agent vision-language model (Oct 15), compressed from Nemotron 3.5 Super VL 120B-A12B down to a 24GB footprint using Star Elastic compression + IQ2 (2.0625-bit) quantization-aware training. Designed to run everyday agentic tasks locally alongside other applications at >=80 tokens/s.

## Architecture
- **Total params:** 74B (9B active), hybrid Mamba-2-Transformer LatentMoE
- **Vision encoder:** C-RADIO v4-H
- **Context length:** 262,144 (256K)
- **Precision:** native IQ2 (weights), NVFP4 (Mamba layers), Q8_0 (embeddings/attention)
- **Structure:** expert top-K 9 (down from 22 in parent Super VL); budget searched for <24GB at batch 1 / 128K ctx
- **Speculative decoding:** LiLiCorr parallel drafter (1.13B), mean acceptance length ~4.7
- **Modality:** text + image + video -> text

## Capabilities
- Compressed-from-large beats trained-from-scratch at the same memory footprint: #1 PinchBench, #2 WebArena, #2 BrowseComp among 24GB-class models (NVIDIA reporting).
- Beats Qwen3.6-35B-A3B (BF16) and Gemma 4 26B-A4B (BF16) on GDPVal-AA-V2, Terminal-Bench 2.1, Tau3-Banking, HLE, GPQA-D, AA-LCR, BrowseComp, WebArena-vision.
- Speeds: ~84 TPS on AIPerf SPEED-Bench (RTX Spark, with LiLiCorr); ~600s agent replay duration (AA AgentPerf Local).
- Reasoning toggled via chat template (`enable_thinking=True/False`, inherited from Super 3.5 VL client).
- Focus: tool calling, web browsing, terminal use; EN + coding primary, ES/FR/DE/IT/JA supported.

## Self-Hosting
- Main 24GB IQ2 checkpoint (llama.cpp-friendly) + GGUF + unquantized BF16 checkpoint + LiLiCorr drafter (with GGUF) all on HuggingFace.
- vLLM recipes for Ampere (A100), Hopper (H100-80GB), Blackwell; llama.cpp on Windows ARM / RTX Spark.
- License: OpenMDW-1.1 (commercial use permitted).
- Not yet served on OpenRouter (self-host only).

## Cost Assessment
No paid API yet — runs in 24GB VRAM (RTX 5090/4090-class or DGX Spark), so the relevant cost is hardware, not tokens. Strong low-cost option for local agent harnesses; effectively free at the margin if you already own a 24GB GPU.