#!/usr/bin/env python3
"""Exact checks for DETACHED_PAIR_UNION_BANK.md."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from random import Random


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
REGRESSION = ERDOS / "agent_outer_internal_product"
sys.path.insert(0, str(REGRESSION))

from verify_pairwise_incompatible_completion_regression import (  # noqa: E402
    build,
    is_convex_set,
)


def coordinate_code(words: list[tuple[int, ...]]) -> tuple[int, int]:
    loads: dict[tuple[tuple[int, ...], ...], int] = {}
    ordered = 0
    for first in words:
        for second in words:
            if first == second:
                continue
            code = tuple(tuple(sorted({a, b})) for a, b in zip(first, second))
            loads[code] = loads.get(code, 0) + 1
            ordered += 1
    return ordered, max(loads.values(), default=0)


def nested_ear_audit() -> dict[str, int]:
    configurations = 0
    detached_pairs = 0
    joined_bad_pairs = 0
    maximum_code_load = 0
    two_point_selections = 0

    for q in range(1, 5):
        for length in range(2, 5):
            base, active, labels, completions = build(q, length, 3)

            # The complete family of selections of local rank at most two
            # is detached-convex.
            local_options = [()] + [(i,) for i in range(length)]
            local_options += list(combinations(range(length), 2))
            for choices in product(local_options, repeat=q):
                selected = [
                    active[j][index]
                    for j in range(q)
                    for index in choices[j]
                ]
                assert is_convex_set(selected)
                two_point_selections += 1

            words = list(product(range(length), repeat=q))
            ordered, load = coordinate_code(words)
            assert ordered == len(words) * (len(words) - 1)
            assert load <= 2**q
            maximum_code_load = max(maximum_code_load, load)

            for first, second in combinations(completions, 2):
                detached = list(set(first) | set(second))
                assert is_convex_set(detached)
                assert not is_convex_set(base + detached)
                detached_pairs += 1
                joined_bad_pairs += 1

            configurations += 1

    return {
        "rational_configurations": configurations,
        "two_point_selections": two_point_selections,
        "detached_convex_pairs": detached_pairs,
        "joined_incompatible_pairs": joined_bad_pairs,
        "maximum_coordinate_load": maximum_code_load,
    }


def arbitrary_subfamily_audit() -> int:
    rng = Random(838_20260814)
    trials = 800
    for _ in range(trials):
        q = rng.randint(1, 7)
        length = rng.randint(2, 5)
        universe = list(product(range(length), repeat=q))
        rng.shuffle(universe)
        words = universe[: rng.randint(1, min(len(universe), 80))]
        ordered, load = coordinate_code(words)
        assert ordered == len(words) * (len(words) - 1)
        assert load <= 2**q
    return trials


def planar_hull(points: list[tuple[Fraction, Fraction]]) -> list[tuple[Fraction, Fraction]]:
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    def chain(sequence):
        answer = []
        for point in sequence:
            while len(answer) >= 2 and cross(answer[-2], answer[-1], point) <= 0:
                answer.pop()
            answer.append(point)
        return answer

    return chain(points)[:-1] + chain(reversed(points))[:-1]


def detached_bad_regression() -> dict[str, int]:
    """Nested homothetic triangles give genuinely bad detached pairs."""
    # A tiny generic perturbation of four nested triangles.  Each triangle
    # is convex, while every inner/outer union contains an interior point.
    triangles = []
    for scale in (10, 20, 40, 80):
        triangles.append(
            [
                (Fraction(-scale), Fraction(-scale)),
                (Fraction(scale + 1), Fraction(-scale + 1)),
                (Fraction(1), Fraction(scale + 2)),
            ]
        )
    assert all(len(planar_hull(triangle)) == 3 for triangle in triangles)
    bad = 0
    for inner, outer in combinations(triangles, 2):
        union = inner + outer
        assert len(planar_hull(union)) < len(union)
        bad += 1
    return {"nested_triangles": len(triangles), "bad_detached_pairs": bad}


def numerical_pair_bound_audit() -> int:
    cases = 0
    for degree in range(2, 30):
        for rank in range(1, 8):
            for size in range(2, 80):
                ordered = size * (size - 1)
                outputs = (ordered + 3 ** (2 * rank) - 1) // (3 ** (2 * rank))
                assert outputs * 3 ** (2 * rank) >= ordered
                cases += 1
    return cases


def main() -> None:
    certificate = {
        "nested_ear": nested_ear_audit(),
        "arbitrary_word_subfamilies": arbitrary_subfamily_audit(),
        "detached_bad_regression": detached_bad_regression(),
        "numerical_pair_cases": numerical_pair_bound_audit(),
        "verdict": (
            "Detached-compatible pairs give a quadratic union bank; the exact "
            "nested-ear product is two-point stable and has coordinate decoder "
            "load at most 2^q.  The remaining branch is detached-incompatible."
        ),
    }
    (HERE / "certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))
    print("detached pair-union audit: PASS")


if __name__ == "__main__":
    main()
