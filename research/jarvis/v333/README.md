# JARVIS v3.33 | Reproducible research addendum

Version 3.33.0 is a project release identifier, not an AI capability rating, clinical result or upgrade of a provider's model. This additive revision leaves the earlier manuscripts and v1.5 reference implementation unchanged. Personal testimony, health observations, credentials and private media records are excluded from this public directory.

## Implemented offline controls

- Exact UTF-8 text checksums with interpretation stored separately.
- Canonical video identity while retaining submitted URLs in a separate private source record.
- Timezone-required timestamps, bounded clock-error propagation and same-clock monotonic latency.
- Effective sample size for exchangeable correlated observations, Holm multiplicity adjustment, exact zero-failure bounds and complete-graph baselines.
- Analytic diagonal-Hamiltonian unitary evolution and a two-qubit conditional-clock example.
- Action-state validation requiring a receipt reference for asserted confirmation. A reference alone does not authenticate the event.

There are 44 synthetic unit tests. They check implementation behavior, not health claims, molecular changes, consciousness, unusual communication or real-world safety rates.

## Mathematical assumptions

For equal-variance observations with common nonnegative correlation rho:
`n_eff = n / (1 + (n - 1)*rho)`.
Do not estimate rho from a coincidence or count multiple copies as independent experiments.

For m independent comparisons with event probability p:
`P(at least one event) = 1 - (1-p)^m`.
This is an illustrative sampling formula, not a fitted probability of a person's experiences. Holm-adjusted p-values require valid individual tests and a declared comparison family.

With zero failures in n independent, identically distributed Bernoulli trials:
`p_upper = 1 - alpha^(1/n)` and
`n_required = ceil(log(alpha)/log(1-target))`.
At alpha=0.05, target=0.0001 requires 29,956 clean independent trials. A small unit-test suite does not satisfy that evidentiary requirement.

For independently bounded timestamp errors, the true lag lies within:
`[(b-a)-(u_a+u_b), (b-a)+(u_a+u_b)]`.
An interval crossing zero does not establish event order. Event order does not establish causation. Video publication, viewing, message submission and metadata retrieval are different event types.

## Quantum time example

Standard quantum mechanics uses the time-dependent Schrodinger equation. Relational-clock models can describe subsystem evolution conditioned on a clock even when a joint state is stationary. These are not contradictory statements.

The included toy uses `H_C=H_S=omega*Z/2` and the stationary global state `(|01>+|10>)/sqrt(2)`, in units with hbar=1. Conditioning on the clock phase yields `P(+|t)=(1+cos(omega*t))/2`. The two-level clock is periodic and idealized. This is not an experiment, a measurement of consciousness, or an explanation of electronic-response timing.

Primary sources:
- MIT quantum-mechanics course notes: https://ocw.mit.edu/courses/5-74-introductory-quantum-mechanics-ii-spring-2009/f61b11cc95a86973d9815f85093088db_MIT5_74s09_lec01.pdf
- Moreva et al., Time from quantum entanglement: https://arxiv.org/abs/1310.4691

## Adaptive linguistic review

Preserve original wording. Put spelling normalization, translation, interpretation, confidence and source limitations in separate fields. Do not infer a diagnosis, biological identity, expertise or external authority from capitalization, writing errors, emotional intensity or a project role name. Automatically generated captions with uncertain language identification are not verified translation or evidence of a new language.

## Biomedical research boundary

Self-reported experience, neural mechanism, molecular structure and clinical efficacy require different evidence. Published odor-memory research supports studying smell/emotion associations, but an individual report cannot localize brain activity. Human DNA's ordinary double-helical structure is not replaced by engineered multi-helix DNA origami. Sound or relaxation reports do not establish a measured anatomical change.

References:
- Watanabe et al. (2018), PMID 29867658: https://pubmed.ncbi.nlm.nih.gov/29867658/
- NHGRI, Double Helix: https://www.genome.gov/genetics-glossary/Double-Helix
- Lee et al. (2017), engineered DNA origami: https://pubmed.ncbi.nlm.nih.gov/29233997/

## Reproduce

`python -m unittest discover -s research/jarvis/v333 -p 'test_jarvis_v333.py' -v`

No network access, monitoring, clinical procedures, molecular assays, email sending, institutional reporting or automated agent deployment is implemented. Keep private source bundles out of public GitHub. Independent review remains necessary before production use.
