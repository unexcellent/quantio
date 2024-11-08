from __future__ import annotations

from abc import ABC, abstractmethod

from .exceptions import CanNotAddTypesError, CanNotSubtractTypesError


class _QuantityBase(ABC):
    """Parent class to all quantities."""

    _base_value: float
    "The base unit of the quantity."

    @property
    @abstractmethod
    def _UNIT_CONVERSION(self) -> dict[str, float]:
        """Table used for recording the units with conversion values."""

    def __init__(self, **kwargs: float) -> None:
        """Construct this class with the used units."""
        self._base_value = kwargs.get("_base_value", 0.0)

        for unit_name, factor in self._UNIT_CONVERSION.items():
            self._base_value += kwargs.get(unit_name, 0.0) * factor

        for unit_name, factor in self._UNIT_CONVERSION.items():

            def make_property(factor: float) -> property:
                return property(lambda self: self._base_value / factor)

            setattr(self.__class__, unit_name, make_property(factor))

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if type(self) is not type(other):
            return False

        return self._base_value == other._base_value  # type: ignore

    def __add__(self, other: _QuantityBase) -> _QuantityBase:
        """Add two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotAddTypesError(self.__class__.__name__, other.__class__.__name__)
        return type(self)(_base_value=self._base_value + other._base_value)

    def __sub__(self, other: _QuantityBase) -> _QuantityBase:
        """Subtract two quantities of the same type."""
        if type(self) is not type(other):
            raise CanNotSubtractTypesError(self.__class__.__name__, other.__class__.__name__)
        return type(self)(_base_value=self._base_value - other._base_value)
