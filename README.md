# Passpod

Passpod is a transport-neutral standard and handshake protocol for structured trust negotiation.

It defines a small shared model for participants to propose meaning, request clarification or evidence, record agreement, and close negotiation without binding the protocol to a specific transport, storage system, identity system, or runtime.

## Core Idea

The canonical Passpod handshake is:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

- `PROPOSE`: states what a participant wants to establish.
- `CHALLENGE`: requests clarification, evidence, constraints, or revision.
- `AGREE`: records acceptance of the negotiated meaning.
- `CLOSE`: records the terminal outcome and ends active negotiation.

A handshake is append-only. Accepted messages are immutable. Later messages may clarify, qualify, or close prior negotiation meaning, but they do not rewrite accepted history.

## Why Passpod

Digital workflows often exchange data without a shared negotiation model. Domain-specific systems frequently reinvent proposal, challenge, agreement, and closure semantics, which makes interoperability harder than it needs to be.

Passpod provides a small interoperable core. Profiles allow domain specialization without forking or redefining the protocol.

## Architecture

Normative architecture documents:

- [Passpod Standard](docs/STANDARD.md): semantic authority for Passpod.
- [Passpod Handshake Protocol](docs/PROTOCOL.md): transport-neutral negotiation flow.
- [State Model](docs/STATE-MODEL.md): conceptual message and handshake lifecycles.
- [Message Model](docs/MESSAGE-MODEL.md): conceptual relationships among messages, handshakes, participants, profiles, evidence, references, versions, and extensions.
- [Profiles](docs/PROFILES.md): domain-specific specialization model.
- [Conformance](docs/CONFORMANCE.md): alignment requirements for documents, profiles, SDKs, validators, CLIs, and related materials.
- [Terminology](docs/TERMINOLOGY.md): active terminology and archived legacy terminology.
- [Specification Freeze Report](docs/SPECIFICATION_FREEZE_REPORT.md): consistency audit for Passpod Specification v0.1.

Implementation tooling:

- [Schemas](schemas): machine-readable representations of the frozen conceptual models.
- [Examples](examples): valid and invalid JSON fixtures.
- [Validator](validator/semantic_validator.py): structural and semantic validation.
- [Passpod SDK](passpod): minimal Python value-object boundary.
- [CLI](passpod/cli.py): local `validate` and `inspect` commands.
- [Tests](tests): unittest coverage for validator, SDK, fixtures, and CLI.

Passpod Pilot is the controlled evaluation path for workflow fit, profile candidates, and implementation feedback. Pilot work does not change the Standard unless incorporated into a later revision.

## Repository Map

- `docs/STANDARD.md`, `docs/PROTOCOL.md`, `docs/STATE-MODEL.md`, `docs/MESSAGE-MODEL.md`, `docs/PROFILES.md`, `docs/CONFORMANCE.md`: canonical documents.
- `schemas/message.schema.json`, `schemas/handshake.schema.json`, `schemas/profile.schema.json`: current Passpod v0.1 schemas.
- `examples/valid/`: valid message, handshake, and profile fixtures.
- `examples/invalid/`: invalid fixtures used to exercise semantic validation.
- `validator/semantic_validator.py`: validator authority used by the SDK and CLI.
- `passpod/`: minimal Python SDK and CLI module.
- `tests/`: local test suite.
- `docs/QUICKSTART.md`: developer quickstart.

Legacy repository files may remain for historical or migration context. They are not the active Passpod v0.1 architecture.

## Quick Example

```json
{
  "handshakeIdentity": "hs-example-001",
  "messages": [
    {
      "messageIdentity": "msg-propose-001",
      "handshakeIdentity": "hs-example-001",
      "messageType": "PROPOSE",
      "sender": "participant-alpha"
    },
    {
      "messageIdentity": "msg-challenge-001",
      "handshakeIdentity": "hs-example-001",
      "parentReference": "msg-propose-001",
      "messageType": "CHALLENGE",
      "sender": "participant-beta"
    },
    {
      "messageIdentity": "msg-agree-001",
      "handshakeIdentity": "hs-example-001",
      "parentReference": "msg-challenge-001",
      "messageType": "AGREE",
      "sender": "participant-alpha"
    },
    {
      "messageIdentity": "msg-close-001",
      "handshakeIdentity": "hs-example-001",
      "parentReference": "msg-agree-001",
      "messageType": "CLOSE",
      "sender": "participant-beta"
    }
  ]
}
```

This is a compact schema-shaped example. It does not define a transport, storage mechanism, signature, identity verification method, or profile implementation.

## Python SDK

Use the repository-local package directly from a checkout:

```python
import json
from pathlib import Path

from passpod import Handshake, Message, PasspodValidationError, Profile

mapping = json.loads(Path("examples/valid/complete-handshake.json").read_text())

try:
    handshake = Handshake.from_mapping(mapping)
except PasspodValidationError as error:
    print(error.errors)
else:
    print(handshake.lifecycle)
    print(handshake.message_count)
```

The package root exposes `Message`, `Handshake`, `Profile`, and `PasspodValidationError`. The SDK does not generate identifiers, load files for you, or define transports.

## CLI

Run the local CLI as a module:

```bash
python3 -m passpod.cli validate <path>
python3 -m passpod.cli inspect <path>
python3 -m passpod.cli validate <path> --json
python3 -m passpod.cli inspect <path> --json
```

Exit codes:

- `0`: command succeeded.
- `1`: recognized artifact is invalid.
- `2`: usage, file, parsing, root-shape, or artifact-detection failure.

The CLI supports only `validate` and `inspect`.

## Current Status

Passpod Specification v0.1 is conceptually frozen.

The repository currently includes canonical documents, schemas, valid and invalid fixtures, a semantic validator, a minimal Python SDK core, SDK ergonomics, and a local CLI.

The implementation is minimal and transport-neutral. Production transports, persistence, signatures, cryptography, identity verification, and profile implementations are not included.

## Pilot

Passpod Pilot is the controlled evaluation path for workflow fit, profile candidates, and implementation feedback.

Pilot work may produce operational learning, profile candidates, implementation feedback, or conformance questions. It does not redefine the active architecture.

## Legacy Terminology

Previous repository material may refer to archived concepts such as:

- TASK Core
- TASK Guard
- Passpod Hub
- AgentTrust
- Control Packs
- Pilot Access Engine
- Sensitive Action Control
- Trust Action Receipt as the primary protocol object

These terms are outside the active Passpod v0.1 architecture. They are preserved as repository history and migration context, not presented as current product modules.

Historical migration references:

- [Legacy specification](SPEC.md)
- [Legacy receipt schema](archive/legacy-task/schemas/trust-action-receipt.schema.json)
- [Legacy OpenAPI reference](archive/legacy-task/openapi/passpod-task.public.yaml)
- [Legacy examples guide](examples/README.md)
- [Legacy validator guide](validator/README.md)
- [Legacy pilot access notes](PILOT_ACCESS.md)
- [Legacy commercial boundary notes](COMMERCIAL_BOUNDARY.md)

Archived legacy wording may include:

```text
Public demo receipts in this repository are not production-valid receipts.
Production-valid receipts require authorized issuer access through Passpod Hub and the Pilot Access Engine.
Passpod TASK Core -> Passpod Hub -> Control Packs -> Pilot Access -> paid pilot / Team / Enterprise.
```

Those archived statements describe previous repository positioning. They do not define the active Passpod v0.1 architecture.

## License and Contribution

- [License](LICENSE)
- [Contributing](CONTRIBUTING.md)
- [Governance](GOVERNANCE.md)
- [Security](SECURITY.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
