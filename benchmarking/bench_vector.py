import pytest
import numpy as np

from quantio import Length, Vector


def bench_from_numpy__base_unit(benchmark):
    f = lambda: Vector.from_numpy(np.ones(100), Length, "meters")
    benchmark.pedantic(f, iterations=100, rounds=100)


def bench_from_numpy__other_unit(benchmark):
    f = lambda: Vector.from_numpy(np.ones(100), Length, "centimeters")
    benchmark.pedantic(f, iterations=100, rounds=100)


def bench_to_numpy__base_unit(benchmark):
    vector = Vector.from_numpy(np.ones(100), Length, "meters")
    f = lambda: vector.to_numpy("meters")
    benchmark.pedantic(f, iterations=100, rounds=100)


def bench_to_numpy__other_unit(benchmark):
    vector = Vector.from_numpy(np.ones(100), Length, "meters")
    f = lambda: vector.to_numpy("centimeters")
    benchmark.pedantic(f, iterations=100, rounds=100)


def bench_add(benchmark):
    vector1 = Vector.from_numpy(np.ones(100), Length, "meters")
    vector2 = Vector.from_numpy(np.ones(100), Length, "meters")
    f = lambda: vector1 + vector2
    benchmark.pedantic(f, iterations=100, rounds=100)


def bench_sub(benchmark):
    vector1 = Vector.from_numpy(np.ones(100), Length, "meters")
    vector2 = Vector.from_numpy(np.ones(100), Length, "meters")
    f = lambda: vector1 - vector2
    benchmark.pedantic(f, iterations=100, rounds=100)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
