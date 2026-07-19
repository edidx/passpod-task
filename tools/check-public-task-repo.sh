#!/usr/bin/env bash
set -euo pipefail

fail() {
  echo "ERROR: $1" >&2
  exit 1
}

require_file() {
  local path="$1"
  [ -f "$path" ] || fail "Missing required file: $path; expected canonical Passpod v0.1 repository asset"
}

require_dir() {
  local path="$1"
  [ -d "$path" ] || fail "Missing required directory: $path; expected canonical Passpod v0.1 repository asset"
}

require_contains() {
  local path="$1"
  local needle="$2"
  local expectation="$3"

  grep -Fq "$needle" "$path" || fail "$path failed check; expected $expectation"
}

require_json() {
  local path="$1"
  PYTHONDONTWRITEBYTECODE=1 python3 -m json.tool "$path" >/dev/null \
    || fail "$path failed JSON parsing; expected valid JSON"
}

canonical_files=(
  README.md
  docs/STANDARD.md
  docs/PROTOCOL.md
  docs/STATE-MODEL.md
  docs/MESSAGE-MODEL.md
  docs/PROFILES.md
  docs/CONFORMANCE.md
  docs/TERMINOLOGY.md
  docs/SPECIFICATION_FREEZE_REPORT.md
  docs/QUICKSTART.md
  docs/CANONICAL_REPOSITORY_MIGRATION_MAP.md
  schemas/message.schema.json
  schemas/handshake.schema.json
  schemas/profile.schema.json
  validator/semantic_validator.py
  passpod/__init__.py
  passpod/cli.py
  passpod/message.py
  passpod/handshake.py
  passpod/profile.py
  passpod/errors.py
  tests/test_semantic_validator.py
  tests/test_sdk_core.py
  tests/test_sdk_fixture_roundtrip.py
  tests/test_cli.py
)

supporting_files=(
  LICENSE
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md
  GOVERNANCE.md
  SECURITY.md
  requirements.txt
  .github/CODEOWNERS
  .github/PULL_REQUEST_TEMPLATE.md
  .github/workflows/validate.yml
)

for path in "${canonical_files[@]}" "${supporting_files[@]}"; do
  require_file "$path"
done

require_dir examples/valid
require_dir examples/invalid
require_dir schemas
require_dir validator
require_dir passpod
require_dir tests

canonical_schema_files=(
  schemas/message.schema.json
  schemas/handshake.schema.json
  schemas/profile.schema.json
)

canonical_valid_fixtures=(
  examples/valid/minimal-propose.json
  examples/valid/propose-challenge.json
  examples/valid/propose-challenge-agree.json
  examples/valid/complete-handshake.json
  examples/valid/minimal-profile.json
)

canonical_invalid_fixtures=(
  examples/invalid/missing-parent.json
  examples/invalid/invalid-transition.json
  examples/invalid/close-before-agree.json
  examples/invalid/duplicate-message-id.json
  examples/invalid/redefine-message-type.json
)

for path in "${canonical_schema_files[@]}" "${canonical_valid_fixtures[@]}" "${canonical_invalid_fixtures[@]}"; do
  require_file "$path"
  require_json "$path"
done

require_contains README.md "PROPOSE -> CHALLENGE -> AGREE -> CLOSE" \
  "README to present the canonical four-message handshake flow"
require_contains README.md "transport-neutral" \
  "README to position Passpod as transport-neutral"
require_contains docs/STANDARD.md "transport-neutral" \
  "the Standard to preserve transport neutrality"
require_contains docs/STANDARD.md "append-only" \
  "the Standard to preserve append-only handshake history"
require_contains docs/STANDARD.md "immutable accepted messages" \
  "the Standard to preserve immutable accepted messages"
require_contains docs/PROTOCOL.md "PROPOSE -> CHALLENGE -> AGREE -> CLOSE" \
  "the Protocol to preserve the canonical handshake flow"
require_contains docs/PROTOCOL.md "The handshake history is append-only" \
  "the Protocol to preserve append-only history"
require_contains docs/PROTOCOL.md "a message is immutable" \
  "the Protocol to preserve immutable accepted messages"
require_contains docs/STATE-MODEL.md "Closure is terminal" \
  "the State Model to preserve terminal closure"
require_contains docs/STATE-MODEL.md "closure ends active negotiation" \
  "the State Model to preserve closure as the end of active negotiation"
require_contains docs/PROFILES.md "Profiles specialize Passpod" \
  "Profiles to be specializations of Passpod"
require_contains docs/PROFILES.md "Profiles MUST NOT redefine" \
  "Profiles not to redefine the protocol"
require_contains docs/CONFORMANCE.md "Semantic conformance" \
  "Conformance to preserve semantic conformance"
require_contains docs/TERMINOLOGY.md "## Archived Legacy Terminology" \
  "Terminology to isolate archived legacy terminology"

PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' || fail "Legacy terminology containment failed; expected archived-only context in active public files"
from pathlib import Path
import sys

legacy_terms = (
    "TASK",
    "TASK Core",
    "TASK Guard",
    "Sensitive Action Control",
    "Trust Action Receipt",
    "Passpod Hub",
    "AgentTrust",
    "Control Packs",
    "Pilot Access Engine",
    "Kill-State",
)

active_sections = (
    ("README.md", "## Legacy Terminology"),
    ("docs/QUICKSTART.md", "## Unsupported Behavior"),
    ("docs/TERMINOLOGY.md", "## Archived Legacy Terminology"),
    ("docs/STANDARD.md", None),
    ("docs/PROTOCOL.md", None),
    ("docs/STATE-MODEL.md", None),
    ("docs/MESSAGE-MODEL.md", None),
    ("docs/PROFILES.md", None),
    ("docs/CONFORMANCE.md", None),
)

for path_text, marker in active_sections:
    path = Path(path_text)
    text = path.read_text(encoding="utf-8")
    active = text.split(marker, 1)[0] if marker else text
    for term in legacy_terms:
        if term in active:
            print(
                f"{path_text}: active section contains legacy term {term!r}; "
                "expected historical or migration-only context",
                file=sys.stderr,
            )
            raise SystemExit(1)
PY

PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' || fail "Relative link audit failed; expected README and quickstart links to resolve"
from pathlib import Path
import re
import sys

root = Path(".").resolve()
paths = [Path("README.md"), Path("docs/QUICKSTART.md")]
missing = []

for path in paths:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        target_path = (path.parent / target).resolve()
        try:
            target_path.relative_to(root)
        except ValueError:
            missing.append(f"{path}: {target} escapes repository root")
            continue
        if not target_path.exists():
            missing.append(f"{path}: {target}")

if missing:
    for entry in missing:
        print(entry, file=sys.stderr)
    raise SystemExit(1)
PY

PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' || fail "SDK import check failed: passpod package; expected Message, Handshake, Profile, PasspodValidationError, and importable CLI"
import passpod
from passpod import Handshake, Message, PasspodValidationError, Profile
import passpod.cli

for name in ("Message", "Handshake", "Profile", "PasspodValidationError"):
    if not hasattr(passpod, name):
        raise SystemExit(f"missing package-root export: {name}")

for value in (Message, Handshake, Profile, PasspodValidationError, passpod.cli):
    if value is None:
        raise SystemExit("unexpected empty SDK or CLI import")
PY

ds_store_paths="$(find . -path './.git' -prune -o -name '.DS_Store' -print)"
if [ -n "$ds_store_paths" ]; then
  fail "Generated operating-system file found: $ds_store_paths; expected no .DS_Store files"
fi

sensitive_local_paths="$(find . -path './.git' -prune -o \( -name '.env' -o -name '.env.local' -o -name '.env.production' -o -name '.env.development' -o -name 'id_rsa' -o -name 'id_dsa' -o -name '*.pem' -o -name '*.p12' -o -name '*.pfx' \) -type f -print)"
if [ -n "$sensitive_local_paths" ]; then
  fail "Sensitive local file found: $sensitive_local_paths; expected no local secrets, credentials, or private keys"
fi

dangerous_patterns='SECRET=|PRIVATE_KEY=|BEGIN PRIVATE KEY|real customer receipt:|production signing key:|scoped key value|sk_live_|pk_live_|AKIA[0-9A-Z]{16}|private pilot record:|private pilot submission:|customer workflow dump:|full monetization workflow|exit roadmap:'
if grep -R -E "$dangerous_patterns" . \
  --exclude-dir=.git \
  --exclude="check-public-task-repo.sh" >/dev/null; then
  fail "Dangerous secret/private leakage pattern found; expected public repository boundary to exclude credentials and private operational records"
fi

echo "Passpod v0.1 public repository gate passed"
