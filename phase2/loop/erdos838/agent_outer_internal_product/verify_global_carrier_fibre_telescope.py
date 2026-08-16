#!/usr/bin/env python3
"""Exact audit for GLOBAL_CARRIER_FIBRE_TELESCOPE.md."""

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
    points = [oval.circle(F(-2)), oval.circle(F(2))]
    pocket_parameters = (F(-3, 25), F(-1, 25), F(3, 100), F(11, 100))
    pocket = tuple(range(len(points), len(points) + m))
    points.extend(oval.circle(t) for t in pocket_parameters)

    guard_parameters = (F(3), F(4), F(6), F(-7), F(-4))
    guard_pool = tuple(range(len(points), len(points) + s))
    points.extend(oval.circle(t) for t in guard_parameters)

    # A fixed carrier marker on the same outer oval creates a second fibre.
    marker = len(points)
    points.append(oval.circle(F(8)))
    z = len(points)
    points.append((F(4), F(1, 7)))

    a, b = 0, 1
    root = tuple(sorted((a, b, z)))
    carriers = ((a, b), (a, b, marker))
    n = len(points)

    assert all(oval.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))
    assert oval.convex((a, b) + pocket + guard_pool + (marker,), points)

    shadow_outputs = Counter()
    completion_outputs = Counter()
    fibre_data = []
    for carrier in carriers:
        sources = []
        fibre_shadows = set()
        fibre_completions = set()
        for chosen in combinations(guard_pool, r):
            guard = tuple(sorted((z,) + chosen))
            source = tuple(sorted(set(carrier) | set(guard)))
            assert oval.convex(source, points)
            assert root in oval.canonical_triples(source, points)
            assert set(source) - set(guard) == set(carrier)

            for x in pocket:
                output = tuple(sorted(set(carrier) | {x}))
                assert oval.convex(output, points)
                fibre_completions.add(output)

            for d in oval.powerset(chosen):
                output = tuple(sorted(set(carrier) | {z} | set(d)))
                assert oval.convex(output, points)
                fibre_shadows.add(output)
            sources.append(source)

        assert len(set(sources)) == 10
        assert len(fibre_shadows) == 16
        assert len(fibre_completions) == 4
        for output in fibre_shadows:
            shadow_outputs[output] += 1
        for output in fibre_completions:
            completion_outputs[output] += 1
        fibre_data.append((10, 16, 4))

    # The marker makes both carrier fibres exactly recoverable in this audit.
    assert len(shadow_outputs) == 32
    assert len(completion_outputs) == 8
    assert max(shadow_outputs.values()) == 1
    assert max(completion_outputs.values()) == 1

    total_mass = sum(k for k, _, _ in fibre_data)
    local_numerator = 10 ** 2
    local_denominator = 16 * 4
    assert (local_numerator, local_denominator) == (100, 64)

    # Both the local square comparison and the global Cauchy step are exact:
    # sqrt(16*4)=8 per fibre and sqrt(K)=5/4.
    sum_square_roots = len(fibre_data) * 8
    assert sum_square_roots ** 2 == 32 * 8
    assert 4 * total_mass == 5 * sum_square_roots

    # With exact overlap one, the theorem says W <= sqrt(K)*V.  It is enough
    # to audit against the union of the two banks, which contains 40 faces;
    # the ambient face count is larger.
    bank_union = set(shadow_outputs) | set(completion_outputs)
    assert len(bank_union) == 40
    assert total_mass ** 2 * local_denominator <= (
        local_numerator * len(bank_union) ** 2)

    print("PASS: global carrier-fibre telescope")
    print(f"  fibres={len(fibre_data)}, total weighted mass={total_mass}")
    print("  per fibre: k=10, shadow=16, completion=4, K=25/16")
    print("  global banks: shadow=32, completion=8, overlap one")
    print("  sharp Cauchy audit: 16^2=32*8 and 20=(5/4)*16")
    print(f"  no per-fibre V spend; audited against one {len(bank_union)}-face union")


if __name__ == "__main__":
    main()
