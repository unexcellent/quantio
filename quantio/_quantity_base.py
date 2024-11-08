from __future__ import annotations

from abc import ABC, abstractmethod


class _QuantityBase(ABC):
    """Parent class to all quantities."""

    _base_value: float
    "The base unit of the quantity."

    @property
    @abstractmethod
    def unit_conversion(self) -> dict[str, float]:
        """Dict containing all units of the quantity."""

    def __init__(self, **kwargs: float) -> None:
        """Construct this class with the used units."""
        self._base_value = 0.0

        for unit_name, factor in self.unit_conversion.items():
            self._base_value += kwargs.get(unit_name, 0.0) * factor

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if type(self) is not type(other):
            return False

        return self._base_value == other._base_value  # type: ignore
