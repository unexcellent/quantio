from __future__ import annotations

from typing import Generic, TypeVar

import numpy as np

from ._quantity_base import _QuantityBase
from .exceptions import NoUnitSpecifiedError

T = TypeVar("T")


class Vector(Generic[T]):
    """A 1 dimensional array of either quantity or numeric elements."""

    _elements: np.array

    def __init__(self, elements: list | tuple | np.ndarray) -> None:
        self._elements = np.array(elements)

    @classmethod
    def arange(cls, start: T, stop: T, step: T) -> Vector[T]:
        """Return evenly spaced values within a given interval."""
        if isinstance(start, _QuantityBase):
            start_val = start._base_value

            if not isinstance(stop, _QuantityBase):
                raise TypeError
            stop_val = stop._base_value

            if not isinstance(step, _QuantityBase):
                raise TypeError
            step_val = step._base_value

            element_type = type(start)
            return Vector(
                [element_type(value) for value in np.arange(start_val, stop_val, step_val)]
            )

        return Vector(np.arange(start, stop, step))

    def to_numpy(self, unit: str | None = None) -> np.ndarray[float]:
        """Convert this vector into a numpy array of floats."""
        if isinstance(self._elements[0], _QuantityBase):
            if unit is None:
                raise NoUnitSpecifiedError
            return np.array([getattr(element, unit) for element in self._elements])

        return np.array([float(element) for element in self._elements])

    @classmethod
    def __class_getitem__(cls, *_: object) -> type:
        """Return this class for type hinting."""
        return cls

    def __getitem__(self, index: int) -> T:
        """Return the element at a specific index."""
        return self._elements[index]

    def __setitem__(self, index: int, value: T) -> None:
        """Set the element at a specific index."""
        self._elements[index] = value

    def __add__(self, other: Vector[T] | np.ndarray) -> Vector[T]:
        """Add another vector to this one."""
        other_elements = other._elements if isinstance(other, Vector) else np.array(other)
        return Vector[T](self._elements + other_elements)

    def __sub__(self, other: Vector[T] | np.ndarray) -> Vector[T]:
        """Subtract another vector from this one."""
        other_elements = other._elements if isinstance(other, Vector) else np.array(other)
        return Vector[T](self._elements - other_elements)

    def __mul__(self, other: Vector | np.ndarray | float) -> np.ndarray:
        """Multipy this vector with either another vector or a scalar."""
        if isinstance(self._elements[0], _QuantityBase):
            self_to_numpy = self.to_numpy(self._elements[0].BASE_UNIT)
        else:
            self_to_numpy = self.to_numpy()
        return self_to_numpy * _other_to_numpy(other)

    def __truediv__(self, other: Vector | np.ndarray | float) -> np.ndarray:
        """Multipy this vector with either another vector or a scalar."""
        if isinstance(self._elements[0], _QuantityBase):
            self_to_numpy = self.to_numpy(self._elements[0].BASE_UNIT)
        else:
            self_to_numpy = self.to_numpy()
        return self_to_numpy / _other_to_numpy(other)

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if not isinstance(other, Vector):
            return False

        return np.all(other._elements == self._elements)


def _other_to_numpy(other: Vector | np.ndarray | float) -> np.ndarray:
    if isinstance(other, (float, int)):
        return np.array([other])

    if isinstance(other, _QuantityBase):
        return np.array([other._base_value])

    if isinstance(other, Vector):
        if isinstance(other._elements[0], _QuantityBase):
            return other.to_numpy(other._elements[0].BASE_UNIT)
        return other.to_numpy()

    if isinstance(other, np.ndarray):
        return other

    raise TypeError
