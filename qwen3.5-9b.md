---
model: Qwen3.5-9B
organization: Alibaba / Qwen
license: Apache 2.0
release_date: 2026
last_updated: 2026-07-04
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

## Notes
- 8.8M downloads — most downloaded model in this tracker
- Dense (not MoE) — simpler deployment
- Good for lightweight tasks, tool-calling, agents
