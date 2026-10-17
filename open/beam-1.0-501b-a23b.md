---
model: Beam 1.0 501B A23B
organization: Reflection AI
license: Apache-2.0
release_date: 2026-10-16
last_updated: 2026-10-17
sources:
  - https://openrouter.ai/reflection/beam-1.0-501b-a23b
  - https://huggingface.co/reflection/Beam-1.0-501B-A23B
  - https://huggingface.co/blog/reflection-beam
---

# Beam 1.0 501B A23B

Released Oct 16, 2026 — the debut model from **Reflection AI**, a new US lab. A large sparse mixture-of-experts model purpose-built for coding, reasoning, and long-horizon agentic workloads.

## Architecture
- **Total params:** 501B
- **Active params per token:** 23B
- **Context length:** 1,048,576 (1M)
- **Architecture:** sparse MoE, 52 layers, 512-token cross-entropy grouping per layer
- **Modality:** text in / text out

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (reflection/beam-1.0-501b-a23b) | $1.00 | $3.00 | 1,048,576 | Oct 16: launch pricing |

## Quality Assessment
New large open-weight reasoning/coding model from a fresh US lab. 501B total / 23B active lands it in frontier-open territory (same parameter class as GLM-5.x), with day-0 support in both vLLM and Ollama for easy self-hosting. Apache-2.0 license and 1M context. Positioned as a coding / long-horizon agentic workhorse; watch for independent benchmarks before treating it as a frontier leader — it's a first release without a track record.

## Notes
- Apache-2.0; open weights on HuggingFace (`reflection/Beam-1.0-501B-A23B`, 1148 downloads / 126 likes).
- Day-0 deployment support: vLLM, Ollama, Cloudflare Workers AI, recipes.vllm.ai.
- From the HF blog: "a 501B open model you can own, customize, and control."