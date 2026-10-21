---
model: Nex N2.5 Mini
organization: Nex AGI
license: Apache 2.0
release_date: 2026-09-08
last_updated: 2026-10-21
sources:
  - https://huggingface.co/nex-agi/Nex-N2.5-mini
  - https://openrouter.ai/nex-agi/nex-n2.5-mini
---

# Nex N2.5 Mini

Compact sibling of **Nex N2.5 Pro** (Apache-2.0, Qwen3.5-MoE architecture per HuggingFace config). Nex's pitch is agentic coding inside a visual feedback loop — explore codebases, make multi-file edits, verify against screenshots — and Mini is the smaller, 16GB-local-sized member of that line, aimed at on-device agentic work.

## Architecture
- **Modality:** text + image input -> text output
- **Architecture:** Qwen3.5-MoE (Qwen3_5MoeForConditionalGeneration)
- **Context length:** 262,144 (256K) on OpenRouter
- **Family:** Nex-N2.5 line = Mini (this), Pro (tracked separately, $0.075/$0.25), Max (largest, HF only)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nex-agi/nex-n2.5-mini) | $0.025 | $0.10 | 262,144 | Live since ~Sep 8, 2026 |

## Quality Assessment
Value play within Nex's agentic niche: N2.5 Mini at $0.025/$0.10 is one of the cheapest open agentic-coding endpoints (40% of the Pro price), targeting local 16GB-class deployment rather than frontier benchmark chasing. Community traction is modest (3.4K HF downloads) but the Pro sibling carries real buzz (33K downloads, GGUF/MLX quants same week) — Mini inherits that ecosystem. Best framed as "most of the N2.5 verification-loop value at a fraction of the cost" rather than a GLM-5.3/Kimi-K3 competitor.

## Notes
- Qwen3.5-based tokenizer/MoE; Apache-2.0 weights on HuggingFace.
- Classified `open` (Lightweight).