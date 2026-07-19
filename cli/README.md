# Passpod CLI

The current CLI is a thin local interface over the SDK and semantic validator.
It is transport-neutral and does not define production behavior.

## Commands

Validate an artifact:

```bash
python3 -m passpod.cli validate <path>
```

Inspect a bounded artifact summary:

```bash
python3 -m passpod.cli inspect <path>
```

Both commands support machine-readable output:

```bash
python3 -m passpod.cli validate <path> --json
python3 -m passpod.cli inspect <path> --json
```

## Exit Codes

- `0`: command succeeded.
- `1`: the artifact was recognized but invalid.
- `2`: usage, file, parsing, root-shape, or artifact-detection failure.

## Boundary

The CLI validates and inspects current Passpod messages, handshakes, and
profiles. It does not define the Standard, Protocol, schemas, validator
semantics, production transport, persistence, signatures, cryptography,
identity verification, authorization, hosted infrastructure, or Profile
implementations.

## References

- [../docs/QUICKSTART.md](../docs/QUICKSTART.md)
- [../passpod/cli.py](../passpod/cli.py)
- [../tests/test_cli.py](../tests/test_cli.py)
