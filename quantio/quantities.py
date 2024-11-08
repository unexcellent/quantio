from __future__ import annotations

from typing import ClassVar

from .exceptions import CanNotAddTypesError


class Length:
    """The one-dimensional extent of an object or the distance between two points."""

    _meters: float
    UNIT_CONVERSION: ClassVar[dict[str, float]] = {
        "miles": 1609.34,
        "kilometers": 10**3,
        "meters": 10**0,
        "feet": 0.3048,
        "inches": 0.0254,
        "centimeters": 10**-2,
        "millimeters": 10**-3,
        "micrometers": 10**-6,
    }

    def __init__(self, **kwargs: float) -> None:
        """Construct this class with the used units."""
        self._meters = (
            kwargs.get("miles", 0.0) * self.UNIT_CONVERSION["miles"]
            + kwargs.get("kilometers", 0.0) * self.UNIT_CONVERSION["kilometers"]
            + kwargs.get("meters", 0.0) * self.UNIT_CONVERSION["meters"]
            + kwargs.get("feet", 0.0) * self.UNIT_CONVERSION["feet"]
            + kwargs.get("inches", 0.0) * self.UNIT_CONVERSION["inches"]
            + kwargs.get("centimeters", 0.0) * self.UNIT_CONVERSION["centimeters"]
            + kwargs.get("millimeters", 0.0) * self.UNIT_CONVERSION["millimeters"]
            + kwargs.get("micrometers", 0.0) * self.UNIT_CONVERSION["micrometers"]
        )

    @property
    def miles(self) -> float:
        """The length in miles."""
        return self._meters / self.UNIT_CONVERSION["miles"]

    @property
    def kilometers(self) -> float:
        """The length in kilometers."""
        return self._meters / self.UNIT_CONVERSION["kilometers"]

    @property
    def meters(self) -> float:
        """The length in meters."""
        return self._meters / self.UNIT_CONVERSION["meters"]

    @property
    def feet(self) -> float:
        """The length in feet."""
        return self._meters / self.UNIT_CONVERSION["feet"]

    @property
    def inches(self) -> float:
        """The length in inches."""
        return self._meters / self.UNIT_CONVERSION["inches"]

    @property
    def centimeters(self) -> float:
        """The length in centimeters."""
        return self._meters / self.UNIT_CONVERSION["centimeters"]

    @property
    def millimeters(self) -> float:
        """The length in millimeters."""
        return self._meters / self.UNIT_CONVERSION["millimeters"]

    @property
    def micrometers(self) -> float:
        """The length in micrometers."""
        return self._meters / self.UNIT_CONVERSION["micrometers"]

    def __eq__(self, other: object) -> bool:
        """Assess if this length is the same as another."""
        if not isinstance(other, Length):
            return False
        return self._meters == other._meters

    def __add__(self, other: Length) -> Length:
        """Add two lengths together."""
        if not isinstance(other, Length):
            raise CanNotAddTypesError(self.__class__.__name__, other.__class__.__name__)
        return Length(meters=self._meters + other._meters)
