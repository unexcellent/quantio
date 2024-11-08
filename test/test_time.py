import pytest

from quantio import Time


def test_hours():
    time = Time(hours=1)
    assert time.hours == 1


def test_minutes():
    time = Time(minutes=1)
    assert time.minutes == 1


def test_seconds():
    time = Time(seconds=1)
    assert time.seconds == 1


def test_milliseconds():
    time = Time(milliseconds=1)
    assert time.milliseconds == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
