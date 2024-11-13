from __future__ import annotations

from typing import Generic, TypeVar

import numpy as np

T = TypeVar("T")


class Vector(Generic[T]):
    """An 1 dimensional array of either quantity or numeric elements."""

    _elements: np.array

    def __init__(self, elements: list | tuple | np.ndarray) -> None:
        self._elements = np.array(elements)

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

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if not isinstance(other, Vector):
            return False

        return np.all(other._elements == self._elements)
