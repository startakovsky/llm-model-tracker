---
model: GLM-5.3-FlashX Legal
organization: Z.ai
license: Proprietary (weights not yet public; base GLM-5.3-FlashX is MIT)
release_date: 2026-11-02
last_updated: 2026-11-02
sources:
  - https://openrouter.ai/z-ai/glm-5.3-flashx-legal
  - https://ai-sdk.dev/playground/zai:glm-5.3-flashx-legal
---

# GLM-5.3-FlashX Legal (GLM-Legal)

Z.ai's legal-domain variant of GLM-5.3-FlashX, live on OpenRouter Nov 2, 2026. Built on the same native multimodal (text + image + video -> text) FlashX base with additional legal-domain mid-training and post-training with reinforcement learning. Optimized for contract review, evidence analysis, and compliance research.

## Availability
- Closed/API-only as of Nov 2 — no Z.ai weights repo on HuggingFace (only unofficial third-party FlashX quants).
- `z-ai/glm-5.3-flashx-legal` on OpenRouter at **$0.37/$1.25 per M**, 1M ctx, 131K max output — identical pricing to the base GLM-5.3-FlashX.
- Cached input $0.075/M.

## Classification
`closed` (Specialized). Quality score 75 — same fast 200-tok/s FlashX engine with a legal-specialist RL post-training; a niche-domain pick for contract/compliance work rather than a general-purpose frontier model. If weights land, this becomes a self-host candidate for sensitive legal documents.

## Notes
- Multimodal input (docs + images + video) inherited from the FlashX base — useful for scanning contracts, exhibits, and evidence files.
- GLM-5.3-FlashX family continues Z.ai's pattern of domain variants alongside the main line (cf. GLM-5.3-Flash).
