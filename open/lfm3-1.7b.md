---
model: LFM3-1.7B
organization: Liquid AI
license: other
release_date: 2026-10-27
last_updated: 2026-11-03
sources:
  - https://huggingface.co/LiquidAI/LFM3-1.7B
  - https://www.liquid.ai/blog/lfm3
---

# LFM3-1.7B

First release of Liquid AI's new-generation LFM3 family (Oct 27, 2026): six open-weight 2B-class models (text, VL, audio, omni, decision variants) built on a new tri-hybrid architecture with new multimodal encoders. The 1.7B text model is post-trained for local agents and specialized applications.

## Availability
- Open weights on HuggingFace (`LiquidAI/LFM3-1.7B`, Liquid custom license; 47.8K downloads, 1.4K likes).
- Also on Liquid's Playground; LFM3-VL-2B (1.92B, on-device image/video understanding, 128K ctx) is listed on LM Studio.
- Not on OpenRouter (self-host / playground only) — tracked as a lightweight release with 0/0 API placeholder.

## Key signals
- Real community traction for a 2B-class release (HF blog, LM Studio support, 1.4K likes in a week).
- New architecture generation (tri-hybrid), successor to the tracked LFM2.5 family.
- LFM3-1.7B averages 49.37 across 29 self-reported benchmarks — above Qwen3.5-9B's 47.24 at a fraction of the size.

## Quality assessment
A competent edge/on-device agent model, not a frontier contender — the point is running on phones and fine-tuning on a single GPU. Quality score 52 (Lightweight). No API pricing, so cost/quality comparison applies only to local deployment.
