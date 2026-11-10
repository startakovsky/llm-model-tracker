---
model: Claude Fable 5.2
organization: Anthropic
license: Proprietary
release_date: 2026-11-09
last_updated: 2026-11-10
sources:
  - https://www.anthropic.com/claude-fable-and-mythos-5-2
  - https://openrouter.ai/anthropic/claude-fable-5.2
  - https://platform.claude.com/docs/en/models/fable-5-2/overview
---

# Claude Fable 5.2

Anthropic's new frontier flagship (Nov 9, 2026), a step above Opus 5.5 across nearly every evaluated capability. **Claude Mythos 5.2 is the same underlying model** served with reduced safeguards via Anthropic's Cyber and Life Sciences Verification Programs; Fable 5.2 carries strong cyber/bio safeguards and is available to all users.

## Key Facts

- **Pricing:** $8/$40 per M (first flagship price cut — Fable 5.1 is $10/$50). Optional fast mode: $16/$80 (up to 2.5x faster).
- **Speed:** ~30% faster outputs than Fable 5.1 at the same setting.
- **Context:** 1M ctx, 128K max output. Closed API (no weights).
- **Live on OpenRouter Nov 9** at `anthropic/claude-fable-5.2` ($8/$40).

## Benchmarks (highest available effort, from Anthropic)

| Benchmark | Fable 5.2 | Fable 5.1 | Opus 5.5 | GPT-6 Astra |
|---|---|---|---|---|
| FrontierCode 2.0 (agentic coding) | **49.1%** (Xhigh) | 32.4% | 45.5% | 42.8% |
| FrontierSWE v2 | **69.9%** | 56.3% | 62.3% | 65.5% |
| AutomationBench | **51.4%** | 31.4% | 42.5% | 41.4% |
| Terminal-Bench-Science 0.1 | **74.6%** | 52.6% | 58.7% | 68.1% |
| WANDR (agentic search) | **82.1%** | 68.7% | 72.3% | — |
| OSWorld 2.1 (partial) | **89.3%** | 83.5% | 87.2% | 79.5% |
| Chartography (no tools) | **73.4%** | 44.8% | 64.4% | 71.0% |
| HLE (with tools) | **74.2%** | 65.6% | 67.7% | 57.2% |
| AA-Briefcase v1.1 (Elo) | 1785 | 1669 | 1800 | 1569 |
| CyScenarioBench (Mythos) | 76.3% | 61.7% | 67.6%† | 61% (GPT-6 Cyber) |

†Opus 5.5 tested without safeguards. Fable 5.2 at High effort ≈ Opus 5.5 at Max effort on FrontierCode 2.0 for ~half the cost per task.

## Notable Early-Testing Feats

- Coordinated 1,000+ subagents over 8 days to build a **bootable OS** from an empty folder (own core, drivers, filesystem, installer, built-in Claude).
- **Formalized a proof of Fermat's Last Theorem in 30 hours** and solved **two open problems in black-hole physics**.
- Designed three working electronic devices from scratch (69% on real-world electronics design vs 25% for Fable 5).

## Quality Assessment

The current frontier leader (benchlm.ai top-10 rank 1 at 91.2, ahead of all comers). The price cut to $8/$40 concurrently with a capability jump makes it a rare win-win vs Fable 5.1 — strictly more capable and 20% cheaper. Worth noting Anthropic's guidance: for most coding/knowledge work, Opus 5.5 remains the recommended daily driver; Fable is for the most ambitious open-ended technical work.

## Notes

- Mythos 5.2 (verified orgs only) adds cybersecurity strength: 89.6% CVE Rediscovery vs 81.3% for Opus 5.5 (without safeguards), and one-in-six confirmed bugs its security-company tester found were missed by every other frontier model tested.
- Also available on AWS Bedrock, Google Cloud, Azure, and Claude Code.
- Classified `closed` (Frontier). Quality score 99.
