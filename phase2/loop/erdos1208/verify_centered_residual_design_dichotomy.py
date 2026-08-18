#!/usr/bin/env python3
"""Exact checks for CENTERED_RESIDUAL_DESIGN_DICHOTOMY.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_foreign_shift_averaging_barrier import build_instance
from verify_transverse_closure_witness import POINTS as CLOSURE_POINTS
from verify_transverse_color_closure import POINTS as COLOUR_POINTS
from verify_transverse_dual_closure import POINTS as HYBRID_POINTS
from verify_transverse_eight_corner_gate import representation_fibres
from verify_two_sided_rotated_support_audit import centered_residual
from verify_welch_relation_rigidity import MODULUS, SQRT_MINUS_ONE


Point = tuple[int, int]
Triple = tuple[int, int, int]
Row = tuple[int, int, int, int, int, int]

COEFFICIENTS = (
    1,
    SQRT_MINUS_ONE,
    -SQRT_MINUS_ONE % MODULUS,
    -1 % MODULUS,
    -SQRT_MINUS_ONE % MODULUS,
    SQRT_MINUS_ONE,
)
ROLE_PAIRS = tuple(combinations(range(6), 2))
EDGE_ROLE_PAIRS = ((0, 3), (1, 2), (4, 5))


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def weighted_pair_sum_residual(points: list[Point]) -> int:
    pair_sums: Counter[Point] = Counter(
        add(left, right) for left in points for right in points
    )
    assert set(pair_sums.values()) <= {1, 2}

    differences = {
        subtract(left, right)
        for left in points
        for right in points
        if left != right
    }
    rotated = {rotate(value) for value in differences}
    return sum(
        left_weight * right_weight
        for left, left_weight in pair_sums.items()
        for right, right_weight in pair_sums.items()
        if subtract(left, right) in rotated
    )


def collision_rows(points: list[Point]):
    for fibre in representation_fibres(points).values():
        for first in fibre:
            for second in fibre:
                if first != second:
                    yield first, second


def is_transverse(points: list[Point], first: Triple, second: Triple) -> bool:
    row_edge = subtract(points[second[1]], points[second[2]])
    colour_edge = subtract(points[second[0]], points[first[0]])
    return (
        colour_edge != (0, 0)
        and row_edge[0] * colour_edge[0]
        + row_edge[1] * colour_edge[1]
        != 0
    )


def add_to_basis(row: dict[int, int], basis: dict[int, dict[int, int]]) -> bool:
    while row:
        pivot = min(row)
        coefficient = row[pivot]
        if pivot not in basis:
            inverse = pow(coefficient, -1, MODULUS)
            basis[pivot] = {
                index: value * inverse % MODULUS
                for index, value in row.items()
            }
            return True
        for index, value in basis[pivot].items():
            new_value = (
                row.get(index, 0) - coefficient * value
            ) % MODULUS
            if new_value:
                row[index] = new_value
            else:
                row.pop(index, None)
    return False


def kernel_vectors(points: list[Point]) -> list[list[int]]:
    size = len(points)
    vectors: list[list[int]] = []

    # Five independent role-constant solutions of sum alpha_r c_r = 0.
    last = COEFFICIENTS[-1]
    for role in range(5):
        vector = [0] * (6 * size)
        for label in range(size):
            vector[role * size + label] = 1
            vector[5 * size + label] = (
                -COEFFICIENTS[role] * pow(last, -1, MODULUS)
            ) % MODULUS
        vectors.append(vector)

    coordinates = [
        (x + SQRT_MINUS_ONE * y) % MODULUS for x, y in points
    ]
    conjugates = [
        (x - SQRT_MINUS_ONE * y) % MODULUS for x, y in points
    ]
    vectors.append(coordinates * 6)

    # alpha=(1,i,-i,-1,-i,i), so conjugation is repaired by
    # the role signs (1,-1,-1,1,-1,-1).
    conjugate_signs = (1, -1, -1, 1, -1, -1)
    vectors.append(
        [
            conjugate_signs[role] * conjugates[label] % MODULUS
            for role in range(6)
            for label in range(size)
        ]
    )
    return vectors


def row_dictionary(row: Row, size: int) -> dict[int, int]:
    return {
        role * size + label: COEFFICIENTS[role]
        for role, label in enumerate(row)
    }


def row_dot(row: dict[int, int], vector: list[int]) -> int:
    return sum(value * vector[index] for index, value in row.items()) % MODULUS


def audit(
    name: str,
    points: list[Point],
    *,
    expected_total: int | None = None,
    expected_union: tuple[int, int, int, int] | None = None,
    expected_hard: int | None = None,
    expected_edge_maxima: tuple[int, int, int] | None = None,
    expected_cross_maximum: int | None = None,
    certify_rank: bool = False,
) -> None:
    size = len(points)
    union = Counter()
    pair_counts = {roles: Counter() for roles in ROLE_PAIRS}
    total = hard = 0
    basis: dict[int, dict[int, int]] = {}
    kernels = kernel_vectors(points) if certify_rank else []
    target_rank = 6 * size - 7

    for first, second in collision_rows(points):
        total += 1
        row = first + second
        union[len(set(row))] += 1
        if len(set(row)) != 6 or not is_transverse(points, first, second):
            continue

        hard += 1
        for roles, counts in pair_counts.items():
            counts[row[roles[0]], row[roles[1]]] += 1

        if certify_rank:
            equation = row_dictionary(row, size)
            assert all(row_dot(equation, vector) == 0 for vector in kernels)
            if len(basis) < target_rank:
                add_to_basis(dict(equation), basis)

    if expected_total is not None:
        assert total == expected_total
    if expected_union is not None:
        assert tuple(union[key] for key in (3, 4, 5, 6)) == expected_union
    if expected_hard is not None:
        assert hard == expected_hard

    edge_maxima = tuple(
        max(pair_counts[roles].values(), default=0)
        for roles in EDGE_ROLE_PAIRS
    )
    cross_maximum = max(
        max(counts.values(), default=0)
        for roles, counts in pair_counts.items()
        if roles not in EDGE_ROLE_PAIRS
    )
    if expected_edge_maxima is not None:
        assert edge_maxima == expected_edge_maxima
    if expected_cross_maximum is not None:
        assert cross_maximum == expected_cross_maximum
    if certify_rank:
        assert len(basis) == target_rank

    print(
        name,
        "k", size,
        "residual", total,
        "hard", hard,
        "edge-pair maxima", edge_maxima,
        "cross maximum", cross_maximum,
        "rank", len(basis) if certify_rank else "-",
    )


def main() -> None:
    seed = CLOSURE_POINTS[:8]
    direct = centered_residual(seed)
    weighted = weighted_pair_sum_residual(seed)
    assert direct == weighted == 52
    print("weighted pair-sum identity", direct)

    endpoint_profiles = {
        20: (5_564, (4, 252, 2_004, 3_304)),
        30: (26_472, (8, 640, 7_088, 18_736)),
        40: (73_282, (8, 1_170, 15_664, 56_440)),
    }
    for size, (total, profile) in endpoint_profiles.items():
        audit(
            f"closure-{size}",
            CLOSURE_POINTS[:size],
            expected_total=total,
            expected_union=profile,
            certify_rank=size == 20,
        )

    audit(
        "closure-60",
        CLOSURE_POINTS[:60],
        expected_total=259_724,
        expected_union=(8, 1_920, 39_156, 218_640),
        expected_hard=218_516,
        expected_edge_maxima=(180, 292, 292),
        expected_cross_maximum=293,
        certify_rank=True,
    )

    _, _, anchor_points = build_instance()
    audit(
        "compact-anchor-117",
        anchor_points,
        expected_total=160_392,
        expected_hard=157_960,
        expected_edge_maxima=(3_880, 34, 34),
        expected_cross_maximum=289,
    )
    audit(
        "fixed-colour-65",
        COLOUR_POINTS,
        expected_total=45_076,
        expected_hard=38_368,
        expected_edge_maxima=(802, 29, 29),
        expected_cross_maximum=74,
    )
    audit(
        "hybrid-45",
        HYBRID_POINTS,
        expected_total=64_968,
        expected_hard=52_664,
        expected_edge_maxima=(188, 114, 114),
        expected_cross_maximum=114,
    )
    print("centered residual design dichotomy: PASS")


if __name__ == "__main__":
    main()
