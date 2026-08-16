#!/usr/bin/env python3
"""Exact certificates for the pocket-restart attack on Erdos 838.

The checks are deliberately finite and exact (integers or Fractions):

* visible chains of one fixed maximal face need not be laminar;
* the apex/concave-chain family has a congestion-one, history-encoding
  restart into the strict final pocket;
* hull expansion is order independent on the certificates; and
* nested rational triangles have linear onion depth both for uniform
  subsets and for the activity-1/2 Boolean law (Bernoulli parameter 1/3).
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path


Point = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point], indices: list[int]) -> list[int]:
    if len(indices) <= 1:
        return indices[:]
    ordered = sorted(indices, key=lambda i: points[i])

    def half(sequence) -> list[int]:
        answer: list[int] = []
        for i in sequence:
            while len(answer) >= 2 and orient(
                points[answer[-2]], points[answer[-1]], points[i]
            ) <= 0:
                answer.pop()
            answer.append(i)
        return answer

    lower = half(ordered)
    upper = half(reversed(ordered))
    return lower[:-1] + upper[:-1]


def is_convex(points: list[Point], indices: list[int]) -> bool:
    return len(indices) <= 2 or len(hull(points, indices)) == len(indices)


def general_position(points: list[Point]) -> bool:
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def check_crossing_visible_pockets() -> dict[str, object]:
    """A fixed maximal face with two crossing hidden boundary intervals."""
    face_points: list[Point] = [(Fraction(x), Fraction(x * x)) for x in range(-4, 5)]
    blockers: list[Point] = [(Fraction(-8), Fraction(-5)),
                             (Fraction(-8), Fraction(17))]
    points = face_points + blockers
    assert general_position(points)
    face = list(range(9))
    assert is_convex(points, face)
    hidden: list[list[int]] = []
    for p in (9, 10):
        new_hull = set(hull(points, face + [p]))
        hidden.append([i for i in face if i not in new_hull])
        assert not is_convex(points, face + [p])
    # No one-point extension is convex, hence heredity makes the face maximal.
    assert hidden == [[1, 2, 3], [0, 1, 2]]
    left, right = map(set, hidden)
    assert left & right and not left <= right and not right <= left
    return {
        "coordinates": [[str(x), str(y)] for x, y in points],
        "maximal_face": face,
        "hidden_visible_chains": hidden,
        "intersection": sorted(left & right),
        "laminar": False,
    }


def visible_family(chain_size: int) -> tuple[list[Point], int]:
    """A strict concave chain q_0,...,q_(N-1) and a high apex."""
    last = chain_size - 1
    chain = [
        (Fraction(i), Fraction(i * (last - i)))
        for i in range(chain_size)
    ]
    apex = (Fraction(-1), Fraction(chain_size * chain_size))
    return chain + [apex], chain_size


def residual_capacity(rank: int) -> Fraction:
    """Capacity left after the canonical cover charges in the HW2 flow."""
    return Fraction(2) - Fraction(3 * rank, 2 ** rank)


def check_visible_restart(chain_size: int = 11) -> dict[str, object]:
    """Route every maximal-triangle bad incidence injectively into its pocket.

    All maximal apex triangles expand by visible flips to the full endpoint
    triangle.  Its strict pocket contains q_1,...,q_(N-2), a Boolean carrier.
    For N>=11 this carrier has at least C(N,2)(N-2) faces, so a binary rank
    encodes the complete source (i,k,j) with congestion one.
    """
    assert chain_size >= 11
    points, apex = visible_family(chain_size)
    assert general_position(points)
    chain = list(range(chain_size))
    assert is_convex(points, chain)

    sources: list[tuple[int, int, int]] = []
    transition_checks = 0
    for i in range(chain_size):
        for k in range(i + 1, chain_size):
            triangle = [apex, i, k]
            assert is_convex(points, triangle)
            for j in chain:
                if j in (i, k):
                    continue
                source_hull = set(hull(points, triangle + [j]))
                if i < j < k:
                    expected = {apex, i, k}
                elif j < i:
                    expected = {apex, j, k}
                else:
                    expected = {apex, i, j}
                assert source_hull == expected
                assert not is_convex(points, triangle + [j])
                sources.append((i, k, j))
                transition_checks += 1

            # At most two exterior expansions reach the common full cage.
            current = triangle
            if i > 0:
                current = hull(points, current + [0])
            if k < chain_size - 1:
                current = hull(points, current + [chain_size - 1])
            assert set(current) == {apex, 0, chain_size - 1}

    expected_sources = comb(chain_size, 2) * (chain_size - 2)
    assert len(sources) == expected_sources
    strict_pocket = list(range(1, chain_size - 1))
    assert 2 ** len(strict_pocket) >= len(sources)

    targets: dict[int, tuple[int, int, int]] = {}
    minimum_capacity = Fraction(10**9)
    rank_histogram: dict[int, int] = {}
    for code, source in enumerate(sources):
        target_mask = sum(
            1 << strict_pocket[bit]
            for bit in range(len(strict_pocket))
            if code >> bit & 1
        )
        assert target_mask not in targets
        targets[target_mask] = source
        target = [i for i in strict_pocket if target_mask >> i & 1]
        assert is_convex(points, target)
        rank = len(target)
        rank_histogram[rank] = rank_histogram.get(rank, 0) + 1
        minimum_capacity = min(minimum_capacity, residual_capacity(rank))

    # Each source incidence has half-activity demand 2^-3.  Even after all
    # canonical cover charges, every target has at least 1/2 residual capacity.
    source_demand = Fraction(1, 8)
    assert minimum_capacity >= Fraction(1, 2)
    assert source_demand <= minimum_capacity
    return {
        "chain_size": chain_size,
        "coordinates": [[str(x), str(y)] for x, y in points],
        "maximal_apex_triangles": comb(chain_size, 2),
        "bad_incidences_routed": len(sources),
        "transition_checks": transition_checks,
        "strict_pocket_size": len(strict_pocket),
        "strict_pocket_boolean_faces": 2 ** len(strict_pocket),
        "injection_unused_targets": 2 ** len(strict_pocket) - len(sources),
        "target_rank_histogram": {str(k): v for k, v in sorted(rank_histogram.items())},
        "source_demand": str(source_demand),
        "minimum_target_residual_capacity": str(minimum_capacity),
        "maximum_relative_load": str(source_demand / minimum_capacity),
        "congestion": 1,
    }


def check_hull_expansion_identity() -> dict[str, int]:
    """Exhaust ext(ext(S)+p)=ext(S+p) on both finite certificates."""
    point_sets = [
        [(Fraction(x), Fraction(x * x)) for x in range(-4, 5)]
        + [(Fraction(-8), Fraction(-5)), (Fraction(-8), Fraction(17))],
        visible_family(11)[0],
    ]
    checks = 0
    for points in point_sets:
        n = len(points)
        for mask in range(1 << n):
            subset = [i for i in range(n) if mask >> i & 1]
            exterior = hull(points, subset)
            for p in range(n):
                lhs = set(hull(points, exterior + [p]))
                rhs = set(hull(points, subset + [p]))
                assert lhs == rhs
                checks += 1
    return {"point_sets": len(point_sets), "exact_subset_point_checks": checks}


def nested_triangles(depth: int) -> list[Point]:
    """The exact shrinking/rotating rational family from the onion audit."""
    base = [(Fraction(-3), Fraction(-2)),
            (Fraction(3), Fraction(-2)),
            (Fraction(0), Fraction(4))]
    a, b = 1, 0  # (3+4i)^level
    points: list[Point] = []
    for level in range(depth):
        denominator = 10 ** level * 5 ** level
        points.extend(
            (Fraction(a * x - b * y, denominator),
             Fraction(b * x + a * y, denominator))
            for x, y in base
        )
        a, b = 3 * a - 4 * b, 4 * a + 3 * b
    return points


def onion_depth(points: list[Point], subset: list[int]) -> int:
    remaining = subset[:]
    depth = 0
    while remaining:
        depth += 1
        layer = set(hull(points, remaining))
        remaining = [i for i in remaining if i not in layer]
    return depth


def check_nested_depth(max_depth: int = 5) -> list[dict[str, object]]:
    """Exact linear-depth certificates for uniform and half-activity laws."""
    reports: list[dict[str, object]] = []
    for depth in range(1, max_depth + 1):
        points = nested_triangles(depth)
        assert general_position(points)
        n = len(points)
        total_uniform = 0
        weighted_numerator = Fraction()
        weighted_denominator = Fraction()
        for mask in range(1 << n):
            subset = [i for i in range(n) if mask >> i & 1]
            d = onion_depth(points, subset)
            full_layers = sum(((mask >> (3 * level)) & 7) == 7
                              for level in range(depth))
            assert d >= full_layers
            total_uniform += d
            weight = Fraction(1, 2 ** len(subset))
            weighted_numerator += d * weight
            weighted_denominator += weight
        uniform_mean = Fraction(total_uniform, 1 << n)
        half_mean = weighted_numerator / weighted_denominator
        assert uniform_mean >= Fraction(depth, 8)
        assert half_mean >= Fraction(depth, 27)
        reports.append({
            "triangle_layers": depth,
            "points": n,
            "uniform_expected_onion_depth": str(uniform_mean),
            "uniform_lower_bound": str(Fraction(depth, 8)),
            "activity_half_boolean_expected_onion_depth": str(half_mean),
            "activity_half_lower_bound": str(Fraction(depth, 27)),
        })
    return reports


def main() -> None:
    result = {
        "description": "exact pocket-restart geometry, decoder, and obstructions",
        "crossing_visible_pockets": check_crossing_visible_pockets(),
        "visible_family_restart": check_visible_restart(),
        "hull_expansion": check_hull_expansion_identity(),
        "nested_onion_depth": check_nested_depth(),
    }
    certificate = HERE / "certificate.json"
    certificate.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
