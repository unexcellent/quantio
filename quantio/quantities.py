from __future__ import annotations

from typing import ClassVar

from ._quantity_base import _QuantityBase


class Length(_QuantityBase):
    """The one-dimensional extent of an object or the distance between two points."""

    unit_conversion: ClassVar[dict[str, float]] = {
        "miles": 1609.34,
        "kilometers": 10**3,
        "meters": 10**0,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 10**-2,
        "millimeters": 10**-3,
        "micrometers": 10**-6,
    }

    @property
    def miles(self) -> float:
        """The length in miles."""
        return self._base_value / self.unit_conversion["miles"]

    @property
    def kilometers(self) -> float:
        """The length in kilometers."""
        return self._base_value / self.unit_conversion["kilometers"]

    @property
    def meters(self) -> float:
        """The length in meters."""
        return self._base_value / self.unit_conversion["meters"]

    @property
    def feet(self) -> float:
        """The length in feet."""
        return self._base_value / self.unit_conversion["feet"]

    @property
    def inches(self) -> float:
        """The length in inches."""
        return self._base_value / self.unit_conversion["inches"]

    @property
    def centimeters(self) -> float:
        """The length in centimeters."""
        return self._base_value / self.unit_conversion["centimeters"]

    @property
    def millimeters(self) -> float:
        """The length in millimeters."""
        return self._base_value / self.unit_conversion["millimeters"]

    @property
    def micrometers(self) -> float:
        """The length in micrometers."""
        return self._base_value / self.unit_conversion["micrometers"]


class Time(_QuantityBase):
    """The duration of an event."""

    unit_conversion: ClassVar[dict[str, float]] = {
        "hours": 60 * 60,
        "minutes": 60,
        "seconds": 1,
        "milliseconds": 10**-3,
    }

    @property
    def hours(self) -> float:
        """The time in hours."""
        return self._base_value / self.unit_conversion["hours"]

    @property
    def minutes(self) -> float:
        """The time in minutes."""
        return self._base_value / self.unit_conversion["minutes"]

    @property
    def seconds(self) -> float:
        """The time in seconds."""
        return self._base_value / self.unit_conversion["seconds"]

    @property
    def milliseconds(self) -> float:
        """The time in milliseconds."""
        return self._base_value / self.unit_conversion["milliseconds"]
