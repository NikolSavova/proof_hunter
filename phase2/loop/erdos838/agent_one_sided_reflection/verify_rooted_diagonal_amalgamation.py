#!/usr/bin/env python3
"""Exact audit of rooted-diagonal two-tangent amalgamation."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def cross(a: Point, b: Point) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def sub(a: Point, b: Point) -> Point:
    return a[0] - b[0], a[1] - b[1]


def orient(points: list[Point], a: int, b: int, c: int) -> int:
    value = cross(sub(points[b], points[a]), sub(points[c], points[a]))
    assert value
    return 1 if value > 0 else -1


def convex(points: list[Point], vertices: set[int]) -> bool:
    ordered = sorted(vertices)
    if len(ordered) <= 3:
        return True
    lower: list[int] = []
    upper: list[int] = []
    for x in ordered:
        while len(lower) >= 2 and orient(points, lower[-2], lower[-1], x) <= 0:
            lower.pop()
        lower.append(x)
        while len(upper) >= 2 and orient(points, upper[-2], upper[-1], x) >= 0:
            upper.pop()
        upper.append(x)
    return len(set(lower + upper)) == len(ordered)


def hull_edge(points: list[Point], vertices: set[int], a: int, b: int) -> bool:
    signs = {orient(points, a, b, c) for c in vertices - {a, b}}
    return len(signs) == 1


def tangent_pair(points: list[Point], vertices: set[int], j: int, ell: int) -> tuple[int, int]:
    at_j = [x for x in vertices - {j} if hull_edge(points, vertices, j, x)]
    at_ell = [x for x in vertices - {ell} if hull_edge(points, vertices, ell, x)]
    assert len(at_j) == len(at_ell) == 2
    return (
        next(x for x in at_j if x != ell),
        next(x for x in at_ell if x != j),
    )


def intersection_parameter(points: list[Point], x: int, y: int, j: int, ell: int) -> Fraction:
    direction = sub(points[y], points[x])
    denominator = cross(sub(points[ell], points[j]), direction)
    assert denominator
    return cross(sub(points[x], points[j]), direction) / denominator


def subsets(items: list[int]):
    for mask in range(1, 1 << len(items)):
        yield {items[a] for a in range(len(items)) if mask >> a & 1}


def general_position(points: list[Point]) -> bool:
    return all(orient(points, *triple) for triple in combinations(range(len(points)), 3))


def proper_cross(a: Point, b: Point, c: Point, d: Point) -> bool:
    return (
        cross(sub(b, a), sub(c, a)) * cross(sub(b, a), sub(d, a)) < 0
        and cross(sub(d, c), sub(a, c)) * cross(sub(d, c), sub(b, c)) < 0
    )


def matching_star_configuration(m: int, q: int, seed: int) -> list[tuple[str, int, Point]]:
    """A small exact rational perturbation of the four-block construction."""
    delta = Fraction(1, 100 * m)
    height = delta / 4
    epsilon = Fraction(1, 100_000_000 * m * q)
    base: list[tuple[str, int, Point]] = []
    for i in range(1, m + 1):
        base.append(("X", i, (Fraction(-2), Fraction(i))))
    for a in range(1, q + 1):
        base.append(("J", a, (-delta, height)))
    for b in range(1, q + 1):
        base.append(("L", b, (delta, height)))
    for k in range(1, m + 1):
        base.append(("Y", k, (Fraction(2), Fraction(k - m - 1))))

    rng = random.Random(seed)
    perturbed = [
        (
            block,
            index,
            (
                point[0] + epsilon * rng.randrange(-1000, 1001),
                point[1] + epsilon * rng.randrange(-1000, 1001),
            ),
        )
        for block, index, point in base
    ]
    perturbed.sort(key=lambda item: item[2][0])
    assert [block for block, _, _ in perturbed] == (
        ["X"] * m + ["J"] * q + ["L"] * q + ["Y"] * m
    )
    assert general_position([point for _, _, point in perturbed])
    return perturbed


def audit_matching_star(m: int, q: int, seed: int) -> dict:
    configuration = matching_star_configuration(m, q, seed)
    lookup = {(block, index): point for block, index, point in configuration}
    extension_count = 0
    for a in range(1, q + 1):
        for b in range(1, q + 1):
            edges = set()
            for i in range(1, m + 1):
                for k in range(1, m + 1):
                    crossed = proper_cross(
                        lookup["J", a],
                        lookup["L", b],
                        lookup["X", i],
                        lookup["Y", k],
                    )
                    assert crossed == (i + k == m + 1)
                    if crossed:
                        edges.add((i, k))
                        extension_count += 1
            assert len(edges) == m
            assert len({i for i, _ in edges}) == len({k for _, k in edges}) == m
            # A matching has no K_{u,v} with u*v>1.  Hence deletion rules
            # out every higher glued face supported on both outer clouds.
            assert max(
                sum(edge[0] == i for edge in edges) for i in range(1, m + 1)
            ) == 1
            assert max(
                sum(edge[1] == k for edge in edges) for k in range(1, m + 1)
            ) == 1
    assert extension_count == q * q * m
    return {"m": m, "q": q, "trace_count": q * q, "extension_mass": extension_count}


def audit_configuration(points: list[Point]) -> dict:
    n = len(points)
    assert [x for x, _ in points] == sorted(x for x, _ in points)
    assert general_position(points)
    local_multiplicity: dict[int, int] = {}
    local_by_rank: dict[int, int] = {}

    for j in range(1, n - 2):
        for ell in range(j + 1, n - 1):
            for sigma in (-1, 1):
                left = [x for x in range(j) if orient(points, j, ell, x) == sigma]
                right = [y for y in range(ell + 1, n) if orient(points, j, ell, y) == -sigma]
                left_faces = []
                right_faces = []
                for X in subsets(left):
                    rooted = X | {j, ell}
                    if convex(points, rooted):
                        left_faces.append((X, tangent_pair(points, rooted, j, ell)))
                for Y in subsets(right):
                    rooted = Y | {j, ell}
                    if convex(points, rooted):
                        right_faces.append((Y, tangent_pair(points, rooted, j, ell)))

                for X, (xj, xl) in left_faces:
                    for Y, (yj, yl) in right_faces:
                        compatible = (
                            intersection_parameter(points, xj, yj, j, ell) > 0
                            and intersection_parameter(points, xl, yl, j, ell) < 1
                        )
                        union = X | Y | {j, ell}
                        is_face = convex(points, union)
                        assert compatible == is_face
                        if not compatible:
                            continue

                        # Once the two tangent guards pass, every cross
                        # singleton pair is automatically a rooted convex quad.
                        for x in X:
                            for y in Y:
                                parameter = intersection_parameter(points, x, y, j, ell)
                                assert 0 < parameter < 1

                        mask = sum(1 << x for x in union)
                        local_multiplicity[mask] = local_multiplicity.get(mask, 0) + 1
                        rank = len(union)
                        local_by_rank[rank] = local_by_rank.get(rank, 0) + 1

    faces_by_rank: dict[int, int] = {}
    expected_multiplicity: dict[int, int] = {}
    mixed_rank_four = 0
    for mask in range(1 << n):
        vertices = {x for x in range(n) if mask >> x & 1}
        if not convex(points, vertices):
            continue
        rank = len(vertices)
        faces_by_rank[rank] = faces_by_rank.get(rank, 0) + 1
        if rank < 4:
            continue
        ordered = sorted(vertices)
        expected = 0
        for a in range(1, rank - 2):
            j, ell = ordered[a], ordered[a + 1]
            left = ordered[:a]
            right = ordered[a + 2 :]
            left_signs = {orient(points, j, ell, x) for x in left}
            right_signs = {orient(points, j, ell, y) for y in right}
            if len(left_signs) == len(right_signs) == 1 and left_signs != right_signs:
                expected += 1
        expected_multiplicity[mask] = expected
        assert local_multiplicity.get(mask, 0) == expected
        assert expected <= rank - 1
        if rank == 4:
            mixed_rank_four += expected

    for rank, incidences in local_by_rank.items():
        assert incidences <= (rank - 1) * faces_by_rank[rank]

    # Independent rank-four calculation T=sum r_ik s_ik.
    T = 0
    for i in range(n):
        for k in range(i + 2, n):
            r = sum(orient(points, i, j, k) > 0 for j in range(i + 1, k))
            s = k - i - 1 - r
            T += r * s
    assert mixed_rank_four == T
    assert local_by_rank.get(4, 0) == T

    return {
        "n": n,
        "convex_faces": sum(faces_by_rank.values()),
        "local_bank_incidences": sum(local_by_rank.values()),
        "rank_four_T": T,
        "maximum_decoder_load": max(local_multiplicity.values(), default=0),
        "maximum_rank_minus_one": max((k - 1 for k in faces_by_rank), default=0),
    }


def random_configuration(n: int, seed: int) -> list[Point]:
    rng = random.Random(seed)
    while True:
        points = [(Fraction(i), Fraction(rng.randrange(-10_000, 10_001))) for i in range(n)]
        try:
            if general_position(points):
                return points
        except AssertionError:
            pass


def convex_polygon_regression() -> list[Point]:
    # Six rational points on a circle, followed by a small x-shear to make
    # all x-coordinates distinct.  This stresses mixed rooted side faces,
    # rather than only pure cap/cup histories.
    points = []
    for t in map(Fraction, (-3, -1)):
        x = (1 - t * t) / (1 + t * t)
        y = 2 * t / (1 + t * t)
        points.append((x + y / 10, y))
    for t in (Fraction(-1, 3), Fraction(1, 3), Fraction(1), Fraction(3)):
        x = (1 - t * t) / (1 + t * t)
        y = 2 * t / (1 + t * t)
        points.append((x + y / 10, y))
    return sorted(points)


def main() -> None:
    records = [audit_configuration(convex_polygon_regression())]
    for seed in range(40):
        records.append(audit_configuration(random_configuration(9, 10_000 + seed)))
    matching_stars = [
        audit_matching_star(5, 4, 31_415),
        audit_matching_star(10, 8, 31_416),
        audit_matching_star(20, 12, 31_417),
    ]
    certificate = {
        "description": "exact two-tangent rooted diagonal amalgamation and global load audit",
        "arithmetic": "fractions.Fraction only",
        "configurations": records,
        "matching_star_regressions": matching_stars,
        "assertions": [
            "union convex iff left tangent crosses after j and right tangent crosses before l",
            "passing tangent guards implies every cross rooted quadrilateral is convex",
            "local decoder multiplicity equals number of consecutive-x diagonal pairs",
            "rank-k global overlap at most k-1",
            "rank-four local bank sum equals T=sum r_ik s_ik",
            "q^2 traces can share the same m-edge matching extension graph",
            "the matching extension graph has no higher outer-cloud amalgamation",
        ],
    }
    output = HERE / "rooted_diagonal_amalgamation_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"audited {len(records)} exact configurations")
    print(f"maximum n={max(row['n'] for row in records)}")
    print(f"maximum T={max(row['rank_four_T'] for row in records)}")
    print(
        "maximum matching-star mass="
        f"{max(row['extension_mass'] for row in matching_stars)}"
    )
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
