# Passpod Terminology

## Status

This document defines active Passpod terminology and archived legacy terminology.

Active terminology belongs to the canonical architecture:

- Passpod Standard
- Passpod Handshake Protocol
- Passpod SDK
- Reference Profiles
- Passpod Pilot

Archived terminology is preserved for historical and migration context, but it is outside the active architecture.

## Normative Language

Normative terms define requirements, constraints, or authoritative meanings for Passpod.

Informative terms provide explanation, context, examples, or non-binding guidance.

## Active Terminology

### Passpod

Passpod is the overall architecture for transport-neutral trust negotiation using a standard, a handshake protocol, SDK implementations, specialized profiles, and pilot validation.

### Passpod Standard

The Passpod Standard defines the semantics of Passpod.

It defines the meaning of the architecture and the relationship between the protocol, SDK, profiles, and pilot work. It does not define message formats, schemas, APIs, or implementation code.

### Handshake Protocol

The Handshake Protocol is the canonical transport-neutral negotiation flow:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

The protocol expresses the semantics of the Standard as an append-only negotiation between participants.

### Handshake

A handshake is a bounded negotiation history between participants.

A handshake begins with a proposal, may include challenges and negotiation turns, records agreement when reached, and ends with closure.

### Message

A message is an immutable unit of handshake communication once accepted into handshake history.

Messages derive their meaning from their position in the handshake and their relationship to prior context.

### Participant

A participant is a party that takes part in a handshake.

Participants may be people, organizations, systems, agents, services, or profile-defined roles. The core architecture does not require a specific identity system.

### Profile

A profile specializes the Handshake Protocol for a domain, workflow, ecosystem, or trust context.

Profiles may define domain expectations and extension rules, but they must preserve the core meaning of `PROPOSE`, `CHALLENGE`, `AGREE`, and `CLOSE`.

### SDK

The SDK implements the Handshake Protocol.

An SDK may provide developer-facing tools for creating, interpreting, transmitting, storing, or inspecting protocol messages. SDKs must preserve Standard semantics and protocol ordering.

### Evidence

Evidence is information introduced into a handshake to support, question, qualify, or resolve negotiation.

Profiles may define evidence expectations. The core terminology does not require a specific evidence format or storage system.

### Reference

A reference is a relationship from one part of a handshake to another piece of handshake context.

References support lineage, reviewability, and negotiation continuity. This terminology does not define representation details.

### Proposal

A proposal is the negotiation meaning introduced by `PROPOSE`.

It states what a participant wants to establish within the handshake.

### Challenge

A challenge is the negotiation meaning introduced by `CHALLENGE`.

It asks for clarification, evidence, constraint, revision, qualification, or other work before agreement.

### Agreement

An agreement is the negotiation meaning introduced by `AGREE`.

It records acceptance of the negotiated meaning within the scope of the handshake and any applicable profile.

### Closure

A closure is the negotiation meaning introduced by `CLOSE`.

It ends active negotiation and records the terminal outcome of the handshake.

### Extension

An extension is a compatible specialization that adds domain detail, transport binding, implementation capability, or profile-level convention without redefining the core architecture.

Extensions must preserve the Standard and the Handshake Protocol.

### Conformance

Conformance is alignment with the Passpod Standard, the Handshake Protocol, and any declared profile.

Conformance is semantic before it is technical. A conformant implementation preserves core meaning even when transport, storage, or runtime choices differ.

### Normative

Normative material defines required meaning, constraints, or architecture.

Normative material is authoritative for conformance.

### Informative

Informative material explains, illustrates, or contextualizes Passpod.

Informative material is helpful but not authoritative for conformance unless a normative document explicitly adopts it.

## Archived Legacy Terminology

The following terms are archived legacy terminology. They may appear in historical, migration, or audit material, but they are outside the active Passpod architecture.

### TASK Guard

Archived legacy terminology outside the active architecture.

### TASK Core

Archived legacy terminology outside the active architecture.

### Passpod Hub

Archived legacy terminology outside the active architecture.

### AgentTrust

Archived legacy terminology outside the active architecture.

### Control Packs

Archived legacy terminology outside the active architecture.

### Pilot Access Engine

Archived legacy terminology outside the active architecture.

### Sensitive Action Control

Archived legacy terminology outside the active architecture.

### Trust Action Receipt as the primary protocol object

Archived legacy terminology outside the active architecture.

Trust Action Receipts may remain relevant in historical or migration documentation, but they are not the primary protocol object in the active architecture.

### Kill-State

Archived legacy terminology outside the active architecture.

