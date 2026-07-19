# Passpod Standard

## Status

This document establishes the purpose and semantic boundary of the Passpod Standard.

The Standard defines what Passpod means at the architecture level. It does not define message formats, JSON structures, APIs, schemas, validators, SDK code, or transport bindings.

## Scope

The Passpod Standard defines the semantics for structured trust negotiation between participants.

The active architecture consists of:

- Passpod Standard
- Passpod Handshake Protocol
- Passpod SDK
- Reference Profiles
- Passpod Pilot

The Standard defines the meaning of the architecture and the responsibilities of each layer. It is the source of semantic alignment for the protocol, SDK, profiles, and pilot work.

## Objectives

The objectives of the Standard are to:

- define the core Passpod concepts in transport-neutral terms;
- define the relationship between proposals, challenges, agreements, and closures;
- support interoperable implementations without prescribing a single runtime;
- allow profiles to specialize Passpod for specific domains without changing the core semantics;
- provide a conformance philosophy for implementations, profiles, documentation, and pilots;
- keep public semantics distinct from private implementation and operational detail.

## Non-objectives

The Standard does not:

- define individual message fields;
- define JSON or any other serialization format;
- define schemas;
- define HTTP routes, APIs, webhooks, or transports;
- define SDK code or package structure;
- define validators or conformance test suites;
- prescribe storage, signing, identity, payment, deployment, or hosting systems;
- make any archived legacy terminology part of the active architecture.

## Relationship with the Protocol

The Standard defines the semantics. The Handshake Protocol expresses those semantics as a transport-neutral negotiation flow.

The canonical protocol flow is:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

The Standard explains what the protocol is for. The protocol explains how participants move through a handshake. The Standard remains higher-level than the protocol and does not define protocol message formats.

## Relationship with the SDK

The SDK implements the protocol.

An SDK may help participants create, interpret, validate, transmit, store, or inspect protocol messages, but the Standard does not prescribe SDK internals. SDK behavior is conformant when it preserves the semantics of the Standard and the ordering discipline of the Handshake Protocol.

## Relationship with Profiles

Profiles specialize the protocol for a specific domain, workflow, ecosystem, or trust context.

A profile may define domain-specific expectations, evidence conventions, extension rules, terminology, or participant roles. A profile must not redefine the core meaning of `PROPOSE`, `CHALLENGE`, `AGREE`, or `CLOSE`.

Profiles are subordinate to the Standard. They may narrow or extend usage, but they must preserve protocol semantics.

## Relationship with Passpod Pilot

Passpod Pilot is the controlled path for evaluating workflow fit against the Standard, the protocol, the SDK, and relevant profiles.

Pilot work may produce operational knowledge, profile candidates, implementation feedback, or conformance questions. Pilot work does not change the Standard unless those learnings are intentionally incorporated into a later Standard revision.

## Conformance Philosophy

Conformance is semantic before it is technical.

A conformant Passpod implementation must preserve:

- the distinction between the Standard, protocol, SDK, profiles, and pilot work;
- the canonical handshake progression;
- transport neutrality;
- append-only negotiation history;
- immutable accepted messages;
- profile specialization without core semantic drift.

Conformance should be testable, but this document does not define tests.

## Extension Philosophy

Passpod is designed to allow extensions without fragmenting the core architecture.

Extensions may add domain detail, evidence conventions, profile rules, transport bindings, or implementation capabilities. Extensions must not replace the protocol flow, redefine core terms, or reintroduce archived legacy product concepts as active architecture.

An extension is acceptable when it clarifies a specialized use while preserving the Standard.

