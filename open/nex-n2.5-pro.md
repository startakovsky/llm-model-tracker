---
model: Nex N2.5 Pro
organization: Nex AGI
license: Apache 2.0
release_date: 2026-09-09
last_updated: 2026-10-09
sources:
  - https://huggingface.co/nex-agi/Nex-N2.5-Pro
  - https://openrouter.ai/nex-agi/nex-n2.5-pro
---

# Nex N2.5 Pro

Open agentic model from Nex AGI (Apache-2.0 weights on HuggingFace). Built to turn goals into working, verified outcomes — its core strength is **agentic coding inside a visual feedback loop**: it can explore codebases, make multi-file edits, then verify the result against screenshots. Surfaced on OpenRouter Sep 2026 with real community buzz (33K HF downloads, 675 likes, GGUF/MLX quants within the same week).

## Architecture
- **Modality:** text + image input -> text output
- **Tokenizer:** Qwen3
- **Context length:** 262,144 (256K) on OpenRouter; max completion 235,929 (~230K)
- **Weights:** ~397GB BF16 (nex-agi/Nex-N2.5-Pro on HuggingFace)
- **Family:** Nex-N2.5 line also includes N2.5-Mini (smaller, 16GB-local) and N2.5-Max (largest, on HF only)

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (nex-agi/nex-n2.5-pro) | $0.075 | $0.25 | 262,144 | Live since ~Sep 9, 2026 |

## Quality Assessment
Positioned as an agentic computer/browser-use + coding model rather than a raw frontier benchmark chaser. Value is in the verification loop (screenshot-driven self-checking of code edits) at a very low price — $0.075/$0.25 puts it at the cheap end of open agentic models. Community tests (YouTube, r/LocalLLaMA) focus on its browser/computer-use agent skills; not a GLM-5.3/Kimi-K3 frontier competitor on coding benchmarks.

## Notes
- Open-weights commitment: Nex releases both Pro and Mini variants open-source (Apache-2.0).
- GGUF/MLX quants by community within days of release (abenzerps, mradermacher, orcarouter repos).
- Listed on OpenRouter at $0.075/$0.25 (not the $0 free intro some posts claimed); mini sibling is cheaper.
- Classified `open` (Self-hostable).
