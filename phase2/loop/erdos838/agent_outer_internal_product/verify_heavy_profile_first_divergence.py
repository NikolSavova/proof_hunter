#!/usr/bin/env python3
"""Exact audit for HEAVY_PROFILE_FIRST_DIVERGENCE.md."""

import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_recoverable_component_toggle as oval  # noqa: E402


def main():
    s, r, m = 5, 2, 4
    a_point = oval.circle(F(-2))
    b_point = oval.circle(F(2))
    pocket_parameters = (F(-3, 25), F(-1, 25), F(3, 100), F(11, 100))
    guard_parameters = (F(3), F(4), F(6), F(-7), F(-4))

    points = [a_point, b_point]
    pocket = tuple(range(len(points), len(points) + m))
    points.extend(oval.circle(t) for t in pocket_parameters)
    guard_pool = tuple(range(len(points), len(points) + s))
    points.extend(oval.circle(t) for t in guard_parameters)
    z = len(points)
    points.append((F(4), F(1, 7)))

    a, b = 0, 1
    base = (a, b)
    root = tuple(sorted((a, b, z)))
    n = len(points)

    assert all(oval.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert oval.convex(base + pocket + guard_pool, points)

    profiles = []
    completion_outputs = Counter()
    shadow_outputs = set()
    carrier_records = 0
    for chosen in combinations(guard_pool, r):
        guard = tuple(sorted((z,) + chosen))
        source = tuple(sorted(base + guard))
        assert oval.convex(source, points)
        assert root in oval.canonical_triples(source, points)

        neighbors = []
        for label in range(n):
            if label in root:
                continue
            if not oval.convex(tuple(sorted(root + (label,))), points):
                neighbors.append(label)
        assert tuple(neighbors) == pocket

        released_base = set(source) - set(guard)
        assert released_base == set(base)
        for x in pocket:
            output = tuple(sorted(released_base | {x}))
            assert oval.convex(output, points)
            completion_outputs[output] += 1

        # Every profile contributes its rooted guard downset.  Restoring z
        # also restores the whole root, so mixing any pocket label is bad.
        for d in oval.powerset(chosen):
            output = tuple(sorted(set(base) | {z} | set(d)))
            assert oval.convex(output, points)
            shadow_outputs.add(output)
            carrier_records += 1
            for x in pocket:
                assert not oval.convex(tuple(sorted(set(output) | {x})), points)
        profiles.append((source, guard))

    assert len(profiles) == 10
    assert len({source for source, _ in profiles}) == 10
    assert sum(completion_outputs.values()) == 10 * m == 40
    assert len(completion_outputs) == m == 4
    assert set(completion_outputs.values()) == {10}
    assert carrier_records == 10 * (2 ** r) == 40
    assert len(shadow_outputs) == 1 + s + 10 == 16

    # Exhaustively confirm the shadow is exactly all levels at most r.
    expected_shadow = {
        tuple(sorted(set(base) | {z} | set(d)))
        for size in range(r + 1)
        for d in combinations(guard_pool, size)
    }
    assert shadow_outputs == expected_shadow

    all_faces = [face for face in oval.powerset(tuple(range(n)))
                 if oval.convex(face, points)]
    rank = max(map(len, all_faces))

    print("PASS: heavy-profile first-divergence regression")
    print(f"  n={n}, profiles=C({s},{r})={len(profiles)}, source rank={r+3}")
    print(f"  completion records: 40 -> {len(completion_outputs)} outputs")
    print(f"  guard-shadow records: 40 -> {len(shadow_outputs)} outputs")
    print(f"  full configuration maximum face rank: {rank}")


if __name__ == "__main__":
    main()
