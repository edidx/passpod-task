# Security Policy

Please report security concerns privately.

The current evidence-backed contact is `pilots@passpod.io`. Whether this remains the long-term security contact or is replaced by a dedicated security-reporting path is unresolved.

If the hosting platform provides a private security-reporting mechanism for this repository, use that private mechanism. Otherwise, use the contact above. Do not post sensitive details publicly.

## Security Scope

Security reports may concern:

- validator bypasses;
- invalid lifecycle acceptance;
- parent-reference failures;
- duplicate identity handling;
- mutation or defensive-copy failures;
- CLI data exposure;
- secret or private-data leakage;
- unsafe network behavior if transport work is added later;
- dependency vulnerabilities;
- archive material accidentally becoming active.

## Current Boundaries

The current reference implementation does not include:

- transport;
- HTTP APIs;
- persistence;
- signatures;
- cryptography;
- identity verification;
- authorization;
- production infrastructure.

Do not assume those unsupported layers are secured by this repository.

## Sensitive Data

Do not submit:

- real secrets;
- private keys;
- tokens;
- private pilot records;
- customer data;
- sensitive evidence payloads.

Use synthetic reproduction data wherever possible. Do not email sensitive secrets.

## Security Claims

This repository does not claim production-grade security, cryptographic proof, key management, enterprise deployment readiness, formal audit, certification, penetration testing, or guaranteed isolation.
