import pytest

from quantio import Time


def bench_init(benchmark):
    f = lambda: Time(seconds=1, milliseconds=1)
    benchmark.pedantic(f, iterations=100, rounds=100)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
