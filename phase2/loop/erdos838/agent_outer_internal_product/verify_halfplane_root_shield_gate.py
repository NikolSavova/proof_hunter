#!/usr/bin/env python3
"""Exact audit for HALFPLANE_ROOT_SHIELD_GATE.md."""

import math
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_recoverable_component_toggle as geom  # noqa: E402


def powerset(labels):
    labels = tuple(labels)
    for size in range(len(labels) + 1):
        yield from combinations(labels, size)


def canonical_richer_side(points, x, z, top):
    positive = tuple(u for u in top if u != z
                     and geom.cross(points[x], points[z], points[u]) > 0)
    negative = tuple(u for u in top if u != z
                     and geom.cross(points[x], points[z], points[u]) < 0)
    assert len(positive) + len(negative) == len(top) - 1
    return max((positive, negative), key=lambda side: (len(side), side))


def main():
    parabola = lambda t: (t, F(1) - t * t)
    parameters = (
        F(-1), F(1), F(0), F(-1, 2), F(-2, 5), F(-3, 10),
        F(-1, 5), F(1, 5), F(3, 10), F(2, 5), F(1, 2),
    )
    points = [parabola(t) for t in parameters]
    carrier = (0, 1)
    roots = tuple(range(2, 11))
    top = tuple(sorted(carrier + roots))

    pocket_points = [
        (x, F(1, 20) + x * x / F(50))
        for x in (F(-2, 5), F(-1, 5), F(0), F(1, 6), F(1, 3))
    ]
    pocket = tuple(range(len(points), len(points) + len(pocket_points)))
    points.extend(pocket_points)

    assert all(geom.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    assert geom.convex(top, points)
    q = len(top)
    r = 4
    k_weight = math.comb(2 * r, r)
    assert q == 11 and k_weight == 70

    all_records = Counter()
    fixed_star_records = None
    side_sizes = []

    for x in pocket:
        star_records = Counter()
        for z in roots:
            root = tuple(sorted(carrier + (z,)))
            assert not geom.convex(root + (x,), points)
            side = canonical_richer_side(points, x, z, top)
            assert len(side) >= math.ceil((q - 1) / 2) == 5
            side_sizes.append(len(side))

            for chosen in powerset(side):
                output = tuple(sorted((x, z) + chosen))
                assert geom.convex(output, points)
                star_records[output] += 1
                all_records[output] += 1

        assert sum(star_records.values()) == 1952
        assert len(star_records) == 1487
        assert max(star_records.values()) == 2 <= q
        if fixed_star_records is None:
            fixed_star_records = star_records

    assert Counter(side_sizes) == Counter({9: 10, 8: 10, 7: 10,
                                           6: 10, 5: 5})
    assert sum(all_records.values()) == 9760
    assert len(all_records) == 7435
    assert max(all_records.values()) == 2 <= q

    # Root-marked top downsets: every record retains z, so its load is at
    # most the output rank.  In the common-top regression the exact degree is
    # the number of selected root labels.
    downset_records = Counter()
    for z in roots:
        remaining = tuple(u for u in top if u != z)
        for chosen in powerset(remaining):
            output = tuple(sorted((z,) + chosen))
            assert geom.convex(output, points)
            downset_records[output] += 1
    assert sum(downset_records.values()) == len(roots) * 2 ** (q - 1) == 9216
    assert len(downset_records) == 2 ** q - 2 ** len(carrier) == 2044
    assert max(downset_records.values()) == len(roots) == 9 <= q

    # The finite central example lies on the wrong side of the exponent gate.
    coefficient = F(q * k_weight, 2 ** 5)
    assert coefficient == F(385, 16)
    marked_mass_one_star = len(roots) * k_weight
    assert marked_mass_one_star == 630

    print("PASS: half-plane root-shield gate")
    print("  q=11, roots=9, r=4, k=70, pocket labels=5")
    print("  side sizes: 5 once and 6,7,8,9 twice per pocket label")
    print("  one star: records=1952, faces=1487, max load=2")
    print("  all five stars: records=9760, faces=7435, max load=2")
    print("  root downsets: records=9216, faces=2044, max load=9")
    print("  theorem load cap=11")
    print(f"  small-carrier coefficient=qk/2^5={coefficient}")


if __name__ == "__main__":
    main()
