# Passpod TASK Core

[![Validate TASK public repo](https://github.com/edidx/passpod-task/actions/workflows/validate.yml/badge.svg)](https://github.com/edidx/passpod-task/actions/workflows/validate.yml)

**Sensitive actions should not execute silently.**

Passpod TASK Core is a public draft standard proposal for **Sensitive Action Control**.

Every decision returns a **Trust Action Receipt**.

**No receipt, no sensitive action.**

Public demo receipts in this repository are not production-valid receipts.
Production-valid receipts require authorized issuer access through Passpod Hub and the Pilot Access Engine.

## Start here

- [Specification](SPEC.md): public v0.1 TASK Core semantics and boundaries.
- [Trust Action Receipt schema](schemas/trust-action-receipt.schema.json): JSON Schema for public draft receipts.
- [OpenAPI reference](openapi/passpod-task.public.yaml): public reference API shape only.
- [Example receipts](examples/README.md): walkthrough for the demo receipts.
- [Validator](validator/README.md): install and run local receipt validation.
- [Pilot Access](PILOT_ACCESS.md): path for real workflow review and hosted pilot access.

## Public test vs Pilot Access

Public repo: schema, examples, local validation, public draft.

Pilot Access: scoped pilot key, hosted receipt endpoint, signed pilot receipts, scenario mapping, security review, and integration support.

Request Pilot Access: pilots@passpod.io

## Public/private boundary

This repo does not contain production signing keys, scoped key generation internals, buyer-specific workflows, real customer receipts, or Passpod Hub backend code.
