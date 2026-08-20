#!/usr/bin/env python3
"""Finite certificate for FINITE_GROUP_ENDPOINT_PROJECTION_CRITICAL_BARRIER.

This is deliberately exact (integer arithmetic only).  It searches a fixed
seeded balanced lift of the full F_3^2 plane and verifies the metric and
finite-field assertions used in the note.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
import random


Q = 3
COPIES = 4
M = 4000
SEED = 12080317


def norm2(v: tuple[int, int]) -> int:
    return v[0] * v[0] + v[1] * v[1]


def is_distance_sidon(points: list[tuple[int, int]]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for i, j in combinations(range(len(points)), 2):
        d = norm2((points[i][0] - points[j][0], points[i][1] - points[j][1]))
        if d in seen:
            return False
        seen[d] = (i, j)
    return True


def random_balanced_lift() -> list[tuple[int, int]]:
    rng = random.Random(SEED)
    residues = list(product(range(Q), repeat=2))
    # At this scale a random balanced lift succeeds almost immediately.  The
    # bounded loop makes a regression failure explicit rather than hanging.
    for _ in range(500):
        points: list[tuple[int, int]] = []
        used: set[tuple[int, int]] = set()
        for rho in residues:
            for _copy in range(COPIES):
                while True:
                    x = rho[0] + Q * rng.randrange((M - rho[0]) // Q + 1)
                    y = rho[1] + Q * rng.randrange((M - rho[1]) // Q + 1)
                    p = (x, y)
                    if p not in used:
                        used.add(p)
                        points.append(p)
                        break
        if is_distance_sidon(points):
            return points
    raise AssertionError("seeded balanced-lift search did not succeed")


def rank_mod(matrix: list[list[int]], prime: int) -> int:
    a = [[x % prime for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, prime)
        a[rank] = [(inv * x) % prime for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor * y) % prime
                        for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def verify() -> None:
    points = random_balanced_lift()
    k = len(points)
    assert k == Q * Q * COPIES
    assert len(set(points)) == k
    assert all(0 <= x <= M and 0 <= y <= M for x, y in points)

    residue_counts = Counter((x % Q, y % Q) for x, y in points)
    assert len(residue_counts) == Q * Q
    assert set(residue_counts.values()) == {COPIES}

    # Euclidean distance-Sidonicity and its two exact consequences.
    distance_owner: dict[int, tuple[int, int]] = {}
    vector_owner: dict[tuple[int, int], tuple[int, int]] = {}
    radial_count: Counter[int] = Counter()
    for i, j in combinations(range(k), 2):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        d = dx * dx + dy * dy
        assert d not in distance_owner
        distance_owner[d] = (i, j)
        radial_count[d] += 2
        for u, v, a, b in ((dx, dy, i, j), (-dx, -dy, j, i)):
            assert (u, v) not in vector_owner
            vector_owner[(u, v)] = (a, b)
    assert len(distance_owner) == k * (k - 1) // 2
    assert len(vector_owner) == k * (k - 1)
    assert set(radial_count.values()) == {2}

    # Anisotropy of x^2+y^2 over F_3.
    zero_norm = [v for v in product(range(Q), repeat=2)
                 if (v[0] * v[0] + v[1] * v[1]) % Q == 0]
    assert zero_norm == [(0, 0)]

    # A balanced full-plane multiset has exact full association-scheme
    # difference statistics.  Nonzero residue differences occur q^2*s^2
    # times; zero occurs q^2*s*(s-1) when equal labels are excluded.
    residue_diff_count: Counter[tuple[int, int]] = Counter()
    residue_norm_count: Counter[int] = Counter()
    for i, j in permutations(range(k), 2):
        h = ((points[i][0] - points[j][0]) % Q,
             (points[i][1] - points[j][1]) % Q)
        residue_diff_count[h] += 1
        residue_norm_count[(h[0] * h[0] + h[1] * h[1]) % Q] += 1

    for h in product(range(Q), repeat=2):
        expected = Q * Q * COPIES * (COPIES - 1) if h == (0, 0) \
            else Q * Q * COPIES * COPIES
        assert residue_diff_count[h] == expected

    circle_sizes = Counter((x * x + y * y) % Q
                           for x, y in product(range(Q), repeat=2))
    assert circle_sizes[0] == 1
    assert all(circle_sizes[r] == Q + 1 for r in range(1, Q))
    for r in range(1, Q):
        assert residue_norm_count[r] == (Q + 1) * Q * Q * COPIES * COPIES

    distance_matrix = [
        [((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) % Q for b in points]
        for a in points
    ]
    finite_rank = rank_mod(distance_matrix, Q)
    assert finite_rank <= 4

    # Exact endpoint cocycle after reduction, checked for every ordered
    # triple of actual endpoints.
    for a, b, c in product(points, repeat=3):
        ab = ((a[0] - b[0]) % Q, (a[1] - b[1]) % Q)
        bc = ((b[0] - c[0]) % Q, (b[1] - c[1]) % Q)
        ac = ((a[0] - c[0]) % Q, (a[1] - c[1]) % Q)
        assert ((ab[0] + bc[0]) % Q, (ab[1] + bc[1]) % Q) == ac

    print("PASS finite-group endpoint projection critical barrier")
    print(f"q={Q} copies={COPIES} k={k} m={M}")
    print(f"distance labels={len(distance_owner)} directed vectors={len(vector_owner)}")
    print(f"residue multiplicities={sorted(set(residue_counts.values()))}")
    print(f"nonzero circle sizes={[circle_sizes[r] for r in range(1, Q)]}")
    print(f"squared-distance matrix rank over F_{Q}={finite_rank}")


if __name__ == "__main__":
    verify()
