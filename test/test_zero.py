import pytest

from quantio import Length


def test_zero():
    actual = Length.zero()
    assert actual == Length(meters=0)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
