---
model: Clover-35B-A3B Preview
organization: DiffuSpace
license: Apache 2.0
release_date: 2026-10-24
last_updated: 2026-10-30
sources:
  - https://huggingface.co/Diffuspace/Clover-35B-A3B-Preview
  - https://diffuspace.ai/blog/clover-35b/
  - https://github.com/DiffuSpace/Clover-35B-A3B-Preview
---

# Clover-35B-A3B Preview

First model released by DiffuSpace (Oct 24, 2026): an open-source diffusion language model (block-diffusion decoding). 35B-total MoE with ~3B active params, backbone derived from Qwen3.6-35B-A3B. 128K ctx, text-only, Apache 2.0.

## Availability
- NOT on OpenRouter (HF + GitHub only; custom-code transformers implementation).
- Open weights on HuggingFace (`Diffuspace/Clover-35B-A3B-Preview`; 164 likes, ~1.5K downloads as of Oct 30).

## Capabilities
- Block-diffusion generation — parallel decoding genre pioneered by Inception's Mercury line, now in an open-weight package.
- Self-reported SOTA among open-source diffusion language models at release (launch blog benchmarks).

## Quality assessment
Early, self-reported numbers from a brand-new lab; 164 likes in week one is modest traction. The architectural interest (open diffusion LM) outranks proven capability. Track as a watch item in the open self-hostable tier rather than a daily-driver recommendation. Quality score 68.