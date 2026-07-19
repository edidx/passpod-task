# Legacy TASK Archive

## Status

This directory contains superseded TASK-era material. It is retained for history, migration analysis, and provenance.

This material is not canonical Passpod v0.1. Trust Action Receipts are not the primary protocol object in Passpod v0.1.

## Historical Context

The archived schema, examples, specification, roadmap, launch-readiness
documents, support documents, and utilities come from the earlier TASK receipt
family. They describe historical Trust Action Receipt concepts, demo receipt
examples, receipt-era tooling inputs, and TASK-era launch planning.

Passpod v0.1 is defined by the Standard, Handshake Protocol, State Model, Message Model, Profile model, Conformance model, canonical schemas, canonical fixtures, semantic validator, SDK core, and CLI.

## Archived Contents

- [docs/SPEC.md](docs/SPEC.md)
- [docs/LAUNCH_READINESS.md](docs/LAUNCH_READINESS.md)
- [docs/ROADMAP.md](docs/ROADMAP.md)
- [docs/production-checklist.md](docs/production-checklist.md)
- [docs/receipt-lifecycle.md](docs/receipt-lifecycle.md)
- [docs/standardization-roadmap.md](docs/standardization-roadmap.md)
- [schemas/trust-action-receipt.schema.json](schemas/trust-action-receipt.schema.json)
- [examples/remote-worker.receipt.json](examples/remote-worker.receipt.json)
- [examples/refund-review.receipt.json](examples/refund-review.receipt.json)
- [examples/agent-freeze.receipt.json](examples/agent-freeze.receipt.json)
- [tools/validate-receipts.py](tools/validate-receipts.py)
- [tools/pilot-readiness.py](tools/pilot-readiness.py)
- [openapi/passpod-task.public.yaml](openapi/passpod-task.public.yaml)
- [openapi/README.md](openapi/README.md)
- [worker-reference/README.md](worker-reference/README.md)

## Canonical Passpod v0.1 Replacements

Active schemas are:

- [../../schemas/message.schema.json](../../schemas/message.schema.json)
- [../../schemas/handshake.schema.json](../../schemas/handshake.schema.json)
- [../../schemas/profile.schema.json](../../schemas/profile.schema.json)

Active fixtures are under:

- [../../examples/valid/](../../examples/valid/)
- [../../examples/invalid/](../../examples/invalid/)

Active normative documents are under:

- [../../docs/](../../docs/)

Current developer guidance is:

- [../../README.md](../../README.md)
- [../../docs/QUICKSTART.md](../../docs/QUICKSTART.md)

## Usage Warning

Archived examples must not be used to infer current protocol semantics. They are legacy receipt examples, not Passpod v0.1 messages, handshakes, profiles, or conformance fixtures.

Do not convert these artifacts into canonical handshakes by assumption. Any future migration of a legacy scenario requires a bounded profile or fixture design pass.

The archived OpenAPI document describes the previous receipt-oriented HTTP service shape. The worker-reference material belongs to the same historical transport family. Neither is part of the Passpod v0.1 core, neither defines current protocol semantics, and there is currently no canonical Passpod HTTP binding.

Future HTTP binding work must be designed separately from the core protocol. The archival decision is documented in [../../docs/OPENAPI_TRANSPORT_MATERIAL_DECISION.md](../../docs/OPENAPI_TRANSPORT_MATERIAL_DECISION.md).

The archived specification, roadmap, launch-readiness, production-checklist,
receipt-lifecycle, and standardization-roadmap documents describe the previous
TASK-era specification, lifecycle, readiness, and launch model. They are
retained for provenance, decision history, and migration analysis. They are not
current normative, roadmap, release, lifecycle, production-readiness, or
launch-readiness material for Passpod v0.1.

The archived utilities operate only on archived receipt-era examples and schema
material. They are retained as historical support tools and are not part of the
active validation, SDK, CLI, CI, or repository-gate boundary.

## Legacy Consumers

The following legacy consumers may still mention or load archived receipt-era or TASK-era material:

- `archive/legacy-task/tools/validate-receipts.py`
- `archive/legacy-task/tools/pilot-readiness.py`
- `archive/legacy-task/docs/SPEC.md`
- `archive/legacy-task/docs/LAUNCH_READINESS.md`
- `archive/legacy-task/docs/ROADMAP.md`
- `archive/legacy-task/docs/production-checklist.md`
- `archive/legacy-task/docs/receipt-lifecycle.md`
- `archive/legacy-task/docs/standardization-roadmap.md`
- `archive/legacy-task/openapi/passpod-task.public.yaml`
- `archive/legacy-task/openapi/README.md`
- `archive/legacy-task/worker-reference/README.md`

These consumers are retained as historical legacy material. They do not define the active Passpod v0.1 architecture.

## Provenance

The receipt schema and examples in this directory were moved from the repository root schema and example locations using `git mv` so Git history remains traceable.

The OpenAPI and worker-reference material in this directory was moved from `openapi/` and `worker-reference/` using `git mv` to preserve the history of the legacy transport family.

The specification, launch-readiness, and roadmap documents in `archive/legacy-task/docs/` were moved from the repository root using `git mv` to preserve the history of the legacy document family.

The receipt lifecycle, production checklist, standardization roadmap, receipt
validator utility, and pilot-readiness utility were moved from active support
locations using `git mv` to preserve provenance while removing receipt-era
semantics from the active repository surface.
