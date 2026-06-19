# Passpod TASK Core Roadmap

Passpod TASK Core is an open-source Trust Action Standard Kit for sensitive-action control.

The goal is to help developers test safer patterns before high-risk actions execute.

## Current scope

- Trust Action Receipt schema
- Example receipts
- Validator / CLI tooling
- OpenAPI reference
- Demo-only implementation guidance
- Public/private boundary documentation

## Near-term milestones

### v0.1.x — OSS clarity and testability

- Make the README understandable in 30 seconds
- Ensure fresh-clone validation works
- Add valid and invalid example receipts
- Document decision states clearly
- Improve OpenAPI/schema consistency

### v0.2.x — Security hardening

- Add replay-risk examples
- Add revocation and freeze examples
- Add unsafe-example checks
- Add regression tests for validator edge cases
- Improve security reporting and maintainer workflow

### v0.3.x — Maintainer automation

- Add issue triage workflow notes
- Add pull request review checklist automation
- Add release checklist automation
- Add documentation drift checks
- Add standards crosswalk notes

## Non-goals for this public repo

This repository does not issue production receipts, production keys, customer credentials, private pilot records, or commercial access.

Production and hosted workflows belong in a separate private/commercial boundary.
