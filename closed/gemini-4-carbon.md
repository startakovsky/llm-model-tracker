---
model: Gemini 4 Carbon
organization: Google
license: Proprietary
release_date: 2026-11-10
last_updated: 2026-11-11
sources:
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
  - https://aistudio.google.com/docs/whats-new-gemini-4-carbon
  - https://openrouter.ai/google/gemini-4-carbon
---

# Gemini 4 Carbon

Google's strongest reasoning model, released Nov 10, 2026 — the second Gemini 4 family member after Argon (Oct 13). Built for sustained agentic workflows: complex software engineering, multimodal knowledge work, scientific reasoning, and cybersecurity defense.

## Availability
- OpenRouter id `google/gemini-4-carbon` at $2.00/$10.00 per M, 1M context (live Nov 10).
- Gemini API + Google AI Studio (paid tier); also in Gemini Managed Agents (Antigravity).
- Closed API (Proprietary) — no open weights.

## Pricing
- Introductory $2/$10 per M through Nov 30, 2026; standard $4/$20 after (same pattern as Argon).
- Implicit caching discounts cached input 95% ($0.10 intro, $0.20 standard).
- On OpenRouter at the intro rate $2/$10 — same as Argon, ~1/5 the cost of GPT-6 Astra ($10/$50).

## Capabilities
- Extended verification and agentic coding: deeper build-and-verify loops across complex repositories, frontend UI design, and 3D scenes.
- Higher-precision multimodal knowledge work: stronger source grounding with fewer unsupported claims across dense PDFs, spreadsheets, slides, workspace data; strict output-schema adherence.
- Scientific and cybersecurity reasoning: formal proofs, experimental data analysis, vulnerability discovery, root-cause patching (frontier cyber capabilities).
- Unified 1,048,576-token window shared by input, thinking, and output; long decode up to 1M output tokens (background execution); thinking levels low/medium/high.
- Carbon spends more thinking tokens per turn than Argon (explores hypotheses, verifies, checks edge cases) — higher per-turn token use and latency; Argon remains the faster, cheaper-per-turn choice for interactive coding.

## Benchmarks
- No independent index score published at launch; Google positions it as its strongest model, above Argon (#1 Vals Index, CWE-Bench v1 68% tie-first).

## Quality assessment
Frontier-class closed model and Google's current top reasoning tier, at the same intro price as Argon. At $2/$10 it undercuts GPT-6 Astra ($10/$50) and matches Claude Opus 5.5 ($4/$20) territory for sustained agentic work. Quality score 96.
