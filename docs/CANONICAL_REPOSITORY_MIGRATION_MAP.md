# Canonical Repository Migration Map

Post-archival note: receipt-era schema, receipt example, OpenAPI, worker-reference, legacy specification, launch-readiness, and roadmap paths quoted in this migration map describe repository state and dependencies observed when the map was written. The legacy receipt, transport, and document families now live under `archive/legacy-task/`; any former active paths retained below are historical dependency evidence, not active Passpod v0.1 requirements.

## 1. Executive Summary

This audit reviewed every tracked repository asset after the Passpod v0.1 reset.

Baseline commands were clean:

```text
git status --short
```

returned no output, and:

```text
git log -5 --oneline
```

showed:

```text
35699ea Migrate README and quickstart to Passpod v0.1
3118802 Add minimal Passpod validate and inspect CLI
96d15ee Refine SDK ergonomics and fixture round trips
d42ce39 Freeze Passpod v0.1 specification and add SDK core
fc8e2aa Document OSS funding use and roadmap (#15)
```

The active Passpod v0.1 architecture is now present and usable:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

Canonical documents, schemas, valid and invalid fixtures, the semantic validator, SDK, CLI, README, and quickstart are in place. The main cleanup risk is that the repository still contains tracked TASK-era documentation, receipt schemas, receipt examples, OpenAPI material, and a public gate that requires legacy terminology and legacy links. Cleanup must therefore start by migrating the gate and CI expectations before archiving or moving old files.

Classification counts across the 74 tracked assets audited:

| Classification | Count |
|---|---:|
| KEEP - Canonical | 33 |
| KEEP - Supporting | 7 |
| MIGRATE | 25 |
| ARCHIVE | 7 |
| DELETE-CANDIDATE | 0 |
| DEFER | 2 |

No cleanup, deletion, rename, move, archive, code change, documentation rewrite, commit, or push was performed in this pass. This document is the only created file.

## 2. Audit Scope

The audit covered all tracked files from `git ls-files`, including:

- root-level public, governance, launch, adoption, roadmap, versioning, and security files;
- `.github` ownership, pull request, and workflow files;
- all files under `docs/`;
- all schema files under `schemas/`;
- all examples under `examples/`;
- all SDK, validator, CLI, and tool code;
- all tests;
- OpenAPI and worker-reference material.

The audit used the current canonical documents and implementation as source of truth. Older README, SPEC, OpenAPI, receipt examples, receipt schema, receipt validator behavior, and historical docs were treated as tracked evidence, not as canonical architecture.

The active architecture does not center TASK, execution control, Trust Action Receipts, Passpod Hub, AgentTrust, Control Packs, Pilot Access Engine, Kill-State, receipt decision states, or receipt issuance.

## 3. Canonical Baseline

Canonical active assets:

- `README.md`
- `docs/STANDARD.md`
- `docs/PROTOCOL.md`
- `docs/STATE-MODEL.md`
- `docs/MESSAGE-MODEL.md`
- `docs/PROFILES.md`
- `docs/CONFORMANCE.md`
- `docs/TERMINOLOGY.md`
- `docs/QUICKSTART.md`
- `schemas/message.schema.json`
- `schemas/handshake.schema.json`
- `schemas/profile.schema.json`
- `examples/valid/*.json`
- `examples/invalid/*.json`
- `validator/semantic_validator.py`
- `passpod/*.py`
- `tests/test_semantic_validator.py`
- `tests/test_sdk_core.py`
- `tests/test_sdk_fixture_roundtrip.py`
- `tests/test_cli.py`

Supporting canonical evidence:

- `docs/SPECIFICATION_FREEZE_REPORT.md`

Important active boundaries:

- Passpod is transport-neutral.
- A handshake is append-only.
- Accepted messages are immutable.
- `CLOSE` ends active negotiation.
- Profiles specialize Passpod without redefining the core protocol.
- The SDK and CLI consume the validator and schemas; they do not redefine the Standard.

## 4. Classification Criteria

| Classification | Meaning used in this audit |
|---|---|
| KEEP - Canonical | The asset is part of active Passpod v0.1 and should remain substantially as-is. |
| KEEP - Supporting | The asset remains useful as governance, legal, dependency, audit, or other supplementary material but is not normative architecture. |
| MIGRATE | The asset contains reusable material but still reflects legacy architecture, terminology, structure, or behavior. |
| ARCHIVE | The asset should remain accessible for history or migration context but should not remain in the active developer path. |
| DELETE-CANDIDATE | The tracked asset appears redundant, obsolete, generated, contaminated beyond useful migration value, or superseded. No tracked asset met this bar with enough dependency evidence. |
| DEFER | Treatment depends on a later product, governance, packaging, release, legal, public-surface, or transport-binding decision. |

For MIGRATE, ARCHIVE, and DEFER assets, dependencies were checked through content inspection, path-reference search, imports, tests, CI workflow configuration, README links, and tool consumers.

## 5. Root-Level Asset Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `README.md` | KEEP - Canonical | Active public entry point for Passpod v0.1 with legacy wording explicitly quarantined. | Links to canonical docs and legacy references required by current gate. | Keep active; remove legacy migration block only after gate migration. |
| `SPEC.md` | ARCHIVE | Legacy TASK Core specification centered on Trust Action Receipt and decision states. | Linked by README legacy section; required by `tools/check-public-task-repo.sh`. | Move conceptually to `archive/legacy-task/` after gate no longer requires it. |
| `ADOPTION.md` | MIGRATE | Reader paths are useful, but active wording is TASK Core, Sensitive Action Control, Hub, and Pilot Access Engine. | Required by current gate for legacy phrases. | Rewrite later for Standard, SDK, validator, and Passpod Pilot audiences. |
| `CHANGELOG.md` | KEEP - Supporting | Minimal release history. Does not define active architecture. | No inbound runtime or gate dependency found. | Keep; expand later with Passpod v0.1 release notes if release policy is defined. |
| `CODE_OF_CONDUCT.md` | KEEP - Supporting | Generic community policy. | No active code dependency. | Keep. |
| `COMMERCIAL_BOUNDARY.md` | MIGRATE | Boundary concept is useful, but product stack is TASK Core, Hub, Control Packs, Pilot Access. | README legacy links; current gate requires exact legacy distinctions. | Rewrite after gate migration for Passpod Pilot and commercial boundary. |
| `CONTRIBUTING.md` | MIGRATE | Public safety guidance is useful, but contribution categories still mention receipt examples and scoped-key internals. | Required file in current gate. | Retain safety policy; update terminology after gate migration. |
| `FUNDING_USE.md` | MIGRATE | Funding narrative still centers TASK Core, receipt gallery, and decision states. | README links were removed from active map but file remains public. | Rewrite only with public-funding strategy approval. |
| `GOVERNANCE.md` | MIGRATE | Governance is needed, but current text says TASK Core is stewarded by DIDX. | Required file in current gate. | Confirm stewardship language, then migrate to Passpod v0.1. |
| `LAUNCH_READINESS.md` | MIGRATE | Launch checklist encodes old public TASK and Pilot Access assumptions. | Current gate searches this file for legacy product terms. | Convert into Passpod v0.1 readiness checklist after gate migration. |
| `LICENSE` | KEEP - Supporting | MIT license and copyright notice. | OpenAPI license metadata references repository license. | Keep; legal changes require explicit approval. |
| `PILOT_ACCESS.md` | MIGRATE | Pilot funnel concept is relevant but uses Hub and Pilot Access Engine. | README legacy link; current gate checks `pilots@passpod.io`. | Rewrite as Passpod Pilot workflow-fit evaluation after gate migration. |
| `ROADMAP.md` | MIGRATE | Roadmap is old receipt/TASK roadmap. | Public file, not test-consumed. | Replace with Passpod v0.1 roadmap only after strategy approval. |
| `SECURITY.md` | KEEP - Supporting | Minimal security contact. | Current gate checks `pilots@passpod.io` here. | Keep; later confirm whether security contact should remain this mailbox. |
| `VERSIONING.md` | MIGRATE | Version ladder is for stable receipt core, not Standard/Protocol/Profile/SDK versioning. | Required file in current gate. | Rewrite after version policy is defined. |
| `requirements.txt` | KEEP - Supporting | Declares `jsonschema[format]>=4,<5`, used by validator and tests. | CI installs it; validator imports `jsonschema`. | Keep until validation dependency strategy changes. |

## 6. Documentation Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `docs/STANDARD.md` | KEEP - Canonical | Normative semantic authority. | Linked by README; source for architecture. | Keep. |
| `docs/PROTOCOL.md` | KEEP - Canonical | Defines canonical transport-neutral handshake flow. | Linked by README; source for validator/SDK semantics. | Keep. |
| `docs/STATE-MODEL.md` | KEEP - Canonical | Defines conceptual message and handshake lifecycle. | Linked by README; reflected by schemas and SDK lifecycle helpers. | Keep. |
| `docs/MESSAGE-MODEL.md` | KEEP - Canonical | Defines conceptual message structure. | Linked by README; represented by message schema and SDK. | Keep. |
| `docs/PROFILES.md` | KEEP - Canonical | Defines profile model and profile boundaries. | Linked by README; represented by profile schema. | Keep. |
| `docs/CONFORMANCE.md` | KEEP - Canonical | Defines conformance philosophy and layer alignment. | Linked by README. | Keep. |
| `docs/TERMINOLOGY.md` | KEEP - Canonical | Normatively defines active terms and labels legacy terms as archived. | Linked by README; source for terminology migration. | Keep. |
| `docs/QUICKSTART.md` | KEEP - Canonical | Active developer quickstart. | Linked by README; commands match current CLI/tests. | Keep. |
| `docs/SPECIFICATION_FREEZE_REPORT.md` | KEEP - Supporting | Historical audit supporting the frozen v0.1 specification. | Linked by README; no runtime consumers. | Keep in docs for now; optional future move to release audit archive. |
| `docs/PASSPOD-RESET-AUDIT.md` | ARCHIVE | Pre-freeze reset audit, now superseded by canonical docs and this map. | Self-references old state; no runtime consumers. | Move conceptually to `docs/archive/` or `archive/legacy-task/` after archive policy exists. |
| `docs/glossary.md` | MIGRATE | Legacy glossary presents TASK Core, Hub, AgentTrust, Control Packs, and Pilot Access Engine as active. | Required by current gate. | Replace with or redirect to `docs/TERMINOLOGY.md` after gate migration. |
| `docs/non-goals.md` | MIGRATE | Useful boundary shape but active subject is TASK. | No direct consumers found. | Migrate useful boundary ideas into canonical non-goals if needed. |
| `docs/production-checklist.md` | MIGRATE | Checklist centers TASK, signatures, storage, verification, freeze, and revoke. | Required by current gate. | Rewrite for implementation readiness only after gate migration. |
| `docs/public-vs-pilot.md` | MIGRATE | Useful public/pilot distinction, but old scoped keys and hosted endpoint framing. | Required by current gate. | Rewrite for public Standard/SDK versus Passpod Pilot. |
| `docs/receipt-lifecycle.md` | ARCHIVE | Legacy lifecycle conflicts with active handshake lifecycle. | No direct consumers found. | Archive as receipt-era documentation after gate and docs cleanup. |
| `docs/security-model.md` | MIGRATE | Security boundary is useful, but old TASK receipt/signing model is active. | No direct consumers found. | Rewrite around handshake, evidence, profiles, and implementation boundaries. |
| `docs/standardization-roadmap.md` | MIGRATE | Public feedback and compatibility idea is useful, but roadmap is receipt-core oriented. | Required by current gate. | Rewrite after roadmap decision. |
| `docs/threat-model.md` | MIGRATE | Threat topics are reusable, but receipt/control framing should be updated. | No direct consumers found. | Migrate into active security/threat model later. |

## 7. Schema Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `schemas/message.schema.json` | KEEP - Canonical | Canonical machine-readable message model. | Loaded by `validator/semantic_validator.py`; covered by tests. | Keep. |
| `schemas/handshake.schema.json` | KEEP - Canonical | Canonical machine-readable handshake model. | Loaded by validator; references message schema; covered by tests. | Keep. |
| `schemas/profile.schema.json` | KEEP - Canonical | Canonical machine-readable profile model. | Loaded by validator; covered by tests. | Keep. |
| `schemas/trust-action-receipt.schema.json` | ARCHIVE | Legacy receipt/TASK schema with decision enum `allow`, `deny`, `review_required`, `freeze`, `revoke`. | README legacy link, SPEC, OpenAPI, `tools/validate-receipts.py`, CI, current gate, validator README. | Do not delete. Archive only after gate, CI, legacy examples, and receipt validator are migrated or retired. |

Schema dependency notes:

- The canonical validator uses the three Passpod v0.1 schemas.
- The legacy receipt validator uses only `schemas/trust-action-receipt.schema.json`.
- The current CI workflow JSON-checks only the legacy receipt schema and three legacy receipt examples before running the legacy gate.
- No `$ref` dependency from canonical schemas points to the legacy receipt schema.

## 8. Examples and Fixtures Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `examples/valid/complete-handshake.json` | KEEP - Canonical | Valid complete `PROPOSE -> CHALLENGE -> AGREE -> CLOSE` fixture. | Validator, SDK round-trip tests, CLI tests. | Keep. |
| `examples/valid/minimal-profile.json` | KEEP - Canonical | Valid minimal profile fixture. | Validator, SDK, CLI tests. | Keep. |
| `examples/valid/minimal-propose.json` | KEEP - Canonical | Valid standalone message fixture. | Validator, SDK, CLI tests. | Keep. |
| `examples/valid/propose-challenge-agree.json` | KEEP - Canonical | Valid partial handshake fixture. | Validator and SDK round-trip tests. | Keep. |
| `examples/valid/propose-challenge.json` | KEEP - Canonical | Valid challenge-stage handshake fixture. | Validator and SDK round-trip tests. | Keep. |
| `examples/invalid/close-before-agree.json` | KEEP - Canonical | Invalid canonical fixture for terminal closure before agreement. | Validator, SDK round-trip, CLI tests. | Keep. |
| `examples/invalid/duplicate-message-id.json` | KEEP - Canonical | Invalid canonical fixture for duplicate message identity. | Validator, SDK round-trip, CLI tests. | Keep. |
| `examples/invalid/invalid-transition.json` | KEEP - Canonical | Invalid canonical fixture for bad message transition. | Validator, SDK round-trip, CLI tests. | Keep. |
| `examples/invalid/missing-parent.json` | KEEP - Canonical | Invalid canonical fixture for missing parent reference. | Validator, SDK round-trip, CLI tests; quickstart uses it. | Keep. |
| `examples/invalid/redefine-message-type.json` | KEEP - Canonical | Invalid canonical fixture for profile redefinition. | Validator, SDK round-trip, CLI tests. | Keep. |
| `examples/README.md` | MIGRATE | Walkthrough for legacy receipt examples. | README legacy link; current gate; legacy validator docs. | Rewrite after legacy receipt examples are archived or reframed. |
| `examples/remote-worker.receipt.json` | MIGRATE | Legacy receipt scenario that may inform a future profile candidate. | CI JSON check, legacy validator, examples README, current gate, pilot-readiness usage. | Preserve until replacement exists; do not promote as active profile without profile governance. |
| `examples/refund-review.receipt.json` | MIGRATE | Legacy receipt scenario that may inform future workflow examples. | CI JSON check, legacy validator, examples README. | Preserve until replacement exists; migrate scenario only if useful. |
| `examples/agent-freeze.receipt.json` | ARCHIVE | Legacy AgentTrust/Kill-State receipt example; tightly coupled to execution freeze. | CI JSON check, legacy validator, examples README. | Archive after CI/gate no longer require it. |

## 9. Validator, SDK, and CLI Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `validator/semantic_validator.py` | KEEP - Canonical | Active structural and semantic validator for message, handshake, and profile artifacts. | Imports `jsonschema`; reads canonical schemas; used by SDK and tests. | Keep. |
| `passpod/__init__.py` | KEEP - Canonical | Public package-root imports. | Used by tests and CLI. | Keep. |
| `passpod/errors.py` | KEEP - Canonical | SDK validation exception boundary. | Used by SDK classes and CLI. | Keep. |
| `passpod/message.py` | KEEP - Canonical | Message value object. | Uses canonical validator; covered by tests. | Keep. |
| `passpod/handshake.py` | KEEP - Canonical | Handshake value object and read-only conveniences. | Uses Message and canonical validator; covered by tests. | Keep. |
| `passpod/profile.py` | KEEP - Canonical | Profile value object. | Uses canonical validator; covered by tests. | Keep. |
| `passpod/cli.py` | KEEP - Canonical | Active local `validate` and `inspect` CLI. | Uses package-root SDK imports; covered by subprocess tests. | Keep. |
| `validator/README.md` | MIGRATE | Documents legacy receipt validator, not active semantic validator. | README legacy link; current gate; links to `tools/validate-receipts.py`. | Rewrite to document `validator/semantic_validator.py` after gate migration. |
| `cli/README.md` | MIGRATE | Says no standalone CLI exists, contradicting active `python3 -m passpod.cli`. | README legacy link; current gate; links to legacy receipt validator. | Rewrite or replace with pointer to `docs/QUICKSTART.md` after gate migration. |
| `tools/validate-receipts.py` | MIGRATE | Legacy receipt validator with useful public-safety checks. | Current gate, CI, examples README, validator README, cli README. | Migrate reusable safety checks into a v0.1 gate, then archive receipt-specific logic. |
| `tools/pilot-readiness.py` | DEFER | Legacy receipt readiness scoring helper. | No CI dependency; usage references `examples/remote-worker.receipt.json`. | Defer until Passpod Pilot assessment model is defined. |

Import notes:

- Active SDK modules import `validator.semantic_validator`.
- Active CLI imports package-root `Handshake`, `Message`, `Profile`, and `PasspodValidationError`.
- Legacy `tools/validate-receipts.py` imports `jsonschema` and does not participate in the active SDK/CLI path.

## 10. OpenAPI and Transport Material Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `openapi/passpod-task.public.yaml` | ARCHIVE | Legacy receipt API shape for `/v1/spec`, `/v1/receipts/validate`, and `/v1/receipts/{receipt_id}`. Passpod v0.1 core is transport-neutral. | README legacy link, openapi README, current gate. | Archive after gate migration unless a separate transport-binding pass explicitly supersedes it. |
| `openapi/README.md` | ARCHIVE | Documents legacy receipt OpenAPI reference and Hub/Pilot Access Engine boundary. | README legacy link; current gate. | Archive with OpenAPI YAML after gate migration. |
| `worker-reference/README.md` | DEFER | Reserved future Worker material tied to legacy receipt validation. | README legacy link; current gate. | Defer until transport/reference implementation scope is decided. |

Transport conclusion:

- No OpenAPI file is part of the active core protocol.
- Any future OpenAPI should be treated as a separate transport binding, not as the Standard or Handshake Protocol.
- The current OpenAPI material describes obsolete receipt endpoints and should not remain on the active developer path after the gate is migrated.

## 11. Tests, CI, and Tooling Map

| Path | Classification | Reason | Dependencies | Proposed future action |
|---|---|---|---|---|
| `tests/test_semantic_validator.py` | KEEP - Canonical | Tests canonical validator and canonical fixtures. | Imports validator by file path; reads `examples/valid` and `examples/invalid`. | Keep. |
| `tests/test_sdk_core.py` | KEEP - Canonical | Tests SDK value objects and validation boundary. | Imports package root. | Keep. |
| `tests/test_sdk_fixture_roundtrip.py` | KEEP - Canonical | Tests canonical fixtures through SDK and validator. | Reads canonical fixtures; imports SDK and validator. | Keep. |
| `tests/test_cli.py` | KEEP - Canonical | Tests active module CLI through subprocess. | Runs `python3 -m passpod.cli`; reads canonical fixtures. | Keep. |
| `.github/CODEOWNERS` | KEEP - Supporting | GitHub review ownership. | GitHub platform behavior. | Keep unless ownership changes. |
| `.github/PULL_REQUEST_TEMPLATE.md` | MIGRATE | Checklist is TASK-era but private-data checks remain useful. | Mentions `tools/check-public-task-repo.sh`. | Update after gate migration. |
| `.github/workflows/validate.yml` | MIGRATE | CI validates legacy receipt schema/examples and runs legacy public gate. | Installs `requirements.txt`, JSON-checks legacy files, runs `tools/check-public-task-repo.sh`. | Retarget after gate migration. |
| `tools/check-public-task-repo.sh` | MIGRATE | Existing gate protects some public/private boundaries but enforces obsolete TASK-era architecture. | Called by CI and PR template; reads many legacy docs and `tools/validate-receipts.py`. | First cleanup dependency to migrate. Preserve secret/private-data scanning and JSON safety checks where useful. |

Legacy gate findings:

- Useful checks to preserve: required public files, JSON validity, public/private leakage scans, secret-key marker scans, no placeholder-only README checks, and sanitized-example discipline.
- Obsolete checks: requiring TASK Core, Sensitive Action Control, Trust Action Receipt as primary object, Passpod Hub, Control Packs, AgentTrust, Pilot Access Engine, old product stack, old README launch navigation, old receipt schema, and old receipt examples.
- Cleanup blocker: archiving `SPEC.md`, legacy OpenAPI, legacy examples, legacy schema, or old README links will break this gate until it is migrated.

## 12. Legacy Terminology Reference Map

Repository-wide search before this report found these legacy/reference counts:

| Term | Hits | Files | Treatment |
|---|---:|---:|---|
| `TASK` | 101 | 26 | Active contamination except in canonical archived-terminology sections and migration docs. |
| `TASK Core` | 48 | 17 | Legacy architecture; should remain only in archive/migration context. |
| `TASK Guard` | 7 | 4 | Already archived terminology in canonical docs or reset audit context. |
| `Trust Action Receipt` | 28 | 18 | Legacy primary object; not active v0.1 protocol object. |
| `Passpod Hub` | 41 | 17 | Legacy hosted product concept; should be archived or migrated out of active path. |
| `AgentTrust` | 22 | 10 | Legacy Control Pack concept; possible scenario evidence only. |
| `Control Packs` | 20 | 8 | Legacy architecture. |
| `Pilot Access Engine` | 36 | 15 | Legacy pilot access implementation concept; superseded by Passpod Pilot framing. |
| `Sensitive Action Control` | 22 | 11 | Legacy category. |
| `Kill-State` | 8 | 4 | Legacy execution-freeze concept, primarily archive material. |
| `allow` | 27 | 13 | Mostly legacy receipt decision state; generic uses must be reviewed in context. |
| `deny` | 9 | 5 | Legacy receipt decision state. |
| `freeze` | 35 | 11 | Legacy receipt/execution-control state. |
| `revoke` | 12 | 6 | Legacy receipt decision state. |
| `receipt` | 223 | 30 | Mostly legacy receipt-era architecture and examples. |
| `issue` | 45 | 22 | Mixed generic language and legacy receipt/production boundary language. |
| `verify` | 0 | 0 | Exact word not found; `verification` appears in legacy and generic security contexts. |

Context distinctions:

- Explicitly archived historical mentions: `docs/TERMINOLOGY.md`, `docs/SPECIFICATION_FREEZE_REPORT.md`, README legacy section, and reset audit material.
- Active legacy architecture: `SPEC.md`, `ADOPTION.md`, `COMMERCIAL_BOUNDARY.md`, `PILOT_ACCESS.md`, `docs/glossary.md`, `examples/README.md`, OpenAPI material, validator README, CLI README, worker reference README, legacy receipt schema, and legacy gate.
- Legitimate generic usage: "evidence", "issue" as ordinary documentation language, "verification" in security notes, and "allow" when used outside the receipt decision enum.
- Implementation dependencies: legacy gate and CI require legacy schema/examples/docs; active SDK/CLI/tests do not.
- False positives: canonical docs use "allow" as English or "verification" as a non-prescribed trust mechanic; those are not contamination by themselves.

## 13. Dependency Risks

| Risk | Affected assets | Why it matters | Required predecessor action |
|---|---|---|---|
| Legacy gate enforces obsolete architecture | `tools/check-public-task-repo.sh`, CI, README legacy links, `SPEC.md`, old docs, old schema, old examples | Cleanup will fail CI if files or strings are moved before the gate changes. | Migrate gate first. |
| CI validates old receipt assets | `.github/workflows/validate.yml`, `schemas/trust-action-receipt.schema.json`, `examples/*.receipt.json` | Removing old examples or schema breaks workflow. | Retarget CI to canonical schemas, fixtures, tests, and v0.1 gate. |
| README retains legacy block for gate compatibility | `README.md`, `tools/check-public-task-repo.sh` | Active public README contains quarantined legacy text only because the gate requires it. | Replace gate checks, then remove legacy block in a later doc pass. |
| Legacy docs have active public-surface links | `README.md`, `SPEC.md`, OpenAPI, examples README, validator README, CLI README, commercial boundary | Archiving too early causes dead links and gate failures. | Produce link rewrite plan after gate migration. |
| Legacy receipt validator contains useful safety checks | `tools/validate-receipts.py`, `tools/check-public-task-repo.sh` | Deleting it would lose secret/private-data marker scanning until replacement exists. | Port safety checks to canonical gate before archiving. |
| Pilot wording mixes useful funnel concepts with obsolete engine language | `PILOT_ACCESS.md`, `SECURITY.md`, `tools/pilot-readiness.py`, commercial docs | Human business/security decisions are needed before rewriting. | Confirm Passpod Pilot and contact policy. |
| OpenAPI may be mistaken for active protocol | `openapi/passpod-task.public.yaml`, `openapi/README.md` | Passpod v0.1 is transport-neutral; old routes are receipt-specific. | Archive old OpenAPI or replace only in a future transport-binding pass. |

Detailed dependency map for highest-risk noncanonical assets:

| Asset | Current purpose | Inbound references | Outbound references/imports | Test/CI/tool consumers | README links | Migration risk | Recommended action | Predecessor actions |
|---|---|---|---|---|---|---|---|---|
| `tools/check-public-task-repo.sh` | Legacy public repo gate. | CI workflow, PR template. | Reads README, SPEC, legacy docs, old schema, old examples; calls `tools/validate-receipts.py`. | Direct CI consumer. | Indirectly protects legacy README links. | Very high. | Migrate to Passpod v0.1 gate. | None; this is first. |
| `.github/workflows/validate.yml` | Runs legacy JSON checks and gate. | GitHub Actions. | `requirements.txt`, old schema, old examples, gate. | CI. | README badge indirectly points at workflow path. | High. | Retarget after gate exists. | Gate migration. |
| `schemas/trust-action-receipt.schema.json` | Legacy receipt schema. | README legacy link, SPEC, OpenAPI, gate, validator. | None beyond JSON Schema draft. | CI and legacy validator. | Yes. | High. | Archive after replacement checks. | Gate and CI migration. |
| `examples/*.receipt.json` | Legacy sanitized receipt examples. | CI, legacy validator, examples README, gate. | Old schema fields. | CI and `tools/validate-receipts.py`. | README links examples README. | High. | Migrate or archive by scenario. | Gate and CI migration. |
| `SPEC.md` | Legacy TASK Core spec. | README legacy link, gate. | Old schema, examples, Pilot Access. | Gate. | Yes. | High. | Archive as legacy specification. | Gate and README link migration. |
| `openapi/passpod-task.public.yaml` | Legacy receipt API reference. | README legacy link, openapi README, gate. | Old schema URL and receipt route models. | Gate requires file exists. | Yes. | Medium-high. | Archive unless future transport binding is approved. | Gate and README link migration. |
| `tools/validate-receipts.py` | Legacy receipt validator. | Gate, examples README, validator README, cli README. | Old schema, `examples/*.receipt.json`, `jsonschema`. | Gate. | Indirect. | High. | Port safety checks, then archive. | Gate migration. |

## 14. Canonical Destination Structure

Conceptual target shape after cleanup:

```text
README.md
docs/
  STANDARD.md
  PROTOCOL.md
  STATE-MODEL.md
  MESSAGE-MODEL.md
  PROFILES.md
  CONFORMANCE.md
  TERMINOLOGY.md
  QUICKSTART.md
  SPECIFICATION_FREEZE_REPORT.md
  archive/
schemas/
  message.schema.json
  handshake.schema.json
  profile.schema.json
examples/
  valid/
  invalid/
validator/
  semantic_validator.py
passpod/
  __init__.py
  cli.py
  errors.py
  message.py
  handshake.py
  profile.py
tests/
  test_semantic_validator.py
  test_sdk_core.py
  test_sdk_fixture_roundtrip.py
  test_cli.py
tools/
  passpod-v0.1-gate.sh
archive/
  legacy-task/
    SPEC.md
    schemas/
    examples/
    openapi/
    docs/
```

Destination principles:

- Normative specification remains in `docs/`.
- Developer documentation remains in README and `docs/QUICKSTART.md`.
- Canonical fixtures remain in `examples/valid/` and `examples/invalid/`.
- Active implementations remain in `validator/`, `passpod/`, and `tests/`.
- Alternative implementations should only appear after they have a defined active purpose.
- Transport bindings should live outside the core protocol and be labeled as bindings.
- Historical legacy material should move to `archive/legacy-task/` or `docs/archive/` with links rewritten after the gate allows it.

## 15. Recommended Cleanup Sequence

1. Canonical gate migration from TASK-era checks to Passpod v0.1 checks.

   Scope: replace legacy assertions in `tools/check-public-task-repo.sh` with checks for canonical docs, canonical schemas, canonical fixtures, SDK/CLI tests, secret/private-data scanning, and archived-terminology containment.

   Stop/go gate: `python3 -m unittest discover -s tests`, migrated gate, `git diff --check`, and CI-local equivalent must pass.

2. CI workflow migration.

   Scope: update `.github/workflows/validate.yml` to run the canonical gate and canonical test suite instead of old receipt-only JSON checks.

   Stop/go gate: GitHub workflow and local commands must pass without referencing old receipt examples as active.

3. Public link migration.

   Scope: remove README legacy compatibility block, point public docs to canonical v0.1 docs, and make old links explicitly archival.

   Stop/go gate: link audit confirms no dead relative links and legacy terms appear only in archive/migration sections.

4. Legacy schema and receipt example archive plan.

   Scope: move old receipt schema, old receipt examples, old examples README, and old receipt validator documentation conceptually into archive. Do not delete until references are fully rewritten.

   Stop/go gate: canonical tests and gate pass without `schemas/trust-action-receipt.schema.json` or `examples/*.receipt.json` on the active path.

5. OpenAPI and transport decision.

   Scope: either archive old OpenAPI material or create a separate future transport-binding plan. Do not make OpenAPI part of the core protocol.

   Stop/go gate: README and docs clearly distinguish transport binding from Standard and Protocol.

6. Legacy root documentation migration.

   Scope: migrate or archive `ADOPTION.md`, `COMMERCIAL_BOUNDARY.md`, `PILOT_ACCESS.md`, `ROADMAP.md`, `VERSIONING.md`, `FUNDING_USE.md`, `LAUNCH_READINESS.md`, and governance/contribution wording.

   Stop/go gate: human review for commercial, governance, security, and roadmap claims.

7. Documentation archive consolidation.

   Scope: move reset audit, legacy glossary, legacy receipt lifecycle, legacy security and production docs into the chosen archive structure.

   Stop/go gate: active docs tree contains only canonical docs, active guidance, and clearly current support docs.

## 16. Explicit Non-actions

This pass did not:

- modify existing files;
- delete files;
- move files;
- rename files;
- archive files;
- rewrite links;
- change tests;
- change the gate;
- update CI;
- update package metadata;
- change active implementation;
- create cleanup scripts;
- create schemas;
- create examples;
- create code;
- commit;
- push.

No tracked asset is recommended as a deletion candidate until dependencies are migrated and human review confirms historical value is no longer needed.

## 17. Final Recommendation

Recommended next bounded pass:

Canonical gate migration from TASK-era checks to Passpod v0.1 checks

Do not begin cleanup, archiving, CI rewrites, link rewrites, OpenAPI changes, or legacy-file moves until that gate migration is complete and passing.
