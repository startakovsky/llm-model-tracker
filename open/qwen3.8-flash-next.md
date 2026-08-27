---
model: Qwen3.8 Flash Next
organization: Alibaba
license: qwen3.8-max
release_date: 2026-08-26
last_updated: 2026-08-27
sources:
  - https://huggingface.co/Qwen/Qwen3.8-Flash-Next
  - https://benchlm.ai/models/qwen3-8-flash-next
---

# Qwen3.8 Flash Next

## Overview
- **Org:** Alibaba (Qwen)
- **License:** Qwen Community License 1.0 (open weight, not Apache)
- **Category:** Self-hostable
- **Context length:** 262,144 native (extensible to 1,000,000 via YaRN)
- **Released:** 2026-08-26
- **Not yet on OpenRouter** — self-host or Qwen Cloud only

## Architecture
The **first open-weight model on the Qwen4 architecture.** Not a normal point release — a preview of the design that will underpin Qwen4:
- **125B total params, 6B active per token** (mixture-of-experts) + 51B n-gram embedding table + 4B multi-token prediction (MTP) layer
- 512 experts total, 10 routed + 1 shared per token
- Gated DeltaNet + Qwen Sparse Attention (QSA), 48 layers
- Native text + vision encoder (image-text-to-text); speculative decoding built in (self-drafted MTP)

## Pricing
- **Not on OpenRouter yet.** Managed production API sibling (Qwen3.8 Flash) is $0.16/$0.47 per M on Qwen Cloud.
- Self-host: memory footprint ~180B effective (51B n-gram table + 4B MTP ride along; quantizers keep the table near full precision). FP8 repo ~186GB; smallest community build (~123GB IQ1_S GGUF) needs a 256GB-class machine.

## Benchmarks (vendor-reported)
- BenchLM score **67.5/100** — **#25 of 226** ranked models
- Agentic **#13/138** (~91st percentile), Coding **#32/144**, Inst-Following **#10/42**
- SWE-bench Pro **62.5**, SWE-bench Multilingual 81.0, liveCodeBench v6 91.9, DeepSWE 58.7
- GPQA Diamond **91.7**, HLE 35.9
- Multimodal: CharXiv 90.6, MathVision 90.6 (95.7 w/ Python), RealWorldQA 88.5
- Qwen positions it against DeepSeek-V4-Flash-0731 and Claude Opus 4.6 — a **6B-active model aimed at frontier agentic coding**

## Self-Hosting
- Weights: `Qwen/Qwen3.8-Flash-Next` on HuggingFace, Qwen Community License 1.0
- Community GGUF quickly available (unsloth UD-IQ1_S ~123GB); FP8 ~186GB
- Practical hardware: Mac Studio M5 Ultra 256GB (~32 tok/s est.), 2x RTX PRO 6000 (192GB VRAM). No Ollama tag / no Q4_K_M build at release.

## Quality Assessment
Qwen3.8 Flash Next is a significant architectural signal: Qwen is scaling via n-gram tables and lean active params rather than dense compute, and an open-weights 6B-active model posting frontier-adjacent agentic scores is a meaningful step for the self-hosting tier. As a research preview it needs third-party benchmarks and a usable Q4 build; **quality score 77 reflects strong position for an open lightweight class, not yet top-frontier**. Watch for OpenRouter presence and Ollama/Q4_K_M support in coming days.