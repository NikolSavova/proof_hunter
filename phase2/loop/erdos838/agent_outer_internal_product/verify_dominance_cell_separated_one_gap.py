#!/usr/bin/env python3
"""Verifier for DOMINANCE_CELL_SEPARATED_ONE_GAP.md."""

from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def convex(points):
    return len(strict_hull(points)) == len(set(points))


def circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def tangent(point):
    x, y = point
    return ((x + 1) / y, (1 - x) / y)


def planar_pair_bank_audit():
    # Ten rational conic points split into four disjoint cells.  Nonuniform
    # bounded-rank trace alphabets cross-complete, and every local subset is
    # a face.
    sizes = (2, 3, 2, 3)
    trace_rank_bounds = (1, 2, 2, 3)
    parameters = iter(Q(i, 13) for i in range(1, 11))
    cells = [tuple(circle(next(parameters)) for _ in range(size)) for size in sizes]
    all_points = tuple(p for cell in cells for p in cell)
    assert convex(all_points)
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(all_points, 3))

    alphabets = [
        tuple(trace for rank in range(1, rank_bound + 1)
              for trace in combinations(cell, rank))
        for cell, rank_bound in zip(cells, trace_rank_bounds)
    ]
    full_words = tuple(product(*alphabets))
    # A sparse parity subfamily with the same coordinate projections.
    indexed_words = tuple(product(*(range(len(alphabet)) for alphabet in alphabets)))
    sparse_indices = tuple(word for word in indexed_words if sum(word) % 2 == 0)
    sparse = tuple(tuple(alphabets[i][word[i]] for i in range(len(cells)))
                   for word in sparse_indices)
    projections = []
    for i in range(len(cells)):
        projections.append(tuple({word[i] for word in sparse}))
        assert set(projections[-1]) == set(alphabets[i])

    m = [len(a) for a in projections]
    h = [2 ** len(cell) for cell in cells]
    p0 = 1
    for value in m:
        p0 *= value
    assert len(full_words) == p0

    bank_sizes = []
    bank_sets = []
    for gap in range(len(cells)):
        pairs = set()
        other_alphabets = [projections[i] for i in range(len(cells)) if i != gap]
        for traces in product(*other_alphabets):
            first = frozenset(p for trace in traces for p in trace)
            assert convex(tuple(first))
            for mask in range(1 << len(cells[gap])):
                second = frozenset(cells[gap][j] for j in range(len(cells[gap]))
                                   if mask & (1 << j))
                assert convex(tuple(second))
                pairs.add((first, second))
        expected = h[gap] * p0 // m[gap]
        assert len(pairs) == expected
        bank_sizes.append(expected)
        bank_sets.append(pairs)

    lhs = 1
    rhs = 1
    for i in range(len(cells)):
        lhs *= bank_sizes[i]
        rhs *= p0 * h[i] // m[i]
    assert lhs == rhs
    assert len(sparse) == p0 // 2
    return {
        "cells": len(cells),
        "cell_sizes": sizes,
        "trace_rank_bounds": trace_rank_bounds,
        "trace_alphabets": m,
        "full_product": p0,
        "sparse_words": len(sparse),
        "local_reservoirs": h,
        "pair_bank_sizes": bank_sizes,
        "maximum_pair_bank": max(bank_sizes),
        "maximum_pair_bank_exceeds_source_square": max(bank_sizes) > len(sparse) ** 2,
        "cyclic_identity_verified": True,
    }


def rational_mixed_bank_counterexample():
    # Four strict tangent-coordinate intervals.  The source words use one
    # point per cell, while the failed gap output uses a two-point
    # directional profile in the final cell.
    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    q = (Q(-19, 20), Q(1, 20))
    x = (Q(-3, 40), Q(7, 8))
    w = (Q(0), Q(10, 11))
    z = (Q(3, 40), Q(7, 8))
    y = (Q(2, 15), Q(8, 9))
    points = (u, v, q, x, w, z, y)
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(points, 3))

    tq, tx, tw, tz, ty = tangent(q), tangent(x), tangent(w), tangent(z), tangent(y)
    assert tq == (Q(1), Q(39))
    assert tx == (Q(37, 35), Q(43, 35))
    assert tw == (Q(11, 10), Q(11, 10))
    assert tz == (Q(43, 35), Q(37, 35))
    assert ty == (Q(51, 40), Q(39, 40))
    assert tq[0] < tx[0] < tw[0] < tz[0] < ty[0]
    assert tq[1] > tx[1] > tw[1] > tz[1] > ty[1] > 0

    # Cells are {q},{x},{w},{z,y}; the final selected trace is {z} or {y}.
    assert convex((u, v, q, x, w, z))
    assert convex((u, v, q, x, w, y))
    assert convex((u, v, z, y))
    assert convex((z, y))

    # Omit {w}; the adjacent singleton profile {x}, two-point directional
    # profile {z,y}, and other singleton {q} fail even without the root:
    # z is strictly inside triangle {q,x,y}.
    weights = (Q(3, 230), Q(122, 575), Q(891, 1150))
    assert sum(weights) == 1
    reconstructed = tuple(weights[0] * q[i] + weights[1] * x[i] + weights[2] * y[i]
                          for i in range(2))
    assert reconstructed == z
    assert all(weight > 0 for weight in weights)
    assert not convex((q, x, z, y))
    assert not convex((u, v, q, x, z, y))
    return {
        "general_position": True,
        "positive_reverse_dominance": True,
        "cell_occupancies": (1, 1, 1, 1),
        "cross_complete_singleton_choices": 2,
        "directional_one_gap_face_convex_without_root": False,
        "directional_one_gap_face_convex_with_root": False,
        "interior_point": "z",
        "barycentric_weights": [str(weight) for weight in weights],
    }


def main():
    certificate = {
        "separated_pair_bank": planar_pair_bank_audit(),
        "ordinary_mixed_bank_counterexample": rational_mixed_bank_counterexample(),
    }
    out = Path(__file__).with_name("dominance_cell_separated_one_gap_certificate.json")
    out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
