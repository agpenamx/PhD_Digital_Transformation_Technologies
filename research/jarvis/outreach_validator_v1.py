"""JARVIS outreach validator: offline-only. No email, API, or network actions."""
from collections import Counter

VALID_STATES = {"DRAFT", "SENT", "DELAYED", "BOUNCED", "AUTO_ACK", "HUMAN_REPLY"}
VALID_CONSENT = {"NOT_REQUESTED", "REQUESTED", "EXPLICIT_OPT_IN", "DECLINED", "WITHDRAWN"}

def validate(rows):
    """Validate origin and consent without implying deliverability."""
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
    if duplicates:
        errors.append(f"duplicate source IDs: {len(duplicates)}")
    return {"rows": len(rows), "unique_ids": len(set(ids)), "duplicates": duplicates, "errors": errors, "passed": not errors}

def contact_decision(role_fit, official_channel, prior_unanswered, declined, private_data):
    """Deterministic human-centered gating, NEVER a send operation."""
    if declined:
        return "STOP", "Recipient declined"
    if prior_unanswered >= 2:
        return "STOP", "Repeated unanswered contact"
    if private_data:
        return "HUMAN_REVIEW", "Confidential data require privacy review"
    if not role_fit or not official_channel:
        return "HUMAN_REVIEW", "Fit/channel not verified"
    return "HUMAN_REVIEW", "One optional, separately approved human-reviewed inquiry"

def self_test():
    fixtures = [
        {"original_message_id":"synthetic-a","transport_state":"SENT","consent_status":"NOT_REQUESTED"},
        {"original_message_id":"synthetic-b","transport_state":"AUTO_ACK","consent_status":"REQUESTED"},
    ]
    assert validate(fixtures)["passed"]
    failing = fixtures + [{"original_message_id":"synthetic-a","transport_state":"BOUNCED",
                           "consent_status":"NOT_REQUESTED","assert_delivered":True}]
    assert len(validate(failing)["errors"]) >= 2
    assert contact_decision(True, True, 17, False, False)[0] == "STOP"
    print("PASS: offline synthetic outreach safety checks")

if __name__ == "__main__":
    self_test()
