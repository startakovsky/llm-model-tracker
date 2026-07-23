---
model: Gemini 3.5 Flash Lite
organization: Google
license: Proprietary
release_date: 2026-07-21
last_updated: 2026-07-22
---

# Gemini 3.5 Flash Lite

## Architecture
- **Context length:** 1,048,576 (1M)
- **Modality:** Text + Image + Video + File + Audio → Text
- **Architecture type:** High-efficiency multimodal model

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (google/gemini-3.5-flash-lite) | $0.30 | $2.50 | 1,048,576 |

## Quality Assessment
Gemini 3.5 Flash Lite is Google's high-efficiency model with upgraded agentic capabilities, released July 21, 2026. Specifically suited for subagents that execute focused tasks within complex, multi-agent workflows. At $0.30/$2.50 per M tokens, it is 5x cheaper than Gemini 3.6 Flash ($1.50/$7.50) and positioned as the subagent tier in Google's model lineup. Full multimodal support with 1M context. Supports reasoning, reasoning_effort, structured outputs, and tool use. Succeeds the older Gemini 3.1 Flash Lite ($0.25/$1.50) with higher pricing but upgraded capabilities. Ideal for high-volume agentic pipelines where cost per token matters most.

## Notes
- Released July 21, 2026 alongside Gemini 3.6 Flash
- Positioned as subagent tier for multi-agent workflows
- 5x cheaper than Gemini 3.6 Flash
- Full multimodal: text, image, video, file, audio input
- 1M context window
- Supports reasoning_effort parameter
- Closed-source (Gemini = closed per tracker classification)
