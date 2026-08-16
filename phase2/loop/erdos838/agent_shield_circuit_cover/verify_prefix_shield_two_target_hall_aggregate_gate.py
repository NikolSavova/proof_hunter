#!/usr/bin/env python3
"""Exact checks for PREFIX_SHIELD_TWO_TARGET_HALL_AGGREGATE_GATE."""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product
from math import log2


def small_hall_audit() -> tuple[int, int, F, int, int, int]:
    # Original records are K_{2,2}; one prefix bit doubles each record.
    expanded = []
    for source in range(2):
        for context in range(2):
            for mask in range(2):
                expanded.append((source, (context, mask), F(1)))
    edge_count = len(expanded)
    targets = {("A", a) for a, _, _ in expanded}
    targets |= {("F", f) for _, f, _ in expanded}
    vertex_count = len(targets)
    best = F(0)
    for mask in range(1, 1 << edge_count):
        mass = F(0)
        union = set()
        for i, (a, f, w) in enumerate(expanded):
            if mask >> i & 1:
                mass += w
                union.add(("A", a))
                union.add(("F", f))
        best = max(best, mass / len(union))
    assert best == F(4, 3)

    source_expanded = max(sum(w for a, _, w in expanded if a == aa)
                          for aa in range(2))
    shield_load = max(sum(w for _, f, w in expanded if f == ff)
                      for ff in {f for _, f, _ in expanded})
    pair_load = max(sum(w for a, f, w in expanded if (a, f) == pair)
                    for pair in {(a, f) for a, f, _ in expanded})
    assert source_expanded == 4
    assert shield_load == 2
    assert pair_load == 1
    assert edge_count <= best * vertex_count
    assert edge_count <= shield_load * vertex_count
    assert edge_count <= pair_load * vertex_count * vertex_count
    # Unexpanded source load is two and gives W=4 <= 2*V.
    assert 4 <= 2 * vertex_count
    return (edge_count, vertex_count, best, int(source_expanded),
            int(shield_load), int(pair_load))


def role_words(sizes: list[int]) -> tuple[tuple[int, ...], ...]:
    return tuple(product(*(range(size) for size in sizes)))


def aggregate_depth_audit() -> tuple[int, int, int]:
    sizes = [2, 2, 3]
    words = role_words(sizes)
    contexts = range(2)
    node = words
    prefix: tuple[tuple[int, int], ...] = ()
    expanded = []
    total_mass = 0
    for depth, size in enumerate(sizes):
        for word in node:
            for context in contexts:
                for subset_mask in range(1 << len(prefix)):
                    subset = frozenset(prefix[i] for i in range(len(prefix))
                                       if subset_mask >> i & 1)
                    expanded.append((word, (context, subset), depth))
                    total_mass += 1
        # Maximum child is symbol zero; all children are equal here.
        node = tuple(word for word in node if word[depth] == 0)
        prefix += ((depth, 0),)

    root_mass = len(words) * len(tuple(contexts))
    assert root_mass == 24
    assert total_mass == 72
    loads: dict[tuple[tuple[int, ...], tuple[int, frozenset]], int] = {}
    for cap, shield, _ in expanded:
        loads[(cap, shield)] = loads.get((cap, shield), 0) + 1
    max_pair = max(loads.values())
    assert max_pair == len(sizes) == 3
    # The pair recovers cap, context, and S. Only depth is erased.
    for (cap, (context, subset)), load in loads.items():
        assert context in contexts
        assert subset.issubset({(i, cap[i]) for i in range(len(sizes))})
        assert load <= len(sizes)
    return root_mass, total_mass, max_pair


def product_role_regression() -> tuple[int, int, int, F, F]:
    a, b, d = 6, 3, 16
    sizes = [2] * a + [d] * b
    total = 1
    for size in sizes:
        total *= size
    node = total
    aggregate = F(0)
    max_branch = F(0)
    for depth, size in enumerate(sizes):
        alpha = F(node, total)
        aggregate += (1 << depth) * alpha
        max_branch = max(max_branch, alpha * size)
        assert node % size == 0
        node //= size
    assert aggregate == F(457, 64)
    assert max_branch == 2

    # Exact half-scale rank/support/entropy checks.
    for ell in range(8, 19):
        n = 1 << ell
        aa, bb = ell, ell // 2
        dd = (n - 2 * aa - 2) // bb
        assert dd >= 3
        support = 2 * aa + bb * dd + 2
        rank = aa + bb + 2
        assert support <= n
        assert rank <= 2 * ell
        log_h = aa + bb * log2(dd)
        assert log_h >= 0.35 * ell * ell
        assert log_h <= 0.5 * ell * ell + 2 * ell
    return a, b, d, aggregate, max_branch


Point = tuple[F, F]


def det(a: Point, b: Point, c: Point) -> F:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def is_cap(points: list[Point]) -> bool:
    ordered = sorted(points)
    return (len(ordered) <= 2 or
            all(det(ordered[i], ordered[j], ordered[k]) < 0
                for i, j, k in combinations(range(len(ordered)), 3)))


def rational_role_geometry() -> tuple[int, int, int, int]:
    a, b, d = 3, 2, 5
    sizes = [2] * a + [d] * b
    cursor = 1
    roles: list[list[Point]] = []
    for size in sizes:
        role = []
        for _ in range(size):
            x = F(cursor)
            role.append((x, -x * x))
            cursor += 1
        roles.append(role)
    u = (F(0), F(0))
    x = F(cursor)
    v = (x, -x * x)
    count = 0
    for choice in product(*roles):
        face = [u, *choice, v]
        assert is_cap(face)
        count += 1
    assert count == (2 ** a) * (d ** b) == 200
    # Every selected prefix and every subset of it is a cap face.
    chosen = [role[0] for role in roles]
    for depth in range(len(chosen) + 1):
        prefix = chosen[:depth]
        for mask in range(1 << depth):
            subset = [prefix[i] for i in range(depth) if mask >> i & 1]
            assert is_cap([u, *subset, v])
    return a, b, d, count


def main() -> None:
    hall = small_hall_audit()
    depth = aggregate_depth_audit()
    role = product_role_regression()
    geometry = rational_role_geometry()
    print(
        "PASS: prefix-shield Hall aggregate; "
        f"hall=({hall[0]}, {hall[1]}, {hall[2].numerator}/"
        f"{hall[2].denominator}, {hall[3]}, {hall[4]}, {hall[5]}), "
        f"depth={depth}, role=({role[0]}, {role[1]}, {role[2]}, "
        f"{role[3].numerator}/{role[3].denominator}, {int(role[4])}), "
        f"geometry={geometry}"
    )


if __name__ == "__main__":
    main()
