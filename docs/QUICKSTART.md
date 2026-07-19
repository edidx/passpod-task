# Passpod Developer Quickstart

This quickstart helps a developer run the current Passpod v0.1 repository locally.

## Requirements

- Python 3
- Repository checkout
- Standard library interfaces for the Passpod SDK and CLI

Validation uses the repository validator dependency declared in [requirements.txt](../requirements.txt).

## Run All Tests

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```

## Validate Fixtures

Validate a known-good handshake fixture:

```bash
python3 -m passpod.cli validate examples/valid/complete-handshake.json
```

Validate a known-invalid handshake fixture:

```bash
python3 -m passpod.cli validate examples/invalid/missing-parent.json
```

Exit-code behavior:

- `0`: command succeeded.
- `1`: recognized artifact is invalid.
- `2`: usage, file, parsing, root-shape, or artifact-detection failure.

Machine-readable output is available with `--json`:

```bash
python3 -m passpod.cli validate examples/valid/complete-handshake.json --json
```

## Inspect A Handshake

Inspect a bounded handshake summary:

```bash
python3 -m passpod.cli inspect examples/valid/complete-handshake.json
```

Inspect the same artifact as JSON:

```bash
python3 -m passpod.cli inspect examples/valid/complete-handshake.json --json
```

Inspection prints only a bounded summary. It does not print full message payloads, evidence payloads, extension payloads, or complete participant payloads.

## SDK Example

```python
import json
from pathlib import Path

from passpod import Handshake

path = Path("examples/valid/complete-handshake.json")
mapping = json.loads(path.read_text(encoding="utf-8"))

handshake = Handshake.from_mapping(mapping)

print(handshake.lifecycle)
print(handshake.message_count)

round_tripped = handshake.to_mapping()
```

SDK objects accept mappings. File loading stays with Python's standard library.

## Validation Layers

Passpod validation proceeds through these layers:

1. JSON parsing.
2. Structural schema validation.
3. Semantic protocol validation.
4. SDK value-object boundary.

The Passpod Standard and Handshake Protocol remain the source of protocol semantics. The schemas, validator, SDK, and CLI consume those semantics; they do not replace them.

## Unsupported Behavior

The current repository does not include:

- network transport;
- HTTP API;
- persistence;
- signatures or cryptography;
- identity verification;
- reference profile implementation;
- legacy TASK behavior.
