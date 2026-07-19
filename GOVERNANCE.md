# Governance

This document describes governance boundaries for the current Passpod repository.

The repository is a combined Passpod specification repository with a reference Python SDK. It contains normative architecture documents, canonical schemas and fixtures, a semantic validator, SDK value objects, a local CLI, tests, supporting documentation, and migration archive material.

## Governance Scope

Governance applies to:

- the Passpod Standard and normative documents;
- the Handshake Protocol;
- the State Model;
- the Message Model;
- the Profile model;
- the Conformance model;
- canonical schemas and fixtures;
- the reference Python SDK;
- the semantic validator;
- the CLI;
- supporting documentation.

The Standard remains the semantic authority for Passpod. The SDK, CLI, validator, schemas, fixtures, tests, CI, and repository gate consume the frozen semantics; they do not replace them.

## Change Categories

Changes may fall into more than one category:

- normative;
- implementation;
- documentation;
- Profile;
- archive or migration;
- security-sensitive.

The category determines the review care required. This document does not create a separate RFC process, standards body, voting procedure, or certification program.

## Normative Changes

Normative changes alter the meaning of the Passpod architecture.

Normative changes include changes to the meaning of:

- `PROPOSE`;
- `CHALLENGE`;
- `AGREE`;
- `CLOSE`;
- append-only history;
- immutable accepted messages;
- terminal closure;
- Profiles;
- core conformance.

Normative changes require explicit project-governance approval before merge. The exact final authority for normative approval is not fully defined in this repository.

Breaking normative changes require a future specification version. They must not be introduced silently through SDK behavior, validator behavior, CLI behavior, schema shape, tests, documentation examples, or profile language.

## Implementation Changes

Implementation changes include changes to:

- SDK ergonomics;
- CLI behavior;
- validator implementation;
- tests;
- tooling;
- CI;
- documentation presentation.

Implementation changes must remain conformant with the frozen normative documents. They may improve local developer experience, validation behavior, or code structure, but they must not redefine the protocol.

## Profile Changes

Profiles specialize Passpod for a domain or workflow. Profiles must not redefine:

- `PROPOSE`;
- `CHALLENGE`;
- `AGREE`;
- `CLOSE`;
- append-only history;
- immutable accepted messages;
- Standard semantics;
- Protocol semantics.

Profile approval authority is unresolved. A profile may be proposed or reviewed for semantic compatibility, but this document does not assign final profile approval to any committee, standards body, release manager, or other new governance body.

## Compatibility

Passpod Specification v0.1 is conceptually frozen.

Implementation changes must not silently redefine the protocol. Profile compatibility may evolve independently, but no universal version syntax is defined in this document.

## Historical Archive

The `archive/legacy-task/` directory is retained for provenance, migration analysis, and decision history.

Archived files are non-canonical. They must not be treated as sources of active protocol meaning, release authority, security authority, or profile authority.

## Authority Boundaries

Repository ownership evidence is limited. The current repository includes `.github/CODEOWNERS`, which identifies repository review ownership, and legal/supporting files that should not be expanded into broader governance claims without explicit approval.

Unresolved authority questions include:

- Standard stewardship;
- normative-change approval;
- Profile approval;
- SDK release authority;
- CLI release authority;
- security reporting contact;
- code-of-conduct enforcement contact;
- pilot approval;
- archive authority.

Until those questions are resolved, contributors should make bounded changes, preserve the active architecture, and avoid claims of formal standards-body recognition, certification, production readiness, or community governance.
