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

        for unit, factor in self.unit_conversion.items():
            self._base_value += kwargs.get(unit, 0.0) * factor
