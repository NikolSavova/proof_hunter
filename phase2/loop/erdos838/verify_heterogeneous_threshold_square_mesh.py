#!/usr/bin/env python3
"""Regression checks for the heterogeneous threshold square-mesh theorem."""

from __future__ import annotations

import random
from itertools import combinations, permutations, product
from math import fsum, log2, sqrt


def endpoint_ranks(vertices, roots):
    """Unweighted cap/cup edge ranks on an induced ordered macro chart."""
    vertices = tuple(sorted(vertices))
    active = set(vertices)
    cap = {value: 0 for value in vertices}
    cup = {value: 0 for value in vertices}
    for left, right in roots:
        if left not in active or right not in active:
            continue
        old_cap_left = cap[left]
        old_cup_right = cup[right]
        cap[left] = max(old_cap_left, cap[right] + 1)
        cup[right] = max(old_cup_right, cup[left] + 1)
    return cap, cup


def weighted_rewards(n, roots, sizes):
    weights = [log2(1 + value) for value in sizes]
    cap = [0.0] * n
    cup = [0.0] * n
    for left, right in roots:
        cap[left] = max(cap[left], cap[right] + weights[right])
        cup[right] = max(cup[right], cup[left] + weights[left])
    return tuple(cap[index] + cup[index] for index in range(n))


def harmonic(m):
    return fsum(1.0 / value for value in range(1, m + 1))


def check_instance(roots, sizes):
    m = len(sizes)
    rewards = weighted_rewards(m, roots, sizes)
    ell = tuple(log2(value) for value in sizes)
    bank = max(0.5 * ell[index] ** 2 + rewards[index]
               for index in range(m))

    order = tuple(sorted(range(m), key=lambda index: (-sizes[index], index)))
    threshold_checks = 0
    for j in range(1, m + 1):
        vertices = order[:j]
        cap, cup = endpoint_ranks(vertices, roots)
        hinge = max(vertices, key=lambda index: cap[index] + cup[index])
        assert cap[hinge] + cup[hinge] + 1e-12 >= log2(j)
        floor = 0.5 * ell[order[j - 1]] ** 2 + ell[order[j - 1]] * log2(j)
        actual = 0.5 * ell[hinge] ** 2 + rewards[hinge]
        assert actual + 1e-9 >= floor
        assert bank + 1e-9 >= floor
        threshold_checks += 1

    total_log = log2(sum(sizes))
    q = log2(m)
    hlog = log2(harmonic(m))
    target = 0.5 * (total_log - hlog) ** 2 - 0.5 * q ** 2
    assert bank + 1e-8 >= target

    transition = sqrt(2 * bank + q ** 2)
    assert sum(sizes) <= (2 ** transition) * harmonic(m) * (1 + 1e-10)
    return threshold_checks, bank - target


def all_n4_orders():
    edges = tuple(combinations(range(4), 2))
    menus = tuple(product((1, 2, 7, 64, 4096), repeat=4))
    instances = checks = 0
    minimum_margin = float("inf")
    for roots in permutations(edges):
        for sizes in menus:
            used, margin = check_instance(roots, sizes)
            checks += used
            instances += 1
            minimum_margin = min(minimum_margin, margin)
    return instances, checks, minimum_margin


def reflection_roots(points):
    return tuple(sorted(
        combinations(range(len(points)), 2),
        key=lambda edge: (
            (points[edge[1]][1] - points[edge[0]][1])
            / (points[edge[1]][0] - points[edge[0]][0])
        ),
    ))


def stretchable_checks():
    rows = (
        (
            ((0, -3), (1, -9003), (2, -8003), (3, -9003), (4, -2)),
            (4250, 1000, 1000, 1000, 1000),
        ),
        (
            ((0, 0), (1, -1), (2, -3), (3, 0)),
            (1024, 3, 17, 511),
        ),
        (
            tuple((index, index * index + (index % 3)) for index in range(8)),
            (1, 2, 4, 8, 16, 32, 64, 128),
        ),
    )
    checks = 0
    for points, sizes in rows:
        roots = reflection_roots(points)
        assert len(roots) == len(points) * (len(points) - 1) // 2
        used, _ = check_instance(roots, sizes)
        checks += used
    return len(rows), checks


def random_arithmetic(seed=838, rounds=50000):
    random.seed(seed)
    minimum_margin = float("inf")
    for _ in range(rounds):
        m = random.randint(1, 80)
        sizes = sorted(
            (random.randint(1, 1 << random.randint(0, 30)) for _ in range(m)),
            reverse=True,
        )
        ell = [log2(value) for value in sizes]
        floor = max(
            0.5 * ell[index] ** 2 + ell[index] * log2(index + 1)
            for index in range(m)
        )
        total_log = log2(sum(sizes))
        target = (
            0.5 * (total_log - log2(harmonic(m))) ** 2
            - 0.5 * log2(m) ** 2
        )
        assert floor + 1e-8 >= target
        minimum_margin = min(minimum_margin, floor - target)
    return rounds, minimum_margin


def uniform_boundary():
    # The threshold floor itself reaches the exact square target for equal
    # sizes at j=m; the theorem loses only when the harmonic envelope is used.
    rows = 0
    for m in range(1, 257):
        for exponent in (0, 1, 7, 31):
            ell = float(exponent)
            threshold = 0.5 * ell ** 2 + ell * log2(m)
            exact_square = 0.5 * (ell + log2(m)) ** 2 - 0.5 * log2(m) ** 2
            assert abs(threshold - exact_square) < 1e-10
            rows += 1
    return rows


def main():
    instances, threshold_checks, minimum_margin = all_n4_orders()
    stretchable_rows, stretchable_thresholds = stretchable_checks()
    arithmetic_rows, arithmetic_margin = random_arithmetic()
    boundary_rows = uniform_boundary()
    print(
        "PASS: heterogeneous threshold square mesh; "
        f"n4_instances={instances}; threshold_checks={threshold_checks}; "
        f"minimum_n4_margin={minimum_margin:.12g}; "
        f"stretchable=({stretchable_rows},{stretchable_thresholds}); "
        f"arithmetic=({arithmetic_rows},{arithmetic_margin:.12g}); "
        f"uniform_boundary={boundary_rows}"
    )


if __name__ == "__main__":
    main()
