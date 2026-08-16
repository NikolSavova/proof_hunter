#!/usr/bin/env python3
"""Exact audit for the common-ear/common-onion Hall obstruction.

The witness is deliberately small (r=6), but every assertion checked here
is the finite instance of the parametric construction proved in REPORT.md.
All predicates use exact rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


Point = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point] | tuple[Point, ...]) -> tuple[Point, ...]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return tuple(pts)

    lower: list[Point] = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: list[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return tuple(lower[:-1] + upper[:-1])


def is_convex_face(points: list[Point] | tuple[Point, ...]) -> bool:
    return len(hull(points)) == len(points)


def strictly_inside_triangle(x: Point, tri: tuple[Point, Point, Point]) -> bool:
    vals = [orient(tri[i], tri[(i + 1) % 3], x) for i in range(3)]
    return all(v > 0 for v in vals) or all(v < 0 for v in vals)


def make_inner_points(count: int, tri: tuple[Point, Point, Point], existing: list[Point]) -> list[Point]:
    """Choose exact rational points in a tiny open neighborhood of the centroid.

    Candidates lie on a rational parabola.  We additionally reject every
    candidate on a line through two earlier points, so the whole configuration
    is in general position.
    """
    cx = sum(x for x, _ in tri) / 3
    cy = sum(y for _, y in tri) / 3
    den = 10**6
    answer: list[Point] = []
    k = 1
    while len(answer) < count:
        t = Fraction(k, den)
        candidate = (cx + t, cy + t * t)
        prior = existing + answer
        if strictly_inside_triangle(candidate, tri) and all(
            orient(a, b, candidate) != 0 for a, b in combinations(prior, 2)
        ):
            answer.append(candidate)
        k += 1
        if k >= den // 100:
            raise RuntimeError("candidate search escaped the protected neighborhood")
    return answer


def main() -> None:
    r = 6
    g = 1
    m = 5 * r
    last = m - 1
    chain: list[Point] = [
        (Fraction(i), Fraction(i * (last - i))) for i in range(m)
    ]
    apex: Point = (Fraction(-1), Fraction(m * m))
    centre_index = last // 2
    anchors = (chain[0], chain[centre_index], chain[last])

    n = 2 ** (r + g)
    inner_count = n - m - 1
    assert inner_count > 0
    inner = make_inner_points(inner_count, anchors, chain + [apex])
    ambient = chain + [apex] + inner

    # Exact general position.
    triple_count = 0
    for a, b, c in combinations(ambient, 3):
        triple_count += 1
        assert orient(a, b, c) != 0

    fixed = {0, centre_index, last}
    variable = [i for i in range(m) if i not in fixed]
    repaired_target = frozenset((apex, chain[0], chain[last]))
    rooted_triples_checked = 0
    for i, j, k in combinations(range(m), 3):
        rooted_triples_checked += 1
        assert strictly_inside_triangle(chain[j], (apex, chain[i], chain[k]))
    source_count = 0
    common_pocket: frozenset[Point] | None = None

    for choice in combinations(variable, r - 3):
        indices = sorted(fixed | set(choice))
        source = [chain[i] for i in indices]
        source_set = set(source)
        assert is_convex_face(source)

        addable: list[Point] = []
        for x in ambient:
            if x not in source_set and is_convex_face(source + [x]):
                addable.append(x)
        assert set(addable) == set(chain) - source_set
        assert len(addable) == 4 * r
        assert len(addable) <= 4 * (r + 1)

        assert frozenset(hull(source + [apex])) == repaired_target
        assert all(strictly_inside_triangle(x, anchors) for x in inner)

        source_hull = hull(source)
        pocket = frozenset(
            x
            for x in ambient
            if x not in source_set
            and len(source_hull) >= 3
            and all(
                orient(source_hull[i], source_hull[(i + 1) % len(source_hull)], x) > 0
                for i in range(len(source_hull))
            )
        )
        # Depending on the orientation returned by monotone chain, reverse the
        # sign test if needed.
        if not pocket:
            pocket = frozenset(
                x
                for x in ambient
                if x not in source_set
                and all(
                    orient(source_hull[i], source_hull[(i + 1) % len(source_hull)], x) < 0
                    for i in range(len(source_hull))
                )
            )
        assert pocket == frozenset(inner)
        if common_pocket is None:
            common_pocket = pocket
        assert pocket == common_pocket
        source_count += 1

    expected_sources = math.comb(5 * r - 3, r - 3)
    assert source_count == expected_sources
    assert len(ambient) == n
    assert math.ceil(math.log2(n)) == r + g

    certificate = {
        "r": r,
        "g": g,
        "n": n,
        "ell": r + g,
        "outer_chain_size": m,
        "inner_pocket_size": inner_count,
        "source_count": source_count,
        "source_count_formula": f"binom({5*r-3},{r-3})",
        "u_each_source": 4 * r,
        "near_max_threshold": 4 * (r + 1),
        "common_repaired_target_size": len(repaired_target),
        "max_chain_vertices_in_any_apex_containing_face": 2,
        "rooted_triples_checked": rooted_triples_checked,
        "common_tangent_endpoint_indices": [0, last],
        "common_onion_pocket": True,
        "general_position_triples_checked": triple_count,
        "source_information_bits": math.log2(source_count),
        "verdict": (
            "exact common-ear/common-onion obstruction verified; "
            "this refutes endpoint-only polynomial-ambiguity recovery, not RNP itself"
        ),
    }
    (HERE / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))


if __name__ == "__main__":
    main()
