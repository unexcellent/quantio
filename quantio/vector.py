from __future__ import annotations

from typing import Generic, TypeVar

import numpy as np

from .exceptions import (
    CanNotAddTypesError,
    CanNotSubtractTypesError,
    EmptyVectorElementsError,
    NoUnitSpecifiedError,
)
from .quantities import Quantity

T = TypeVar("T")


class Vector(Generic[T]):
    """A 1 dimensional array of either quantity or numeric elements."""

    _elements: np.array[float]
    _quantitiy: type

    @property
    def elements(self) -> np.ndarray[T]:
        """Return the elements of the Vector as a numpy array."""
        return np.array([self._quantitiy(value) for value in self._elements])

    def __init__(self, elements: list | tuple | np.ndarray) -> None:
        if len(elements) == 0:
            raise EmptyVectorElementsError

        if isinstance(elements[0], Quantity):
            self._elements = np.array([getattr(element, element.BASE_UNIT) for element in elements])
        else:
            self._elements = np.array(elements)
        self._quantitiy = type(elements[0])

    @classmethod
    def arange(cls, start: T, stop: T, step: T) -> Vector[T]:
        """Return evenly spaced values within a given interval."""
        if isinstance(start, Quantity):
            start_val = start._base_value

            if not isinstance(stop, Quantity):
                raise TypeError
            stop_val = stop._base_value

            if not isinstance(step, Quantity):
                raise TypeError
            step_val = step._base_value

            element_type = type(start)
            return Vector(
                [element_type(value) for value in np.arange(start_val, stop_val, step_val)]
            )

        return Vector(np.arange(start, stop, step))

    @classmethod
    def tile(cls, element: T | Vector[T] | list[T], length: int) -> Vector[T]:
        """Construct a Vector by repeating an element a certain number of times."""
        if isinstance(element, Vector):
            return Vector(np.tile(element._elements, length))

        return Vector(np.tile(element, length))

    @classmethod
    def from_numpy(
        cls, array: np.ndarray, element_class: type[Quantity], unit: str
    ) -> Vector[Quantity]:
        """Construct a quantity vector from a numpy array."""
        vector: Vector[Quantity] = Vector([0])

        if unit == element_class.BASE_UNIT:
            vector._elements = array
        else:
            conversion_factor = getattr(element_class(1), unit)
            vector._elements = array / conversion_factor

        vector._quantitiy = element_class
        return vector

    def to_numpy(self, unit: str | None = None) -> np.ndarray[float]:
        """Convert this vector into a numpy array of floats."""
        if not isinstance(self.elements[0], Quantity):
            return self._elements

        if unit is None:
            raise NoUnitSpecifiedError

        if unit == self._quantitiy.BASE_UNIT:  # type: ignore
            return self._elements

        return np.array([getattr(element, unit) for element in self.elements])

    def sum(self) -> T:
        """Return a sum of all elements of this array."""
        return self._quantitiy(np.sum(self._elements))

    @classmethod
    def __class_getitem__(cls, *_: object) -> type:
        """Return this class for type hinting."""
        return cls

    def __getitem__(self, index: int) -> T:
        """Return the element at a specific index."""
        return self._quantitiy(self._elements[index])

    def __setitem__(self, index: int, value: T) -> None:
        """Set the element at a specific index."""
        if isinstance(value, Quantity):
            self._elements[index] = getattr(value, value.BASE_UNIT)
        else:
            self._elements[index] = value

    def __add__(self, other: Vector[T] | np.ndarray) -> Vector[T]:
        """Add another vector to this one."""
        if not isinstance(other[0], self._quantitiy):
            raise CanNotAddTypesError(self[0].__class__.__name__, other[0].__class__.__name__)
        other_elements = other.elements if isinstance(other, Vector) else np.array(other)
        return Vector[T](self.elements + other_elements)

    def __sub__(self, other: Vector[T] | np.ndarray) -> Vector[T]:
        """Subtract another vector from this one."""
        if not isinstance(other[0], self._quantitiy):
            raise CanNotSubtractTypesError(self[0].__class__.__name__, other[0].__class__.__name__)
        other_elements = other.elements if isinstance(other, Vector) else np.array(other)
        return Vector[T](self.elements - other_elements)

    def __mul__(self, other: Vector | np.ndarray | float) -> np.ndarray:
        """Multiply this vector with either another vector or a scalar."""
        if isinstance(self[0], Quantity):
            self_to_numpy = self.to_numpy(self[0].BASE_UNIT)
        else:
            self_to_numpy = self.to_numpy()
        return self_to_numpy * _other_to_numpy(other)

    def __truediv__(self, other: Vector | np.ndarray | float) -> np.ndarray:
        """Multipy this vector with either another vector or a scalar."""
        if isinstance(self[0], Quantity):
            self_to_numpy = self.to_numpy(self[0].BASE_UNIT)
        else:
            self_to_numpy = self.to_numpy()
        return self_to_numpy / _other_to_numpy(other)

    def __eq__(self, other: object) -> bool:
        """Assess if this object is the same as another."""
        if not isinstance(other, Vector):
            return False

        try:
            return np.all(other._elements == self._elements)
        except ValueError:
            return False

    def __len__(self) -> int:
        """Return the number of elements in this vector."""
        return self._elements.__len__()

    def __str__(self) -> str:
        """Display this vector as a string for printing."""
        elements_str = ""
        for element in self.elements:
            elements_str += f"{element}, "
        elements_str = elements_str[:-2]
        return f"Vector([{elements_str}])"

    def __repr__(self) -> str:
        """Return an unambiguous representation of this vector."""
        return self.__str__()


def _other_to_numpy(other: Vector | np.ndarray | float) -> np.ndarray:
    if isinstance(other, (float, int)):
        return np.array([other])

    if isinstance(other, Quantity):
        return np.array([other._base_value])

    if isinstance(other, Vector):
        if isinstance(other[0], Quantity):
            return other.to_numpy(other[0].BASE_UNIT)
        return other.to_numpy()

    if isinstance(other, np.ndarray):
        return other

    raise TypeError
