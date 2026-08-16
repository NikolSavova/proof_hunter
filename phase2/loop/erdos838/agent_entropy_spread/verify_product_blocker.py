#!/usr/bin/env python3
"""Exact verifier for the entropy-rich product-blocker obstruction."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point], indices: list[int] | tuple[int, ...]) -> set[int]:
    ordered = sorted(indices, key=lambda i: points[i][0])
    if len(ordered) <= 2:
        return set(ordered)
    lower: list[int] = []
    for i in ordered:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return set(lower[:-1] + upper[:-1])


def build(r: int, m: int) -> tuple[list[Point], list[list[int]], list[int], Fraction, Fraction]:
    """Search dyadic scales for the exact rational construction."""
    last = r - 1
    shear = 2 * r
    macro = [
        (Fraction(i), Fraction(i * (last - i) + shear * i))
        for i in range(r)
    ]
    apex = (Fraction(-1), Fraction(r * r - shear))

    for eps_power in range(5, 30):
        eps = Fraction(1, 2**eps_power)
        points: list[Point] = []
        blocks: list[list[int]] = []
        for block, (x, y) in enumerate(macro):
            ids: list[int] = []
            block_size = 1 if block in (0, last) else m
            for j in range(block_size):
                ids.append(len(points))
                points.append((x + eps * eps * j, y + eps * j * j))
            blocks.append(ids)

        for delta_power in range(eps_power + 3, eps_power + 25):
            delta = Fraction(1, 2**delta_power)
            candidate = list(points)
            cloud: list[int] = []
            for j in range(m):
                cloud.append(len(candidate))
                candidate.append(
                    (apex[0] + delta * delta * j, apex[1] + delta * j * j)
                )
            if any(
                orient(candidate[i], candidate[j], candidate[k]) == 0
                for i, j, k in combinations(range(len(candidate)), 3)
            ):
                continue
            return candidate, blocks, cloud, eps, delta
    raise AssertionError("failed to find dyadic realization")


def finite_geometry_audit(r: int = 6, m: int = 4) -> dict[str, object]:
    points, blocks, cloud, eps, delta = build(r, m)
    endpoints = (blocks[0][0], blocks[-1][0])
    all_indices = set(range(len(points)))
    sources = []
    visible_incidence_count = 0
    hidden_incidence_count = 0
    visible_targets: set[tuple[int, ...]] = set()
    hidden_faces: set[tuple[int, ...]] = set()
    hidden_boolean: set[tuple[int, ...]] = set()
    exterior_counts: list[int] = []
    interior_counts: list[int] = []

    for choices in product(*blocks[1:-1]):
        source = (endpoints[0], *choices, endpoints[1])
        assert hull(points, source) == set(source)
        sources.append(source)
        exterior = interior = addable = 0
        source_set = set(source)

        hidden = tuple(choices)
        hidden_faces.add(hidden)
        for mask in range(1 << len(hidden)):
            hidden_boolean.add(tuple(hidden[j] for j in range(len(hidden)) if mask >> j & 1))

        for p in all_indices - source_set:
            support = list(source) + [p]
            boundary = hull(points, support)
            if len(boundary) == r + 1:
                addable += 1
                continue
            if p in boundary:
                exterior += 1
            else:
                interior += 1

            if p in cloud:
                hidden_incidence_count += 1
                assert boundary == {endpoints[0], p, endpoints[1]}
            else:
                block = next(i for i, ids in enumerate(blocks) if p in ids)
                selected = source[block]
                if p in boundary:
                    visible_incidence_count += 1
                    expected = (source_set - {selected}) | {p}
                    assert boundary == expected
                    visible_targets.add(tuple(sorted(expected)))
                else:
                    assert boundary == source_set

        assert addable == 0
        exterior_counts.append(exterior)
        interior_counts.append(interior)

    source_count = m ** (r - 2)
    assert len(sources) == source_count
    assert len(set(sources)) == source_count
    assert hidden_incidence_count == source_count * m
    assert visible_incidence_count == source_count * (r - 2) * (m - 1) // 2
    # Every word except the unique extreme word in the replacement
    # direction has an incoming exterior coordinate move.
    assert len(visible_targets) == source_count - 1
    assert len(hidden_faces) == source_count
    assert len(hidden_boolean) == (m + 1) ** (r - 2)
    assert sum(exterior_counts) == source_count * (
        m + Fraction((r - 2) * (m - 1), 2)
    )
    assert sum(interior_counts) == source_count * Fraction((r - 2) * (m - 1), 2)

    # The capacity ignored by one-sided half-face routing: two points in
    # each endpoint internal block and one in every block between them.
    two_ended_count = 0
    middle_blocks = blocks[2:-2]
    for left_pair in combinations(blocks[1], 2):
        for right_pair in combinations(blocks[-2], 2):
            for middle in product(*middle_blocks):
                target = (*left_pair, *middle, *right_pair)
                assert hull(points, target) == set(target)
                two_ended_count += 1
    expected_two_ended = math.comb(m, 2) ** 2 * m ** (r - 4)
    assert two_ended_count == expected_two_ended

    # Exact residual spread/codegree census.
    residual_sources = [frozenset(source[1:-1]) for source in sources]
    for k in range(r - 1):
        degrees: dict[frozenset[int], int] = {}
        for source in residual_sources:
            for core in combinations(source, k):
                key = frozenset(core)
                degrees[key] = degrees.get(key, 0) + 1
        assert set(degrees.values()) == {m ** (r - 2 - k)}

    mean_rank = Fraction(1) + Fraction((r - 2) * m, m + 1)
    variance = Fraction(1, 2) + Fraction((r - 2) * m, (m + 1) ** 2)
    return {
        "r": r,
        "M": m,
        "n": len(points),
        "epsilon": str(eps),
        "cloud_delta": str(delta),
        "orientation_determinants_checked": math.comb(len(points), 3),
        "sources": source_count,
        "source_nonmember_incidences_checked": source_count * (len(points) - r),
        "visible_exterior_incidences": visible_incidence_count,
        "hidden_large_incidences": hidden_incidence_count,
        "distinct_visible_full_targets": len(visible_targets),
        "distinct_hidden_faces": len(hidden_faces),
        "distinct_hidden_boolean_targets": len(hidden_boolean),
        "two_ended_microblock_faces": two_ended_count,
        "average_exterior_blockers": str(Fraction(sum(exterior_counts), source_count)),
        "average_interior_blockers": str(Fraction(sum(interior_counts), source_count)),
        "transversal_pool_mean_rank": str(mean_rank),
        "transversal_pool_variance": str(variance),
    }


def log2_binom(n: int, k: int) -> float:
    return sum(math.log2(n - j) - math.log2(j + 1) for j in range(k))


def scalable_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for r in (16, 24, 32, 48, 64):
        m = 2**r
        b = r - 2
        n = (r - 1) * m + 2
        ell = (n - 1).bit_length()
        g = ell - r
        demand = 2**g
        source_log = b * r
        C = 3
        frame_log_lower = source_log - log2_binom(r**C, r)
        k = b // 2
        half_core_log_degree = (b - k) * r
        avg_exterior = Fraction(m) + Fraction(b * (m - 1), 2)
        target_ratio = Fraction((m + 1) ** b, m**b)
        rows.append(
            {
                "r": r,
                "M": m,
                "n": n,
                "ell": ell,
                "g": g,
                "RNP_demand_2_to_g": demand,
                "log2_source_count": source_log,
                "log2_frame_cover_lower_for_F_r_cubed": frame_log_lower,
                "half_core_internal_coordinates": k,
                "log2_half_core_codegree": half_core_log_degree,
                "log2_extension_frame_lower": math.log2((b - k) * m),
                "average_exterior_blockers_log2": math.log2(avg_exterior),
                "hidden_boolean_union_over_sources": float(target_ratio),
                "transversal_pool_mean_rank": float(Fraction(1) + Fraction(b * m, m + 1)),
                "transversal_pool_variance": float(Fraction(1, 2) + Fraction(b * m, (m + 1) ** 2)),
            }
        )
        assert frame_log_lower > 0
        assert avg_exterior >= demand
        assert (b - k) * m > r**C
    return rows


def main() -> None:
    finite = finite_geometry_audit()
    rows = scalable_rows()
    output = {
        "schema": "erdos838-entropy-rich-product-obstruction-v1",
        "finite_exact_geometry": finite,
        "scalable_arithmetic": rows,
        "verdict": (
            "Quadratic frame entropy plus exact residual spread does not close "
            "visible half-face routing or hidden Boolean routing; high half-cores "
            "have exponential extension frames and require pocket recursion."
        ),
    }
    path = HERE / "certificate.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print("entropy-rich product obstruction: PASS")
    print("wrote", path)
    print(
        "finite",
        f"n={finite['n']}",
        f"sources={finite['sources']}",
        f"visible={finite['visible_exterior_incidences']}",
        f"hidden={finite['hidden_large_incidences']}",
    )
    for row in rows:
        print(
            "scale",
            f"r={row['r']}",
            f"g={row['g']}",
            f"log2 frames>={row['log2_frame_cover_lower_for_F_r_cubed']:.2f}",
            f"log2 avg-e={row['average_exterior_blockers_log2']:.2f}",
        )


if __name__ == "__main__":
    main()
