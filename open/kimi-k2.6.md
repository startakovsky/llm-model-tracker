---
model: Kimi K2.6
organization: Moonshot AI
license: other
release_date: 2026-04-20
last_updated: 2026-07-11
---

# Kimi K2.6

## Architecture
- **Total params:** ~1T (MoE)
- **Active params per token:** ~32B
- **Context length:** 262,144
- **Modality:** Text + Image → Text
- **Architecture type:** Mixture-of-Experts, native multimodal

## Pricing (OpenRouter)
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (moonshotai/kimi-k2.6) | $0.66 | $3.41 | 262,144 |

## Quality Assessment
Kimi K2.6 is Moonshot AI's next-generation multimodal model succeeding K2.7. Designed for long-horizon coding, coding-driven UI/UX generation, and multi-agent orchestration. Handles complex end-to-end coding tasks across Python, Rust, and Go. The successor to K2.7 (already tracked), offering improved multimodal capabilities and multi-agent orchestration. At $0.66/$3.41/M, it's competitively priced against GLM-5.2 ($0.35/$1.10) but higher — quality parity is yet to be independently benchmarked.

## Notes
- Open weights on HuggingFace (1.7M downloads, 1508 likes)
- Native multimodal (text + image input)
- Strong in long-horizon coding tasks across multiple languages
