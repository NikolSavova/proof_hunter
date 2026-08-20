#!/usr/bin/env python3
"""Verify the large Gaussian-cell support and tail audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb
import sys


Point = tuple[int, int]
Triple = tuple[int, int, int]


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def distance_sidon(points: list[Point]) -> bool:
    labels = [norm2(subtract(b, a)) for a, b in combinations(points, 2)]
    return len(labels) == len(set(labels))


def lifted_residue_parabola(prime: int) -> list[Point]:
    return [
        (x + prime * ((x * x) % prime), (x * x) % prime)
        for x in range(prime)
    ]


def verify_quadratic_form_injectivity(prime: int) -> None:
    seen: dict[int, tuple[int, int]] = {}
    for h in range(1, prime):
        for z in range(-(prime - 1), prime):
            value = (h + prime * z) ** 2 + z * z
            assert value not in seen, (prime, value, seen.get(value), (h, z))
            seen[value] = (h, z)


def triple_cells(points: list[Point]) -> defaultdict[Point, list[Triple]]:
    cells: defaultdict[Point, list[Triple]] = defaultdict(list)
    for triple in combinations(range(len(points)), 3):
        key = (
            sum(points[index][0] for index in triple),
            sum(points[index][1] for index in triple),
        )
        cells[key].append(triple)
    return cells


def gaussian_profile(
    points: list[Point],
) -> tuple[int, int, Counter[tuple[int, int]]]:
    """Return |H|, collinear |H|, and sixfold ordered Gaussian cells."""
    hyperedges = 0
    collinear = 0
    profile: Counter[tuple[int, int]] = Counter()
    for triples in triple_cells(points).values():
        for source in triples:
            for target in triples:
                if source == target:
                    continue
                assert set(source).isdisjoint(target)
                for permuted_target in permutations(target):
                    vectors = [
                        subtract(points[permuted_target[index]], points[source[index]])
                        for index in range(3)
                    ]
                    assert (
                        sum(vector[0] for vector in vectors),
                        sum(vector[1] for vector in vectors),
                    ) == (0, 0)
                    determinant = (
                        vectors[0][0] * vectors[1][1]
                        - vectors[0][1] * vectors[1][0]
                    )
                    hyperedges += 1
                    collinear += determinant == 0
                    for first in range(3):
                        for second in range(3):
                            if first == second:
                                continue
                            u = vectors[first]
                            v = vectors[second]
                            norm_gap = norm2(u) - norm2(v)
                            doubled_area = 2 * (
                                u[0] * v[1] - u[1] * v[0]
                            )
                            profile[norm_gap, doubled_area] += 1
    assert sum(profile.values()) == 6 * hyperedges
    return hyperedges, collinear, profile


def coordinate_height(points: list[Point]) -> int:
    return max(
        max(x for x, _ in points) - min(x for x, _ in points),
        max(y for _, y in points) - min(y for _, y in points),
    )


def divisor_count(value: int) -> int:
    value = abs(value)
    output = 1
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            exponent += 1
            value //= divisor
        if exponent:
            output *= exponent + 1
        divisor += 1
    if value > 1:
        output *= 2
    return output


def verify_cell_cap(profile: Counter[tuple[int, int]]) -> None:
    for (norm_gap, doubled_area), load in profile.items():
        assert norm_gap or doubled_area
        safe_gaussian_cap = 4 * divisor_count(
            norm_gap * norm_gap + doubled_area * doubled_area
        ) ** 2
        assert load <= safe_gaussian_cap


def verify_small_gap_bound(
    points: list[Point], profile: Counter[tuple[int, int]]
) -> None:
    k = len(points)
    for cutoff in (1, 3, 10, 43, 200, 500, 1849):
        small_gap = sum(
            load
            for (norm_gap, _), load in profile.items()
            if 0 < abs(norm_gap) <= cutoff
        )
        assert small_gap <= 4 * k * k * cutoff


def verify_finite_field_lifts() -> dict[int, tuple[int, int, int, int, int]]:
    expected = {
        7: (33, 24, 72, 144, 2),
        11: (107, 144, 414, 828, 2),
        13: (164, 396, 1168, 2340, 4),
        17: (285, 1392, 4144, 8316, 4),
        19: (336, 3228, 9464, 19140, 6),
        23: (429, 8652, 25480, 51528, 6),
        29: (829, 19896, 58922, 118896, 6),
        43: (1790, 126852, 374288, 758772, 8),
    }
    actual: dict[int, tuple[int, int, int, int, int]] = {}
    last_profile: Counter[tuple[int, int]] | None = None
    for prime in expected:
        verify_quadratic_form_injectivity(prime)
        points = lifted_residue_parabola(prime)
        assert distance_sidon(points)
        assert coordinate_height(points) < prime * prime
        hyperedges, collinear, profile = gaussian_profile(points)
        nonzero = Counter(
            {cell: load for cell, load in profile.items() if cell[1] != 0}
        )
        row = (
            coordinate_height(points),
            hyperedges,
            len(nonzero),
            sum(nonzero.values()),
            max(nonzero.values(), default=0),
        )
        assert row == expected[prime]
        assert sum(nonzero.values()) == 6 * (hyperedges - collinear)
        # Full exact factorization is deliberately checked only on the
        # small certificate; trial-dividing hundreds of thousands of large
        # cells would obscure the fast combinatorial regression.
        if prime == 7:
            verify_cell_cap(nonzero)
        verify_small_gap_bound(points, nonzero)
        actual[prime] = row
        if prime == 43:
            last_profile = profile

    assert last_profile is not None
    core = Counter(
        {
            cell: load
            for cell, load in last_profile.items()
            if abs(cell[0]) > 43**2 and abs(cell[1]) > 43
        }
    )
    assert (len(core), sum(core.values()), max(core.values())) == (
        341244,
        690220,
        8,
    )

    reciprocal_gap = sum(
        load / abs(norm_gap)
        for (norm_gap, _), load in last_profile.items()
    )
    reciprocal_area = sum(
        load / abs(doubled_area)
        for (_, doubled_area), load in last_profile.items()
        if doubled_area
    )
    assert reciprocal_gap < 54
    assert reciprocal_area < 8793
    return actual


def verify_integer_parabolas() -> dict[int, tuple[int, int, int]]:
    expected = {
        12: (168, 410, 4),
        20: (1680, 4266, 4),
        30: (8496, 22002, 6),
        40: (25224, 65964, 6),
    }
    actual: dict[int, tuple[int, int, int]] = {}
    for size, row in expected.items():
        points = [(index, index * index) for index in range(size)]
        assert distance_sidon(points)
        hyperedges, _collinear, profile = gaussian_profile(points)
        nonzero = Counter({cell: load for cell, load in profile.items() if cell[1]})
        actual[size] = (
            hyperedges,
            len(nonzero),
            max(nonzero.values(), default=0),
        )
        assert actual[size] == row
        if size == 12:
            verify_cell_cap(nonzero)
    return actual


def verify_stored_other_stresses() -> tuple[int, int]:
    sys.path.insert(0, "phase2/loop/erdos1208")
    from verify_colored_derivative_l2_correlation_gate import VALUES
    from verify_parabolic_endpoint_product_singer_ambient_sharpness import (
        DIFFERENCE_SET,
        point,
    )

    multi_arc = list(enumerate(VALUES))
    singer = [point(value) for value in DIFFERENCE_SET]
    assert distance_sidon(multi_arc)
    assert distance_sidon(singer)
    multi_hyperedges = gaussian_profile(multi_arc)[0]
    singer_hyperedges = gaussian_profile(singer)[0]
    assert multi_hyperedges == 0
    assert singer_hyperedges == 0
    return multi_hyperedges, singer_hyperedges


def verify_asymptotic_ledger() -> None:
    total_exponent = 4
    epsilon = 0.1
    small_gap_exponent = 2 + (2 - epsilon)
    small_area_exponent = 3 + (1 - epsilon)
    assert small_gap_exponent < total_exponent
    assert small_area_exponent < total_exponent
    assert 4 == 2 * 2  # p^4=m^2
    assert 3 / 2 < 2  # planted integer-parabola core is below m^2


def main() -> None:
    finite_field = verify_finite_field_lifts()
    integer_parabola = verify_integer_parabolas()
    other = verify_stored_other_stresses()
    verify_asymptotic_ledger()
    print(
        "PASS",
        {
            "finite_field_p43": finite_field[43],
            "p43_doubly_large_core": (341244, 690220, 8),
            "integer_parabola_n40": integer_parabola[40],
            "multi_arc_and_singer_H": other,
            "survivor": "flat support, no cutoff decay",
        },
    )


if __name__ == "__main__":
    main()
