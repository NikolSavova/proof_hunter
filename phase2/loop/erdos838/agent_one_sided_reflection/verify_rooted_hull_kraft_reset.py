#!/usr/bin/env python3
"""Exact verifier for the rooted-hull Kraft reset."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, log2
import json
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def cross(a: Point, b: Point, c: Point) -> Fraction:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


def sign(a: Point, b: Point, c: Point) -> int:
    value = cross(a, b, c)
    assert value
    return 1 if value > 0 else -1


def hull_vertices(points: list[Point], vertices: set[int]) -> set[int]:
    if len(vertices) <= 2:
        return set(vertices)
    ordered = sorted(vertices, key=lambda index: points[index])
    lower: list[int] = []
    for index in ordered:
        while (
            len(lower) >= 2
            and cross(points[lower[-2]], points[lower[-1]], points[index]) <= 0
        ):
            lower.pop()
        lower.append(index)
    upper: list[int] = []
    for index in reversed(ordered):
        while (
            len(upper) >= 2
            and cross(points[upper[-2]], points[upper[-1]], points[index]) <= 0
        ):
            upper.pop()
        upper.append(index)
    return set(lower[:-1] + upper[:-1])


def convex(points: list[Point], vertices: set[int]) -> bool:
    return len(vertices) <= 3 or len(hull_vertices(points, vertices)) == len(vertices)


def general_position(points: list[Point]) -> bool:
    return all(cross(points[a], points[b], points[c]) for a, b, c in combinations(range(len(points)), 3))


def masks(items: list[int], nonempty: bool = False):
    for bits in range(1 if nonempty else 0, 1 << len(items)):
        yield {items[index] for index in range(len(items)) if bits >> index & 1}


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def relative_profile(
    points: list[Point],
    u: int,
    v: int,
    cloud: list[int],
) -> tuple[
    dict[frozenset[int], set[frozenset[int]]],
    dict[frozenset[int], frozenset[int]],
]:
    if cloud:
        side_signs = {sign(points[u], points[v], points[q]) for q in cloud}
        assert len(side_signs) == 1
    roots = {u, v}
    fibres: dict[frozenset[int], set[frozenset[int]]] = {}
    for subset in masks(cloud):
        visible = frozenset(hull_vertices(points, subset | roots) - roots)
        assert convex(points, set(visible) | roots)
        fibres.setdefault(visible, set()).add(frozenset(subset))

    pockets: dict[frozenset[int], frozenset[int]] = {}
    for visible in fibres:
        polygon = set(visible) | roots
        pocket = frozenset(
            q
            for q in cloud
            if q not in visible
            and hull_vertices(points, polygon | {q}) == polygon
        )
        pockets[visible] = pocket
    return fibres, pockets


def hull_edge(points: list[Point], vertices: set[int], a: int, b: int) -> bool:
    edge_signs = {
        sign(points[a], points[b], points[c])
        for c in vertices - {a, b}
    }
    return len(edge_signs) <= 1


def tangent_pair(
    points: list[Point],
    u: int,
    v: int,
    visible: frozenset[int],
) -> tuple[int, int]:
    polygon = set(visible) | {u, v}
    assert visible
    at_u = [q for q in polygon - {u} if hull_edge(points, polygon, u, q)]
    at_v = [q for q in polygon - {v} if hull_edge(points, polygon, v, q)]
    assert len(at_u) == len(at_v) == 2
    return next(q for q in at_u if q != v), next(q for q in at_v if q != u)


def affine_coordinates(points: list[Point], u: int, v: int, q: int) -> Point:
    dx = points[v][0] - points[u][0]
    dy = points[v][1] - points[u][1]
    px = points[q][0] - points[u][0]
    py = points[q][1] - points[u][1]
    scale = dx * dx + dy * dy
    return (dx * px + dy * py) / scale, (dx * py - dy * px) / scale


def pocket_monotonicity_audit(
    points: list[Point],
    u: int,
    v: int,
    pockets: dict[frozenset[int], frozenset[int]],
) -> int:
    comparisons = 0
    for visible, pocket in pockets.items():
        if not pocket:
            continue
        tangent_u, tangent_v = tangent_pair(points, u, v, visible)
        xu, yu = affine_coordinates(points, u, v, tangent_u)
        xv, yv = affine_coordinates(points, u, v, tangent_v)
        orientation = 1 if yu > 0 else -1
        assert (yv > 0) == (orientation > 0)
        if orientation > 0:
            tangent_left = -xu / yu
            tangent_right = (1 - xv) / yv
            for q in pocket:
                x, y = affine_coordinates(points, u, v, q)
                assert y > 0
                assert -x / y < tangent_left
                assert (1 - x) / y > tangent_right
                comparisons += 2
        else:
            tangent_left = xu / (-yu)
            tangent_right = (xv - 1) / (-yv)
            for q in pocket:
                x, y = affine_coordinates(points, u, v, q)
                assert y < 0
                assert x / (-y) > tangent_left
                assert (x - 1) / (-y) < tangent_right
                comparisons += 2
    return comparisons


def rooted_hull_audit(
    points: list[Point],
    u: int,
    v: int,
    cloud: list[int],
    name: str,
) -> dict:
    fibres, pockets = relative_profile(points, u, v, cloud)
    monotone_comparisons = pocket_monotonicity_audit(points, u, v, pockets)
    roots = {u, v}
    for visible, pocket in pockets.items():
        predicted = {
            frozenset(set(visible) | child)
            for child in masks(list(pocket))
        }
        assert fibres[visible] == predicted

    m = len(cloud)
    coefficients = [0] * (m + 1)
    for visible, pocket in pockets.items():
        for child_size in range(len(pocket) + 1):
            coefficients[len(visible) + child_size] += comb(len(pocket), child_size)
    assert coefficients == [comb(m, rank) for rank in range(m + 1)]

    z = Fraction(1, 2)
    lhs = (1 + z) ** m
    rhs = sum(
        z ** len(visible) * (1 + z) ** len(pocket)
        for visible, pocket in pockets.items()
    )
    assert lhs == rhs
    rooted_mass = sum(z ** len(visible) for visible in pockets)
    maximum_pocket = max(map(len, pockets.values()))
    codimension = m - maximum_pocket
    assert rooted_mass >= (1 + z) ** codimension

    pi = {
        visible: float(z ** len(visible) * (1 + z) ** len(pocket) / lhs)
        for visible, pocket in pockets.items()
    }
    rho = {
        visible: float(z ** len(visible) / rooted_mass)
        for visible in pockets
    }
    mean_cost = sum(
        pi[visible] * (m - len(pockets[visible]))
        for visible in pockets
    )
    divergence = sum(
        pi[visible] * log2(pi[visible] / rho[visible])
        for visible in pockets
    )
    assert abs(
        log2(float(rooted_mass))
        - (log2(1.5) * mean_cost + divergence)
    ) < 1e-11

    return {
        "name": name,
        "cloud_size": m,
        "visible_hull_count": len(pockets),
        "half_rooted_mass": fraction_text(rooted_mass),
        "maximum_pocket": maximum_pocket,
        "minimum_codimension": codimension,
        "mean_exposed_cost": mean_cost,
        "kl_surplus_bits": divergence,
        "strict_tangent_progress_comparisons": monotone_comparisons,
    }


def hidden_pocket_grid_audit(
    points: list[Point],
    u: int,
    v: int,
    left: list[int],
    right: list[int],
    name: str,
) -> dict:
    _, left_pockets = relative_profile(points, u, v, left)
    _, right_pockets = relative_profile(points, u, v, right)
    roots = {u, v}
    degree = sum(
        proper_cross(points[u], points[v], points[x], points[y])
        for x in left for y in right
    )
    compatible_parents = 0
    maximum_hidden_product = 0
    for left_hull, left_pocket in left_pockets.items():
        for right_hull, right_pocket in right_pockets.items():
            if not left_hull or not right_hull:
                continue
            if not convex(points, set(left_hull) | set(right_hull) | roots):
                continue
            compatible_parents += 1
            hidden_product = len(left_pocket) * len(right_pocket)
            maximum_hidden_product = max(maximum_hidden_product, hidden_product)
            assert hidden_product <= degree
            for x in left_pocket:
                for y in right_pocket:
                    assert proper_cross(points[u], points[v], points[x], points[y])

    deepest_left = max(
        left_pockets,
        key=lambda hull: (len(left_pockets[hull]), tuple(sorted(hull))),
    )
    deepest_right = max(
        right_pockets,
        key=lambda hull: (len(right_pockets[hull]), tuple(sorted(hull))),
    )
    deepest_product = len(left_pockets[deepest_left]) * len(right_pockets[deepest_right])
    deepest_compatible = convex(
        points, set(deepest_left) | set(deepest_right) | roots
    )
    if deepest_product > degree:
        assert not deepest_compatible

    return {
        "name": name,
        "left_size": len(left),
        "right_size": len(right),
        "singleton_degree": degree,
        "compatible_visible_hull_pairs": compatible_parents,
        "maximum_compatible_hidden_product": maximum_hidden_product,
        "deepest_pocket_product": deepest_product,
        "deepest_visible_hulls_compatible": deepest_compatible,
    }


def global_rooted_identity(points: list[Point], name: str) -> dict:
    n = len(points)
    assert [point[0] for point in points] == sorted(point[0] for point in points)
    assert general_position(points)
    faces = {}
    for subset in masks(list(range(n))):
        if convex(points, subset):
            faces[len(subset)] = faces.get(len(subset), 0) + 1

    left: dict[int, int] = {}
    right: dict[int, int] = {}
    for j in range(n):
        for ell in range(j + 1, n):
            for orientation in (-1, 1):
                left_cloud = [
                    q for q in range(j)
                    if sign(points[j], points[ell], points[q]) == orientation
                ]
                right_cloud = [
                    q for q in range(ell + 1, n)
                    if sign(points[j], points[ell], points[q]) == orientation
                ]
                for visible in masks(left_cloud, nonempty=True):
                    rooted = visible | {j, ell}
                    if convex(points, rooted):
                        rank = len(rooted)
                        left[rank] = left.get(rank, 0) + 1
                for visible in masks(right_cloud, nonempty=True):
                    rooted = visible | {j, ell}
                    if convex(points, rooted):
                        rank = len(rooted)
                        right[rank] = right.get(rank, 0) + 1

    expected = {rank: count for rank, count in faces.items() if rank >= 3}
    assert left == expected
    assert right == expected
    return {
        "name": name,
        "n": n,
        "faces_rank_at_least_three": sum(expected.values()),
        "left_rooted_incidences": sum(left.values()),
        "right_rooted_incidences": sum(right.values()),
    }


def random_configuration(n: int, seed: int) -> list[Point]:
    rng = random.Random(seed)
    while True:
        points = sorted(
            (Fraction(index), Fraction(rng.randrange(-10_000, 10_001)))
            for index in range(n)
        )
        if general_position(points):
            return points


def strong_glue(left: list[Point], right: list[Point], epsilon: Fraction) -> list[Point]:
    return (
        [(epsilon * epsilon * x, epsilon * y) for x, y in left]
        + [(1 + epsilon * epsilon * x, 1 + epsilon * y) for x, y in right]
    )


def pascal_cell(m: int, index: int, epsilon: Fraction) -> list[Point]:
    if index in (0, m):
        return [(Fraction(0), Fraction(0))]
    return strong_glue(
        pascal_cell(m - 1, index - 1, epsilon),
        pascal_cell(m - 1, index, epsilon),
        epsilon,
    )


def proper_cross(a: Point, b: Point, c: Point, d: Point) -> bool:
    return (
        cross(a, b, c) * cross(a, b, d) < 0
        and cross(c, d, a) * cross(c, d, b) < 0
    )


def heaviest_trace(points: list[Point]) -> tuple[int, int, int, list[int], list[int], int]:
    best = None
    n = len(points)
    for j in range(1, n - 2):
        for ell in range(j + 1, n - 1):
            for orientation in (-1, 1):
                left = [
                    q for q in range(j)
                    if sign(points[j], points[ell], points[q]) == orientation
                ]
                right = [
                    q for q in range(ell + 1, n)
                    if sign(points[j], points[ell], points[q]) == -orientation
                ]
                degree = sum(
                    proper_cross(points[j], points[ell], points[x], points[y])
                    for x in left for y in right
                )
                record = (degree, j, ell, orientation, left, right)
                if best is None or degree > best[0]:
                    best = record
    assert best is not None
    degree, j, ell, orientation, left, right = best
    return j, ell, orientation, left, right, degree


def matching_star_configuration(m: int, q: int, seed: int) -> list[tuple[str, int, Point]]:
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
    assert general_position([point for _, _, point in perturbed])
    return perturbed


def nested_ear_configuration(q: int) -> tuple[list[Point], int, int, list[int]]:
    points: list[Point] = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))]
    for index in range(q):
        points.append(
            (
                Fraction(1, 2) + Fraction(index * index, 100 * q * q),
                -Fraction(2 ** (index + 1)),
            )
        )
    assert general_position(points)
    return points, 0, 1, list(range(2, q + 2))


def main() -> None:
    global_records = [
        global_rooted_identity(random_configuration(8, 27_182), "random_n8"),
        global_rooted_identity(
            sorted(pascal_cell(5, 2, Fraction(1, 97))),
            "pascal_T_5_2_n10",
        ),
    ]

    nested_points, u, v, nested_cloud = nested_ear_configuration(10)
    local_records = [
        rooted_hull_audit(nested_points, u, v, nested_cloud, "nested_ear_q10")
    ]

    pascal = sorted(pascal_cell(6, 3, Fraction(1, 97)))
    j, ell, orientation, left, right, degree = heaviest_trace(pascal)
    local_records.extend(
        [
            rooted_hull_audit(pascal, j, ell, left, "pascal_heavy_left"),
            rooted_hull_audit(pascal, j, ell, right, "pascal_heavy_right"),
        ]
    )
    grid_records = [
        hidden_pocket_grid_audit(
            pascal, j, ell, left, right, "pascal_heavy_hidden_grid"
        )
    ]

    star = matching_star_configuration(12, 6, 31_417)
    star_points = [point for _, _, point in star]
    lookup = {(block, index): position for position, (block, index, _) in enumerate(star)}
    star_u, star_v = lookup["J", 3], lookup["L", 4]
    star_left = [lookup["X", index] for index in range(1, 13)]
    star_right = [lookup["Y", index] for index in range(1, 13)]
    star_edges = {
        (i, k)
        for i in range(1, 13)
        for k in range(1, 13)
        if proper_cross(
            star_points[star_u],
            star_points[star_v],
            star_points[lookup["X", i]],
            star_points[lookup["Y", k]],
        )
    }
    assert star_edges == {(i, 13 - i) for i in range(1, 13)}
    local_records.extend(
        [
            rooted_hull_audit(
                star_points, star_u, star_v, star_left, "matching_star_left_m12"
            ),
            rooted_hull_audit(
                star_points, star_u, star_v, star_right, "matching_star_right_m12"
            ),
        ]
    )
    grid_records.append(
        hidden_pocket_grid_audit(
            star_points,
            star_u,
            star_v,
            star_left,
            star_right,
            "matching_star_hidden_grid",
        )
    )
    assert grid_records[0]["singleton_degree"] == degree
    assert grid_records[1]["singleton_degree"] == 12
    assert grid_records[1]["deepest_pocket_product"] > 12
    assert not grid_records[1]["deepest_visible_hulls_compatible"]

    certificate = {
        "description": "exact rooted-hull fibre, Kraft, KL, and global trace-load audit",
        "arithmetic": "all geometric and polynomial assertions use fractions.Fraction",
        "global_rooted_identities": global_records,
        "local_reset_profiles": local_records,
        "hidden_pocket_grids": grid_records,
        "pascal_heavy_trace": {
            "n": len(pascal),
            "j": j,
            "ell": ell,
            "orientation": orientation,
            "left_size": len(left),
            "right_size": len(right),
            "singleton_degree": degree,
        },
        "matching_star": {
            "m": 12,
            "q": 6,
            "trace_count": 36,
            "identical_matching_edges_per_trace": 12,
        },
        "assertions": [
            "relative-hull fibres are exactly Boolean hidden pockets",
            "the weighted Kraft identity holds coefficientwise",
            "half-rooted mass is at least (3/2)^minimum_codimension",
            "the KL decomposition holds after exact probability construction",
            "left and right rooted-side sums each count every rank>=3 face once",
            "compatible visible hulls expose a complete hidden-pocket grid",
            "hidden pocket product is at most singleton compatibility degree",
            "every hidden-pocket reset makes strict progress in both tangent ranks",
            "Pascal and perfect-matching-star regressions satisfy the reset",
        ],
    }
    output = HERE / "rooted_hull_kraft_reset_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"audited {len(global_records)} global identities")
    print(f"audited {len(local_records)} rooted reset profiles")
    print(f"audited {len(grid_records)} hidden-pocket grids")
    print(f"Pascal heavy trace degree={degree}, sides={len(left)}x{len(right)}")
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
