# Tencent Hy-MT2-7B

An open-weight 7B dense translation model from Tencent, published on HuggingFace
under Apache 2.0 (`tencent/Hy-MT2-7B`) and live on OpenRouter as
`tencent/hy-mt2-7b`.

- **Org:** Tencent
- **License:** Apache 2.0
- **Architecture:** 7B dense (translation)
- **Context:** 8,192 tokens
- **OpenRouter pricing:** $0.074 prompt / $0.295 completion per million tokens
- **Released:** 2026-08-19
- **Classification:** open (weights on HuggingFace), Specialized
- **HuggingFace traction:** ~13.9K downloads, 206 likes

## Notes

The middle sibling of Tencent's Hy-MT2 translation family (1.8B / 7B / 30B-A3B).
All three are Apache 2.0 open weights on HuggingFace. The 7B sits between the too-small
1.8B and the 30B-A3B flagship; at the same OpenRouter price as the 30B ($0.074/$0.295
per M), there is no cost reason to prefer the 7B, so the 30B remains the tracker's pick
for the family. Its 8K context caps long-horizon use.

First tracked 2026-08-23.