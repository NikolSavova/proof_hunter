#!/usr/bin/env python3
"""Exact stresses for the surviving positive metric-scalar charge.

The first audit counts the collisions which survive every integral linear
change of coordinates on finite-field parabola lifts.  The second tests
two-, three-, and four-ruler-arm distance-Sidon families, including arm
scales which grow with the family size.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb, gcd


Point = tuple[int, int]
C = 18


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


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
    marks = [2 * p * j + (j * j % p) for j in range(mark_count)]
    gaps: set[int] = set()
    for i, j in combinations(range(mark_count), 2):
        gap = marks[j] - marks[i]
        assert gap not in gaps
        gaps.add(gap)
    return marks


def finite_field_parabola(p: int) -> list[Point]:
    assert is_prime(p)
    return [(x, x * x % p) for x in range(p)]


def distance_sidon(points: list[Point]) -> bool:
    labels: set[int] = set()
    for i, j in combinations(range(len(points)), 2):
        label = norm2(sub(points[i], points[j]))
        if label in labels:
            return False
        labels.add(label)
    return True


def pair_data(points: list[Point]):
    pair_by_sum: dict[Point, tuple[int, int]] = {}
    edge_by_sum: dict[Point, Point] = {}
    for i, j in combinations(range(len(points)), 2):
        total = add(points[i], points[j])
        assert total not in pair_by_sum
        pair_by_sum[total] = (i, j)
        edge_by_sum[total] = sub(points[i], points[j])
    return pair_by_sum, edge_by_sum


def clean_fibres(points: list[Point]):
    pair_by_sum, edge_by_sum = pair_data(points)
    fibres: dict[Point, list[Point]] = defaultdict(list)
    for a in range(len(points)):
        for b in range(len(points)):
            if a == b:
                continue
            q = sub(points[a], points[b])
            for start, (c, d) in pair_by_sum.items():
                target = add(start, q)
                if target not in pair_by_sum:
                    continue
                e, f = pair_by_sum[target]
                if len({a, b, c, d, e, f}) == 6:
                    fibres[q].append(start)
    return fibres, pair_by_sum, edge_by_sum


def matrix_key(u: Point, v: Point) -> tuple[int, int, int]:
    """Upper triangle of uu^T+C vv^T."""
    return (
        u[0] * u[0] + C * v[0] * v[0],
        u[0] * u[1] + C * v[0] * v[1],
        u[1] * u[1] + C * v[1] * v[1],
    )


def primitive_direction(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    divisor = gcd(abs(vector[0]), gcd(abs(vector[1]), abs(vector[2])))
    assert divisor > 0
    answer = tuple(value // divisor for value in vector)
    for value in answer:
        if value:
            return tuple(-entry for entry in answer) if value < 0 else answer
    raise AssertionError("zero direction")


def safe_matrix_difference_profile(p: int) -> tuple[int, int, int, int]:
    """Remove directions which would already force an edge-norm collision."""
    points = finite_field_parabola(p)
    fibres, pair_by_sum, edge_by_sum = clean_fibres(points)
    q = max(fibres, key=lambda z: len(fibres[z]))
    starts = fibres[q]
    outer_keys = [
        (u[0] * u[0], 2 * u[0] * u[1], u[1] * u[1])
        for u in edge_by_sum.values()
    ]
    forbidden = {
        primitive_direction(tuple(left[i] - right[i] for i in range(3)))
        for left, right in combinations(outer_keys, 2)
    }
    record_keys = list({
        (key[0], 2 * key[1], key[2])
        for start in starts
        for total in pair_by_sum
        for key in [matrix_key(edge_by_sum[start], edge_by_sum[total])]
    })
    safe_counts: Counter[tuple[int, int, int]] = Counter()
    for left, right in combinations(record_keys, 2):
        direction = primitive_direction(
            tuple(left[i] - right[i] for i in range(3))
        )
        if direction not in forbidden:
            safe_counts[direction] += 1
    return len(outer_keys), len(forbidden), len(safe_counts), max(safe_counts.values())


def lex_transform(p: int, point: Point) -> Point:
    # Every matrix-key coordinate has absolute value at most
    # Q=(C+1)(p-1)^2.  The Gram matrix of this L is
    # [[1,B],[B,10B^2]], which lexicographically separates distinct keys.
    qbound = (C + 1) * (p - 1) ** 2
    base = 2 * qbound + 1
    return point[0] + base * point[1], 3 * base * point[1]


def parabola_matrix_profile(p: int) -> dict[str, int | float]:
    points = finite_field_parabola(p)
    fibres, pair_by_sum, edge_by_sum = clean_fibres(points)
    q = max(fibres, key=lambda z: len(fibres[z]))
    starts = fibres[q]
    sums = list(pair_by_sum)

    matrix_loads = Counter(
        matrix_key(edge_by_sum[start], edge_by_sum[total])
        for start in starts
        for total in sums
    )
    matrix_energy = sum(load * load for load in matrix_loads.values())

    transformed = [lex_transform(p, point) for point in points]
    assert distance_sidon(transformed)
    transformed_fibres, transformed_pairs, transformed_edges = clean_fibres(transformed)
    tq = sub(lex_transform(p, q), lex_transform(p, (0, 0)))
    # L is linear, so the chosen clean fibre is transported exactly.
    assert len(transformed_fibres[tq]) == len(starts)
    scalar_loads = Counter(
        norm2(transformed_edges[start]) + C * norm2(transformed_edges[total])
        for start in transformed_fibres[tq]
        for total in transformed_pairs
    )
    scalar_energy = sum(load * load for load in scalar_loads.values())
    assert scalar_energy == matrix_energy
    assert sorted(scalar_loads.values()) == sorted(matrix_loads.values())

    records = len(starts) * len(sums)
    return {
        "p": p,
        "h": len(starts),
        "N": len(sums),
        "records": records,
        "matrix_image": len(matrix_loads),
        "matrix_energy": matrix_energy,
        "max_matrix_load": max(matrix_loads.values()),
        "energy_over_records": matrix_energy / records,
    }


def best_internal_fibre(
    points: list[Point], arm_size: int, arm_count: int
) -> tuple[Point, tuple[int, int], list[Point], list[Point], dict[Point, tuple[int, int]], dict[Point, Point]]:
    pair_by_sum, edge_by_sum = pair_data(points)
    best: tuple[int, Point, tuple[int, int], list[Point]] | None = None
    for arm in range(arm_count):
        indices = set(range(arm * arm_size, (arm + 1) * arm_size))
        internal = {
            total: pair
            for total, pair in pair_by_sum.items()
            if pair[0] in indices and pair[1] in indices
        }
        for a in indices:
            for b in indices:
                if a == b:
                    continue
                q = sub(points[a], points[b])
                starts: list[Point] = []
                for start, (c, d) in internal.items():
                    target = add(start, q)
                    if target not in internal:
                        continue
                    e, f = internal[target]
                    if len({a, b, c, d, e, f}) == 6:
                        starts.append(start)
                candidate = (len(starts), q, (a, b), starts)
                if best is None or candidate[0] > best[0]:
                    best = candidate
    assert best is not None and best[0] > 0
    _, q, endpoints, internal_starts = best

    full_starts: list[Point] = []
    a, b = endpoints
    for start, (c, d) in pair_by_sum.items():
        target = add(start, q)
        if target not in pair_by_sum:
            continue
        e, f = pair_by_sum[target]
        if len({a, b, c, d, e, f}) == 6:
            full_starts.append(start)
    return q, endpoints, internal_starts, full_starts, pair_by_sum, edge_by_sum


def ruler_arm_profile(name: str, s: int, directions: list[Point]) -> dict[str, int | float | str]:
    arm_count = len(directions)
    marks = dense_ruler(arm_count * s)
    blocks = [marks[i * s : (i + 1) * s] for i in range(arm_count)]
    points = [
        (mark * direction[0], mark * direction[1])
        for block, direction in zip(blocks, directions)
        for mark in block
    ]
    assert len(points) == len(set(points))
    assert distance_sidon(points)
    _, _, internal_starts, starts, pair_by_sum, edge_by_sum = best_internal_fibre(
        points, s, arm_count
    )
    sums = list(pair_by_sum)
    loads = Counter(
        norm2(edge_by_sum[start]) + C * norm2(edge_by_sum[total])
        for start in starts
        for total in sums
    )
    energy = sum(load * load for load in loads.values())
    records = len(starts) * len(sums)
    weak_target = len(sums) * (len(starts) + len(points))
    return {
        "family": name,
        "s": s,
        "k": len(points),
        "h_internal": len(internal_starts),
        "h_full": len(starts),
        "N": len(sums),
        "records": records,
        "image": len(loads),
        "energy": energy,
        "max_load": max(loads.values()),
        "energy_over_records": energy / records,
        "energy_over_weak_target": energy / weak_target,
    }


def main() -> None:
    expected_matrix = {
        17: (14, 136, 1_904, 1_904, 1_904, 1),
        31: (86, 465, 39_990, 39_982, 40_006, 2),
        43: (171, 903, 154_413, 154_363, 154_513, 2),
        61: (336, 1_830, 614_880, 614_754, 615_132, 2),
    }
    for p, expected in expected_matrix.items():
        row = parabola_matrix_profile(p)
        actual = (
            row["h"], row["N"], row["records"], row["matrix_image"],
            row["matrix_energy"], row["max_matrix_load"],
        )
        assert actual == expected, (p, actual, expected)
        print("parabola-matrix", row)

    safe_profile = safe_matrix_difference_profile(13)
    assert safe_profile == (78, 2_417, 164_639, 4), safe_profile
    print("parabola-safe-matrix-directions", safe_profile)

    families = [
        ("two-perpendicular", 40, [(1, 0), (0, 1)]),
        ("two-scaled-heavy-fibre", 50, [(1, 0), (0, 47)]),
        ("three-fixed", 32, [(1, 0), (0, 1), (1, 1)]),
        ("three-growing-scale", 32, [(1, 0), (0, 1), (32, 32)]),
        ("four-fixed", 24, [(1, 0), (0, 1), (1, 1), (1, -1)]),
        ("four-growing-scale", 24, [(1, 0), (0, 1), (24, 24), (24, -24)]),
    ]
    for name, s, directions in families:
        row = ruler_arm_profile(name, s, directions)
        assert row["energy"] >= row["records"]
        assert row["max_load"] <= 3
        print("ruler-arm", row)

    print("metric scalar universal-matrix and ruler-arm stress: PASS")


if __name__ == "__main__":
    main()
