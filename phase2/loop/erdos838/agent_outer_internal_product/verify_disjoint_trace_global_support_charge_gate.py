#!/usr/bin/env python3
"""Exact checks for DISJOINT_TRACE_GLOBAL_SUPPORT_CHARGE_GATE.md."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import ceil, comb, log2
from pathlib import Path
import importlib.util
import sys


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
PASCAL_VERIFIER = (
    ERDOS
    / "agent_common_shield_mixing"
    / "verify_live_pascal_common_guard_barrier.py"
)


def binomial_sum(n, d):
    return sum(comb(n, i) for i in range(min(n, d) + 1))


def matched_trace_shadow_audit():
    # Two physical sources, four pocket histories per row, and three
    # disjoint traces of ranks 1,2,3.  The common labels 0,1 model a
    # retained exposed edge.
    sources = (
        frozenset(range(8)),
        frozenset((0, 1, 8, 9, 10, 11, 12, 13)),
    )
    traces = (
        (frozenset((2,)), frozenset((3, 4)), frozenset((5, 6, 7))),
        (frozenset((8,)), frozenset((9, 10)), frozenset((11, 12, 13))),
    )
    pocket_degree = 4
    record_weight = Fraction(1, pocket_degree)
    output_load = defaultdict(Fraction)
    total_weight = Fraction()
    incidence_weight = Fraction()
    s = 3

    for source, trace_system in zip(sources, traces):
        assert all(trace for trace in trace_system)
        assert sum(map(len, trace_system)) == 6
        assert all(
            first.isdisjoint(second)
            for first, second in combinations(trace_system, 2)
        )
        for _pocket in range(pocket_degree):
            total_weight += record_weight
            for mask in range(1 << s):
                deleted = set()
                for i, trace in enumerate(trace_system):
                    if mask >> i & 1:
                        deleted.update(trace)
                output = source - deleted
                assert {0, 1}.issubset(output)
                output_load[output] += record_weight
                incidence_weight += record_weight

    assert total_weight == len(sources)
    assert incidence_weight == (1 << s) * total_weight
    rho = 1  # row normalization
    n = 14
    assert max(output_load.values()) <= rho * binomial_sum(n, 3 * s)
    assert incidence_weight <= rho * binomial_sum(n, 3 * s) * len(output_load)
    rank_counts = Counter(map(len, output_load))
    r = len(sources[0])
    refined_rhs = rho * sum(
        comb(n - q, r - q) * count
        for q, count in rank_counts.items()
        if r - 3 * s <= q <= r
    )
    assert incidence_weight <= refined_rhs
    # Pocket histories cancel locally: each toggle output has load one per
    # source row after the 1/H normalization.  The fully deleted output is
    # the common retained edge and is shared by the two source rows.
    assert set(output_load.values()) == {Fraction(1), Fraction(2)}
    assert max(output_load.values()) == len(sources)
    return len(output_load), max(output_load.values())


def det(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def ordinary(points):
    return len(set(points)) == len(points) and len(hull(points)) == len(points)


def four_cover_audit():
    # The logical four-cover: every possible crossing four-set is captured
    # by B plus one completion.
    B = frozenset(range(3))
    Q = frozenset(range(3, 9))
    completions = tuple(frozenset(U) for U in combinations(Q, 4))
    for size in range(1, 5):
        for trace in combinations(Q, size):
            assert any(set(trace) <= U for U in completions)
    captured = 0
    for circuit in combinations(B | Q, 4):
        trace = set(circuit) & Q
        if not trace:
            continue
        assert any(trace <= U and set(circuit) <= B | U for U in completions)
        captured += 1

    # A literal convex realization gives all 2^|Q| rooted outputs.
    points = [(Fraction(x), Fraction(x * x)) for x in range(-4, 5)]
    base_points = points[:3]
    q_points = points[3:]
    assert ordinary(points)
    outputs = set()
    for mask in range(1 << len(q_points)):
        output = tuple(
            sorted(
                base_points
                + [q_points[i] for i in range(len(q_points)) if mask >> i & 1]
            )
        )
        assert ordinary(list(output))
        outputs.add(output)
    assert len(outputs) == 1 << len(q_points) == 64

    # Necessity calibration: singleton completion traces need not lift.
    q = 2
    delta = Fraction(1, 100 * q * q)
    u, v, w = (Fraction(-2), Fraction(0)), (Fraction(2), Fraction(0)), (
        Fraction(0),
        Fraction(6),
    )
    m, nvec, dvec = (Fraction(1), Fraction(3)), (
        Fraction(3),
        Fraction(1),
    ), (Fraction(-2), Fraction(6))

    def a(t):
        return (
            m[0] + t * nvec[0] + delta * t * t * dvec[0],
            m[1] + t * nvec[1] + delta * t * t * dvec[1],
        )

    a1, a2 = a(1), a(2)
    assert ordinary([u, v, w, a1])
    assert ordinary([u, v, w, a2])
    assert not ordinary([u, v, w, a1, a2])
    return captured, len(outputs)


def scalar_capacity_audit():
    rows = []
    c = Fraction(49, 100)
    sigma = Fraction(1, 4)
    C = 1
    for L in (64, 96, 128, 192, 256):
        delta = ceil(log2(L))
        v_exp = (49 * L * L) // 100
        k_exp = (L * delta) // 4
        s = ceil(C * delta)
        V0 = 1 << v_exp
        H = 1 << (v_exp - 1)
        K = 1 << k_exp
        assert H + K * (1 << (3 * s)) <= V0
        assert K * H >= V0 * (1 << max(0, k_exp - 2))
        assert k_exp + 3 * s < v_exp - 1
        rows.append((L, delta, s, v_exp, k_exp))
    return rows


def load_pascal_module():
    spec = importlib.util.spec_from_file_location(
        "trace_charge_pascal_verifier", PASCAL_VERIFIER
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def all_nonempty_subsets(indices):
    for size in range(1, len(indices) + 1):
        yield from combinations(indices, size)


def hull_cycle(indices, points, g):
    ordered = sorted(indices, key=lambda index: (points[index].x, points[index].y))

    def build(sequence):
        out = []
        for index in sequence:
            while (
                len(out) >= 2
                and g.det(points[out[-2]], points[out[-1]], points[index]) <= 0
            ):
                out.pop()
            out.append(index)
        return out

    lower = build(ordered)
    upper = build(reversed(ordered))
    cycle = tuple(lower[:-1] + upper[:-1])
    assert set(cycle) == set(indices) and len(cycle) == len(indices)
    return cycle


def pascal_trace_reuse_audit():
    module = load_pascal_module()
    g = module.load_geometry()
    n, h = 6, 3
    points = g.cell(n, h)
    left_size = comb(n - 1, h - 1)
    left = tuple(range(left_size))
    right = tuple(range(left_size, len(points)))
    orient = g.orient_table(points)

    left_faces = [
        face
        for face in all_nonempty_subsets(left)
        if g.is_convex(face, orient)
    ]
    right_faces = [
        face
        for face in all_nonempty_subsets(right)
        if g.is_convex(face, orient)
    ]
    sources = [face for face in left_faces if not g.is_cap(face, orient)]
    pockets = [face for face in right_faces if not g.is_cup(face, orient)]
    assert len(left_faces) == len(right_faces) == 375
    assert len(sources) == len(pockets) == 274

    # Canonical first noncap triple and rank fibre.
    buckets = defaultdict(list)
    for source in sources:
        witnesses = [
            triple
            for triple in combinations(source, 3)
            if not g.is_cap(triple, orient)
        ]
        assert witnesses
        buckets[(min(witnesses), len(source))].append(source)
    root, rank = max(buckets, key=lambda key: len(buckets[key]))
    fibre = buckets[(root, rank)]
    assert len(fibre) == 6 and rank == 5

    # Every singleton source label is a source trace against every pocket.
    singleton_trace_checks = 0
    for source in fibre:
        for pocket in pockets:
            for y in source:
                witnesses = [
                    triple
                    for triple in combinations(pocket, 3)
                    if not g.is_convex(tuple(sorted((y,) + triple)), orient)
                ]
                assert witnesses
                singleton_trace_checks += 1

    # Pigeonhole an actual exposed edge-and-side state.
    edge_fibres = defaultdict(list)
    for source in fibre:
        cycle = hull_cycle(source, points, g)
        for i, first in enumerate(cycle):
            second = cycle[(i + 1) % len(cycle)]
            a, b = sorted((first, second))
            witness = next(x for x in source if x not in (a, b))
            side = (g.det(points[a], points[b], points[witness]) > 0) - (
                g.det(points[a], points[b], points[witness]) < 0
            )
            edge_fibres[(a, b, side)].append(source)
    edge_state, edge_sources = max(edge_fibres.items(), key=lambda item: len(item[1]))
    e0, e1, _side = edge_state
    assert edge_sources
    assert all(e0 in source and e1 in source for source in edge_sources)
    assert all(len(source) - 2 == 3 for source in edge_sources)

    # Every nonempty left downface is incompatible with every selected
    # pocket.  This exhausts the exact reuse claim.
    mixed_checks = 0
    for left_face in left_faces:
        for pocket in pockets:
            assert not g.is_convex(left_face + pocket, orient)
            mixed_checks += 1

    source_downshadow = set()
    for source in fibre:
        for size in range(len(source) + 1):
            source_downshadow.update(frozenset(face) for face in combinations(source, size))
    assert all(
        not face or tuple(sorted(face)) in left_faces for face in source_downshadow
    )
    assert len(source_downshadow) <= len(left_faces) + 1

    # Full deletion sends every source row to the same literal pocket.
    terminal_load = Counter()
    for source in fibre:
        for pocket in pockets:
            terminal_load[frozenset(pocket)] += 1
    assert set(terminal_load.values()) == {len(fibre)}
    assert len(terminal_load) == len(pockets)

    # Row-normalized version: total row weight one and exact terminal load.
    weighted_load = defaultdict(Fraction)
    total_weight = Fraction()
    for source in fibre:
        for pocket in pockets:
            weight = Fraction(1, len(pockets))
            weighted_load[frozenset(pocket)] += weight
            total_weight += weight
    assert total_weight == len(fibre)
    assert set(weighted_load.values()) == {
        Fraction(len(fibre), len(pockets))
    }

    return {
        "fibre": len(fibre),
        "rank": rank,
        "pockets": len(pockets),
        "singleton_trace_checks": singleton_trace_checks,
        "common_edge_sources": len(edge_sources),
        "mixed_checks": mixed_checks,
        "source_downshadow": len(source_downshadow),
        "terminal_load": len(fibre),
    }


def main():
    shadow = matched_trace_shadow_audit()
    four_cover = four_cover_audit()
    scalar = scalar_capacity_audit()
    pascal = pascal_trace_reuse_audit()
    print(
        "PASS: disjoint-trace weighted shadow, four-cover lift, "
        "low-V scalar capacity, and Pascal reuse barrier; "
        f"shadow={shadow}; four-cover={four_cover}; "
        f"scalar={scalar}; Pascal={pascal}"
    )


if __name__ == "__main__":
    main()
