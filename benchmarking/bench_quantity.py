import pytest

from quantio import Time


def init_only_base_unit():
    Time(seconds=1, milliseconds=1)


def bench_init(benchmark):
    benchmark.pedantic(init_only_base_unit, iterations=100, rounds=100)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
