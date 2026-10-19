---
model: Glimpse
organization: Elorian
license: Proprietary
release_date: 2026-10-16
last_updated: 2026-10-19
sources:
  - https://openrouter.ai/elorian/glimpse
  - https://elorian.ai/blog/introducing-glimpse
  - https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/
---

# Glimpse

Elorian's first model (launched Oct 16, 2026, TechCrunch-covered). A vision-reasoning model positioned around "reasoning with images, not just about them" — i.e., using image representations inside the reasoning process rather than only describing images.

## Architecture
- **Context length:** 262,144 (262K)
- **Positioning:** multimodal reasoning, vision-forward

## API Providers
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (elorian/glimpse) | $0.60 | $3.00 | 262,144 |
| Together AI | $0.60 | $3.00 | 262,144 |

## Quality Assessment
First-gen model from a new lab; tracked for the TechCrunch buzz and the distinctive vision-reasoning angle rather than proven benchmark dominance. At $0.60/$3.00 it sits mid-pack — cheaper than frontier priced-models, pricier than commodity flash models. Treat as a "watch this space" entry until independent eval data lands. Quality score 78 is provisional.

## Notes
- Closed API only; no weights on HuggingFace as of Oct 19
- Distributed through Together AI as well as OpenRouter