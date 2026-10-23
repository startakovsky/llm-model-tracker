---
model: Mellum 2.1
organization: JetBrains
license: Apache 2.0
release_date: 2026-10-08
last_updated: 2026-10-23
---

# Mellum 2.1

## Architecture
- **Total params:** 12B (MoE)
- **Active params per token:** 2.5B
- **Context length:** 131,072 (128K)
- **Architecture type:** Sparse Mixture-of-Experts (64 experts, 8 active; GQA 32/4 heads; sliding-window attention in 3 of every 4 layers)
- **Modality:** Text → Text

## Pricing (OpenRouter)
Not listed on OpenRouter. Self-host only (Apache 2.0 weights); GGUF builds for llama.cpp/Ollama/LM Studio announced as "coming soon" at launch.

## Self-Hosting
- Weights available on HuggingFace: `JetBrains/Mellum2.1-12B-A2.5B-Thinking` (Apache 2.0; Base/Instruct/Thinking checkpoints)
- Official Thinking repo 5.3K downloads / 175 likes; bartowski GGUF 8.4K + community quants; JetBrains' own GGUF build 188K downloads
- 2.5B active params → runs on a single workstation GPU

## Quality Assessment
Mellum 2.1 is JetBrains' agentic update to Mellum 2 (same 12B-A2.5B MoE architecture, retrained with RL in real sandboxed environments as the primary training stage instead of a final step). Strong on self-contained coding tasks — 47.0% SWE-bench Verified, 82.0% LiveCodeBench v6, 91.5% HumanEval+ — but drops hard on long-horizon agentic work (Terminal-Bench 2.1 17.4%, SWE-bench Pro 28.0%). Positioned as a fast, local sub-agent/routing model rather than a frontier replacement; JetBrains claims ~2x the throughput of Qwen3.5-9B under heavy load. Good fit for self-hosted coding agents and IDE-adjacent workflows where data residency matters.

## Notes
- Apache 2.0, open weights (Base/Instruct/Thinking)
- RL-first training across millions of sandboxed tasks
- 47% SWE-bench Verified — strong for a 12B-class model
- Weak on long-horizon agentic benchmarks (Terminal-Bench 2.1 17.4%)
- Not on OpenRouter; GGUF builds announced post-launch
- Added Oct 23 (released Oct 8, caught in daily scan; JetBrains/Mellum2.1-12B-A2.5B-Thinking on HF)