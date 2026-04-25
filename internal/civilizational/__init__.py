"""
civilizational/__init__.py
WEALTH Civilizational Organ Package.

Exports:
    - prosperity_index, prosperity_band
    - cascade_detect
    - boundary_monitor
"""
from __future__ import annotations

from .prosperity_index import prosperity_index, prosperity_band
from .cascade_detector import cascade_detect, CASCADE_MECHANISMS
from .boundary_monitor import boundary_monitor, BOUNDARY_CATEGORIES, SAFE_RANGES

__all__ = [
    "prosperity_index",
    "prosperity_band",
    "cascade_detect",
    "CASCADE_MECHANISMS",
    "boundary_monitor",
    "BOUNDARY_CATEGORIES",
    "SAFE_RANGES",
]
