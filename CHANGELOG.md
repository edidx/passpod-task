# Changelog

## Unreleased

### Fixed

- Reject handshake lifecycle or terminal-closure summaries that contradict the accepted message history.

### Added

- Passpod Standard, Handshake Protocol, State Model, Message Model, Profiles model, Conformance model, and Terminology documents for Passpod Specification v0.1.
- Specification freeze report documenting internal consistency of the canonical v0.1 architecture.
- Canonical machine-readable schemas for messages, handshakes, and profiles.
- Valid and invalid fixtures for the canonical handshake and profile model.
- Semantic validator for structural and protocol-level validation.
- Reference Python SDK value objects for messages, handshakes, profiles, and validation errors.
- SDK fixture round-trip coverage for canonical examples.
- CLI `validate` and `inspect` commands.
- Developer quickstart for local tests, validation, inspection, and SDK usage.
- Passpod v0.1 repository gate.
- Canonical CI validation for JSON parsing, unit tests, and the repository gate.

### Changed

- README migrated to present Passpod v0.1 as a transport-neutral specification and handshake protocol.
- Repository positioning migrated to a combined Passpod specification repository with a reference Python SDK.
- CI and pull request checks migrated from TASK-era requirements to Passpod v0.1 architecture checks.
- Governance, security, contribution, and conduct documents migrated to current Passpod v0.1 terminology and authority boundaries.

### Archived

- Legacy receipt schema and receipt examples moved into the legacy archive.
- Legacy OpenAPI and worker-reference material moved into the legacy archive.
- Legacy TASK-era specification, roadmap, and launch-readiness documents moved into the legacy archive.

See [archive/legacy-task/README.md](archive/legacy-task/README.md) for archive context. Archived materials are historical and do not define active Passpod v0.1 compatibility.

### Security

- Repository gate preserves checks for secrets, private keys, sensitive local files, and private operational data patterns.
- CLI inspection output is bounded and does not dump full message payloads, evidence references, extensions, sender payloads, or recipient payloads.

## Historical TASK-Era Tags

These tags predate the Passpod v0.1 architectural reset. They are retained as repository history and do not represent a Passpod Specification v0.1 release.

### v0.1.1

- Public validation and launch-readiness checkpoint for the earlier TASK Core architecture.

### v0.1.0

- Initial public draft structure.
