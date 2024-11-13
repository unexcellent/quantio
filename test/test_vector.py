import pytest

import numpy as np

from quantio import Vector, Length, CanNotAddTypesError, CanNotSubtractTypesError


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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
