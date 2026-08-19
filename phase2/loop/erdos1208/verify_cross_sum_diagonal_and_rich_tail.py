#!/usr/bin/env python3
"""Exact checks for CROSS_SUM_DIAGONAL_AND_RICH_TAIL_REDUCTION.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import isqrt

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import dense_perpendicular_points
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def complete_difference(points: list[Point]) -> set[Point]:
    return {subtract(left, right) for left in points for right in points}


def translation_counts(points: set[Point]) -> Counter[Point]:
    return Counter(subtract(left, right) for left in points for right in points)


def endpoint_energy_profile(points: list[Point]) -> tuple[int, int, int]:
    """Return total, eight-distinct, and repeated-endpoint cross-sum energy."""

    k = len(points)
    cross_records: dict[Point, tuple[int, int]] = {}
    for left_index, left in enumerate(points):
        for right_index, right in enumerate(points):
            value = add(left, rotate(right))
            assert value not in cross_records
            cross_records[value] = (left_index, right_index)
    assert len(cross_records) == k * k

    pair_sums: dict[Point, list[tuple[int, int, int, int]]] = defaultdict(list)
    records = list(cross_records.items())
    for first_value, (a, b) in records:
        for second_value, (c, d) in records:
            pair_sums[add(first_value, second_value)].append((a, b, c, d))

    total = sum(len(fibre) ** 2 for fibre in pair_sums.values())
    distinct = 0
    for fibre in pair_sums.values():
        for first in fibre:
            for second in fibre:
                if len(set(first + second)) == 8:
                    distinct += 1
    repeated = total - distinct
    assert repeated <= 56 * k**5
    return total, distinct, repeated


def difference_profile(points: list[Point]) -> tuple[int, int, int, int]:
    k = len(points)
    differences = complete_difference(points)
    number = len(differences)
    assert number == k * (k - 1) + 1
    counts = translation_counts(differences)

    orthogonal = sum(
        count * counts.get(rotate(shift), 0)
        for shift, count in counts.items()
    )
    realized_cross = sum(
        counts.get(rotate(shift), 0)
        for shift in differences
        if shift != (0, 0)
    )
    predicted_cross_energy = (
        orthogonal
        - number * number
        + (2 * k * k - k) ** 2
        + 4 * (k - 1) * realized_cross
    )

    rich_tail = sum(
        count * counts.get(rotate(shift), 0)
        for shift, count in counts.items()
        if shift != (0, 0)
        and count * count > number
        and counts.get(rotate(shift), 0) ** 2 > number
    )
    # Outside the jointly rich tail, at least one of the two integer
    # multiplicities is at most floor(sqrt(number)).  This is the exact
    # integer version of the 2 N^(5/2) estimate in the note.
    low_part = orthogonal - rich_tail
    assert low_part <= number * number + 2 * isqrt(number) * number * number
    assert predicted_cross_energy <= orthogonal + 8 * k**5
    return orthogonal, realized_cross, rich_tail, predicted_cross_energy


def main() -> None:
    full_ruler = dense_perpendicular_points()
    families = [
        ("closure-8", POINTS[:8]),
        ("closure-10", POINTS[:10]),
        (
            "Costas-10",
            [apply(ROWS[11][0], point) for point in welch(11)],
        ),
        ("perpendicular-ruler-8", full_ruler[:4] + full_ruler[20:24]),
    ]

    for name, points in families:
        assert is_distance_sidon(points)
        endpoint = endpoint_energy_profile(points)
        difference = difference_profile(points)
        assert endpoint[0] == difference[3]
        print(name, "endpoint", endpoint, "difference", difference)

    print("cross-sum diagonal and rich-tail reduction: PASS")


if __name__ == "__main__":
    main()
