import pytest

from quantio import Length


def test_construction():
    actual = Length(meters=5)
    assert actual.meters == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
