---
model: MiMo-V2.6-Flash MOPD
organization: Xiaomi
license: MIT
release_date: 2026-11-23
last_updated: 2026-11-25
sources:
  - https://openrouter.ai/xiaomi/mimo-v2.6-flash-mopd
  - https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD
---

# MiMo-V2.6-Flash MOPD — Xiaomi

| Field | Value |
|---|---|
| **Org** | Xiaomi |
| **OpenRouter ID** | `xiaomi/mimo-v2.6-flash-mopd` |
| **HuggingFace** | [XiaomiMiMo/MiMo-V2.6-Flash-MOPD](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD) (30K DL, 78 likes) |
| **License** | MIT (open weights) |
| **Release date** | 2026-11-23 |
| **Pricing** | $0.50/$1.00 per M (cached $0.05) |
| **Context** | 1,048,576 |
| **Category** | Lightweight (open) |

## Architecture

- Updated MOPD checkpoint of MiMo-V2.6-Flash: 309B total / 15B active MoE, 1M ctx, native multimodal input (text+image+video).
- Adds a multi-teacher RL upgrade over base Flash (per OR card).

## Quality Assessment

Variant of the open MiMo-V2.6-Flash line at ~3.6x the base price ($0.50/$1.00 vs $0.14/$0.28) — priced closer to the Pro tier. Open weights make the base Flash the value pick; MOPD targets upgraded-checkpoint consumers. Score 74.

## Sources
- https://openrouter.ai/xiaomi/mimo-v2.6-flash-mopd
