---
model: Qwen4-Max Preview
organization: Alibaba
license: Proprietary
release_date: 2026-11-11
last_updated: 2026-11-11
sources:
  - https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview
  - https://technode.com/2026/11/11/alibaba-opens-qwen4-max-preview-with-a-million-token-context-window/
  - https://modelfit.io/blog/qwen4-max-preview-cloud-only-no-weights/
---

# Qwen4-Max Preview

First model of Alibaba's next-generation Qwen4 family, announced Nov 11, 2026. Next-gen flagship multimodal model built for coding, office work, frontend design, and agentic tasks. Cloud-only — no weights, no parameter count published.

## Availability
- Alibaba Cloud Model Studio only: Token Plan subscription (no pay-as-you-go, no per-token price).
- Also early access in the Qwen app, Qoder, QwenWork, QwenStudio (TechNode).
- NOT on OpenRouter (0/0 placeholder in this tracker).
- Preview window: 10:00 Nov 11 to 24:00 Nov 25, 2026 (UTC+8), then retired.

## Specs
- Input: text, images, video. Context: 1M tokens.
- Max output 393,216 tokens, shared by thinking and final answer (`max_tokens` now counts both — API-breaking detail).
- Thinking on by default; `reasoning_effort` low/medium/xhigh (default xhigh).
- Tools: function calling, web search, built-in tools, JSON Object/Schema outputs.
- API compatibility: OpenAI Chat Completions, Responses, and Anthropic Messages.

## Missing / unknowns
- No weights (nothing named Qwen4 on HuggingFace as of Nov 11).
- No parameter count, no per-token price, no published benchmarks, no license, no technical report.
- Wider Qwen4 launch, other sizes, and open-weights plans unconfirmed (Qwen 4.5 / Qwen 5 projected to 5-10T params per Apsara Conference roadmap).

## Quality assessment
Flagship positioning but zero verifiable data at launch — no weights, benchmarks, or pricing. Tracker quality score 78 reflects family positioning, not evidence. The closest local Qwen4 is Qwen3.8-Flash-Next (open weights, Qwen4 architecture preview).
