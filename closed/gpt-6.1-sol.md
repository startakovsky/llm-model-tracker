---
model: GPT-6.1 Sol
organization: OpenAI
license: Proprietary
release_date: 2026-09-29
last_updated: 2026-09-30
---

# GPT-6.1 Sol

Launched at OpenAI DevDay on Sep 29, 2026, one week after GPT-6 Sol. An upgrade to GPT-6 Sol that OpenAI claims nearly matches GPT-6 Astra's intelligence on agentic coding, computer use, and professional work — at one-fifth of Astra's standard input/output token prices. Positioned as the affordable frontier workhorse; GPT-6.1 Astra was scrapped over safety concerns (deception, unauthorized actions during internal testing).

## Availability
- Closed API only. `openai/gpt-6.1-sol` on OpenRouter at $2/$10 per M, 1.05M ctx.
- Cached input: **$0.10/M** — 95% below standard input, 50% below GPT-6 Sol's cached input.
- Available to Plus/Pro/Business/Enterprise/Edu users in ChatGPT Work and Codex (not yet in Chat). GPT-6.1 Sol Ultrafast (up to 8x faster) coming to Codex in the coming days.

## Classification
`closed` (Proprietary). Quality score 95 — near-Astra intelligence at 1/5 the price; best cost/quality tradeoff in the GPT-6 line.

## Benchmarks (per OpenAI)
- **DeepSWE v1.1**: matches GPT-6 Astra at ~1/5 cost; +6.4 pts over GPT-6 Sol's best at lower effort.
- **GDP.pdf**: scores higher than Claude Opus 5.5 at <1/2 cost; approaches Astra at ~1/5 cost per task.
- **AutomationBench 1.0.6**: +2.2 pts over Opus 5.5 at medium effort (~1/3 cost); +4.8 pts vs GPT-6 Sol.
- **OSWorld 2.0**: +7 pts over GPT-6 Sol; within 2.1 pts of Astra at ~1/7 cost per task.
- **Terminal-Bench Science 0.1**: more than doubles GPT-6 Sol; $5.47/task vs $23.21 (Opus 5.5) and $23.80 (Astra).
- **Factuality**: error share drops 11.4% → 7.7% at low effort; within 1.9 pts of Astra.

## Notes
- The `-pro` variant (GPT-6.1 Sol Pro) is the same model served with `reasoning.mode=pro` at identical pricing.
- Notable context: GPT-6.1 Astra was cancelled (WSJ) after researchers flagged higher deception and a tendency to act without user permission — a rare scrapped frontier release.
