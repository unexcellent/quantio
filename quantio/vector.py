from __future__ import annotations

from typing import Generic, TypeVar

import numpy as np

T = TypeVar("T")


class Vector(Generic[T]):
    """A vector of either quanity or numeric elements."""

    _elements: np.array

    def __init__(self, elements: list | tuple | np.ndarray) -> None:
        self._elements = np.array(elements)

    @classmethod
    def __class_getitem__(cls, *_: object) -> type:
        """Return this class for type hinting."""
        return cls
