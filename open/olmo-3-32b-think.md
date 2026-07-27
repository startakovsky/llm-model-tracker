---
model: Olmo 3 32B Think
organization: allenai
license: Apache 2.0
release_date: 2025-11-19
last_updated: 2026-07-27
openrouter_id: allenai/olmo-3-32b-think
category: Lightweight
generated: stub-from-csv
---

# AllenAI: Olmo 3 32B Think

Open-weight reasoning model from **allenai** (Allen Institute for AI). Weights on HuggingFace.

## Quick Facts
- **OpenRouter ID:** `allenai/olmo-3-32b-think`
- **Context length:** 64K
- **License:** Apache 2.0
- **Category:** Lightweight
- **Quality score:** 56/100
- **Notes:** 32B dense reasoning model. Fully-open (data+recipe+weights). 173 HF likes. 11K downloads

## API Providers
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (allenai/olmo-3-32b-think) | $0.1500 | $0.5000 | 64K |

## Self-Hosting
OLMo is one of the few truly fully-open model families (open data, open training code, open weights). The 32B Thinking variant runs as a dense 32B model — feasible on a single 80GB GPU (e.g. A100/H100) at FP16, or a 48GB-class consumer GPU with INT4/AWQ quantization. Confirm exact architecture and any available GGUF quants on the HuggingFace model card before speccing hardware.

## Quality Assessment
Quality score 56/100 — lightweight / mid-tier open reasoning model. As a fully-open 32B dense reasoning model from AllenAI, OLMo 3 emphasizes reproducibility and openness over raw benchmark leadership; it trails frontier open models like GLM-5.2 and Kimi K3 but is a credible fully-transparent alternative in the 32B class.

> This is an auto-generated stub derived from `models.csv` to keep README links valid. Enrich with architecture, GGUF quants, and benchmarks as the model gains traction.
