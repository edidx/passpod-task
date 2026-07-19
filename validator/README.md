# Passpod Semantic Validator

The semantic validator evaluates current Passpod artifacts against the frozen
v0.1 specification. It is an evaluator, not the source of protocol semantics.

## Validation Layers

The validator performs:

- structural schema validation;
- bounded semantic validation;
- deterministic error-code reporting.

Semantic checks include message ordering, parent references, duplicate message
identity, terminal closure, and Profile non-redefinition of the core protocol.

## Public Operations

The public validator operations are:

- `validateMessage`
- `validateHandshake`
- `validateProfile`

They are implemented in [semantic_validator.py](semantic_validator.py).

## Fixtures

Canonical fixtures live under:

- [../examples/valid/](../examples/valid/)
- [../examples/invalid/](../examples/invalid/)

Valid fixtures must pass. Invalid fixtures are intentionally shaped as JSON
artifacts that fail bounded structural or semantic checks.

## Boundary

The Standard and Handshake Protocol remain authoritative. The validator
consumes the active semantics and reports evaluation results; it does not
define JSON beyond the canonical schemas, transport behavior, SDK classes,
storage, signatures, cryptography, identity, authorization, or certification.

Historical receipt validation tooling is archived at
[../archive/legacy-task/tools/validate-receipts.py](../archive/legacy-task/tools/validate-receipts.py).
It is not current Passpod validation guidance.
