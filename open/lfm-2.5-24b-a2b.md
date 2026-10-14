---
model: LFM2.5-24B-A2B
organization: Liquid AI
license: other
release_date: 2026-10-12
last_updated: 2026-10-14
sources:
  - https://openrouter.ai/liquid/lfm-2.5-24b-a2b
  - https://huggingface.co/LiquidAI/LFM2.5-24B-A2B
  - https://www.liquid.ai/models
---

# LFM2.5-24B-A2B

Liquid AI's largest LFM2.5 family member, released Oct 12, 2026. A 24B-total / 2.45B-active mixture-of-experts reasoning model designed for fast, private agents running on-device (laptops/PCs).

## Availability
- OpenRouter id `liquid/lfm-2.5-24b-a2b` at $0.05/$0.70 per M, 128K context.
- Open weights on HuggingFace (`LiquidAI/LFM2.5-24B-A2B`), Liquid custom license.

## Capabilities
- Always reasons before answering (reasoning model).
- Built for agents that call tools; Liquid recommends pairing with retrieval or web search for knowledge-heavy tasks.
- Efficient local deployment: 2.45B active params make it cheap to serve on consumer hardware.

## Key signals
- Newest LFM2.5 family member (supersedes the smaller LFM2.5 tiers) with community traction (r/LocalLLaMA, 4K+ HF downloads, 258 likes within days).
- 128K ctx — modest but workable for agentic sub-tasks.

## Quality assessment
A competent lightweight on-device reasoning agent model rather than a frontier contender. At $0.05/$0.70 it sits in the cheap open tier alongside models like GLM-4.5-Air ($0.13/$0.85) and Nemotron 3 Nano; well suited to local/edge agent workflows. Quality score 64.
