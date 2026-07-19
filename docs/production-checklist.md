# Production Readiness Boundary

Passpod v0.1 is not a production deployment checklist. The repository is ready
for specification evaluation, local validation, SDK experimentation, CLI
inspection, and Passpod Pilot evaluation.

## Current Readiness

Current repository readiness covers:

- reading the frozen conceptual specification;
- validating canonical fixtures locally;
- exercising the transport-neutral SDK and CLI;
- evaluating whether workflows fit `PROPOSE -> CHALLENGE -> AGREE -> CLOSE`;
- collecting Pilot feedback and conformance questions.

## Before Production Work

Production work requires separate design and governance decisions for:

- transport;
- persistence;
- security review;
- identity;
- authorization;
- operational processes;
- production infrastructure;
- support and governance responsibilities.

## References

- [FINAL_CANONICAL_RELEASE_READINESS_AUDIT.md](FINAL_CANONICAL_RELEASE_READINESS_AUDIT.md)
- [../SECURITY.md](../SECURITY.md)
- [../PILOT_ACCESS.md](../PILOT_ACCESS.md)
