# Commercial Boundary

This repository is public proof for Passpod TASK Core.

It helps developers and reviewers inspect the public standard/test layer:

- Trust Action Receipt schema;
- public demo receipts;
- local validator;
- public OpenAPI reference shape;
- basic doctrine for Sensitive Action Control.

## Product stack

Passpod TASK Core -> Passpod Hub -> Control Packs -> Pilot Access -> paid pilot / Team / Enterprise.

- Passpod TASK Core is the public standard/test layer in this repo.
- Passpod Hub is the paid hosted product layer and is not included here.
- Control Packs are AgentTrust and Remote Worker Trust.
- Pilot Access Engine is the scoped access path for authorized hosted access.
- DIDX is the company, legal, and registry anchor.

## Not in this repo

This repo does not expose:

- production issuer logic;
- production signing internals;
- scoped key generation;
- Passpod Hub internals;
- customer workflows;
- private commercial strategy;
- Sentinel/Ops internals;
- exit roadmap.

Public demo receipts are not production-valid receipts. Production-valid
receipts require authorized issuer access through Passpod Hub and the Pilot
Access Engine.
