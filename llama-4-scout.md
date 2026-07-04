---
model: Llama 4 Scout
organization: Meta
license: Llama 4 Community License
release_date: 2026
last_updated: 2026-07-04
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

## Notes
- 10M context window is unique advantage
- License restrictions (Llama 4 Community License, not MIT/Apache)
- Limited self-hosting info — needs more research
