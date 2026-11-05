---
model: Ripple-65B Preview
organization: Ricursive Intelligence
license: Apache 2.0
release_date: 2026-11-04
last_updated: 2026-11-05
sources:
  - https://www.ricursive.com/ripple
  - https://openrouter.ai/ricursiveai/ripple-65b-preview
  - https://huggingface.co/ricursiveAI/Ripple-65B-Preview
---

# Ripple-65B Preview

First model from Ricursive Intelligence (Anna Goldie's new full-stack AI lab), released Nov 4, 2026. A 65B dense model **pretrained from scratch on 12 trillion tokens**, post-trained for agentic coding with native tool calling. Claims a new U.S. open-weight SOTA on agentic coding (80.5% Terminal-Bench 2.1, 79.1% SWE-Bench Pro v2.0) despite being a relatively compact dense model. Apache 2.0.

## Architecture
- **Total params:** 65B (dense — no MoE)
- **Context length:** 1,048,576 (1M), max completion 131,072
- **Modality:** text -> text
- Native tool calling; served in BF16 on OpenRouter
- Pretrained from scratch on 12T tokens (~$32M compute per lab)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (ricursiveai/ripple-65b-preview) | $0.20 | $0.60 | 1,048,576 | Live Nov 4 at launch pricing |

## Quality Assessment
Early days (launch week), so mostly self-reported benchmarks and community enthusiasm. Claimed numbers are striking for a 65B dense:

- **Terminal-Bench 2.1: 80.5%** and **SWE-Bench Pro v2.0: 79.1%** — lab claims "new U.S. open-weight SOTA on agentic coding"
- Native tool calling is the core design (agent-first, not chat-first)
- r/LocalLLaMA + X buzz on launch; GGUF quants (AtomicChat) same day, so local testing is easy

At $0.20/$0.60 on OpenRouter it's priced like a lightweight model despite 65B params. If the agentic claims hold up under third-party replication it's a remarkable price/performance entry in the self-hostable class — roughly GPT-6 Luna tier pricing with frontier-agentic ambitions. Treat as unverified until independent evals land.

## Notes
- Ricursive is a hardware+AI lab co-optimizing model and silicon (per their site); Ripple is their first model.
- Apache 2.0 weights, no gating — same license class as Qwen/GLM/DeepSeek.
- Classified `open`, Self-hostable (65B dense needs ~2x H100/1x H200-class node, but GGUF quants bring it down).
