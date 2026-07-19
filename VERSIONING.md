# Versioning

## Purpose

Versioning communicates compatibility across the Passpod specification and its reference implementation.

The repository is a combined Passpod specification repository with a reference Python SDK. Different layers may evolve independently, and this document does not collapse them into one universal version number.

## Version Domains

### Specification Version

The specification version identifies the normative Passpod architecture and semantics.

The current conceptual specification is:

```text
Passpod Specification v0.1
```

Its frozen documents are under `docs/`. This phrase describes the conceptual specification state; it does not imply a Git tag unless such a tag exists.

### Protocol Version

A future protocol-version identifier may be needed for message compatibility.

No separate protocol version representation is currently defined by the canonical documents or schemas.

### Schema Version

Canonical schemas currently express the machine-readable v0.1 model.

Schema changes must preserve compatibility or intentionally version compatibility. This repository does not currently define schema package releases.

### Profile Version

Profiles evolve independently from the core specification.

No active reference Profile is currently implemented, and this document does not define Profile version syntax.

### SDK and CLI Version

The reference Python SDK and CLI exist in this repository.

They are not currently presented as published packages, and this document does not create SDK or CLI package versions.

### Repository Tags and Releases

Git tags identify repository snapshots.

A repository tag does not automatically mean the specification, protocol, schemas, profiles, SDK, CLI, and repository all share the same version number.

Existing repository tags are historical TASK-era snapshots unless later evidence establishes a different scope.

## Compatibility Principles

- Normative semantic changes require an intentional future specification version.
- Implementation changes must not silently redefine frozen semantics.
- Backwards-compatible SDK ergonomics may evolve independently.
- Validator error-code changes may affect consumers and must be deliberate.
- Schemas and fixtures must remain traceable to applicable normative documents.
- Profile compatibility is scoped to each Profile.
- Archived TASK-era versions do not define Passpod v0.1 compatibility.

This document does not promise permanent backwards compatibility.

## Breaking Changes

A breaking change is a change that makes existing conformant material, tooling behavior, or documented compatibility expectations incompatible with the affected version domain.

Normative breaking changes may include:

- redefining `PROPOSE`, `CHALLENGE`, `AGREE`, or `CLOSE`;
- changing append-only history semantics;
- changing immutable accepted-message semantics;
- changing terminal closure semantics;
- changing core Profile non-redefinition rules.

Implementation breaking changes may include:

- changing required schema structure incompatibly;
- removing stable validator error codes relied on by consumers;
- changing SDK behavior in an incompatible way;
- changing CLI behavior in an incompatible way;
- changing a Profile incompatibly.

Normative breaking changes affect the meaning of Passpod. Implementation breaking changes affect a concrete artifact such as schemas, SDK, CLI, validator, fixtures, or a Profile.

## Pre-1.0 Discipline

The `v0.x` label indicates early evolution, but frozen v0.1 semantics should still be changed deliberately and documented.

Pre-1.0 status does not remove compatibility obligations. Semantic Versioning may guide future package or SDK releases if those release surfaces are created, but this repository does not currently claim that every layer follows SemVer.

## Release and Tag Authority

Authority to approve specification releases, repository tags, SDK or CLI releases, schema compatibility changes, and Profile releases is governed by [GOVERNANCE.md](GOVERNANCE.md).

Where `GOVERNANCE.md` marks authority unresolved, this document does not resolve it.

## Archived Versions

TASK-era receipt, schema, and API versions are retained under [archive/legacy-task/](archive/legacy-task/).

They are historical and do not participate in active Passpod v0.1 compatibility.

## Non-goals

This document does not:

- create a Git tag;
- publish an SDK package;
- define a release calendar;
- define universal version syntax;
- certify compatibility;
- define Profile governance;
- create an HTTP API version.
