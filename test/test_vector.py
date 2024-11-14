import pytest

import numpy as np

from quantio import (
    Vector,
    Length,
    CanNotAddTypesError,
    CanNotSubtractTypesError,
    NoUnitSpecifiedError,
)


def test_init():
    vec: Vector[Length] = Vector([Length.zero(), Length.zero()])
    assert np.all(vec._elements == np.array([Length.zero(), Length.zero()]))


def test_init_with_type_hint():
    vec = Vector[Length]([Length.zero(), Length.zero()])
    assert np.all(vec._elements == np.array([Length.zero(), Length.zero()]))


def test_indexing():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    assert vec[0] == Length(meters=1)


def test_set_item():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec[0] = Length(meters=3)

    assert vec[0] == Length(meters=3)


def test_addition():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])

    actual = vec1 + vec2
    assert actual == Vector([Length(meters=4), Length(meters=6)])


def test_addition__wrong_type():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[float] = Vector([3, 4])

    with pytest.raises(CanNotAddTypesError):
        vec1 + vec2


def test_subtract():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=3)])

    actual = vec2 - vec1
    assert actual == Vector([Length(meters=2), Length(meters=1)])


def test_subtract__wrong_type():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[float] = Vector([3, 4])

    with pytest.raises(CanNotSubtractTypesError):
        vec1 - vec2


def test_multiply__with_vector_of_quantities():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])

    actual = vec2 * vec1
    assert np.all(actual == np.array([3, 8]))


def test_multiply__with_vector_of_float():
    vec1: Vector[float] = Vector([1, 2])
    vec2: Vector[float] = Vector([3, 4])

    actual = vec2 * vec1
    assert np.all(actual == np.array([3, 8]))


def test_multiply__with_array():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    array = np.array([3, 4])

    actual = vec * array
    assert np.all(actual == np.array([3, 8]))


def test_multiply__with_scalar_float():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    scalar = 5

    actual = vec * scalar
    assert np.all(actual == np.array([5, 10]))


def test_multiply__with_scalar_quantitiy():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    scalar = Length(meters=5)

    actual = vec * scalar
    assert np.all(actual == np.array([5, 10]))


def test_multiply__wrong_dimension():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])

    with pytest.raises(ValueError):
        vec1 * vec2


def test_divide__with_vector_of_quantities():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])

    actual = vec2 / vec1
    assert np.all(actual == np.array([3, 2]))


def test_divide__with_vector_of_float():
    vec1: Vector[float] = Vector([1, 2])
    vec2: Vector[float] = Vector([3, 4])

    actual = vec2 / vec1
    assert np.all(actual == np.array([3, 2]))


def test_divide__with_array():
    vec: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])
    array = np.array([1, 2])

    actual = vec / array
    assert np.all(actual == np.array([3, 2]))


def test_divide__with_scalar_float():
    vec: Vector[Length] = Vector([Length(meters=2), Length(meters=4)])
    scalar = 2

    actual = vec / scalar
    assert np.all(actual == np.array([1, 2]))


def test_divide__with_scalar_quantitiy():
    vec: Vector[Length] = Vector([Length(meters=2), Length(meters=4)])
    scalar = Length(meters=2)

    actual = vec / scalar
    assert np.all(actual == np.array([1, 2]))


def test_divide__wrong_dimension():
    vec1: Vector[Length] = Vector([Length(meters=1), Length(meters=2), Length(meters=2)])
    vec2: Vector[Length] = Vector([Length(meters=3), Length(meters=4)])

    with pytest.raises(ValueError):
        vec1 / vec2


def test_to_numpy__floats():
    vec: Vector[float] = Vector([0.0, 1.0])

    actual = vec.to_numpy()
    assert np.all(actual == np.array([0.0, 1.0]))


def test_to_numpy__quantity():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2), Length(meters=3)])

    actual = vec.to_numpy("centimeters")
    assert np.all(actual == np.array([100.0, 200.0, 300.0]))


def test_to_numpy__quantity_no_unit():
    vec: Vector[Length] = Vector([Length(meters=1), Length(meters=2), Length(meters=3)])

    with pytest.raises(NoUnitSpecifiedError):
        vec.to_numpy()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
