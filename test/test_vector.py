import pytest

import numpy as np

from quantio import Vector, Length


def test_init():
    actual: Vector[Length] = Vector([Length.zero(), Length.zero()])
    assert np.all(actual._elements == np.array([Length.zero(), Length.zero()]))


def test_init_with_type_hint():
    actual = Vector[Length]([Length.zero(), Length.zero()])
    assert np.all(actual._elements == np.array([Length.zero(), Length.zero()]))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
