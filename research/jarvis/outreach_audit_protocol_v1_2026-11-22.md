# JARVIS Outreach Audit Protocol v1.0 (Public, Privacy-Safe)
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
