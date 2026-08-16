#!/usr/bin/env python3
"""Exact audit for CROSS_ANCHOR_COMPLETION_TELESCOPE.md."""

import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_recoverable_component_toggle as geom  # noqa: E402


def main():
    parabola = lambda t: (t, F(1) - t * t)
    outer_parameters = tuple(F(i, 40) for i in range(-9, 0)) + tuple(
        F(i, 40) for i in range(1, 10)
    )
    points = [parabola(F(-1)), parabola(F(1))]
    outer = tuple(range(2, 2 + len(outer_parameters)))
    points.extend(parabola(t) for t in outer_parameters)
    groups = (outer[:9], outer[9:])

    pocket_points = [
        (x, F(1, 20) + x * x / F(50))
        for x in (F(-2, 5), F(-1, 5), F(0), F(1, 6), F(1, 3))
    ]
    pocket = tuple(range(len(points), len(points) + len(pocket_points)))
    points.extend(pocket_points)

    carrier = (0, 1)
    r = 4
    k = math.comb(2 * r, r)
    m = len(pocket)
    assert k == 70 and m == 5
    assert all(geom.cross(points[i], points[j], points[jj]) != 0
               for i, j, jj in combinations(range(len(points)), 3))

    completion_sets = {}
    completion_records = defaultdict(Counter)
    top_faces = []
    cell_count = 0
    marked_mass = 0

    for group_index, outer_group in enumerate(groups):
        top = tuple(sorted(carrier + outer_group))
        assert geom.convex(top, points)
        top_faces.append(top)
        local_completions = set()

        for z in outer_group:
            root = tuple(sorted(carrier + (z,)))
            core = tuple(x for x in outer_group if x != z)
            assert len(core) == 2 * r
            guards = tuple(combinations(core, r))
            assert len(guards) == k
            for chosen in guards:
                source = root + chosen
                assert geom.convex(source, points)
                assert root in geom.canonical_triples(source, points)
                marked_mass += 1

            for x in pocket:
                output = tuple(sorted(carrier + (x,)))
                assert geom.convex(output, points)
                assert not geom.convex(root + (x,), points)
                completion_records[group_index][output] += 1
                local_completions.add(output)
                for u in core:
                    assert not geom.convex(carrier + (x, u), points)
            cell_count += 1

        completion_sets[group_index] = local_completions

    assert len(set(top_faces)) == 2
    assert cell_count == 18
    assert marked_mass == 18 * 70 == 1260

    # Exact actual overlap parameters.
    r_group = 9
    within_overlap = max(
        count for records in completion_records.values()
        for count in records.values()
    )
    assert within_overlap == 9
    assert all(len(outputs) == m for outputs in completion_sets.values())
    cross_overlap = Counter()
    for outputs in completion_sets.values():
        for output in outputs:
            cross_overlap[output] += 1
    rho = max(cross_overlap.values())
    assert rho == 2
    assert sum(map(len, completion_sets.values())) == 10

    # Decoder cap lambda <= q*C(b+1,2).
    q_rank = 11
    b_rank = 2
    conditional_cap = q_rank * math.comb(b_rank + 1, 2)
    assert conditional_cap == 33 >= within_overlap

    # The groupwise inequality and global Cauchy step are both sharp with
    # actual overlaps: K=(k^2*lambda*R/m).
    local_k = F(k * k * within_overlap * r_group, m)
    assert local_k == 79380
    assert marked_mass * marked_mass == local_k * 2 * 10

    # A shared completion output first-diverges into two top groups with the
    # same pocket label, carrier, and retained edge, but distinct root labels.
    shared_output = min(cross_overlap)
    x = next(label for label in shared_output if label not in carrier)
    chosen_roots = []
    for outer_group in groups:
        z = min(outer_group)
        root = tuple(sorted(carrier + (z,)))
        assert not geom.convex(root + (x,), points)
        chosen_roots.append(z)
    assert len(set(chosen_roots)) == 2
    assert all(z in top for z, top in zip(chosen_roots, top_faces))

    print("PASS: cross-anchor completion telescope")
    print(f"  top groups=2, cells={cell_count}, marked mass={marked_mass}")
    print("  actual parameters: R=9, lambda=9, rho=2, m=5, k=70")
    print("  completion sets: 5+5 records as sets, all cross-collide")
    print("  conditioned decoder cap=33")
    print("  sharp global identity: 1260^2=79380*2*10")
    print("  first-divergence star: common B,x,e; two distinct z and top shields")
    print("  all carrier/core/pocket mixed outputs rejected")


if __name__ == "__main__":
    main()
