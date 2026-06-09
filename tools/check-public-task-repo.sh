#!/usr/bin/env bash
set -euo pipefail
fail() { echo "❌ $1" >&2; exit 1; }

required_files=(README.md SPEC.md PILOT_ACCESS.md ADOPTION.md SECURITY.md CONTRIBUTING.md GOVERNANCE.md VERSIONING.md schemas/trust-action-receipt.schema.json examples/remote-worker.receipt.json docs/public-vs-pilot.md docs/production-checklist.md docs/standardization-roadmap.md tools/validate-receipts.py)

for f in "${required_files[@]}"; do
  [ -f "$f" ] || fail "Missing required file: $f"
done

grep -R "No receipt, no sensitive action" README.md SPEC.md >/dev/null || fail "Canonical doctrine missing"
grep -R "Sensitive Action Control" README.md SPEC.md ADOPTION.md >/dev/null || fail "Sensitive Action Control category missing"
grep -R "public draft standard proposal" README.md SPEC.md ADOPTION.md >/dev/null || fail "Public draft standard proposal wording missing"
grep -R "pilots@passpod.io" README.md PILOT_ACCESS.md SECURITY.md >/dev/null || fail "Pilot Access email missing"

dangerous_patterns='SECRET=|PRIVATE_KEY=|BEGIN PRIVATE KEY|real customer receipt:|production signing key:|scoped key value|sk_live_|pk_live_|AKIA[0-9A-Z]{16}'
if grep -R -E "$dangerous_patterns" . \
  --exclude-dir=.git \
  --exclude="check-public-task-repo.sh" \
  --exclude="seed_passpod_task.py" >/dev/null; then
  fail "Dangerous secret/private leakage pattern found"
fi

python3 tools/validate-receipts.py
echo "✅ Public TASK repo gate passed"
