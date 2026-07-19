# Contributing

Passpod is a specification repository with a reference Python SDK, semantic validator, CLI, schemas, fixtures, tests, and migration archive.

Start with:

- [README.md](README.md)
- [docs/QUICKSTART.md](docs/QUICKSTART.md)
- [docs/STANDARD.md](docs/STANDARD.md)
- [docs/PROTOCOL.md](docs/PROTOCOL.md)
- [docs/STATE-MODEL.md](docs/STATE-MODEL.md)
- [docs/MESSAGE-MODEL.md](docs/MESSAGE-MODEL.md)
- [docs/PROFILES.md](docs/PROFILES.md)
- [docs/CONFORMANCE.md](docs/CONFORMANCE.md)
- [docs/TERMINOLOGY.md](docs/TERMINOLOGY.md)
- [.github/PULL_REQUEST_TEMPLATE.md](.github/PULL_REQUEST_TEMPLATE.md)

## Local Validation

Run these commands from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
bash tools/check-public-task-repo.sh
```

The script `tools/check-public-task-repo.sh` keeps its historical filename. Treat it as the Passpod v0.1 repository gate.

## Contribution Boundaries

Contributions must preserve:

- `PROPOSE -> CHALLENGE -> AGREE -> CLOSE`;
- transport neutrality;
- append-only history;
- immutable accepted messages;
- terminal closure;
- Profile non-redefinition;
- validator error-code stability where applicable;
- SDK and CLI behavior as consumers of semantics, not sources of semantics.

Keep changes bounded. Include tests for behavior changes. Do not mix unrelated refactors with normative architecture changes.

Do not add unsupported transports, HTTP APIs, persistence, signatures, cryptography, identity verification, authorization, production infrastructure, or published package claims unless a future approved pass explicitly scopes that work.

## Artifact Guidance

Normative documents: changes require explicit architectural review and must not be mixed casually with implementation refactors.

Schemas: express frozen concepts without inventing semantics.

Fixtures: valid and invalid fixtures must state the behavior they demonstrate.

Validator: deterministic error codes must remain stable unless intentionally versioned.

SDK: consume validator semantics and preserve defensive-copy and append-only guarantees.

CLI: remain a thin local interface over the SDK and validator.

Archive: historical files must not be rewritten as current Passpod v0.1 material.

## Pull Requests

Use the current [pull request template](.github/PULL_REQUEST_TEMPLATE.md).

Pull requests should have:

- bounded scope;
- no unrelated changes;
- exact test results;
- accurate claims;
- no secrets or private data;
- verified links and commands.

## Python Assumptions

Use Python 3.

The SDK and CLI use standard library interfaces. Validation tooling and CI use dependencies installed from [requirements.txt](requirements.txt) where required.

CI currently validates on Python 3.12. The repository does not claim PyPI publication or a packaged installation path.

## Sensitive Data

Do not submit private customer data, production keys, private keys, tokens, private pilot records, sensitive evidence payloads, or buyer-specific workflows.

Use synthetic data in fixtures, tests, issues, and pull requests.
