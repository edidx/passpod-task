# Adoption

This document explains how an evaluator, implementer, standards participant, or potential pilot partner can assess Passpod without assuming established adoption.

Passpod is a transport-neutral standard and handshake protocol for structured trust negotiation. The canonical flow is:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

Adoption in this document means evaluation, experimentation, implementation, interoperability exploration, workflow-fit analysis, Profile design, or conformance feedback. It does not imply customers, ecosystem adoption, market traction, production deployment, or formal standards recognition.

## Adoption Paths

### 1. Read The Specification

Start with:

- [README.md](README.md)
- [docs/STANDARD.md](docs/STANDARD.md)
- [docs/PROTOCOL.md](docs/PROTOCOL.md)
- [docs/STATE-MODEL.md](docs/STATE-MODEL.md)
- [docs/MESSAGE-MODEL.md](docs/MESSAGE-MODEL.md)
- [docs/PROFILES.md](docs/PROFILES.md)
- [docs/CONFORMANCE.md](docs/CONFORMANCE.md)

The Standard remains the semantic authority. The protocol, state model, message model, Profiles model, and conformance model explain how the architecture is interpreted.

### 2. Run The Reference Implementation

Use the local reference implementation to inspect the current repository behavior:

- [docs/QUICKSTART.md](docs/QUICKSTART.md)
- [schemas/](schemas/)
- [examples/valid/](examples/valid/)
- [examples/invalid/](examples/invalid/)
- [validator/semantic_validator.py](validator/semantic_validator.py)
- [passpod/](passpod/)
- [passpod/cli.py](passpod/cli.py)

The reference implementation is minimal and transport-neutral. It is useful for evaluation, fixtures, SDK behavior, CLI inspection, and validator feedback. It is not a production transport or hosted service.

### 3. Evaluate A Workflow

An evaluator may model an existing negotiation as:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

This can help identify participants, evidence expectations, constraints, agreement boundaries, and terminal outcomes. The repository does not prescribe business outcomes.

### 4. Explore A Profile Candidate

Domain-specific roles, evidence expectations, constraints, terminology, workflow guidance, and terminal interpretations belong in Profiles.

No active Reference Profile is currently implemented. A Profile candidate should preserve the Standard, the Handshake Protocol, append-only history, immutable accepted messages, and terminal closure.

### 5. Participate In Passpod Pilot

Passpod Pilot is the controlled evaluation path for workflow fit, handshake modeling, Profile candidate discovery, implementation feedback, evidence expectation discovery, conformance questions, and developer experience feedback. See [PILOT_ACCESS.md](PILOT_ACCESS.md).

Pilot work does not automatically change the Standard. Any normative change requires intentional architectural review.

## Adoption Maturity

Current status:

- Passpod Specification v0.1 is conceptually frozen.
- A minimal transport-neutral reference implementation exists.
- No production transport binding is included.
- No active Reference Profile is implemented.
- No certification program is defined.
- No conformance certification program exists.
- No guaranteed interoperability is claimed.
- No published package is assumed.
- No adoption metrics are claimed.

The existing test suite demonstrates repository behavior. It is not evidence of market adoption, production use, pilot acceptance, or standards-body recognition.

## Unsupported Commitments

This repository currently does not provide:

- production SLA;
- hosted service;
- deployment support;
- commercial support commitment;
- certification;
- cryptographic trust;
- identity verification;
- persistence;
- HTTP API;
- formal standards-body process.

These are not promised future products in this document.
