---
model: Ternary Bonsai 2.5 (27B)
organization: prism-ml
license: Apache-2.0
release_date: 2026-11-24
last_updated: 2026-11-25
sources:
  - https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF
  - https://github.com/PrismML-Eng/Bonsai-demo
---

# Ternary Bonsai 2.5 (27B)

Agentic ternary release of the Bonsai line, built on the Qwen3.8-27B hybrid-attention base. **1.76 bits/weight, 5.93 GB GGUF vs 53.8 GB FP16 (~9x smaller).** Not on OpenRouter (self-host; llama.cpp on CUDA/Metal/CPU).

| Field | Value |
|---|---|
| **Org** | prism-ml |
| **HuggingFace** | [prism-ml/Ternary-Bonsai-2.5-27B-GGUF](https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF) (59K DL, 254 likes; PTQ1_0/PQ2_0/Q2_0 + MTP drafts + mmproj vision) |
| **License** | Apache-2.0 (GGUF) |
| **Release date** | 2026-11-24 |
| **Pricing** | n/a (self-host) |
| **Context** | 262,144 (Qwen3.8-27B base) |
| **Category** | Self-hostable (open) |

## Benchmark claims (README)

- FP16-level agentic tool calling: 77.2 avg vs 77.7 FP16 (tau2/tau3, BFCL v3/v4, AppWorld).
- 90% of FP16 agentic coding (up from 63% in Bonsai 2): DeepSWE 0->27.0, SWE-bench Verified 60.8->75.6, Terminal-Bench 2.1 52.8->60.1.
- Strongest agentic model under 10 GB; general capability 82.1 vs 84.3 FP16.
- MTP variants: 1.5-1.8x faster decode on NVIDIA.

## Quality Assessment

The compression breakthrough trend continues: a 27B agentic coder that fits in ~6 GB runs the tool-calling loop nearly at FP16 parity. For local agent work on consumer hardware this beats any larger 2-bit MoE on portability. Follow-on to tracked Ternary Bonsai 2 (27B/9B). Score 74.

## Sources
- https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF
