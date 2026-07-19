## Passpod v0.1 checklist

### Scope

- [ ] Change is bounded and described.
- [ ] Unrelated files are not modified.
- [ ] Active architecture is not redesigned unintentionally.

### Canonical semantics

- [ ] Preserves `PROPOSE -> CHALLENGE -> AGREE -> CLOSE`.
- [ ] Preserves transport neutrality.
- [ ] Preserves append-only history.
- [ ] Preserves immutable accepted messages.
- [ ] Preserves terminal closure.
- [ ] Profiles do not redefine core message meanings.

### Implementation

- [ ] Existing schemas remain authoritative for structure.
- [ ] Semantic validator remains authoritative for bounded protocol validity.
- [ ] SDK and CLI do not introduce new semantics.
- [ ] No unsupported transport, persistence, signature, cryptographic, or identity claims are added.

### Validation

- [ ] `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests`
- [ ] `bash tools/check-public-task-repo.sh` (Passpod v0.1 repository gate)

### Security and privacy

- [ ] No secrets, credentials, private keys, tokens, or private pilot records.
- [ ] No sensitive local files.
- [ ] Inspection output does not expose full private payloads.
- [ ] No new network behavior unless explicitly scoped in a later approved transport pass.

### Documentation

- [ ] Active terminology matches Passpod v0.1.
- [ ] Archived terms appear only in migration or historical context.
- [ ] Links and commands are verified.
- [ ] Claims do not overstate production readiness, adoption, certification, cryptography, or deployment.
