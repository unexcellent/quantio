import pytest

import numpy as np

from quantio import Vector, Length


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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
