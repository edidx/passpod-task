# Example Receipts

This directory contains public demo Trust Action Receipts for Passpod TASK Core.
They are intentionally sanitized examples for learning, schema validation, and
tooling tests.

These receipts are valid public examples, not production-valid receipts. They
use `demo-signature-not-production` and do not include production receipt IDs,
policy references, proof references, customer workflows, issuer internals, or
scoped key logic.

Production-valid receipts require authorized issuer access through Passpod Hub
and the Pilot Access Engine.

## remote-worker.receipt.json

Demonstrates a Remote Worker TrustPass-style reference check.

- `scenario_id`: `remote_worker_reference_check`
- `action`: `request_work_reference_trustpass`
- `decision`: `review_required`
- Why it matters: work-reference requests should collect consent and context
  before a trust decision is made.

## refund-review.receipt.json

Demonstrates a high-risk refund approval that needs review before execution.

- `scenario_id`: `high_risk_refund_review`
- `action`: `approve_high_risk_refund`
- `decision`: `review_required`
- Why it matters: large or risky refund actions should not execute silently.

## agent-freeze.receipt.json

Demonstrates a freeze decision for abnormal agent behavior.

- `scenario_id`: `agent_emergency_freeze`
- `action`: `freeze_agent_execution`
- `decision`: `freeze`
- Why it matters: unsafe or abnormal agent actions may need immediate pause
  before further execution.

## Validate examples

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 tools/validate-receipts.py
```

Expected result:

```text
schema-valid public demo receipt
```

That means the JSON matches the public draft schema and keeps the public demo
safety boundary. It does not mean hosted issuance, production signature
verification, or commercial authorization.
