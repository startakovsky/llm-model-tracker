---
model: Qwen3-VL-235B-A22B-Thinking
organization: Alibaba (Qwen)
license: Apache 2.0
release_date: 2026-05-01
last_updated: 2026-07-18
---

# Qwen3-VL-235B-A22B-Instruct (Thinking)

## Architecture
- **Total params:** 235B (MoE)
- **Active params per token:** ~22B
- **Context length:** 131,072
- **Architecture type:** Qwen3 MoE vision-language model (thinking/reasoning variant)

## Pricing
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (`qwen/qwen3-vl-235b-a22b-thinking`) | $0.26 | $2.60 | 131,072 |

## Quality Assessment
The "thinking" variant of Qwen3-VL-235B-A22B — a 235B/22B MoE vision-language model with explicit reasoning. Strong on multimodal reasoning and agentic tool-use tasks that benefit from chain-of-thought. Pairs vision input with the Qwen3 thinking trajectory.

**Cost/quality framing:** At quality 84, it sits in the frontier open tier alongside GLM-5 Turbo and just below the GLM-5.2 reference (90). The thinking variant trades higher completion cost ($2.60/M) for stronger multi-step reasoning than its instruct sibling.

## Notes
- Sister model to `qwen/qwen3-vl-235b-a22b-instruct` (non-thinking, lower completion price).
- Open weights on HuggingFace under Apache 2.0.
