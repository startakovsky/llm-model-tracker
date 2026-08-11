# Muse Glimmer 30B — Meta

| Field | Value |
|---|---|
| **Org** | Meta (Meta Superintelligence Labs) |
| **OpenRouter ID** | `meta/muse-glimmer-30b` — live on OpenRouter at $0.35/$1.50 (as of Aug 11 2026); also self-hostable |
| **License** | Apache 2.0 |
| **Release date** | 2026-08-10 |
| **Pricing** | $0.35 / $1.50 per M tokens on OpenRouter (live Aug 11); free + open weights on HuggingFace (local deployment) |
| **Context** | 131,072 (128K+) |
| **Category** | Self-hostable (open) |
| **Quality score** | 68 |

## Architecture

Muse Glimmer is Meta's **open-weight**, multimodal agentic model, distilled from the closed flagship **Muse Spark** down to:

- **30B total dense params** — 28B text decoder + **2B ViT-style "Perception Encoder"** for vision
- **Multimodal:** text + image in → text out
- Optional **speculative-decoding drafter** (DFlash) for faster generation, especially on structured/coding output
- Ships **day-0 support** in `transformers`, `llama.cpp`, `vLLM`, `SGLang`, Ollama, LM Studio, and HF Inference Endpoints
- Runs on a **single consumer GPU** (~58 GB in BF16; Unsloth GGUF < 20 GB at 4-bit)

## Benchmarks (vs comparable local models)

Muse Glimmer-30B High Reasoning vs Gemma 4 31B Thinking and Qwen3.6-27B Thinking (bold = best):

| Benchmark | Muse Glimmer 30B | Gemma4-31B | Qwen3.6-27B |
|---|---|---|---|
| MCP Atlas (agentic) | **75.5** | 54.2 | 62.5 |
| DeepSearch QA | **74.6** | 61.7 | 71.1 |
| WildClawBench | **47.6** | 37.6 | 43.2 |
| GAIA2 | **43.3** | 36.4 | 40.0 |
| SWE-Bench Pro | **51.2** | 36.9 | 50.2 |
| SWE-Bench Verified | 76.0 | 66.6 | **77.2** |
| TerminalBench 2.1 | 51.7 | 43.4 | **60.7** |
| AIME 2026 | **94.7** | 89.2 | 94.1 |
| GPQA Diamond | 83.5 | **85.7** | 84.2 |
| Charxiv Reasoning | **78.8** | 77.7 | 78.4 |
| Beam 128K | **65.1** | 58.2 | 63.0 |

Muse Glimmer leads the comparable-size local pack on most general-agentic and agentic-coding benchmarks, while staying roughly on par with Qwen3.6-27B on pure coding speed (TerminalBench/SWE-bench Verified).

## Quality Assessment

Glimmer is the strongest **open-weight model in the ~30B local class** as of mid-August 2026. Meta's return to open weights (Apache 2.0) after the closed Muse Spark pivot is a notable strategic reversal, and the model is purpose-built for local agentic workloads (coding, document analysis, personal assistants, Claw/Hermes-style setups). It beats Gemma 4 31B and matches Qwen3.6-27B on most agentic suites, at the cost of nothing — it is fully self-hostable.

**Cost/quality framing:** At $0 (local weights), Glimmer delivers roughly Qwen3.6-27B-level agentic capability (~$0.60/$3.60 on OpenRouter) with no per-token cost — only the hardware. On a single consumer GPU it replaces a recurring API bill for privacy-sensitive agent tasks.

**Community signal:** Massive launch buzz — Reuters, NYT, CNBC coverage (Aug 10), trending on r/LocalLLaMA, day-0 Unsloth GGUF, Ollama library. The first "open-source version" of Meta's most powerful model as a 30B distilled form factor.

**Verdict:** Compelling open local-agent model. Now also available via OpenRouter at $0.35/$1.50, so it can be used as a low-cost API model in addition to fully self-hosted deployment. Ideal for local personal assistants and coding agents on consumer hardware.
