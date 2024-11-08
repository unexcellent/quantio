import pytest

from quantio import Length, CanNotAddTypesError, CanNotSubtractTypesError


def test_construction__multiple_units():
    actual = Length(meters=5, kilometers=1, centimeters=7)
    assert actual.meters == 1005.07


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


def test_add__success():
    length1 = Length(meters=1)
    length2 = Length(meters=2)

    actual = length1 + length2
    assert actual == Length(meters=3)


def test_add__false_class():
    length = Length(meters=1)

    with pytest.raises(CanNotAddTypesError):
        length += 1


def test_sub__success():
    length1 = Length(meters=1)
    length2 = Length(meters=2)

    actual = length2 - length1
    assert actual == Length(meters=1)


def test_sub__false_class():
    length = Length(meters=1)

    with pytest.raises(CanNotSubtractTypesError):
        length -= 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
