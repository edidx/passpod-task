#!/usr/bin/env bash
set -euo pipefail
fail() { echo "❌ $1" >&2; exit 1; }

required_files=(README.md SPEC.md PILOT_ACCESS.md ADOPTION.md SECURITY.md CONTRIBUTING.md GOVERNANCE.md VERSIONING.md COMMERCIAL_BOUNDARY.md requirements.txt schemas/trust-action-receipt.schema.json examples/remote-worker.receipt.json examples/README.md openapi/passpod-task.public.yaml openapi/README.md validator/README.md cli/README.md worker-reference/README.md docs/glossary.md docs/public-vs-pilot.md docs/production-checklist.md docs/standardization-roadmap.md tools/validate-receipts.py)

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
  "PILOT_ACCESS.md" \
  "COMMERCIAL_BOUNDARY.md"
do
  grep -q "$link" README.md || fail "README missing launch navigation link: $link"
done

grep -q "Public demo receipts in this repository are not production-valid receipts" README.md \
  || fail "README must state that public demo receipts are not production-valid"
grep -q "Production-valid receipts require authorized issuer access through Passpod Hub and the Pilot Access Engine" README.md \
  || fail "README must state the production-valid receipt access boundary"
grep -q "Passpod TASK Core -> Passpod Hub -> Control Packs -> Pilot Access -> paid pilot / Team / Enterprise" README.md \
  || fail "README missing canonical product stack"

for term in \
  "Passpod TASK Core" \
  "Passpod Hub" \
  "Control Packs" \
  "AgentTrust" \
  "Remote Worker Trust" \
  "Pilot Access Engine" \
  "Trust Action Receipt" \
  "Sensitive Action Control" \
  "DIDX"
do
  grep -R "$term" README.md SPEC.md docs/glossary.md PILOT_ACCESS.md ADOPTION.md LAUNCH_READINESS.md COMMERCIAL_BOUNDARY.md >/dev/null \
    || fail "Canonical term missing from public docs: $term"
done

grep -R "Passpod Hub is the paid hosted product layer" README.md COMMERCIAL_BOUNDARY.md >/dev/null \
  || fail "Public docs must distinguish TASK Core from Passpod Hub"
grep -R "production issuer logic" README.md SPEC.md ADOPTION.md LAUNCH_READINESS.md COMMERCIAL_BOUNDARY.md cli/README.md worker-reference/README.md openapi/README.md >/dev/null \
  || fail "Public docs must exclude production issuer logic"
grep -R "Sentinel/Ops internals" ADOPTION.md LAUNCH_READINESS.md COMMERCIAL_BOUNDARY.md >/dev/null \
  || fail "Public docs must exclude Sentinel/Ops internals"

for readme in examples/README.md openapi/README.md validator/README.md cli/README.md worker-reference/README.md; do
  if grep -Eiq 'placeholder|skeleton placeholder|TODO|TBD|coming soon|lorem|fixme' "$readme"; then
    fail "Public directory README still contains placeholder-only language: $readme"
  fi
done

dangerous_patterns='SECRET=|PRIVATE_KEY=|BEGIN PRIVATE KEY|real customer receipt:|production signing key:|scoped key value|sk_live_|pk_live_|AKIA[0-9A-Z]{16}|production-valid receipt issuance|production-valid issuance|full monetization workflow|exit roadmap:'
if grep -R -E "$dangerous_patterns" . \
  --exclude-dir=.git \
  --exclude="check-public-task-repo.sh" \
  --exclude="seed_passpod_task.py" >/dev/null; then
  fail "Dangerous secret/private leakage pattern found"
fi

python3 tools/validate-receipts.py
echo "✅ Public TASK repo gate passed"
