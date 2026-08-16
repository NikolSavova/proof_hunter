#!/usr/bin/env python3
"""Exact audit for CIRCUIT_TRANSVERSAL_CENTRAL_LAYER_BARRIER.md."""

import sys
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_recoverable_component_toggle as geom  # noqa: E402


def projected_traces(fixed, core, points):
    universe = tuple(sorted(set(fixed) | set(core)))
    return tuple(sorted(set(
        tuple(x for x in witness if x in core)
        for witness in geom.bad_circuits(universe, points)
    )))


def independent(subset, traces):
    subset = set(subset)
    return not any(set(edge) <= subset for edge in traces)


def minimum_transversals(core, traces):
    for size in range(len(core) + 1):
        answers = tuple(
            chosen for chosen in combinations(core, size)
            if all(set(chosen) & set(edge) for edge in traces)
        )
        if answers:
            return answers
    raise AssertionError("an empty trace has no transversal")


def matching_number(traces):
    answer = 0
    for size in range(1, len(traces) + 1):
        if any(all(set(left).isdisjoint(right)
                   for left, right in combinations(chosen, 2))
               for chosen in combinations(traces, size)):
            answer = size
    return answer


def audit_nonempty_circuit_complex():
    # The first ten labels are a fixed exact general-position configuration.
    points = [
        (F(6), F(10)), (F(-3), F(-3)), (F(-1), F(-11)),
        (F(-4), F(-12)), (F(8), F(8)), (F(11), F(2)),
        (F(11), F(10)), (F(-4), F(-3)), (F(-7), F(-10)),
        (F(-5), F(-1)),
    ]
    pocket_points = [
        (F(-29, 5), F(-157, 15)),
        (F(-331, 58), F(-603, 58)),
        (F(-43, 7), F(-361, 35)),
        (F(-14, 3), F(-193, 18)),
        (F(-40, 7), F(-32, 3)),
    ]
    pocket = tuple(range(len(points), len(points) + len(pocket_points)))
    points.extend(pocket_points)

    root = tuple(sorted((8, 3, 2)))
    z = 3
    carrier = (2, 8)
    core = (0, 1, 4, 5, 6, 7)
    fixed = tuple(sorted(set(carrier) | {z}))

    assert all(geom.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    guards = tuple(
        chosen for chosen in combinations(core, 4)
        if geom.convex(fixed + chosen, points)
    )
    assert len(guards) == 6
    assert set().union(*(set(chosen) for chosen in guards)) == set(core)
    assert all(root in geom.canonical_triples(fixed + chosen, points)
               for chosen in guards)

    # These are actual root-pocket labels and singleton completions.
    assert all(not geom.convex(root + (x,), points) for x in pocket)
    assert all(geom.convex(carrier + (x,), points) for x in pocket)

    traces = projected_traces(fixed, core, points)
    assert len(traces) == 8
    assert all(1 <= len(edge) <= 4 for edge in traces)
    assert all(independent(chosen, traces) for chosen in guards)

    convex_outputs = []
    for chosen in geom.powerset(core):
        is_face = geom.convex(fixed + chosen, points)
        assert is_face == independent(chosen, traces)
        if is_face:
            convex_outputs.append(chosen)
    assert len(convex_outputs) == 43

    transversals = minimum_transversals(core, traces)
    tau = len(transversals[0])
    nu = matching_number(traces)
    alpha = max(map(len, convex_outputs))
    assert tau == 2
    assert nu == 2
    assert alpha == 4 == len(core) - tau
    assert tau <= 4 * nu

    canonical = transversals[0]
    released = tuple(x for x in core if x not in canonical)
    assert len(released) == 4
    assert all(geom.convex(fixed + chosen, points)
               for chosen in geom.powerset(released))
    return len(convex_outputs), tau, nu


def audit_central_parabola_barrier():
    parabola = lambda t: (t, F(1) - t * t)
    parameters = (
        F(-1), F(1), F(0), F(-1, 2), F(-2, 5), F(-3, 10),
        F(-1, 5), F(1, 5), F(3, 10), F(2, 5), F(1, 2),
    )
    points = [parabola(t) for t in parameters]
    a, b, z = 0, 1, 2
    root = tuple(sorted((a, b, z)))
    carrier = (a, b)
    core = tuple(range(3, 11))
    pocket_points = [
        (x, F(1, 20) + x * x / F(50))
        for x in (F(-2, 5), F(-1, 5), F(0), F(1, 6), F(1, 3))
    ]
    pocket = tuple(range(len(points), len(points) + len(pocket_points)))
    points.extend(pocket_points)

    assert all(geom.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))
    complete_union = root + core
    assert geom.convex(complete_union, points)

    guards = tuple(combinations(core, 4))
    assert len(guards) == 70
    assert all(geom.convex(root + chosen, points) for chosen in guards)
    assert all(root in geom.canonical_triples(root + chosen, points)
               for chosen in guards)

    union_bank = set()
    for chosen in geom.powerset(core):
        output = tuple(sorted(set(root) | set(chosen)))
        assert geom.convex(output, points)
        union_bank.add(output)
    assert len(union_bank) == 2 ** 8 == 256
    assert projected_traces(root, core, points) == ()

    completion_bank = set()
    for x in pocket:
        completion = tuple(sorted(carrier + (x,)))
        assert geom.convex(completion, points)
        assert not geom.convex(root + (x,), points)
        completion_bank.add(completion)
        for u in core:
            assert not geom.convex(carrier + (x, u), points)
        for chosen in geom.powerset(core):
            if chosen:
                assert not geom.convex(carrier + (x,) + chosen, points)
    assert len(completion_bank) == 5

    # Delete one middle-layer guard.  Its four-trace is uncovered although
    # the geometric projected-circuit hypergraph is still empty.
    uncovered = guards[0]
    incomplete = guards[1:]
    assert len(incomplete) == 69
    assert not any(set(uncovered) <= set(chosen) for chosen in incomplete)
    assert all(geom.convex(root + chosen, points) for chosen in incomplete)
    assert projected_traces(root, core, points) == ()

    k, cube, m = 70, 256, 5
    assert k * k == 4900
    assert m * cube == 1280
    assert F(k * k, m * cube) == F(245, 64)
    assert F(k, 2 ** 4) == F(35, 8)

    b_rank = 2
    q_rank = 11
    n = len(points)
    union_overlap = 3 * len(tuple(combinations(range(q_rank), 3)))
    completion_overlap = n * len(tuple(combinations(range(b_rank + 1), 2)))
    assert union_overlap == 495
    assert completion_overlap == 48
    return k, cube, m, union_overlap, completion_overlap


def main():
    faces, tau, nu = audit_nonempty_circuit_complex()
    k, cube, m, union_overlap, completion_overlap = (
        audit_central_parabola_barrier()
    )
    print("PASS: circuit-transversal and central-layer barrier")
    print(f"  projected complex: faces={faces}, tau={tau}, matching={nu}")
    print(f"  central layer: k={k}, cube={cube}, completions={m}")
    print("  incomplete oval layer: 69/70 guards, uncovered trace, zero circuits")
    print("  mixed carrier/core/completion outputs: zero")
    print(f"  exact decoder overlaps: L_J={union_overlap}, L_C={completion_overlap}")
    print("  local square constant=245/64; ideal root-loss factor=35/8")


if __name__ == "__main__":
    main()
