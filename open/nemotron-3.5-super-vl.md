---
model: Nemotron 3.5 Super VL
organization: NVIDIA
license: OpenMDW-1.1
release_date: 2026-10-15
last_updated: 2026-10-16
sources:
  - https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/
  - https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
---

# Nemotron 3.5 Super VL

Released October 15, 2026. NVIDIA's new open vision-language reasoning model — 120B total / 12B active, hybrid Mamba-2–Transformer MoE with a C-RADIO vision encoder and vision-language connector. First VL addition to the Nemotron 3.5 family. Fully open (OpenMDW-1.1: weights, data, recipes). 1M-token context.

## Key signals
- 120B/12B hybrid Mamba-2 + MoE + attention, C-RADIO vision encoder; text+image+video in, text out.
- Multi-Token Prediction (MTP) enables native speculative decoding.
- GPQA-Diamond 89.5, SWE-bench Verified 71.1, Terminal-Bench 2.1 60.7, LiveCodeBench v6 88.2, GDPval-AA v2 1211.
- Artificial Analysis: "leading US open weight model" — twice the intelligence of prior generation at ~60% fewer output tokens (noted before Muse Spark Open landed the same day).
- Built from the Nemotron 3 Nano 30B-A3B backbone; configurable reasoning (off/on/medium) via chat template.
- Deploys on 4× H100 or 2× GB200; BF16 reference + NVFP4 optimized releases.

## Availability
- **OpenRouter:** **$0.15/$0.50 per M** (1M ctx). Listed Oct 15.
- **Weights:** HuggingFace `nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16` (57 likes, 2.1K downloads day one).

## Classification
`open` (OpenMDW-1.1, weights on HF). Quality score **83** — a strong open multimodal/SWE model in the 120B class, well undercutting the 816B frontier models while landing near them on several benchmarks. Self-hostable on ~2–4 high-end GPUs.

## Sources
- NVIDIA blog: https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/
- HF model card: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16
