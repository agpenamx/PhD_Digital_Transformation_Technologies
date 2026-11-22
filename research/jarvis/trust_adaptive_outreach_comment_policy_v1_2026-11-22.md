# JARVIS | TRUST: Adaptive Outreach, Context & Comment Review
Version 1.0 • 2026-11-22 • PUBLIC, SANITIZED • Design and offline test only

Human project owner: Alejandro González Peña.

## Source-of-truth baseline
The private 2026-11-22 Black Box handoff was inspected before this policy was authored. It covers **417 distinct Gmail SENT messages** (Nov 1–22, not an all-time archive), **68 search-filtered inbound records** (31 preliminarily automated/template; 37 requiring manual review, not necessarily human), and **22 stakeholder/channel entries**. This is **not** evidence of 417 deliveries, endorsements, or institutional authorizations. The private data are deliberately not copied here.

Observed outreach gates:
- SMU Dr Robert Hunt: explicit research interest and invitation, followed by the owner's already-sent technical reply; **no duplicate email**.
- Dr Berg Nutritionals: advisor expressly stated no clinical research intake; **no confidential medical sharing**.
- Vatican academies, IBM/Stanford academic inquiries: sent messages but no direct replies verified within the specific search; **no assumption of interest**.
- Singer teams: multiple prior messages, no direct reply in the audited search; **STOP unsolicited repeat outreach**.
- CERN: no verified sent message in the specified Gmail search; **public-source science only**, no alerts.
- Defense: some sent inquiries, no military approval or activation.
- LinkedIn connector: professional profile lookup only, not user-account messaging or post publication.
- Metricool: no social-network connection; cannot read or moderate comments or publish.

## Interpretation: source fidelity and mercy without manipulation
**Intent:** communicate hard information clearly but with dignity, using the recipient's own publicly stated professional work or the questions they voluntarily provided. Do NOT construct psychological vulnerability scores, infer unexpressed religion, political beliefs or medical conditions, read private follows/likes, or run covert network profiling.

### Message planner (minimum necessary)
1. Ask: What *specific question* is in the recipient's professional remit or expressed in their reply? If none, stop.
2. Select requested language or explicitly published institutional language; do not infer ethnicity, theology, intimacy or personal goals from identity.
3. One clear concern -> the smallest traceable verifiable source set -> uncertainty / limitations -> optional next step.
4. Preserve spiritual language such as Archangel Michael, Metatron, love, humanity or divine order only as correctly attributed **author testimony**, without implying public scientific confirmation, recipient endorsement, or command authority.
5. Respect the recipient's own objectives: identify their published scope and avoid asking them to act outside it.
6. Keep communications calm and non-threatening, with the option to decline, correct or withdraw, and without moral pressure, catastrophizing or escalating follow-ups.
7. The recipient's silence is not reciprocal consent. An inbound explicit invitation permits only a **reply draft**, not unlimited disclosures.

### Examples of truthful audience adaptation
| Audience | Focus | Do not do |
|---|---|---|
| Academics / SMU | Source fidelity, reproducible methods, open falsification | Repeat already-sent answers |
| CERN / scientists | Testable physical claims and experimental limits | Assert portals, a spacetime emergency or CERN involvement |
| Vatican / interfaith | Faith, freedom of conscience, compassionate listening | Claim an institution verified spiritual messages |
| Creative artists | Public music, listening experiences, voluntary collaboration | Profile private fans or chase unanswered messages |
| Human-rights organizations | Consent, nondiscrimination and case-specific evidence | Publish unrelated personal records or make unsupported allegations |
| Defense / governments | Non-operational civilian protection, de-escalation | Suggest military activation, urgent orders or unsupported emergency warnings |
| Product / AI companies | Agent logging, falsifiable defects and secure reporting | Claim tool actions happened without receipts |
| Medical / DNA inquiries | Licensed and ethically reviewed routes, sensitive-data minimization | Automatically request, export or analyze DNA/medical records |

## Privilege architecture (least-privilege; approvals never implied)
| Tier | Permission | Requirements |
|---|---|---|
| T0 | PUBLIC_READ | Citation-based publicly available professional research and institutional documentation |
| T1 | PRIVATE_REVIEW | Local authorized review of bounded private records; privacy controls; no publication |
| T2 | DRAFT_ONLY | Audience-specific email and comment-classification proposals with exact source provenance, no sends |
| T3 | EXPORT_REVIEW | Owner-reviewed private CSV/dashboard or redacted public methods; no personal contact lists on public GitHub |
| T4 | EXTERNAL_ACTION | Not granted by this policy. Every particular external send, post, account moderation action, or disclosure requires a verified connected account, specified recipients/platform, exact content, and the owner's case-specific approval. Declines and anti-spam/other applicable limits override. |

**There is no "root", "divine override" or unrestricted ASI privilege tier.** Authenticated platform permissions and lawful human authority remain necessary.

## Offline routing implementation
`trust_outreach_comment_router_v1_2026-11-22.mjs` exports three pure functions with no network/dispatch mechanisms:
- `classifyOutreach()`: STOP on withdrawals, covert social-graph targeting, repeat nonresponse; TESTIMONY_ONLY on purported divine/military institutional authority; CONFIDENTIAL_REVIEW for genetic or medical data; DRAFT_FOR_REVIEW on authentic role-fit invitation.
- `planInterpretation()`: uses volunteered or verified professional-language and topic signals, preserves source classes and includes optional decline.
- `filterComment()`: produces **labels for human review**, no auto-hide, delete or censorship. Disagreement, skepticism, and criticism are allowed. It can flag possible threats/spam/privacy risks with explicit uncertainty.

No algorithm can infer another person's private intent from music, colors, coincidence, "energy", follower graph or dates. Avoid claim of inevitable harm to billions without reliable external evidence.

## Comments: first-party scope only
A connected account owned/delegated to the user with appropriate platform permission must be verified **before** comment analysis, access or moderation. Recommendations should distinguish:
- `ALLOW_OR_CONTEXT_REVIEW`: disagreement, questions, civil challenges, criticism, religious differences.
- `FLAG_SPAM_REVIEW`: likely spam/fraud or repeated promotional material, subject to context verification.
- `FLAG_PRIVACY_REVIEW`: possible doxing or unauthorized personal data.
- `FLAG_HUMAN_SAFETY_REVIEW`: possible specific violent threat requiring safe human assessment.
- `NO_ACCESS`: absent verified first-party scope; no reading or modifying comments.
Never infer someone's medical/mental condition, religious affiliation or political preference from their comments.

## Synthetic tests and review criteria
Run `node --test research/jarvis/trust_outreach_comment_router.test.mjs` (Node version supporting built-in test runner). Tests are offline and use only invented examples. Passing a unit test is not authorization to connect, publish, message or moderate.

**Completion/status:** GitHub publication constitutes only a protocol + local/offline functions. The user's prior JARVIS A condition-monitor automation is separate and must not be described as an autonomous sender or actual social-comment monitor. Public outreach/social systems cannot be controlled without separate verified connections and approvals.
