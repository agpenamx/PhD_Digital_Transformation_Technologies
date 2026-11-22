# JARVIS | Biomedical Science Evidence Tracker
Initial snapshot: 2026-11-22 • Evidence review, not diagnosis or medical device.
Scope: cardiopulmonary physiology, glucose/insulin regulation, sensory peripheral nerves, bioelectric signaling, and falsifiable intersections.

## Research question register

| ID | Domain | Mechanism established independently | What remains to be evaluated |
| --- | --- | --- | --- |
| S1 | Respiratory–cardiovascular coupling | Inhaled oxygen crosses alveolar-capillary surfaces; blood circulation distributes it to tissues, and carbon dioxide returns to the lungs | Patient-specific oxygen status requires measured data, not description alone |
| S2 | Insulin and glucose | Pancreatic beta cells regulate insulin secretion in relation to metabolic need; insulin helps regulate glucose use and storage | A reported sensation does not establish an insulin concentration or blood-glucose value |
| S3 | Nerve bioelectricity | Nerve cells propagate electrochemical action potentials arising from ion flow across membranes | A felt electrical sensation does not identify its source or provide a direct measurement of nerve signaling |
| S4 | "First two fingers" | Depending on precisely which digits are meant, median-nerve and other sensory distributions can be relevant; compression is one possible cause of tingling | Unspecified fingers, location, duration, trigger and accompanying symptoms mean no cause can be inferred |
| S5 | Cross-system hypotheses | Nerve activity and glucose/oxygen availability are part of normal physiology | Any proposed direct temporal or causal linkage must specify synchronized independent measurements, controls and confounders |

### Terminology and epistemic rules

- `OBSERVED`: concrete firsthand sensory report or independently measured numeric data, clearly distinguished.
- `MEASURED`: device measurement, method, units, timestamp, conditions, uncertainty.
- `HYPOTHESIS`: explicit prediction, appropriate comparator and potential refutation.
- `ESTABLISHED`: robust scientific consensus supported by authoritative evidence.
- `SPIRITUAL_INTERPRETATION`: testimony about spiritual meaning. Respectfully record if the author requests; no inferred biomedical mechanism.
- `UNVERIFIED`: no independent evidence supporting a causal claim.

**Never infer** insulin levels, oxygen saturation, heart rate, nerve damage, EEG activity or consciousness changes without evidence. Do not treat spiritual or demonic influence, telepathy, timeline changes or external forces as experimentally confirmed explanations for symptoms. Distinguish neural electrical activity from externally applied electrical energy.

### Minimal, voluntary private observation schema

`event_id`, `reported_at_local`, `described_sensation_verbatim`, `digits_involved_optional`, `side_optional`, `duration_optional`, `activity_optional`, `measured_glucose_optional`, `measured_spo2_optional`, `measured_hr_optional`, `measurement_device_optional`, `source`, `evidence_class`, `interpretation_optional`, `privacy_permission`.

Do not solicit or publish measurements automatically. Never expose personal health records or specific individual observations on this public file. A private, clinical follow-up should be voluntary and conducted by appropriate professionals when indicated.

## Primary reference baseline (checked 2026-11-22)

- National Heart, Lung, and Blood Institute (NIH), *How the Lungs Work: The Respiratory System*. https://www.nhlbi.nih.gov/health/lungs/respiratory-system
- National Heart, Lung, and Blood Institute (NIH), *How the Heart Works*. https://www.nhlbi.nih.gov/health/heart
- National Institute of Diabetes and Digestive and Kidney Diseases (NIH), *How Eating and Fasting Regulate Insulin* (2023). https://www.niddk.nih.gov/news/archive/2023/how-eating-fasting-regulate-insulin
- MedlinePlus, *Carpal Tunnel Syndrome*. https://medlineplus.gov/carpaltunnelsyndrome.html
- NCBI Bookshelf, *Physiology, Nerve* (StatPearls). https://www.ncbi.nlm.nih.gov/books/NBK551652/
- NCBI Bookshelf, *Electrical Signals of Nerve Cells* (Purves et al., neuroscience textbook; historical mechanistic reference, not latest empirical research). https://www.ncbi.nlm.nih.gov/books/NBK11053/

## Monitoring and communication

- Existing JARVIS B independent-verification daily automation updated 2026-11-22 to check for important *new* relevant findings, clearly compare study design, replication, evidence strength and dates.
- Notification only on substantive developments; avoid repetitive reports with no changes.
- No autonomous DNA analysis, clinical intervention, drug advice, outreach, publication of private data, or physical monitoring.
- GitHub protocol file alone does not activate sensors or establish continuous vital sign monitoring.
