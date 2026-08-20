#!/usr/bin/env python3
"""Exact finite certificates for the resonant two-arm charge barrier."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb


Point = tuple[int, int]


def add(x: Point, y: Point) -> Point:
    return (x[0] + y[0], x[1] + y[1])


def sub(x: Point, y: Point) -> Point:
    return (x[0] - y[0], x[1] - y[1])


def lam(x: Point) -> Point:
    # 3(I+J)(x,y)=3(x-y,x+y)
    return (3 * (x[0] - x[1]), 3 * (x[0] + x[1]))


def norm2(x: Point) -> int:
    return x[0] * x[0] + x[1] * x[1]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def first_prime_at_least(n: int) -> int:
    while not is_prime(n):
        n += 1
    return n


def dense_ruler(mark_count: int) -> list[int]:
    p = first_prime_at_least(mark_count)
    assert p < 2 * mark_count
    marks = [2 * p * j + (j * j % p) for j in range(mark_count)]
    differences: dict[int, tuple[int, int]] = {}
    for i, j in combinations(range(mark_count), 2):
        d = marks[j] - marks[i]
        assert d not in differences
        differences[d] = (i, j)
    return marks


def distance_sidon(points: list[Point]) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for i, j in combinations(range(len(points)), 2):
        d2 = norm2(sub(points[i], points[j]))
        if d2 in seen:
            return False
        seen[d2] = (i, j)
    return True


def choose_translation(rx: list[int], ry: list[int]) -> Point:
    # The proof guarantees that only finitely many Z are bad.  These finite
    # certificates simply scan the polynomial curve T=(Z,Z^2).
    start = max(rx + ry) + 1
    for z in range(start, start + 2_000_000):
        t = (z, z * z)
        points = [(r, 0) for r in rx] + [(t[0] - r, t[1] - r) for r in ry]
        if distance_sidon(points):
            return t
    raise AssertionError("translation search exhausted")


def pair_data(points: list[Point]):
    pair_by_sum: dict[Point, tuple[int, int]] = {}
    edge_by_sum: dict[Point, Point] = {}
    for i, j in combinations(range(len(points)), 2):
        s = add(points[i], points[j])
        assert s not in pair_by_sum
        pair_by_sum[s] = (i, j)
        a, b = sorted((points[i], points[j]))
        edge_by_sum[s] = sub(a, b)
    return pair_by_sum, edge_by_sum


def clean_fibres(points: list[Point]):
    pair_by_sum, edge_by_sum = pair_data(points)
    fibres: dict[Point, list[Point]] = defaultdict(list)
    for a in range(len(points)):
        for b in range(len(points)):
            if a == b:
                continue
            q = sub(points[a], points[b])
            for s, (c, d) in pair_by_sum.items():
                target = add(s, q)
                if target not in pair_by_sum:
                    continue
                e, f = pair_by_sum[target]
                if len({a, b, c, d, e, f}) == 6:
                    fibres[q].append(s)
    return fibres, pair_by_sum, edge_by_sum


def certificate(s: int) -> dict[str, int]:
    marks = dense_ruler(2 * s)
    rx, ry = marks[:s], marks[s:]
    tvec = choose_translation(rx, ry)
    xpoints = [(r, 0) for r in rx]
    ypoints = [(tvec[0] - r, tvec[1] - r) for r in ry]
    points = xpoints + ypoints
    assert distance_sidon(points)

    # The scalar triple-sum argument behind the asymptotic h >> s^2 bound.
    triple_bins: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for triple in combinations(ry, 3):
        triple_bins[sum(triple)].append(triple)
    triple_collisions = sum(comb(len(bucket), 2) for bucket in triple_bins.values())
    for bucket in triple_bins.values():
        for c, e in combinations(bucket, 2):
            assert set(c).isdisjoint(e), (c, e)

    fibres, pair_by_sum, edge_by_sum = clean_fibres(points)
    y_indices = set(range(s, 2 * s))

    # Retain, for each q, precisely the certified clean starts whose source
    # and target pairs both lie on the Y arm.
    internal_y: dict[Point, list[Point]] = defaultdict(list)
    for q, starts in fibres.items():
        for start in starts:
            target = add(start, q)
            if set(pair_by_sum[start]) <= y_indices and set(pair_by_sum[target]) <= y_indices:
                internal_y[q].append(start)

    # Each unordered collision of disjoint equal-sum triples has two source
    # orders and 3*3 choices of the distinguished q endpoints.
    assert sum(map(len, internal_y.values())) == 18 * triple_collisions

    q = max(internal_y, key=lambda z: len(internal_y[z]))
    hy = internal_y[q]
    h = len(fibres[q])
    assert len(hy) > 0

    x_sums = [
        psum
        for psum, ij in pair_by_sum.items()
        if set(ij) <= set(range(s))
    ]
    restricted = Counter(
        add(edge_by_sum[start], lam(edge_by_sum[psum]))
        for start in hy
        for psum in x_sums
    )
    restricted_records = len(hy) * comb(s, 2)
    assert sum(restricted.values()) == restricted_records
    restricted_energy = sum(v * v for v in restricted.values())

    # Exact sign/orientation audit.  With u = lex-smaller minus lex-larger,
    # a Y edge is a*d and an X edge is -b*e, hence Gamma=(a+3b)*d.
    dvec = (-1, -1)
    for start in hy:
        uy = edge_by_sum[start]
        assert uy[0] == uy[1] < 0
        a_gap = -uy[0]
        assert uy == (-a_gap, -a_gap)
        for psum in x_sums:
            ux = edge_by_sum[psum]
            assert ux[1] == 0 and ux[0] < 0
            b_gap = -ux[0]
            expected = ((a_gap + 3 * b_gap) * dvec[0],
                        (a_gap + 3 * b_gap) * dvec[1])
            assert add(uy, lam(ux)) == expected

    all_sums = list(pair_by_sum)
    full = Counter(
        add(edge_by_sum[start], lam(edge_by_sum[psum]))
        for start in fibres[q]
        for psum in all_sums
    )
    full_energy = sum(v * v for v in full.values())
    n = comb(2 * s, 2)

    # Every restricted key is collinear with (1,1).
    assert all(z[0] == z[1] for z in restricted)
    assert len(restricted) <= 4 * (max(marks) - min(marks)) + 1
    assert full_energy >= restricted_energy

    return {
        "s": s,
        "k": 2 * s,
        "height": max(max(abs(x), abs(y)) for x, y in points),
        "q_x": q[0],
        "q_y": q[1],
        "h_full": h,
        "h_internal_y": len(hy),
        "triple_collisions": triple_collisions,
        "N": n,
        "restricted_records": restricted_records,
        "restricted_image": len(restricted),
        "restricted_energy": restricted_energy,
        "full_energy": full_energy,
        "target_N_h_plus_k": n * (h + 2 * s),
        "max_load": max(full.values()),
    }


def main() -> None:
    # s=8 is the first member of this deterministic split with a triple-sum
    # collision.  The larger rows display the growing fibre and energy;
    # s=50 already beats the raw N(h+k) target before exponent comparison.
    rows = [certificate(s) for s in (8, 16, 32, 50)]
    for row in rows:
        print(row)
    assert all(row["full_energy"] >= row["restricted_energy"] for row in rows)
    assert rows[-1]["full_energy"] > rows[-1]["target_N_h_plus_k"]
    print("two-arm Gaussian edge-vector barrier: PASS")


if __name__ == "__main__":
    main()
