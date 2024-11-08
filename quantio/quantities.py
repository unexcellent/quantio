from __future__ import annotations

from ._quantity_base import _QuantityBase


class Length(_QuantityBase):
    """The one-dimensional extent of an object or the distance between two points."""

    _UNIT_CONVERSION: dict[str, float] = {
        "miles": 1609.34,
        "kilometers": 10**3,
        "meters": 10**0,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 10**-2,
        "millimeters": 10**-3,
        "micrometers": 10**-6,
    }


class Time(_QuantityBase):
    """The duration of an event."""

    _UNIT_CONVERSION: dict[str, float] = {
        "hours": 60 * 60,
        "minutes": 60,
        "seconds": 1,
        "milliseconds": 10**-3,
    }
