"""JARVIS 3.33.0: offline research primitives; Python 3.11+ standard library.
No diagnosis, device monitoring, molecular inference, dispatch or model training.
Statistical formulas are conditional on their documented assumptions.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
from hashlib import sha256
from urllib.parse import urlparse, parse_qs
from zoneinfo import ZoneInfo
import cmath
import math
import re

VERSION = "3.33.0"


def finite(value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("finite real number required")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("finite real number required")
    return value


def count(value: int, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("integer count outside allowed range")
    return value


def probability(value: float, *, open_interval: bool = False) -> float:
    value = finite(value)
    if not (0 < value < 1 if open_interval else 0 <= value <= 1):
        raise ValueError("probability outside allowed range")
    return value


def text_digest(text: str) -> str:
    """Exact UTF-8 checksum, not a signature or trusted timestamp."""
    if not isinstance(text, str):
        raise ValueError("text required")
    return sha256(text.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class TextRecord:
    raw: str
    source_id: str
    sha256_utf8: str
    interpretation: str = ""

    def __post_init__(self):
        if not isinstance(self.source_id, str) or not self.source_id.strip():
            raise ValueError("source ID required")
        if self.sha256_utf8 != text_digest(self.raw):
            raise ValueError("raw text does not match checksum")

    @classmethod
    def preserve(cls, raw: str, source_id: str, interpretation: str = ""):
        return cls(raw, source_id, text_digest(raw), interpretation)


def video_id(url: str) -> str:
    """Group share URL variants, without modifying the original records."""
    p = urlparse(url)
    if p.scheme not in {"https", "http"} or p.username or p.password:
        raise ValueError("supported public YouTube URL required")
    host = (p.hostname or "").lower()
    if host == "youtu.be":
        ident = p.path.strip("/")
    elif host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if p.path == "/watch":
            values = parse_qs(p.query).get("v", [])
            if len(values) != 1:
                raise ValueError("single video identifier required")
            ident = values[0]
        elif re.fullmatch(r"/(shorts|embed|live)/[\w-]{11}/?", p.path):
            ident = p.path.strip("/").split("/")[1]
        else:
            raise ValueError("unsupported video path")
    else:
        raise ValueError("unsupported host")
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", ident):
        raise ValueError("invalid video identifier")
    return ident


def parse_time(value: str) -> datetime:
    """Reject missing timezone; never infer message or viewing times."""
    d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if d.tzinfo is None or d.utcoffset() is None:
        raise ValueError("timezone required")
    return d.astimezone(timezone.utc)


def local_time(value: str, zone: str = "America/Mexico_City") -> str:
    return parse_time(value).astimezone(ZoneInfo(zone)).isoformat()


def lag_bounds(first: str, second: str, first_error_s: float, second_error_s: float):
    """Conservative interval for second-first using bounded clock errors."""
    a, b = finite(first_error_s), finite(second_error_s)
    if min(a, b) < 0:
        raise ValueError("error bounds must be nonnegative")
    delta = (parse_time(second) - parse_time(first)).total_seconds()
    return delta - a - b, delta + a + b


def latency_ms(start_ns: int, finish_ns: int, start_clock: str, finish_clock: str) -> float:
    """Elapsed monotonic time only for the SAME instrument/clock domain."""
    count(start_ns, 0); count(finish_ns, 0)
    if not start_clock or start_clock != finish_clock or finish_ns < start_ns:
        raise ValueError("incompatible clocks or event order")
    return (finish_ns - start_ns) / 1_000_000


def independent_family_chance(p: float, comparisons: int) -> float:
    """P(at least one event) for m INDEPENDENT identical Bernoulli trials.
    Not a probability for personal meaning or a causal explanation.
    """
    p = probability(p); count(comparisons, 0)
    if comparisons == 0 or p == 0:
        return 0.0
    if p == 1:
        return 1.0
    return -math.expm1(comparisons * math.log1p(-p))


def effective_n(n: int, rho: float) -> float:
    """Equal-variance, exchangeable observations with common nonnegative rho."""
    count(n); rho = probability(rho)
    return n / (1 + (n - 1) * rho)


def holm_adjust(pvalues: list[float]) -> list[float]:
    """Holm FWER-adjusted p values; valid marginal tests still required."""
    p = [probability(x) for x in pvalues]
    m = len(p); result = [0.0] * m; running = 0.0
    for rank, i in enumerate(sorted(range(m), key=lambda j: p[j])):
        running = max(running, min(1.0, (m - rank) * p[i]))
        result[i] = running
    return result


def zero_failure_upper(n: int, alpha: float = 0.05) -> float:
    """Exact one-sided 1-alpha bound after zero i.i.d. Bernoulli failures."""
    count(n); alpha = probability(alpha, open_interval=True)
    return -math.expm1(math.log(alpha) / n)


def required_clean_trials(target: float, alpha: float = 0.05) -> int:
    target = probability(target, open_interval=True)
    alpha = probability(alpha, open_interval=True)
    return math.ceil(math.log(alpha) / math.log1p(-target))


def complete_graph_edges(n: int) -> int:
    count(n, 0)
    return n * (n - 1) // 2


def evolve_diagonal(energies: list[float], amplitudes: list[complex], t: float,
                    hbar: float = 1.0) -> list[complex]:
    """Analytic unitary evolution for a diagonal finite-dimensional Hamiltonian.
    Dimensionless natural units by default; not an experimental measurement.
    """
    t = finite(t); hbar = finite(hbar)
    es = [finite(e) for e in energies]
    if hbar <= 0 or len(es) != len(amplitudes) or not es:
        raise ValueError("positive hbar and matching nonempty arrays required")
    a = [complex(z) for z in amplitudes]
    if any(not (math.isfinite(z.real) and math.isfinite(z.imag)) for z in a):
        raise ValueError("finite amplitudes required")
    if not math.isclose(sum(abs(z)**2 for z in a), 1.0, abs_tol=1e-12):
        raise ValueError("normalized initial state required")
    phases = [e*t/hbar for e in es]
    if any(not math.isfinite(p) for p in phases):
        raise ValueError("phase overflow")
    return [z * cmath.exp(-1j*p) for z, p in zip(a, phases)]


def clock_conditioned_plus_probability(omega: float, t: float) -> float:
    """Two-qubit relational-clock toy: P(+|t)=(1+cos(omega*t))/2.
    Global state (|01>+|10>)/sqrt(2); H_C=H_S=omega*Z/2, hbar=1.
    A periodic two-level clock is not a universal clock or a personal signal.
    """
    phase = finite(omega) * finite(t)
    if not math.isfinite(phase):
        raise ValueError("phase overflow")
    return (1 + math.cos(phase)) / 2


def validate_action_status(status: str, receipt: str | None) -> bool:
    """Require a receipt reference for asserted completion; not authentication.
    This does not send anything or establish delivery, reading or consent.
    """
    if status not in {"NOT_STARTED", "PREPARED", "ATTEMPTED", "CONFIRMED", "FAILED"}:
        raise ValueError("unsupported action state")
    return status != "CONFIRMED" or (isinstance(receipt, str) and bool(receipt.strip()))
