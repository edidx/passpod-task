# Passpod Profiles

## Status

This document defines the conceptual model for Passpod Profiles.

Profiles are first-class architecture. Profiles specialize Passpod. Profiles do not redefine Passpod.

This document does not define JSON, schemas, SDK classes, APIs, storage, cryptography, transports, or implementation.

## Purpose

Profiles exist so Passpod can adapt to different domains while preserving a single Standard and Handshake Protocol.

A profile gives domain-specific meaning to participant roles, evidence expectations, terminology, extensions, workflow guidance, and terminal interpretation. It allows a domain to be precise without changing the core architecture.

Profiles make specialization explicit. They prevent domain assumptions from silently becoming universal Passpod semantics.

## Relationship to Other Documents

Profiles are subordinate to the Standard, Protocol, State Model, Message Model, and Conformance documents.

Profiles may specialize those documents for a domain, but they must preserve their normative meaning.

### Standard

The Standard defines Passpod semantics.

A profile may narrow or clarify Standard semantics for a domain, but it must not replace the Standard or create conflicting semantics.

### Protocol

The Protocol defines the canonical handshake:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

A profile may guide how a domain uses the handshake, but it must not redefine the protocol messages or the protocol's transport-neutral character.

### State Model

The State Model defines conceptual message and handshake lifecycles.

A profile may interpret terminal outcomes or add domain guidance for lifecycle usage, but it must not replace append-only history, immutable accepted messages, or closure as the end of active negotiation.

### Message Model

The Message Model defines conceptual relationships between messages, handshakes, participants, profiles, evidence, references, versions, and extensions.

A profile may add domain-specific expectations for those relationships, but it must not prescribe core representation details unless it is explicitly defining a profile-level convention.

### Conformance

The Conformance document defines how artifacts align with Passpod.

A profile may add profile-specific conformance expectations, but it must preserve core conformance and must not make profile-specific behavior appear universal.

## Profile Concept

A Profile is a domain-specific specialization of Passpod.

A profile describes how the Passpod Standard, Handshake Protocol, State Model, and Message Model apply in a particular domain or workflow context.

Illustrative domains may include:

- employment;
- banking;
- procurement;
- healthcare;
- education;
- digital identity.

These are illustrative only. This document does not prescribe any active profile.

## What Profiles MAY Define

Profiles MAY define domain-specific guidance and constraints, conceptually including:

- participant roles;
- evidence expectations;
- terminology;
- domain-specific extensions;
- version expectations;
- workflow guidance;
- terminal outcome interpretation;
- optional constraints.

Profile definitions must remain compatible with the active Passpod architecture.

## What Profiles MUST NOT Redefine

Profiles MUST NOT redefine:

- `PROPOSE`;
- `CHALLENGE`;
- `AGREE`;
- `CLOSE`;
- append-only history;
- immutable accepted messages;
- Standard semantics;
- Protocol semantics.

A profile that redefines the core architecture is not a conformant Passpod Profile.

## Profile Lifecycle

Profile lifecycle stages are conceptual governance stages, not implementation states.

### Draft

A Draft profile is exploratory and not yet approved as a stable specialization.

### Review

A Review profile is being evaluated for semantic compatibility, domain usefulness, and conformance with the active architecture.

### Approved

An Approved profile is accepted as a conformant specialization for its stated domain or workflow context.

### Deprecated

A Deprecated profile remains historically understandable but is no longer recommended for new use.

### Archived

An Archived profile is preserved for historical, migration, or audit purposes and is outside active use.

## Profile Versioning

Profiles evolve independently.

The Standard, Protocol, Message Model, Conformance model, and individual Profiles may have different version histories.

Profile versioning supports compatibility, migration, and interpretation. This document does not prescribe version syntax.

## Profile Extensions

Profiles may introduce compatible extensions.

Profile extensions may add domain detail, evidence conventions, participant role distinctions, workflow guidance, or optional constraints.

Extensions must preserve semantic compatibility with the Standard, Protocol, State Model, Message Model, and Conformance model.

An extension must not use profile specificity to redefine Passpod itself.

## Future Reference Profiles

Future reference profiles may exist.

Reference profiles are intentionally outside this document. This document defines the profile model only; it does not create actual profiles or select active profile domains.

## Non-goals

This document does not define:

- schemas;
- APIs;
- SDKs;
- validators;
- CLI;
- storage;
- signatures;
- certification;
- implementation.

