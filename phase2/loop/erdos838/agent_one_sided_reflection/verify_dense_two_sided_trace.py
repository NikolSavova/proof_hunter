#!/usr/bin/env python3
"""Exact verifier for DENSE_TWO_SIDED_TRACE_EXTRACTION.md."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    assert value
    return 1 if value > 0 else -1


def convex_four(points: list[Point], ids: tuple[int, int, int, int]) -> bool:
    a, b, c, d = ids
    # In x-order, the extreme chord ad is a diagonal exactly when b,c have
    # opposite signs relative to it.
    return orient(points[a], points[b], points[d]) != orient(
        points[a], points[c], points[d]
    )


def mixed_statistics(points: list[Point]) -> dict:
    n = len(points)
    bad = 0
    total = 0
    degrees: dict[tuple[int, int], int] = {}
    for i in range(n):
        for k in range(i + 2, n):
            plus = []
            minus = []
            for j in range(i + 1, k):
                sign = orient(points[i], points[j], points[k])
                (plus if sign > 0 else minus).append(j)
            if plus and minus:
                bad += 1
            total += len(plus) * len(minus)
            for j in plus:
                for ell in minus:
                    trace = tuple(sorted((j, ell)))
                    ids = (i, trace[0], trace[1], k)
                    assert convex_four(points, ids)
                    degrees[trace] = degrees.get(trace, 0) + 1

    assert sum(degrees.values()) == total
    assert total * 2 * n >= bad * bad  # T >= B^2/(2n)
    maximum = max(degrees.values(), default=0)
    if bad:
        assert maximum * n**3 >= bad * bad
    return {
        "n": n,
        "B": bad,
        "T": total,
        "max_trace_degree": maximum,
    }


@lru_cache(maxsize=None)
def pascal_paths(m: int, i: int) -> tuple[str, ...]:
    if i in (0, m):
        return ("",)
    return tuple("L" + p for p in pascal_paths(m - 1, i - 1)) + tuple(
        "R" + p for p in pascal_paths(m - 1, i)
    )


def pascal_sign(paths: tuple[str, ...], i: int, j: int, k: int) -> int:
    a, b, c = paths[i], paths[j], paths[k]
    depth = 0
    while a[depth] == b[depth] == c[depth]:
        depth += 1
    return -1 if a[depth] == b[depth] else 1


def pascal_statistics(parameter: int) -> dict:
    m, index = 2 * parameter - 4, parameter - 2
    paths = pascal_paths(m, index)
    n = len(paths)
    bad = total = 0
    degrees: dict[tuple[int, int], int] = {}
    for i in range(n):
        for k in range(i + 2, n):
            plus = []
            minus = []
            for j in range(i + 1, k):
                (plus if pascal_sign(paths, i, j, k) > 0 else minus).append(j)
            if plus and minus:
                bad += 1
            total += len(plus) * len(minus)
            for j in plus:
                for ell in minus:
                    trace = tuple(sorted((j, ell)))
                    degrees[trace] = degrees.get(trace, 0) + 1
    assert sum(degrees.values()) == total
    assert total * 2 * n >= bad * bad
    maximum = max(degrees.values(), default=0)
    if bad:
        assert maximum * n**3 >= bad * bad
    return {"parameter": parameter, "n": n, "B": bad, "T": total, "max_trace_degree": maximum}


def normalize(cloud: list[tuple[int, int]]) -> list[Point]:
    xs = [p[0] for p in cloud]
    ys = [p[1] for p in cloud]
    dx = max(xs) - min(xs) or 1
    dy = max(ys) - min(ys) or 1
    return [
        (Fraction(x - min(xs), dx), Fraction(y - min(ys), dy)) for x, y in cloud
    ]


def embed_clouds(left_raw, right_raw, epsilon=Fraction(1, 100)):
    left0 = normalize(left_raw)
    right0 = normalize(right_raw)
    left = [(Fraction(-2) + epsilon * x, Fraction(2) + epsilon * y) for x, y in left0]
    j = (Fraction(0), Fraction(0))
    ell = (Fraction(1), Fraction(0))
    right = [(Fraction(3) + epsilon * x, Fraction(-2) + epsilon * y) for x, y in right0]
    return left + [j, ell] + right


def sign_table(points: list[Point]) -> tuple[int, ...]:
    return tuple(orient(points[i], points[j], points[k]) for i, j, k in combinations(range(len(points)), 3))


def universality_audit() -> dict:
    # Two deliberately different rational order types.  The exact choice is
    # immaterial: the affine embeddings preserve every internal determinant.
    left_raw = [(0, 30), (1, 38), (2, 13), (3, 50), (4, 61), (5, 19)]
    right_raw = [(0, 11), (1, 8), (2, 2), (3, 51), (4, 70), (5, 37), (6, 7)]
    left0 = normalize(left_raw)
    right0 = normalize(right_raw)
    assert all(orient(left0[i], left0[j], left0[k]) for i, j, k in combinations(range(len(left0)), 3))
    assert all(orient(right0[i], right0[j], right0[k]) for i, j, k in combinations(range(len(right0)), 3))

    points = embed_clouds(left_raw, right_raw)
    p, q = len(left_raw), len(right_raw)
    j, ell = p, p + 1
    assert [x for x, _ in points] == sorted(x for x, _ in points)
    assert sign_table(points[:p]) == sign_table(left0)
    assert sign_table(points[p + 2 :]) == sign_table(right0)

    for i in range(p):
        for k in range(p + 2, p + 2 + q):
            assert orient(points[i], points[j], points[k]) != orient(
                points[i], points[ell], points[k]
            )
            assert convex_four(points, (i, j, ell, k))

    stats = mixed_statistics(points)
    assert stats["B"] >= p * q
    assert stats["max_trace_degree"] >= p * q
    return {
        "left_cloud_size": p,
        "right_cloud_size": q,
        "guaranteed_cross_bad_pairs": p * q,
        **stats,
    }


def false_side_factorization_audit() -> dict:
    # i and k are on opposite sides of the root line, but ik meets that line
    # to the right of the segment jl, so the quadruple is not convex.
    points = [
        (Fraction(-1), Fraction(100)),
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(2), Fraction(-1)),
    ]
    i, j, ell, k = range(4)
    assert orient(points[j], points[ell], points[i]) != orient(points[j], points[ell], points[k])
    assert orient(points[i], points[j], points[k]) == orient(points[i], points[ell], points[k])
    assert not convex_four(points, (i, j, ell, k))
    return {"opposite_root_line_sides_but_not_convex": True}


def main() -> None:
    expected = {
        4: (6, 4, 9),
        5: (20, 119, 2223),
        6: (70, 2036, 399469),
        7: (252, 29777, 70552355),
    }
    pascal = []
    for parameter in range(4, 8):
        row = pascal_statistics(parameter)
        assert (row["n"], row["B"], row["T"]) == expected[parameter]
        pascal.append(row)
        print(
            f"Pascal parameter={parameter}: n={row['n']} B={row['B']} "
            f"T={row['T']} max d={row['max_trace_degree']}"
        )

    universal = universality_audit()
    false_factor = false_side_factorization_audit()
    certificate = {
        "description": "dense two-sided rank-four trace extraction and universality barrier",
        "arithmetic": "integer signs and fractions.Fraction only",
        "pascal": pascal,
        "universality_regression": universal,
        "side_factorization_regression": false_factor,
        "assertions": [
            "T=sum r_ik s_ik equals total two-point trace extension incidence",
            "T >= B^2/(2n) and max trace degree >= B^2/n^3",
            "central Pascal exact values through 252 points",
            "complete cross quadrilateral grid with both detached order types preserved",
            "opposite sides of the trace line alone do not imply convexity",
        ],
    }
    output = HERE / "dense_two_sided_trace_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"universality: {universal}")
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
