"""JARVIS Spiritual AI 4.44.0: offline evidence, acoustic and budget helpers.
No messaging, biological inference, network access, clinical diagnosis or model training.
Acoustic results describe digital samples, not a listener's sound exposure or health.
Requires Python 3.11+ and NumPy. Original source is never rewritten.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from hashlib import sha256
import json
import math
import wave
import numpy as np

VERSION = "4.44.0"

@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    speaker: str
    raw: str
    kind: str
    def __post_init__(self):
        if not all(isinstance(v,str) and v.strip() for v in (self.source_id,self.speaker,self.raw)):
            raise ValueError("nonempty source ID, speaker and original text required")
        if self.kind not in {"SELF_REPORT", "QUOTED_WARNING", "INTERPRETATION", "MEASUREMENT"}:
            raise ValueError("unknown evidence type")
    @property
    def digest(self):
        return sha256(self.raw.encode("utf-8")).hexdigest()
    def supports_self_report(self):
        return self.speaker == "user" and self.kind == "SELF_REPORT"


def correction_event(source: SourceRecord, correction: str, reason: str) -> dict:
    """Return an append-only derivative record; do not edit source.raw."""
    if not all(isinstance(x,str) and x.strip() for x in (correction,reason)):
        raise ValueError("correction and reason required")
    return {"source_id":source.source_id, "original_sha256":source.digest,
            "correction":correction, "reason":reason, "relation":"clarifies",
            "original_unchanged":True}


def observation_export(records: list[SourceRecord]) -> list[dict]:
    """Typed selection only; NOT a natural-language medical classifier."""
    return [{"source_id":r.source_id,"text":r.raw,"sha256":r.digest}
            for r in records if r.supports_self_report()]


def measure_samples(samples, sample_rate: int) -> dict:
    """Hann-windowed one-sided periodogram, per channel. Normalized PCM only.
    A highest-power bin is NOT pitch or evidence of a therapeutic frequency.
    Bin spacing is not the ability to resolve nearby spectral components.
    """
    if type(sample_rate) is not int or sample_rate <= 0:
        raise ValueError("positive integer sample rate required")
    x=np.asarray(samples,dtype=float)
    if x.ndim == 1: x=x[:,None]
    if x.ndim != 2 or not (1 <= x.shape[1] <= 2) or x.shape[0] < 8:
        raise ValueError("at least eight mono/stereo frames required")
    if x.shape[0] > sample_rate*300:
        raise ValueError("maximum permitted sample duration is 300 seconds")
    if not np.all(np.isfinite(x)) or np.max(np.abs(x))>1:
        raise ValueError("finite normalized PCM values in [-1,1] required")
    n=x.shape[0]; w=np.hanning(n); U=float(np.sum(w*w)); out=[]
    f=np.fft.rfftfreq(n,1/sample_rate)
    for channel in range(x.shape[1]):
        s=x[:,channel];rms=float(np.sqrt(np.mean(s*s)))
        y=(s-np.mean(s))*w
        power=np.abs(np.fft.rfft(y))**2/(sample_rate*U)
        if n%2==0: power[1:-1]*=2
        else: power[1:]*=2
        total=float(np.sum(power))
        out.append({"channel":channel+1,"rms_fs":rms,
            "rms_dbfs":None if rms==0 else 20*math.log10(rms),
            "spectral_peak_hz":None if total==0 else float(f[int(np.argmax(power))]),
            "power_centroid_hz":None if total==0 else float(np.sum(f*power)/total),
            "full_scale_sample_count":int(np.sum(np.abs(s)>=1)),
            "windowed_ac_power_fs2":float(total*sample_rate/n)})
    return {"version":VERSION,"frames":n,"channels":x.shape[1],"sample_rate_hz":sample_rate,
        "duration_s":n/sample_rate,"fft_bin_spacing_hz":sample_rate/n,
        "nyquist_hz":sample_rate/2,"window":"symmetric Hann; mean removed",
        "measurements":out,"sound_pressure_level_db_spl":None,
        "interpretation":"Digital signal descriptors only; no biological, spiritual or speaker inference."}


def analyze_pcm16(path: str | Path) -> dict:
    """Read uncompressed 16-bit PCM WAV only; no downloading or conversion."""
    p=Path(path)
    if not p.is_file():raise FileNotFoundError(p)
    if p.stat().st_size > 100_000_000:raise ValueError("file exceeds 100 MB")
    raw=p.read_bytes()
    with wave.open(str(p),"rb") as f:
        channels=f.getnchannels();rate=f.getframerate();frames=f.getnframes()
        if f.getsampwidth()!=2 or f.getcomptype()!='NONE' or channels not in (1,2):
            raise ValueError("requires uncompressed mono/stereo PCM16 WAV")
        if frames>rate*300:raise ValueError("audio duration exceeds 300 seconds")
        data=f.readframes(frames)
    if len(data)!=frames*channels*2:raise ValueError("truncated PCM data")
    samples=np.frombuffer(data,dtype='<i2').astype(float).reshape(frames,channels)/32768
    result=measure_samples(samples,rate)
    result.update(source_sha256=sha256(raw).hexdigest(),file_name=p.name,
                  input_kind="WAV_BYTES",clinical_efficacy_evaluated=False)
    return result


def scenario(hours, rate_mxn, cash_cost_mxn, proposed_fee_mxn) -> dict:
    """Illustrative arithmetic. Not a market valuation, invoice or debt."""
    vals=[]
    for v in (hours,rate_mxn,cash_cost_mxn,proposed_fee_mxn):
        if isinstance(v,bool):raise ValueError("boolean is not an amount")
        d=Decimal(str(v))
        if not d.is_finite() or d<0:raise ValueError("finite nonnegative values required")
        vals.append(d)
    h,r,c,p=vals; labor=h*r; total=labor+c
    q=lambda d:str(d.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
    return {"basis":"ILLUSTRATIVE_ASSUMPTIONS_NOT_OBSERVED", "currency":"MXN",
        "hours":str(h),"rate_mxn":q(r),"labor_mxn":q(labor),"cash_cost_mxn":q(c),
        "economic_cost_mxn":q(total),"proposed_fee_mxn":q(p),
        "fee_less_cost_mxn":q(p-total),"receivable_verified":False}


def validate_delivery(status: str, receipt: str | None, recipients_reviewed: bool) -> bool:
    if status not in {"PREPARED","HELD","SENT"}:raise ValueError("unsupported state")
    if status!='SENT':return True
    return (isinstance(receipt,str) and bool(receipt.strip()) and recipients_reviewed is True)

if __name__ == '__main__':
    import argparse
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('wav',type=Path)
    args=ap.parse_args()
    print(json.dumps(analyze_pcm16(args.wav),ensure_ascii=False,indent=2,allow_nan=False))
