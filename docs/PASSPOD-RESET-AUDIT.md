# Passpod Reset Audit

Audit date: 2026-07-19
Repository audited: `/Users/liping/passpod-task`
Branch observed: `main`
Remote observed: `https://github.com/edidx/passpod-task.git`
Audit mode: read-only audit plus this single new report file

Post-archival note: legacy receipt schema and receipt example paths referenced by their former active locations in this historical audit have since been moved to `archive/legacy-task/`. Those former paths remain in this report as observations of repository state at audit time, not active Passpod v0.1 requirements.

## 1. Executive summary

The current repository is implemented as a public "Passpod TASK Core" standard/test repository. It is not yet aligned with the reset architecture:

- Passpod Standard
- Passpod Handshake Protocol
- Passpod SDK
- Reference Profiles
- Passpod Pilot

No tracked product asset in the repository currently expresses the canonical handshake `PROPOSE -> CHALLENGE -> AGREE -> CLOSE`.

The active public surface still presents the legacy stack as `Passpod TASK Core -> Passpod Hub -> Control Packs -> Pilot Access -> paid pilot / Team / Enterprise`. That stack appears in `README.md`, `COMMERCIAL_BOUNDARY.md`, `SPEC.md`, `docs/glossary.md`, and the public gate script. The validation gate currently enforces old product terms, including `Passpod TASK Core`, `Passpod Hub`, `Control Packs`, `AgentTrust`, `Remote Worker Trust`, `Pilot Access Engine`, `Sensitive Action Control`, and `DIDX`.

The repository has useful reusable material: JSON Schema validation patterns, demo-fixture safety checks, documentation boundary patterns, threat-model prompts, CI structure, and public/private data leakage checks. However, the current schema, OpenAPI route shape, examples, documentation, navigation, badge, GitHub Action name, and repo identity are contaminated by archived TASK/Hub/Control Pack/Pilot Access Engine language.

No real secrets, tokens, credentials, production keys, real user data, or private pilot submissions were found in the tracked files. The only email-like operational contact found is `pilots@passpod.io`. The JSON examples use demo actors and demo subjects. The repo contains no package metadata, package exports, deployment configuration, Cloudflare config, application routes, HTML pages, or public website navigation beyond Markdown links and the OpenAPI reference.

High breakage risk: removing or archiving legacy assets before updating the gate will break CI. The current CI calls `tools/check-public-task-repo.sh`, and that script requires the old file set and old terminology.

Recommended bounded next pass: create a migration plan for the public surface and validation gate only, covering `README.md`, `SPEC.md`, `docs/glossary.md`, `PILOT_ACCESS.md`, `openapi/passpod-task.public.yaml`, `schemas/trust-action-receipt.schema.json`, `examples/`, `.github/workflows/validate.yml`, and `tools/check-public-task-repo.sh`, without changing implementation code.

## 2. Repository architecture as currently implemented

Current implementation shape:

- Public documentation layer: top-level Markdown files plus `docs/*.md`.
- Public schema layer: `schemas/trust-action-receipt.schema.json`.
- Public example fixture layer: `examples/*.receipt.json`.
- Public OpenAPI reference layer: `openapi/passpod-task.public.yaml`.
- Public validator tooling: `tools/validate-receipts.py`.
- Public repository gate: `tools/check-public-task-repo.sh`.
- Pilot scoring helper: `tools/pilot-readiness.py`.
- Placeholder documentation directories: `cli/`, `validator/`, `worker-reference/`.
- CI: `.github/workflows/validate.yml`.
- Governance metadata: `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `GOVERNANCE.md`.

No source implementation exists in tracked files under `src/`, `spec/`, or `packages/validator`; those directories are present but empty and untracked by git. No package manager metadata, SDK package, API server, Cloudflare Worker, website, HTML, navigation code, or deployment configuration exists in this repository.

Active inbound dependency shorthand used below:

- `README nav`: public Markdown links from `README.md`.
- `CI`: `.github/workflows/validate.yml`.
- `gate`: `tools/check-public-task-repo.sh`.
- `validator`: `tools/validate-receipts.py`.
- `example docs`: `examples/README.md`.
- `OpenAPI`: `openapi/passpod-task.public.yaml`.

## 3. Canonical assets

No existing tracked product file is canonical under the reset architecture. The repository contains no active Standard document, no Handshake Protocol document, no SDK package, no Reference Profile hierarchy, and no Passpod Pilot material that avoids the legacy Pilot Access Engine/Hub stack.

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `docs/PASSPOD-RESET-AUDIT.md` | CANONICAL | This audit report only. | Supports reset governance by documenting migration scope; not an active product asset. | New file requested by audit. | References audited repository paths only. | None. | Keep as reset record. | Low. | No, unless facts are disputed. |

## 4. Reusable assets

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `.github/CODEOWNERS` | REUSABLE | Assigns ownership to `@edidx`. | Generic repository governance; no product conflict, but ownership may need business confirmation. | GitHub CODEOWNERS behavior. | None. | GitHub review routing. | Keep unless owner changes. | Medium if removed, because review routing changes. | Yes for ownership. |
| `CODE_OF_CONDUCT.md` | REUSABLE | Minimal conduct statement. | Generic and not tied to legacy architecture. | None found. | None. | Public community expectations. | Keep or expand later. | Low. | No. |
| `CONTRIBUTING.md` | REUSABLE | Contribution guidance and private-data exclusion. | Useful public boundary pattern; contains scoped-key phrasing that should be checked during migration. | `gate` required file. | None. | CI gate currently requires it. | Retain pattern, adjust terms only during migration. | Medium before gate update. | Yes for public contribution policy. |
| `LICENSE` | REUSABLE | MIT license with DIDX copyright. | Legal asset, not product architecture. DIDX label needs legal/stewardship confirmation. | `OpenAPI` license name says "See repository LICENSE". | None. | Legal reuse rights; OpenAPI metadata references it. | Do not change in cleanup pass. | High if removed or altered. | Yes, legal approval required. |
| `requirements.txt` | REUSABLE | Pins `jsonschema[format]>=4,<5`. | Supports reusable validation tooling. | `CI`, `cli/README.md`, `validator/README.md`, `examples/README.md`, `validator`. | Python dependency spec. | Required for local and CI validation. | Keep until validation stack changes. | High before validator migration. | No. |
| `tools/validate-receipts.py` | REUSABLE | Validates example receipts against schema and public safety markers. | Strong reusable validation pattern; currently tied to Trust Action Receipt schema, demo signature, and old example directory. | `CI` via `gate`, `cli/README.md`, `validator/README.md`, `examples/README.md`, `gate`. | `schemas/trust-action-receipt.schema.json`, `examples/*.receipt.json`, `jsonschema`. | Required by current gate. | Retarget to canonical handshake/profile fixtures after schema migration. | High before replacement because CI depends on it. | No for mechanics; yes for new validation policy. |
| `docs/threat-model.md` | REUSABLE | Lists generic risks: forged receipts, bypassed controls, excessive evidence, confused authority, private leakage. | Useful threat prompts for Standard/Handshake/Profile work; not heavily branded. | None found. | None. | None. | Adapt into canonical Standard/SDK security notes. | Low. | Yes for security semantics. |

## 5. Assets requiring migration

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `README.md` | MIGRATE | Main public entry, badge, stack position, start-here links, public/private boundary. | Publicly presents TASK Core, Hub, Control Packs, AgentTrust, Remote Worker Trust, Pilot Access Engine, DIDX, and sensitive-action doctrine as active. No canonical handshake or SDK path. | GitHub landing page; `gate` checks many phrases. | `SPEC.md`, schema, OpenAPI, examples, validator, `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, `ROADMAP.md`, `FUNDING_USE.md`, GitHub Actions badge. | Removing or changing terms breaks `gate`. | Rewrite to Standard -> SDK -> reference profile -> validation -> workflow-fit assessment -> paid pilot path after gate update. | High. | Yes, public positioning. |
| `SPEC.md` | MIGRATE | Public v0.1 TASK Core specification. | Defines TASK decision model, Trust Action Receipt, `allow/deny/review_required/freeze/revoke`, AgentTrust, Remote Worker Trust, Hub, Control Packs, Pilot Access Engine. Conflicts with canonical handshake. | `README nav`, `gate`. | Schema, examples, Pilot Access, Hub/Control Pack stack. | Gate enforces phrases from it. | Replace with Passpod Standard and Handshake Protocol semantics. Preserve useful boundary disclaimers. | High. | Yes, standard semantics. |
| `ROADMAP.md` | MIGRATE | Public TASK Core roadmap. | Roadmap centers Trust Action Receipt, freeze/revocation, validator, OpenAPI, OSS maintenance; not reset sequence. | `README nav`. | None. | Public roadmap expectations. | Reframe to Standard, SDK, Reference Profiles, external validation, workflow-fit assessment, paid pilot. | Medium. | Yes, strategy. |
| `ADOPTION.md` | MIGRATE | Adoption reader paths. | Uses TASK Core, Sensitive Action Control, Hub, Pilot Access Engine, Passpod Protocol, Sentinel/Ops exclusions. | `gate`. | None. | Gate requires wording from it. | Rewrite reader paths for Standard, SDK adopters, validators, and pilot buyers. | High before gate update. | Yes, public funnel. |
| `COMMERCIAL_BOUNDARY.md` | MIGRATE | Public/commercial boundary. | Explicit old product stack: TASK Core -> Hub -> Control Packs -> Pilot Access -> paid pilot / Team / Enterprise. | `README nav`, `gate`. | None. | Gate requires Hub and stack wording. | Reframe around workflow-fit assessment, paid pilot, implementation/support, managed services only after demand. | High before gate update. | Yes, commercial positioning. |
| `FUNDING_USE.md` | MIGRATE | OSS funding/credits plan. | Describes TASK Core and decision states as active; contains standards crosswalk material that may be reusable. | `README nav`. | None. | Public funding narrative. | Update only with explicit funding/strategy approval. | Medium. | Yes, fundraising/public claims. |
| `GOVERNANCE.md` | MIGRATE | Stewardship note. | Says TASK Core is stewarded by DIDX and pilots handled through scoped Pilot Access. DIDX may remain legal, but active TASK/Pilot Access phrasing conflicts. | `gate`. | None. | Governance expectations. | Human-confirm legal/steward model, then update product terms. | Medium. | Yes, legal/stewardship. |
| `LAUNCH_READINESS.md` | MIGRATE | v0.1 launch checklist. | Encodes old launch success criteria: Pilot Access path, TASK Core, Sensitive Action Control, Hub exclusions, paid pilot/Team/Enterprise. | `gate`. | None. | Public/internal launch readiness. | Convert to reset readiness checklist only after public surface plan is approved. | Medium. | Yes, launch strategy. |
| `PILOT_ACCESS.md` | MIGRATE | Current pilot access page. | Has legitimate future paid-pilot material, but routes through Passpod Hub and Pilot Access Engine. | `README nav`, `gate`. | None. | Public pilot funnel; `pilots@passpod.io` checks. | Rewrite as Passpod Pilot and paid workflow-fit assessment. Do not treat all pilot content as obsolete. | High. | Yes, commercial/ops. |
| `SECURITY.md` | MIGRATE | Security contact. | Useful, but contact is `pilots@passpod.io`; may conflate security reporting with pilot funnel. | `gate` checks contact. | None. | Public security process. | Confirm whether security contact should remain pilot mailbox or become dedicated security channel. | Medium. | Yes, security ops. |
| `VERSIONING.md` | MIGRATE | Public draft version ladder. | Versioning belongs to old receipt core, not reset Standard/SDK/Profile release tracks. | `gate`. | None. | Gate requires file. | Replace with reset versioning policy after artifacts are named. | Medium. | Yes, release policy. |
| `.github/PULL_REQUEST_TEMPLATE.md` | MIGRATE | Public TASK repo checklist. | Checklist title and gate command are TASK-specific; private-data checks are reusable. | GitHub PR UI. | `tools/check-public-task-repo.sh`. | Developer workflow. | Update after gate is renamed/retargeted. | Medium. | No for mechanics; yes for policy wording. |
| `.github/workflows/validate.yml` | MIGRATE | CI validation workflow. | Workflow name is "Validate TASK public repo" and validates old examples plus old gate. | README badge references workflow path. | `requirements.txt`, schema JSON, three example JSON files, `tools/check-public-task-repo.sh`. | CI and README badge. | Retarget after schema/examples/gate migration. | High if changed first. | No for mechanics; yes for required checks. |
| `cli/README.md` | MIGRATE | States no standalone CLI, points to validator. | Useful CLI boundary, but blocks production signing via Hub/Pilot Access Engine language and does not describe SDK developer path. | `gate`, README mentions Validator not CLI directly. | `requirements.txt`, `tools/validate-receipts.py`. | Gate requires it. | Convert to SDK/CLI boundary or archive if no CLI remains. | Medium. | Yes if CLI becomes SDK surface. |
| `docs/glossary.md` | MIGRATE | Defines public vocabulary. | Central contamination file: TASK Core, Passpod Protocol as control doctrine, Hub, Control Packs, AgentTrust, Remote Worker Trust, Pilot Access Engine, DIDX. | `gate`. | None. | Gate requires terms from it. | Replace with reset glossary: Standard, Handshake Protocol, SDK, Reference Profiles, Passpod Pilot. | High before gate update. | Yes, naming authority. |
| `docs/non-goals.md` | MIGRATE | Short list of what TASK is not. | Boundary ideas are reusable, but active subject is TASK. | None found. | None. | None. | Rewrite around Passpod Standard/Protocol non-goals. | Low. | Yes for doctrine. |
| `docs/production-checklist.md` | MIGRATE | Production checklist. | Contains TASK plus freeze/revoke behavior. Useful controls checklist, but old decision model is central. | `gate`. | None. | Gate requires it. | Rewrite around handshake, profile validation, pilot readiness, implementation/support. | Medium. | Yes for security/process. |
| `docs/public-vs-pilot.md` | MIGRATE | Public vs pilot distinction. | Legitimate pilot distinction, but current shape is scoped keys, hosted endpoint, signed pilot receipts, Pilot Access. | `gate`. | None. | Gate requires it. | Convert to public Standard/SDK/reference profile vs paid workflow-fit/pilot boundary. | Medium. | Yes, public/commercial boundary. |
| `docs/receipt-lifecycle.md` | MIGRATE | Receipt lifecycle. | Uses `Request -> TASK check -> decision -> Trust Action Receipt`. Conflicts with canonical handshake sequence. | None found. | None. | None. | Replace with `PROPOSE -> CHALLENGE -> AGREE -> CLOSE` lifecycle. | Low. | Yes, protocol semantics. |
| `docs/security-model.md` | MIGRATE | Security model note. | Says TASK is control-and-receipt layer and production signing through Pilot Access. | None found. | None. | None. | Rewrite around Standard/Handshake/SDK trust boundaries. | Low. | Yes, security semantics. |
| `docs/standardization-roadmap.md` | MIGRATE | Public standardization progression. | Contains useful public feedback/external compatibility shape, but old v0.1/v0.2/v1 receipt-core path is not reset strategy. | `gate`. | None. | Gate requires it. | Reframe around Standard, SDK, reference profile, external validation. | Medium. | Yes, strategy. |
| `examples/README.md` | MIGRATE | Explains public demo receipts. | Documents TASK Core, Hub, Pilot Access Engine, Remote Worker TrustPass, freeze, and agent behavior examples. | `README nav`, `gate`. | Three example JSON files, `requirements.txt`, `tools/validate-receipts.py`. | Gate and docs. | Rewrite when examples become canonical reference-profile fixtures. | High before examples/gate update. | Yes for public examples. |
| `examples/refund-review.receipt.json` | MIGRATE | Demo high-risk refund review fixture. | Potentially reusable as a reference profile example, but currently uses `AgentTrust Live Control API` and old receipt/decision model. | `CI`, `validator`, `example docs`. | Schema fields. | Required by CI JSON check and validator. | Retain until replacement fixture exists; migrate concept away from Live Control API. | High before CI update. | Yes for scenario meaning. |
| `examples/remote-worker.receipt.json` | MIGRATE | Demo remote worker reference fixture. | Could become a reference profile, but currently uses Remote Worker TrustPass naming and old receipt/decision model. | `CI`, `gate`, `validator`, `example docs`, `tools/pilot-readiness.py` usage text. | Schema fields. | Required by CI JSON check, gate, validator, pilot helper usage. | Migrate into a canonical Reference Profile if remote-work remains approved. | High before CI/gate/helper update. | Yes for profile approval. |
| `openapi/README.md` | MIGRATE | Explains public OpenAPI reference. | Useful API boundary language, but tied to TASK Core, Hub, Pilot Access Engine, receipt lookup. | `gate`. | `openapi/passpod-task.public.yaml`. | Gate requires it. | Rewrite for SDK/reference validation API only if an API remains in reset scope. | Medium. | Yes, API surface. |
| `openapi/passpod-task.public.yaml` | MIGRATE | Public reference API shape. | Defines `/v1/spec`, `/v1/receipts/validate`, `/v1/receipts/{receipt_id}` and TASK receipt schemas. No canonical handshake routes. | `README nav`, `gate`, `openapi/README.md`. | Schema URL, LICENSE, `pilots@passpod.io`. | CI only JSON-checks examples/schema, not this YAML; gate requires file exists. | Replace or archive after deciding whether reset has public API routes or SDK-only validation. | Medium to high for clients using the reference. | Yes, public API contract. |
| `schemas/trust-action-receipt.schema.json` | MIGRATE | JSON Schema for Trust Action Receipt. | Reusable schema discipline, but title and fields encode TASK receipt and central `allow/deny/review_required/freeze/revoke` model. | `README nav`, `SPEC.md`, `validator`, `CI`, `gate`, `OpenAPI`. | JSON Schema draft URL. | Required by validator and CI. | Design canonical handshake/profile schema before changing. | High. | Yes, protocol/schema. |
| `tools/check-public-task-repo.sh` | MIGRATE | Public repo gate. | Major blocker: enforces old architecture, old README links, Pilot Access Engine, Hub, Control Packs, AgentTrust, Remote Worker Trust, Sensitive Action Control, DIDX, and old required files. | `CI`, `.github/PULL_REQUEST_TEMPLATE.md`. | Many docs, schema, examples, `tools/validate-receipts.py`, dangerous-pattern grep. | CI fails if changed incompatibly. | First gate to redesign in any cleanup pass; preserve secret/private-data checks. | High. | Yes for policy assertions. |
| `tools/pilot-readiness.py` | MIGRATE | Scores a receipt for production readiness. | Could inform paid workflow-fit assessment, but currently depends on receipt fields, `policy_ref`, `proof_ref`, demo signatures, and Pilot Access email. | None except self usage text. | Arbitrary input receipt path; no writes. | No CI dependency found. | Migrate to workflow-fit assessment only if scoring remains approved. | Low to medium. | Yes, commercial/security scoring. |
| `validator/README.md` | MIGRATE | Validator documentation. | Useful local validation instructions, but tied to Trust Action Receipts, demo signatures, Hub, Pilot Access Engine. | `README nav`, `gate`. | Schema, examples, `requirements.txt`, `tools/validate-receipts.py`. | Gate requires it. | Rewrite with canonical validation target after schema/examples migration. | Medium. | No for mechanics; yes for semantics. |

## 6. Archive candidates

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `CHANGELOG.md` | ARCHIVE | Historical v0.1.0 note. | Useful as historical evidence of the TASK public draft; not a reset roadmap. | None found. | None. | Public release history. | Preserve as historical record or replace only with explicit release-history plan. | Medium if deleted because history is lost. | Yes for release history. |
| `examples/agent-freeze.receipt.json` | ARCHIVE | Demo agent emergency freeze fixture. | Tightly coupled to AgentTrust, Kill-State API, freeze action, and old execution-control model. Historically useful, but should not remain active public fixture in reset architecture. | `CI`, `validator`, `example docs`. | Schema fields. | Required by CI JSON check and validator. | Archive only after CI/gate/examples are migrated to canonical fixtures. | High before CI update. | Yes, because it is active in tests. |

## 7. Delete candidates

These are not tracked by git, but they exist in the working tree as empty directories.

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `packages/validator/` | DELETE-CANDIDATE | Empty local placeholder directory. | Could be intended SDK/validator package space, but contains no tracked files. | None found. | None. | None observed. | Do not delete during reset audit. Confirm whether it is an intentional SDK placeholder before removal. | Low in git, unknown locally. | Yes. |
| `spec/` | DELETE-CANDIDATE | Empty local placeholder directory. | Could be intended canonical spec space, but contains no tracked files. | None found. | None. | None observed. | Confirm before removal; may be useful for future Standard source. | Low in git, unknown locally. | Yes. |
| `src/` | DELETE-CANDIDATE | Empty local placeholder directory. | Could be intended implementation space, but contains no tracked files. | None found. | None. | None observed. | Confirm before removal; do not infer broader unused state from emptiness alone. | Low in git, unknown locally. | Yes. |

## 8. Deferred assets

| Exact path | Classification | Current purpose | Why it supports or conflicts | Active inbound references | Active outbound references | Dependencies | Recommended action | Deletion risk | Human review |
|---|---|---|---|---|---|---|---|---|---|
| `worker-reference/` | DEFER | Directory for future minimal public reference Worker docs. | Not part of immediate reset architecture unless converted into SDK/reference implementation material. | `gate` through README file. | `worker-reference/README.md`. | Gate requires README. | Leave untouched until Standard/SDK/reference implementation scope is decided. | Medium before gate update. | Yes. |
| `worker-reference/README.md` | DEFER | States no production Worker/issuer/Hub component exists. | Contains legacy Hub and Pilot Access Engine language; future Worker may be irrelevant to reset path. | `gate`. | None. | Gate requires it. | Defer; if kept, migrate later to SDK/reference implementation boundary. | Medium. | Yes. |

## 9. TASK Guard contamination map

Literal `TASK Guard` was not found in tracked files. However, TASK and related execution-control concepts are active throughout the repository.

Pure legacy branding:

- `README.md`: `Passpod TASK Core`, `Validate TASK public repo`, and old public stack.
- `SPEC.md`: `Passpod TASK Core Specification`, `TASK check`, `TASK decision`.
- `ROADMAP.md`, `ADOPTION.md`, `COMMERCIAL_BOUNDARY.md`, `FUNDING_USE.md`, `docs/glossary.md`, `docs/non-goals.md`, `docs/production-checklist.md`, `docs/security-model.md`, `docs/receipt-lifecycle.md`, `openapi/README.md`, `openapi/passpod-task.public.yaml`.
- `.github/workflows/validate.yml`: workflow name `Validate TASK public repo`.
- `.github/PULL_REQUEST_TEMPLATE.md`: `Public TASK repo checklist`.

Reusable validation or receipt infrastructure:

- `tools/validate-receipts.py`: reusable schema-validation and public-safety marker scanning.
- `requirements.txt`: reusable dependency.
- `schemas/trust-action-receipt.schema.json`: reusable schema practice, but schema semantics must be migrated.
- `examples/*.receipt.json`: fixture pattern reusable, current content not canonical.

Tightly coupled execution-control code or data:

- `schemas/trust-action-receipt.schema.json`: central `decision` enum includes `allow`, `deny`, `review_required`, `freeze`, `revoke`.
- `SPEC.md`: defines decision meanings around continuing, rejecting, pausing, and revoking actions.
- `examples/agent-freeze.receipt.json`: `AgentTrust Kill-State API`, `freeze_agent_execution`, `decision: freeze`.
- `examples/refund-review.receipt.json`: `AgentTrust Live Control API`.
- `docs/production-checklist.md`: `freeze/revoke behavior`.

Public-facing contamination:

- `README.md` and GitHub badge expose `passpod-task`.
- `SPEC.md`, `COMMERCIAL_BOUNDARY.md`, `PILOT_ACCESS.md`, `ADOPTION.md`, `docs/glossary.md`, `examples/README.md`, `openapi/README.md`, `openapi/passpod-task.public.yaml`, `validator/README.md`, `cli/README.md`, `worker-reference/README.md`.
- `tools/check-public-task-repo.sh` enforces contaminated terms as required.

Historical material worth preserving:

- `CHANGELOG.md`: v0.1.0 public draft record.
- `examples/agent-freeze.receipt.json`: useful record of the archived Kill-State/execution-control experiment after it is removed from active CI.

## 10. Pilot architecture contamination map

Legitimate future paid-pilot material:

- `PILOT_ACCESS.md`: contains a real funnel concept that maps to Passpod Pilot after migration.
- `LAUNCH_READINESS.md`: paid pilot / Team / Enterprise evaluation path can inform future pilot readiness, but old terms must be removed.
- `docs/public-vs-pilot.md`: useful public/pilot boundary pattern.
- `tools/pilot-readiness.py`: potential seed for paid workflow-fit assessment, but not safe as-is.
- `README.md` and `COMMERCIAL_BOUNDARY.md`: current funnel language includes paid pilot and support concepts.

Obsolete Pilot Access Engine infrastructure:

- No implementation of scoped key generation or Pilot Access Engine was found.
- `README.md`, `SPEC.md`, `COMMERCIAL_BOUNDARY.md`, `PILOT_ACCESS.md`, `ADOPTION.md`, `docs/glossary.md`, `openapi/README.md`, `validator/README.md`, `cli/README.md`, `worker-reference/README.md`, and `tools/check-public-task-repo.sh` contain active Pilot Access Engine messaging.

Private operational records:

- None found in tracked files.
- No pilot submissions, private records, customer workflows, or production scoped keys were found.

Public funnel content:

- `README.md`: "Request Pilot Access: pilots@passpod.io".
- `PILOT_ACCESS.md`: pilot access upgrade path.
- `SECURITY.md`: same pilot mailbox used for security concerns.
- `openapi/passpod-task.public.yaml`: contact is `Passpod Pilot Access`.
- `tools/pilot-readiness.py`: prints next step to request Pilot Access.

Generic reusable intake or workflow code:

- `tools/pilot-readiness.py`: reads arbitrary receipt JSON and produces a readiness score. It does not store data and has no CI dependency, but scoring criteria are legacy and should be redesigned before reuse.

## 11. Public-surface contamination map

Public surfaces found:

- GitHub repository identity: remote `edidx/passpod-task`, branch `main`.
- README badge: links to `https://github.com/edidx/passpod-task/actions/workflows/validate.yml`.
- Public docs: all top-level Markdown and `docs/*.md`.
- Public examples: `examples/*.receipt.json`.
- Public schema URL: `https://passpod.io/schemas/trust-action-receipt.schema.json`.
- Public OpenAPI placeholder server: `https://api.passpod.example`.
- Contact email: `pilots@passpod.io`.

No HTML pages, website routing files, app navigation files, CTAs in code, Cloudflare deployment files, package metadata, or API portal implementation were found in this repository.

Contaminating terms found on public surfaces:

- `Passpod TASK Core`
- `TASK check`
- `TASK decision`
- `Sensitive Action Control`
- `No receipt, no sensitive action`
- `Passpod Hub`
- `Control Packs`
- `AgentTrust`
- `Remote Worker Trust`
- `Remote Worker TrustPass`
- `Pilot Access Engine`
- `Live Control API`
- `Kill-State API`
- `allow`, `deny`, `freeze`, `revoke` as central decision model
- `DIDX`

Terms not found as active literals:

- `TASK Guard`
- `TASK modules`
- `Passpod Standard` as a named active architecture
- `PROPOSE`
- `CHALLENGE`
- `AGREE`
- `CLOSE`
- `Passpod SDK`
- `Reference Profiles`

## 12. Dependency and breakage risks

Tests and CI:

- `bash tools/check-public-task-repo.sh` passes today, but it validates the old TASK public repo model.
- `.github/workflows/validate.yml` installs `requirements.txt`, JSON-parses the schema and three example receipts, then runs `tools/check-public-task-repo.sh`.
- Removing or renaming `README.md`, `SPEC.md`, `PILOT_ACCESS.md`, `ADOPTION.md`, `SECURITY.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `VERSIONING.md`, `COMMERCIAL_BOUNDARY.md`, `requirements.txt`, schema, `examples/remote-worker.receipt.json`, `examples/README.md`, OpenAPI, `openapi/README.md`, `validator/README.md`, `cli/README.md`, `worker-reference/README.md`, selected `docs/*.md`, or `tools/validate-receipts.py` will break the current gate.
- Removing or changing old required phrases in `README.md`, `SPEC.md`, `ADOPTION.md`, `COMMERCIAL_BOUNDARY.md`, `docs/glossary.md`, `PILOT_ACCESS.md`, `LAUNCH_READINESS.md`, `cli/README.md`, `worker-reference/README.md`, or `openapi/README.md` will break the current gate until the gate is migrated.

Imports and runtime:

- `tools/validate-receipts.py` imports `json`, `pathlib`, and `jsonschema`.
- `tools/pilot-readiness.py` imports `json`, `sys`, and `pathlib`.
- No application imports, SDK package exports, package manager scripts, or API server routes were found.

Routes and API shapes:

- OpenAPI defines `/v1/spec`, `/v1/receipts/validate`, and `/v1/receipts/{receipt_id}`.
- No implemented HTTP routes were found.
- If external docs or clients use this OpenAPI file, migration could break expectations even though this repo has no runtime route implementation.

Links and navigation:

- README links to `SPEC.md`, schema, OpenAPI, examples README, validator README, `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, `ROADMAP.md`, and `FUNDING_USE.md`.
- OpenAPI metadata references `LICENSE`.
- Several READMEs instruct `python3 -m pip install -r requirements.txt` and `python3 tools/validate-receipts.py`.

Deployment:

- No Cloudflare, Wrangler, Pages, Vercel, Netlify, Docker, GitLab CI, package deployment, or public website deployment files were found.
- Cloudflare deployment breakage risk in this repo is currently none observed.

Package exports:

- No `package.json`, lockfile, SDK package, package exports, npm config, or Python package metadata were found.

Local development commands:

- `python3 tools/validate-receipts.py` passes.
- `bash tools/check-public-task-repo.sh` passes.
- These commands are tied to old terminology and fixtures.

## 13. Sensitive/private data findings

Data categories observed:

- Demo receipt fixtures: `examples/*.receipt.json` contain demo actors, demo subjects, static demo timestamps, and `demo-signature-not-production`.
- Contact email: `pilots@passpod.io` appears in public docs, OpenAPI contact, and tooling output.
- Ownership/legal labels: `@edidx` in CODEOWNERS and DIDX in governance/license/docs.
- No real user information found.
- No pilot submissions found.
- No secrets, tokens, credentials, passwords, production keys, or private key blocks found.
- No private operational records found.
- No generated artifacts found except ordinary source/documentation files.
- No `.env`, `.dev.vars`, Wrangler state, deployment secrets, or package lock secrets found in this repo.

Remediation requirements:

- Keep the dangerous-pattern checks from `tools/check-public-task-repo.sh` or an equivalent reset gate.
- Treat `pilots@passpod.io`, `@edidx`, and DIDX labels as public operational/legal labels requiring owner confirmation before changing.
- Do not add real pilot data or workflow-fit assessment records to this public repo.

## 14. Recommended cleanup order

1. Update the validation gate design first, because the current gate enforces old architecture terms and old required files.
2. Migrate the public entry and core doctrine together: `README.md`, `SPEC.md`, `docs/glossary.md`, and `COMMERCIAL_BOUNDARY.md`.
3. Migrate the schema and example fixtures together so CI always has a coherent validation target.
4. Migrate OpenAPI only after deciding whether the reset architecture exposes public API routes or relies on SDK/reference validation.
5. Migrate pilot funnel language separately from obsolete Pilot Access Engine language; keep legitimate paid-pilot concepts.
6. Re-run CI/local checks after each bounded group; do not archive or delete active fixtures until replacements are wired into the gate.

## 15. Proposed bounded next pass

Exactly one bounded next pass is recommended:

Draft a public-surface and gate migration plan for the reset architecture, limited to `README.md`, `SPEC.md`, `docs/glossary.md`, `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, `schemas/trust-action-receipt.schema.json`, `examples/`, `openapi/passpod-task.public.yaml`, `.github/workflows/validate.yml`, and `tools/check-public-task-repo.sh`. The pass should produce a proposed mapping and test plan only; it should not rewrite files until the mapping is approved.

## 16. Files that must not be touched without explicit approval

Do not touch these without explicit approval:

- `README.md`
- `SPEC.md`
- `COMMERCIAL_BOUNDARY.md`
- `PILOT_ACCESS.md`
- `ADOPTION.md`
- `ROADMAP.md`
- `FUNDING_USE.md`
- `GOVERNANCE.md`
- `SECURITY.md`
- `LICENSE`
- `schemas/trust-action-receipt.schema.json`
- `openapi/passpod-task.public.yaml`
- `examples/agent-freeze.receipt.json`
- `examples/refund-review.receipt.json`
- `examples/remote-worker.receipt.json`
- `.github/workflows/validate.yml`
- `.github/CODEOWNERS`
- `tools/check-public-task-repo.sh`
- `tools/validate-receipts.py`
- `tools/pilot-readiness.py`

Reason: these files carry public positioning, legal/stewardship labels, active validation behavior, CI behavior, active example fixtures, or pilot/security funnel language.

## Checks and searches performed

Commands and checks performed:

- `git status --short`
- `git rev-parse --show-toplevel` during repo discovery
- `git ls-files`
- `git branch --show-current`
- `git remote -v`
- `rg --hidden --files -g '!*.pyc' -g '!__pycache__' -g '!.git'`
- `find . -maxdepth 3 -type d -not -path './.git*'`
- `find . -type d -empty -not -path './.git*'`
- `find . -maxdepth 3 -type f` for package, deployment, HTML, script, and config files
- `file` over non-git files
- `wc -l` over non-git files
- Full content reads of top-level Markdown, `docs/*.md`, `.github/*`, schema JSON, example JSON, OpenAPI YAML, validator docs, CLI docs, worker reference docs, and tools
- Targeted `rg` searches for TASK, TASK Guard, TASK modules, Pilot Access Engine, Control Packs, AgentTrust, Passpod Hub, TASK Core, Live Control API, Kill-State, Sensitive Action Control, allow, deny, freeze, revoke, Pilot Access, pilot, Remote Worker, PassPal, DIDX, console, API portal, Passpod Protocol, Passpod Standard, Handshake, SDK, Reference Profiles, Passpod Pilot, TrustPass, Trust Action Receipt, and No receipt
- Targeted `rg` searches for links, route paths, operation IDs, CI `uses`/`run`, Python commands, schema/example/OpenAPI/validator references, deployment terms, package terms, and imports
- Targeted `rg` searches for sensitive/private data markers: secret assignments, private keys, live keys, AWS key pattern, token, credential, password, customer, email, pilot submissions, real customer, scoped key, `.dev.vars`, Wrangler, and Cloudflare
- `python3 tools/validate-receipts.py`
- `bash tools/check-public-task-repo.sh`

Observed validation output:

- `python3 tools/validate-receipts.py`: passed for all three demo receipts.
- `bash tools/check-public-task-repo.sh`: passed and printed `Public TASK repo gate passed`; this is a pass of the old TASK gate, not evidence of reset alignment.

## Uncertainties

- Whether the GitHub repository name `edidx/passpod-task` will be renamed, archived, or kept as a historical public repo is a strategic decision not inferable from local files.
- Whether DIDX remains the legal/stewardship label under the reset architecture needs human/legal confirmation.
- Whether `pilots@passpod.io` should remain the pilot and security contact needs operational confirmation.
- Whether `Remote Worker` should become a canonical Reference Profile or be archived is not inferable from this repo alone.
- Whether external clients use `openapi/passpod-task.public.yaml` is not inferable from local imports.
- Empty local directories `packages/validator/`, `spec/`, and `src/` are not tracked by git; their intended purpose is unknown.
