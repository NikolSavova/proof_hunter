#!/usr/bin/env python3
"""Exact audit of the linear-depth tangent-reset wrapper."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import random

import verify_rooted_hull_kraft_reset as kraft


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def normalize_core(core: list[Point]) -> list[Point]:
    xs = [point[0] for point in core]
    ys = [point[1] for point in core]
    dx = max(xs) - min(xs)
    dy = max(ys) - min(ys)
    assert dx and dy
    return [
        (
            Fraction(99, 200) + Fraction(1, 100) * (x - min(xs)) / dx,
            -Fraction(201, 200) + Fraction(1, 100) * (y - min(ys)) / dy,
        )
        for x, y in core
    ]


def wrapped_core(core: list[Point], levels: int) -> tuple[list[Point], list[int], list[int]]:
    compressed = normalize_core(core)
    points: list[Point] = [
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        *compressed,
    ]
    core_ids = list(range(2, 2 + len(compressed)))
    for level in range(levels):
        points.append(
            (
                Fraction(1, 2) + Fraction(level, 100 * levels),
                -Fraction(2 ** (level + 2)),
            )
        )
    apex_ids = list(range(2 + len(compressed), len(points)))
    # Orientation-preserving shear.  Roots stay fixed and every cloud label
    # moves strictly to the left of the first root.
    points = [(x + y, y) for x, y in points]
    assert kraft.general_position(points)
    assert len({point[0] for point in points}) == len(points)
    assert all(points[index][0] < points[0][0] for index in core_ids + apex_ids)
    return points, core_ids, apex_ids


def rooted_coefficients(
    points: list[Point], u: int, v: int, cloud: list[int]
) -> list[int]:
    coefficients = [0] * (len(cloud) + 1)
    for subset in kraft.masks(cloud):
        if kraft.convex(points, subset | {u, v}):
            coefficients[len(subset)] += 1
    return coefficients


def greedy_reset_chain(
    points: list[Point], u: int, v: int, cloud: list[int]
) -> list[dict]:
    records = []
    current = list(cloud)
    while current:
        _, pockets = kraft.relative_profile(points, u, v, current)
        half_mass = sum(Fraction(1, 2) ** len(hull) for hull in pockets)
        selected = max(
            pockets,
            key=lambda hull: (
                len(pockets[hull]),
                -len(hull),
                tuple(sorted(hull)),
            ),
        )
        child = list(pockets[selected])
        kraft.pocket_monotonicity_audit(points, u, v, pockets)
        records.append(
            {
                "cloud_size": len(current),
                "selected_hull_rank": len(selected),
                "child_size": len(child),
                "codimension": len(current) - len(child),
                "half_rooted_mass": (
                    f"{half_mass.numerator}/{half_mass.denominator}"
                ),
            }
        )
        current = child
    return records


def wrapper_audit(core: list[Point], levels: int, name: str) -> dict:
    points, core_ids, apex_ids = wrapped_core(core, levels)
    u, v = 0, 1
    base_coefficients = rooted_coefficients(points, u, v, core_ids)
    full_coefficients = rooted_coefficients(points, u, v, core_ids + apex_ids)
    expected = base_coefficients + [0] * levels
    expected[1] += levels
    assert full_coefficients == expected

    coexistence_failures_checked = 0
    for offset, apex in enumerate(apex_ids):
        inner = core_ids + apex_ids[:offset]
        triangle = {u, v, apex}
        # Exact strict containment: adding an inner point changes no hull.
        for point in inner:
            assert kraft.hull_vertices(points, triangle | {point}) == triangle
            assert not kraft.convex(points, triangle | {point})
            coexistence_failures_checked += 1

        _, pockets = kraft.relative_profile(points, u, v, inner + [apex])
        singleton = frozenset({apex})
        assert pockets[singleton] == frozenset(inner)

    # The missing cross-level bank is Boolean.
    assert kraft.convex(points, set(apex_ids))
    detached_apex_faces = 1 << levels

    chain = greedy_reset_chain(points, u, v, core_ids + apex_ids)
    assert [row["codimension"] for row in chain[:levels]] == [1] * levels
    assert [row["selected_hull_rank"] for row in chain[:levels]] == [1] * levels
    for step in range(levels):
        initial = Fraction(chain[0]["half_rooted_mass"])
        current = Fraction(chain[step]["half_rooted_mass"])
        assert current == initial - Fraction(step, 2)

    return {
        "name": name,
        "core_size": len(core_ids),
        "wrapper_levels": levels,
        "rooted_base_coefficients": base_coefficients,
        "rooted_full_coefficients": full_coefficients,
        "coexistence_failures_checked": coexistence_failures_checked,
        "detached_apex_faces": detached_apex_faces,
        "reset_chain": chain,
    }


def pascal_and_matching_stress() -> list[dict]:
    pascal = sorted(kraft.pascal_cell(6, 3, Fraction(1, 97)))
    j, ell, _, left, right, degree = kraft.heaviest_trace(pascal)
    pascal_record = {
        "name": "central_pascal_T_6_3",
        "singleton_degree": degree,
        "left_chain": greedy_reset_chain(pascal, j, ell, left),
        "right_chain": greedy_reset_chain(pascal, j, ell, right),
    }
    assert degree == 81

    star = kraft.matching_star_configuration(12, 6, 31_417)
    star_points = [point for _, _, point in star]
    lookup = {
        (block, index): position
        for position, (block, index, _) in enumerate(star)
    }
    u, v = lookup["J", 3], lookup["L", 4]
    star_left = [lookup["X", index] for index in range(1, 13)]
    star_right = [lookup["Y", index] for index in range(1, 13)]
    grid = kraft.hidden_pocket_grid_audit(
        star_points, u, v, star_left, star_right, "matching_star"
    )
    assert grid["singleton_degree"] == 12
    assert grid["deepest_pocket_product"] > 12
    assert not grid["deepest_visible_hulls_compatible"]
    star_record = {
        "name": "perfect_matching_star_m12_q6",
        "grid": grid,
        "left_chain": greedy_reset_chain(star_points, u, v, star_left),
        "right_chain": greedy_reset_chain(star_points, u, v, star_right),
    }
    return [pascal_record, star_record]


def alternating_stress(n: int = 14) -> dict:
    scale = 50
    points = [
        (
            Fraction(index),
            Fraction((-1) ** index * scale ** (n - index)),
        )
        for index in range(n - 2)
    ] + [
        (Fraction(n - 2), Fraction(0)),
        (Fraction(n - 1), Fraction(0)),
    ]
    assert kraft.general_position(points)
    u, v = n - 2, n - 1
    records = []
    for orientation in (-1, 1):
        cloud = [
            index
            for index in range(n - 2)
            if kraft.sign(points[u], points[v], points[index]) == orientation
        ]
        chain = greedy_reset_chain(points, u, v, cloud)
        assert len(chain) == 1
        expected = Fraction(3, 2) ** len(cloud)
        assert Fraction(chain[0]["half_rooted_mass"]) == expected
        assert chain[0]["child_size"] == 0
        records.append(
            {
                "orientation": orientation,
                "cloud_size": len(cloud),
                "half_rooted_mass": chain[0]["half_rooted_mass"],
            }
        )
    return {"name": "alternating_terminal_trace", "sides": records}


def random_core(size: int, seed: int) -> list[Point]:
    rng = random.Random(seed)
    while True:
        points = [
            (Fraction(index), Fraction(rng.randrange(-1000, 1001)))
            for index in range(size)
        ]
        if kraft.general_position(points):
            return points


def main() -> None:
    pascal_core = sorted(kraft.pascal_cell(4, 2, Fraction(1, 97)))
    wrappers = [
        wrapper_audit(pascal_core, 10, "pascal_core_six_plus_ten_ears"),
        wrapper_audit(random_core(6, 16_180), 8, "random_core_six_plus_eight_ears"),
    ]
    stress = pascal_and_matching_stress()
    alternating = alternating_stress()
    certificate = {
        "description": "exact linear-depth tangent reset coexistence barrier",
        "arithmetic": "fractions.Fraction for all geometric and polynomial assertions",
        "arbitrary_core_wrappers": wrappers,
        "pascal_and_matching_stress": stress,
        "alternating_stress": alternating,
        "assertions": [
            "each wrapper ear gives a codimension-one deepest pocket reset",
            "both endpoint tangent coordinates progress strictly at every reset",
            "rooted polynomial equals core polynomial plus L singleton terms",
            "no nonempty child face coexists with its parent wrapper ear",
            "discarded wrapper apices form a Boolean convex-face bank",
            "Pascal, matching-star, and alternating profiles retain their expected branches",
        ],
    }
    output = HERE / "tangent_reset_chain_barrier_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"audited {len(wrappers)} arbitrary-core wrappers")
    print(f"audited {len(stress) + 1} external stress families")
    print(
        "maximum certified linear reset depth="
        f"{max(wrapper['wrapper_levels'] for wrapper in wrappers)}"
    )
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
