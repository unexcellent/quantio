import pytest

from quantio import Length


def test_construction__multiple_units():
    actual = Length(meters=5, kilometers=1, centimeters=7)
    assert actual.meters == 1005.07


def test_kilometers():
    actual = Length(meters=1)
    assert actual.kilometers == 10**-3


def test_meters():
    actual = Length(meters=1)
    assert actual.meters == 1


def test_centimeters():
    actual = Length(meters=1)
    assert actual.centimeters == 10**2


def test_millimeters():
    actual = Length(meters=1)
    assert actual.millimeters == 10**3


def test_micrometers():
    actual = Length(meters=1)
    assert actual.micrometers == 10**6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
