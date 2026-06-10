#!/usr/bin/env python3
import json
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit("Missing dependency. Run: python3 -m pip install -r requirements.txt") from exc


SCHEMA_PATH = Path("schemas/trust-action-receipt.schema.json")
EXAMPLES_DIR = Path("examples")
DEMO_SIGNATURE = "demo-signature-not-production"
FORBIDDEN_PUBLIC_MARKERS = (
    "BEGIN " + "PRIVATE KEY",
    "PRIVATE_KEY" + "=",
    "SECRET" + "=",
    "sk_" + "live_",
    "pk_" + "live_",
    "AKIA",
    "scoped key " + "value",
    "production signing " + "key",
    "real customer " + "receipt",
)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def public_safety_errors(path, receipt):
    errors = []
    text = path.read_text(encoding="utf-8")

    for marker in FORBIDDEN_PUBLIC_MARKERS:
        if marker in text:
            errors.append(f"contains forbidden public marker: {marker}")

    signature = receipt.get("signature")
    if signature != DEMO_SIGNATURE:
        errors.append("public examples must keep the demo signature marker")

    if receipt.get("receipt_id"):
        errors.append("public examples must not claim a production receipt_id")

    if receipt.get("policy_ref"):
        errors.append("public examples must not include production policy_ref")

    if receipt.get("proof_ref"):
        errors.append("public examples must not include production proof_ref")

    return errors


def main():
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    paths = sorted(EXAMPLES_DIR.glob("*.receipt.json"))
    ok = True

    if not paths:
        print("❌ examples: no *.receipt.json files found")
        return 1

    for path in paths:
        receipt = load_json(path)
        schema_errors = sorted(validator.iter_errors(receipt), key=lambda err: list(err.path))
        safety_errors = public_safety_errors(path, receipt)

        if schema_errors or safety_errors:
            ok = False
            print(f"❌ {path}: invalid public demo receipt")
            for err in schema_errors:
                field = ".".join(str(part) for part in err.path) or "<root>"
                print(f"   schema: {field}: {err.message}")
            for err in safety_errors:
                print(f"   safety: {err}")
            continue

        print(f"✅ {path}: schema-valid public demo receipt")

    return 0 if ok else 1


raise SystemExit(main())
