#!/usr/bin/env python3
"""Exact dyadic-boundary block-doubling obstruction certificates.

The two configurations are integral and are built from the saved 58-point
onion record using tiny lexicographic clusters.  All slope comparisons and
all profile coefficients are evaluated with integers.  Only ranks needed for
the block tests are retained.
"""

from __future__ import annotations

import functools
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
APA = ROOT / "agent_apa_rank"
sys.path.insert(0, str(APA))

import verify_half_weight_counterexample as half  # noqa: E402


Point = tuple[int, int]


N65_ADDITIONS: tuple[Point, ...] = (
    (13587261094, -161046672),
    (13587262672, -161046178),
    (13587261667, -161046280),
    (13587261092, -161045986),
    (13587261523, -161046095),
    (13587261403, -161046041),
    (13587261413, -161045617),
)

N65_PROFILE = (1, 65, 2080, 43680, 353852, 863119, 788398)

N129_EXTRA_BLOCKS = frozenset((8, 11, 20, 23, 29, 32, 33, 35, 37, 39, 42, 48, 54))
N129_SIGNS = (
    -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1,
    1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1,
    -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1,
    1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1,
)
N129_PROFILE = (1, 129, 8256, 349504, 5832916, 30290697, 65584381, 72859822)


def n65_points() -> tuple[Point, ...]:
    macro = tuple((round(x * 10**9), round(y)) for x, y in half.points())
    return macro + N65_ADDITIONS


def n129_points() -> tuple[Point, ...]:
    macro = tuple((round(x * 10**6), round(y)) for x, y in sorted(half.points()))
    scale = 10**7
    points = []
    for block, ((x, y), sign) in enumerate(zip(macro, N129_SIGNS)):
        size = 3 if block in N129_EXTRA_BLOCKS else 2
        for micro in range(size):
            points.append(
                (
                    scale * scale * x + micro,
                    scale * scale * y + scale * sign * micro * micro,
                )
            )
    return tuple(points)


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (value > 0) - (value < 0)


def slope_roots(raw_points: tuple[Point, ...]) -> tuple[tuple[int, int], ...]:
    points = tuple(sorted(raw_points))
    slopes = [
        (points[j][1] - points[i][1], points[j][0] - points[i][0], i, j)
        for i in range(len(points))
        for j in range(i + 1, len(points))
    ]

    def compare(left, right) -> int:
        determinant = left[0] * right[1] - right[0] * left[1]
        if determinant:
            return (determinant > 0) - (determinant < 0)
        return ((left[2], left[3]) > (right[2], right[3])) - (
            (left[2], left[3]) < (right[2], right[3])
        )

    slopes.sort(key=functools.cmp_to_key(compare))
    # Parallel disjoint edges are harmless commuting ties.  An equal-slope
    # pair sharing a label is exactly a collinear triple and is forbidden.
    first = 0
    while first < len(slopes):
        last = first + 1
        while (
            last < len(slopes)
            and slopes[first][0] * slopes[last][1]
            == slopes[last][0] * slopes[first][1]
        ):
            last += 1
        labels: set[int] = set()
        for _, _, i, j in slopes[first:last]:
            if i in labels or j in labels:
                raise AssertionError("collinear triple")
            labels.update((i, j))
        first = last
    return tuple((i, j) for _, _, i, j in slopes)


def path_matrix(n: int, roots, cutoff: int):
    matrix = [[[0] * (cutoff + 1) for _ in range(n)] for _ in range(n)]
    for label in range(n):
        matrix[label][label][0] = 1
    for i, j in roots:
        for column in range(n):
            source = matrix[i][column]
            target = matrix[j][column]
            for degree in range(1, cutoff + 1):
                target[degree] += source[degree - 1]
    return matrix


def truncated_profile(points: tuple[Point, ...], cutoff: int) -> tuple[int, ...]:
    roots = slope_roots(points)
    n = len(points)
    cups = path_matrix(n, roots, cutoff)
    caps = path_matrix(n, reversed(roots), cutoff)
    profile = [0] * (cutoff + 1)
    profile[0], profile[1] = 1, n
    for row in range(n):
        for column in range(n):
            for a, cap_count in enumerate(caps[row][column]):
                if not cap_count:
                    continue
                for b, cup_count in enumerate(cups[row][column][: cutoff + 1 - a]):
                    if a + b >= 2:
                        profile[a + b] += cap_count * cup_count
    return tuple(profile)


def chain_profiles(points: tuple[Point, ...], cutoff: int) -> tuple[list[int], list[int]]:
    """Return cap/cup profiles, with degree equal to number of vertices."""
    roots = slope_roots(points)
    n = len(points)
    cups_matrix = path_matrix(n, roots, cutoff - 1)
    caps_matrix = path_matrix(n, reversed(roots), cutoff - 1)

    def collect(matrix) -> list[int]:
        result = [0] * (cutoff + 1)
        result[1] = n
        for row in range(n):
            for column in range(n):
                for edges, count in enumerate(matrix[row][column]):
                    if edges:
                        result[edges + 1] += count
        return result

    return collect(caps_matrix), collect(cups_matrix)


def compose_with_pair(template, cutoff: int):
    """Exact profile recurrence for replacing every macro point by a pair."""
    size, macro_caps, macro_cups, macro_convex = template
    pair = [0] * (cutoff + 1)
    pair[1], pair[2] = 2, 1
    new_caps = [0] * (cutoff + 1)
    new_cups = [0] * (cutoff + 1)
    new_convex = [size * value for value in pair]
    for old_rank in (1, 2):
        for macro_rank in range(1, cutoff - old_rank + 2):
            target = old_rank + macro_rank - 1
            new_caps[target] += (
                pair[old_rank] * macro_caps[macro_rank] * 2 ** (macro_rank - 1)
            )
            new_cups[target] += (
                pair[old_rank] * macro_cups[macro_rank] * 2 ** (macro_rank - 1)
            )
    for cap_rank in (1, 2):
        for cup_rank in (1, 2):
            for macro_rank in range(2, cutoff - cap_rank - cup_rank + 3):
                target = cap_rank + cup_rank + macro_rank - 2
                new_convex[target] += (
                    pair[cap_rank]
                    * pair[cup_rank]
                    * macro_convex[macro_rank]
                    * 2 ** (macro_rank - 2)
                )
    return 2 * size, new_caps, new_cups, new_convex


def pair_tower_audit() -> list[dict[str, object]]:
    """Show that the finite resonance disappears under homogeneous scaling."""
    cutoff = 20
    points = n129_points()
    caps, cups = chain_profiles(points, cutoff)
    convex = list(truncated_profile(points, cutoff))
    convex[0] = 0
    state = (len(points), caps, cups, convex)
    rows = []
    for depth in range(7):
        size, _, _, nonempty = state
        ell = (size - 1).bit_length()
        profile = [1] + nonempty[1:]
        tests = block_rows(tuple(profile), size)
        minimum = next(row["block"] for row in tests if row["passes"])
        rows.append(
            {
                "pair_depth": depth,
                "n": size,
                "ell": ell,
                "profile_through_ell": profile[: ell + 1],
                "minimal_doubling_block": minimum,
                "adjacent_worst_ratio": min(
                    (Fraction(row["lhs"], row["rhs"]) for row in tests[0]["tests"]),
                    default=Fraction(1),
                ).__str__(),
            }
        )
        state = compose_with_pair(state, cutoff)
    if [row["minimal_doubling_block"] for row in rows] != [2, 2, 1, 1, 1, 1, 1]:
        raise AssertionError("unexpected pair-tower block sequence")
    return rows


def block_rows(profile: tuple[int, ...], n: int) -> list[dict[str, object]]:
    ell = (n - 1).bit_length()
    rows = []
    for block in (1, 2):
        tests = []
        for rank in range(ell - 2 * block + 1):
            lhs = profile[rank + block]
            rhs = 2 * profile[rank]
            tests.append(
                {
                    "rank": rank,
                    "lhs": lhs,
                    "rhs": rhs,
                    "ratio": str(Fraction(lhs, rhs)),
                }
            )
        rows.append(
            {
                "block": block,
                "passes": all(row["lhs"] >= row["rhs"] for row in tests),
                "tests": tests,
            }
        )
    return rows


def cumulative_rows(profile: tuple[int, ...], n: int) -> list[dict[str, object]]:
    prefix = list(itertools.accumulate(profile))
    ell = (n - 1).bit_length()
    return [
        {
            "rank": rank,
            "lhs": prefix[rank + 1],
            "rhs": 2 * prefix[rank],
            "ratio": str(Fraction(prefix[rank + 1], 2 * prefix[rank])),
        }
        for rank in range(ell - 1)
    ]


def main() -> None:
    cases = []
    for name, points, expected in (
        ("deep_cluster_n65", n65_points(), N65_PROFILE),
        ("heterogeneous_vertical_n129", n129_points(), N129_PROFILE),
    ):
        if len(points) != expected[1] or len(set(points)) != len(points):
            raise AssertionError("bad point count")
        # The tied-slope audit inside slope_roots distinguishes harmless
        # parallel disjoint edges from forbidden collinear triples.
        actual = truncated_profile(points, len(expected) - 1)
        if actual != expected:
            raise AssertionError((name, actual, expected))
        cases.append(
            {
                "name": name,
                "n": len(points),
                "ell": (len(points) - 1).bit_length(),
                "points": [list(point) for point in points],
                "profile": list(actual),
                "block_tests": block_rows(actual, len(points)),
                "cumulative_adjacent_tests": cumulative_rows(actual, len(points)),
            }
        )
    output = {
        "description": "exact integral dyadic-boundary failures of adjacent block doubling",
        "cases": cases,
        "homogeneous_pair_tower_from_n129": pair_tower_audit(),
    }
    path = HERE / "block_resonance_certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for row in cases:
        last = row["block_tests"][0]["tests"][-1]
        print(row["name"], "profile", row["profile"])
        print("  terminal adjacent ratio-to-doubling", last["ratio"])
    print("block resonance verifier: PASS")


if __name__ == "__main__":
    main()
