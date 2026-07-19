# Passpod State Model

## Status

This document defines conceptual lifecycle states for Passpod messages and handshakes.

It does not define implementation details, message fields, schemas, transports, APIs, storage systems, validators, or SDK internals.

## Message Lifecycle

A message lifecycle describes how a single protocol message becomes part of a handshake history.

Conceptual lifecycle:

```text
[Composed]
     |
     v
[Emitted]
     |
     v
[Accepted into handshake history]
     |
     v
[Referenced by later message]
     |
     v
[Preserved as immutable history]
```

A message that is not accepted into the handshake history remains outside the authoritative negotiation record.

Conceptual rejection path:

```text
[Composed]
     |
     v
[Emitted]
     |
     v
[Not accepted into handshake history]
```

## Handshake Lifecycle

A handshake lifecycle describes the state of the negotiation as a whole.

Conceptual lifecycle:

```text
[Not started]
     |
     v
[Proposed]
     |
     v
[Challenged]
     |
     v
[Agreed]
     |
     v
[Closed]
```

Negotiation may repeat before agreement when a profile allows additional turns.

Conceptual repeated negotiation:

```text
[Proposed] -> [Challenged] -> [Revised negotiation context]
      ^                                |
      |                                v
      +--------- [Further challenge] <-+
```

## Allowed Transitions

The canonical transition path is:

```text
[Not started] -> [Proposed] -> [Challenged] -> [Agreed] -> [Closed]
```

Profiles may allow repeated proposal and challenge turns:

```text
[Proposed] -> [Challenged] -> [Proposed]
[Challenged] -> [Challenged]
[Agreed] -> [Closed]
```

Closure is terminal:

```text
[Closed] -x-> [Proposed]
[Closed] -x-> [Challenged]
[Closed] -x-> [Agreed]
```

The state model does not require every implementation to expose state names directly. The requirement is conceptual conformance to the handshake lifecycle.

## Terminal Outcomes

A handshake reaches a terminal outcome when it is closed.

Conceptual terminal outcomes:

```text
[Agreed] -> [Closed: completed]
[Challenged] -> [Closed: unresolved]
[Proposed] -> [Closed: withdrawn]
[Proposed] -> [Closed: declined]
```

Profiles may define more specific terminal meanings, but they must preserve the concept that `CLOSE` ends active negotiation.

## State Principles

The state model follows these principles:

- accepted messages are immutable;
- handshake history is append-only;
- later messages may qualify earlier messages;
- closure ends active negotiation;
- profiles may specialize state meaning without replacing the canonical protocol flow.

