"""
civilizational/prosperity_index.py
=================================
WEALTH Civilizational Organ — Prosperity Index.

Measures multi-dimensional prosperity at civilization scale.
Based on:物质 / relational / capability / resilience /生态.

DITEMPA BUKAN DIBERI — Forged from real civilizational patterns, not handed down.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional


def _sigmoid(x: float, center: float = 0.5, steepness: float = 8.0) -> float:
    """Sigmoid centering: maps raw 0-1 to curve that plateaus at extremes."""
    import math
    return 1.0 / (1.0 + math.exp(-steepness * (x - center)))


def _harmonic_mean(values: List[float]) -> float:
    """Harmonic mean — penalizes extremes harder than arithmetic mean."""
    import math
    n = len(values)
    if n == 0:
        return 0.0
    valid = [v for v in values if v > 0]
    if not valid:
        return 0.0
    return n / sum(1.0 / v for v in valid)


def prosperity_index(
    material: float,           # 0-1, material security (income, assets, basic needs)
    relational: float,         # 0-1, relational capital (trust, networks, community)
    capability: float,         # 0-1, capability development (education, skills, agency)
    resilience: float,        # 0-1, resilience (adaptability, recovery, buffers)
    ecological: float,        # 0-1, ecological sustainability (environmental health)
    stability_weight: float = 0.15,  # weight for stability floor
    floor_mode: bool = True,  # if True, prosperity can't exceed weakest dimension + floor
) -> Dict[str, Any]:
    """
    Compute civilizational prosperity index (CPI).

    Unlike GDP which only measures throughput, CPI captures:
    - Is growth actually improving lives?
    - Is prosperity resilient or fragile?
    - Are ecological costs being externalized?

    Returns prosperity index (0-1) + breakdown + integrity signals.
    """
    dimensions = {
        "material": material,
        "relational": relational,
        "capability": capability,
        "resilience": resilience,
        "ecological": ecological,
    }

    # Clamp all to [0, 1]
    clamped = {k: max(0.0, min(1.0, v)) for k, v in dimensions.items()}

    # Individual scores
    individual = {k: round(v, 6) for k, v in clamped.items()}

    # Core composite: harmonic mean (penalizes imbalance)
    # If one dimension is near zero, overall prosperity collapses
    harmonic = _harmonic_mean(list(clamped.values()))
    
    # Arithmetic mean as upper bound reference
    arithmetic = sum(clamped.values()) / len(clamped)

    # Stability floor: minimum of all dimensions (weakest-link constraint)
    min_dim = min(clamped.values())
    
    # Prosperity index: weighted blend of harmonic + floor
    # Imbalanced wealth (high material, low relational) scores lower
    prosperity = (1.0 - stability_weight) * harmonic + stability_weight * min_dim
    prosperity = round(prosperity, 6)

    # Integrity signals
    flags: List[str] = []
    imbalances: Dict[str, float] = {}

    for name, val in clamped.items():
        gap = arithmetic - val
        if gap > 0.3:
            imbalances[name] = round(gap, 4)
            flags.append(f"IMBALANCE_{name.upper()}")

    weak_link = min(clamped, key=clamped.get)
    if clamped[weak_link] < 0.3:
        flags.append("PROSPERITY_FRAGILE")

    # Sustainability check: if ecological is lowest, flag extractive pattern
    sorted_dims = sorted(clamped.items(), key=lambda x: x[1])
    if sorted_dims[0][0] == "ecological":
        flags.append("ECOLOGICAL_BASELINE_VIOLATION")

    return {
        "prosperity_index": prosperity,
        "harmonic_mean": round(harmonic, 6),
        "arithmetic_mean": round(arithmetic, 6),
        "weakest_link": weak_link,
        "weakest_value": round(clamped[weak_link], 6),
        "dimensions": individual,
        "imbalances": imbalances,
        "integrity_flags": flags,
        "verdict": "SEAL" if not any(f.startswith("IMBALANCE_") or f in (
            "PROSPERITY_FRAGILE", "ECOLOGICAL_BASELINE_VIOLATION"
        ) for f in flags) else "888-HOLD",
    }


def prosperity_band(cpi: float) -> str:
    """Map prosperity index to human-readable band."""
    if cpi >= 0.85:
        return "THRIVING"
    if cpi >= 0.70:
        return "STABLE"
    if cpi >= 0.55:
        return "SURVIVING"
    if cpi >= 0.35:
        return "FRAGILE"
    return "CRITICAL"
