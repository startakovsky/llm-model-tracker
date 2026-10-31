---
model: Nanbeige4.3-33B
organization: Nanbeige
license: Apache-2.0
release_date: 2026-10-24
last_updated: 2026-10-31
sources:
  - https://huggingface.co/Nanbeige/Nanbeige4.3-33B
---

# Nanbeige4.3-33B

Released Oct 24, 2026 — flagship teacher-agent model of the Nanbeige4.3 series, built as a high-capacity teacher to anchor distillation of agentic capabilities into smaller models (3B class next). Claims state-of-the-art agentic performance among open ~30B models.

## Architecture
- **Total params:** 33B (dense)
- **Context length:** 524,288 (512K, native)
- **Architecture:** Llama-style (52 layers, hidden 7168, GQA 8 KV heads)
- **Modality:** text in / text out

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter | — | — | — | Not listed (self-host / HF) |

## Quality Assessment
Self-reported agentic benchmarks put it ahead of the current open ~30B pack: Terminal-Bench 2.1 80.9 (vs Qwen3.8-27B 73.0, Muse Glimmer 30B 61.8, Gemma 4 31B 47.2), DeepSWE 65.5 (vs 42.5 / 4.4 / 2.7), SWE-Bench Pro 60.3 (vs 61.7 / 51.2 / 36.9). If the claims hold, it's the best ~30B open agentic model at self-hostable cost — worthwhile for local agentic/coding workloads where a 33B dense fits on a single GPU. First-week traction (833 HF likes, 13.8K downloads) confirms community interest. Treat vendor benchmarks with caution until third-party confirmation.

## Notes
- Apache-2.0, open weights on HuggingFace (`Nanbeige/Nanbeige4.3-33B`, base variant `Nanbeige4.3-33B-Base`).
- EN + ZH languages.
- Not on OpenRouter as of Oct 31, 2026 — self-host only.
