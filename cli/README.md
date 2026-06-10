# CLI

No standalone CLI is shipped in this public v0.1 draft.

For now, use the Python validator from the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 tools/validate-receipts.py
```

Future CLI work should stay limited to public schema validation and local
developer ergonomics unless a separate production design is approved.

The CLI must not implement production signing, issuer internals, scoped key
generation, Passpod Hub internals, customer workflows, or private commercial
logic. Production-valid receipts require authorized issuer access through
Passpod Hub and the Pilot Access Engine.
