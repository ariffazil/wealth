"""
civilizational/boundary_monitor.py
==================================
WEALTH Civilizational Organ — Boundary Monitor.

Tracks when systems approach or exceed safe operating boundaries.
Based on: planetary boundaries / carrying capacity / maruah floor.

DITEMPA BUKAN DIBERI — Forged from real boundary science, not handed down.
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional
import math


# Boundary categories
BOUNDARY_CATEGORIES = {
    "ecological": {
        "description": "Planetary/civilizational ecological carrying capacity",
        "unit": "ratio_to_safe_boundary",
        "direction": "lower_is_safer",
    },
    "financial": {
        "description": "Debt/inflation/money supply stability boundaries",
        "unit": "ratio_to_collapse_threshold",
        "direction": "lower_is_safer",
    },
    "social": {
        "description": "Inequality, trust erosion, institutional legitimacy",
        "unit": "gini_or_trust_index",
        "direction": "context_dependent",
    },
    "informational": {
        "description": "Narrative integrity, epistemicCommons health",
        "unit": "fraction_clean_information",
        "direction": "higher_is_safer",
    },
    "capability": {
        "description": "Distributed capability — education, health, agency",
        "unit": "capability_index",
        "direction": "higher_is_safer",
    },
}


# Safe operating ranges (all normalized 0-1)
SAFE_RANGES = {
    "ecological":      (0.20, 0.80),   # breach <0.20 or >0.80 is critical
    "financial":        (0.30, 0.85),   # financial ratio to threshold
    "social":           (0.40, 1.00),   # gini: lower is safer; trust: higher is safer
    "informational":    (0.50, 1.00),   # fraction clean: higher is safer
    "capability":       (0.45, 1.00),   # capability index: higher is safer
}


def _distance_to_boundary(value: float, safe_low: float, safe_high: float) -> float:
    """Distance from safe zone — 0 = inside safe, positive = outside."""
    if safe_low <= value <= safe_high:
        return 0.0
    if value < safe_low:
        return round((safe_low - value) / safe_low, 6)
    # value > safe_high
    return round((value - safe_high) / (1.0 - safe_high + 1e-9), 6)


def boundary_monitor(
    current_state: Dict[str, float],
    boundary_targets: Optional[Dict[str, float]] = None,
    time_horizon_years: int = 10,
    growth_rate: float = 0.0,          # assumed growth in current_state per year
    margin_preference: float = 0.15,    # how close to boundary before warning (0-1)
    categories: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Monitor system state against safe operating boundaries.

    current_state: dict of category -> normalized value (0-1)
    boundary_targets: optional dict of category -> target values (for planning)
    growth_rate: assumed annual growth rate affecting trajectory

    Returns per-boundary status + composite boundary integrity score.
    """
    categories = categories or list(SAFE_RANGES.keys())
    boundary_integrity_scores: Dict[str, float] = {}
    boundary_flags: List[str] = []
    boundary_trajectories: Dict[str, Dict[str, Any]] = {}

    for cat in categories:
        if cat not in SAFE_RANGES:
            continue

        value = current_state.get(cat, 0.5)
        safe_low, safe_high = SAFE_RANGES[cat]

        # Distance from boundary
        dist = _distance_to_boundary(value, safe_low, safe_high)

        # Margin check: warning when within margin_preference of boundary
        in_safe = safe_low <= value <= safe_high

        if not in_safe:
            if value < safe_low:
                breach_direction = "BELOW_FLOOR"
                breach_amount = round(safe_low - value, 6)
            else:
                breach_direction = "ABOVE_CEILING"
                breach_amount = round(value - safe_high, 6)
            boundary_flags.append(f"BOUNDARY_BREACH_{cat.upper()}")
            boundary_integrity_scores[cat] = round(max(0.0, 1.0 - dist), 6)
        elif dist < margin_preference:
            boundary_flags.append(f"BOUNDARY_APPROACHING_{cat.upper()}")
            boundary_integrity_scores[cat] = round((dist / margin_preference) * 0.9 + 0.1, 6)
        else:
            boundary_integrity_scores[cat] = round(1.0 - (dist / 2.0), 6)

        # Trajectory projection
        if growth_rate != 0.0 and time_horizon_years > 0:
            projected = value + growth_rate * time_horizon_years
            projected = max(0.0, min(1.0, projected))
            projected_dist = _distance_to_boundary(projected, safe_low, safe_high)
            years_to_breach: Optional[float] = None
            
            if growth_rate > 0 and projected > safe_high:
                # Growing toward ceiling
                if growth_rate > 0:
                    years_to_breach = round((value - safe_high) / growth_rate + 1e-9, 2)
            elif growth_rate < 0 and projected < safe_low:
                # Declining toward floor
                if growth_rate < 0:
                    years_to_breach = round((safe_low - value) / abs(growth_rate) + 1e-9, 2)

            boundary_trajectories[cat] = {
                "current": round(value, 6),
                "projected": round(projected, 6),
                "years_to_breach": years_to_breach,
                "direction": "growing" if growth_rate > 0 else "declining" if growth_rate < 0 else "stable",
            }
        else:
            boundary_trajectories[cat] = {
                "current": round(value, 6),
                "projected": round(value, 6),
                "years_to_breach": None,
                "direction": "stable",
            }

    # Composite boundary integrity score: harmonic mean (weakest-link matters most)
    scores = list(boundary_integrity_scores.values())
    n = len(scores)
    if n == 0:
        composite_integrity = 1.0
    else:
        valid = [s for s in scores if s > 0]
        if not valid:
            composite_integrity = 0.0
        else:
            composite_integrity = round(n / sum(1.0 / s for s in valid), 6)

    # Overall verdict
    breach_count = sum(1 for f in boundary_flags if "BREACH" in f)
    approaching_count = sum(1 for f in boundary_flags if "APPROACHING" in f)

    if breach_count >= 2:
        verdict = "VOID"
    elif breach_count == 1:
        verdict = "888-HOLD"
    elif approaching_count >= 3:
        verdict = "CAUTION"
    elif approaching_count >= 1:
        verdict = "QUALIFY"
    else:
        verdict = "SEAL"

    return {
        "composite_boundary_integrity": composite_integrity,
        "boundary_scores": {k: round(v, 6) for k, v in boundary_integrity_scores.items()},
        "trajectories": boundary_trajectories,
        "verdict": verdict,
        "integrity_flags": boundary_flags,
        "summary": {
            "breach_count": breach_count,
            "approaching_count": approaching_count,
            "margin_preference": margin_preference,
            "time_horizon_years": time_horizon_years,
            "assumed_growth_rate": round(growth_rate, 4),
        },
    }
