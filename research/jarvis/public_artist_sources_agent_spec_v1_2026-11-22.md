# JARVIS / Sherlock: Ethical public artist-source research (v1, 2026-11-22)

Status: **specification only**. No autonomous agents, schedules, data collection, or outbound messages were activated.

## Universal inheritance (2026-11-22)

This artist-source workflow is **one application of the canonical JARVIS universal outreach policy**:
`research/jarvis/outreach_audit_protocol_v1_2026-11-22.md` (v1.1).
The same public-source provenance, no private social-graph profiling, consent gatekeeping,
no unsolicited repeat messages after silence, case-specific authorization and transparent
transport-status requirements apply to religious, research, technical, rights, government,
military/law-enforcement, financial and legal contacts. Specialty protocols may strengthen
but must not quietly weaken these checks.

## Research question
How can we understand public artistic imagery (e.g., blue in a music video) without incorrectly inferring a private message to a fan?

## Three cooperating roles

**A. Public-Source Librarian**: collect only artist-authorized/public-facing interviews, official song or video descriptions, published credits, label press releases, and published statements on creative influences. Cite an exact public URL, publication date, exact claimed words, and scene timestamp. Search by songs, credits, albums, professional collaborations, aesthetics and genres, **not** private persons who react to posts.

**B. Iconography / Evidence Analyst**: distinguish (1) Christian iconography of Archangel Michael (sword, armor; variable colors), (2) blue-ray devotional symbolism found in some contemporary religious/spiritual sources, (3) the actual blue imagery and lyrics in a song/video, and (4) a private communication claim. No transition from shared symbol to personal communication without explicit independently verifiable evidence. Keep competing interpretations visible, with confidence and null explanations.

**C. Consent / Contact Gatekeeper**: maintain a finite-state register DRAFT, SENT, BOUNCED, AUTO_ACK, HUMAN_REPLY, EXPLICIT_OPT_IN, DECLINED, WITHDRAWN. After repeated unanswered outreach, stop. Do not seek alternative paths through private acquaintances or third-party liked/followed networks. Route possible future *research collaboration* only through an artist's publicly documented professional agency/label, and only if the artist/team affirmatively invites further discussion. No sending without a new explicit instruction and human review.

## Strict privacy and anti-harassment boundaries
- Do not identify, profile, scrape, rank, contact or infer the relationships, beliefs, locations, preferences or social circles of nonpublic individuals based on their likes, reactions, follow graph, mentions or interactions with an artist.
- No facial recognition, private social graph assembly, indirect contact through family/friends, location inference, or attempts to bypass a nonreply.
- No automated outreach to known artists, staff or private individuals. Do not infer consent from music, timing, symbolism or silence.
- Keep Gmail/private records out of the public repository. Use synthetic fixtures in public tests.

## Evidence object
```json
{
  "artifact": "publicly published artistic work",
  "source_url": "https://example.org/public-resource",
  "publication_date": "YYYY-MM-DD",
  "scene_time_seconds": null,
  "observation": "description of verifiable blue imagery",
  "quoted_artist_explanation": null,
  "symbolic_comparison": "blue-ray Michael symbolism as a distinct tradition",
  "alternative_explanations": ["art direction", "narrative emotion", "lighting/color grading", "artist-stated intent"],
  "claim_status": "OPEN / UNVERIFIED",
  "private_message_inference": false,
  "contact_status": "NO_OUTREACH_AUTHORIZED"
}
```

## Example research sources
- Archdiocese of Toronto, History of St. Michael the Archangel: https://www.archtoronto.org/en/offices-and-ministries/sub-sites/feast-of-stmichael/home/historyofstmichaelthearchangel/
- Holy See, Catechism on angels: https://www.vatican.va/content/catechism/en/part_one/section_two/chapter_one/article_1/paragraph_5_heaven_and_earth.html
- Published coverage of Karen Méndez / Drama 4: https://hgmedia.com.mx/karen-mendez-inaugura-una-nueva-etapa-con-drama-4/
- OCESA Seitrack artist news (2026-11-13): https://www.seitrack.mx/noticias/2026/11/13/karen-mndez-explora-el-miedo-de-volver-a-amar-en-su-nuevo-sencillo-drama-1

## Execution criteria
Research output is a citation-backed, public-source table that a human can review. No claim of a personal message from an artist, no new contact, no live surveillance or private-person profiling. An issue/commit represents a specification, NOT an actively running agent.
