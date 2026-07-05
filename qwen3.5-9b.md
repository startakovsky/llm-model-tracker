---
model: Qwen3.5-9B
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026
last_updated: 2026-07-05
---

# Qwen3.5-9B

## Architecture
- **Total params:** 9B (dense)
- **Context length:** 262,144

## Self-Hosting
- GGUF (unsloth): Q4 ~5GB — runs on anything
- MLX 4-bit available
- Even a Raspberry Pi can run this

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (qwen/qwen3.5-9b) | $0.10 | $0.15 | 262,144 | 8.8M downloads |

## Quality Assessment
Qwen3.5-9B is the most downloaded model in this tracker (8.8M downloads). As a dense 9B model, it's surprisingly capable for its size — good for chat, simple tool-calling, and basic coding. Not suitable for complex reasoning, long agentic chains, or deep coding work. Its value is in being able to run anywhere at minimal cost. Use as a fallback or edge model, not a primary workhorse.

## Notes
- Dense (not MoE) — simpler deployment
