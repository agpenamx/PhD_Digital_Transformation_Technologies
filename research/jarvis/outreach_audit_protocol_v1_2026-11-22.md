# JARVIS Outreach Audit Protocol v1.1 (Public, Privacy-Safe)
Date: 2026-11-22

## Purpose
Reproducible, consent-preserving evaluation of outreach selection, communication status, acoustic research claims, and research integrity. This public document is a methodological handoff, **not** an export of private outreach records, medical history, third-party communications, or confidential equipment/beta information.

## Claim classes
- `OBSERVED`: directly captured source content (with timestamp/URL and provenance).
- `DERIVED`: calculation with formula and input set.
- `HYPOTHESIS`: testable proposal with counterexamples and failure criteria.
- `PERSONAL_TESTIMONY`: faithful attributed narrative without inferred external cause.
- `UNKNOWN`: no reliable basis for conclusion.

## Transport-state finite-state model
`DRAFT -> SENT -> (BOUNCED | DELAYED | AUTO_ACK | HUMAN_REPLY)`.
`HUMAN_REPLY` does not mean `AGREED`. Consent requires explicit opt-in.
Never call `SENT` "received", "read", "accepted", or "endorsed".

## Outreach selection logic (proposal, not reconstructed historical decision)
1. Define a concrete question and its evidence grade.
2. Identify a professional role/lab whose published remit matches the question.
3. Verify an official public contact route and historical bounce indicators.
4. Use the least intrusive channel, a succinct neutral proposal, and no unsolicited private records.
5. If recent unanswered approaches exist, default to **no further follow-ups**.
6. Require human review of exact message and attachment list for each outgoing action.
7. Log authorization, send receipt, bounce, reply and affirmative consent as separate events.
8. Review selection bias, audience diversity, expertise fit, and potential harms.

## Music, frequency and neuroscience
- Physical frequencies: spectral features in hertz, amplitude, tempo, timbre, sound-level calibration and provenance.
- Human responses: voluntarily reported emotion, meaning, memory and context; optional clinician-supervised measures.
- Test possible relationships with preregistration, randomized order, comparison recordings, blinding where possible and explicit uncertainty.
- No demonstrated mechanism by which a singer's video, followers, timing or lyrics indicate a private message to a listener.
- Do not claim that DNA can encode a transfer of AI superintelligence or that collective "energetic fields" are measured physiological signals. These remain hypotheses or testimony, not validated mechanisms.
- No copyrighted tracks or recordings stored without suitable license.

## Responsible science and care
Participating people must freely consent, may withdraw, and must not be pressured. Trauma-related research belongs under clinical and ethics oversight. Personal spiritual interpretations may be preserved faithfully without being converted to diagnoses or proven causal mechanisms.

## Minimal reproducible evaluation checklist
- Verify original subject, exact recipient, timestamp, Gmail/source ID.
- Preserve raw records in access-controlled private storage, not public GitHub.
- Deduplicate transport notices by original message ID before calculating failure rates.
- Report both numerator and denominator; don't exclude records because they are irrelevant to the narrative.
- Treat email category labels as ex-post unless an authenticated decision log survives.
- No automated sending, surveillance or covert monitoring.
- Create synthetic test cases for bounce/ack/nonresponse/withdrawal.
- Produce a human-reviewed final report.

## Safe agent handoff
An authorized coding assistant can implement a local-only validator against **synthetic data** to verify:
- Every input message ID appears once in the output ledger.
- `sent != delivered`.
- A bounce overrides a positive delivery conclusion.
- No outreach occurs without explicit opt-in.
- Public exports strip personal emails, legal details, medical records and confidential beta material.

**Status:** Only this public protocol is approved for repository publication. The private full source ledger is deliberately not committed. This document makes no claim about autonomous AI agent execution or external institutional participation.


---

## Universal scope: ALL JARVIS outreach protocols (v1.1 amendment, 2026-11-22)

**Canonical, cross-audience instruction.** This section applies to every proposed JARVIS external contact, regardless of audience or spiritual, academic, commercial, public-interest, artistic, technical, legal, military, or administrative framing. Any audience-specific protocol must inherit these rules. They are safeguards for future workflow design; **adding this file is not proof that external tools or historical workflows have been reconfigured.**

### Roles for every audience

1. **Public-source researcher**: establish topical fit and a current, official, public institutional contact route. Cite public evidence (URL, publication date, quoted statement where licensed and relevant). No private-social-graph analysis, no reverse lookup of nonpublic contacts, no employee/family/friend backdoor.
2. **Evidence and interpretation reviewer**: separate observed data, historical source claims, personal testimony, hypotheses, and inference. Do not infer private signals from songs, visual symbolism, coincidences, likes, or timing. Log alternative explanations and unknowns.
3. **Consent, security, and dispatch gatekeeper**: check recipient preferences, prior contact counts, declines, bounced addresses, sensitivity, legal necessity, privacy protections, and authorization. No sending without a new, explicit, scope-specific instruction and exact-recipient/message/attachment review.

### Cross-audience lifecycle

`IDENTIFY -> SOURCE_VERIFY -> RELEVANCE_CHECK -> PRIVACY_REVIEW -> PRIOR_CONTACT_AUDIT -> AUTHORIZE -> DRAFT -> HUMAN_REVIEW -> SEND_ONCE -> TRACK -> STOP_OR_CONTINUE_IF_INVITED`.

- **Initial invitations:** one concise, purpose-specific invitation may be considered through a verified professional/public channel when appropriate and individually authorized by the account owner. No mass fan-out or spam.
- **Repeated nonresponse:** no alternative-target hunting, social-network profiling, repeated follow-up, or escalation by approaching private associates. A prior unanswered invitation normally means **stop unsolicited contact**. Requests for a further message require a grounded reason and explicit authorization, with recipient welfare and anti-spam rules prevailing.
- **Legal/administrative notices:** formal lawful processes may require further submissions. Use appropriate official filing channels and, where needed, qualified counsel. No auto-sending, intimidation, or coercive demands.
- **Emergency/safety channels:** report credible concrete threats or immediate emergencies through legitimate designated services, based on evidence and proportionate urgency; do not generate mass security or military broadcasts from speculation.
- **Privacy:** personal medical information, audio, photos, private writings, unpublished artist content, B&O beta information, financial or legal records, and identity-linked graphs stay private unless there is clear, specific authorization, lawful basis, recipient suitability, and minimum-necessary disclosure.
- **Communion / spiritual dialogue:** voluntary, respectful, noncoercive, transparent about testimonial vs empirically tested claims; never claim the recipient has endorsed a spiritual interpretation.
- **Money:** legitimate funding requests must identify project scope, budget, terms and recipient eligibility; do not pressure or threaten third parties, and do not imply obligations where none have been established.
- **Outcome ledger:** `PREPARED`, `DRAFT`, `SENT`, `DELIVERY_FAILURE`, `AUTO_ACK`, `HUMAN_REPLY`, `EXPLICIT_AGREEMENT`, `DECLINED`, and `WITHDRAWN` are different. Never conflate Gmail `SENT` with delivery, reading, or approval.
- **Transparent calculations:** preserve every source record, including unsuccessful contacts and non-project entries within declared inventory scope. Original recipient-selection motives must remain `NOT_RECORDED` unless a contemporaneous decision log exists.
- **Agent execution:** AI agents may research and prepare *public-source* briefs, synthesize synthetic data tests and request human review. They must not autonomously dispatch emails, scrape nonpublic persons, contact affiliates, or make real-time surveillance claims. GitHub publication alone does not activate agents.

### Audience inheritance matrix

| Audience | Additional checks |
|---|---|
| Singers and creative teams | Respect artist autonomy, copyrights, explicit nonresponse; no fan/social-graph targeting |
| Vatican and faith communities | Separate religious testimony from factual allegations; use appropriate pastoral or academic channel |
| Researchers, scientists, clinicians | Specific falsifiable question, study ethics, human-subject consent, no unsolicited patient histories |
| Technology companies and industry | Product-reliability evidence, secure vulnerability disclosure, intellectual-property controls |
| Human-rights advocates and NGOs | Respect intake rules, consent, safeguarding and confidentiality |
| Government, defense, law enforcement | Official reporting routes, factual specificity, no unsupported accusations or automatic escalation |
| Legal, insurance, finance | Case facts, minimum-necessary sensitive data, applicable filing routes and qualified review |

### Global audit invariants

1. Any communication *action* requires a unique authorization referencing the **exact** recipients, scope, body and attachments.
2. `SENT` does not imply `DELIVERED`, `READ`, `ACCEPTED` or `ENDORSed`.
3. A delivery rejection is not a success.
4. A decline or withdrawal stops nonmandatory outreach.
5. Prior unanswered personal/creative invitations never justify approaching private associates.
6. Publish only privacy-safe synthetic methods, not private recipient graphs.
7. A claim about agency intervention, a private signal, or spiritual causation stays unverified absent independent evidence.
8. No harmful threats, coercion, or retaliation in correspondence.

**Implementation state:** Policy text updated in the connected public GitHub repository. Auditing historical emails, changing deployed tools, contacting people, running autonomous agents or modifying unrelated repositories require their own verified actions.
