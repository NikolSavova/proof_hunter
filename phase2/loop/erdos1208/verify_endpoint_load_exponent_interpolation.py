#!/usr/bin/env python3
"""Exact checks for ENDPOINT_LOAD_EXPONENT_INTERPOLATION.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import sys

from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_endpoint_cross_switched_collision_charge import (
    endpoint_decorations,
    endpoint_head_code,
    midpoint,
)
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import subtract


Point = tuple[int, int]


def conditioned_maximum(prime: int) -> tuple[int, int]:
    """Return refined maximum, and maximum after fixing both selected tails."""
    points = transformed_costas(prime)
    differences = difference_set(points)
    decorations = endpoint_decorations(points)

    groups: dict[tuple[Point, Point], list[tuple[Point, ...]]] = defaultdict(list)
    for (u_value, _), q_forms, p_forms in iter_records(differences):
        row = (
            u_value,
            q_forms[0],
            p_forms[0],
            q_forms[1],
            p_forms[1],
            q_forms[2],
            p_forms[2],
        )
        groups[(row[1], row[6])].append(row)

    loads: Counter[tuple[object, ...]] = Counter()
    conditioned: Counter[tuple[object, ...]] = Counter()
    for records in groups.values():
        for first in records:
            first_midpoint = midpoint(decorations[first[0]])
            for second in records:
                midpoint_difference = subtract(
                    first_midpoint,
                    midpoint(decorations[second[3]]),
                )
                head_code = endpoint_head_code(
                    decorations[first[4]],
                    decorations[second[2]],
                )
                if midpoint_difference != (0, 0):
                    key: tuple[object, ...] = (
                        "nonzero",
                        midpoint_difference,
                        head_code,
                    )
                else:
                    if second[3] == first[0]:
                        sign = 1
                    else:
                        assert second[3] == (-first[0][0], -first[0][1])
                        sign = -1
                    key = ("zero", first[0], sign, head_code)

                loads[key] += 1
                conditioned[
                    (
                        key,
                        decorations[first[4]][1],
                        decorations[second[2]][1],
                    )
                ] += 1

    return max(loads.values(), default=0), max(conditioned.values(), default=0)


def main() -> None:
    # If max mu <= N^rho, the ambient n=m^2 exponent is 1/(3-rho/4).
    rho = Fraction(1, 2)
    exponent = 1 / (3 - rho / 4)
    assert exponent == Fraction(8, 23)

    expected = {
        13: (6, 3),
        17: (20, 5),
        19: (22, 8),
    }
    for prime, profile in expected.items():
        actual = conditioned_maximum(prime)
        assert actual == profile, (prime, actual, profile)
        print(f"Costas-{prime}", actual)

    print("rho=1/2 exponent", exponent, float(exponent))
    print("ENDPOINT LOAD EXPONENT INTERPOLATION: PASS")


if __name__ == "__main__":
    sys.path.insert(0, ".")
    main()
