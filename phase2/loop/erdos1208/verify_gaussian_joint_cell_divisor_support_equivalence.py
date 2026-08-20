#!/usr/bin/env python3
"""Verify the Gaussian joint-cell divisor and support-equivalence theorem."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, isqrt


Point = tuple[int, int]
VectorTriple = tuple[Point, Point, Point]


def add(*vectors: Point) -> Point:
    return (sum(v[0] for v in vectors), sum(v[1] for v in vectors))


def sub(first: Point, second: Point) -> Point:
    return (first[0] - second[0], first[1] - second[1])


def norm2(vector: Point) -> int:
    return vector[0] ** 2 + vector[1] ** 2


def det(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def gaussian_product_conjugate(first: Point, second: Point) -> Point:
    # (a+bi)(c-di)=(ac+bd)+i(bc-ad).
    return (
        first[0] * second[0] + first[1] * second[1],
        first[1] * second[0] - first[0] * second[1],
    )


def gaussian_divides(divisor: Point, value: Point) -> bool:
    denominator = norm2(divisor)
    if denominator == 0:
        return False
    real_numerator = value[0] * divisor[0] + value[1] * divisor[1]
    imag_numerator = value[1] * divisor[0] - value[0] * divisor[1]
    return (
        real_numerator % denominator == 0
        and imag_numerator % denominator == 0
    )


def gaussian_quotient(value: Point, divisor: Point) -> Point:
    assert gaussian_divides(divisor, value)
    denominator = norm2(divisor)
    return (
        (value[0] * divisor[0] + value[1] * divisor[1]) // denominator,
        (value[1] * divisor[0] - value[0] * divisor[1]) // denominator,
    )


def tau(number: int) -> int:
    assert number >= 1
    result = 1
    prime = 2
    remaining = number
    while prime * prime <= remaining:
        if remaining % prime:
            prime += 1
            continue
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        result *= exponent + 1
        prime += 1
    if remaining > 1:
        result *= 2
    return result


def residue_parabola(prime: int) -> list[Point]:
    return [(value, value * value % prime) for value in range(prime)]


def shear(points: list[Point], amount: int) -> list[Point]:
    return [(x + amount * y, y) for x, y in points]


def distance_sidon(points: list[Point]) -> bool:
    distances = [
        norm2(sub(points[second], points[first]))
        for first, second in combinations(range(len(points)), 2)
    ]
    return len(distances) == len(set(distances))


def triple_cells(points: list[Point]) -> defaultdict[Point, list[tuple[int, int, int]]]:
    cells: defaultdict[Point, list[tuple[int, int, int]]] = defaultdict(list)
    for triple in combinations(range(len(points)), 3):
        total = add(*(points[index] for index in triple))
        cells[total].append(triple)
    return cells


def base_hyperedge_vector_triples(points: list[Point]) -> list[VectorTriple]:
    triples: list[VectorTriple] = []
    for centroid_cell in triple_cells(points).values():
        for source in centroid_cell:
            for target in centroid_cell:
                if source == target:
                    continue
                assert set(source).isdisjoint(target)
                for permuted_target in permutations(target):
                    vectors = tuple(
                        sub(points[permuted_target[index]], points[source[index]])
                        for index in range(3)
                    )
                    assert add(*vectors) == (0, 0)
                    triples.append(vectors)  # type: ignore[arg-type]
    assert len(triples) == len(set(triples))
    return triples


def joint_cell(vectors: VectorTriple) -> Point:
    first, second, third = vectors
    difference = sub(second, third)
    value = gaussian_product_conjugate(first, difference)
    signed_area = det(first, second)
    assert value == (norm2(third) - norm2(second), -2 * signed_area)
    assert value != (0, 0)
    return value


def ordered_cell_profile(
    base_triples: list[VectorTriple],
) -> tuple[Counter[Point], defaultdict[Point, set[Point]]]:
    profile: Counter[Point] = Counter()
    first_factors: defaultdict[Point, set[Point]] = defaultdict(set)
    for base in base_triples:
        for order in permutations(range(3)):
            vectors = tuple(base[index] for index in order)
            value = joint_cell(vectors)  # type: ignore[arg-type]
            first = vectors[0]
            assert gaussian_divides(first, value)
            quotient = gaussian_quotient(value, first)
            # quotient is conjugate(w), so conjugate once more.
            difference = (quotient[0], -quotient[1])
            recovered_second = (
                (difference[0] - first[0]) // 2,
                (difference[1] - first[1]) // 2,
            )
            recovered_third = (
                (-difference[0] - first[0]) // 2,
                (-difference[1] - first[1]) // 2,
            )
            assert all(
                component % 2 == 0
                for component in (
                    difference[0] - first[0],
                    difference[1] - first[1],
                    -difference[0] - first[0],
                    -difference[1] - first[1],
                )
            )
            assert recovered_second == vectors[1]
            assert recovered_third == vectors[2]
            assert first not in first_factors[value]
            first_factors[value].add(first)
            profile[value] += 1
    for value, load in profile.items():
        assert load == len(first_factors[value])
        assert load % 2 == 0
    return profile, first_factors


def coordinate_height(points: list[Point]) -> int:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def check_projection_envelopes(profile: Counter[Point], height: int) -> None:
    by_imaginary: defaultdict[int, set[int]] = defaultdict(set)
    by_real: defaultdict[int, set[int]] = defaultdict(set)
    for real, imaginary in profile:
        by_imaginary[imaginary].add(real)
        by_real[real].add(imaginary)
    assert all(len(values) <= 4 * height * height + 1 for values in by_imaginary.values())
    assert all(len(values) <= 4 * height * height + 1 for values in by_real.values())
    assert len(profile) == sum(len(values) for values in by_imaginary.values())
    assert len(profile) == sum(len(values) for values in by_real.values())


def check_small_certificate() -> None:
    points = shear(residue_parabola(7), 4)
    assert distance_sidon(points)
    base = base_hyperedge_vector_triples(points)
    assert len(base) == 24
    profile, first_factors = ordered_cell_profile(base)
    assert sum(profile.values()) == 6 * len(base) == 144
    assert 2 * len(profile) <= sum(profile.values())
    height = coordinate_height(points)
    for value, load in profile.items():
        gaussian_norm = norm2(value)
        assert gaussian_norm <= 16 * height**4
        assert load <= 4 * tau(gaussian_norm) ** 2
        assert all(gaussian_divides(factor, value) for factor in first_factors[value])
    check_projection_envelopes(profile, height)


def check_parabola_43_stress() -> None:
    points = shear(residue_parabola(43), 28)
    assert distance_sidon(points)
    assert coordinate_height(points) == 1175
    base = base_hyperedge_vector_triples(points)
    assert len(base) == 126852
    profile, _first_factors = ordered_cell_profile(base)
    histogram = Counter(profile.values())
    assert sum(profile.values()) == 761112
    assert len(profile) == 375096
    assert max(profile.values()) == 8
    assert histogram == Counter({2: 369934, 4: 4886, 6: 254, 8: 22})

    nonzero = {value: load for value, load in profile.items() if value[1] != 0}
    assert sum(nonzero.values()) == 758772
    assert len(nonzero) == 374220
    tail = {value: load for value, load in profile.items() if abs(value[1]) > 20}
    assert sum(tail.values()) == 727104
    assert len(tail) == 358868
    assert max(tail.values()) == 8
    check_projection_envelopes(profile, coordinate_height(points))


def main() -> None:
    check_small_certificate()
    check_parabola_43_stress()
    print(
        "PASS",
        {
            "p43_hyperedges": 126852,
            "ordered_records": 761112,
            "joint_support": 375096,
            "cell_histogram": {2: 369934, 4: 4886, 6: 254, 8: 22},
            "nonzero_area": (758772, 374220),
            "abs_det_gt_10": (727104, 358868),
            "height": 1175,
        },
    )


if __name__ == "__main__":
    main()
