#!/usr/bin/env python3
"""Exact verifier for projective universality of singleton reset chains."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import random

import verify_rooted_hull_kraft_reset as kraft


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def orientation(points: list[Point], a: int, b: int, c: int) -> int:
    value = kraft.cross(points[a], points[b], points[c])
    assert value
    return 1 if value > 0 else -1


def projective_reset_chain(source: list[Point]) -> tuple[list[Point], dict]:
    source = sorted(source)
    assert kraft.general_position(source)
    assert len({point[0] for point in source}) == len(source)
    n = len(source)

    required_slopes = [
        (source[i][1] - source[j][1]) / (source[j][0] - source[i][0])
        for i in range(n)
        for j in range(i + 1, n)
    ]
    shear = max([Fraction(0), *required_slopes]) + 1
    b_coordinates = [y + shear * x for x, y in source]
    assert all(
        b_coordinates[i] < b_coordinates[i + 1]
        for i in range(n - 1)
    )
    translation = max(
        b_coordinates[i] + source[i][0] for i in range(n)
    ) + 1
    a_coordinates = [translation - x for x, _ in source]
    assert all(
        a_coordinates[i] > a_coordinates[i + 1]
        for i in range(n - 1)
    )
    assert all(a > b for a, b in zip(a_coordinates, b_coordinates))

    tips = [
        (a / (a - b), -Fraction(1, a - b))
        for a, b in zip(a_coordinates, b_coordinates)
    ]
    # Move the complete cloud to the left of the first root.
    final_shear = max(a_coordinates) + 1
    tips = [(x + final_shear * y, y) for x, y in tips]
    assert all(x < 0 and y < 0 for x, y in tips)
    assert kraft.general_position(tips)

    return tips, {
        "monotone_shear": str(shear),
        "a_translation": str(translation),
        "final_left_shear": str(final_shear),
    }


def convex_masks(points: list[Point]) -> set[int]:
    result = set()
    for bits in range(1 << len(points)):
        subset = {index for index in range(len(points)) if bits >> index & 1}
        if kraft.convex(points, subset):
            result.add(bits)
    return result


def audit_source(source: list[Point], name: str) -> dict:
    source = sorted(source)
    tips, parameters = projective_reset_chain(source)
    n = len(source)
    roots_and_tips = [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)), *tips]
    assert kraft.general_position(roots_and_tips)

    sign_products = {
        orientation(source, i, j, k) * orientation(tips, i, j, k)
        for i, j, k in combinations(range(n), 3)
    }
    assert len(sign_products) == 1
    source_faces = convex_masks(source)
    tip_faces = convex_masks(tips)
    assert source_faces == tip_faces

    # Full-prefix pocket containment.
    for outer in range(1, n):
        triangle = {0, 1, outer + 2}
        for inner in range(outer):
            assert (
                kraft.hull_vertices(
                    roots_and_tips, triangle | {inner + 2}
                )
                == triangle
            )
            assert not kraft.convex(
                roots_and_tips, triangle | {inner + 2}
            )

    rooted_coefficients = [0] * (n + 1)
    for bits in range(1 << n):
        subset = {index + 2 for index in range(n) if bits >> index & 1}
        if kraft.convex(roots_and_tips, subset | {0, 1}):
            rooted_coefficients[len(subset)] += 1
    assert rooted_coefficients == [1, n] + [0] * (n - 1)

    # Prefix chronology identity.
    prefix_face_sum = 0
    for end in range(n):
        prefix_face_sum += sum(
            1
            for bits in tip_faces
            if bits < (1 << (end + 1))
        )
    chronology_sum = n
    maximum_nonempty_load = 0
    for bits in tip_faces - {0}:
        maximum = bits.bit_length() - 1
        multiplicity = n - maximum
        chronology_sum += multiplicity
        maximum_nonempty_load = max(maximum_nonempty_load, multiplicity)
    assert prefix_face_sum == chronology_sum
    assert maximum_nonempty_load == n

    return {
        "name": name,
        "n": n,
        "projective_parameters": parameters,
        "global_orientation_product": next(iter(sign_products)),
        "convex_subset_count": len(tip_faces),
        "rooted_coefficients": rooted_coefficients,
        "prefix_history_incidences": prefix_face_sum,
        "maximum_nonempty_history_load": maximum_nonempty_load,
    }


def random_points(n: int, seed: int) -> list[Point]:
    rng = random.Random(seed)
    while True:
        points = [
            (Fraction(index), Fraction(rng.randrange(-10_000, 10_001)))
            for index in range(n)
        ]
        if kraft.general_position(points):
            return points


def alternating_points(n: int) -> list[Point]:
    scale = 50
    points = [
        (
            Fraction(index),
            Fraction((-1) ** index * scale ** (n - index)),
        )
        for index in range(n)
    ]
    assert kraft.general_position(points)
    return points


def tangent_coordinates_upper(point: Point) -> tuple[Fraction, Fraction]:
    x, y = point
    assert y > 0
    return -x / y, (1 - x) / y


def tangent_coordinates_lower(point: Point) -> tuple[Fraction, Fraction]:
    x, y = point
    assert y < 0
    return x / (-y), (x - 1) / (-y)


def failure_pattern(values: list[Fraction]) -> list[bool]:
    return [value <= 0 for value in values]


def assert_single_transition(pattern: list[bool]) -> int:
    transitions = sum(pattern[i] != pattern[i - 1] for i in range(1, len(pattern)))
    assert transitions <= 1
    if transitions:
        transition = next(i for i in range(1, len(pattern)) if pattern[i] != pattern[i - 1])
        assert pattern[:transition] == [True] * transition
        assert pattern[transition:] == [False] * (len(pattern) - transition)
    return transitions


def guard_monotonicity_audit(n: int = 9) -> dict:
    lower, _ = projective_reset_chain(random_points(n, 91_001))
    upper_seed, _ = projective_reset_chain(random_points(n, 91_002))
    upper = [(x, -y) for x, y in upper_seed]
    chronology = list(reversed(range(n)))

    def margins(upper_shear: Fraction) -> tuple[list[Fraction], list[Fraction]]:
        shifted_upper = [(x + upper_shear * y, y) for x, y in upper]
        left = []
        right = []
        for index in chronology:
            alpha, beta = tangent_coordinates_upper(shifted_upper[index])
            a_value, b_value = tangent_coordinates_lower(lower[index])
            left.append(a_value - alpha)
            right.append(beta - b_value)
        assert all(left[i] < left[i + 1] for i in range(n - 1))
        assert all(right[i] < right[i + 1] for i in range(n - 1))
        return left, right

    base_left, base_right = margins(Fraction(0))
    left_crossing_shear = -(base_left[0] + base_left[-1]) / 2
    left_values, left_other = margins(left_crossing_shear)
    assert left_values[0] < 0 < left_values[-1]
    left_transitions = assert_single_transition(failure_pattern(left_values))
    assert_single_transition(failure_pattern(left_other))

    right_crossing_shear = (base_right[0] + base_right[-1]) / 2
    right_other, right_values = margins(right_crossing_shear)
    assert right_values[0] < 0 < right_values[-1]
    right_transitions = assert_single_transition(failure_pattern(right_values))
    assert_single_transition(failure_pattern(right_other))

    return {
        "levels": n,
        "left_crossing_shear": str(left_crossing_shear),
        "right_crossing_shear": str(right_crossing_shear),
        "left_guard_transitions": left_transitions,
        "right_guard_transitions": right_transitions,
        "alternation_detected": False,
    }


def main() -> None:
    sources = [
        audit_source(
            sorted(kraft.pascal_cell(5, 2, Fraction(1, 97))),
            "central_pascal_T_5_2",
        ),
        audit_source(random_points(9, 27_182), "random_n9"),
        audit_source(alternating_points(10), "alternating_n10"),
    ]
    guards = guard_monotonicity_audit()
    certificate = {
        "description": "projective universality and chronology of singleton reset chains",
        "arithmetic": "fractions.Fraction for all geometric assertions",
        "source_transfers": sources,
        "guard_monotonicity": guards,
        "assertions": [
            "arbitrary source and discarded tips have identical convex-subset complexes",
            "every earlier prefix is the full hidden pocket of the next singleton tip",
            "rooted polynomial is exactly 1+L*s",
            "every nonempty parent-child coexistence product is empty",
            "prefix-history multiplicity of face S is L-max(S)",
            "both guard margins increase and each failure can heal at most once",
        ],
    }
    output = HERE / "singleton_reset_universality_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"audited {len(sources)} arbitrary-order-type transfers")
    print(
        "largest transferred configuration="
        f"{max(record['n'] for record in sources)}"
    )
    print("guard alternation ruled out on exact synthetic chain")
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
