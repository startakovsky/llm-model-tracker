---
model: Cohere: North Mini Code
organization: Cohere
license: Apache 2.0
release_date: 2026-06-17
last_updated: 2026-10-12
openrouter_id: cohere/north-mini-code
category: Specialized
quality_score: 78
generated: stub-from-csv
---

# Cohere: North Mini Code

Cohere's first open-source agentic coding model, part of the new North family. A 30B-total/3B-active sparse MoE trained specifically for code generation, agentic software engineering, and terminal tool-use tasks.

## Quick Facts
- **OpenRouter ID:** `cohere/north-mini-code`
- **Context length:** 256K (64K max output)
- **License:** Apache 2.0 (open weights on CohereLabs/North-Mini-Code-1.0)
- **Category:** Specialized
- **Quality score:** 78/100
- **Notes:** 30B/3B MoE. SWE-bench Verified 67.6, SWE-bench Pro 40.2, Terminal-Bench 2. Insanely efficient agentic coder for local deployment.

## API Providers
| Provider | Prompt USD/M | Completion USD/M | Context |
|---|---|---|---|
| OpenRouter (cohere/north-mini-code) | 0.00 | 0.00 | 256K |

## Quality Assessment
Quality score 78/100. At 30B total / 3B active it is a lightweight, directly runnable agentic coding model — SWE-bench Verified 67.6 and Terminal-Bench 2 support solid terminal/agent tool-use. It uses an efficient attention (sliding-window + global in 3:1 ratio, 128 experts/8 active) and was post-trained with cascaded SFT + RLVR on agentic coding. Listed as free tier on OpenRouter since ~Jun 2026. Strong r/LocalLLaMA buzz as Cohere's first open agentic coder.

## Notes
- OpenRouter: https://openrouter.ai/cohere/north-mini-code
- Open weights (Apache-2.0, CohereLabs/North-Mini-Code-1.0, ~10K downloads/mo).
- Supports interleaved thinking + tool use via chat templates; vLLM/OpenCode integration documented by Cohere.
- Free tier on OpenRouter as of Oct 12 2026.