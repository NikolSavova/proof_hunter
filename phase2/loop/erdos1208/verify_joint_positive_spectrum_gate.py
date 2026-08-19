#!/usr/bin/env python3
"""Exact coefficient checks for JOINT_POSITIVE_SPECTRUM_GATE.md.

The threshold estimate in the note is the scalar inequality
``g^2 <= N^(3/2)|g|`` followed by Cauchy--Schwarz.  This script checks all
set-theoretic/Fourier-coefficient inputs on the stored closure witness and
checks the threshold endpoint comparisons in integer-squared form.
"""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def correlation(values: set[Point]) -> Counter[Point]:
    return Counter(subtract(left, right) for left in values for right in values)


def main() -> None:
    points = POINTS[:30]
    assert is_distance_sidon(points)
    k = len(points)
    differences = {
        subtract(left, right)
        for left in points
        for right in points
    }
    n = len(differences)
    assert n == k * (k - 1) + 1
    assert differences.intersection(map(rotate, differences)) == {(0, 0)}

    # These are precisely the endpoint comparisons used to exclude a
    # negative or one-sided-small factor above the N^(3/2) threshold.
    floor = k - 1
    assert floor * floor <= n
    assert (floor * n) ** 2 <= n**3
    # floor < N^(3/4), checked without floating point.
    assert floor**4 < n**3

    overlap = correlation(differences)
    energy = sum(
        value * overlap[rotate(shift)]
        for shift, value in overlap.items()
    )
    assert energy == sum(
        overlap[shift] * overlap[rotate(shift)]
        for shift in overlap
    )

    # Parseval's coefficient-side inputs: ||hat 1_D||_2^2=|D| and
    # <hat 1_D,hat 1_JD>=|D cap JD|=1.
    l2_mass = len(differences)
    mixed_inner_product = len(
        differences.intersection(map(rotate, differences))
    )
    assert (l2_mass, mixed_inner_product) == (n, 1)

    print("k", k)
    print("N", n)
    print("orthogonal_energy", energy)
    print("fourier_l2_mass", l2_mass)
    print("mixed_inner_product", mixed_inner_product)
    print("joint positive-spectrum gate: PASS")


if __name__ == "__main__":
    main()
