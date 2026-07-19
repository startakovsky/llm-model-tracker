---
model: Qwen3.8 Max Preview
organization: Alibaba
license: Apache 2.0
release_date: 2026-07-19
last_updated: 2026-07-19
---

# Qwen3.8 Max Preview

## Architecture
- **Total params:** 2.4T (MoE)
- **Active params per token:** Not disclosed
- **Context length:** 1,048,576 (1M)
- **Modality:** Multimodal — text, image, video, documents
- **Architecture type:** Sparse Mixture-of-Experts
- **Note:** First Qwen multimodal model with more than 1 trillion parameters

## Availability
- **Status:** Preview (API only). Open weights promised by July 27, 2026.
- **Access:** Alibaba Token Plan subscription, Qoder, QoderWork — at 10% of standard price
- **OpenRouter:** Not yet listed (no model ID as of July 19, 2026)
- **HuggingFace:** Weights coming soon

## Quality (preliminary)
- No public benchmarks yet (as of July 19, 2026)
- Qwen team claims it is "second only to Anthropic's Claude Fable 5"
- Qwen says it outperforms Qwen3.7-Max, especially in:
  - Coding and full-stack development
  - Data analysis
  - Office productivity workflows
- Estimated quality_score: 86 (between Qwen3.7-Max at 84 and Kimi K3 at 93, pending benchmarks)

## Competitive Context
Qwen 3.8 Max is Alibaba's direct response to Moonshot AI's Kimi K3 (2.8T params, released July 16, 2026). Both are trillion-scale open-weight MoE models targeting long-horizon coding and agentic workloads. Qwen's pitch: match K3's scale with multimodal capability (K3 is text+vision; Qwen 3.8 adds video and document understanding).

The open-weight release by July 27 would make Qwen 3.8 the second trillion-class open model after Kimi K3 (whose weights are also promised by July 27 under Modified MIT).

## Quality Assessment
This is a preview with no independent benchmarks. The "second only to Fable 5" claim is vendor-reported. Until weights ship and the community runs it through neutral harnesses (Artificial Analysis Intelligence Index, SWE-bench, Terminal-Bench), treat the quality score as provisional. If benchmarks confirm parity with Kimi K3 (~57 on the AAII), this model is a top-3 open-weight contender. At 10% preview pricing via Token Plan, it is also the cheapest way to evaluate a frontier-class model right now.

## Notes
- Preview launched July 19, 2026 (Bloomberg, SCMP, The Decoder coverage)
- Open weights expected on HuggingFace by July 27, 2026
- Will likely appear on OpenRouter after open-weight release
- Qwen 4 (API) scheduled for September 2026 per Reddit r/Qwen_AI
