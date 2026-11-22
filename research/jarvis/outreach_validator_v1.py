"""JARVIS universal outreach validator v1.1.

Offline-only synthetic validator. NO external calls, messaging, scraping,
privileged attachments, Gmail actions, or agent dispatch.
"""
from collections import Counter

VALID_STATES = {"DRAFT", "SENT", "DELAYED", "BOUNCED", "AUTO_ACK", "HUMAN_REPLY"}
VALID_CONSENT = {"NOT_REQUESTED", "REQUESTED", "EXPLICIT_OPT_IN", "DECLINED", "WITHDRAWN"}
VALID_AUDIENCES = {
    "artists_creative", "vatican_religious", "research_scientific_clinical",
    "tech_industry", "human_rights", "government_defense_law_enforcement",
    "legal_insurance_finance", "other",
}
VALID_PERMISSIONS = {
    "NOT_AUTHORIZED", "EXPLICIT_REVIEW_AUTHORIZED", "EXPLICIT_SEND_AUTHORIZED"
}


def validate(rows, strict_universal=False):
    """Audit evidence fields. Legacy rows remain readable in nonstrict mode.

    strict_universal=True checks all current routing metadata, but does NOT
    authorize or perform any contact.
    """
    rows = list(rows)
    errors = []
    ids = [str(r.get("original_message_id", "")).strip() for r in rows]
    duplicates = [k for k, n in Counter(ids).items() if k and n > 1]
    for index, row in enumerate(rows, 1):
        state = row.get("transport_state")
        consent = row.get("consent_status")
        if not ids[index - 1]:
            errors.append(f"row {index}: missing message ID")
        if state not in VALID_STATES:
            errors.append(f"row {index}: invalid transport state")
        if consent not in VALID_CONSENT:
            errors.append(f"row {index}: invalid consent state")
        if row.get("assert_delivered") is True and state in {"SENT", "DELAYED", "BOUNCED"}:
            errors.append(f"row {index}: no delivery proof")
        if row.get("assert_reciprocal_consent") is True and consent != "EXPLICIT_OPT_IN":
            errors.append(f"row {index}: consent must be explicit")
        if row.get("social_graph_or_private_person_targeting") is True:
            errors.append(f"row {index}: nonpublic social-graph targeting prohibited")
        if consent in {"DECLINED", "WITHDRAWN"} and row.get("proposed_unsolicited_followup"):
            errors.append(f"row {index}: must respect decline/withdrawal")
        if strict_universal:
            if row.get("audience_category") not in VALID_AUDIENCES:
                errors.append(f"row {index}: missing/invalid audience category")
            if row.get("outreach_permission") not in VALID_PERMISSIONS:
                errors.append(f"row {index}: missing/invalid outreach permission")
            if type(row.get("previous_unanswered_contacts")) is not int or row["previous_unanswered_contacts"] < 0:
                errors.append(f"row {index}: invalid prior unanswered contact count")
            if type(row.get("official_professional_channel_verified")) is not bool:
                errors.append(f"row {index}: official route verification missing")
            if type(row.get("social_graph_or_private_person_targeting")) is not bool:
                errors.append(f"row {index}: private targeting flag missing")
            if type(row.get("sensitive_personal_data_included")) is not bool:
                errors.append(f"row {index}: sensitive disclosure flag missing")
    if duplicates:
        errors.append(f"duplicate source IDs: {len(duplicates)}")
    return {"rows": len(rows), "unique_ids": len(set(ids)), "duplicates": duplicates,
            "errors": errors, "passed": not errors}


def contact_decision(role_fit, official_channel, prior_unanswered, declined,
                     private_data, *, social_graph_targeting=False,
                     audience_kind="other", user_authorized=False,
                     formal_legal_or_emergency=False):
    """Offline route recommendation. NEVER returns permission to send.

    Formal legal notice / real emergency cases require their own qualified
    channel and review, rather than broad mass outreach.
    """
    if declined and not formal_legal_or_emergency:
        return "STOP", "Recipient declined or withdrew"
    if social_graph_targeting:
        return "STOP", "No profiling or indirect outreach via private associates"
    if formal_legal_or_emergency:
        return "OFFICIAL_CHANNEL_REVIEW", "Check concrete necessity, proper authority and evidence; no auto send"
    if prior_unanswered >= 1:
        return "STOP", "Unanswered optional outreach; do not escalate or route around silence"
    if private_data:
        return "HUMAN_REVIEW", "Sensitive material; minimum necessary disclosure"
    if not role_fit or not official_channel:
        return "HUMAN_REVIEW", "Fit/channel not verified"
    if audience_kind not in VALID_AUDIENCES:
        return "HUMAN_REVIEW", "Unknown audience class"
    if not user_authorized:
        return "DRAFT_ONLY", "No explicit, scope-specific approval"
    return "HUMAN_REVIEW", "Exact message, audience and attachments still require human review"


def self_test():
    fixtures = [
        {"original_message_id": "synth-vatican", "transport_state": "SENT",
         "consent_status": "NOT_REQUESTED", "audience_category": "vatican_religious",
         "outreach_permission": "NOT_AUTHORIZED", "previous_unanswered_contacts": 0,
         "official_professional_channel_verified": True,
         "social_graph_or_private_person_targeting": False,
         "sensitive_personal_data_included": False},
        {"original_message_id": "synth-artist", "transport_state": "AUTO_ACK",
         "consent_status": "REQUESTED", "audience_category": "artists_creative",
         "outreach_permission": "EXPLICIT_REVIEW_AUTHORIZED", "previous_unanswered_contacts": 1,
         "official_professional_channel_verified": True,
         "social_graph_or_private_person_targeting": False,
         "sensitive_personal_data_included": False},
    ]
    assert validate(fixtures, strict_universal=True)["passed"]
    failing = fixtures + [
        {"original_message_id": "synth-vatican", "transport_state": "BOUNCED",
         "consent_status": "NOT_REQUESTED", "assert_delivered": True,
         "social_graph_or_private_person_targeting": True}
    ]
    assert len(validate(failing)["errors"]) >= 3
    assert contact_decision(True, True, 17, False, False,
                            audience_kind="artists_creative", user_authorized=True)[0] == "STOP"
    assert contact_decision(True, True, 0, False, False,
                            social_graph_targeting=True, user_authorized=True)[0] == "STOP"
    assert contact_decision(True, True, 0, False, False,
                            audience_kind="research_scientific_clinical")[0] == "DRAFT_ONLY"
    assert contact_decision(True, True, 0, False, False,
                            audience_kind="government_defense_law_enforcement",
                            formal_legal_or_emergency=True)[0] == "OFFICIAL_CHANNEL_REVIEW"
    for audience in sorted(VALID_AUDIENCES):
        outcome, reason = contact_decision(True, True, 0, False, False,
                                           audience_kind=audience, user_authorized=True)
        assert outcome == "HUMAN_REVIEW" and reason
    print("PASS: offline universal outreach safeguards (synthetic fixtures only)")


if __name__ == "__main__":
    self_test()
