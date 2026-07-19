# OpenAPI Reference

`passpod-task.public.yaml` is a public reference shape for Passpod TASK
Core. It documents draft endpoints for spec discovery, public demo receipt
validation, and receipt lookup response shape.

This OpenAPI file is not a production API contract. It does not define or expose:

- production receipt issuance;
- production signing internals;
- scoped key generation;
- issuer internals;
- Passpod Hub internals;
- customer workflows;
- private commercial logic.

Production-valid receipts require authorized issuer access through Passpod Hub
and the Pilot Access Engine.

Use this file to understand the public validation surface only. It is safe for
developer review, mock clients, and standards discussion.
