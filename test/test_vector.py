import pytest

import numpy as np

from quantio import (
    Vector,
    Length,
    Time,
    CanNotAddTypesError,
    CanNotSubtractTypesError,
    NoUnitSpecifiedError,
)


def test_init():
    vec: Vector[Length] = Vector([Length.zero(), Length.zero()])
    assert np.all(vec.elements == np.array([Length.zero(), Length.zero()]))


def test_init_with_type_hint():
    vec = Vector[Length]([Length.zero(), Length.zero()])
    assert np.all(vec.elements == np.array([Length.zero(), Length.zero()]))


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


def test_arange__float():
    actual = Vector[float].arange(start=0.0, stop=5.0, step=2)
    assert actual == Vector([0.0, 2.0, 4.0])


def test_arange__quantity():
    actual = Vector[Length].arange(
        start=Length(meters=0), stop=Length(meters=5), step=Length(meters=2)
    )
    assert actual == Vector([Length(meters=0), Length(meters=2), Length(meters=4)])


def test_arange__false_type_combination():
    with pytest.raises(TypeError):
        Vector.arange(start=Length(meters=0), stop=Time(meters=5), step=Length(meters=2))


def test_len():
    vec = Vector[float]([0, 0, 0, 0])
    assert len(vec) == 4


def test_tile__floats():
    actual = Vector.tile(0, 5)
    assert actual == Vector([0, 0, 0, 0, 0])


def test_tile__quantities():
    actual = Vector.tile(Length.zero(), 3)
    assert actual == Vector([Length.zero(), Length.zero(), Length.zero()])


def test_tile__elements_are_independent():
    actual = Vector.tile(Length(meters=1), 2)
    actual[0] = Length(meters=2)
    assert actual == Vector([Length(meters=2), Length(meters=1)])


def test_tile__vector():
    actual = Vector[float].tile(Vector([0, 1, 2]), 2)
    assert actual == Vector([0, 1, 2, 0, 1, 2])


def test_tile__list():
    actual = Vector[float].tile([0, 1, 2], 2)
    assert actual == Vector([0, 1, 2, 0, 1, 2])


def test_sum__float():
    actual = Vector[float]([0, 1, 2, 3]).sum()
    assert actual == 6


def test_sum__quantity():
    actual = Vector[Length](
        [Length(meters=0), Length(meters=1), Length(meters=2), Length(meters=3)]
    ).sum()
    assert actual == Length(meters=6)


def test_from_numpy__quantity():
    array = np.array([0, 1, 2])
    actual = Vector[Length].from_numpy(array, Length, "meters")
    assert actual == Vector([Length(meters=0), Length(meters=1), Length(meters=2)])


def test_str__float():
    actual = str(Vector[float]([0.0, 1.0]))
    assert actual == "Vector([0.0, 1.0])"


def test_str__quantity():
    actual = str(Vector[Time]([Time(seconds=1.0), Time(seconds=1.0)]))
    assert actual == "Vector([Time(seconds=1.0), Time(seconds=1.0)])"


def test_repr__float():
    vector = Vector[float]([0.0, 1.0])
    assert vector.__str__() == vector.__repr__()


def test_repr__quantity():
    vector = Vector[Time]([Time(seconds=1.0), Time(seconds=1.0)])
    assert vector.__str__() == vector.__repr__()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
