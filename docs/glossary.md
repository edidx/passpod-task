# Glossary

This glossary is an informative navigation aid. Normative definitions live in
[TERMINOLOGY.md](TERMINOLOGY.md).

## Active Terms

- Passpod: the overall architecture defined by the active specification.
- Passpod Standard: the semantic authority for Passpod.
- Handshake Protocol: the transport-neutral negotiation protocol.
- handshake: one append-only negotiation history.
- message: an immutable accepted protocol statement within a handshake.
- participant: an actor represented in a handshake.
- Profile: a domain-specific specialization of Passpod.
- evidence: information referenced during negotiation.
- reference: a conceptual pointer to another message, evidence item, or resource.
- extension: a compatible specialization point.
- conformance: alignment with the active Passpod semantics.
- Passpod SDK: the reference Python implementation surface in this repository.
- Passpod Pilot: the controlled evaluation path for workflow fit and feedback.
- PROPOSE: the initial proposal message type.
- CHALLENGE: a request for clarification, evidence, or negotiation.
- AGREE: acceptance of negotiated terms.
- CLOSE: terminal closure of a handshake.

## Legacy Terms

Archived terminology from the earlier TASK-era architecture is listed in
[TERMINOLOGY.md#archived-legacy-terminology](TERMINOLOGY.md#archived-legacy-terminology).
Those terms are outside the active Passpod v0.1 architecture.
