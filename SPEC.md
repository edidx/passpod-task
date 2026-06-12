# Passpod TASK Core Specification

## Status

Public v0.1 draft standard proposal.

This document describes the public Passpod TASK Core contract in this
repository. It is intended for review, local validation, and public discussion
of Sensitive Action Control. It is not a production issuance specification.

## Category

Sensitive Action Control.

## Core principle

No receipt, no sensitive action.

Sensitive actions should not execute silently. A TASK check produces a Trust
Action Receipt that records what was checked, who or what requested the action,
what the action targeted, what decision was returned, and what evidence labels
were considered.

## Trust Action Receipt

A Trust Action Receipt is the portable output of a TASK decision.

In this public v0.1 draft, a receipt is a JSON object that can be validated
against `schemas/trust-action-receipt.schema.json`. A schema-valid public
receipt means the object follows the draft shape. It does not mean the receipt
was issued by a production service, signed by a production issuer, stored by a
hosted verification service, or accepted for a real workflow.

## Required Fields

The public v0.1 schema requires these fields:

- `receipt_type`: must be `trust_action_receipt`.
- `scenario_id`: identifies the scenario or control pattern being tested.
- `actor`: identifies the requester, reviewer, agent, system, or role attempting the action.
- `subject`: identifies the target of the action. Conceptually, this is the action target.
- `action`: names the sensitive action being checked before execution.
- `decision`: the TASK decision result.
- `evidence`: an array of evidence labels or reason labels considered by the check.
- `issued_at`: an RFC 3339 date-time string for when the public draft receipt was produced.

## Optional Public Fields

The public schema also allows optional fields:

- `module`: names a public module or example context, such as AgentTrust or Remote Worker Trust.
- `signature`: allowed in public examples only as a demo marker.
- `receipt_id`: allowed by the schema as a response or lookup identifier, but public examples must not claim production receipt IDs.
- `policy_ref`: conceptually points to a policy or rule set used in a real workflow. Production workflow mapping belongs to Pilot Access.
- `proof_ref`: conceptually points to hosted verification or proof material. Hosted verification belongs to Pilot Access.

The schema currently permits additional properties so the draft can evolve
without breaking early public examples. Additional fields must not be used to
smuggle private workflows, issuer internals, scoped access logic, customer data,
or hosted Passpod Hub behavior into the public repo.

## Decision Meanings

- `allow`: the action is allowed to continue under the checked policy context.
- `deny`: the action is rejected and should not continue.
- `review_required`: the action needs human or policy review before execution.
- `freeze`: the action, agent, account, or workflow should be paused to prevent further execution.
- `revoke`: an existing permission, delegation, token, or action allowance should be withdrawn.

These decisions describe control outcomes. They do not replace the responsible
party, legal authority, business owner, or production approval process.

## Public Demo Receipts vs Production-Valid Receipts

Receipts in `examples/` are public demo receipts. They are intentionally
sanitized and use:

```json
"signature": "demo-signature-not-production"
```

Public demo receipts are useful for learning, schema validation, and tooling
tests. They are not production-valid receipts.

A production-valid receipt requires controls that are intentionally outside
this repository, including issuer authority, production signing, hosted
verification, retention rules, escalation behavior, and workflow-specific
security review. Use Pilot Access for real workflows.

## Public Validation

The public validator checks example receipts against the JSON Schema and keeps
the examples in demo-only mode. A passing validator result means:

- the JSON is well formed;
- the receipt matches the public draft schema;
- the example keeps the public demo safety boundary.

A passing validator result does not mean production issuance, production
signature verification, commercial authorization, or hosted receipt lookup.

## Ecosystem Positioning

- Passpod Protocol: governance, doctrine, and receipt-backed control principles.
- Passpod TASK Core: public schema, examples, validator, and OpenAPI reference in this repo.
- Passpod Hub: hosted production layer; not included in this repo.
- Control Packs: AgentTrust and Remote Worker Trust.
- Pilot Access Engine: scoped pilot access path; not included in this repo.
- DIDX: steward and company source of truth for the ecosystem.

## Public/Private Boundary

This repository must not contain production signing internals, issuer internals,
scoped key generation, Passpod Hub internals, customer workflows, real customer
data, or private commercial logic.

The public draft should remain inspectable, local-first, and safe to fork while
preserving the boundary between public validation and production trust services.
