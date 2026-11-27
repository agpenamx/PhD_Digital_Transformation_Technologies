# JARVIS PRO v1.5 | Public-safe research controls (23 Nov 2026)

**Status:** independent AI-assisted research; offline reference implementation only. No agents were deployed and no external messages were sent by this change.

**Preservation:** The original JARVIS / Gray Box manuscripts, uploaded credentials, private correspondence and personal testimony are *not* committed. The source author retains editorial control. This is an additive, non-destructive update; it does not revise the earlier sources.

## Technical delta
- Keep first-person testimony verbatim, separate from scientific hypotheses, interpretations and claims of external causation.
- Track `OBSERVED`, `DERIVED`, `HYPOTHESIS`, `PERSONAL_TESTIMONY` and `UNKNOWN` separately.
- Treat external sources and generative-model answers as evidence inputs, never as authorization instructions.
- Introduce offline-only checks for duplicate message IDs, unsupported delivery assertions and assent without opt-in.
- Block optional outreach after silence, withdrawal, private-network targeting or coercion.
- Require exact-recipient/message/attachment authorization before any future outgoing action.
- Distinguish an append-only SHA-256 checksum demonstration from signed, trusted or post-quantum security.
- Evaluate false refusals as well as false approvals, with a human appeal/remedy channel.

## Scope and limits
The local private release retained 26 uploaded sources: 2 JARVIS research archives, 22 professional-learning PDFs and 2 text files. Local historical scripts and 22 v1.5 synthetic tests passed. These are **not** external peer review, live system certification or validation of cosmological, clinical or institutional claims. The earlier 111-destination outreach subset represents historical metadata, not new contact actions or endorsements.

## Research programme
Preregister a four-arm comparison of conventional review, LLM-only, JARVIS ledger/control and JARVIS plus independent review/appeal. Report privacy events, unauthorized permissions, erroneous refusals, evidence provenance errors, remedy time and human costs. Compare 12/13/14-node graph baselines; 78 connections in a 13-node complete undirected graph is a combinatorial identity, not independent evidence of a cosmological structure.

## Standards references
- NIST AI RMF Generative AI Profile (AI 600-1): https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- FIPS 203 (ML-KEM): https://csrc.nist.gov/pubs/fips/203/final
- FIPS 204 (ML-DSA): https://csrc.nist.gov/pubs/fips/204/final
- FIPS 205 (SLH-DSA) is a published NIST post-quantum signature standard: https://csrc.nist.gov/Projects/Post-Quantum-Cryptography

No FIPS PQC implementation is asserted. A SHA-256 ledger is not a quantum-resistant signature.

## Use
Run the public synthetic offline test suite with:

`python -m unittest discover -s research/jarvis -p 'test_jarvis_pro_v1_5_gate.py' -v`

No external transport, scraping, surveillance, messaging, live profile enrichment or institutional access is implemented.

## Release boundary
Do not commit the full private source bundle or medical/legal/financial records to a public repository. Public release requires explicit file-level review and independent documentation of any external action actually performed.
