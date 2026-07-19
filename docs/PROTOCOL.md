# Passpod Handshake Protocol

## Status

This document describes the conceptual Passpod Handshake Protocol.

The protocol is transport-neutral. It does not define individual fields, schemas, JSON, APIs, transports, validators, or SDK internals.

## Handshake Concept

A handshake is an append-only negotiation between participants.

The canonical handshake flow is:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

The flow creates a shared negotiation history. Each step adds meaning to the handshake without rewriting earlier messages.

## Participants

A participant is an actor, system, organization, profile-defined role, or other party that takes part in a handshake.

Participants may initiate proposals, raise challenges, express agreement, or close the handshake. Profiles may specialize participant roles, but the protocol does not require a particular identity system, authorization system, transport, or runtime.

## Message Relationships

Protocol messages are related by their position in a handshake.

A proposal begins a handshake. A challenge responds to a proposal or to prior negotiation context. An agreement records accepted negotiation meaning. A closure completes the handshake and records its terminal outcome.

Messages do not stand alone as isolated facts. Their meaning comes from their relationship to the handshake and to the messages that precede them.

## Parent References

Messages after the initial proposal refer back to earlier handshake context.

Parent references preserve negotiation lineage. They allow participants to understand what a message is responding to, what it depends on, and where it belongs in the handshake history.

This document does not define how parent references are represented.

## Handshake Identifier

A handshake has a stable identifier that lets participants recognize which messages belong to the same negotiation.

The identifier provides continuity across the handshake. It is not a transport requirement and this document does not define its format.

## Append-only Philosophy

The handshake history is append-only.

Participants add messages to advance negotiation. They do not rewrite accepted prior messages. Corrections, refinements, replacements, or withdrawals are expressed by adding later messages that clarify the negotiation history.

Append-only history supports reviewability, shared context, and profile-level conformance.

## Immutable Messages

Once accepted into a handshake history, a message is immutable.

Immutability means the message remains stable as part of the negotiation record. Later messages may supersede, reject, qualify, or close prior negotiation meaning, but they do not mutate the prior message itself.

## Negotiation Flow

The protocol flow is intentionally small:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

Profiles may allow repeated negotiation turns, such as additional challenges or revised proposals, as long as the handshake remains append-only and eventually reaches closure.

## PROPOSE

`PROPOSE` begins or advances a negotiation by stating what a participant wants to establish.

A proposal creates the initial subject of negotiation. It gives other participants something to examine, question, refine, or accept.

## CHALLENGE

`CHALLENGE` responds to a proposal or prior negotiation context.

A challenge asks for clarification, evidence, constraint, revision, qualification, or other negotiation work before agreement. A challenge does not close the handshake by itself.

## AGREE

`AGREE` records that the relevant participants accept the negotiated meaning for the handshake context.

Agreement is not necessarily universal across every possible party or future use. It is scoped to the handshake and any applicable profile semantics.

## CLOSE

`CLOSE` completes the handshake.

Closure records that the negotiation has reached a terminal outcome. A closed handshake is no longer active negotiation, though later systems or profiles may refer to the closed record.

## Transport Neutrality

The protocol does not depend on HTTP, queues, email, files, ledgers, databases, blockchains, wallets, browsers, or any other transport.

A transport can carry protocol messages, but the transport is not the protocol.

## Relationship to the Standard, SDK, and Profiles

The Standard defines protocol semantics.

The SDK implements the protocol.

Profiles specialize the protocol.

The protocol remains the shared negotiation model across those layers.

