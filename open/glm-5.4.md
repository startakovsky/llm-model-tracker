---
model: GLM-5.4
organization: Z.ai (Zhipu AI)
license: MIT (weights pending release)
release_date: 2026-11-23
last_updated: 2026-11-23
sources:
  - https://www.unite.ai/z-ais-glm-5-4-uses-iterative-depth-without-adding-parameters/
  - https://benchlm.ai/models/glm-5-4
  - https://deepseekv4pro.com/news/glm-5-4-launch-kingbench-4-highest-open-model
---

# GLM-5.4

Released November 23, 2026. Z.ai's **first Loop Transformer flagship**: a 750B-parameter model that reuses 28 layers twice (shared weights) to deepen reasoning without adding parameters, claiming 2T–3T-class intelligence at 750B scale. Native vision input, 1M context. Live quietly in Z.ai Chat / GLM Coding Plan / ZCode with 50% more weekly quota than GLM-5.3; API "coming soon", weights pending safety hardening.

## Architecture: Loop Transformer
- Takes 28 layers from the GLM-5 base and runs them for two iterations with shared weights; per-token gates control candidate-update flow (first pass writes conservatively, second refines; step size varies with token difficulty).
- Hybrid KV cache: second loop reuses sparse KV entries selected during the first; new entries live in a sliding window — deployment cost stays near GLM-5.3 at 1M ctx.
- Reuses first loop's sparse-attention indices (nearly identical results to recomputing).
- Built by adapting a pre-trained base (looped-from-scratch trails unshared layers at equal compute). Validated on 1B/4B/30B probes; ~10% extra compute at 30B gave gains mainly in math, scientific reasoning, long-context.
- Reported: 10–14% shorter outputs (CoT moves "into the loop"), up to 200 tok/s off-peak / 70–80 tok/s peak. Principal limitation: excessively long reasoning loops.

## Signals
- **KingBench 4 (third-party launch-day board, marked internal/NDA):** 33.2/60 — 7th of 19, **highest open model** on the board, ahead of Kimi K3.1 Pro (32.2), DeepSeek V4.1 Flash (31.0), GLM-5.3 (27.5), and +5.7 over its predecessor. Caveats: mixed grading (tasks graded by Gemini 4 Neon / GLM-5.4 itself), same-prompt total 31.8. Unverified.
- **Generalized Coding:** code → video, games, 3D/FreeCAD modeling, mechanical design (editorial distinction, no benchmarks published).
- Early user report: "possibly the most careful model I have used" — found bugs/security issues other models (incl. Fable) missed. Anecdotal.

## Availability
- **Now:** Z.ai Chat, GLM Coding Plan (all tiers), ZCode, Trae, WorkBuddy, Qoder, CatPaw, OpenCode. 50% more quota than GLM-5.3 (Coding Plan V2/V3/Team).
- **OpenRouter:** **not listed** as of Nov 23 (0/0 placeholder).
- **Weights:** not yet public; "open-source after safety hardening" per Z.ai.
- Input modalities: text + image; output: text. 1M context.

## Classification
`open` (pending) — Z.ai committed to open weights after safety hardening; consistent with the MIT GLM-5.x line. Quality score 92: Loop-Transformer gains + strongest-open-model KingBench 4 placement put it just above GLM-5.3 (91), pending official benchmarks.

## Sources
- Unite.AI: https://www.unite.ai/z-ais-glm-5-4-uses-iterative-depth-without-adding-parameters/
- BenchLM: https://benchlm.ai/models/glm-5-4
- DeepSeekV4Pro launch report: https://deepseekv4pro.com/news/glm-5-4-launch-kingbench-4-highest-open-model
