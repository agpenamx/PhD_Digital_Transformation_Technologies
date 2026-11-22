# JARVIS / PROMETHEUS: source-transparent outreach audit (2026-11-22)

**Status:** Public *methodology only*. No private mailbox records or attachments are stored in this repository.

## Scope and observable evidence
- Audit window: Gmail `in:sent after:2026/11/01 before:2026/11/23`.
- Control inventory: **417 sent message IDs**, reconciled to **417 source-linked metadata rows**. No rows removed based on theme or recipient.
- Recipient parsing: **432 To-address occurrences** and **123 distinct parsed addresses** (counts are not confirmed independent human recipients).
- Additional **8** historical project keyword matches before November are kept in a *separate* private worksheet. That is not an all-time mailbox census.
- **35** separate delivery status notices were found (27 failure, 8 delay); they are not automatically one-to-one with unique original messages.
- The full detailed register, private legal records, original correspondence and attachments remain in the owner's **private** audit workspace.

## Why recipients appeared
No surviving machine-readable historical decision trace was found for each contact. Audience categories were therefore added **after** discovering all messages. These labels are hypotheses for the author's review and must never be described as proof that an agent chose a recipient, that the recipient reviewed the material, or that the recipient endorsed it.

Relevant topics in original messages include AI accountability, freedom of conscience, creative rights, the meaning of music to listeners, verifiable acoustic measurements, scientific falsification, privacy, and civilian safety. No unverified physiological, quantum, or spiritual causal mechanism is assumed.

## Source-first reconciliation algorithm
1. Enumerate all Gmail `SENT` IDs in a declared time window with pagination.
2. Fetch metadata for every ID. Backfill missing summary objects from authoritative per-ID reads.
3. Preserve every row and original provider timestamp without time-zone rewriting.
4. Verify unique message IDs and record-count agreement; do not deduplicate by recipient.
5. Only *after* completeness checks, add review labels inferred from observable subjects/recipients.
6. Separately collect bounce, delay, auto-acknowledgment, substantive human reply, and explicit consent events.
7. Associate a delivery notice to an original message only with adequate transport-level evidence; do not simply subtract notices from sent counts.
8. Generate a private, full-fidelity register and a public, redacted methodology report.

## AI-to-AI exchange contract
This repository offers a **machine-readable research handoff**, not an autonomous transmission or a Copilot execution. An authorized coding agent may ingest the schema, tests and public synthetic fixtures. Private messages are not to be uploaded automatically.

Minimal schema fields:
`timestamp_raw, to_full, cc_full, bcc_full, subject_original, gmail_message_id, gmail_thread_id, gmail_status, has_attachment, gmail_message_url, review_category_inferred, selection_reason_record, classification_basis, evidence_scope`.

Allowed workflow: inspect locally -> validate -> summarize -> human review.
Disallowed workflow: bulk send, scrape private social followers, infer personal consent, expose identifiable private correspondence, or attribute secret agency participation without evidence.

## Review criteria
- Complete coverage of the stated date window
- Unambiguous source provenance and UTC normalization for comparisons
- Distinct SENT / BOUNCED / AUTO-ACK / HUMAN-REPLY / OPT-IN labels
- Explicit reasoning about outreach fatigue and consent
- No publication of private health, legal or financial materials
- Full audit of omitted categories and exceptions

**No GitHub Copilot or other paid coding agent was invoked by this Markdown commit.** Running an AI coding agent or submitting additional material requires separate action through a supported tool or the GitHub interface.
