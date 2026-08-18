#!/usr/bin/env python3
"""Exact finite checks for the sparse oblique midpoint barrier."""

from __future__ import annotations

from collections import defaultdict


Coefficient = tuple[int, int]
Point = tuple[int, int]


def physical(basis_scale: int, coefficient: Coefficient) -> Point:
    first, second = coefficient
    diagonal = first + second
    return basis_scale * diagonal + second, diagonal


def norm_square(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def verify_instance(basis_scale: int, multiplier: int) -> tuple[int, int]:
    side = multiplier * basis_scale * basis_scale
    fibres: dict[int, list[Coefficient]] = defaultdict(list)
    for first in range(side):
        for second in range(side):
            coefficient = first, second
            fibres[norm_square(physical(basis_scale, coefficient))].append(
                coefficient
            )

    collision_pairs = 0
    for fibre in fibres.values():
        for left_index, left in enumerate(fibre):
            for right in fibre[left_index + 1 :]:
                collision_pairs += 1
                left_s = left[0] + left[1]
                right_s = right[0] + right[1]
                assert left_s != right_s
                if left_s < right_s:
                    low_s, high_s = left_s, right_s
                    low, high = left, right
                else:
                    low_s, high_s = right_s, left_s
                    low, high = right, left

                low_point = physical(basis_scale, low)
                high_point = physical(basis_scale, high)
                assert low_point[0] > high_point[0]
                k = high_s - low_s
                h = low_point[0] - high_point[0]
                j = k - basis_scale * h
                assert 1 <= j < h < multiplier

                low_b, high_b = low[1], high[1]
                assert low_b - high_b == h + basis_scale * k
                assert h * (low_b + high_b) == j * (low_s + high_s)
                assert (
                    h * (basis_scale * basis_scale + 1) + basis_scale * j
                    <= side - 1
                )

    assert collision_pairs < multiplier * multiplier * side

    # One representative from each norm fibre is an explicit radial
    # transversal.  Its deficit is at most the number of collision pairs.
    transversal = [fibre[0] for fibre in fibres.values()]
    assert len({norm_square(physical(basis_scale, c)) for c in transversal}) == len(
        transversal
    )
    deficit = side * side - len(transversal)
    assert deficit <= collision_pairs
    assert len(transversal) >= side * side - multiplier * multiplier * side

    height = (2 * basis_scale + 1) * (side - 1)
    assert (
        height * height * basis_scale * basis_scale * multiplier
        <= (2 * basis_scale + 1) ** 2 * side**3
    )
    return collision_pairs, deficit


def main() -> None:
    cases = [(5, 2), (6, 3), (8, 5), (10, 8)]
    for basis_scale, multiplier in cases:
        pairs, deficit = verify_instance(basis_scale, multiplier)
        side = multiplier * basis_scale * basis_scale
        print(
            "B",
            basis_scale,
            "T",
            multiplier,
            "r",
            side,
            "collision pairs",
            pairs,
            "transversal deficit",
            deficit,
            "PASS",
        )
    print("sparse oblique midpoint barrier: PASS")


if __name__ == "__main__":
    main()
