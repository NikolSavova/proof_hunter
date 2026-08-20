#!/usr/bin/env python3
"""Verify the projective-dilation audit for the global pair energy P."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, gcd
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_closed_fibre_q_height_layered_barrier import (  # noqa: E402
    ambient_side,
    closed_q_profile,
    distance_sidon,
    dominance_euclideanize,
    layered_vector_sidon,
    lifted_residue_parabola,
    vector_sidon,
)
from verify_transverse_closure_witness import POINTS  # noqa: E402


Point = tuple[int, int]
Direction = tuple[int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def primitive(vector: Point) -> tuple[Direction, int]:
    divisor = gcd(abs(vector[0]), abs(vector[1]))
    direction = vector[0] // divisor, vector[1] // divisor
    if direction[0] < 0 or (direction[0] == 0 and direction[1] < 0):
        direction = -direction[0], -direction[1]
    return direction, divisor


def directional_profiles(
    points: list[Point],
) -> tuple[dict[Direction, int], dict[Direction, int], int]:
    differences = [
        subtract(right, left)
        for first, left in enumerate(points)
        for second, right in enumerate(points)
        if first != second
    ]
    contents: defaultdict[Direction, set[int]] = defaultdict(set)
    for left, right in combinations(points, 2):
        direction, content = primitive(subtract(right, left))
        contents[direction].add(content)
    assert sum(map(len, contents.values())) == len(differences) // 2

    pair_energy = {}
    projection_energy = {}
    size = len(points)
    for direction in contents:
        fibre_sizes = Counter(
            determinant(direction, vector) for vector in differences
        )
        pair_energy[direction] = sum(
            comb(load, 2)
            for residue, load in fibre_sizes.items()
            if residue
        )

        point_lines = Counter(
            determinant(direction, point) for point in points
        )
        edge_count = sum(comb(load, 2) for load in point_lines.values())
        assert edge_count == len(contents[direction])
        full_energy = sum(load * load for load in fibre_sizes.values())
        # Young's convolution inequality: ||n * n~||_2^2 <= ||n||_1^2 ||n||_2^2.
        assert full_energy <= size * size * (size + 2 * edge_count)
        projection_energy[direction] = full_energy
    return pair_energy, projection_energy, len(differences)


def direct_projective_count(points: list[Point]) -> int:
    differences = [
        subtract(right, left)
        for first, left in enumerate(points)
        for second, right in enumerate(points)
        if first != second
    ]
    active = {
        primitive(subtract(right, left))[0]
        for left, right in combinations(points, 2)
    }
    output = 0
    for first, second in combinations(differences, 2):
        gap = subtract(first, second)
        if gap == (0, 0):
            continue
        direction, _content = primitive(gap)
        output += direction in active and determinant(direction, first) != 0
    return output


def horizontal_pair_and_q(points: list[Point]) -> tuple[int, int, int]:
    differences = [
        subtract(right, left)
        for first, left in enumerate(points)
        for second, right in enumerate(points)
        if first != second
    ]
    horizontal_contents = {
        abs(right[0] - left[0])
        for left, right in combinations(points, 2)
        if right[1] == left[1]
    }
    sizes = Counter(vector[1] for vector in differences)
    pair_energy = 0
    q_energy = 0
    for residue, load in sizes.items():
        if residue == 0:
            continue
        cap = comb(load, 2)
        pair_energy += cap
        alpha = Counter(
            (content * abs(residue)).bit_length() - 1
            for content in horizontal_contents
        )
        q_energy += sum(
            min(cap, multiplicity * load)
            for multiplicity in alpha.values()
        )
    return pair_energy, q_energy, len(horizontal_contents)


def greedy_prescribed_projection(size: int) -> list[Point]:
    """Distance-Sidon points with y-multiset 0,0,1,...,size-2."""
    ordinates = [0, 0, *range(1, size - 1)]
    points: list[Point] = []
    used_distances: set[int] = set()
    for ordinate in ordinates:
        for abscissa in range(20 * size**3 + 1):
            if any(abscissa == old[0] for old in points):
                continue
            new_distances = [
                (abscissa - old[0]) ** 2 + (ordinate - old[1]) ** 2
                for old in points
            ]
            if len(new_distances) != len(set(new_distances)):
                continue
            if set(new_distances) & used_distances:
                continue
            points.append((abscissa, ordinate))
            used_distances.update(new_distances)
            break
        else:
            raise AssertionError("greedy finite-avoidance interval exhausted")
    assert distance_sidon(points)
    assert len({point[0] for point in points}) == size
    return points


def verify_projective_identity() -> dict[str, tuple[int, int]]:
    output = {}
    for name, points in (
        ("closure-10", POINTS[:10]),
        ("modular-7", lifted_residue_parabola(7)),
    ):
        assert distance_sidon(points)
        directional, _full, directed_size = directional_profiles(points)
        total = sum(directional.values())
        assert total == direct_projective_count(points)
        assert total <= comb(directed_size, 2)
        assert total == closed_q_profile(points)[1]
        output[name] = total, directed_size
    return output


def verify_layered_obstruction() -> dict[int, tuple[int, int, int, int]]:
    expected = {
        3: (378, 486, 668, 9),
        5: (18_500, 24_800, 6_663, 25),
        7: (217_462, 298_214, 26_256, 49),
        11: (5_630_130, 7_914_368, 165_138, 121),
    }
    output = {}
    for prime, row in expected.items():
        base = layered_vector_sidon(prime)
        lifted = dominance_euclideanize(base, prime)
        pair_energy, q_energy, edge_count = horizontal_pair_and_q(lifted)
        assert edge_count == prime * comb(prime, 2)
        assert (pair_energy, q_energy, ambient_side(lifted), len(lifted)) == row
        exact = 2 * sum(
            comb(height * prime * prime, 2)
            for height in range(1, prime)
        )
        assert pair_energy == exact
        output[prime] = row
    return output


def verify_one_direction_loss() -> dict[int, tuple[int, ...]]:
    expected = {
        20: (115, 26_748, 29_002, 2_280, 376),
        40: (362, 345_908, 401_212, 19_760, 1_556),
        60: (711, 1_576_232, 1_824_114, 68_440, 3_536),
    }
    output = {}
    for size, row in expected.items():
        points = greedy_prescribed_projection(size)
        q_total, p_total = closed_q_profile(points)[:2]
        p_horizontal, q_horizontal, edge_count = horizontal_pair_and_q(points)
        assert edge_count == 1
        actual = (
            ambient_side(points),
            p_total,
            q_total,
            p_horizontal,
            q_horizontal,
        )
        assert actual == row
        assert p_horizontal == 2 * comb(size, 3)
        assert p_horizontal > (size // 4) * q_horizontal
        output[size] = actual
    return output


def main() -> None:
    identity = verify_projective_identity()
    layered = verify_layered_obstruction()
    one_direction = verify_one_direction_loss()
    # A larger genuine critical prefix for the summed gate.
    closure = closed_q_profile(POINTS[:60])
    assert closure[:2] == (896_292, 787_498)
    modular = closed_q_profile(lifted_residue_parabola(43))
    assert modular[:2] == (988_328, 847_864)
    print(
        "PASS",
        {
            "projective_identity": identity,
            "layered_obstruction": layered,
            "one_direction_loss": one_direction,
            "closure_60_P": closure[1],
            "modular_43_P": modular[1],
            "flat_gate_status": "survives genuine stresses; critical radial packing open",
        },
    )


if __name__ == "__main__":
    main()
