import pytest

from quantio import Length


def test_str():
    actual = str(Length(meters=1.0))
    assert actual == "Length(meters=1.0)"


def test_repr():
    length = Length(meters=1.0)
    assert length.__str__() == length.__repr__()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
