# Passpod Examples

These examples are canonical Passpod v0.1 fixtures for local validation, SDK
round trips, CLI behavior, and conformance discussion.

## Valid Fixtures

[valid/](valid/) contains artifacts expected to pass schema and semantic
validation:

- `minimal-propose.json`: a minimal `PROPOSE` message.
- `propose-challenge.json`: a handshake through `CHALLENGE`.
- `propose-challenge-agree.json`: a handshake through `AGREE`.
- `complete-handshake.json`: a closed `PROPOSE -> CHALLENGE -> AGREE -> CLOSE`
  handshake.
- `minimal-profile.json`: a minimal Profile model artifact.

## Invalid Fixtures

[invalid/](invalid/) contains JSON-shaped artifacts expected to fail validation:

- `missing-parent.json`
- `invalid-transition.json`
- `close-before-agree.json`
- `duplicate-message-id.json`
- `redefine-message-type.json`

These fixtures are useful for deterministic error-code behavior and negative
conformance checks.

## Usage

Validate a fixture from the repository root:

```bash
python3 -m passpod.cli validate examples/valid/complete-handshake.json
```

Inspect a fixture from the repository root:

```bash
python3 -m passpod.cli inspect examples/valid/complete-handshake.json
```

SDK fixture round-trip coverage is exercised in
[../tests/test_sdk_fixture_roundtrip.py](../tests/test_sdk_fixture_roundtrip.py).

## Historical Material

Archived receipt examples are retained at
[../archive/legacy-task/examples/](../archive/legacy-task/examples/) for
history, migration analysis, and provenance. They are not current Passpod v0.1
fixtures.
