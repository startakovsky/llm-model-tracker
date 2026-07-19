---
model: Mercury 2
organization: Inception (Inception Labs)
license: Proprietary
release_date: 2026-03-15
last_updated: 2026-07-19
---

# Mercury 2

## Architecture
- **Type:** Diffusion-based language model (not autoregressive)
- **Context length:** 128,000
- **Decoding:** 1,000+ tokens/second on standard NVIDIA Blackwell GPUs
- **Speed advantage:** ~5x faster than comparable autoregressive models
- **Reasoning:** Tunable reasoning depth — controllable compute per query
- **Native capabilities:** Tool use, schema-constrained output, long context compaction

## Why It Matters
Mercury 2 is the first **reasoning diffusion LLM**. Instead of generating tokens left-to-right (autoregressive), it refines a noisy sequence through iterative denoising — the same principle behind image diffusion models like Stable Diffusion, applied to text. This architectural choice enables:

1. **Speed:** 1,009 tokens/sec on Blackwell GPUs. Fast enough for real-time voice agents ("pick up the phone" latency).
2. **Tunable reasoning:** Adjust reasoning depth per request — spend more compute on hard queries, less on easy ones.
3. **Subagent routing:** Inception positions Mercury 2 for subagent orchestration — context compaction, tool search, and routing at sub-second latency.

## API Pricing
| Provider | Prompt $/M | Completion $/M | Context |
|---|---|---|---|
| OpenRouter (inception/mercury-2) | $0.25 | $0.75 | 128,000 |
| Inception direct | $0.25 | $0.75 | 128,000 |

## Quality Assessment
Mercury 2 is not a frontier-tier model on raw quality — it does not compete with GLM-5.2 or Kimi K3 on benchmark scores. Its value proposition is **latency at acceptable quality**: a reasoning model fast enough for real-time voice, subagent routing, and interactive agents where 200-500ms response time matters more than squeezing the last 2% on GPQA. Think of it as a **specialized inference-breakthrough model** rather than a frontier competitor. At $0.25/$0.75 per million tokens, it is also cheap enough to run as a high-volume routing/compaction layer in front of more expensive frontier models.

## Notes
- Diffusion LLMs are an active research area; Google's DiffusionGemma is a competing open approach
- No downloadable weights (proprietary, API only)
- Quality score (68) reflects "good enough for routing/agents, not frontier reasoning"
- Best use case: real-time agents, voice, subagent orchestration, tool routing
