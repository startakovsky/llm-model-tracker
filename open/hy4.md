---
model: Hy4
organization: Tencent
license: Apache 2.0
release_date: 2026-11-04
last_updated: 2026-11-04
---

# Hy4

Tencent's official GA release of the Hy4 line (Nov 4, 2026), successor to Hy4-preview. Same 770B/49B MoE backbone; adds vision (text+image input) and computer-use (CLI + GUI, with Blender/CAD-targeted training) for the first time.

## Availability
- OpenRouter id `tencent/hy4` at $0.417/$1.25 per M (half of Tencent Cloud list $0.834/$2.501), 1048576 context, 65536 completion limit, Tencent Cloud provider.
- Weights + system card promised "in coming days"; preview (Apache 2.0) was already open on HF.

## Capabilities
- Gains over preview: instruction following, long-context understanding, long-horizon agentic tasks, deep research.
- WorkBuddy eval: 83.18 avg score, 96.15% pass rate, 9/12 scenarios first in mainland China.
- GameDev +19.1% / GameLogic +9.8% vs preview (Unreal/Unity/Godot workflows).
- Finance: #1 among open-weight models in Tencent's company-run eval (213 finance pros, 579 real-world tasks).

## Classification
`open weights` (Apache 2.0, weights pending). Quality score 83.
