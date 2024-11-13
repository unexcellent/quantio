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
