# AI Agent Action Agreement

## 1. Document status

| Field | Value |
|---|---|
| Status | INVESTIGATE |
| Normative status | Non-normative |
| Record owner | DIDX / Passpod founder |
| Last decision date | 2026-07-28 |
| Source verification date | 2026-07-28 |
| Next review date | 2026-08-11 |

This opportunity hypothesis is not part of Passpod Standard v0.1, creates no
product commitment, and does not alter or reinterpret the frozen architecture.

Gate progress:

| Gate condition | Progress |
|---|---:|
| Relevant practitioner conversations | 0/5 |
| Organizations represented | 0/3 |
| Distinct role types represented | 0/3 |
| Confirmed real workflows | 0/3 |
| Material dissatisfaction signals | 0/2 |
| Interviewed buyer or budget owner with confirmed budget path | 0/1 |
| Organization willing to review a pilot design | 0/1 |
| Pre-agreed pilot metric, baseline, and threshold | 0/1 |
| Demonstrated differentiation against actual incumbent workflow | 0/1 |

### Public-repository data boundary

Record only sanitized, non-confidential evidence. Prohibited content includes
customer or prospect names, contact details, confidential workflows, private
interview material, credentials, security-sensitive architecture, unsanitized
evidence, and information under confidentiality obligations. Store private
material elsewhere and include only sanitized summaries here.

Labels are **verified external evidence**, **internal hypothesis**, and
**customer-validation assumption**.

## 2. Executive hypothesis

**Internal hypothesis:** An agent export of a bounded sensitive dataset to a
named recipient should require structured agreement, with conditions and
closure evidence remaining reconstructable.

Proposed mapping to the existing frozen protocol:

- **PROPOSE:** The initiator declares the dataset, recipient, purpose, and export.
- **CHALLENGE:** The authority requests constraints, evidence, or approval.
- **AGREE:** The parties accept bounded export conditions.
- **CLOSE:** The workflow records execution, rejection, expiry, or cancellation.

This proposed application of `PROPOSE -> CHALLENGE -> AGREE -> CLOSE` changes no
protocol meaning, message type, or lifecycle state.

## 3. Target workflow

This investigation covers one workflow only:

> An enterprise AI agent requests export of a bounded sensitive dataset to a
> named recipient for a declared purpose, subject to action-specific
> constraints and approval before execution.

Customer-record modification, payment instructions, access grants, and
production-configuration changes are out of scope and do not influence this
record.

## 4. Target buyers and stakeholders

Responsibilities and roles remain **customer-validation assumptions**:

| Responsibility | Candidate role |
|---|---|
| Operational owner | Product or data owner |
| Decision authority | Data owner, privacy authority, or delegated approver |
| Technical evaluator | IAM or authorization architect |
| Security or compliance reviewer | AI governance lead; secondarily application security lead |
| Economic or budget owner | Unconfirmed; CISO is one hypothesis |

First interview priority:

1. Enterprise AI platform lead.
2. IAM or authorization architect.
3. AI governance lead.

Interview target tracker:

| Target ID | Organization type | Priority role | Outreach status | Interview status | Evidence-log reference | Next action |
|---|---|---|---|---|---|---|
| T-01 | Enterprise deploying AI agents | Enterprise AI platform lead | Not started | Not scheduled | — | Identify a sanitized candidate |
| T-02 | Enterprise deploying AI agents | IAM or authorization architect | Not started | Not scheduled | — | Identify a sanitized candidate |
| T-03 | Enterprise deploying AI agents | AI governance lead | Not started | Not scheduled | — | Identify a sanitized candidate |

## 5. Current alternatives

The workflow may already be covered by IAM, authorization, policy, data-loss
prevention, approvals, guardrails, security, observability, SIEM, audit, and
orchestration. Map the actual incumbent workflow before claiming a gap; section
14 contains the competitive hypotheses.

## 6. Problem hypothesis

Problems to validate within the sensitive-data-export workflow are:

- overbroad privilege or unclear authority;
- recipient and purpose detached from authorization;
- export conditions lost before execution;
- outcome evidence detached from conditions;
- approvals unverifiable downstream;
- difficult reconstruction.

Frequency, severity, and incumbent-tool adequacy are unverified.

## 7. Economic consequence hypothesis

Possible consequences are data leakage, review cost, deployment delay, approval
overhead, duplicated controls, and weak accountability. Impact is unverified.

## 8. Passpod-specific role

**Internal hypothesis:** Passpod could serve as a transport-neutral agreement
and evidence layer between the export initiator and the authority responsible
for allowing, constraining, or rejecting the export.

It would complement, not replace, existing controls; differentiation must be demonstrated.

## 9. Example handshake

This sensitive-data-export example is illustrative and non-normative:

- **PROPOSE:** The agent requests a bounded export to a named recipient for a declared purpose.
- **CHALLENGE:** The authority requests recipient verification, field and count limits, retention, approval, and expiry.
- **AGREE:** The agent accepts the bounded conditions.
- **CLOSE:** Execution, failure, expiry, or rejection is linked to the conditions.

It defines no JSON, schema, field, Profile, or protocol behavior.

## 10. Pilot hypothesis

After the gate, a pilot could use one agent, export, authority, low-risk
integration, and Profile candidate without a production platform.

Any approved pilot must proceed through the existing
[Passpod Pilot process](../../PILOT_ACCESS.md). Its Profile candidate would be
an evaluation artifact, not an approved Reference Profile.

## 11. Pilot success criteria

Pre-agreed criteria must test whether:

- every export has a traceable proposal and prior constraints;
- no export proceeds without mandatory agreement;
- conditions remain linked to outcome;
- the sequence is reconstructable;
- integration effort and latency are measured;
- the evaluator confirms improvement over the incumbent.

## 12. Commercial entry offer

**Internal hypothesis:** An **AI Agent Action-Control Assessment** could provide
workflow and authority maps, failure analysis, incumbent comparison, Profile
outline, pilot architecture, criteria, and recommendation.

Scope, pricing, duration, and willingness to pay are unvalidated.

## 13. Evidence supporting investigation

These sources support investigation, not opportunity validation:

- **NIST — [AI Agent Standards
  Initiative](https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative).**
  Created 2026-02-17; updated 2026-04-20. Supports investigation of secure,
  interoperable agents, protocols, authentication, and identity. It does not
  prove demand, budget, differentiation, or adoption.
- **NIST NCCoE — draft concept paper [Accelerating the Adoption of Software and
  AI Agent Identity and
  Authorization](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf).**
  February 2026. NCCoE seeks input on a proposed effort examining how identity
  and authorization standards could apply to agents, including its scope,
  feasibility, and value. It does not prove a gap or Passpod demand.
- **OWASP GenAI Security Project — [OWASP Top 10 for Agentic Applications for
  2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).**
  Published 2025-12-09 as the 2026 edition. Neutral evidence of agentic risks,
  including tool misuse and identity or privilege abuse; it does not prove
  market demand, buyer ownership, or Passpod effectiveness.
- **Microsoft Learn — [Microsoft Entra Agent ID
  documentation](https://learn.microsoft.com/en-us/entra/agent-id/) and
  [agent-management
  roles](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-roles-perms?view=o365-worldwide).**
  Role page updated 2026-05-08; verified 2026-07-28. This vendor capability and
  positioning evidence covers identity, authorization, lifecycle, approval,
  and governance; it may disconfirm the opportunity.
- **Google Cloud — [Govern your
  agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern).**
  Updated 2026-07-23. This vendor capability and positioning evidence covers
  registry, IAM, policy, governance, gateways, oversight, and audit. It does
  not prove demand or a gap and may disconfirm differentiation.
- **European Commission — [AI
  Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai).**
  Updated 2026-07-27; entered into force 2024-08-01. The timetable is contextual
  evidence only. It does not require Passpod or this workflow or validate
  demand. Commercial urgency is an internal inference; legal applicability
  requires qualified advice.

## 14. Competitive boundary

The following are **internal competitive hypotheses requiring practitioner
interviews and product evaluation**:

| Category | Evidenced incumbent capability | Potential coordination gap | Validation required |
|---|---|---|---|
| IAM and authorization | Identity, entitlements, contextual access decisions | Export intent and conditions may sit outside the decision | Compare fine-grained and transaction authorization |
| Policy engines | Enforced rules and decision reasons | Clarification and acceptance may not persist with outcome | Inspect inputs, outputs, evidence, retention |
| Agent security | Discovery, identity protection, tool controls, containment | Agreement evidence may not be portable | Evaluate deployed control planes |
| Guardrails | Model, data, output, and tool-use constraints | Authority acceptance may be separate | Test action-gate evidence |
| Observability | Traces, tool calls, metrics, context | Traces may not establish accepted conditions | Inspect semantics and integrity |
| Workflow automation | State, approvals, integrations, retries | Agreement meaning may vary | Compare native records |
| Human approval | Review, escalation, recorded decisions | Conditions may not be enforceable downstream | Test execution enforcement |
| Audit, SIEM, and compliance | Correlation, retention, investigation, reporting | Intent through outcome may not form one sequence | Reconstruct from current records |

## 15. Critical assumptions

- Agreement evidence is distinct from access decisions and logs.
- The export problem is frequent and fundable.
- Incumbents do not solve it adequately.
- Integration remains lightweight.
- Buyers accept a protocol layer.
- A pilot demonstrates measurable advantage.

## 16. Disconfirming evidence

Archive or demote if incumbents suffice, no budget exists, exports are rare,
integration cost exceeds value, no organization will review a pilot, or
Passpod adds latency without measurable improvement.

## 17. Interview questions

Ask about recent behavior before explaining the proposed solution:

1. When did an AI agent last initiate or prepare a sensitive-data export?
2. Which systems initiated and executed or rejected it?
3. Who had authority to decide that specific export?
4. Walk through the decision path, identity, permissions, and controls used.
5. Which recipient, purpose, field, count, retention, approval, or expiry constraints applied?
6. What evidence linked the request, authority, decision, and outcome?
7. Where was each condition recorded after the decision?
8. When did an export last fail, wait, require rework, or impede review?
9. How much manual effort and elapsed time did that decision require?
10. Which tools enforced, reviewed, observed, or retained export evidence?
11. Did information move between tools during that workflow? If so, how?
12. Who was accountable for the workflow's operational risk?
13. Who owned the budget, and which funded control category applied?
14. What event created urgency, and what control spending followed?
15. What was the most recent comparable control change tested in a low-risk
    environment, how long did integration take, and which result determined
    whether it progressed?

For a feasible test from question 15, record the baseline, metric, and pass/fail
threshold. Do not ask whether the participant would buy Passpod.

## 18. Build / no-build gate

A **relevant practitioner conversation** is with someone who operated,
approved, secured, governed, or investigated a consequential AI-agent write
action in the previous 12 months.

A **confirmed real workflow** has a recent action, named system categories,
decision authority, current control, retained evidence, and observed friction,
failure, delay, or audit difficulty.

**Material dissatisfaction** means a control failure, material manual effort,
measurable delay, duplicate implementation, review difficulty, or inability to
enforce or reconstruct action conditions.

Every condition must be satisfied before proceeding:

- at least 5 relevant conversations across at least 3 organizations and at
  least 3 role types;
- at least 3 confirmed real sensitive-data-export workflows;
- at least 2 material dissatisfaction signals;
- an interviewed buyer or budget owner confirming a budget path or funded control category;
- 1 organization willing to review a pilot design;
- one pre-agreed pilot metric, current baseline, and pass/fail threshold;
- comparison with the actual incumbent workflow;
- a specific advantage beyond logs, static authorization, or generic approvals.

No SDK feature, schema, Profile, adapter, demo, or hosted product is authorized
until every gate condition is satisfied. A completed pilot outcome is not
required to authorize a Reference Profile or demo after the gate.

## 19. Current decision

**Status: INVESTIGATE**

No engineering is authorized. Current work is limited to sanitized customer
discovery, evidence collection, incumbent mapping, and assessment-offer
preparation for the sensitive-data-export workflow.

Decision history:

| Date | Status | Decision | Reason | Next review |
|---|---|---|---|---|
| 2026-07-28 | INVESTIGATE | No engineering authorized | Opportunity and buyer remain unvalidated | 2026-08-11 |

## 20. Evidence log

Use only sanitized evidence permitted by the public-repository data boundary.

| Date | Evidence | Source | Workflow | Buyer | Signal type | Confidence | Effect on ranking | Gate criterion | Follow-up |
|---|---|---|---|---|---|---|---|---|---|
