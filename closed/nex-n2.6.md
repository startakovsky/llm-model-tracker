---
model: Nex-N2.6
organization: Nex AGI
license: other
release_date: 2026-11-09
last_updated: 2026-11-10
sources:
  - https://openrouter.ai/nex-agi/nex-n2.6
  - https://huggingface.co/nex-agi/Nex-N2.5-Pro
---

# Nex-N2.6

New agentic model from Nex AGI (Nov 9, 2026), the follow-up to the open-weights Nex-N2.5 Pro. It is **built on GLM-5.3-Flash (~321B total parameters)** and oriented toward computer use, coding, and long-horizon tasks that involve tools.

## Key Facts

- **Pricing:** $0.12/$0.40 per M on OpenRouter, 262K ctx (236K max output).
- **vs N2.5-Pro:** reduces repetitive reasoning and follows the tools available in the current environment more closely — i.e., tighter environment coupling for agent loops.
- **Live on OpenRouter Nov 9** as `nex-agi/nex-n2.6`.
- No public weights on HuggingFace as of Nov 10 (the N2.5 line, including N2.5-Pro, is Apache-2.0, so open weights are likely to follow).

## Quality Assessment

A cheap agentic computer-use/coding model riding the GLM-5.3-Flash backbone at a small margin over the base (base GLM-5.3-Flash is $0.0399/$0.0784; Nex-N2.6 charges $0.12/$0.40 for the agentic post-training + computer-use behavior). Successor to the well-received Apache-2.0 N2.5-Pro; value proposition depends on how much of the agent-loop behavior survives outside Nex's own harness. Watch for the weights release to judge the actual delta over GLM-5.3-Flash.

## Notes

- Positioned similarly to N2.5-Pro: visual-feedback-loop agentic coding (explore codebase, multi-file edits, verify via screenshots) carried into computer use.
- Classified `closed` (Self-hostable) pending weights — flip to `open` when the HF repo drops.
