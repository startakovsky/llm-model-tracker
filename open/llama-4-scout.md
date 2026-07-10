---
model: Llama 4 Scout
organization: Meta
license: Llama 4 Community License
release_date: 2026
last_updated: 2026-07-08
---

# Llama 4 Scout

## Architecture
- **Total params:** ~109B (MoE)
- **Active params per token:** ~17B
- **Context length:** 10,000,000 (10M tokens — largest available)

## Self-Hosting
- Q4 estimated ~66GB (fits 96GB VRAM or 96GB+ RAM)
- Details on HuggingFace: https://huggingface.co/meta-llama/Llama-4-Scout

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (meta-llama/llama-4-scout) | $0.10 | $0.30 | 10,000,000 | Very cheap, huge context |

## Quality Assessment
Llama 4 Scout's unique advantage is the 10M token context window — no other model comes close. For coding quality and reasoning, it's a tier below GLM-5.2 and DeepSeek V4 Flash. At $0.10+$0.30/M, it's very cheap. Best used when you need extreme context length (entire codebases, massive documents) rather than peak reasoning quality. License restrictions limit commercial use compared to MIT/Apache alternatives.

## Notes
- 10M context window is unique advantage
- License restrictions (Llama 4 Community License, not MIT/Apache)
- Limited self-hosting info — needs more research
