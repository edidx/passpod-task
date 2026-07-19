# Root Package Surface Migration Audit

Post-archival note: the legacy `SPEC.md`, `LAUNCH_READINESS.md`, and `ROADMAP.md` files evaluated in this audit have since been moved to `archive/legacy-task/docs/`. Original root paths retained below describe audited pre-archival locations and dependencies, not active Passpod v0.1 authority.

## 1. Executive Summary

This audit reviewed the remaining root-level documents, package surfaces, tooling surfaces, release metadata, governance files, and supporting repository files after the Passpod v0.1 reset and the legacy receipt/OpenAPI archives.

Baseline was clean:

```text
git status --short
```

returned no output, and:

```text
git log -12 --oneline
```

showed `e8b5f41 Archive legacy OpenAPI and worker reference material` as the latest commit.

Key findings:

- The repository is currently best treated as a combined specification and reference Python SDK repository.
- There is no tracked JavaScript validator, JavaScript CLI, `package.json`, `package-lock.json`, npm bin entry, package script, or npm publication surface.
- Python packaging metadata is intentionally absent. The Python SDK/CLI is repository-local and exercised through `python3 -m passpod.cli` and unit tests.
- `requirements.txt` is still required for `jsonschema`, which is used by the canonical semantic validator and tests.
- The most active legacy confusion now sits in root and support documentation: `SPEC.md`, `LAUNCH_READINESS.md`, `ROADMAP.md`, `ADOPTION.md`, `COMMERCIAL_BOUNDARY.md`, `PILOT_ACCESS.md`, `VERSIONING.md`, `FUNDING_USE.md`, `cli/README.md`, `validator/README.md`, and several noncanonical docs.
- The highest-risk next cleanup is not package metadata. It is the old TASK specification and launch-family documents that still present receipt/TASK/Hub concepts as public doctrine.

Recommended next bounded pass:

```text
Archive legacy SPEC and launch-readiness document family
```

## 2. Audit Scope

Audited tracked assets included:

- root documents: `SPEC.md`, `CHANGELOG.md`, `VERSIONING.md`, `GOVERNANCE.md`, `ADOPTION.md`, `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `LAUNCH_READINESS.md`, `PILOT_ACCESS.md`, `ROADMAP.md`, `COMMERCIAL_BOUNDARY.md`, `FUNDING_USE.md`, `CODE_OF_CONDUCT.md`, `README.md`;
- package/dependency surfaces: `requirements.txt`, absence of `package.json`, `package-lock.json`, `pyproject.toml`, `setup.py`, `setup.cfg`, Makefile, tox config, and nox config;
- Python implementation: `passpod/`, `validator/semantic_validator.py`, canonical tests;
- documentation-only CLI and validator surfaces: `cli/README.md`, `validator/README.md`;
- tools: `tools/check-public-task-repo.sh`, `tools/validate-receipts.py`, `tools/pilot-readiness.py`;
- GitHub surfaces: `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/workflows/validate.yml`;
- noncanonical docs under `docs/`;
- historical archive under `archive/legacy-task/`.

Local empty directories were observed under `src/`, `spec/`, `packages/validator/`, and `.github/ISSUE_TEMPLATE/`. They contain no tracked files and are not treated as repository assets in this audit.

## 3. Canonical Baseline

Canonical active assets:

| Asset | Classification | Evidence |
|---|---|---|
| `README.md` | KEEP - Canonical | Active public entry point; legacy material is isolated in the legacy section. |
| `docs/QUICKSTART.md` | KEEP - Canonical | Current developer commands use canonical fixtures, SDK, CLI, tests, and unsupported-behavior boundaries. |
| `docs/STANDARD.md`, `docs/PROTOCOL.md`, `docs/STATE-MODEL.md`, `docs/MESSAGE-MODEL.md`, `docs/PROFILES.md`, `docs/CONFORMANCE.md`, `docs/TERMINOLOGY.md` | KEEP - Canonical | Normative Passpod v0.1 architecture. |
| `schemas/message.schema.json`, `schemas/handshake.schema.json`, `schemas/profile.schema.json` | KEEP - Canonical | Current machine-readable schema set. |
| `examples/valid/`, `examples/invalid/` | KEEP - Canonical | Current valid and invalid fixtures for semantic validation. |
| `validator/semantic_validator.py` | KEEP - Canonical | Active structural and semantic validator. |
| `passpod/` | KEEP - Canonical | Active repository-local Python SDK and CLI package. |
| `tests/` | KEEP - Canonical | Canonical test suite. |
| `tools/check-public-task-repo.sh` | KEEP - Canonical | Active Passpod v0.1 repository gate. |
| `.github/workflows/validate.yml` | KEEP - Canonical | Active CI runs canonical JSON parsing, tests, and gate. |

The active protocol remains:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

## 4. Root Document Inventory

| Path | Classification | Current purpose | Dependencies | Risk | Proposed future action | Predecessor actions |
|---|---|---|---|---|---|---|
| `README.md` | KEEP - Canonical | Public entry and quickstart map with quarantined legacy links. | Gate link audit; public entry. | Medium if legacy links move without updates. | Keep active; update only moved historical links in future archival passes. | Preserve link audit. |
| `SPEC.md` | ARCHIVE WITH LEGACY TASK | Historical TASK Core spec centered on Trust Action Receipt and receipt decisions. | README legacy link; historical docs; archive references. | High confusion risk if kept at root as "SPEC". | Archive intact under legacy TASK material after updating README link. | Link audit and archive README update. |
| `ADOPTION.md` | MIGRATE | Legacy adoption paths for TASK Core, receipt model, OpenAPI, Hub, and Pilot Access Engine. | Historical public surface; no canonical runtime dependency. | High public-positioning confusion. | Migrate useful reader-path concepts to Passpod v0.1 adoption guidance or archive if fully superseded. | Decide public adoption model. |
| `COMMERCIAL_BOUNDARY.md` | DEFER | Legacy commercial boundary and product stack. | README legacy link; governance/commercial claims. | High because commercial claims require human approval. | Rewrite around Passpod Pilot and support boundaries or archive old product-stack material. | Commercial and pilot policy decision. |
| `PILOT_ACCESS.md` | DEFER | Legacy pilot access funnel through Hub/Pilot Access Engine. | README legacy link; security contact overlap. | High business/process ambiguity. | Migrate to Passpod Pilot workflow-fit evaluation if still valid. | Confirm pilot intake and contact policy. |
| `LAUNCH_READINESS.md` | ARCHIVE WITH LEGACY TASK | Historical v0.1.0 launch checklist for TASK Core. | No current README link found; historical audit references. | Medium public confusion if treated as current launch state. | Archive with SPEC/launch family. | Link/reference audit. |
| `ROADMAP.md` | ARCHIVE WITH LEGACY TASK | TASK Core roadmap for receipt gallery, OpenAPI/schema consistency, freeze/revoke examples. | Public root file; historical references. | Medium because it contradicts current architecture direction. | Archive intact or replace later with Passpod v0.1 roadmap. | Strategy approval for any replacement roadmap. |
| `FUNDING_USE.md` | DEFER | Funding narrative for TASK Core, receipt gallery, OpenAPI checks, and public OSS maintenance. | Historical public file; no runtime dependency. | Medium because funding claims are strategy-sensitive. | Rewrite only with funding/public-positioning approval. | Funding strategy decision. |
| `CHANGELOG.md` | MIGRATE | Minimal historical v0.1.0 entry. | No runtime dependency. | Low, but missing reset/archive history. | Migrate changelog in a dedicated release-history pass. | Version/release authority decision. |
| `VERSIONING.md` | MIGRATE | Old receipt-core version ladder. | Historical docs; version search surface. | High semantic conflict with independent Standard/Profile/SDK versions. | Replace with Passpod v0.1 versioning policy after authority is defined. | Version governance decision. |
| `GOVERNANCE.md` | MIGRATE | Minimal stewardship note for TASK Core and Pilot Access. | Gate requires file presence; public governance surface. | Medium because authority terms are obsolete. | Update terminology and authority scope; do not archive without replacement. | Stewardship approval. |
| `CONTRIBUTING.md` | MIGRATE | Contribution boundary; still mentions sanitized receipt examples and scoped-key internals. | Gate requires file presence. | Low to medium. | Retain safety principle; update examples and terminology to v0.1. | Decide contribution categories. |
| `SECURITY.md` | KEEP - Supporting | Minimal security reporting contact. | Gate requires file presence. | Medium unresolved contact question. | Keep; later confirm whether `pilots@passpod.io` remains the security contact. | Security contact decision. |
| `LICENSE` | KEEP - Supporting | MIT license with DIDX copyright. | Gate requires file presence; archived OpenAPI license metadata references repository license. | High if changed without legal approval. | Keep unchanged unless legal authority approves. | Legal approval. |
| `CODE_OF_CONDUCT.md` | KEEP - Supporting | Minimal community conduct note. | Gate requires file presence. | Low. | Keep or expand later. | None. |

## 5. Governance and Security Documents

| Path | Classification | Governance/security finding | Recommended action |
|---|---|---|---|
| `GOVERNANCE.md` | MIGRATE | Still says Passpod TASK Core is stewarded by DIDX and pilots are scoped Pilot Access. Governance likely still needed, but subject and scope are obsolete. | Terminology and authority migration, not archive-first. |
| `SECURITY.md` | KEEP - Supporting | Provides a private-reporting instruction and contact. Contact may conflate security and pilot intake. | Keep until a dedicated security contact decision exists. |
| `CONTRIBUTING.md` | MIGRATE | Useful private-data boundary, but contribution examples are receipt-era. | Update to canonical schemas, fixtures, validator, SDK, CLI, and docs. |
| `LICENSE` | KEEP - Supporting | Legal support asset. DIDX copyright is a legal/stewardship question, not a technical migration target. | Keep unchanged. |
| `CODE_OF_CONDUCT.md` | KEEP - Supporting | Generic, not tied to legacy architecture. | Keep. |
| `.github/CODEOWNERS` | KEEP - Supporting | Ownership points to `@edidx`. | Keep unless repository ownership changes. |
| `.github/PULL_REQUEST_TEMPLATE.md` | KEEP - Supporting | Current checklist is aligned to Passpod v0.1 and transport neutrality. | Keep. |

Open governance questions:

- Who has final authority over Standard, Protocol, Profile, SDK, and Pilot changes?
- Does DIDX remain the public legal/stewardship label?
- Should `pilots@passpod.io` remain the security contact, or should security reporting be separated from pilot intake?
- Who approves profile proposals and compatibility claims?

## 6. Version and Release Documents

| Asset | Classification | Version finding | Conflict or gap | Recommended action |
|---|---|---|---|---|
| `CHANGELOG.md` | MIGRATE | Only contains `v0.1.0` "Initial public draft structure." | Missing Passpod Specification v0.1 freeze, SDK/CLI, schema, gate, CI, and archive history. | Dedicated changelog migration. |
| `VERSIONING.md` | MIGRATE | Defines `v0.1.x`, `v0.2.x`, and `v1.0.0` around public draft/schema refinement/stable receipt core. | Conflicts with architecture where Standard, Protocol, Profile, SDK, schemas, and implementations may version independently. | Replace after version authority is decided. |
| `LAUNCH_READINESS.md` | ARCHIVE WITH LEGACY TASK | Describes v0.1.0 TASK Core launch checklist. | Refers to receipt schema, OpenAPI, public demo receipts, Hub, scoped keys, and signed pilot receipts. | Archive with legacy launch material. |
| `ROADMAP.md` | ARCHIVE WITH LEGACY TASK | Defines old receipt/TASK roadmap. | Does not reflect Passpod Standard, Protocol, SDK, Profiles, Conformance, or Pilot direction. | Archive or replace in a later roadmap pass. |
| Git tags `v0.1.0`, `v0.1.1` | DEFER | Tags exist but local docs do not explain how they map to the frozen Passpod Specification v0.1. | Release authority and tag semantics are unresolved. | Decide release taxonomy before editing tags or release docs. |

## 7. Package Metadata Inventory

| Surface | Finding | Classification | Action |
|---|---|---|---|
| `package.json` | Not present. | Not applicable | Do not create without a package strategy. |
| `package-lock.json` | Not present. | Not applicable | Do not create. |
| npm bin entries | None found. | Not applicable | No npm CLI surface exists. |
| npm scripts | None found. | Not applicable | No npm script consumer exists. |
| JavaScript dependencies | None found. | Not applicable | No JavaScript dependency surface exists. |
| `pyproject.toml`, `setup.py`, `setup.cfg` | Not present. | Not applicable | Python publication remains deferred. |
| `requirements.txt` | `jsonschema[format]>=4,<5`. | KEEP - Supporting | Required by validator and CI/test environment. |
| Makefile/tox/nox | Not present. | Not applicable | No release automation surface found. |

Conclusion: there is no active package metadata to migrate in this pass. The package-surface decision should remain deferred until the repository decides whether it is a specification repository with a reference SDK, a Python package, or a multi-language monorepo.

## 8. Python Package Surface

| Asset | Classification | Current purpose | Dependencies | Risk | Proposed action |
|---|---|---|---|---|---|
| `passpod/__init__.py` | KEEP - Canonical | Package-root exports for `Message`, `Handshake`, `Profile`, and `PasspodValidationError`. | Tests and CLI. | Low. | Keep. |
| `passpod/message.py` | KEEP - Canonical | Message value object backed by canonical validator. | `validator.semantic_validator`. | Low. | Keep. |
| `passpod/handshake.py` | KEEP - Canonical | Handshake value object and append/read helpers. | `Message`, canonical validator. | Low. | Keep. |
| `passpod/profile.py` | KEEP - Canonical | Profile value object. | Canonical validator. | Low. | Keep. |
| `passpod/cli.py` | KEEP - Canonical | Local `validate` and `inspect` CLI through `python3 -m passpod.cli`. | SDK classes and tests. | Medium if documentation still points to legacy CLI README. | Keep; update docs later. |
| `passpod/errors.py` | KEEP - Canonical | SDK validation error boundary. | SDK and CLI. | Low. | Keep. |
| `validator/semantic_validator.py` | KEEP - Canonical | Canonical schema and semantic validator. | `jsonschema`, canonical schemas. | Low. | Keep. |
| `requirements.txt` | KEEP - Supporting | Declares `jsonschema[format]>=4,<5`. | CI, tests, semantic validator, legacy receipt validator. | Medium if removed before dependency strategy exists. | Keep. |

The Python SDK is repository-local only. No publication metadata was found, and no version metadata is present in `passpod/`.

## 9. JavaScript Validator and CLI Surface

No tracked JavaScript validator, JavaScript CLI, TypeScript source, npm package metadata, npm scripts, npm lockfile, or JavaScript tests were found.

| Surface | Finding | Classification |
|---|---|---|
| JavaScript validator | Not present. | Not applicable |
| JavaScript CLI | Not present. | Not applicable |
| `src/` | Local empty untracked directory; no files. | Not a tracked asset |
| `packages/validator/` | Local empty untracked directory; no files. | Not a tracked asset |
| `package.json` | Not present. | Not applicable |

No asset qualifies as `RETAIN AS ALTERNATIVE IMPLEMENTATION` today because no non-Python implementation exists in tracked files.

## 10. Tooling Inventory

| Tool | Classification | Inputs | Outputs | Semantics | Consumers | Risk | Proposed action |
|---|---|---|---|---|---|---|---|
| `tools/check-public-task-repo.sh` | KEEP - Canonical | Canonical docs, schemas, fixtures, SDK/CLI imports, safety patterns. | Pass/fail gate. | Passpod v0.1 repository gate. | CI and PR template. | Low; contains legacy terms only as containment list. | Keep. |
| `tools/validate-receipts.py` | MIGRATE | Archived receipt schema and archived receipt examples. | Receipt validation messages. | Legacy TASK receipt validation plus useful public-safety checks. | Legacy docs; not CI. | Medium: useful checks but legacy semantics. | Extract reusable safety scanning later, then archive original tool. |
| `tools/pilot-readiness.py` | DEFER | Arbitrary receipt JSON path; usage points to archived remote-worker receipt. | Readiness score and Pilot Access messaging. | Legacy receipt production-readiness scoring. | None found in CI/tests. | Medium: business/pilot semantics unresolved. | Defer until Passpod Pilot assessment model is defined. |

## 11. Dependency and Reference Map

| Asset or family | Inbound references | Runtime consumers | Test/CI consumers | Public link risk | Dependency conclusion |
|---|---|---|---|---|---|
| `SPEC.md` | README legacy link; historical audit/migration docs. | None. | None. | Medium because root name looks authoritative. | Safe to archive with README link update. |
| `LAUNCH_READINESS.md` | Historical docs and local root visibility. | None. | None. | Medium. | Safe to archive as historical launch material. |
| `ROADMAP.md` | Historical docs and local root visibility. | None. | None. | Medium. | Safe to archive or replace later after strategy decision. |
| `ADOPTION.md` | Historical docs; root visibility. | None. | None. | Medium. | Migrate or archive after adoption model is approved. |
| `PILOT_ACCESS.md` | README legacy link; historical docs. | None. | None. | High because pilot/commercial expectations are external-facing. | Defer pending Pilot policy. |
| `COMMERCIAL_BOUNDARY.md` | README legacy link; historical docs. | None. | None. | High. | Defer pending commercial boundary decision. |
| `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `LICENSE`, `CODE_OF_CONDUCT.md` | README support links; gate required files. | None. | Gate checks file presence. | Medium for governance/security only. | Keep/migrate carefully, not archive-first. |
| `requirements.txt` | Quickstart, CI, legacy docs, validator import failure text. | Validator/tests. | CI installs. | Low. | Keep. |
| `cli/README.md` | Historical docs; root directory. | None. | None. | Medium because it contradicts active CLI existence. | Migrate or archive with legacy tool docs. |
| `validator/README.md` | README legacy link; historical docs. | None. | None. | Medium. | Archive or rewrite after legacy receipt validator treatment. |
| `tools/validate-receipts.py` | Legacy docs and archive README. | Manual only. | None. | Low to medium. | Migrate useful scanning, then archive. |
| `tools/pilot-readiness.py` | Archive README; usage only. | Manual only. | None. | Medium. | Defer. |

## 12. Legacy Terminology Findings

Active contamination found:

- `SPEC.md`: TASK Core, Sensitive Action Control, Trust Action Receipt, receipt decisions, Hub, Control Packs, Pilot Access Engine.
- `LAUNCH_READINESS.md`: public demo receipts, Hub, scoped keys, TASK Core, signed pilot receipts.
- `ROADMAP.md`: TASK Core, receipt gallery, freeze/revoke examples, OpenAPI/schema drift.
- `ADOPTION.md`: TASK Core, Trust Action Receipt, Hub, Pilot Access Engine.
- `COMMERCIAL_BOUNDARY.md`: TASK Core -> Hub -> Control Packs -> Pilot Access stack.
- `PILOT_ACCESS.md`: TASK Core, Trust Action Receipt, Hub, Pilot Access Engine.
- `FUNDING_USE.md`: TASK Core, receipts, OpenAPI references, allow/deny/freeze/revoke.
- `VERSIONING.md`: stable receipt core.
- `cli/README.md`: says no standalone CLI exists and points to legacy receipt validator.
- `validator/README.md`: legacy receipt validator, Hub, Pilot Access Engine.
- `docs/glossary.md`, `docs/receipt-lifecycle.md`, `docs/production-checklist.md`, `docs/public-vs-pilot.md`, `docs/security-model.md`, `docs/standardization-roadmap.md`: legacy receipt/TASK/Pilot material.

Historical context:

- `README.md` legacy section.
- `docs/TERMINOLOGY.md` archived terminology section.
- `archive/legacy-task/`.
- Audit and migration reports.

Legitimate generic use:

- `allow` as ordinary English in README.
- `receipt` inside explicit legacy/archive contexts.
- `evidence`, `version`, and `profile` in canonical docs and schemas.

## 13. Versioning Conflicts

Conflicts and gaps:

- `VERSIONING.md` defines a receipt-core ladder but does not govern Standard, Protocol, Message Model, Profile, SDK, CLI, schema, or conformance versioning.
- `CHANGELOG.md` does not mention the frozen Passpod Specification v0.1 or subsequent implementation/archive milestones.
- Git tags `v0.1.0` and `v0.1.1` exist, but local docs do not define whether they map to repository releases, specification versions, package versions, or legacy receipt releases.
- Canonical schemas intentionally do not prescribe version syntax.
- Profiles intentionally evolve independently and do not prescribe version syntax.
- The Python SDK has no package/distribution version metadata.
- Archived OpenAPI has `0.1.0-draft`, which is a legacy API version and should not be reused as the Passpod core version.

Missing authority:

- Release authority for specification versions.
- Version authority for SDK/CLI.
- Profile version governance.
- Compatibility policy for schema evolution.
- Changelog scope and tag policy.

## 14. Governance Questions

Unresolved questions:

- Should the repository remain under DIDX stewardship language, and how should that be expressed for Passpod v0.1?
- Who approves normative Standard and Protocol changes?
- Who approves Profile lifecycle transitions?
- Who owns SDK and CLI releases?
- Is Passpod Pilot a governance process, a commercial process, or both?
- Should security reports go to `pilots@passpod.io` or a dedicated security contact?
- What compatibility promises are made for schemas, fixtures, SDK, and CLI?
- Are legacy root documents public history, or should root only expose active documents plus archive links?

This audit does not invent answers.

## 15. Recommended Repository Model

Recommended near-term model:

```text
combined specification and reference Python SDK repository
```

Rationale:

- The canonical docs, schemas, fixtures, validator, SDK, CLI, tests, gate, and CI already live together.
- There is no active package publication surface.
- There is no alternative language implementation.
- The active quickstart is local-repository based, not package-install based.
- The repository still benefits from keeping implementation tests near the frozen specification while v0.1 semantics stabilize.

Conceptual future structure:

- Normative specifications: `docs/STANDARD.md`, `docs/PROTOCOL.md`, state/message/profile/conformance/terminology docs.
- Developer documentation: `README.md`, `docs/QUICKSTART.md`, future SDK/CLI docs.
- Active Python implementation: `passpod/`, `validator/semantic_validator.py`, `tests/`.
- Optional future alternative implementations: separate explicitly named implementation directories only after conformance criteria exist.
- Package metadata: defer until publication strategy exists.
- Release/version documents: migrate after version authority is assigned.
- Tools: keep canonical gate; archive or migrate receipt-era utilities separately.
- Historical archive: `archive/legacy-task/` plus future legacy document families.

## 16. Classification by Asset

Counts below group closely related directories/families where audited as one surface.

| Classification | Count | Assets |
|---|---:|---|
| KEEP - Canonical | 11 | `README.md`, `docs/QUICKSTART.md`, normative docs family, canonical schemas, `examples/valid/`, `examples/invalid/`, `validator/semantic_validator.py`, `passpod/`, `tests/`, `tools/check-public-task-repo.sh`, `.github/workflows/validate.yml` |
| KEEP - Supporting | 9 | `LICENSE`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `requirements.txt`, `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `docs/SPECIFICATION_FREEZE_REPORT.md`, `docs/CANONICAL_REPOSITORY_MIGRATION_MAP.md`, `docs/OPENAPI_TRANSPORT_MATERIAL_DECISION.md` |
| MIGRATE | 13 | `CHANGELOG.md`, `VERSIONING.md`, `GOVERNANCE.md`, `ADOPTION.md`, `CONTRIBUTING.md`, `cli/README.md`, `validator/README.md`, `tools/validate-receipts.py`, `docs/glossary.md`, `docs/non-goals.md`, `docs/public-vs-pilot.md`, `docs/security-model.md`, `docs/threat-model.md` |
| ARCHIVE WITH LEGACY TASK | 7 | `SPEC.md`, `LAUNCH_READINESS.md`, `ROADMAP.md`, `examples/README.md`, `docs/receipt-lifecycle.md`, `docs/production-checklist.md`, archived receipt/OpenAPI/worker family already under `archive/legacy-task/` |
| RETAIN AS ALTERNATIVE IMPLEMENTATION | 0 | None found |
| DEFER | 4 | `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, `FUNDING_USE.md`, `tools/pilot-readiness.py` |
| DELETE-CANDIDATE | 0 | None |

## 17. Recommended Migration Sequence

1. Archive legacy SPEC and launch-readiness document family.

   Scope: move `SPEC.md`, `LAUNCH_READINESS.md`, `ROADMAP.md`, and tightly coupled receipt/TASK lifecycle/checklist docs into `archive/legacy-task/` while updating only direct links.

   Stop/go checks: tests pass, gate passes, README links resolve, no canonical docs change, no root `SPEC.md` ambiguity remains.

2. Migrate governance, security, and contribution documents to Passpod v0.1.

   Scope: update `GOVERNANCE.md`, `CONTRIBUTING.md`, and security contact wording after authority decisions.

   Stop/go checks: gate passes, legacy terms appear only in archive/migration contexts, governance questions are answered by maintainers.

3. Decide Passpod Pilot and commercial boundary language.

   Scope: migrate or archive `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, relevant public/pilot docs, and `tools/pilot-readiness.py`.

   Stop/go checks: no Pilot Access Engine claims remain active; pilot contact and commercial claims are approved.

4. Migrate release and version documents.

   Scope: replace `VERSIONING.md` and update `CHANGELOG.md` around specification, schema, SDK, CLI, profile, and repository release tracks.

   Stop/go checks: version authority is documented; no universal version number is invented without support.

5. Archive or migrate legacy receipt validator documentation and utility.

   Scope: extract any reusable public-safety scanning from `tools/validate-receipts.py`, then archive the receipt-specific validator and docs.

   Stop/go checks: canonical gate still covers private-data leakage; canonical tests and CI remain green.

6. Decide package/publication surface.

   Scope: determine whether to add Python packaging metadata or keep repository-local usage.

   Stop/go checks: package strategy is approved; no npm surface is introduced without an implementation.

## 18. Explicit Non-actions

This pass did not:

- modify existing files;
- move or rename files;
- archive or delete files;
- update package metadata;
- rewrite governance;
- create packaging;
- create scripts;
- change tests;
- change CI;
- change the gate;
- change canonical code;
- commit;
- push.

## 19. Final Recommendation

The immediate package-surface audit does not support a JavaScript archival pass because no tracked JavaScript implementation or npm package surface exists.

The next highest-value, dependency-safe cleanup is to remove ambiguity around the old root `SPEC.md` and related TASK launch documents by archiving them as historical legacy material.

Recommended next bounded pass:

```text
Archive legacy SPEC and launch-readiness document family
```

Do not begin that pass from this report.
