---
model: Ornith-1.5-122B
organization: Ornith AI
license: MIT
release_date: 2026-10-16
last_updated: 2026-10-31
sources:
  - https://huggingface.co/ornith-ai/Ornith-1.5-122B
  - https://ornith.ai/ornith_1_5.html
---

# Ornith-1.5-122B

Released Oct 16, 2026 — most capable member of the Ornith-1.5 family (122B MoE), built on Qwen3.5 + Gemma4 continued pretraining. Ornith's differentiator is end-to-end self-improvement: the training loop jointly optimizes task generation, scaffold construction, and solution rollouts via reinforcement learning rather than a fixed human-curated task set.

## Architecture
- **Total params:** ~122B MoE (Qwen3.5-MoE architecture)
- **Context length:** 262,144 (256K)
- **Architecture:** Qwen3.5 MoE for conditional generation
- **Modality:** text in / text out (tool calling supported)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter | — | — | — | Not listed (self-host / HF) |

## Quality Assessment
A 122B-class MoE designed for single-GPU deployment, with a quantized mobile/edge variant (Ornith-1.5-122B-Mobile). Real traction: 134K HF downloads, 204 likes, multiple independent community quants (EXL3, DFlash2, NVFP4) within days of release, plus official GGUF builds that run in Ollama and llama.cpp. As a continued-pretraining derivative of Qwen3.5/Gemma4 rather than a from-scratch model, treat it as a strong agentic fine-tune family rather than a new base architecture — but the self-improvement training loop is genuinely novel and worth watching.

## Notes
- MIT license; open weights on HuggingFace (`ornith-ai/Ornith-1.5-122B`, GGUF at `ornith-ai/Ornith-1.5-122B-GGUF`).
- OpenAI-compatible API endpoint with tool calling; Ollama `ollama run ornith-1.5:122b`.
- Not on OpenRouter as of Oct 31, 2026 — self-host only.
