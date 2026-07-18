# Inkling — Thinking Machines

| Field | Value |
|---|---|
| **Org** | Thinking Machines (Mira Murati) |
| **OpenRouter ID** | `thinkingmachines/inkling` (live as of ~Jul 18 2026) |
| **HuggingFace** | [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling) |
| **License** | Apache 2.0 |
| **Release date** | 2026-07-15 |
| **Pricing** | OpenRouter $1.00 prompt / $4.05 completion per M tokens (live ~Jul 18 2026); open weights also self-hostable |
| **Context** | 1,048,576 (1M) |
| **Category** | Frontier (open) |

## Architecture

Inkling is the **first open-weight model from Thinking Machines**, the lab founded by former OpenAI CTO Mira Murati. It is a **decoder-only multimodal Mixture-of-Experts** transformer:

- **975B total / 41B active** parameters — 256 routed experts, 6 selected per token, plus 2 always-on shared experts (shared-expert-sink routing).
- **66 layers**, hidden size 6144, vocab 201K.
- **Relative attention** (not RoPE): a fourth projection produces a per-token/per-head relative feature injected into attention logits, letting each layer learn position directly.
- **Hybrid attention**: 5:1 ratio of sliding-window to global layers; final layer is global. Sliding window 512.
- **Short convolution (SConv)**: a 1D conv (kernel 4) over hidden states handles local representation, freeing attention/MoE for longer-range structure.
- **Native multimodal**: images/video via a hierarchical MLP patchifier; audio via discretized mel-spectrogram token encoding (100 ms chunks). All modalities project into the shared hidden space — no separate encoder towers.
- **Speculative MTP layers** for faster inference; numerics in **BF16** and a well-calibrated **NVFP4** variant.
- Trained on **45 trillion tokens** of text, images, audio, and video.

Day-0 inference support: Hugging Face Transformers, SGLang, vLLM, Unsloth, llama.cpp, TokenSpeed.

## Benchmarks (effort=0.99, reported Jul 14 2026)

| Benchmark | Inkling | GLM 5.2 | Kimi K2.6 | DeepSeek V4 Pro | GPT 5.6 Sol (closed) |
|---|---|---|---|---|---|
| AIME 2026 | **97.1%** | 99.2% | 96.4% | 96.7% | 99.9% |
| GPQA Diamond | 87.2% | 89.5% | 91.1% | 88.8% | 94.1% |
| HLE (text only) | 29.7% | 40.1% | 35.9% | 35.9% | 47.2% |
| HLE (with tools) | 46.0% | 54.7% | 54.0% | 48.2% | 55.0% |
| SWE-bench Verified | 77.6% | – | 80.2% | 80.6% | – |

## Quality Assessment

Inkling lands in the **frontier open tier but just below the very top**. Its math reasoning is excellent (97.1% AIME, 87.2% GPQA), within striking distance of GLM-5.2 and DeepSeek V4 Pro. It trails the leaders on hard knowledge/reasoning (HLE) and agentic coding (SWE-bench Verified 77.6% vs ~80% for K2.6/V4 Pro).

The standout differentiator is **native multimodality at ~1T scale**: it is the first large open model to natively accept image, text, *and* audio with a 1M context in a single decoder — no bolted-on encoders. That makes it especially attractive for multimodal reasoning apps, audio-understanding agents, and fine-tuning for domain adaptation, which is its stated intent.

**Cost/quality framing:** As open weights there is no per-token API cost; self-hosting a 975B/41B MoE is heavy (BF16 is ~2 TB; the NVFP4 variant brings this down substantially), so most users will reach it via 3rd-party inference once providers light it up. Relative to GLM-5.2 (the open reference at quality 90), Inkling is **~90–93% as capable on text reasoning/coding** while adding genuine multimodal breadth the text-only leaders lack.

**Community signal:** 690 HuggingFace likes on day one — strong buzz, amplified by being Thinking Machines' first public model.

**Verdict:** A landmark open release for multimodal reasoning, not yet a GLM-5.2 replacement on pure text/agentic coding. Now live on OpenRouter at $1.00/$4.05 per M (added ~Jul 18 2026) — a reasonable mid-tier price for a 975B/41B frontier open model with native multimodality.
