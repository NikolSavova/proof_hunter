#!/usr/bin/env python3
"""Exact checks for LARGE_DETERMINANT_PROJECTION_DYADIC_GATE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd, sqrt
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    centroid_matching_determinant_profile,
    primitive_unoriented,
    residue_parabola,
    shear,
    sub,
)

Point = tuple[int, int]
Direction = tuple[int, int]


def determinant(a: Point, b: Point) -> int:
    return a[0] * b[1] - a[1] * b[0]


def directed_differences(points: list[Point]) -> list[Point]:
    differences = [
        sub(points[j], points[i])
        for i in range(len(points))
        for j in range(len(points))
        if i != j
    ]
    assert len(differences) == len(set(differences))
    return differences


def active_direction_data(
    points: list[Point],
) -> tuple[Counter[Direction], dict[Direction, set[int]]]:
    occupancies: Counter[Direction] = Counter()
    contents: dict[Direction, set[int]] = {}
    for i, j in combinations(range(len(points)), 2):
        vector = sub(points[j], points[i])
        direction = primitive_unoriented(vector)
        content = gcd(abs(vector[0]), abs(vector[1]))
        occupancies[direction] += 1
        contents.setdefault(direction, set()).add(content)
    for direction, occupancy in occupancies.items():
        # Equal content in one primitive direction would repeat a directed
        # vector after orienting both edges consistently.
        assert len(contents[direction]) == occupancy
    return occupancies, contents


def projection_data(
    points: list[Point],
) -> tuple[
    int,
    Counter[Direction],
    dict[Direction, Counter[int]],
    dict[Direction, int],
]:
    differences = directed_differences(points)
    N = len(differences)
    occupancies, _ = active_direction_data(points)
    projections: dict[Direction, Counter[int]] = {}
    energies: dict[Direction, int] = {}

    for direction in occupancies:
        loads = Counter(determinant(direction, vector) for vector in differences)
        assert sum(loads.values()) == N

        # Endpoint convolution identity B_w(r).
        levels = Counter(determinant(direction, point) for point in points)
        convolution: Counter[int] = Counter()
        for source_level, source_load in levels.items():
            for target_level, target_load in levels.items():
                convolution[target_level - source_level] += source_load * target_load
        convolution[0] -= len(points)
        if convolution[0] == 0:
            del convolution[0]
        assert loads == convolution

        projections[direction] = loads
        energies[direction] = sum(load * load for load in loads.values())

    return N, occupancies, projections, energies


def check_global_projection_budget(points: list[Point]) -> tuple[int, int, float]:
    N, occupancies, projections, energies = projection_data(points)
    assert sum(occupancies.values()) * 2 == N
    assert len(occupancies) <= N // 2

    line_pair_total = 0
    for direction, loads in projections.items():
        line_pairs = sum(load * (load - 1) // 2 for load in loads.values())
        assert energies[direction] == N + 2 * line_pairs
        line_pair_total += line_pairs
    assert line_pair_total <= N * (N - 1) // 2

    energy_total = sum(energies.values())
    assert 2 * energy_total < 3 * N * N

    z_value = sum(
        sqrt(occupancies[direction] * energies[direction])
        for direction in occupancies
    )
    assert z_value < sqrt(3) * N ** 1.5 / 2

    # Endpoint Young bound E_w <= k^2(k+2e_w).
    k = len(points)
    for direction in occupancies:
        assert energies[direction] <= k * k * (
            k + 2 * occupancies[direction]
        )

    return N, energy_total, z_value


def alpha_energy(contents: set[int], D: int) -> int:
    loads: Counter[int] = Counter()
    for r in range(-2 * D, 2 * D + 1):
        loads[r] = sum(D <= content * abs(r) < 2 * D for content in contents)
    return sum(load * load for load in loads.values())


def exhaustive_multiplicative_interval_check() -> None:
    universe = range(1, 9)
    for mask in range(1, 1 << 8):
        contents = {value for bit, value in enumerate(universe) if mask & (1 << bit)}
        for D in range(1, 21):
            assert alpha_energy(contents, D) <= 8 * D * len(contents)


def dyadic_profile(profile: Counter[int]) -> dict[int, int]:
    result: dict[int, int] = {}
    D = 1
    maximum = max(profile)
    while D <= maximum:
        result[D] = sum(load for value, load in profile.items() if D <= value < 2 * D)
        D *= 2
    return result


def check_band_bounds(points: list[Point]) -> tuple[dict[int, int], int, int, float]:
    N, energy_total, z_value = check_global_projection_budget(points)
    determinant_profile = centroid_matching_determinant_profile(points)
    bands = dyadic_profile(determinant_profile)

    differences = directed_differences(points)
    ordered_pair_profile = Counter(
        abs(determinant(first, second))
        for first in differences
        for second in differences
    )
    _, contents = active_direction_data(points)
    _, _, projections, _ = projection_data(points)

    for D, hyperedges in bands.items():
        # Exact lattice-coset formula (1.4), checked against raw ordered
        # vector pairs, followed by the matching-hyperedge discard (1.5).
        direct_pair_count = sum(
            load
            for value, load in ordered_pair_profile.items()
            if D <= value < 2 * D
        )
        formula_pair_count = 2 * sum(
            projection_load
            for direction, projection_loads in projections.items()
            for residue, projection_load in projection_loads.items()
            for content in contents[direction]
            if D <= content * abs(residue) < 2 * D
        )
        assert direct_pair_count == formula_pair_count
        assert 6 * hyperedges <= direct_pair_count

        # Universal square form of
        # H_D <= sqrt(6D) N^(3/2) / 3.
        assert 3 * hyperedges * hyperedges <= 2 * D * N ** 3
        # Refined endpoint-weighted form.
        assert hyperedges <= (2 * sqrt(2 * D) / 3) * z_value + 1e-9

    fixed_max = max(
        load for determinant_value, load in determinant_profile.items()
        if determinant_value != 0
    )
    assert fixed_max <= sqrt(2) * z_value / 3 + 1e-9
    return bands, N, energy_total, z_value


def main() -> None:
    exhaustive_multiplicative_interval_check()

    small = shear(residue_parabola(7), 4)
    small_bands, small_N, small_energy, small_z = check_band_bounds(small)
    assert small_bands == {1: 0, 2: 6, 4: 6, 8: 12}

    parabola = shear(residue_parabola(43), 28)
    bands, N, energy_total, z_value = check_band_bounds(parabola)
    expected_bands = {
        1: 446,
        2: 1_006,
        4: 2_034,
        8: 4_258,
        16: 8_648,
        32: 15_514,
        64: 25_066,
        128: 31_370,
        256: 27_520,
        512: 10_236,
        1_024: 364,
    }
    assert bands == expected_bands
    assert N == 1_806
    assert energy_total == 2_797_244
    assert abs(z_value - 49_630.64717292388) < 1e-8

    print("large determinant projection dyadic gate: PASS")
    print(
        "p=7:",
        f"N={small_N}, sum_E={small_energy}, Z={small_z:.6f}, bands={small_bands}",
    )
    print(
        "p=43:",
        f"N={N}, sum_E={energy_total}, Z={z_value:.6f}, bands={bands}",
    )


if __name__ == "__main__":
    main()
