#!/usr/bin/env python3
"""Exact checks for CLOSED_FIBRE_Q_AFFINE_DENSE_COSTAS_BARRIER.md."""

from __future__ import annotations

import math
import sys
from collections import Counter
from itertools import combinations
from math import comb, gcd

sys.path.insert(0, "phase2/loop/erdos1208")

from analyze_affine_costas_energy import is_distance_sidon, welch  # noqa: E402
from verify_ambient_cross_sum_energy_gate import side_length  # noqa: E402
from verify_determinant_prime_costas_resonance import apply  # noqa: E402
from verify_large_determinant_closed_fibre_energy_gate import (  # noqa: E402
    direction_fibres,
)
from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    primitive_unoriented,
)
from verify_directional_midpoint_pointwise_no_go_global_gate import (  # noqa: E402
    directional_midpoint_profile,
)


Point = tuple[int, int]
Matrix = tuple[int, int, int, int]


FULL_ROWS: dict[int, tuple[Matrix, int, int, int]] = {
    # matrix, side length, Q(base), Q(image)
    11: ((-3, 2, 2, -5), 41, 2_190, 2_180),
    23: ((-5, -2, -1, -5), 131, 61_370, 61_406),
    43: ((-5, 13, -1, -6), 612, 874_300, 874_292),
    47: ((-10, 11, 3, -8), 666, 1_289_926, 1_290_082),
    59: ((-10, -9, -9, -14), 1_144, 3_348_872, 3_349_322),
}


EXPECTED_P = {
    11: 1_764,
    23: 53_442,
    43: 762_092,
    47: 1_127_250,
    59: 2_848_616,
}


EXPECTED_CLEAN_MIDPOINT = {
    11: 216,
    23: 18_684,
    43: 338_904,
    47: 517_932,
    59: 1_365_624,
}


EXTENDED_ROWS: dict[int, tuple[Matrix, int]] = {
    101: ((-22, -23, -9, -14), 4_029),
    139: ((-39, -34, -20, -21), 9_437),
    211: ((-57, 46, 14, -15), 18_498),
    251: ((-53, 59, -33, 32), 26_980),
}


# One exact balanced distance-separator for every tested prime in [11, 251].
# Full Q is intentionally evaluated only on the smaller rows above.
SEARCH_ROWS: dict[int, Matrix] = {
    11: (-3, 2, 2, -5),
    13: (-3, 7, -1, -2),
    17: (-7, 5, -2, -1),
    19: (-5, -3, 3, -2),
    23: (-5, -2, -1, -5),
    29: (-11, 9, -2, -1),
    31: (-9, -13, 1, -2),
    37: (-4, -13, 1, -6),
    41: (-16, -7, -1, -3),
    43: (-5, 13, -1, -6),
    47: (-10, 11, 3, -8),
    53: (-15, -13, 11, 6),
    59: (-10, -9, -9, -14),
    61: (-15, -14, 14, 9),
    67: (-19, -17, 14, 9),
    71: (-17, -16, 14, 9),
    73: (-20, -17, 9, 4),
    79: (-19, -17, 8, 3),
    83: (-23, 24, 9, -13),
    89: (-16, -17, -7, -13),
    97: (-28, -19, 11, 4),
    101: (-22, -23, -9, -14),
    103: (-19, -24, -6, -13),
    107: (-25, -24, 18, 13),
    109: (-23, -22, -17, -21),
    113: (-26, -23, 23, 16),
    127: (-23, 31, 10, -19),
    131: (-29, -32, -24, -31),
    137: (-31, -27, -11, -14),
    139: (-39, -34, -20, -21),
    149: (-35, 34, -26, 21),
    151: (-31, -41, 12, 11),
    157: (-39, 32, 28, -27),
    163: (-33, -38, -7, -13),
    167: (-41, 37, 11, -14),
    173: (-43, -45, -21, -26),
    179: (-46, 39, -27, 19),
    181: (-46, -41, -27, -28),
    191: (-39, -49, -16, -25),
    193: (-20, 43, 9, -29),
    197: (-46, 41, 21, -23),
    199: (-49, 32, 29, -23),
    211: (-57, 46, 14, -15),
    223: (-55, -49, -28, -29),
    227: (-55, -42, 46, 31),
    229: (-45, 53, 22, -31),
    233: (-55, -46, -32, -31),
    239: (-48, -53, -29, -37),
    241: (-61, -55, -30, -31),
    251: (-53, 59, -33, 32),
}


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def matrix_determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def directed_differences(points: list[Point]) -> list[Point]:
    values = [
        (target[0] - source[0], target[1] - source[1])
        for source in points
        for target in points
        if source != target
    ]
    assert len(values) == len(set(values))
    return values


def q_data(
    points: list[Point],
) -> tuple[
    int,
    dict[Point, set[int]],
    dict[Point, dict[int, int]],
    dict[Point, int],
]:
    _, contents, _, fibres = direction_fibres(points)
    total = 0
    contributions: dict[Point, int] = {}
    fibre_loads: dict[Point, dict[int, int]] = {}

    for direction, gaps in contents.items():
        direction_total = 0
        loads = {residue: len(fibre) for residue, fibre in fibres[direction].items()}
        fibre_loads[direction] = loads
        for residue, fibre_size in loads.items():
            if residue == 0:
                continue
            alpha_by_band = Counter(
                (gap * abs(residue)).bit_length() - 1 for gap in gaps
            )
            direction_total += sum(
                min(comb(fibre_size, 2), alpha * fibre_size)
                for alpha in alpha_by_band.values()
            )
        contributions[direction] = direction_total
        total += direction_total
    return total, contents, fibre_loads, contributions


def verify_local_collided_mass(points: list[Point]) -> None:
    total, contents, fibre_loads, contributions = q_data(points)
    assert total == sum(contributions.values())
    k = len(points)
    n = k * (k - 1)
    m = side_length(points)

    for direction, gaps in contents.items():
        q = max(abs(direction[0]), abs(direction[1]))
        loads = fibre_loads[direction]
        assert loads.get(0, 0) == 2 * len(gaps)
        assert len(gaps) <= m // q
        collided_mass = sum(
            load for residue, load in loads.items() if residue and load >= 2
        )
        assert 2 * contributions[direction] >= collided_mass
        assert collided_mass >= n - 4 * q * m - 2 * m / q


def verify_direction_reciprocal_bound() -> None:
    directions: list[Point] = []
    for x in range(-200, 201):
        for y in range(-200, 201):
            if (x, y) == (0, 0) or gcd(abs(x), abs(y)) != 1:
                continue
            direction = primitive_unoriented((x, y))
            if direction == (x, y):
                directions.append(direction)
    directions.sort(key=lambda w: max(abs(w[0]), abs(w[1])))
    reciprocal_sum = 0.0
    for count, direction in enumerate(directions, 1):
        q = max(abs(direction[0]), abs(direction[1]))
        reciprocal_sum += 1 / q
        assert reciprocal_sum <= 6 * math.sqrt(count) + 1e-12


def verify_affine_mapping(base: list[Point], matrix: Matrix) -> None:
    delta = matrix_determinant(matrix)
    assert delta != 0
    image = [apply(matrix, point) for point in base]
    base_total, base_contents, base_loads, _ = q_data(base)
    image_total, image_contents, image_loads, _ = q_data(image)
    assert base_total <= 2 * image_total
    assert image_total <= 2 * base_total

    a, b, c, d = matrix
    for base_direction, gaps in base_contents.items():
        transformed_vector = (
            a * base_direction[0] + b * base_direction[1],
            c * base_direction[0] + d * base_direction[1],
        )
        content_multiplier = gcd(
            abs(transformed_vector[0]), abs(transformed_vector[1])
        )
        image_direction = primitive_unoriented(transformed_vector)
        epsilon = 1
        if transformed_vector != (
            content_multiplier * image_direction[0],
            content_multiplier * image_direction[1],
        ):
            epsilon = -1
        assert transformed_vector == (
            epsilon * content_multiplier * image_direction[0],
            epsilon * content_multiplier * image_direction[1],
        )
        assert image_contents[image_direction] == {
            content_multiplier * gap for gap in gaps
        }

        for residue, load in base_loads[base_direction].items():
            numerator = epsilon * delta * residue
            assert numerator % content_multiplier == 0
            image_residue = numerator // content_multiplier
            assert image_loads[image_direction][image_residue] == load
            for gap in gaps:
                mapped_gap = content_multiplier * gap
                assert mapped_gap * abs(image_residue) == abs(delta) * gap * abs(residue)


def verify_power_two_equality() -> None:
    base = welch(23)
    scaled = [(2 * x, 2 * y) for x, y in base]
    base_total = q_data(base)[0]
    scaled_total = q_data(scaled)[0]
    assert base_total == scaled_total == 61_370


def verify_full_rows() -> None:
    for prime, (matrix, wanted_m, wanted_base_q, wanted_image_q) in FULL_ROWS.items():
        assert matrix_determinant(matrix) == prime
        base = welch(prime)
        image = [apply(matrix, point) for point in base]
        assert is_distance_sidon(image)
        assert side_length(image) == wanted_m
        base_data = q_data(base)
        image_data = q_data(image)
        base_q = base_data[0]
        image_q = image_data[0]
        assert (base_q, image_q) == (wanted_base_q, wanted_image_q)
        assert base_q <= 2 * image_q and image_q <= 2 * base_q
        base_p = sum(
            comb(load, 2)
            for loads in base_data[2].values()
            for residue, load in loads.items()
            if residue != 0
        )
        image_p = sum(
            comb(load, 2)
            for loads in image_data[2].values()
            for residue, load in loads.items()
            if residue != 0
        )
        assert base_p == image_p == EXPECTED_P[prime]
        directional_loads, _, _ = directional_midpoint_profile(image)
        clean_midpoint = sum(directional_loads.values())
        assert clean_midpoint == EXPECTED_CLEAN_MIDPOINT[prime]

        # Coefficient-count form of the rational-line Fourier identity
        # and its r=0 correction in (6.5).
        n = len(base) * (len(base) - 1)
        all_pair_energy = sum(
            (sum(load * load for load in loads.values()) - n) // 2
            for loads in base_data[2].values()
        )
        zero_fibre_correction = sum(
            comb(2 * len(gaps), 2) for gaps in base_data[1].values()
        )
        assert base_p == all_pair_energy - zero_fibre_correction
        k = len(base)
        print(
            f"p={prime}",
            f"k={k}",
            f"m={wanted_m}",
            f"Q0={base_q}",
            f"Q={image_q}",
            f"Q/k^4={image_q / k**4:.6f}",
            f"Q/(k^3+m^2)={image_q / (k**3 + wanted_m**2):.6f}",
            f"P={base_p}",
            f"H={clean_midpoint}",
            f"H/(k^3+m^2)={clean_midpoint / (k**3 + wanted_m**2):.6f}",
        )


def verify_extended_rows() -> None:
    for prime, (matrix, wanted_m) in EXTENDED_ROWS.items():
        assert matrix_determinant(matrix) == prime
        assert max(abs(value) for value in matrix) ** 2 <= 16 * prime
        image = [apply(matrix, point) for point in welch(prime)]
        assert is_distance_sidon(image)
        assert side_length(image) == wanted_m
        print(
            f"extended p={prime}",
            f"m={wanted_m}",
            f"max-entry/sqrt(p)={max(map(abs, matrix)) / math.sqrt(prime):.6f}",
        )


def verify_complete_balanced_search_table() -> None:
    expected_primes = [
        value
        for value in range(11, 252)
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1))
    ]
    assert sorted(SEARCH_ROWS) == expected_primes
    for prime, matrix in SEARCH_ROWS.items():
        assert matrix_determinant(matrix) == prime
        assert max(map(abs, matrix)) ** 2 <= 16 * prime
        image = [apply(matrix, point) for point in welch(prime)]
        assert is_distance_sidon(image)


def main() -> None:
    verify_direction_reciprocal_bound()
    verify_power_two_equality()
    verify_affine_mapping(welch(11), FULL_ROWS[11][0])
    verify_local_collided_mass(welch(23))
    verify_full_rows()
    verify_extended_rows()
    verify_complete_balanced_search_table()
    print("closed-fibre Q affine/dense Costas barrier: PASS")


if __name__ == "__main__":
    main()
