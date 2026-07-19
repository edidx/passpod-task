# OpenAPI Transport Material Decision

Post-archival note: the OpenAPI and worker-reference assets evaluated in this decision have since been moved to `archive/legacy-task/openapi/` and `archive/legacy-task/worker-reference/`. Original paths retained below describe the audited pre-archival locations and are not active Passpod v0.1 paths.

## 1. Executive Summary

This audit reviewed the remaining OpenAPI, worker-reference, API documentation, and transport-oriented material after the Passpod v0.1 specification, schemas, fixtures, validator, SDK, CLI, README, quickstart, gate, CI, and legacy receipt archive were completed.

Baseline was clean:

```text
git status --short
```

returned no output, and:

```text
git log -9 --oneline
```

showed `b776a7d Archive legacy receipt schema and examples` as the latest commit.

Finding: the current OpenAPI and worker-reference family is not canonical Passpod v0.1. It is a legacy TASK/receipt/Hub-oriented public reference shape. It has no active runtime, SDK, CLI, test, CI, package-script, or validator dependency. The only current public inbound link is the README legacy OpenAPI link, and historical audit/migration documents reference it as legacy material.

Decision: classify `openapi/passpod-task.public.yaml`, `openapi/README.md`, and `worker-reference/README.md` as `ARCHIVE WITH LEGACY TASK`.

Recommended next bounded pass: Archive legacy OpenAPI and worker-reference family.

## 2. Audit Scope

Audited files and locations:

- `openapi/passpod-task.public.yaml`
- `openapi/README.md`
- `worker-reference/README.md`
- README legacy references
- SPEC legacy transport references
- API-oriented references in `docs/`, `examples/`, `tools/`, `validator/`, `cli/`, `.github/`, tests, schemas, SDK code, and package metadata

Search coverage included:

- `openapi/`
- `passpod-task.public.yaml`
- `worker-reference/`
- `HTTP`
- `REST`
- `endpoint`
- `webhook`
- `server`
- `sandbox`
- `issue`
- `verify`
- `revoke`
- `receipt`
- `Hub`
- `Pilot Access Engine`
- `API key`
- `scoped key`

Package metadata found:

- `requirements.txt`

No `package.json`, `pyproject.toml`, `setup.py`, `setup.cfg`, Makefile, tox config, nox config, API-client package, generated API docs, or API-specific package script was found.

## 3. Passpod Transport-Neutral Boundary

Passpod v0.1 is transport-neutral. The canonical architecture is:

- Passpod Standard
- Passpod Handshake Protocol
- State Model
- Message Model
- Profiles
- Conformance
- SDK
- Pilot

The canonical protocol flow is:

```text
PROPOSE -> CHALLENGE -> AGREE -> CLOSE
```

HTTP, REST, OpenAPI, webhooks, queues, wallets, files, and other transports are not the core protocol. A future OpenAPI document may describe an optional HTTP binding or service implementation, but it must not become the source of Passpod semantics.

Current source-of-truth evidence:

- `docs/STANDARD.md` says the Standard does not define HTTP routes, APIs, webhooks, or transports.
- `docs/PROTOCOL.md` says the protocol does not depend on HTTP, queues, email, files, ledgers, databases, blockchains, wallets, browsers, or any other transport.
- `docs/QUICKSTART.md` lists HTTP API as unsupported behavior.
- `.github/PULL_REQUEST_TEMPLATE.md` requires preserving transport neutrality.

## 4. OpenAPI Inventory

| Asset | Finding |
|---|---|
| Path | `openapi/passpod-task.public.yaml` |
| OpenAPI version | `3.1.0` |
| Title | `Passpod TASK Public Reference API` |
| API version | `0.1.0-draft` |
| Server URL | `https://api.passpod.example` |
| Tags | `Spec`, `Receipts` |
| Paths | `GET /v1/spec`, `POST /v1/receipts/validate`, `GET /v1/receipts/{receipt_id}` |
| Operation IDs | `getTaskSpec`, `validateTrustActionReceipt`, `getReceiptById` |
| Request models | `TrustActionReceipt` for receipt validation |
| Response models | `PublicSpec`, `ReceiptValidationResult`, `ReceiptLookupResult`, `ErrorResponse` |
| Security schemes | None found |
| External schema references | No external `$ref`; example value references `https://passpod.io/schemas/trust-action-receipt.schema.json` |
| Internal `$ref` usage | Component schemas reference each other within the same OpenAPI document |
| Receipt-era operations | Spec metadata points to receipt schema; receipt validation; receipt lookup |
| Hub assumptions | Description excludes Passpod Hub internals but frames production validity through legacy Hub/Pilot concepts |
| Pilot Access Engine assumptions | No literal `Pilot Access Engine` in YAML, but `Pilot Access` appears in contact and hosted-verification text |
| Generated-code consumers | None found |
| Documentation consumers | README legacy link, `openapi/README.md`, reset audit, migration map, archive README |
| Runtime consumers | None found |
| Test consumers | None found |
| CI consumers | None found |
| Package-script consumers | None found |

OpenAPI character:

| Question | Determination |
|---|---|
| Does it describe the core protocol correctly? | No. It does not model `PROPOSE`, `CHALLENGE`, `AGREE`, or `CLOSE`. |
| Does it describe a legacy hosted TASK service? | Mostly yes. It is a public TASK receipt validation and lookup reference. |
| Is it a potentially reusable optional HTTP binding? | Only at the concept level: metadata, validation, and lookup could inform later work. |
| Is it a mixture? | Yes. It contains reusable API-boundary patterns, but the concrete semantics are legacy receipt-primary semantics. |

## 5. OpenAPI Semantic Comparison

| Operation | Current semantics | Passpod v0.1 mapping | Classification |
|---|---|---|---|
| `GET /v1/spec` | Returns public TASK draft metadata and a receipt schema URL. | Does not map to a canonical message. Could inspire future non-semantic metadata discovery only. | Potentially adaptable later, but currently legacy. |
| `POST /v1/receipts/validate` | Validates a Trust Action Receipt against receipt-era schema and public demo safety rules. | Does not create or submit `PROPOSE`, return `CHALLENGE`, record `AGREE`, record `CLOSE`, or validate a canonical handshake. | Reusable validation concept; incompatible legacy operation as written. |
| `GET /v1/receipts/{receipt_id}` | Defines receipt lookup response shape and hosted-verification boundary. | Could loosely resemble artifact inspection in a future service, but current object is receipt lookup, not handshake inspection. | Potentially adaptable later; currently legacy. |

Legacy concepts present:

- Trust Action Receipt as primary object
- receipt validation
- receipt lookup
- `allow`, `deny`, `review_required`, `freeze`, `revoke` decision enum
- production issuance boundary
- hosted verification boundary
- Pilot Access contact and assumptions
- Passpod Hub exclusions
- legacy public schema URL

Legacy operations not present as explicit OpenAPI paths:

- issue receipt
- verify receipt
- revoke receipt
- scoped pilot key creation
- hosted Hub workflow execution

The absence of explicit issue, verify, revoke, or key routes lowers immediate runtime risk, but it does not make the OpenAPI document canonical.

## 6. Worker-Reference Inventory

| Asset | Finding |
|---|---|
| Path | `worker-reference/README.md` |
| Language/runtime | Documentation only; no code found |
| Implemented endpoints | None |
| Validation behavior | None implemented |
| Signing behavior | None implemented |
| Storage behavior | None implemented |
| Demo behavior | Describes a possible future public validation Worker around TASK Core receipts |
| Legacy schema imports | None |
| README references | No active README link found |
| Package scripts | None found |
| Tests | None found |
| CI references | None found |
| Deployment config | None found |
| Reusable transport-neutral logic | None found |
| Future optional HTTP reference value | Very low as-is because the only tracked file is receipt/HUB-oriented documentation |

The worker-reference directory is not an implementation. It is a reserved documentation placeholder for a future Worker framed around public demo receipt validation and legacy Hub/Pilot Access Engine boundaries.

## 7. API Documentation and Tooling References

| Location | Reference type | Classification |
|---|---|---|
| `README.md` | Legacy OpenAPI link in historical migration references | Explicit historical mention |
| `openapi/README.md` | Describes OpenAPI TASK receipt endpoints | Active legacy API material |
| `openapi/passpod-task.public.yaml` | OpenAPI API shape | Active legacy API material |
| `worker-reference/README.md` | Future Worker placeholder around TASK receipts | Active legacy API material |
| `SPEC.md` | Hosted lookup, receipt issuance, Hub, Pilot Access Engine wording | Historical legacy specification |
| `ADOPTION.md` | Mentions OpenAPI reference and scoped Hub access | Historical legacy public-surface material |
| `PILOT_ACCESS.md` | Hosted/scoped pilot access language | Deferred pilot/commercial material |
| `COMMERCIAL_BOUNDARY.md` | Hub/Pilot Access Engine public/private boundary | Deferred commercial material |
| `docs/public-vs-pilot.md` | Hosted endpoint and signed pilot receipt wording | Deferred pilot boundary material |
| `docs/STANDARD.md` | Says HTTP/API/webhooks/transports are non-goals | Canonical transport-neutral reference |
| `docs/PROTOCOL.md` | Says protocol is independent of transports | Canonical transport-neutral reference |
| `docs/QUICKSTART.md` | Lists HTTP API as unsupported | Canonical transport-neutral reference |
| `tools/check-public-task-repo.sh` | Canonical gate plus public/private leakage patterns | Implementation-neutral support |
| `.github/workflows/validate.yml` | Canonical tests and gate only | Implementation-neutral support |
| `.github/PULL_REQUEST_TEMPLATE.md` | Requires preserving transport neutrality | Implementation-neutral support |
| `tools/validate-receipts.py` | Legacy receipt validator, no HTTP behavior | Historical supporting utility |
| `tools/pilot-readiness.py` | Legacy receipt readiness scoring, no HTTP behavior | Deferred pilot utility |
| `tests/`, `passpod/`, `validator/semantic_validator.py` | No OpenAPI or worker-reference references found | No transport dependency |

No webhook documentation, sandbox API material, API-client helper, generated API documentation, transport-specific tests, or package scripts invoking API material were found.

## 8. Dependency Map

| Asset | Current purpose | Inbound links | Outbound refs | Runtime consumers | Test/CI consumers | Package consumers | Public URL assumptions | Migration risk | Classification | Proposed future action | Required predecessors |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `openapi/passpod-task.public.yaml` | Legacy TASK receipt API reference | README legacy link; `openapi/README.md`; audit/migration docs; archive README | Internal component `$ref`; example `receipt_schema` URL; LICENSE metadata; Pilot Access contact | None | None | None | `https://api.passpod.example`; `https://passpod.io/schemas/trust-action-receipt.schema.json` | Medium: public link and possible external readers, but no local canonical dependency | ARCHIVE WITH LEGACY TASK | Move under `archive/legacy-task/openapi/` in a later pass | Update README/archive links and verify links |
| `openapi/README.md` | Explains legacy OpenAPI reference | Audit/migration docs | `openapi/passpod-task.public.yaml` | None | None | None | None beyond referenced file | Low to medium: must move with YAML to avoid orphaned doc | ARCHIVE WITH LEGACY TASK | Move with OpenAPI YAML | Same as OpenAPI YAML |
| `worker-reference/README.md` | Reserved future Worker placeholder around TASK receipts | Audit/migration docs | None | None | None | None | None | Low: no code, no active consumer | ARCHIVE WITH LEGACY TASK | Move under legacy archive with OpenAPI family | Verify no README/CI/test link is introduced |
| `README.md` legacy OpenAPI link | Historical navigation | Public README | `openapi/passpod-task.public.yaml` | None | Link audit in gate | None | None | Medium because public README link must keep resolving | RETAIN AS HISTORICAL SUPPORTING MATERIAL | Update link only during archive pass | Archive destination must exist |
| `archive/legacy-task/README.md` legacy consumer list | Provenance of receipt-era material | None | Mentions OpenAPI as remaining legacy consumer | None | None | None | None | Low | RETAIN AS HISTORICAL SUPPORTING MATERIAL | Update list if OpenAPI moves | Archive destination must exist |
| `tools/check-public-task-repo.sh` | Canonical v0.1 public gate | CI, PR template | Canonical docs/schemas/fixtures only; no OpenAPI dependency | Local command | CI | None | None | Low for this pass | KEEP AS IMPLEMENTATION-NEUTRAL SUPPORT | Leave unchanged | None |
| `.github/workflows/validate.yml` | Canonical CI | GitHub Actions | Canonical JSON, tests, gate | CI | CI | None | None | Low | KEEP AS IMPLEMENTATION-NEUTRAL SUPPORT | Leave unchanged | None |

## 9. Stable Identifier and URL Findings

| Identifier or URL | Location | Finding | Treatment |
|---|---|---|---|
| `https://api.passpod.example` | OpenAPI server URL | Placeholder reference URL; no evidence it is live or canonical | Preserve until archival; do not reinterpret |
| `https://passpod.io/schemas/trust-action-receipt.schema.json` | OpenAPI example and archived schema `$id` | Stable legacy schema identifier; filesystem archival does not require changing it | Preserve as legacy identifier |
| `/v1/spec` | OpenAPI path | Legacy TASK metadata route | Archive with OpenAPI |
| `/v1/receipts/validate` | OpenAPI path | Legacy receipt validation route | Archive with OpenAPI |
| `/v1/receipts/{receipt_id}` | OpenAPI path | Legacy receipt lookup route | Archive with OpenAPI |
| `getTaskSpec` | OpenAPI operation ID | Legacy TASK operation ID | Archive with OpenAPI |
| `validateTrustActionReceipt` | OpenAPI operation ID | Legacy receipt operation ID | Archive with OpenAPI |
| `getReceiptById` | OpenAPI operation ID | Legacy receipt operation ID | Archive with OpenAPI |
| `pilots@passpod.io` | OpenAPI contact and legacy docs | Public pilot contact, not proof of an active API | Defer to pilot/commercial policy |

Stable URL distinction:

- Do not change schema `$id` values merely because files moved.
- Do not assume placeholder server URLs are live.
- Do not treat OpenAPI path names as Passpod protocol semantics.

## 10. Classification by Asset

| Classification | Count | Assets |
|---|---:|---|
| ARCHIVE WITH LEGACY TASK | 3 | `openapi/passpod-task.public.yaml`, `openapi/README.md`, `worker-reference/README.md` |
| RETAIN AS HISTORICAL SUPPORTING MATERIAL | 7 | `README.md` legacy OpenAPI link, `SPEC.md`, `ADOPTION.md`, `examples/README.md`, `validator/README.md`, `cli/README.md`, `archive/legacy-task/README.md` |
| MIGRATE LATER INTO OPTIONAL HTTP BINDING | 0 | None as concrete assets; only abstract concepts were reusable |
| KEEP AS IMPLEMENTATION-NEUTRAL SUPPORT | 5 | `docs/STANDARD.md`, `docs/PROTOCOL.md`, `docs/QUICKSTART.md`, `.github/workflows/validate.yml`, `tools/check-public-task-repo.sh` |
| DEFER | 4 | `PILOT_ACCESS.md`, `COMMERCIAL_BOUNDARY.md`, `docs/public-vs-pilot.md`, `tools/pilot-readiness.py` |
| DELETE-CANDIDATE | 0 | None |

Reusable transport concepts found:

- API metadata discovery could be useful later if clearly non-semantic.
- Artifact validation over HTTP could be useful later if it validates canonical messages, handshakes, profiles, or bundles.
- Artifact lookup or inspection could be useful later if scoped to canonical handshake inspection and privacy-preserving summaries.
- Public/private boundary language remains useful, but current wording is receipt/Hub/Pilot Access oriented.

None of these concepts are sufficient to retain the current OpenAPI or worker-reference files on the active developer path.

## 11. Future HTTP Binding Criteria

Before Passpod may create an official optional HTTP binding, the binding must satisfy all of the following criteria:

- It explicitly states that HTTP is optional and separate from the core protocol.
- It maps all four canonical message types: `PROPOSE`, `CHALLENGE`, `AGREE`, and `CLOSE`.
- It does not make receipts the primary protocol object.
- It does not hide hosted-service assumptions inside protocol semantics.
- It has versioning that is independent from the core Standard where appropriate.
- It defines a transport-specific conformance scope.
- It derives schemas from canonical message, handshake, and profile models.
- It includes tests proving transport behavior does not redefine protocol semantics.
- It states security and privacy boundaries clearly.
- It avoids production signing, storage, identity, cryptography, and hosted verification claims unless those are explicitly in scope for that binding.
- It does not claim that HTTP is required for Passpod conformance.
- It keeps profiles subordinate to the Standard, Protocol, State Model, Message Model, and Conformance model.

This audit does not create that binding.

## 12. Recommended Treatment

| Material family | Selected treatment | Reason |
|---|---|---|
| OpenAPI family | Archive entire family now | The YAML and README are receipt/TASK/Hub-oriented, have no canonical consumer, and are already linked as legacy. |
| Worker-reference family | Archive entire family now | It contains only a legacy receipt-oriented placeholder README, no reusable code, no runtime, and no local consumer. |
| Legacy API documentation and receipt utilities | Retain frozen or defer | These are broader cleanup subjects and should not be bundled into the OpenAPI/worker move. |
| Canonical docs, schemas, fixtures, validator, SDK, CLI, tests, CI, gate | Keep unchanged | They are transport-neutral and do not depend on OpenAPI or worker-reference material. |

The appropriate decision option is:

```text
A. Archive entire family now
```

for both the OpenAPI family and the worker-reference family.

## 13. Required Predecessor Actions

Before the next archival pass moves files:

1. Confirm the working tree is clean.
2. Move OpenAPI and worker-reference assets with `git mv`.
3. Update README legacy OpenAPI link to the archive location.
4. Update any archive README or migration-map links that would otherwise break.
5. Do not modify canonical docs, schemas, fixtures, SDK, CLI, tests, gate, or CI unless a direct moved-path link requires a minimal path update.
6. Verify relative links.
7. Run canonical tests and the Passpod v0.1 gate.
8. Confirm no API material remains on the active developer path.

No external compatibility evidence was found locally. If external users rely on the OpenAPI file, that evidence is outside this repository and must be supplied by a later human decision.

## 14. Explicit Non-actions

This pass did not:

- move OpenAPI files;
- move worker-reference files;
- rewrite OpenAPI;
- create an HTTP binding;
- create endpoints;
- create SDK transport code;
- create validators;
- create CLI code;
- modify README;
- modify SPEC;
- modify CI;
- modify the gate;
- modify canonical docs, schemas, fixtures, validator, SDK, CLI, or tests;
- commit;
- push.

## 15. Final Recommendation

The remaining OpenAPI and worker-reference material is legacy TASK transport material. It should not become canonical Passpod v0.1 and should not be used as the starting point for an HTTP binding without a separate design pass.

Recommended next bounded pass:

```text
Archive legacy OpenAPI and worker-reference family
```

Do not begin that pass from this report.
