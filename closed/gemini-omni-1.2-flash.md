---
model: Gemini Omni 1.2 Flash
organization: Google
license: Proprietary
release_date: 2026-11-05
last_updated: 2026-11-06
---

# Gemini Omni 1.2 Flash

Google's video-generation/editing model, generally available Nov 5, 2026. Native 15-second video generation and editing, stronger consistency, ~30% lower pricing than the Omni 1.1 Flash line. Multimodal (video + image + text).

## Availability
- Closed API. `google/gemini-omni-1.2-flash` on OpenRouter at $1.50/$9.00 per M, 131K ctx.

## Classification
`closed` (Proprietary). Quality score 70 — specialized video-gen model, tracked because it's a major Google release with real OpenRouter pricing.

## Notes
- Video-gen model, not an LLM — relevant if you need generated/edited video in agent pipelines.
- Predecessor `google/gemini-omni-1.1-flash` (Nov 4) sits at the same OpenRouter price; 1.2 supersedes it.
- GA announcement on Google Cloud blog + blog.google (Nov 5).
