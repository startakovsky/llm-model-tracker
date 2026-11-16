---
model: Qwen4 Max
organization: Alibaba
license: Proprietary
release_date: 2026-11-16
last_updated: 2026-11-16
sources:
  - https://mlq.ai/news/alibaba-launches-qwen4-max-saying-it-cuts-task-costs-by-about-60-with-tighter-cyber-guardrails
  - https://thenextweb.com/news/alibaba-launches-qwen4-max-flagship-ai-model-without-open-weights
  - https://news.sulat.com/2026/11/16/qwen4-max-launch
---

# Qwen4 Max

Alibaba's next-generation Qwen4 flagship, GA'd Nov 16, 2026 — the first full Qwen4 family release, following the Nov 11 Qwen4-Max-Preview (Token-Plan only). This is the real per-token launch: $1.50/$4.50 on OpenRouter, 1M context.

## Availability
- OpenRouter id `qwen/qwen4-max` at $1.50/$4.50 per M, 1M ctx, live Nov 16.
- QwenCloud API, Qwen Studio, QwenWork, Qoder apps.
- Cloud-only: weights closed. Alibaba says smaller Qwen4 models will get open weights, no date given.

## Specs
- Sparse MoE: 2.4T backbone params, 71B active per token + 328B N-gram embedding params.
- Architecture: Gated DeltaNet layers mixed with a new sparse attention scheme (cuts long-context cost).
- Input: text + image + video. Context: 1M tokens. Reasoning on by default.
- Cached input reads $0.075/M.

## Benchmarks (Alibaba-reported, not independently verified)
- Work360 (26 domains/721 fields): 52.69 vs Qwen3.8-Max 47.74; uses ~24-35% fewer tokens at high/xhigh effort, ~48-49% fewer on Terminal-Bench 4.0.
- Average cost/task on Work360: $4.43 (Qwen3.8-Max) -> $1.67 (-62%).
- DeepSWE v1.1: 75.7 (just ahead of Claude Opus 5.5's 74.2).
- Terminal-Bench 4.0: 48.5 (behind Opus 5.5 59.6 and Kimi K3.1 67.2).
- Bloomberg-reported: near top of coding benchmarks, beating Claude Fable 5.1 and Kimi K3.1 Pro (per Alibaba's own charts).

## Safety
- Removed training data aimed at offensive cyber tasks; kept defensive data (vulnerability verification/detection/remediation).
- Added dedicated CBRN safety training.
- Secure-coding test pass rate (functionality + security): 22.0% -> 31.8%.

## Quality assessment
Frontier flagship, list-priced 25% below Qwen3.8-Max ($1.50 vs $2.00 input) with ~62% lower cost/task on Alibaba's own benchmark — genuinely cheaper work per dollar. Coding strong (DeepSWE ahead of Opus 5.5) but Terminal-Bench 4.0 notably weak (48.5), so agentic-terminal work lags the top tier. No weights, no independent verification of benchmarks yet. Score 85 reflects flagship positioning + credible pricing, not verified parity with Fable 5.2/Gemini 4 Carbon.
