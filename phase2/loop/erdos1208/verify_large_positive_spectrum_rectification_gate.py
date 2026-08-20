#!/usr/bin/env python3
"""Regression checks for LARGE_POSITIVE_SPECTRUM_RECTIFICATION_GATE.md.

The additive and finite-group checks are exact.  Complex Fourier sums are
used only as an independent numerical audit of the exact counting identities.
"""

from __future__ import annotations

import cmath
import math
import random
from collections import Counter
from itertools import product


Point = tuple[int, int]


def add(*points: Point) -> Point:
    return sum(point[0] for point in points), sum(point[1] for point in points)


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def third_representations(points: list[Point]) -> Counter[Point]:
    return Counter(add(first, second, third) for first in points for second in points for third in points)


def third_energy(points: list[Point]) -> int:
    return sum(load * load for load in third_representations(points).values())


def oriented_differences(points: list[Point]) -> Counter[Point]:
    return Counter(
        subtract(first, second)
        for first in points
        for second in points
        if first != second
    )


def assert_vector_sidon(points: list[Point]) -> set[Point]:
    differences = oriented_differences(points)
    assert len(differences) == len(points) * (len(points) - 1)
    assert set(differences.values()) == {1}
    return set(differences)


def assert_distance_sidon(points: list[Point]) -> None:
    squared_distances: set[int] = set()
    for first_index, first in enumerate(points):
        for second in points[first_index + 1 :]:
            difference = subtract(first, second)
            value = difference[0] ** 2 + difference[1] ** 2
            assert value not in squared_distances
            squared_distances.add(value)
    assert len(squared_distances) == len(points) * (len(points) - 1) // 2


def schur_triples(differences: set[Point]) -> int:
    return sum(
        (-first[0] - second[0], -first[1] - second[1]) in differences
        for first in differences
        for second in differences
    )


def exact_complete_difference_audit(points: list[Point]) -> tuple[int, int]:
    differences = assert_vector_sidon(points)
    k = len(points)
    assert len(differences) == k * (k - 1)

    # The first and second moments of S are coefficient counts.  Symmetry
    # makes every d pair with -d exactly once in the second moment.
    assert all((-difference[0], -difference[1]) in differences for difference in differences)
    second_moment = sum(
        add(first, second) == (0, 0)
        for first in differences
        for second in differences
    )
    assert second_moment == k * (k - 1)

    triple_count = schur_triples(differences)
    energy = third_energy(points)
    assert energy == 4 * k**3 - 3 * k**2 + triple_count
    return energy, triple_count


def finite_torus_audit(points: list[Point], modulus: int) -> None:
    k = len(points)
    m = max(max(x for x, _ in points), max(y for _, y in points))
    assert min(min(x for x, _ in points), min(y for _, y in points)) >= 0
    assert modulus > 3 * m

    exact_representations = third_representations(points)
    modular_representations: Counter[Point] = Counter(
        (total[0] % modulus, total[1] % modulus)
        for total, load in exact_representations.items()
        for _ in range(load)
    )
    # The deliberately expanded counter above checks fibres, rather than
    # merely comparing the final energy.
    assert sorted(exact_representations.values()) == sorted(modular_representations.values())
    exact_energy = sum(load * load for load in exact_representations.values())
    assert sum(load * load for load in modular_representations.values()) == exact_energy

    differences = assert_vector_sidon(points)
    exact_triples = schur_triples(differences)
    modular_triples = sum(
        ((-first[0] - second[0]) % modulus, (-first[1] - second[1]) % modulus)
        in {(d[0] % modulus, d[1] % modulus) for d in differences}
        for first in differences
        for second in differences
    )
    assert modular_triples == exact_triples

    # Independent discrete-Fourier audit.
    sum_p3 = 0.0
    sum_s2 = 0.0
    sum_s3 = 0.0
    positive_tail = 0.0
    dyadic_weight = 0
    frequencies_by_level: Counter[int] = Counter()
    for xi, eta in product(range(modulus), repeat=2):
        fourier = sum(
            cmath.exp(-2j * math.pi * (xi * x + eta * y) / modulus)
            for x, y in points
        )
        p_value = abs(fourier) ** 2
        s_value = p_value - k
        assert -k - 1e-8 <= s_value <= k * (k - 1) + 1e-8
        sum_p3 += p_value**3
        sum_s2 += s_value**2
        sum_s3 += s_value**3
        if s_value > k + 1e-9:
            positive_tail += s_value**3
            level = 0
            while s_value > (2 ** (level + 1)) * k + 1e-8:
                level += 1
            assert 2**level * k < s_value + 1e-8
            frequencies_by_level[level] += 1

    group_size = modulus**2
    assert abs(sum_p3 / group_size - exact_energy) < 1e-6
    assert abs(sum_s2 / group_size - k * (k - 1)) < 1e-7
    assert abs(sum_s3 / group_size - exact_triples) < 1e-6
    assert abs(exact_triples - positive_tail / group_size) < k**3 + 1e-7

    for level, load in frequencies_by_level.items():
        # Exact fourth-moment/Markov benchmark (with harmless numerical
        # tolerance only at the strict band boundary).
        assert load * (2**level * k) ** 2 <= group_size * k * (k - 1) + 1e-7
        dyadic_weight += 2 ** (3 * level) * load
    lower = k**3 * dyadic_weight / group_size
    assert lower < positive_tail / group_size + 1e-6
    assert positive_tail / group_size <= 8 * lower + 1e-6


def parabola(prime: int) -> list[Point]:
    return [(x, x * x % prime) for x in range(prime)]


def base_encode(points: list[Point], base: int) -> list[int]:
    return [x + base * y for x, y in points]


def scalar_pair_representations(points: list[int]) -> Counter[int]:
    return Counter(first + second for first in points for second in points)


def scalar_third_representations(points: list[int]) -> Counter[int]:
    return Counter(first + second + third for first in points for second in points for third in points)


def assert_scalar_sidon(points: list[int]) -> None:
    differences = Counter(first - second for first in points for second in points if first != second)
    assert len(differences) == len(points) * (len(points) - 1)
    assert set(differences.values()) == {1}


def parabola_rectification_barrier(prime: int) -> tuple[int, int, int, int]:
    points = parabola(prime)
    assert_vector_sidon(points)
    m = prime - 1
    base = 3 * prime
    assert base > 3 * m
    encoded = base_encode(points, base)
    assert_scalar_sidon(encoded)

    vector_pairs = Counter(add(first, second) for first in points for second in points)
    scalar_pairs = scalar_pair_representations(encoded)
    assert sorted(vector_pairs.values()) == sorted(scalar_pairs.values())

    vector_triples = third_representations(points)
    scalar_triples = scalar_third_representations(encoded)
    assert sorted(vector_triples.values()) == sorted(scalar_triples.values())
    vector_energy = sum(load * load for load in vector_triples.values())
    scalar_energy = sum(load * load for load in scalar_triples.values())
    assert vector_energy == scalar_energy
    assert len(vector_triples) <= (3 * prime - 2) ** 2
    assert vector_energy * (3 * prime - 2) ** 2 >= prime**6
    assert vector_energy * 9 > prime**4

    interval_maximum = max(encoded)
    assert interval_maximum <= (3 * prime + 1) * (prime - 1)
    assert interval_maximum < 4 * prime**2
    # Polynomial failure of E_3=O(k^3+N); already visible at p=43.
    assert vector_energy > 3 * (prime**3 + interval_maximum)
    return prime, interval_maximum, len(vector_triples), vector_energy


def sampled_real_torus_audit(points: list[Point]) -> None:
    random.seed(1208)
    k = len(points)
    for _ in range(2_000):
        theta, phi = random.random(), random.random()
        fourier = sum(
            cmath.exp(2j * math.pi * (theta * x + phi * y))
            for x, y in points
        )
        s_value = abs(fourier) ** 2 - k
        assert -k - 1e-10 <= s_value <= k * (k - 1) + 1e-10
        if s_value <= k:
            assert abs(s_value**3) <= k * s_value**2 + 1e-10


def main() -> None:
    distance_example = [(0, 0), (1, 0), (0, 2), (3, 3)]
    assert_distance_sidon(distance_example)
    energy, triple_count = exact_complete_difference_audit(distance_example)
    assert (energy, triple_count) == (256, 48)
    finite_torus_audit(distance_example, modulus=11)
    sampled_real_torus_audit(distance_example)
    print("distance example", "E3", energy, "T(D*)", triple_count)

    barrier = parabola_rectification_barrier(43)
    assert barrier == (43, 5_316, 6_904, 1_306_561)
    print(
        "encoded parabola",
        barrier,
        "E3/(k^3+N)",
        barrier[3] / (barrier[0] ** 3 + barrier[1]),
    )
    print("all large-positive-spectrum/rectification checks passed")


if __name__ == "__main__":
    main()
