# Passpod Conformance

## Status

This document defines conceptual conformance for Passpod.

It does not define tests, certification, implementation checklists, schemas, APIs, transports, SDK classes, validators, storage, signatures, cryptography, or implementation details.

## Purpose

Conformance describes what it means for documents, profiles, SDKs, validators, CLIs, and related materials to align with Passpod.

Semantic conformance comes before implementation conformance. A system can only be implementation-conformant if it preserves the semantics of the Passpod Standard, the Handshake Protocol, and any declared profile.

## Normative Language

Normative language defines requirements for conformance.

The terms `MUST`, `SHOULD`, `MAY`, and `MUST NOT` are used to express requirement levels within Passpod normative material.

## MUST

`MUST` indicates a required condition for conformance.

If a conformant artifact claims to satisfy a normative requirement, it must preserve that requirement without redefining it through implementation detail, profile specialization, or extension behavior.

## SHOULD

`SHOULD` indicates a recommended condition for conformance.

An artifact may vary from a `SHOULD` requirement only when the variance is intentional, justified by the applicable profile or context, and does not violate any `MUST` or `MUST NOT` requirement.

## MAY

`MAY` indicates an allowed option.

An artifact may choose whether to implement, describe, or support a `MAY` behavior. Optional behavior must still preserve the Standard and the Handshake Protocol.

## MUST NOT

`MUST NOT` indicates a prohibited condition for conformance.

An artifact that violates a `MUST NOT` requirement is not conformant for the affected scope.

## Semantic Conformance

Semantic conformance means preserving the meaning of the Passpod architecture.

A semantically conformant artifact preserves:

- the separation between Standard, protocol, message model, profiles, SDK, validators, CLI, documentation, and pilot work;
- the canonical protocol sequence `PROPOSE`, `CHALLENGE`, `AGREE`, `CLOSE`;
- transport neutrality;
- append-only handshake history;
- immutable accepted messages;
- profile specialization without core semantic redefinition;
- extension compatibility with the active architecture.

## Standard Conformance

Standard conformance means aligning with the Passpod Standard as the semantic authority.

An artifact that claims Standard conformance MUST preserve the Standard's scope, objectives, non-objectives, conformance philosophy, and extension philosophy.

An artifact MUST NOT treat transport, encoding, storage, signatures, cryptography, SDK structure, validator behavior, or CLI behavior as part of the Standard unless the Standard itself defines that meaning.

## Protocol Conformance

Protocol conformance means preserving the Handshake Protocol.

A protocol-conformant artifact MUST preserve the canonical message meanings:

- `PROPOSE` introduces or advances what a participant wants to establish;
- `CHALLENGE` asks for clarification, evidence, constraint, revision, qualification, or other negotiation work;
- `AGREE` records accepted negotiation meaning within handshake scope;
- `CLOSE` ends active negotiation and records terminal outcome.

Profiles MAY extend the protocol, but profiles MUST NOT redefine `PROPOSE`, `CHALLENGE`, `AGREE`, or `CLOSE`.

## Message Model Conformance

Message Model conformance means preserving the conceptual relationships among messages, handshakes, participants, profiles, evidence, references, versions, and extensions.

A conformant message model artifact MUST keep representation unspecified unless it is explicitly defining a separate serialization or implementation layer.

A conformant message model artifact MUST NOT make JSON, a transport, a storage system, a signature mechanism, or an SDK class required by the core message model.

## Profile Conformance

Profile conformance means specializing Passpod without redefining Passpod.

A conformant profile MAY define domain-specific participant roles, evidence expectations, extension rules, version expectations, and terminal meanings.

A conformant profile MUST preserve the Standard, the Handshake Protocol, and the Message Model.

A conformant profile MUST NOT reintroduce archived legacy terminology as active architecture.

## SDK Conformance

SDK conformance means implementing the protocol while preserving Passpod semantics.

A conformant SDK SHOULD help developers create, interpret, transmit, store, inspect, or validate protocol messages in ways that preserve the Standard and any declared profile.

A conformant SDK MUST NOT redefine protocol message meanings through class names, runtime behavior, helper methods, or implementation convenience.

## Validator Conformance

Validator conformance means evaluating declared conformance without becoming the source of protocol meaning.

A conformant validator MAY check artifacts against the Standard, protocol, message model, profiles, or future machine-readable definitions.

A conformant validator MUST NOT make its own implementation assumptions normative unless those assumptions are defined by the applicable normative material.

## CLI Conformance

CLI conformance means exposing developer-facing operations without changing protocol semantics.

A conformant CLI MAY help compose, inspect, validate, or explain Passpod artifacts.

A conformant CLI MUST preserve the Standard, protocol, message model, and declared profile semantics.

## Documentation Conformance

Documentation conformance means describing Passpod without contradicting the normative architecture.

Conformant documentation SHOULD clearly distinguish normative requirements from informative explanation.

Conformant documentation MUST NOT present archived legacy terminology as active architecture.

## Future Conformance Classes

Future conformance classes may group requirements by artifact type. These classes are conceptual and do not define tests, certification, or implementation checklists.

### Core Conformance

Core conformance means preserving the Passpod Standard, Handshake Protocol, Message Model, and active terminology.

### Profile Conformance

Profile conformance means preserving core conformance while adding domain-specific specialization.

### SDK Conformance

SDK conformance means preserving core and declared profile conformance in developer-facing implementation.

### Validator Conformance

Validator conformance means evaluating declared requirements while preserving the authority of the normative material being evaluated.

## Non-goals

This document does not define:

- tests;
- certification;
- implementation checklists;
- schemas;
- APIs;
- SDK classes;
- validators;
- CLI commands;
- storage rules;
- signature rules;
- cryptographic requirements.

