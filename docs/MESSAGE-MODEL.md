# Passpod Message Model

## Status

This document defines the conceptual structure of a Passpod message.

Representation is intentionally unspecified. JSON is only one possible serialization. Message fields named here are informative examples, not protocol requirements.

This document does not define JSON, schemas, APIs, transports, SDK classes, storage, signatures, cryptography, or implementation details.

## Purpose

The message model explains how messages relate to handshakes, participants, profiles, evidence, references, versions, and extensions.

The model provides shared vocabulary for future schemas, SDKs, validators, profiles, and documentation without committing Passpod to a particular encoding.

## Conceptual Message

A Passpod message is a unit of communication within a handshake.

Once accepted into handshake history, a message is treated as immutable. Later messages may refer to it, qualify it, supersede its negotiation meaning, or close the handshake, but they do not rewrite the accepted message.

## Message Identity

Message identity is the conceptual ability to distinguish one message from another.

An implementation may need message identity to support references, reviewability, lineage, and append-only history. The protocol does not prescribe how identity is represented.

## Handshake Identity

Handshake identity is the conceptual ability to associate messages with the same handshake.

A message belongs to a handshake context. The handshake identity gives participants a way to understand that a message is part of a bounded negotiation history.

## Parent Reference

A parent reference relates a message to earlier handshake context.

Parent references preserve negotiation lineage. They can show what a message responds to, depends on, revises, challenges, accepts, or closes.

The representation of parent references is intentionally unspecified.

## Sender

The sender is the participant responsible for emitting a message.

The sender concept does not require a specific identity system, authorization model, credential format, or runtime. Profiles may specialize sender expectations.

## Recipient

The recipient is the participant, participants, role, or audience addressed by a message.

A recipient may be explicit, profile-defined, inferred from the handshake context, or otherwise determined by a conformant implementation or profile. The core message model does not prescribe addressing mechanics.

## Timestamp Concept

A timestamp concept supports ordering, reviewability, and interpretation of handshake history.

The message model does not prescribe time format, clock source, precision, authority, synchronization, or storage behavior. Profiles may define stricter expectations when timing is material to a domain.

## Message Type

Message type is the conceptual role a message plays in the handshake.

The canonical protocol message types are `PROPOSE`, `CHALLENGE`, `AGREE`, and `CLOSE`. Profiles may add domain-specific distinctions, but they must not redefine the core meaning of the canonical message types.

## Profile Association

Profile association identifies the profile context that specializes a message or handshake.

A profile association helps participants interpret domain-specific expectations, evidence conventions, extension rules, and conformance obligations. The message model does not prescribe how profile association is encoded.

## Version Association

Version association identifies the relevant version context for the Standard, protocol, message model, profile, or extension.

Version association supports compatibility and interpretation. It does not require a particular versioning scheme.

## Evidence References

Evidence references connect a message to evidence used to support, question, qualify, or resolve negotiation.

Evidence may be introduced by proposals, requested by challenges, accepted in agreements, or summarized at closure. The message model does not define evidence format, storage, verification, or trust mechanics.

## Extension Points

Extension points allow compatible specialization without changing the core architecture.

Extensions may add domain meaning, profile conventions, transport bindings, or implementation capabilities. Extensions must preserve the Standard, the Handshake Protocol, and the append-only message history.

## Conceptual Relationships

A message belongs to a handshake.

A handshake is a bounded negotiation history between participants.

A participant emits, receives, interprets, or responds to messages.

A profile specializes how messages and handshakes are interpreted for a domain or workflow.

Evidence supports, questions, qualifies, or resolves negotiation meaning.

An extension adds compatible specialization without redefining core semantics.

## Non-requirements

This message model does not require:

- a specific data format;
- a specific serialization;
- a specific transport;
- a specific identity system;
- a specific storage system;
- a specific signature or cryptographic mechanism;
- a specific SDK structure;
- a specific validator design.

