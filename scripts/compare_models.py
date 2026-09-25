#!/usr/bin/env python3
"""Compare OpenRouter API against models.csv. Report new models and price changes."""
import json, urllib.request, csv, sys, os

def fetch_or_models():
    req = urllib.request.Request("https://openrouter.ai/api/v1/models",
                                 headers={"User-Agent": "llm-model-tracker/0.2"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    out = {}
    for m in data.get("data", []):
        pricing = m.get("pricing", {})
        # OpenRouter now reports per-token prices; CSV stores $/M tokens -> x1e6
        prompt = float(pricing.get("prompt", "0") or 0) * 1_000_000
        completion = float(pricing.get("completion", "0") or 0) * 1_000_000
        ctx = m.get("context_length", 0) or 0
        out[m["id"]] = {"name": m.get("name", ""), "prompt": prompt,
                        "completion": completion, "ctx": ctx,
                        "created": m.get("created", "")}
    return out

def load_csv(path):
    rows = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            rows[r["id"]] = r
    return rows

def main():
    api = fetch_or_models()
    rows = load_csv(os.path.expanduser("~/.hermes/personal/llm-models/models.csv"))
    csv_ids = set(rows.keys())

    new_ids = [i for i in api if i not in csv_ids]
    print(f"=== API total: {len(api)} models; CSV: {len(csv_ids)} models ===")
    print(f"=== NEW models on OpenRouter not in CSV ({len(new_ids)}) ===")
    for i in sorted(new_ids):
        m = api[i]
        print(f"  {i} | {m['name']} | ${m['prompt']:.4f}/${m['completion']:.4f} | ctx={m['ctx']}")

    print(f"\n=== NEW models (with created date) not in CSV ===")
    for i in sorted(new_ids):
        m = api[i]
        print(f"  {i} | {m['name']} | ${m['prompt']:.4f}/${m['completion']:.4f} | ctx={m['ctx']} | created={m['created']}")

    print(f"\n=== Price/ctx CHANGES for tracked models (>=1% move) ===")
    changes = []
    for i, r in sorted(rows.items()):
        if i not in api:
            changes.append(("GONE", i, None, r))
            continue
        a = api[i]
        op, oc, ocx = float(r["prompt_per_m"]), float(r["completion_per_m"]), int(r["context_length"])
        np_, nc, ncx = a["prompt"], a["completion"], a["ctx"]
        pd = (np_ - op) / max(op, 1e-9)
        cd = (nc - oc) / max(oc, 1e-9)
        if abs(pd) > 0.01 or abs(cd) > 0.01:
            changes.append(("PRICE", i, a, r))
        elif ocx != ncx:
            changes.append(("CTX", i, a, r))
    for kind, i, a, r in changes:
        if kind == "GONE":
            print(f"  GONE  {i} (was ${r['prompt_per_m']}/${r['completion_per_m']})")
        else:
            print(f"  {kind}  {i}: ${r['prompt_per_m']}/${r['completion_per_m']}@{r['context_length']} -> ${a['prompt']:.4f}/${a['completion']:.4f}@{a['ctx']}")
    print(f"\nTotal changes: {len(changes)}")

if __name__ == "__main__":
    main()
