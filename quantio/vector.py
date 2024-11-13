from __future__ import annotations

from typing import Generic, TypeVar

import numpy as np

from ._quantity_base import _QuantityBase

T = TypeVar("T")


class Vector(Generic[T]):
    """An 1 dimensional array of either quantity or numeric elements."""

    _elements: np.array

    def __init__(self, elements: list | tuple | np.ndarray) -> None:
        self._elements = np.array(elements)

    def to_numpy(self) -> np.ndarray[float]:
        """Convert this vector into a numpy array of floats."""
        if len(self._elements) == 0:
            return np.array([])

        if isinstance(self._elements[0], _QuantityBase):
            return np.array([element._base_value for element in self._elements])

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
        return self.to_numpy() * _other_to_numpy(other)

    def __truediv__(self, other: Vector | np.ndarray | float) -> np.ndarray:
        """Multipy this vector with either another vector or a scalar."""
        return self.to_numpy() / _other_to_numpy(other)

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
        return other.to_numpy()

    if isinstance(other, np.ndarray):
        return other

    raise TypeError
