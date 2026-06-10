#!/usr/bin/env bash
set -euo pipefail
fail() { echo "❌ $1" >&2; exit 1; }

required_files=(README.md SPEC.md PILOT_ACCESS.md ADOPTION.md SECURITY.md CONTRIBUTING.md GOVERNANCE.md VERSIONING.md requirements.txt schemas/trust-action-receipt.schema.json examples/remote-worker.receipt.json examples/README.md openapi/passpod-task.public.yaml openapi/README.md validator/README.md cli/README.md worker-reference/README.md docs/public-vs-pilot.md docs/production-checklist.md docs/standardization-roadmap.md tools/validate-receipts.py)

for f in "${required_files[@]}"; do
  [ -f "$f" ] || fail "Missing required file: $f"
done

find openapi -type f | grep -q . || fail "openapi/ must contain a public reference draft"

grep -R "No receipt, no sensitive action" README.md SPEC.md >/dev/null || fail "Canonical doctrine missing"
grep -R "Sensitive Action Control" README.md SPEC.md ADOPTION.md >/dev/null || fail "Sensitive Action Control category missing"
grep -R "public draft standard proposal" README.md SPEC.md ADOPTION.md >/dev/null || fail "Public draft standard proposal wording missing"
grep -R "pilots@passpod.io" README.md PILOT_ACCESS.md SECURITY.md >/dev/null || fail "Pilot Access email missing"

for link in \
  "SPEC.md" \
  "schemas/trust-action-receipt.schema.json" \
  "openapi/passpod-task.public.yaml" \
  "examples/README.md" \
  "validator/README.md" \
  "PILOT_ACCESS.md"
do
  grep -q "$link" README.md || fail "README missing launch navigation link: $link"
done

grep -q "Public demo receipts in this repository are not production-valid receipts" README.md \
  || fail "README must state that public demo receipts are not production-valid"
grep -q "Production-valid receipts require authorized issuer access through Passpod Hub and the Pilot Access Engine" README.md \
  || fail "README must state the production-valid receipt access boundary"

for readme in examples/README.md openapi/README.md validator/README.md cli/README.md worker-reference/README.md; do
  if grep -Eiq 'placeholder|skeleton placeholder|TODO|TBD|coming soon|lorem|fixme' "$readme"; then
    fail "Public directory README still contains placeholder-only language: $readme"
  fi
done

dangerous_patterns='SECRET=|PRIVATE_KEY=|BEGIN PRIVATE KEY|real customer receipt:|production signing key:|scoped key value|sk_live_|pk_live_|AKIA[0-9A-Z]{16}'
if grep -R -E "$dangerous_patterns" . \
  --exclude-dir=.git \
  --exclude="check-public-task-repo.sh" \
  --exclude="seed_passpod_task.py" >/dev/null; then
  fail "Dangerous secret/private leakage pattern found"
fi

python3 tools/validate-receipts.py
echo "✅ Public TASK repo gate passed"
