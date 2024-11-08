import pytest

from quantio import Length, CanNotAddTypesError, CanNotSubtractTypesError


def test_miles():
    actual = Length(meters=1)
    assert actual.miles == 1 / 1609.34


def test_kilometers():
    actual = Length(kilometers=1)
    assert actual.kilometers == 1


def test_meters():
    actual = Length(meters=1)
    assert actual.meters == 1


def test_feet():
    actual = Length(feet=1)
    assert actual.feet == 1


def test_inches():
    actual = Length(inches=1)
    assert actual.inches == 1


def test_centimeters():
    actual = Length(centimeters=1)
    assert actual.centimeters == 1


def test_millimeters():
    actual = Length(millimeters=1)
    assert actual.millimeters == 1


def test_micrometers():
    actual = Length(micrometers=1)
    assert actual.micrometers == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
