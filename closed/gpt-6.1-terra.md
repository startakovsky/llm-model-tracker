---
model: GPT-6.1 Terra
organization: OpenAI
license: Proprietary
release_date: 2026-10-26
last_updated: 2026-10-27
---

# GPT-6.1 Terra

OpenAI's new "workday" model (Oct 26, 2026), the successor to GPT-5.6 Terra in the GPT-6.1 family. Fast and efficient, it combines detailed visual reasoning and precise computer use with clearer, more natural writing. Positioned for the communication and computer-based tasks that fill the workday — drafting proposals, interpreting technical drawings, filling forms, editing videos, and high-volume automation.

## Availability
- Closed API only. `openai/gpt-6.1-terra` on OpenRouter at **$1/$5 per M**, 1.05M ctx, 128K max output.
- Standard API pricing is **50% lower** than GPT-5.6 Terra and GPT-6.1 Sol ($1/$5 vs $2/$12 and $2/$10).
- Cached input **$0.05/M**. Available to Plus/Pro/Enterprise/Edu in ChatGPT Work and Codex.

## Classification
`closed` (Proprietary). Quality score 90 — a strong cost-intelligence tier: ~GPT-6 Astra-level computer use and visual reasoning at 1/10 the price, ~9x lower cost per task than Claude Opus 5.5 at max effort.

## Benchmarks (per OpenAI)
- **Agents' Last Exam** (computer use): +15 pts over GPT-5.6 Terra at medium effort at ~1/3 cost; on par with GPT-6 Astra at 1/10 the price.
- **MMMU-Pro** (visual reasoning): beats GPT-5.6 Terra at every reasoning setting; nearly matches GPT-6 Astra / GPT-6.1 Sol.
- **OSWorld 2.1** (desktop app agents): surpasses GPT-5.6 Terra's best score at a fraction of the cost per task.
- **Factuality**: error rate 53.6% → 16.7% at low effort; 4.3% at max effort (near Astra/Sol).
- **Terminal-Bench 4.0**: 50.3% at max effort — more than double GPT-5.6 Terra's 21.5%. For the hardest coding, Sol/Astra remain the better choice.
- **Terminal-Bench-Science 0.1**: beats GPT-6.1 Sol at lower cost, within 5 pts of Opus 5.5 at <1/5 cost.
- **Throughput**: completes tasks over 3x faster than GPT-6 Astra and GPT-6.1 Sol.

## Notes
- The `-pro` variant (GPT-6.1 Terra Pro) is the same model served with `reasoning.mode=pro` at identical pricing.
- The `:batch` variants are ~50% discounted batch endpoints ($0.50/$2.50).
