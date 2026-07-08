---
model: Kimi-K2.7-Code
organization: Moonshot AI
license: Other (Moonshot AI License)
release_date: 2026-06
last_updated: 2026-07-08
---

# Kimi K2.7 Code

Moonshot AI's specialized coding model. Built on the Kimi K2.5 architecture (MoE, 61 layers, 8 experts active). Native multimodal (image-text-to-text). Released June 2026 via OpenRouter and HuggingFace. Targets agentic long-horizon coding workflows.

## Architecture
- Total params: ~1T (est., based on K2.5 architecture)
- Active params per token: ~32B (8 experts active, est.)
- Architecture: KimiK25 (MoE, custom code)
- Layers: 61
- Hidden size: 7168
- Attention heads: 64, KV heads: 64 (MHA, not GQA)
- Intermediate size: 18,432
- Context length: 262,144 (256K)
- Multimodal: image-text-to-text
- License: "other" (Moonshot AI custom — check before commercial use)

## Self-Hosting
### GGUF (llama.cpp via unsloth/Kimi-K2.7-Code-GGUF)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| UD-IQ1_M | ~135 GB (8 shards) | ~150 GB | Extreme quant, requires 192GB RAM |
| UD-IQ2_M | ~165 GB (8 shards) | ~185 GB | Better quality |
| UD-IQ2_XXS | ~145 GB | ~165 GB | Smallest usable |
| BF16 | ~2 TB (46 shards) | n/a | Impractical for self-host |

### FP8/FP4 (vLLM on GPU)
- FP8: ~1 TB, requires 13× H100 80GB — datacenter only
- KTransformers: MoE offload to CPU, practical on 256GB RAM + H100

### Other engines
- KTransformers is the primary path for partial self-hosting
- Requires substantial CPU RAM (256GB+) even at IQ2 quants

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (moonshotai/kimi-k2.7-code) | $0.74 | $3.50 | 256K | Premium coding model |

## Quality Benchmarks
- Top-tier on coding benchmarks (SWE-bench, HumanEval)
- Strong on long-horizon agentic coding tasks
- Native multimodal supports UI/UX workflows
- Competes with Claude Sonnet on coding

## Notes
- HuggingFace: https://huggingface.co/moonshotai/Kimi-K2.7-Code
- 857K downloads, 1047 likes
- Released 2026-06-12, very recent
- Specialized for agentic long-horizon coding (build apps from specs)
- License is "other" — verify terms before commercial deployment
- Extreme IQ1/IQ2 quants exist but quality is degraded
- Sources: OpenRouter API, HuggingFace API, unsloth GGUF repo
