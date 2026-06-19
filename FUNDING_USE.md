# Funding Use: Codex Open Source Fund

Passpod TASK Core is a public open-source standard layer for sensitive-action control: **no receipt, no sensitive action**.

This repository provides schemas, examples, validator/CLI tooling, OpenAPI references, and documentation for Trust Action Receipts and decision states such as `allow`, `deny`, `review_required`, `freeze`, and `revoke`.

## Why API credits matter

Passpod TASK Core is security-sensitive OSS. Developers may copy its schemas, examples, and validation patterns when building AI-agent, automation, approval, or sensitive-action workflows. Weak examples or inconsistent validation could spread unsafe patterns.

API credits would help maintain and harden the public OSS layer as a solo maintainer.

## Planned use of API credits

Credits would be used for public repository maintenance only:

- Codex-assisted schema validation checks
- Validator and CLI test generation
- OpenAPI consistency checks
- Example receipt generation and review
- Regression tests for valid and invalid receipts
- Detection of unsafe or ambiguous examples
- Documentation drift checks
- Release note and changelog drafting
- Issue and pull request triage automation
- Security review of receipt, state, and revocation flows

## Not for private commercial use

Credits requested for this repository would not be used for private customer operations, private pilot data, commercial backend execution, or production key issuance.

Commercial and private systems remain separate from this public OSS standard layer.

## 30 / 60 / 90 day plan

### First 30 days

- Harden validator examples
- Add invalid and replay-risk test cases
- Improve README quickstart
- Add clear public/private boundary notes

### First 60 days

- Expand receipt gallery
- Add OpenAPI/schema drift checks
- Add issue templates for schema, security, docs, and validator feedback

### First 90 days

- Add maintainer automation for pull request review
- Publish release workflow notes
- Improve standards crosswalk notes for OWASP, NIST, OpenID, W3C DID/VC, EUDI, MCP, and FIDO
