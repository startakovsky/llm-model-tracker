---
model: DeepSeek V4 Pro 0813
organization: DeepSeek
license: MIT
release_date: 2026-08
last_updated: 2026-08-13
sources:
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
  - https://openrouter.ai/deepseek/deepseek-v4-pro-0813
  - https://news.ycombinator.com/item?id=49274600
---

# DeepSeek V4 Pro 0813

The official general-availability (GA) build of DeepSeek's frontier open-weight model, rolling out to the API on 2026-08-13. It drops from preview pricing (~$1.17/$2.34) to a strikingly cheap $0.435/$0.87 — reportedly equal-or-better benchmark results at a lower cost than the earlier V4 Pro preview build.

## Architecture
- Total params: 1.6T (MoE)
- Active params per token: 49B
- Architecture: DeepSeek V4 MoE (1.6T total)
- Context length: 1,048,576 (1M)
- License: MIT (open weights)
- Weights: deepseek-ai/DeepSeek-V4-Pro on HF (1.39M downloads, 5,434 likes)
- Latest: V4 Pro 0813 is the newest revision after the July 24 V4 GA and the earlier flash builds

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (deepseek/deepseek-v4-pro-0813) | $0.435 | $0.87 | 1M | New GA endpoint; cheaper than deepseek-v4-pro ($1.168/$2.336) |
| DeepSeek API | varies | varies | 1M | Peak/off-peak pricing introduced Aug 2026 |

Note: DeepSeek announced (Reuters, Aug 13) upcoming API price increases for V4-Pro/V4-Flash effective Aug 16, including peak/off-peak tiers — watch this if relying on the API route; the open weights are unaffected.

## Quality Assessment
Community reports and early benchmarks put V4 Pro 0813 ahead of Claude Opus 4.8 on Terminal-Bench 2.1 and CyberGym, while the same-cost/lower-cost framing ("equal to or even better than before, but at a lower cost") makes it the best cost/quality open frontier model available. It excels in cybersecurity-adjacent and agentic terminal work per SCMP's hands-on. As an open MIT model, the 1.6T/49B MoE is self-hostable but needs a large cluster; on API price it is now a fraction of GPT-5.6 Sol ($5/$30) and Claude Opus 5 ($5/$25).

**Agentic verdict:** DeepSeek V4 Pro 0813 is ~open-GLM-5.2-class reasoning/agentic strength at roughly half the cost of GLM-5.2's current $0.63/$1.98, and ~88-90 quality. It maintains DeepSeek's edge in cost-per-task while matching the leading closed labs on terminal agentic benchmarks — the strongest value open frontier model of the week.

## Sources
- Primary: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (MIT weights, downloads)
- GA / pricing: https://news.ycombinator.com/item?id=49274600, https://www.gmicloud.ai/en/blog/deepseek-v4-pro-steps-out-of-preview-the-0813-build-is-live
- Benchmarks: https://www.scmp.com/tech/big-tech/article/3363895 (bench footprint), OpenRouter model card
- Price policy: https://www.reuters.com/world/china/deepseek-raises-api-pricing-its-v4-models-2026-08-13