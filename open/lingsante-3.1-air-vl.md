---
model: LingSante 3.1 Air VL
organization: inclusionAI
license: MIT
release_date: 2026-11-19
last_updated: 2026-11-26
sources:
  - https://openrouter.ai/inclusionai/lingsante-3.1-air-vl
  - https://huggingface.co/inclusionAI/LingSante-3.1-air-VL
---

# LingSante 3.1 Air VL — inclusionAI

| Field | Value |
|---|---|
| **Org** | inclusionAI (Ant Group healthcare team) |
| **OpenRouter ID** | `inclusionai/lingsante-3.1-air-vl` |
| **License** | MIT (weights on HF) |
| **Release date** | 2026-11-19 (HF) / 2026-11-26 (OpenRouter) |
| **Pricing** | $0.06/$0.18 per M |
| **Context** | 131,072 on OpenRouter (256K native w/ YaRN) |
| **Category** | Specialized (open) |

## Architecture

- 124B total / 5.5B active per-token MoE (`bailing_moe_v3_vl`), natively multimodal text+image, built on Ling-3.0-flash-VL.
- 256K ctx native (OpenRouter lists 131K); MTP (NEXTN) speculative decoding, long-context/YaRN optimizations.

## Specialty: Real-world healthcare

First large multimodal medical model released open-source by Ant Group's healthcare team. Four clinical focus areas:

1. **Medical imaging reports** — systematic image review, weighted differentials, Findings/Impression; 8–9 finding types on a single chest X-ray (cardiomegaly, pleural effusion, atelectasis, consolidation, pneumonia, pneumothorax).
2. **Multimodal health assessment** — 120+ skin diseases with multi-turn history-taking; diet/nutrition analysis; medical report interpretation (links blood counts with inflammatory/immune markers).
3. **Medical search & evidence synthesis** — image-to-image search, guidelines/case retrieval, bounding-box lesion verification; traceable image→search→evidence→answer.
4. **Medical GUI agents** — appointments, medication purchases (spec selection, prescriptions, pop-up handling) — evaluated on real apps.

Retains general capabilities: multimodal, OCR, document/chart understanding, tool use. Research model; **not a medical device**.

## Quality Assessment

Narrowly-specialized (medical) but cheap given size: $0.06/$0.18 for a 124B-class MoE, MIT-licensed and self-hostable on 4×141GB-class GPUs via SGLang (TP4). Deep evaluation is domain-limited — use for medical reasoning/health-assistant tasks, not a general-purpose frontier pick. Score 68.

## Sources
- https://openrouter.ai/inclusionai/lingsante-3.1-air-vl
- https://huggingface.co/inclusionAI/LingSante-3.1-air-VL