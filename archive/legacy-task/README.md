# Legacy TASK Archive

## Status

This directory contains superseded TASK-era material. It is retained for history, migration analysis, and provenance.

This material is not canonical Passpod v0.1. Trust Action Receipts are not the primary protocol object in Passpod v0.1.

## Historical Context

The archived schema and examples come from the earlier TASK receipt family. They describe historical Trust Action Receipt concepts, demo receipt examples, and receipt-era tooling inputs.

Passpod v0.1 is defined by the Standard, Handshake Protocol, State Model, Message Model, Profile model, Conformance model, canonical schemas, canonical fixtures, semantic validator, SDK core, and CLI.

## Archived Contents

- [schemas/trust-action-receipt.schema.json](schemas/trust-action-receipt.schema.json)
- [examples/remote-worker.receipt.json](examples/remote-worker.receipt.json)
- [examples/refund-review.receipt.json](examples/refund-review.receipt.json)
- [examples/agent-freeze.receipt.json](examples/agent-freeze.receipt.json)

## Canonical Passpod v0.1 Replacements

Active schemas are:

- [../../schemas/message.schema.json](../../schemas/message.schema.json)
- [../../schemas/handshake.schema.json](../../schemas/handshake.schema.json)
- [../../schemas/profile.schema.json](../../schemas/profile.schema.json)

Active fixtures are under:

- [../../examples/valid/](../../examples/valid/)
- [../../examples/invalid/](../../examples/invalid/)

## Usage Warning

Archived examples must not be used to infer current protocol semantics. They are legacy receipt examples, not Passpod v0.1 messages, handshakes, profiles, or conformance fixtures.

Do not convert these artifacts into canonical handshakes by assumption. Any future migration of a legacy scenario requires a bounded profile or fixture design pass.

## Legacy Consumers

The following legacy consumers may still mention or load archived receipt-era material:

- `tools/validate-receipts.py`
- `tools/pilot-readiness.py`
- `validator/README.md`
- `examples/README.md`
- `SPEC.md`
- `openapi/passpod-task.public.yaml`

These consumers are retained as historical legacy material. They do not define the active Passpod v0.1 architecture.

## Provenance

The files in this directory were moved from the repository root schema and example locations using `git mv` so Git history remains traceable.
