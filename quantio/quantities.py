from __future__ import annotations

from ._quantity_base import _QuantityBase


class Area(_QuantityBase):
    """The two-dimensional extent of an object."""

    _UNIT_CONVERSION: dict[str, float] = {
        "square_miles": 1609.34**2,
        "square_kilometers": 10 ** (3 * 2),
        "square_meters": 10**0,
        "square_feet": 0.3048**2,
        "square_inches": 0.0254**2,
        "square_centimeters": 10 ** (-2 * 2),
        "square_millimeters": 10 ** (-3 * 2),
        "square_micrometers": 10 ** (-6 * 2),
    }


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
