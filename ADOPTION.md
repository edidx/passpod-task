# Adopting Passpod TASK Core

Passpod TASK Core is a public draft standard proposal for Sensitive Action Control.

Vocabulary: Sensitive Action Control, Trust Action Receipt, No receipt, no sensitive action, Passpod TASK Core.

## Reader paths

- Developer: inspect the schema, examples, OpenAPI reference, and validator to understand the public receipt model.
- Security reviewer: review the demo-vs-production boundary, threat model, and public/private exclusions.
- Pilot buyer: use the public repo to evaluate the standard, then request scoped Passpod Hub access through the Pilot Access Engine.
- Standards/community reader: evaluate Sensitive Action Control, Trust Action Receipt semantics, and Passpod Protocol doctrine without relying on private product internals.

## Boundary

This repository proves the public standard and test layer. It does not expose
the full Passpod Hub product, production issuer logic, scoped key generation,
customer workflows, private commercial logic, Sentinel/Ops internals, or an
exit roadmap.
