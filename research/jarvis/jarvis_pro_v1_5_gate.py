"""JARVIS PRO v1.5: synthetic, offline-only outreach and claim integrity gates.
Reference methodology, not a sender, monitoring agent or safety certification.
"""
from dataclasses import dataclass
from hashlib import sha256
import json

CLAIMS = frozenset(("OBSERVED", "DERIVED", "HYPOTHESIS", "PERSONAL_TESTIMONY", "UNKNOWN"))
CONSENT = frozenset(("NOT_REQUESTED", "REQUESTED", "EXPLICIT_OPT_IN", "DECLINED", "WITHDRAWN"))
TRANSPORT = frozenset(("DRAFT", "SENT", "DELAYED", "BOUNCED", "AUTO_ACK", "HUMAN_REPLY"))

def seal_verbatim(text: str) -> str:
    """Checksum preserves bytes of UTF-8 encoding; NOT a digital signature."""
    return sha256(text.encode("utf-8")).hexdigest()

def classify(label: str) -> str:
    if label not in CLAIMS:
        raise ValueError("not a recognized evidentiary class")
    return label

@dataclass(frozen=True)
class DraftRequest:
    recipient_id: str
    authorized_exact_scope: bool
    reviewed_exact_message: bool
    reviewed_attachments: bool
    official_channel_verified: bool
    unanswered_previous: int = 0
    consent: str = "NOT_REQUESTED"
    sensitive_data: bool = False
    social_graph_targeting: bool = False
    coercive: bool = False
    formal_or_emergency: bool = False

def preflight(req: DraftRequest) -> str:
    """Return a REVIEW state; never grants permission or performs a send."""
    if req.consent not in CONSENT or req.unanswered_previous < 0:
        raise ValueError("invalid consent or unanswered count")
    if req.coercive or req.social_graph_targeting:
        return "HOLD"
    if req.consent in {"DECLINED", "WITHDRAWN"} or req.unanswered_previous > 0:
        return "HOLD"
    if req.formal_or_emergency:
        return "OFFICIAL_CHANNEL_REVIEW"
    if req.sensitive_data or not req.official_channel_verified or not req.recipient_id:
        return "HOLD"
    if not (req.authorized_exact_scope and req.reviewed_exact_message and req.reviewed_attachments):
        return "DRAFT_ONLY"
    return "APPROVAL_PENDING"

def inspect_historical_messages(rows: list[dict]) -> dict:
    """State audit only, without Gmail access or claims of delivery."""
    seen = set()
    issues = []
    for index, row in enumerate(rows, 1):
        ident = row.get("id")
        state = row.get("transport")
        consent = row.get("consent")
        if not ident or ident in seen:
            issues.append(f"row {index}: missing or duplicate ID")
        seen.add(ident)
        if state not in TRANSPORT or consent not in CONSENT:
            issues.append(f"row {index}: invalid state")
        if row.get("assert_delivered") and state in {"DRAFT", "SENT", "DELAYED", "BOUNCED"}:
            issues.append(f"row {index}: no delivery evidence")
        if row.get("assert_agreed") and consent != "EXPLICIT_OPT_IN":
            issues.append(f"row {index}: no affirmative opt-in")
    return {"rows": len(rows), "issues": issues, "passed": not issues,
            "note": "Synthetic/local audit only; no transport or account access"}

def check_chain(rows: list[dict]) -> bool:
    """Check canonicalized hash chain; no authentication or immutability claim."""
    previous = "0"*64
    for i, row in enumerate(rows):
        body = {"index": i, "previous": previous, "payload": row.get("payload")}
        encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        if row.get("previous") != previous or row.get("hash") != sha256(encoded.encode("utf-8")).hexdigest():
            return False
        previous = row["hash"]
    return True
