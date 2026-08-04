---
model: Qwen3.8 Max
organization: Alibaba
license: TBD (Apache 2.0 expected)
release_date: 2026-08-03
last_updated: 2026-08-04
---

# Qwen3.8 Max

## Architecture
- **Total params:** 2.4T (MoE)
- **Active params per token:** 95B
- **Context length:** 1,000,000 (1M)
- **Modality:** Multimodal — text, image, video, documents
- **Architecture type:** Sparse Mixture-of-Experts with hybrid attention mechanism
- **Foundation:** Built on Qwen 3.5

## Availability
- **Status:** Officially launched August 3, 2026. API-only (closed). Open weights promised "next week" alongside Qwen3.8-27B.
- **Access:** Alibaba Cloud Model Studio, QwenWork, OpenRouter (`qwen/qwen3.8-max`)
- **OpenRouter price:** $2.00/$6.00 per M tokens
- **HuggingFace:** Weights not yet available (as of Aug 4, 2026)

## Benchmarks (vendor-reported)
- **OSWorld-Verified:** 86.1 — beats GPT-5.6 Sol Max (83.2), Fable 5 (85.0), Gemini 3.1 Pro (76.2)
- **PaperBench:** 93.0
- **TerminalBench 2.1:** 86.6
- **Vision2Web:** 69.0
- **LVBench:** 81.8
- **ERQA:** 77.8
- **Arena rankings:** 5th Text Arena, 2nd Vision Arena, 4th Frontend Code Arena

## Competitive Context
Qwen3.8-Max is Alibaba's largest and most capable model, targeting autonomous software engineering and long-horizon enterprise work. It can autonomously execute software projects spanning 10+ days, reproduce research papers, and perform iterative chip-design optimization. Priced at $2/$6 — below Kimi K3 ($3/$15) and competitive with GPT-5.6 tiers.

Nikkei reported it "falls short of 'second only to Fable 5' claim" in independent testing, tempering Alibaba's marketing. Nevertheless, the agentic benchmarks (OSWorld, TerminalBench) are class-leading if they hold up under independent evaluation.

The open-weight release (promised next week) would be the first time a Max-class Qwen model becomes available for self-hosting — a significant strategic shift. License terms are TBD; could be Apache 2.0 or a more restrictive custom license (as with Moonshot's Kimi K3).

## Quality Assessment
At quality_score 86, Qwen3.8-Max sits just below the top tier (GPT-5.5 Pro 98, Claude Opus 5 96, GLM-5.2 90) but is competitive on agentic benchmarks. The OSWorld score of 86.1 is the highest reported, ahead of both GPT-5.6 Sol Max and Fable 5. However, these are vendor-reported; independent validation is pending. At $2/$6, it offers strong value for agentic workflows — roughly 10x cheaper than GPT-5.5 Pro ($30/$180) with potentially comparable agentic capability.

## Notes
- Officially launched August 3, 2026 (Bloomberg, VentureBeat, TechNode, The Register coverage)
- Now live on OpenRouter at $2/$6 with 1M context
- Open weights expected "next week" alongside smaller Qwen3.8-27B
- RecreationBench introduced alongside the model (reconstructs apps from scratch in black-box environment)
- Alibaba open-sourced `oh-my-cli` agent framework created autonomously by the model over 16 days
