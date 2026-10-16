---
model: Muse Spark Open
organization: Meta
license: Muse Model License
release_date: 2026-10-15
last_updated: 2026-10-16
sources:
  - https://research.meta.ai/blog/muse-spark-open
  - https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
---

# Muse Spark Open

Released October 15, 2026. Meta's first major open-weight release after the closed Muse Spark 1.x line — billed as the **most capable US open-weight model to date**. 816B total / 42B active parameters, natively multimodal (text, image, video, audio), 1M-token context. The open-weight sibling of the closed Muse Spark 1.3 (which sits at $1.25/$4.25).

## Key signals
- 816B/42B sparse MoE, natively multimodal, 1M ctx.
- **Terminal-Bench 2.1: 76.4** · GPQA Diamond: 89 · DeepSWE: 60 · Toolathlon Verified: 72.8.
- First model in its class to run on desktop: 2× Apple M5 Ultra Mac Studio (~1 TB unified memory) via MLX.
- Meta positions it for coding and agentic work — long-horizon tasks, complex software engineering, multi-step reasoning.
- Hosted at Baseten, Fireworks, Groq, Modal, Nebius, OpenRouter, Together. Custom Helion GPU kernels in SGLang (1.03–3.95× kernel speedups on NVIDIA/AMD).
- Released under the **Muse Model License** (limited commercial terms): free for most use, but requires "Built with Muse Spark Open" attribution and a separate paid agreement if you run it as MaaS with >$20M annual revenue.

## Availability
- **OpenRouter:** **$1.25/$4.25 per M** (1M ctx) — parity with Muse Spark 1.2/1.3. Listed Oct 15.
- **Weights:** HuggingFace `meta-models/Muse-Spark-Open-816B-A42B` (390 likes, 815 downloads in first day).

## Classification
`open` (weights on HuggingFace; Muse Model License — permissive-ish with MaaS revenue clause). Quality score **90** — a genuine US open-weight frontier candidate, competing with GLM-5.3/Kimi K3 for best open coding model, priced as a mid-tier API.

## Sources
- Meta research blog: https://research.meta.ai/blog/muse-spark-open
- HF model card: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
