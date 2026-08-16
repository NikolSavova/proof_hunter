#!/usr/bin/env python3
"""Exact audit for PAIRWISE_INCOMPATIBLE_COMPLETION_REGRESSION.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from random import Random


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def is_convex_set(points):
    return len(set(points)) == len(points) == len(convex_hull(points))


def local_chain(edge, length, delta, K):
    j = edge
    b = (F(j), F(j * j))
    c = (F(j + 1), F((j + 1) ** 2))
    midpoint = ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2)
    direction = (c[0] - b[0], c[1] - b[1])
    out = []
    for t in range(1, length + 1):
        ell = F(1, K + t)
        right = F(1, K + 2 * t)
        s = (ell - right) / (ell + right)
        h = F(2) / (ell + right)
        out.append((midpoint[0] + s * direction[0] / 2,
                    midpoint[1] + s * direction[1] / 2 - delta * h))
    return out


def build(q, L, D):
    m = 2 * q + 3
    scale = 10 ** 8 * (m + L + D) ** 4
    delta = F(1, scale)
    K = 10 * (m + L + D)
    base = [(F(j), F(j * j)) for j in range(m)]
    active = [local_chain(2 * j, L, delta, K) for j in range(q)]
    labels = local_chain(2 * q, D, delta, K + L + 7)
    completions = [tuple(active[j][word[j]] for j in range(q))
                   for word in product(range(L), repeat=q)]
    return base, active, labels, completions


def audit_geometry():
    configurations = 0
    completion_faces = 0
    bad_pairs = 0
    for q in range(1, 4):
        for L in range(2, 5):
            D = 4
            base, active, labels, completions = build(q, L, D)
            ambient = base + [x for chain in active for x in chain] + labels
            assert is_convex_set(base)
            assert all(cross(*triple) != 0
                       for triple in combinations(ambient, 3))
            assert all(is_convex_set(chain) for chain in active)

            for Q in completions:
                assert is_convex_set(base + list(Q))
                for y in labels:
                    assert is_convex_set(base + list(Q) + [y])
                    completion_faces += 1

            for Q, R in combinations(completions, 2):
                union = list(set(Q) | set(R))
                assert not is_convex_set(base + union)
                bad_pairs += 1

            # Every pair in a local chain is a bad trace with the edge
            # endpoints; traces form K_L independently in each pocket.
            witnesses = set()
            for j, chain in enumerate(active):
                b, c = base[2 * j], base[2 * j + 1]
                for x, y in combinations(chain, 2):
                    assert not is_convex_set([b, c, x, y])
                    witnesses.add(frozenset((x, y)))
            assert len(witnesses) == q * comb(L, 2)
            support = [x for chain in active for x in chain]
            tau = len(support)
            for mask in range(1 << len(support)):
                guard = {support[i] for i in range(len(support))
                         if mask >> i & 1}
                if all(guard & trace for trace in witnesses):
                    tau = min(tau, len(guard))
            assert tau == q * (L - 1)
            configurations += 1
    return configurations, completion_faces, bad_pairs


def greedy_independent_set(vertices, adjacency):
    remaining = set(vertices)
    chosen = []
    while remaining:
        v = min(remaining)
        chosen.append(v)
        remaining.discard(v)
        remaining.difference_update(adjacency[v])
    return chosen


def audit_graph_thinning():
    rng = Random(83820260814)
    trials = 500
    for _ in range(trials):
        n = rng.randint(2, 80)
        cap = rng.randint(0, min(10, n - 1))
        adjacency = {i: set() for i in range(n)}
        pairs = list(combinations(range(n), 2))
        rng.shuffle(pairs)
        for i, j in pairs:
            if len(adjacency[i]) < cap and len(adjacency[j]) < cap:
                if rng.randrange(3) == 0:
                    adjacency[i].add(j)
                    adjacency[j].add(i)
        T = max(map(len, adjacency.values()))
        independent = greedy_independent_set(range(n), adjacency)
        assert len(independent) * (T + 1) >= n
        assert all(j not in adjacency[i]
                   for i, j in combinations(independent, 2))
    return trials


def audit_rank_descent():
    cases = 0
    for n in range(2, 9):
        labels = tuple(range(n))
        for q in range(1, min(4, n) + 1):
            family = [frozenset(x) for x in combinations(labels, q)]
            Q0 = family[0]
            loads = {}
            for Q in family[1:]:
                x = min(Q - Q0)
                loads.setdefault(x, []).append(Q)
            if loads:
                x, child = max(loads.items(), key=lambda item: len(item[1]))
                assert len(child) * n >= len(family) - 1
                stripped = [Q - {x} for Q in child]
                assert len(set(stripped)) == len(child)
                assert all(len(Q) == q - 1 for Q in stripped)
            cases += 1
    return cases


def main():
    configs, faces, bad = audit_geometry()
    graphs = audit_graph_thinning()
    descents = audit_rank_descent()
    print("PASS: pairwise-incompatible completion regression")
    print(f"  exact rational configurations: {configs}")
    print(f"  verified completion extensions: {faces}")
    print(f"  verified incompatible pairs: {bad}")
    print(f"  bounded-degree graph thinnings: {graphs}")
    print(f"  witness-label descents: {descents}")


if __name__ == "__main__":
    main()
