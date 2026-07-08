---
model: GLM-4.5-Air
organization: Z.ai
license: MIT
release_date: 2025-08
last_updated: 2026-07-08
---

# GLM-4.5-Air

## Architecture
- **Total params:** ~106B (MoE)
- **Active params per token:** ~7B (8 of 128 experts)
- **Context length:** 131,072
- **Layers:** 46, hidden_size=4096, 128 routed experts, moe_intermediate_size=1408

## Self-Hosting

### GGUF (llama.cpp)
| Quant | Size | Min RAM | Notes |
|---|---|---|---|
| BF16 | ~213GB | 256GB+ | Full precision |
| FP8 | 113GB | 128GB+ | zai-org/GLM-4.5-Air-FP8 |
| UD-Q6_K_XL | 101.6GB | 128GB+ | High quality |
| UD-Q4_K_XL | 67.7GB | 96GB+ | Recommended balance |
| Q2_K | 45.3GB | 64GB+ | Minimum viable |

Source: https://huggingface.co/unsloth/GLM-4.5-Air-GGUF

### FP8 (vLLM on GPU)
- Model: zai-org/GLM-4.5-Air-FP8 (112.6GB)
- Fits on 2x RTX PRO 6000 (192GB VRAM)
- Expected: 40-60 t/s

### MLX (Apple Silicon)
- mlx-community/GLM-4.5-Air-4bit (900 downloads)
- lmstudio-community/GLM-4.5-Air-MLX-4bit

## API Providers
| Provider | Prompt $/M | Completion $/M | Context | Notes |
|---|---|---|---|---|
| OpenRouter (z-ai/glm-4.5-air) | $0.13 | $0.85 | 131,072 | 7x cheaper than GLM-5.2 |

## Quality Benchmarks
- 63.2 average across 12 industry-standard tests (per Z.ai)
- Strong coding and agentic capability
- Full tool-calling support (chat template includes tool parsing)

## Quality Assessment
GLM-4.5-Air scores 63.2 average across 12 benchmarks. It's a capable model for coding, tool-use, and personal-assistant tasks, but noticeably below GLM-5.2 on deep reasoning and long-context work. At $0.13+$0.85/M (7x cheaper than GLM-5.2), it's a strong value pick for self-hosting where frontier quality isn't required. Best used as a daily driver with GLM-5.2 as the escalation target.

## Notes
- 391K downloads on HuggingFace — widely tested
- Designed by Z.ai specifically for local/self-hosted use
- No 1M context (caps at 131K)
- Potential Tier 1 model for cost-conscious self-hosting
