---
model: Muse Ember
organization: Meta
license: Proprietary
release_date: 2026-11-09
last_updated: 2026-11-10
sources:
  - https://research.meta.ai/blog/muse-ember
  - https://dev.meta.ai/models/muse-ember
  - https://openrouter.ai/meta/muse-ember
---

# Muse Ember

Meta Superintelligence Lab's smallest and most efficient model (Nov 9, 2026), and the **first model trained from Muse Wonder Full**. Designed for the work agents repeat all day — tool calls, coding subtasks, routing, extraction, long-document parsing — rather than for frontier problem-solving.

## Key Facts

- **Pricing:** $0.10/$0.50 per M ($0.004/M cached input), 1M ctx, up to 512K max output.
- **Multimodal:** natively understands text, image, audio, and video; native computer use (operates a computer directly from screenshots).
- **Availability:** Muse Code and Meta Model API as `muse-ember-1.0` (Responses API), plus Google Cloud and Oracle Cloud. **On OpenRouter Nov 9** at `meta/muse-ember` ($0.10/$0.50).
- Closed API — no public weights on HuggingFace.

## Efficiency Position (Artificial Analysis, Nov 9)

- AA Intelligence Index 36 at max reasoning — **ties Claude Haiku 5.5's max score for about a third of the cost**, and beats every GPT-6 Luna setting.
- Meta claims it sits on the **AA efficiency frontier**: no model scores higher for less per task (~$0.14/task vs Haiku 5.5 up to $0.41, vs Muse Spark 1.3 $2.39).
- vs Muse Spark 1.3 (max): Intelligence Index 36 vs 37, but $0.14/task vs $2.39 — same ballpark intelligence at ~1/17th the task cost.

## Benchmarks (max reasoning, from Meta)

| Benchmark | Muse Ember | Haiku 5.5 (max) | GPT-6 Luna (max) |
|---|---|---|---|
| AutomationBench-AA | **37.8** | 13.9 | 20.2 |
| Agents' Last Exam | **61.6** | 57.0 | 57.1 |
| Terminal-Bench 4.0 | **40.9** | 39.2 | 16.4 |
| Coding Agent Index-AA | **46** | 37 | 31 |
| OSWorld 2.1 (partial) | **69.5** | 68.9 | 50.5 |
| PerceptionBench (w/ tools) | **80.6** | 78.6 | 62.8 |
| FrontierCode 2.0-AA | 27.2 | **34.9** | 25.2 |
| AA Index | **36** | 36 | 28 |

## Quality Assessment

Best-in-class intelligence-per-dollar for high-volume subagent/agentic work — the budget workhorse of the Meta Muse line. Not a frontier coder (loses to Haiku 5.5 on FrontierCode 2.0), but dominates on automation/agent-loop benchmarks at a fraction of the cost. Directly competes with Claude Haiku 5.5 ($0.10/$0.50 vs $0.10/$0.50 — same price, Meta claims more intelligence) and GPT-6 Luna ($0.10/$0.50).

## Notes

- Rounds out Meta's portfolio: Muse Wonder (hardest problems), Muse Spark (coding/agentic), Muse Ember (repeatable agent tasks at scale).
- Meta says "even more efficient models in training."
- Classified `closed` (Lightweight). Quality score 76.
