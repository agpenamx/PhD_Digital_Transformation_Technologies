# JARVIS Trust AI: Intent-Correction Research Prototype

**Research lead / conceptual author:** Alejandro González Peña  
**Version:** 0.1-review | **Snapshot:** 2026-11-20 (America/Mexico_City)  
**Status:** draft for independent review, not a certified clinical or autonomous safety system.

## Research question
How can a conversational AI distinguish philosophical discussion of mortality from an immediate safety concern, while retaining the ability to respond appropriately to **new** explicit risk evidence?

The design records an initial interpretation, a user clarification, and a correction event rather than silently rewriting what happened. It minimizes unjustified inferences about intent and unrequested personal data exposure.

## Technical proposal
A loss to evaluate on independently labeled, consented data is
`L = w_D * D + w_F * F + w_R * R + w_P * P`,
where D=meaning distortion, F=false-positive alarm, R=missed material safety concern, P=privacy exposure. All weights are hypothetical and must be selected through governance, testing and external review.

Expected invariants:
1. Preserve original statements and provenance, distinguish user claims from assistant inference.
2. Let an explicit user clarification correct an unsupported earlier interpretation.
3. An earlier correction must not mask **new** evidence of acute danger.
4. Never diagnose, infer genetics, profile by religion, or contact third parties from this prototype.
5. Human review, consent, privacy and incident audit before deployment.

## Run
`python -m unittest -v test_trust_policy.py`

**Important:** This is a tiny transparent rule-based demonstration, not a clinical triage classifier. Keyword-based logic is unreliable across dialects and contexts. The test set is synthetic and far too small for a safety or fairness claim.

## Independent references
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- FDA implanted BCI guidance: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/implanted-brain-computer-interface-bci-devices-patients-paralysis-or-amputation-non-clinical-testing

## Scope and rights
This public branch deliberately excludes medical records, private testimony, personal contacts, minors' information, outbound campaign lists and private JARVIS archives. The user's thesis/repository README lists GitHub https://github.com/agpenamx and LinkedIn https://linkedin.com/in/agpenamxio as professional contact channels.

Copyright (c) 2026 Alejandro González Peña. Code contribution follows the parent repository's existing MIT License; retain attribution. Source documents and third-party media retain their separate rights. Copyright notices are not proof of patent or trademark registration.
