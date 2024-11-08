import pytest

from quantio import Length


def test_miles():
    length = Length(meters=1)
    assert length.miles == 1 / 1609.34


def test_kilometers():
    length = Length(kilometers=1)
    assert length.kilometers == 1


def test_meters():
    length = Length(meters=1)
    assert length.meters == 1


def test_feet():
    length = Length(feet=1)
    assert length.feet == 1


def test_inches():
    length = Length(inches=1)
    assert length.inches == 1


def test_centimeters():
    length = Length(centimeters=1)
    assert length.centimeters == 1


def test_millimeters():
    length = Length(millimeters=1)
    assert length.millimeters == 1


def test_micrometers():
    length = Length(micrometers=1)
    assert length.micrometers == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
