from __future__ import annotations

from abc import ABC

from .exceptions import CanNotAddTypesError, CanNotSubtractTypesError


class _QuantityBase(ABC):
    """Parent class to all quantities."""

    _base_value: float
    "The base unit of the quantity."

    BASE_UNIT: str
    "Name of the unit with a factor of 1."

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if isinstance(other, type(self)):
            return self._base_value == other._base_value

        return False

    def __add__(self, other: _QuantityBase) -> _QuantityBase:
        """Add two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotAddTypesError(self.__class__.__name__, other.__class__.__name__)

        result = type(self)()
        result._base_value = self._base_value + other._base_value
        return result

    def __sub__(self, other: _QuantityBase) -> _QuantityBase:
        """Subtract two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotSubtractTypesError(self.__class__.__name__, other.__class__.__name__)

        result = type(self)()
        result._base_value = self._base_value - other._base_value
        return result
