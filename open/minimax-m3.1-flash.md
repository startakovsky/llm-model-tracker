---
model: MiniMax M3.1 Flash
organization: MiniMax AI
license: other (MiniMax; weights expected Oct 23)
release_date: 2026-10-19
last_updated: 2026-10-19
sources:
  - https://openrouter.ai/minimax/minimax-m3.1-flash:free
  - https://artificialanalysis.ai/models/minimax-m3-1-flash
---

# MiniMax M3.1 Flash

Released Oct 19, 2026 — the "Flash" fast sibling in the MiniMax M3 line, launched directly on a free OpenRouter endpoint. MiniMax tagline: "space performance + bunny speed." Weights expected on HuggingFace Oct 23.

## Architecture
- **Context length:** 1,048,576 (1M)
- **Positioning:** fast/cheap flash-tier model, successor interest within the open-weight MiniMax M3 family (M3 = 428B MoE, open weights)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (minimax/minimax-m3.1-flash:free) | $0 | $0 | 1,048,576 | Free preview endpoint; paid pricing TBA |

## Quality Assessment
Day-one assessment is thin: the free endpoint exists, benchmarks are not yet public, and weights land Oct 23. Positioned as the efficient flash member of an open frontier family — the pattern that made GLM-5-Flash/4.7-Flash useful self-hosting picks. Quality score 72 provisional, to revise once eval data lands.

## Notes
- Weights expected Oct 23 per MiniMax's announcement (Reddit r/LocalLLaMA Oct 19)
- Watch for a paid non-free endpoint to appear within days of the free launch