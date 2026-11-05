---
model: Kimi K3.1 Pro
organization: Moonshot AI
license: other (Moonshot open-weights release, Nov 4 2026)
release_date: 2026-10-23
last_updated: 2026-11-05
sources:
  - https://huggingface.co/moonshotai/Kimi-K3.1-Pro
  - https://openrouter.ai/moonshotai/kimi-k3.1-pro
---

# Kimi K3.1 Pro

Moonshot AI's most capable 3T-class model, launched Oct 23, 2026 as API-only. **Weights released Nov 4, 2026** on HuggingFace (`moonshotai/Kimi-K3.1-Pro`, 2.8T/104B MoE, ungated, 11.7K downloads / 809 likes day-1). Now the **highest-scoring open-weights model** on the Artificial Analysis Intelligence Index (55), closing the open-vs-closed gap from 12 points to 3.

## Availability
- `moonshotai/kimi-k3.1-pro` on OpenRouter at **$2/$10 per M** (cached input **$0.20/M**), 1M ctx.
- Open weights on HF (ungated Nov 4): 2.8T total / 104B active MoE, natively multimodal agentic (text+image). r/LocalLLaMA reports 30–120 t/s prefill on big iron.
- Pricing is 33% below Kimi K3 on all three rates — matches GPT-6.1 Sol, half of Claude Opus 5.5.
- A "Highspeed" tier is 2–3x faster at 2x price (except cache hits, priced the same).

## Classification
`open` as of Nov 4, 2026 (weights live). Quality score 95 — #4 on the AA Intelligence Index (55), the leading open-weights model against the frontier, trailing only Claude Opus 5.5 (58), Claude Sonnet 5.5 (56), and Muse Wonder Full (56).

## Benchmarks (per Artificial Analysis, Oct 23)
- **AA Intelligence Index 55** — +11 points over Kimi K3 (max, 44).
- **GDPval-AA: 1,846 Elo (3rd)** — +312 Elo over K3; behind only Claude Opus 5.5 (1,866) and Muse Wonder Full (1,857).
- **Terminal-Bench 4.0: 67% (highest of any model)** — up from 13% for K3, ahead of Claude Sonnet 5.5 (64%).
- **AutomationBench-AA: 73%** — up from 58% for K3.
- **HLE 52%** (from 47%), **CritPt 25%** (from 23%), **SciCode 61%** (from 59%).
- **AA-Omniscience 30** (from 20); hallucination rate falls 53% → 44%, accuracy 48% → 51%.
- **Cost/task ~$1.98** — roughly equal to K3: 14% more output tokens (55K vs 48K) but 33% lower first-party token prices.

## Notes
- 2.8T total / 104B active parameters, 1M ctx, text+image input.
- Moonshot's own benchmarks show it approximately level with Claude Opus 5.5 and GPT-6 Astra — ahead on a few, close on others.
- First open-weight model to score this highly against the closed frontier — the open-vs-closed gap is now 3 points.
