---
model: Mistral Large 4
organization: Mistral AI
license: Apache 2.0 (expected; weights drop end of Oct 2026)
release_date: 2026-10-06
last_updated: 2026-10-06
sources:
  - https://mistral.ai/news/mistral-large-4/
  - https://openrouter.ai/mistralai/mistral-large-4-0
---

# Mistral Large 4 (ML4 / "Le Chonk")

Released Oct 6, 2026 — Mistral's largest and most capable model ever: a 1-trillion-parameter, 49B-active natively multimodal (text + image) MoE. Trained from scratch on 3,800 NVIDIA Grace Blackwell GPUs in Mistral's own European datacenters. Public preview on Mistral Studio + OpenRouter; **weights drop end of October 2026** (Apache 2.0 expected).

## Architecture
- **Total params:** 1T (sparse MoE)
- **Active params per token:** 49B
- **Context length:** 524,288 (512K) on OpenRouter; max completion 262,144
- **Modality:** text + image input -> text output
- **Multimodal:** native, includes visual grounding (surpasses GPT-6 Astra on Dense 200: 42% vs 41%)
- Trained from scratch; 160+ languages (incl. every official EU language)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| Mistral Studio (list) | $1.36 | $4.18 | 524,288 | Launch list pricing |
| OpenRouter (mistralai/mistral-large-4-0) | $0.68 | $2.09 | 524,288 | Oct 6 launch preview price (~half Mistral list) |

## Quality Assessment
Positioned as the strongest open-weight model outside China — state-of-the-art among open weights on cybersecurity, finance, and law, and competitive with the global open frontier on coding/agentic work:

- **Coding Agent Index 49.8%** — ahead of DeepSeek V4 Pro 0813 and Qwen3.8 Max (DeepSWE v1.1 61.7%, SWE-Atlas-QnA 59.4%, Terminal-Bench 4 28.3%)
- **Cybersecurity:** top-5 globally on Artificial Analysis AI Cyber Index; 82% on vuln-reproduce-and-patch (highest of any model); 93% Cybench. Closed models (Opus 5.5, GPT-6 Astra) score near zero here due to refusals — ML4's open weights remove that constraint.
- **Agentic workflows:** AutomationBench 59.9% (ahead of Kimi K3, MiMo-V2.6-Pro, DeepSeek V4 Pro); AA-Briefcase 1,393 Elo
- **Blind human eval (Surge AI):** ranked 2nd of 5 (3.74), ahead of Kimi K3 (3.59), GLM-5.3 (3.60), GLM-5.2 (3.40), behind only Claude Opus 5 (4.22)
- **Safety:** 93.3% on Lakera B3 (highest among competitors); KORA 1.691 (Mistral's highest)
- **Math/Science:** SOTA open-weight on SciCode-Verified; one-shot full Hartree–Fock chemistry simulation

At $0.68/$2.09 on OpenRouter it undercuts GLM-5.3 ($0.07/$7) and Kimi K3 ($0.83/$14) on prompt price while competing at the frontier — a strong European self-host candidate once weights drop. Cost/quality tradeoff: roughly GLM-5.3/Kimi-K3-class agentic capability at a fraction of the completion cost.

## Notes
- Nicknamed "le Chonk" by Mistral.
- Trained on Mistral's own infrastructure; €3B Series D (largest equity round ever by a European tech company) funding further scale-up.
- Will be the foundation for a new generation of specialized Mistral models.
- Classified `open` (announced open-weight, Apache 2.0 planned) — weights not yet on HuggingFace as of Oct 6; verify on release.
