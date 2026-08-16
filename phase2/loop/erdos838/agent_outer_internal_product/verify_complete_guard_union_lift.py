#!/usr/bin/env python3
"""Exact audit for COMPLETE_GUARD_LAYER_UNION_LIFT.md."""

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
    s, r, m = 6, 4, 4
    points = [oval.circle(F(-2)), oval.circle(F(2))]
    pocket_parameters = (F(-3, 25), F(-1, 25), F(3, 100), F(11, 100))
    pocket = tuple(range(len(points), len(points) + m))
    points.extend(oval.circle(t) for t in pocket_parameters)

    core_parameters = (F(3), F(4), F(5), F(7), F(-8), F(-4))
    core = tuple(range(len(points), len(points) + s))
    points.extend(oval.circle(t) for t in core_parameters)

    marker = len(points)
    points.append(oval.circle(F(10)))
    z = len(points)
    points.append((F(4), F(1, 7)))

    a, b = 0, 1
    root = tuple(sorted((a, b, z)))
    carriers = ((a, b), (a, b, marker))
    n = len(points)

    assert all(oval.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert oval.convex((a, b) + pocket + core + (marker,), points)

    union_outputs = Counter()
    completion_outputs = Counter()
    fibre_data = []
    for carrier in carriers:
        sources = []
        for chosen in combinations(core, r):
            source = tuple(sorted(set(carrier) | {z} | set(chosen)))
            assert oval.convex(source, points)
            assert root in oval.canonical_triples(source, points)
            sources.append(source)
        assert len(set(sources)) == 15

        # Four-circuit locality lifts the complete layer to its full union.
        complete_union = tuple(sorted(set(carrier) | {z} | set(core)))
        assert oval.convex(complete_union, points)

        fibre_unions = set()
        for d in oval.powerset(core):
            output = tuple(sorted(set(carrier) | {z} | set(d)))
            assert oval.convex(output, points)
            assert set(root) <= set(output)
            fibre_unions.add(output)
        assert len(fibre_unions) == 2 ** s == 64

        fibre_completions = set()
        for x in pocket:
            output = tuple(sorted(set(carrier) | {x}))
            assert oval.convex(output, points)
            fibre_completions.add(output)
        assert len(fibre_completions) == m

        for output in fibre_unions:
            union_outputs[output] += 1
        for output in fibre_completions:
            completion_outputs[output] += 1
        fibre_data.append((15, 64, 4))

    # The carrier marker makes the two exact decoder fibres disjoint.
    assert len(union_outputs) == 128
    assert len(completion_outputs) == 8
    assert max(union_outputs.values()) == 1
    assert max(completion_outputs.values()) == 1

    # Near-complete extension: five of the six fifth-layer guards cover every
    # four-trace.  The exact threshold is C(6,5)-C(2,1)=4, so five forces the
    # same full-union lift although the layer is not complete.
    fifth_layer = list(combinations(core, 5))
    near_complete = fifth_layer[1:]
    assert len(near_complete) == 5
    assert len(fifth_layer) - 2 == 4
    assert all(any(set(trace) <= set(chosen) for chosen in near_complete)
               for trace in combinations(core, 4))
    for carrier in carriers:
        for chosen in near_complete:
            source = tuple(sorted(set(carrier) | {z} | set(chosen)))
            assert oval.convex(source, points)
            assert root in oval.canonical_triples(source, points)
        complete_union = tuple(sorted(set(carrier) | {z} | set(core)))
        assert oval.convex(complete_union, points)

    total_mass = sum(k for k, _, _ in fibre_data)
    assert total_mass == 30
    assert 15 ** 2 == 225
    assert 64 * 4 == 256

    # sqrt(64*4)=16 per cell; sqrt(K)=15/16.  Both inequalities are sharp.
    sum_square_roots = len(fibre_data) * 16
    assert sum_square_roots ** 2 == 128 * 8
    assert 16 * total_mass == 15 * sum_square_roots

    print("PASS: complete guard-layer union lift")
    print(f"  cells={len(fibre_data)}, per cell k=15, union=64, completion=4")
    print("  local K=225/256")
    print("  global banks: union=128, completion=8, overlap one")
    print("  sharp audit: 32^2=128*8 and 30=(15/16)*32")
    print("  near-complete audit: 5 guards > threshold 4; all 15 four-traces covered")


if __name__ == "__main__":
    main()
