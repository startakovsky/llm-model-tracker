---
model: Agents-A1
organization: InternScience (Shanghai AI Lab)
license: Apache 2.0
release_date: 2026-06-22
last_updated: 2026-07-12
---

# Agents-A1

## Architecture
- **Total params:** ~35B (MoE)
- **Architecture type:** Qwen3.5 MoE (`Qwen3_5MoeForConditionalGeneration`)
- **Model type:** `qwen3_5_moe` — multimodal VLM (vision + text)
- **Context length:** 262,144 (262K)
- **Experts:** 256 experts, top-8 routing per token
- **Hidden size:** 2,048
- **Layers:** 40 (hybrid linear/full attention — full attention every 4 layers)
- **Vision config:** 27-depth encoder, 16 heads, patch_size=16, 1152 hidden
- **Vocab size:** 248,320
- **MTP:** 1 dedicated MTP hidden layer

## Self-Hosting
- Weights available on HuggingFace: `InternScience/Agents-A1` (Apache 2.0)
- 29,038 downloads, 502 likes (high community engagement)
- Quantized variants:
  - `InternScience/Agents-A1-Q4_K_M-GGUF` (42,985 downloads — most popular)
  - `InternScience/Agents-A1-Q8_0-GGUF` (10,994 downloads)
  - `InternScience/Agents-A1-FP8` (15,007 downloads)
  - `huihui-ai/Huihui-Agents-A1-abliterated` (uncensored variant)
- Transformers library: `transformers >= 4.57.0` required
- Uses `qwen3_5_moe` architecture — compatible with Qwen3.5 MoE inference frameworks

## API Providers
Not available on OpenRouter. No public API pricing as of July 12, 2026.

## Quality Assessment
Agents-A1 is a 35B agentic VLM from Shanghai AI Lab's InternScience program, built on the Qwen3.5 MoE architecture. It is specifically designed for long-horizon agentic tasks — "scaling the horizon, not the parameters." Community reports on r/LocalLLaMA praise its research and data compilation abilities, noting it "thinks a lot" and burns tokens for deeper reasoning. The model accepts both text and image inputs, making it suitable for multimodal agentic workflows. The Q4_K_M GGUF has 42K+ downloads, indicating strong community adoption for local deployment. It is ~90% as capable as frontier models for research/agentic tasks at zero API cost (self-hosted), making it an excellent choice for budget-conscious agent deployments.

## Notes
- Hybrid attention: linear attention for most layers, full attention every 4th layer (efficiency optimization)
- Uses M-RoPE (multimodal rotary position embedding) with interleaved sections [11,11,10]
- ArXiv paper: arxiv:2606.30616
- Not a general-purpose LLM — optimized for agentic workflows with tool use, long task runs
- GGUF quantization widely adopted (Q4_K_M is the community standard)
