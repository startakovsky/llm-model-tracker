---
model: Nex-N2.5-Pro
organization: Nex AGI
license: Apache 2.0
release_date: 2026-09-08
last_updated: 2026-09-20
sources:
  - https://huggingface.co/nex-agi/Nex-N2.5-pro
  - https://openrouter.ai/nex-agi/nex-n2.5-pro:free
  - https://nex.sii.edu.cn/
---

# Nex-N2.5-Pro

## Architecture
- **Base:** Qwen3.5-MoE (successor to N2-Pro's 397B/17B MoE)
- **Context length:** 262,144
- **Model type:** qwen3_5_moe (Qwen3_5MoeForConditionalGeneration)
- **Modality:** text+image→text (multimodal)
- **Family:** Nex-N2.5 (mini / Pro / Max; Max is 1.6T MoE on DeepSeek V4 base)
- **Positioning:** "Vision into Action" — computer use, web browsing, vision-assisted agency

## Self-Hosting
- Open weights on HuggingFace: `nex-agi/Nex-N2.5-pro` (~32K downloads, 667 likes)
- Qwen3.5-MoE arch, vLLM/SGLang support expected out of the box
- Pro tier targets real-world agentic productivity (computer use, browsing, coding)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nex-agi/nex-n2.5-pro:free) | $0 | $0 | 262,144 | Free tier only so far |

## Quality Assessment
Nex-N2.5 is the successor to the Nex-N2 family (N2-Pro/N2-Mini were delisted from OpenRouter around Sep 20). Pro is the mid-tier open agentic model, built on Qwen3.5-MoE, with strengthened computer-use, web-browsing, and vision-assisted agency. The family tops out at Max (1.6T MoE on DeepSeek V4 base) for complex reasoning and coding.

**Agentic verdict:** A capable open agentic model in the Frontier/self-hostable class. Only the free tier is live on OpenRouter as of Sep 20, so no paid pricing to compare. The N2.5 line is Nex AGI's current open push; Pro is the practical workhorse tier. Worth watching as paid pricing arrives.

## Notes
- Open-source agentic model family from Nex AGI (nex.sii.edu.cn)
- Successor to the delisted Nex-N2-Pro / Nex-N2-Mini
- Only `:free` variant live on OpenRouter as of Sep 20, 2026