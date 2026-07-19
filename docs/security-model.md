# Security Model

This document describes implementation-neutral security boundaries for the
active Passpod v0.1 repository. It is informative; the Standard remains the
semantic authority.

## Semantic Boundaries

Passpod separates protocol semantics from implementation mechanisms. The
canonical architecture preserves transport neutrality, append-only handshake
history, immutable accepted messages, and terminal closure.

Profiles may specialize domain expectations, but they do not redefine the
Standard or the canonical message types `PROPOSE`, `CHALLENGE`, `AGREE`, and
`CLOSE`.

## Validation Boundaries

Structural validation checks whether an artifact has the expected machine-
readable shape. Semantic validation checks bounded protocol rules such as
message ordering, parent references, closure, and Profile non-redefinition.

The validator evaluates artifacts against the active specification. It is not
the source of protocol semantics.

## Implementation Boundaries

The SDK uses defensive copying at value-object boundaries so caller-owned data
is not shared as mutable internal state. The CLI provides bounded local
validation and inspection; inspection avoids printing full payloads.

## Not Included

The active repository does not include:

- network transport;
- signing;
- cryptography;
- identity verification;
- authorization;
- persistence;
- production infrastructure;
- a security proof;
- production security claims.

For vulnerability reporting and repository security policy, see
[../SECURITY.md](../SECURITY.md).
