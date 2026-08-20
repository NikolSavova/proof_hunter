#!/usr/bin/env python3
"""Checks for SHORTEST_PRIMITIVE_DIRECTION_ASSIGNMENT_NO_GO.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import permutations
import sys

sys.path.insert(0, "phase2/loop/erdos1208")

from verify_ambient_centroid_endpoint_difference_hypergraph_gate import (  # noqa: E402
    direction_occupancies,
    is_distance_sidon,
    primitive_unoriented,
    residue_parabola,
    shear,
    sub,
    triple_cells,
)
from verify_transverse_closure_witness import POINTS  # noqa: E402

Point = tuple[int, int]
Direction = tuple[int, int]


def coordinate_height(points: list[Point]) -> int:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def assigned_profile(
    points: list[Point],
) -> tuple[int, Counter[Direction], Counter[Direction], int, int]:
    """Assign every clean hyperedge to its shortest primitive direction."""
    assert is_distance_sidon(points)
    occupancies = direction_occupancies(points)
    assigned: Counter[Direction] = Counter()
    hyperedge_count = 0
    genuine_ties = 0

    for triples in triple_cells(points).values():
        for source in triples:
            for target in triples:
                if source == target:
                    continue
                assert len(set(source + target)) == 6
                for permuted_target in permutations(target):
                    directional_sizes: list[tuple[int, Direction]] = []
                    vectors: list[Point] = []
                    for source_index, target_index in zip(source, permuted_target):
                        vector = sub(points[target_index], points[source_index])
                        vectors.append(vector)
                        direction = primitive_unoriented(vector)
                        directional_sizes.append(
                            (
                                max(abs(direction[0]), abs(direction[1])),
                                direction,
                            )
                        )
                    assert (
                        sum(vector[0] for vector in vectors) == 0
                        and sum(vector[1] for vector in vectors) == 0
                    )
                    minimum_size = min(size for size, _ in directional_sizes)
                    candidates = sorted(
                        {
                            direction
                            for size, direction in directional_sizes
                            if size == minimum_size
                        }
                    )
                    genuine_ties += len(candidates) > 1
                    assigned[candidates[0]] += 1
                    hyperedge_count += 1

    return (
        hyperedge_count,
        assigned,
        occupancies,
        coordinate_height(points),
        genuine_ties,
    )


def assigned_envelope(
    points: list[Point],
) -> tuple[int, Fraction, tuple[Fraction, Direction, int, int], int]:
    total, assigned, occupancies, height, ties = assigned_profile(points)
    k = len(points)
    rows = []
    for direction, occupancy in occupancies.items():
        direction_size = max(abs(direction[0]), abs(direction[1]))
        denominator = (
            Fraction(k * occupancy)
            + Fraction(height * height, direction_size * direction_size)
        )
        rows.append(
            (
                Fraction(assigned[direction], 1) / denominator,
                direction,
                assigned[direction],
                occupancy,
            )
        )
    return total, max(row[0] for row in rows), max(rows), ties


def main() -> None:
    # Exact p=43 certificate and its shortest-direction extremizer.
    stress = shear(residue_parabola(43), 28)
    total, maximum_ratio, maximum_row, ties = assigned_envelope(stress)
    assert total == 126_852
    assert ties == 108
    assert maximum_row[1:] == ((85, 3), 1_648, 6)
    assert maximum_ratio == Fraction(476_272, 129_787)

    # The ratio continues to grow on larger genuine Euclidean shears.
    certificates = {
        7: (4, 24, 0.125),
        13: (6, 396, 0.3050740624015128),
        23: (13, 8_652, 1.3555540059967925),
        43: (28, 126_852, 3.6696433387011025),
        47: (32, 200_532, 4.697796414516179),
        59: (40, 496_968, 6.143513538170553),
        71: (54, 1_141_140, 9.102897638149077),
        79: (52, 1_713_576, 10.113125362212319),
    }
    for prime, (shear_value, expected_total, expected_ratio) in certificates.items():
        family_total, family_ratio, _, _ = assigned_envelope(
            shear(residue_parabola(prime), shear_value)
        )
        assert family_total == expected_total
        assert abs(float(family_ratio) - expected_ratio) < 1e-12

    # Independent closure stresses are benign but do not repair the
    # asymptotic parabola counterexample.
    closure_expected = {
        20: (432, 0.1686259244842351),
        40: (8_280, 0.3491536936552694),
    }
    for size, (expected_total, expected_ratio) in closure_expected.items():
        family_total, family_ratio, _, _ = assigned_envelope(POINTS[:size])
        assert family_total == expected_total
        assert abs(float(family_ratio) - expected_ratio) < 1e-12

    print("shortest primitive direction assignment no-go: PASS")
    print(
        "p=43:",
        f"assigned={total}, ties={ties}, max_ratio={float(maximum_ratio):.6f},",
        f"direction={maximum_row[1]}, load={maximum_row[2]}",
    )


if __name__ == "__main__":
    main()
