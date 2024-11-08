from __future__ import annotations

from typing import ClassVar


class Length:
    """The one-dimensional extent of an object or the distance between two points."""

    _meters: float
    UNIT_CONVERSION: ClassVar[dict[str, float]] = {
        "kilometers": 10**3,
        "meters": 10**0,
        "centimeters": 10**-2,
        "millimeters": 10**-3,
        "micrometers": 10**-6,
    }

    def __init__(self, **kwargs: float) -> None:
        """Construct this class with the used units."""
        self._meters = (
            kwargs.get("kilometers", 0.0) * self.UNIT_CONVERSION["kilometers"]
            + kwargs.get("meters", 0.0) * self.UNIT_CONVERSION["meters"]
            + kwargs.get("centimeters", 0.0) * self.UNIT_CONVERSION["centimeters"]
            + kwargs.get("millimeters", 0.0) * self.UNIT_CONVERSION["millimeters"]
            + kwargs.get("micrometers", 0.0) * self.UNIT_CONVERSION["micrometers"]
        )

    @property
    def kilometers(self) -> float:
        """The length in kilometers."""
        return self._meters / self.UNIT_CONVERSION["kilometers"]

    @property
    def meters(self) -> float:
        """The length in meters."""
        return self._meters / self.UNIT_CONVERSION["meters"]

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
