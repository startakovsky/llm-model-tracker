---
model: Nex-N2.5-Mini
organization: Nex AGI
license: Apache 2.0
release_date: 2026-09-08
last_updated: 2026-09-20
sources:
  - https://huggingface.co/nex-agi/Nex-N2.5-mini
  - https://openrouter.ai/nex-agi/nex-n2.5-mini:free
  - https://nex.sii.edu.cn/
---

# Nex-N2.5-Mini

## Architecture
- **Base:** Qwen3.5-35B-A3B (MoE, ~35B total / 3B active)
- **Context length:** 262,144
- **Model type:** qwen3_5_moe (Qwen3_5MoeForConditionalGeneration)
- **Modality:** text+image→text (multimodal)
- **Family:** Nex-N2.5 (mini / Pro / Max; Max is 1.6T MoE on DeepSeek V4 base)
- **Positioning:** "Vision into Action" — computer use, web browsing, vision-assisted agency

## Self-Hosting
- Open weights on HuggingFace: `nex-agi/Nex-N2.5-mini` (~8.4K downloads, 839 likes)
- Qwen3.5-MoE arch, so vLLM/SGLang support expected out of the box
- Lightweight 35B/3B class — fits consumer/small GPU deployments

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nex-agi/nex-n2.5-mini:free) | $0 | $0 | 262,144 | Free tier only so far |

## Quality Assessment
Nex-N2.5 is the successor to the Nex-N2 family (N2-Pro/N2-Mini were delisted from OpenRouter around Sep 20). The Mini tier is a 35B/3B open agentic MoE built on the Qwen3.5-35B-A3B base, oriented toward high-speed instruction following, real-time tool execution, and cost-efficient scale-out. Pro adds more capacity for computer-use/browsing/coding agents; Max is the 1.6T flagship.

**Agentic verdict:** A cheap open agentic model in the Lightweight class. Only the free tier is live on OpenRouter as of Sep 20, so no paid pricing to compare. Community reception is positive (r/LocalLLaMA, Nex ecosystem). Worth watching as the N2.5 line matures and paid tiers arrive.

## Notes
- Open-source agentic model family from Nex AGI (nex.sii.edu.cn)
- Strengthens computer use, web browsing, and vision-assisted interaction vs N2
- Only `:free` variant live on OpenRouter as of Sep 20, 2026