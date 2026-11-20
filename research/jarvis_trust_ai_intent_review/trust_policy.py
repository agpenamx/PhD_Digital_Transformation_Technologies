"""JARVIS Trust AI synthetic prototype, NOT a clinical risk assessor.

Copyright (c) 2026 Alejandro González Peña. MIT License (parent repo).
No external API calls, storage, health profiling, genetic inference or outreach.
"""
from __future__ import annotations
from dataclasses import dataclass
from hashlib import sha256
from typing import Literal

Label = Literal["acute_signal_for_review", "mortality_philosophy", "ambiguous_request_clarification", "undetermined"]

@dataclass(frozen=True)
class Result:
    label: Label
    rationale: str
    diagnosed: bool = False

@dataclass(frozen=True)
class CorrectionEvent:
    original_sha256: str
    first_assessment: Label
    clarified_meaning: str
    corrected_assessment: Label

def assess_synthetic(text: str) -> Result:
    """Demonstrates distinction, not generalizable safety. Do not use clinically."""
    s = text.lower().strip()
    # Only very explicit sample phrases trigger safety review in this demo.
    if any(p in s for p in (
        "i plan to kill myself tonight",
        "i will end my life today",
        "i intend to hurt myself now",
    )):
        return Result("acute_signal_for_review", "Explicit first-person near-term intent in synthetic sentence.")
    if any(p in s for p in (
        "when my body dies",
        "when i eventually die",
        "my soul is eternal",
        "human mortality",
    )):
        return Result("mortality_philosophy", "Mortality or personal spiritual perspective, not evidence of immediate action.")
    if any(p in s for p in ("when you no longer hear from me", "when you don't hear from me")):
        return Result("ambiguous_request_clarification", "Multiple plausible meanings; do not infer a plan.")
    return Result("undetermined", "Insufficient evidence; do not fabricate motives.")

def apply_clarification(original: str, first: Result, clarification: str) -> CorrectionEvent:
    """Keep original immutable, record superseding user clarification separately."""
    revised = assess_synthetic(clarification)
    return CorrectionEvent(
        original_sha256=sha256(original.encode("utf-8")).hexdigest(),
        first_assessment=first.label,
        clarified_meaning=clarification,
        corrected_assessment=revised.label,
    )

def weighted_loss(distortion: float, false_alarm: float, missed_risk: float, privacy: float,
                  weights: tuple[float, float, float, float]=(1.0, 1.0, 2.0, 2.0)) -> float:
    """A conceptual toy loss, not a scientifically calibrated risk probability."""
    values=(distortion, false_alarm, missed_risk, privacy)
    if any(not (0 <= v <= 1) for v in values) or any(w < 0 for w in weights):
        raise ValueError("Provide normalized nonnegative losses and weights.")
    return sum(w*x for w,x in zip(weights,values))
