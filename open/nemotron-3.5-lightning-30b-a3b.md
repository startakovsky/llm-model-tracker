---
model: NVIDIA: Nemotron 3.5 Lightning
organization: NVIDIA
license: OpenMDW-1.1
release_date: 2026-08-04
last_updated: 2026-08-12
openrouter_id: nvidia/nemotron-3.5-lightning-30b-a3b
category: Lightweight
generated: stub-from-csv
---

# NVIDIA: Nemotron 3.5 Lightning

Open-weight model from **NVIDIA**. Weights on HuggingFace (BF16 + NVFP4).

## Quick Facts
- **OpenRouter ID:** `nvidia/nemotron-3.5-lightning-30b-a3b`
- **Context length:** 262K
- **License:** OpenMDW-1.1
- **Category:** Lightweight
- **OpenRouter price:** $0.10 + $0.25/M

## Architecture
- **30B total / 3B active** MoE (Nemotron-H architecture)
- 52 layers, 6 experts per token, latent-MoE
- Hybrid Mamba-Transformer lineage
- HF sizes: `nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16` (~15.7K downloads, 103 likes) and `-NVFP4` (~19.2K downloads, 182 likes)

## Positioning
- **~90% of Nemotron 3.5-class capability at self-hostable size** — a fraction of the cost of frontier-class models.
- High-throughput agentic workloads and specialized tasks.
- Open weights + datasets + recipes (OpenMDW-1.1); full GGUF quant ecosystem (ggml-org, bartowski, unsloth, MTP quants) and MLX (Apple Silicon) released Aug 11-12, 2026 — strong community traction.
- On OpenRouter at $0.10/$0.25 per M — competitive with Gemma 4 26B and Qwen3 Next 80B pricing.
- Runs on a single 96GB GPU (or less with quants), fitting the "self-hostable" lightweight tier.

## Cost/Quality
~Frontier-grade agentic throughput for ~1/12th the price of GLM-5.2 — a strong value pick for local/small agentic deployments.
