#!/usr/bin/env python3
"""Exact checks for DOUBLE_BAD_PREFIX_HALL_THRESHOLD_AND_HALF_BARRIER."""

from __future__ import annotations

import itertools
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402
from agent_common_shield_mixing.verify_two_anchor_double_circuit_elimination_gate import (  # noqa: E402
    canonical_bad_sides,
    is_chain,
    is_convex,
)


def hall_two_target_audit() -> F:
    # K_{lambda,kappa}: left degree kappa, right degree lambda.
    kappa, lam = 3, 4
    edges = tuple((x, y) for x in range(lam) for y in range(kappa))
    best = F(0)
    for mask in range(1, 1 << len(edges)):
        left = set()
        right = set()
        mass = 0
        for index, (x, y) in enumerate(edges):
            if mask >> index & 1:
                mass += 1
                left.add(x)
                right.add(y)
        best = max(best, F(mass, len(left) + len(right)))
    harmonic = F(kappa * lam, kappa + lam)
    assert best == harmonic == F(12, 7)
    assert len(edges) == harmonic * (kappa + lam)
    assert max(sum(x == xx for x, _ in edges) for xx in range(lam)) == kappa
    assert max(sum(y == yy for _, y in edges) for yy in range(kappa)) == lam
    assert len(set(edges)) == len(edges)  # pair load one
    return best


def hall_three_target_audit() -> F:
    # Complete 2x2x2 product. Every marginal load is four and the full
    # family attains the three-way harmonic Hall constant 4/3.
    records = tuple(itertools.product(range(2), repeat=3))
    best = F(0)
    for mask in range(1, 1 << len(records)):
        supports = [set(), set(), set()]
        mass = 0
        for index, record in enumerate(records):
            if mask >> index & 1:
                mass += 1
                for coordinate in range(3):
                    supports[coordinate].add(record[coordinate])
        best = max(best, F(mass, sum(map(len, supports))))
    marginal = 4
    harmonic = F(1, 3 * F(1, marginal))
    assert best == harmonic == F(4, 3)
    assert len(records) == harmonic * 6
    for pair in ((0, 1), (0, 2), (1, 2)):
        loads = Counter((record[pair[0]], record[pair[1]]) for record in records)
        assert max(loads.values()) == 2
    assert len(set(records)) == len(records)  # triple load one
    return best


def pascal_double_bad_audit() -> tuple[int, int, int, int, int, int]:
    q = sorted(rt.pascal_cell(4, 2, F(1, 97)))
    points = rt.strong_glue(q, q, F(1, 16384))
    assert rt.evaluate(sorted(points))[:3] == (248, 248, 1061)
    left, right = canonical_bad_sides(q)

    source_loads: Counter[tuple[int, ...]] = Counter()
    seam_loads: Counter[tuple[int, ...]] = Counter()
    pair_loads: Counter[tuple[tuple[int, ...], tuple[int, ...]]] = Counter()
    for (cap, y), a_pair in left.items():
        for (cup, z_local), b_pair in right.items():
            z = z_local + 6
            b_physical = (b_pair[0] + 6, b_pair[1] + 6)
            detached = tuple(
                [i for i in range(6) if cap >> i & 1]
                + [i + 6 for i in range(6) if cup >> i & 1]
            )
            seam = tuple(sorted((min(a_pair), y, z, min(b_physical))))
            assert is_convex([points[i] for i in detached])
            assert is_convex([points[i] for i in seam])
            source_loads[detached] += 1
            seam_loads[seam] += 1
            pair_loads[detached, seam] += 1

    mass = sum(source_loads.values())
    values = (
        mass,
        len(source_loads),
        len(seam_loads),
        max(source_loads.values()),
        max(seam_loads.values()),
        max(pair_loads.values()),
    )
    assert values == (3600, 625, 121, 9, 108, 1)

    p, q_support = values[1], values[2]
    kappa, lam, delta = values[3:]
    harmonic = F(kappa * lam, kappa + lam)
    bounds = (
        kappa * p,
        lam * q_support,
        delta * p * q_support,
        harmonic * (p + q_support),
    )
    assert bounds == (5625, 13068, 75625, F(80568, 13))
    assert all(mass <= bound for bound in bounds)
    return values


def pascal_prefix_nonmerge_audit() -> tuple[int, int, int]:
    q = sorted(rt.pascal_cell(4, 2, F(1, 97)))
    points = rt.strong_glue(q, q, F(1, 16384))

    # Exact rank-three record identified by the common double-circuit audit.
    a_side = (0, 1, 3)
    y = 2
    b_side = (6, 7, 8)
    z = 9
    seam = {0, y, z, 6}
    detached = set(a_side + b_side)
    assert is_convex([points[i] for i in detached])
    assert is_convex([points[i] for i in seam])
    assert not is_convex([points[i] for i in detached | seam])

    shield_count = 0
    merged_count = 0
    for mask in range(1 << len(a_side)):
        subset = {
            a_side[i] for i in range(len(a_side)) if mask >> i & 1
        }
        shield = set(b_side) | subset
        assert is_convex([points[i] for i in shield])
        shield_count += 1
        if is_convex([points[i] for i in shield | seam]):
            merged_count += 1

    two_sided_safe = 0
    for left_mask in range(1 << len(a_side)):
        left_subset = {
            a_side[i] for i in range(len(a_side)) if left_mask >> i & 1
        }
        for right_mask in range(1 << len(b_side)):
            right_subset = {
                b_side[i] for i in range(len(b_side)) if right_mask >> i & 1
            }
            if is_convex([points[i] for i in seam | left_subset | right_subset]):
                two_sided_safe += 1

    assert (shield_count, merged_count, two_sided_safe) == (8, 0, 8)
    return shield_count, merged_count, two_sided_safe


def parabolic_guard_audit() -> tuple[int, int, int, int]:
    m = 8
    height = 10**6
    cap_cloud = [(F(i), F(-i * i)) for i in range(1, m + 1)]
    cup_cloud = [(F(i), F(i * i)) for i in range(1, m + 1)]
    y = (F(-1), F(height))
    z = (F(-1), F(-height))
    a = cap_cloud[0]
    b = cup_cloud[0]
    assert is_chain(cap_cloud, -1)
    assert is_chain(cup_cloud, +1)
    assert all(rt.determinant(y, a, point) > 0 for point in cap_cloud[1:])
    assert all(rt.determinant(z, b, point) < 0 for point in cup_cloud[1:])

    left_safe = 0
    right_safe = 0
    actual_left = set()
    actual_right = set()
    for mask in range(1 << m):
        left = tuple(cap_cloud[i] for i in range(m) if mask >> i & 1)
        right = tuple(cup_cloud[i] for i in range(m) if mask >> i & 1)
        left_trace = tuple(sorted(set(left + (a, y))))
        right_trace = tuple(sorted(set(right + (z, b))))
        if is_chain(list(left_trace), -1):
            left_safe += 1
            actual_left.add(left_trace)
        if is_chain(list(right_trace), +1):
            right_safe += 1
            actual_right.add(right_trace)
    assert left_safe == right_safe == 2
    assert len(actual_left) == len(actual_right) == 1
    assert left_safe * right_safe == 4
    assert (1 << (2 * m)) > left_safe * right_safe
    return m, left_safe, right_safe, left_safe * right_safe


def half_scale_threshold_audit() -> tuple[int, int, int, F]:
    # Exact scalar consequences of the stretchable Q_{k,d} family. E is
    # chosen at a quasipolynomial scale only to verify the load comparison.
    n = 1 << 10
    rank = 20
    endpoint = 1 << 100
    child_faces = endpoint * endpoint
    parent_faces_upper = 3 * endpoint * endpoint
    nonaddable_lower = (n - 2 * rank) * endpoint
    record_lower = nonaddable_lower * nonaddable_lower
    endpoint_product = (n + 2) ** 2 * endpoint * endpoint

    theta_lower = F(record_lower, endpoint_product)
    density_lower = F(record_lower, parent_faces_upper)
    average_source_load = F(record_lower, endpoint * endpoint)
    seam_load_lower = F(record_lower, n**4)
    source_load_upper = n * n
    hall_lower = F(source_load_upper) * seam_load_lower / (
        F(source_load_upper) + seam_load_lower
    )
    routing_lower = F(record_lower, endpoint * endpoint + n**4)
    prefix_factor = 17
    three_routing_lower = F(
        prefix_factor * record_lower,
        2 * parent_faces_upper + n**4,
    )

    assert theta_lower == F((n - 2 * rank) ** 2, (n + 2) ** 2)
    assert density_lower == F((n - 2 * rank) ** 2, 3)
    assert average_source_load == (n - 2 * rank) ** 2
    assert average_source_load <= source_load_upper
    assert seam_load_lower > 1000 * source_load_upper
    assert hall_lower > F(999, 1000) * source_load_upper
    assert routing_lower > F(999, 1000) * average_source_load
    assert three_routing_lower > F(prefix_factor, 7) * average_source_load

    rhos = [
        F(k - 2, 1) / math.log2(math.comb(2 * k - 4, k - 2))
        for k in (4, 8, 16, 32, 64, 128, 256, 512)
    ]
    assert all(first > second > F(1, 2)
               for first, second in zip(rhos, rhos[1:]))
    return n, rank, (n - 2 * rank) ** 2, density_lower


def main() -> None:
    hall2 = hall_two_target_audit()
    hall3 = hall_three_target_audit()
    pascal = pascal_double_bad_audit()
    prefix = pascal_prefix_nonmerge_audit()
    guard = parabolic_guard_audit()
    half = half_scale_threshold_audit()
    print(
        "PASS: double-bad Hall threshold; "
        f"hall2={hall2.numerator}/{hall2.denominator} "
        f"hall3={hall3.numerator}/{hall3.denominator}; "
        f"Pascal={pascal}; prefix={prefix}; guard={guard}; "
        f"half=({half[0]}, {half[1]}, {half[2]}, "
        f"{half[3].numerator}/{half[3].denominator})"
    )


if __name__ == "__main__":
    main()
