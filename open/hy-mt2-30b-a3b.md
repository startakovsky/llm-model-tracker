# Tencent Hy-MT2-30B-A3B

A new open-weight 30B/3B MoE from Tencent, published on HuggingFace under Apache 2.0
(`tencent/Hy-MT2-30B-A3B`) and live on OpenRouter as `tencent/hy-mt2-30b-a3b`.

- **Org:** Tencent
- **License:** Apache 2.0
- **Architecture:** 30B / 3B-A3B Mixture-of-Experts (hybrid multimodal)
- **Context:** 8,192 tokens
- **OpenRouter pricing:** $0.074 prompt / $0.295 completion per million tokens
- **Released:** 2026-08-20
- **Classification:** open (weights on HuggingFace), Lightweight
- **HuggingFace traction:** ~12.4K downloads, 486 likes (day of release)

## Notes

Tencent continues its open-weight push with the Hy-MT2 family. The 30B-A3B variant
is the flagship of the pair (the 1.8B sibling is too small to track in a frontier
tracker). Apache 2.0 licensing and cheap OpenRouter pricing ($0.074/$0.295 per M)
make it a reasonable lightweight / self-hostable option for a 30B-class MoE, though
its modest 8K context limits long-horizon use.

First tracked 2026-08-20.