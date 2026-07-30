# Ornith-1.0-397B

- **Org:** Unsloth
- **OpenRouter ID:** `unsloth/ornith-1.0-397b` (not on OpenRouter)
- **HuggingFace:** [unsloth/Ornith-1.0-397B](https://huggingface.co/unsloth/Ornith-1.0-397B) · [GGUF quants](https://huggingface.co/unsloth/Ornith-1.0-397B-GGUF)
- **License:** MIT (globally accessible, no regional limits)
- **Released:** 2026-07-30
- **Architecture:** 397B total / ~17B active MoE, post-trained on top of Gemma 4 and Qwen 3.5
- **Context:** 262,144
- **Category:** Self-hostable (open weights)
- **Quality score:** 80

## Overview

Ornith-1.0 is a family of self-improving open-source models for **agentic coding**, released by Unsloth on 2026-07-30. The family ships in four sizes — 9B-Dense, 31B-Dense, 35B-MoE, and 397B-MoE — with this card documenting the 397B-MoE flagship. It is the largest release in the Ornith line and targets single-GPU-friendly deployment via Unsloth's Dynamic 2.0 quants.

## Self-Improving Training Framework

The defining novelty is the training method: instead of only RL over solution rollouts, Ornith-1.0 jointly optimizes **both the scaffold (the code/test harness that drives rollouts) and the resulting solution**. By learning to generate better scaffolds, the model discovers better search trajectories and produces higher-quality solutions. This is a "self-improving" loop where the agent gets better at setting up its own problem-solving environment.

## Benchmarks (agentic coding)

Reported vs. comparable open/frontier models:

| Benchmark | Ornith-1.0-397B | Qwen3.5-397B | Qwen3.7-Max | GLM-5.2 | Claude Opus 4.8 |
|---|---|---|---|---|---|
| Terminal-Bench 2.1 (Terminus-2) | **77.5** | 53.5 | 73.5 | 81.0 | 70.3 |
| Terminal-Bench 2.1 (Claude Code) | **78.2** | 48.6 | 69.8 | 82.7 | 78.9 |

Ornith-1.0-397B achieves **state-of-the-art among open-source models of comparable size** on Terminal-Bench 2.1, SWE-Bench, NL2Repo, and OpenClaw. Its Terminal-Bench scores (77.5–78.2) land just below GLM-5.2 (81–82.7) and roughly match Claude Opus 4.8 on the Claude-Code variant — a strong result for a fully open, MIT-licensed model.

## Cost / Quality Tradeoff

Not currently offered via OpenRouter, so there is no per-token API price; run it yourself. The 397B-MoE with ~17B active parameters is inference-light relative to its total size, and Unsloth's Dynamic 2.0 GGUF quants (BF16 down to Q4_K_M and lower) make local/vLLM serving practical on a single high-VRAM GPU. As an open coding agent it is **free** — the cost is hardware, not tokens.

For comparison: at GLM-5.2's current API price ($0.97/$3.04 per M) a heavy coding session can rack up dollars quickly; Ornith self-hosted is a fixed-cost alternative with ~95% of GLM-5.2's Terminal-Bench performance and a permissive MIT license.

## How to Run

- **vLLM:** `vllm serve "unsloth/Ornith-1.0-397B"`
- **llama.cpp:** `llama serve -hf unsloth/Ornith-1.0-397B-GGUF:UD-Q4_K_M`
- **Unsloth Studio:** `unsloth studio -H 0.0.0.0 -p 8888` then search for the repo
- **HF Space:** https://huggingface.co/spaces/unsloth/studio (no setup)

## Verdict

A genuinely new entry in the open agentic-coding space: MIT-licensed, frontier-adjacent Terminal-Bench scores, and a novel self-improving scaffold+solution RL recipe. Best suited to developers who want a self-hostable coding agent with no regional license strings attached. Worth tracking as the smaller 9B/31B/35B variants roll out and community quantization matures.
