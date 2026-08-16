#!/usr/bin/env python3
"""Exact checks for COHERENT_RAMP_ENDPOINT_MODULE_LOCALIZATION.md."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def general_position(points):
    return len({x for x, _ in points}) == len(points) and all(
        orient(points[i], points[j], points[k]) != 0
        for i, j, k in combinations(range(len(points)), 3)
    )


def is_cap(points, trace):
    """An x-monotone upper chain; pairs and singletons are allowed."""
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(orient(word[i], word[i + 1], word[i + 2]) < 0
               for i in range(len(word) - 2))


def is_cup(points, trace):
    """An x-monotone lower chain; pairs and singletons are allowed."""
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(orient(word[i], word[i + 1], word[i + 2]) > 0
               for i in range(len(word) - 2))


def hull(points, trace):
    word = sorted((points[i], i) for i in trace)
    if len(word) <= 1:
        return [i for _, i in word]

    lower = []
    for p, idx in word:
        while len(lower) >= 2 and orient(
            lower[-2][0], lower[-1][0], p
        ) <= 0:
            lower.pop()
        lower.append((p, idx))

    upper = []
    for p, idx in reversed(word):
        while len(upper) >= 2 and orient(
            upper[-2][0], upper[-1][0], p
        ) <= 0:
            upper.pop()
        upper.append((p, idx))
    return [idx for _, idx in lower[:-1] + upper[:-1]]


def is_face(points, trace):
    return len(hull(points, trace)) == len(trace)


def endpoint_factorization(points):
    assert general_position(points)
    n = len(points)
    caps = defaultdict(list)
    cups = defaultdict(list)
    faces = []

    for mask in range(1, 1 << n):
        trace = tuple(i for i in range(n) if mask >> i & 1)
        if is_face(points, trace):
            faces.append(frozenset(trace))
        if len(trace) >= 2:
            ordered = sorted(trace, key=lambda i: points[i][0])
            endpoint = (ordered[0], ordered[-1])
            if is_cap(points, trace):
                caps[endpoint].append(frozenset(trace))
            if is_cup(points, trace):
                cups[endpoint].append(frozenset(trace))

    Cbar = sum(map(len, caps.values()))
    Ubar = sum(map(len, cups.values()))
    Hbar = len(faces) - n
    assert Hbar == sum(len(caps[e]) * len(cups[e]) for e in caps)

    # The same-endpoint cap/cup map is a bijection onto all rank >= 2 faces.
    unions = []
    for e in caps:
        for cap in caps[e]:
            for cup in cups[e]:
                union = cap | cup
                assert is_face(points, union)
                unions.append(union)
    assert len(unions) == len(set(unions)) == Hbar
    assert set(unions) == {face for face in faces if len(face) >= 2}

    # Exact collision identity and the D^2 endpoint localization.
    overlap = F(Hbar, Cbar * Ubar)
    endpoint_count = len(caps)
    best_e = max(caps, key=lambda e: F(len(caps[e]) * len(cups[e]),
                                      Cbar * Ubar))
    p = F(len(caps[best_e]), Cbar)
    q = F(len(cups[best_e]), Ubar)
    assert p * q >= overlap / endpoint_count
    assert endpoint_count <= n * (n - 1) // 2 < n**2
    assert p >= p * q and q >= p * q
    return n, len(faces), Cbar, Ubar, Hbar, best_e


def check_prefix_surplus_lemma():
    # Exact exhaustive audit of the purely algebraic telescope.
    h = F(3)
    T = F(3, 2)
    P = h + T - 1
    avals = [F(1), F(3, 2), F(2), F(5, 2), F(3), F(7, 2), F(4)]
    svals = [F(0), F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(3)]
    checked = 0
    for q in range(2, 5):
        for As in product(avals, repeat=q):
            if any(not (F(1) <= A < P) for A in As):
                continue
            ys = [As[i] - i for i in range(q)]
            for ss in product(svals, repeat=q - 1):
                surpluses = [F(0), *ss]
                unpaid = all(
                    surpluses[j] + ys[i] - ys[j] < T
                    for j in range(1, q)
                    for i in range(j)
                )
                if not unpaid:
                    continue
                checked += 1
                positive = sum(
                    max(F(0), surpluses[j] - T)
                    for j in range(1, q)
                )
                assert positive < P - 1
                high = sum(surpluses[j] >= 2 * T for j in range(1, q))
                assert high * T <= positive
    assert checked > 100
    return checked


if __name__ == "__main__":
    point_sets = [
        [(0, 0), (1, 5), (2, -3), (3, 8), (4, 1), (5, -7), (6, 6)],
        [(0, 3), (1, -4), (2, 9), (3, 1), (4, -8), (5, 7), (6, -2)],
        [(0, -5), (1, 4), (2, 11), (3, -3), (4, 8), (5, -9), (6, 2)],
    ]
    summaries = [endpoint_factorization(points) for points in point_sets]
    checked = check_prefix_surplus_lemma()
    print(
        "PASS: exact endpoint cap/cup bijections, D^2 localization, and "
        f"prefix-surplus telescope; arrays={checked}, summaries={summaries}"
    )
