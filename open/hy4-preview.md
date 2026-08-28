---
model: Hy4 preview
organization: tencent
license: Apache 2.0
release_date: 2026-08-28
last_updated: 2026-08-28
openrouter_id: tencent/hy4-preview
category: Frontier
quality_score: 83
generated: manual
---

# Hy4 preview

Tencent's old-flagship open-weights Mixture-of-Experts model, released open-source on **August 28, 2026**. The direct successor to Hy3 (July 6), ~2.6x larger with 4x the context. Heavily agentic/coding oriented.

## Quick Facts
- **OpenRouter ID:** `tencent/hy4-preview`
- **Parameters:** 770B total / **49B active** (sparse MoE)
- **Context length:** 1M tokens (1,048,576); 64K max completion
- **License:** Apache 2.0 (no field-of-use clause, no geo carve-out)
- **Category:** Frontier
- **Quality score:** 83/100
- **Live on OpenRouter since:** Aug 28, 2026

## Architecture
- 78 layers — layer 1 dense FFN, layers 2–78 MoE
- 256 routed + 1 shared expert per MoE layer, top-8 routed activated
- Hidden size 6,144; 64 attention heads
- **Gated DeepSeek Sparse Attention** with IndexCache (cross-layer sparse index reuse) — enables economical 1M context
- Identity Hyper-Connections residual scheme
- Integrated **MTP layer** (10B params / 0.7B active) for in-weight speculative decoding
- Vocabulary 120,832

## Benchmarks
| Benchmark | Score |
|---|---|
| GPQA Diamond | 92.3 |
| HLE (High + Tools) | 55.4 |
| SWE-Bench Multilingual | 82.9 |
| SWE-Bench Pro | 65.7 |
| DeepSWE | 64.3 |
| Terminal-Bench 2.1 | 85.4 |
| MCP-Atlas | 83.7 |
| CyberGym | 78.4 |
| Office QA Pro | 66.2 |

Frontier-adjacent for an Apache 2.0 model; the agentic column (Terminal-Bench 85.4, MCP-Atlas 83.7) is the standout for tool-calling loops. Tencent's blind eval (163 internal experts, 203 tasks) scored it 2.99/4 vs Kimi K3 2.94 and GLM-5.3 2.92 — i.e. it reached the GLM-5.3/Kimi K3 tier, though that 0.05 margin on vendor-selected tasks is effectively noise.

## Pricing vs. peers (per 1M tokens)
| Model | Input | Output |
|---|---|---|
| DeepSeek V4 Pro | ~$0.44 | ~$0.87 |
| **Hy4 preview** | **$0.834** | **$2.501** (cache read $0.042) |
| GLM-5.3 | $1.40 | $4.40 |
| Kimi K3 | $3.00 | $15.00 |

~40% cheaper than GLM-5.3 on output, 6x cheaper on output vs Kimi K3. Aggressive $0.042/M cached input (20x off) matters for agentic loops resending large system prompts / tool history. DeepSeek V4 Pro remains the price floor.

## Self-Hosting
**Not single-node capable.** FP8 weights alone are ~770GB — too large for 8xH100 (640GB); needs H200-class (8xH200 1.1TB) or multi-node. Recommended serving: vLLM / SGLang prebuilt images with tensor parallelism + speculative decoding. Practical path for most teams is the API.

## Caveats
- Tencent's own card: "early version... known issues... spending longer than necessary reasoning through complex tasks, and a tendency to over-verify its own work."
- ~36 tok/s at P50, 3.19s latency (Tencent Cloud sole provider) — over-reasoning tax lands on latency + bill.
- ~86% availability over first three days (capacity, likely temporary).
- Text-only (no multimodal in this checkpoint).

## Assessment
One of the strongest open-weights releases of late 2026 at the mid price point — enterprise-grade agentic coding at ~40–80% below GLM-5.3/Kimi K3, Apache 2.0 so vendor can't revoke self-hosting rights. Not for tight/realtime agent loops until Tencent addresses the over-verification tendency and throughput; frame it as ~GLM-5.3 tier for ~40% less.