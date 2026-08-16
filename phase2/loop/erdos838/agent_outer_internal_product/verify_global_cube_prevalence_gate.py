#!/usr/bin/env python3
"""Exact audit for GLOBAL_CUBE_PREVALENCE_GATE.md."""

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


def main():
    parabola = lambda t: (t, F(1) - t * t)
    parameters = (
        F(-1), F(1), F(0), F(-1, 2), F(-2, 5), F(-3, 10),
        F(-1, 5), F(1, 5), F(3, 10), F(2, 5), F(1, 2),
    )
    points = [parabola(t) for t in parameters]
    a, b = 0, 1
    carrier = (a, b)
    outer = tuple(range(2, 11))
    r = 4

    pocket_points = [
        (x, F(1, 20) + x * x / F(50))
        for x in (F(-2, 5), F(-1, 5), F(0), F(1, 6), F(1, 3))
    ]
    pocket = tuple(range(len(points), len(points) + len(pocket_points)))
    points.extend(pocket_points)

    assert all(geom.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    assert geom.convex(carrier + outer, points)

    cube_records = Counter()
    completion_records = Counter()
    high_counts = []
    source_count = 0

    for z in outer:
        root = tuple(sorted(carrier + (z,)))
        core = tuple(x for x in outer if x != z)
        assert len(core) == 2 * r == 8

        guards = tuple(combinations(core, r))
        assert len(guards) == math.comb(2 * r, r) == 70
        for chosen in guards:
            source = root + chosen
            assert geom.convex(source, points)
            assert root in geom.canonical_triples(source, points)
            source_count += 1

        local_outputs = set()
        local_high = 0
        for chosen in geom.powerset(core):
            output = tuple(sorted(set(carrier) | {z} | set(chosen)))
            assert geom.convex(output, points)
            local_outputs.add(output)
            cube_records[output] += 1
            if 1 + len(chosen) > r:
                local_high += 1
        assert len(local_outputs) == 2 ** (2 * r) == 256
        high_counts.append(local_high)

        for x in pocket:
            completion = tuple(sorted(carrier + (x,)))
            assert geom.convex(completion, points)
            assert not geom.convex(root + (x,), points)
            completion_records[completion] += 1
            for u in core:
                assert not geom.convex(carrier + (x, u), points)

    p = len(outer)
    assert p == 2 * r + 1 == 9
    assert source_count == p * math.comb(2 * r, r) == 630

    assert sum(cube_records.values()) == p * 2 ** (p - 1) == 2304
    assert len(cube_records) == 2 ** p - 1 == 511
    for output, degree in cube_records.items():
        outer_trace = set(output) & set(outer)
        assert degree == len(outer_trace)
    degree_frequency = Counter(cube_records.values())
    assert all(degree_frequency[d] == math.comb(p, d)
               for d in range(1, p + 1))

    ordered_energy = sum(d * (d - 1) for d in cube_records.values())
    assert ordered_energy == p * (p - 1) * 2 ** (p - 2) == 9216
    pairwise_energy = 0
    roots = list(outer)
    for left in roots:
        for right in roots:
            if left != right:
                pairwise_energy += 2 ** (p - 2)
    assert pairwise_energy == ordered_energy

    expected_high = sum(math.comb(2 * r, size)
                        for size in range(r, 2 * r + 1))
    assert expected_high == 163 > 128
    assert high_counts == [expected_high] * p

    assert sum(completion_records.values()) == p * len(pocket) == 45
    assert len(completion_records) == len(pocket) == 5
    assert set(completion_records.values()) == {p}

    # Exact finite audit of the central ratios in the theorem and regression.
    a_size = 2 ** (2 * r)
    k_weight = math.comb(2 * r, r)
    assert F(k_weight, a_size) == F(35, 128)
    light_coefficient_at_delta_1 = F(2 * k_weight, a_size)
    assert light_coefficient_at_delta_1 == F(35, 64)

    print("PASS: global cube prevalence gate")
    print(f"  cells={p}, marked sources={source_count}")
    print("  cube records=2304, distinct=511, ordered collision energy=9216")
    print("  exact degree law d(B union S)=|S|")
    print("  per-cell degree>4 outputs=163/256")
    print("  completion records=45 -> 5 outputs, overlap 9")
    print("  all carrier/core/pocket mixed outputs rejected")
    print(f"  Delta=1 light coefficient={light_coefficient_at_delta_1}")


if __name__ == "__main__":
    main()
