#!/usr/bin/env python3
"""Exact checks for FIXED_ROW_LONGEST_BOOK_GATE.md."""

from __future__ import annotations

from collections import Counter

from analyze_fixed_row_cycle_longest_charge import profile as charge_profile
from analyze_fixed_row_orbits import transform
from analyze_fixed_row_rigidity import profile as rigidity_profile
from analyze_parabola_distances import profile as parabola_profile
from analyze_transverse_longest_charge import DIAMETER_POINTS
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_local_gate import differences


HEAVY_CHARGE = [
    (1869, 14, 7595),
    (1922, 29, 12838),
    (1923, 29, 13991),
    (2008, 44, 15126),
    (2063, 38, 15117),
    (2071, 26, 9419),
]

DIAMETER_CHARGE = [
    (473, 30, 5215),
    (243, 15, 1407),
    (262, 22, 1928),
    (312, 14, 2058),
    (447, 34, 4701),
    (230, 16, 1162),
]


def first_three(rows):
    return [tuple(row[:3]) for row in rows]


def orbit_occupancy(points, row):
    dset = differences(points)
    seen = set()
    occupancy = Counter()
    for edge in dset:
        if edge in seen:
            continue
        orbit = []
        current = edge
        while current not in orbit:
            orbit.append(current)
            current = transform(current, row)
        assert current == edge
        seen.update(orbit)
        occupancy[(len(orbit), sum(item in dset for item in orbit))] += 1
    return occupancy


def main():
    heavy = first_three(charge_profile(HEAVY_POINTS, (0, -1)))
    diameter = first_three(charge_profile(DIAMETER_POINTS, (10_000, 0)))
    assert heavy == HEAVY_CHARGE
    assert diameter == DIAMETER_CHARGE
    assert max(row[2] for row in heavy) == 15126
    assert max(row[2] for row in diameter) == 5215

    assert rigidity_profile(HEAVY_POINTS, (0, -1)) == (948, 118, 2)
    assert rigidity_profile(DIAMETER_POINTS, (10_000, 0)) == (266, 85, 5)

    occupancy = orbit_occupancy(HEAVY_POINTS, (0, -1))
    assert occupancy == Counter({
        (4, 1): 12078,
        (4, 2): 909,
        (4, 3): 115,
        (4, 4): 10,
    })

    assert parabola_profile(1000) == (499500, 499500, 1, 0)

    print("heavy charge profile:", heavy)
    print("diameter charge profile:", diameter)
    print("heavy rigidity: (relations, rank, nullity) = (948, 118, 2)")
    print("diameter rigidity: (relations, rank, nullity) = (266, 85, 5)")
    print("affine quarter-turn occupancy:", sorted(occupancy.items()))
    print("integer parabola n=1000: 499500 distinct distances")
    print("FIXED-ROW LONGEST-BOOK AUDIT: PASS")


if __name__ == "__main__":
    main()
