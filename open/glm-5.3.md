---
model: GLM-5.3
organization: Z.ai (Zhipu AI)
license: MIT
release_date: 2026-08-14
last_updated: 2026-08-19
sources:
  - https://the-decoder.com/zhipu-ai-releases-glm-5-3-claims-its-the-strongest-open-weights-coding-model/
  - https://www.marktechpost.com/2026/08/14/z-ai-ships-glm-5-3-without-retraining-the-base-model-better-at-complex-coding-and-long-horizon-tasks/
  - https://venturebeat.com/technology/glm-5-3-hits-the-api-at-1-4-4-4-per-million-tokens
---

# GLM-5.3

Released August 14, 2026. Reuses the same 743B (753B/40B MoE) base model as GLM-5.2 — every capability gain comes from extended post-training (more task environments, more environment types, longer training). Z.ai calls it the most powerful open-weights coding model, with the biggest jumps on long-horizon agentic tasks.

## Key signals (vendor-reported, launch day)
- Same base as GLM-5.2, all gains from post-training.
- Terminal-Bench 3.0: 4.6 → 28.3 (vs GLM-5.2).
- DeepSWE v1.1: 46.2 → 66.9.
- Agents' Last Exam (CLI): 23.8 → 28.5.
- GDPval-AA v2: 1,769 (spans 44 occupations).
- Z.ai Code Bench (internal): ~50% improvement over GLM-5.2; 31.4% at ~50K output tokens/task (Claude Opus 4.8: 29.5% at 120K; Claude Fable 5 leads at 39.5%).
- Cybersecurity (unplanned capability): CyberGym 77.2% → 84.5% (edges Mythos 5 at 83.8% and GPT-5.6 Sol at 83.6%). ExploitBench 24.4% → 54.4% (Mythos 5 at 78.0%). Found 2,436 real vulnerabilities across 269 projects.

## Availability
- **Now:** Z.ai API, GLM Coding Plan, ZCode — works with Claude Code / OpenCode.
- **OpenRouter:** **Live Aug 19 at $1.40/$4.40 per M** (prompt/completion, 1M ctx). Artificial Analysis Intelligence Index ~59.5 (in line with GPT-5.6 Sol ~60).
- **Weights:** expected within ~1 week of API launch (security review); not public yet.

## Classification
`open` (GLM family is MIT open-weights; weights pending security review). Quality score 91 — positioned ahead of GLM-5.2 (90) given the post-training gains, but weights/independently-verified benchmarks are still pending.

## Sources
- the-decoder: https://the-decoder.com/zhipu-ai-releases-glm-5-3-claims-its-the-strongest-open-weights-coding-model/
- marktechpost: https://www.marktechpost.com/2026/08/14/z-ai-ships-glm-5-3-without-retraining-the-base-model-better-at-complex-coding-and-long-horizon-tasks/
