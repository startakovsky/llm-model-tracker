---
model: Qwen3.8 Flash Next
organization: Alibaba (Qwen)
license: qwen3.8-max
release_date: 2026-08-24
last_updated: 2026-10-23
---

# Qwen3.8 Flash Next

## Architecture
- **Total params:** 125B (MoE)
- **Active params per token:** 6B
- **Context length:** 262,144 (extensible to 1,000,000)
- **Architecture type:** Sparse Mixture-of-Experts (Qwen4 experimental / `qwen4_exp`)
- **Modality:** Image + Text → Text

## Pricing (OpenRouter)
Not listed on OpenRouter (no paid endpoint). Closed sibling **Qwen3.8 Flash** is the managed API at $0.15/$0.47.

## Self-Hosting
- Weights available on HuggingFace: `Qwen/Qwen3.8-Flash-Next` (qwen3.8-max license)
- **2,787,377 downloads, 6,431 likes** — among the largest open-model followings this year
- Experimental research preview of the Qwen4 architecture; MTP layer (1, trained multi-step)

## Quality Assessment
Qwen3.8 Flash Next is the open-weights research preview of Qwen's next-generation Qwen4 architecture — 125B total with only 6B active, making it unusually cheap to serve for a frontier-adjacent release. The Qwen team frames it as the experimental sibling of the closed Qwen3.8 Flash managed tier (which adds 1M ctx by default and built-in tools). Its massive HuggingFace traction (2.8M downloads / 6.4K likes, one of the highest of any 2026 open release) signals strong community adoption for self-hosting. Skipped earlier because it is a research preview with self-reported benchmarks; added Oct 23 given the sustained top-tier download counts.

## Notes
- Open-weights preview of Qwen4 architecture (`qwen4_exp`)
- 125B/6B active MoE — small active footprint for the size class
- 262K ctx native, 1M extensible
- 2.8M HF downloads / 6.4K likes (as of Oct 23)
- Not on OpenRouter; managed sibling is closed Qwen3.8 Flash ($0.15/$0.47)