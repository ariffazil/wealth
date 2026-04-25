"""
civilizational/cascade_detector.py
=================================
WEALTH Civilizational Organ — Cascade Detector.

Detects cascade risk: when local failures propagate globally.
Based on: coup / financial contagion / supply chain / information cascade.

DITEMPA BUKAN DIBERI — Forged from real cascade events, not handed down.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional
import math


CASCADE_MECHANISMS = {
    "financial": {
        "description": "Asset price collapse → margin calls → forced sales → deeper collapse",
        "velocity": "fast",         # seconds to minutes
        "reversibility": "low",
        "attenuation": "low",
        "typical_trigger": "liquidity_sudden_stop",
    },
    "information": {
        "description": "Narrative spreads faster than correction, behavior changes before facts",
        "velocity": "instant",      # social media amplification
        "reversibility": "medium",
        "attenuation": "low",
        "typical_trigger": "credible_source_repeats_falsehood",
    },
    "institutional": {
        "description": "Authority loss triggers authority loss — legitimacy cascade",
        "velocity": "slow",         # days to weeks
        "reversibility": "very_low",
        "attenuation": "very_low",
        "typical_trigger": "high_profile_betrayal",
    },
    "supply_chain": {
        "description": "Single-point-of-failure node collapse propagates upstream and downstream",
        "velocity": "medium",      # hours to days
        "reversibility": "medium",
        "attenuation": "medium",
        "typical_trigger": "key_supplier_default",
    },
    "social": {
        "description": "Network effect: each participant joining increases others' joining probability",
        "velocity": "fast",
        "reversibility": "low",
        "attenuation": "low",
        "typical_trigger": "social_movement_momentum",
    },
}


def _network_cascade_risk(
    node_count: int,
    connectivity: float,          # 0-1, how connected each node is
    vulnerability_density: float,   # 0-1, fraction of nodes vulnerable
    cascade_threshold: float,       # 0-1, fraction of nodes failed before cascade starts
) -> float:
    """
    Estimate cascade probability in a network.
    
    High connectivity + high vulnerability = cascade likely.
    High threshold = robust to cascades.
    """
    # Percolation-style: cascade happens when vulnerable nodes form spanning cluster
    # Simplified: effective_vulnerability = connectivity * vulnerability_density
    effective = connectivity * vulnerability_density
    
    # Cascade probability rises steeply above cascade_threshold
    if effective <= cascade_threshold:
        return round(max(0.0, effective), 6)
    
    # Above threshold: cascade probability grows toward 1
    overshoot = effective - cascade_threshold
    max_overshoot = 1.0 - cascade_threshold
    return round(min(1.0, cascade_threshold + math.sqrt(overshoot * max_overshoot)), 6)


def cascade_detect(
    mechanism: str,
    trigger_magnitude: float,          # 0-1, severity of triggering event
    connectivity: float = 0.5,          # 0-1, how interconnected is the system
    vulnerability_density: float = 0.3,  # 0-1, fraction of vulnerable nodes
    cascade_threshold: float = 0.15,     # 0-1, cascade starts when this fraction fails
    damping: float = 0.1,               # 0-1, attenuates cascade as it propagates
    failed_nodes: int = 0,              # current count of failed nodes
    total_nodes: int = 100,            # total nodes in network
    historical_cascade_events: int = 0, # prior known cascades in this system
) -> Dict[str, Any]:
    """
    Detect cascade risk for a given mechanism and trigger.

    Returns cascade risk score, propagation estimate, and mitigation signals.
    """
    mechanism_key = mechanism.lower().strip()
    if mechanism_key not in CASCADE_MECHANISMS:
        mechanism_key = "financial"  # fallback

    meta = CASCADE_MECHANISMS[mechanism_key]

    # Network cascade risk
    if total_nodes > 0:
        vuln_density = max(0.0, min(1.0, (failed_nodes / total_nodes) + vulnerability_density * trigger_magnitude))
    else:
        vuln_density = vulnerability_density * trigger_magnitude

    cascade_prob = _network_cascade_risk(
        total_nodes,
        max(0.0, min(1.0, connectivity)),
        max(0.0, min(1.0, vuln_density)),
        max(0.0, min(1.0, cascade_threshold)),
    )

    # Attenuation effect: each propagation step reduces intensity
    velocity_rank = {"instant": 4, "fast": 3, "medium": 2, "slow": 1}
    velocity_score = velocity_rank.get(meta["velocity"], 2) / 4.0
    reversibility_rank = {"very_low": 0, "low": 0.25, "medium": 0.5, "high": 1.0}
    reversibility_score = reversibility_rank.get(meta["reversibility"], 0.5)

    # Cascade severity: combines trigger magnitude, velocity, low reversibility, low damping
    severity = (
        trigger_magnitude * 0.3
        + velocity_score * 0.2
        + (1.0 - reversibility_score) * 0.3
        + (1.0 - damping) * 0.2
    )
    severity = round(max(0.0, min(1.0, severity)), 6)

    # Cascade velocity: how fast does it spread (1 = instant global)
    velocity_descriptor = meta["velocity"]
    velocity_map = {"instant": 1.0, "fast": 0.75, "medium": 0.4, "slow": 0.15}
    cascade_velocity = velocity_map.get(velocity_descriptor, 0.5)

    # Estimated propagation: what fraction of network is affected at peak
    propagation_estimate = round(min(1.0, cascade_prob * cascade_velocity * severity * 2), 6)

    # Flags
    flags: List[str] = []
    if cascade_prob > 0.6:
        flags.append("CASCADE_PROBABILITY_HIGH")
    if severity > 0.7:
        flags.append("CASCADE_SEVERITY_CRITICAL")
    if reversibility_score < 0.3:
        flags.append("CASCADE_POORLY_REVERSIBLE")
    if damping < 0.2:
        flags.append("LOW_DAMPING_MITIGATION")
    if historical_cascade_events >= 3:
        flags.append("RECURRENT_CASCADE_PATTERN")

    # Mitigation signals
    mitigation_signals = []
    if damping < 0.3:
        mitigation_signals.append("Increase damping buffers")
    if connectivity > 0.7:
        mitigation_signals.append("Reduce network connectivity to slow propagation")
    if vulnerability_density > 0.5:
        mitigation_signals.append("Harden vulnerable nodes against cascade trigger")
    if reversibility_score < 0.3:
        mitigation_signals.append("Pre-position recovery resources for rapid restoration")

    verdict = "SEAL"
    if cascade_prob > 0.7 or severity > 0.8:
        verdict = "888-HOLD"
    elif cascade_prob > 0.5 or severity > 0.6:
        verdict = "CAUTION"

    return {
        "mechanism": mechanism_key,
        "trigger_magnitude": round(trigger_magnitude, 4),
        "cascade_probability": cascade_prob,
        "cascade_severity": severity,
        "cascade_velocity": cascade_velocity,
        "propagation_estimate": propagation_estimate,
        "reversibility_score": reversibility_score,
        "damping": round(damping, 4),
        "integrity_flags": flags,
        "mitigation_signals": mitigation_signals,
        "mechanism_description": meta["description"],
        "typical_trigger": meta["typical_trigger"],
        "verdict": verdict,
    }
