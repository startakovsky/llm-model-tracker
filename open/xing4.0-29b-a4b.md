---
model: Xing4.0-29B-A4B
organization: China Telecom (XingChen AGI)
license: Apache-2.0
release_date: 2026-10-16
last_updated: 2026-10-19
sources:
  - https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B
  - https://github.com/XingChen-AGI/Xing4.0-29B-A4B
  - https://www.modelscope.ai/models/XingChen-AGI/Xing4.0-29B-A4B
---

# Xing4.0-29B-A4B

Next-generation model in the Xing series (formerly TeleChat, from Tele-AI), developed by China Telecom AI. Released Oct 16, 2026 with strong early community traction: 43K HF downloads and ~1.9K likes within days.

## Architecture
- **Type:** 29B total / 4B active MoE (mHC + MLA + MTP architecture)
- **Context length:** 256K native (extensible to 512K); 262,144 on OpenRouter
- **Training:** first model at this scale trained entirely on Ascend NPU (910C) with MindSpore/MindFormers
- **Positioning:** agent-oriented — multi-step planning, tool calling, long-context reasoning chains; explicit adapters for OpenCode, Claude Code, OpenClaw, and Hermes

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (xingchen-agi/xing4.0-29b-a4b:free) | $0 | $0 | 262,144 | Free endpoint at launch; paid pricing TBA |

## Quality Assessment
A credible self-hostable agent-model candidate at 29B/4B: runs on consumer-class hardware, Apache-2.0, built for tool-calling and agent frameworks (the org explicitly ships Hermes/OpenCode adapters). Early Reddit/LocalLLaMA and MindStudio coverage is positive. Quality score 75 provisional — strong architecture story, benchmarks still settling.

## Notes
- Apache-2.0 weights on HuggingFace and ModelScope; GGUF variants already available (18K downloads)
- Compatible with vLLM, SGLang, KTransformers, LLaMA-Factory