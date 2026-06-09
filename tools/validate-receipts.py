#!/usr/bin/env python3
import json
from pathlib import Path

required = ["receipt_type", "scenario_id", "actor", "subject", "action", "decision", "evidence", "issued_at"]
valid_decisions = {"allow", "deny", "review_required", "freeze", "revoke"}
ok = True

for path in sorted(Path("examples").glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = [k for k in required if k not in data]
    if missing:
        print(f"❌ {path}: missing {', '.join(missing)}")
        ok = False
    elif data["receipt_type"] != "trust_action_receipt":
        print(f"❌ {path}: invalid receipt_type")
        ok = False
    elif data["decision"] not in valid_decisions:
        print(f"❌ {path}: invalid decision")
        ok = False
    else:
        print(f"✅ {path}: valid public draft receipt")
raise SystemExit(0 if ok else 1)
