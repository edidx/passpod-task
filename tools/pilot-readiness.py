#!/usr/bin/env python3
import json, sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python3 tools/pilot-readiness.py examples/remote-worker.receipt.json")
    raise SystemExit(2)

data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
score = 40
score += 10 if all(k in data for k in ["receipt_type", "actor", "subject", "action", "decision", "evidence", "issued_at"]) else 0
score += 10 if isinstance(data.get("evidence"), list) and data.get("evidence") else 0
score += 10 if data.get("policy_ref") else 0
score += 10 if data.get("proof_ref") else 0
score += 10 if data.get("signature") and not str(data.get("signature")).startswith("demo-") else 0
score += 10 if data.get("receipt_id") else 0

print(f"Production Readiness Score: {min(score, 100)}/100")
print("Status: valid public demo receipt, not production-ready.")
print("⚠ demo signature only; production signing requires Pilot Access" if str(data.get("signature", "")).startswith("demo-") else "✅ production-like signature present")
print("⚠ missing policy_ref for real workflow mapping" if not data.get("policy_ref") else "✅ policy_ref present")
print("⚠ missing proof_ref for external verification" if not data.get("proof_ref") else "✅ proof_ref present")
print("Next step for real workflows: request Pilot Access at pilots@passpod.io")
