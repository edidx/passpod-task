# Validator

The public validator checks the example Trust Action Receipts against the
public JSON Schema and the demo-only safety boundary.

It validates that:

- each `examples/*.receipt.json` file is JSON;
- each example matches `schemas/trust-action-receipt.schema.json`;
- public examples keep `demo-signature-not-production`;
- public examples do not claim production receipt IDs, policy references, or
  proof references.

## Install

From the repository root:

```bash
python3 -m pip install -r requirements.txt
```

## Run

```bash
python3 tools/validate-receipts.py
```

Expected output includes:

```text
schema-valid public demo receipt
```

## Boundary

A passing validator result means the receipt is a valid public demo example. It
does not mean the receipt was issued, signed, stored, or verified by a
production service.

Production-valid receipts require authorized issuer access through Passpod Hub
and the Pilot Access Engine. This repository does not contain production
signing internals, scoped key generation, issuer logic, customer workflows, or
Passpod Hub internals.
