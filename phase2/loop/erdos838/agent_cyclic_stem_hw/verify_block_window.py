#!/usr/bin/env python3
"""Exact audit of block-doubling and cumulative-window variants for #838.

The finite geometric counterexample is checked with integral predicates and
two independent convex-profile enumerations.  The saved-profile and Pascal
cell stress tests use exact integer/rational arithmetic.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = HERE / "block_window_certificate.json"

sys.path[:0] = [
    str(HERE),
    str(ROOT / "agent_graded_supersat"),
    str(ROOT / "agent_generalized_deletion"),
    str(ROOT / "agent_apa_rank"),
]

from amplification_probe import cap_cup_profiles  # noqa: E402
from graded_balanced import pascal_row, vertical_iterate  # noqa: E402
from verify_apa_counterexample import matrix_profile  # noqa: E402
from verify_fvector_shape import (  # noqa: E402
    circuit_profile,
    direct_profile,
    general_position,
)


BLOCK_KILL_Y = (
    -610766,
    -553100,
    -480898,
    -445553,
    -319263,
    -72366,
    270063,
    589685,
    996351,
    -299655,
    2060498,
    -384200,
    4986319,
    -526183,
    -679887,
    -723778,
    -808443,
)
BLOCK_KILL_PROFILE = (1, 17, 136, 680, 824, 645, 349, 142, 33, 3, 0, 0, 0, 0, 0, 0, 0, 0)


def prefixes(profile: list[int] | tuple[int, ...]) -> list[int]:
    answer = []
    total = 0
    for value in profile:
        total += value
        answer.append(total)
    return answer


def block_failures(
    profile: list[int] | tuple[int, ...], block: int, cumulative: bool
) -> list[dict[str, int]]:
    ell = (profile[1] - 1).bit_length()
    values = prefixes(profile) if cumulative else list(profile)
    failures = []
    for rank in range(max(0, ell - 2 * block + 1)):
        lhs = values[rank + block]
        rhs = 2 * values[rank]
        if lhs < rhs:
            failures.append({"rank": rank, "lhs": lhs, "rhs": rhs})
    return failures


def minimal_block(profile: list[int] | tuple[int, ...], cumulative: bool) -> int:
    ell = (profile[1] - 1).bit_length()
    return next(
        block
        for block in range(1, ell + 1)
        if not block_failures(profile, block, cumulative)
    )


def mean(profile: list[int] | tuple[int, ...]) -> Fraction:
    return Fraction(
        sum(rank * value for rank, value in enumerate(profile)), sum(profile)
    )


def saved_audit() -> dict[str, object]:
    source = json.loads((HERE / "fvector_shape_certificate.json").read_text())
    rows = source["saved_profile_audits"]
    result = []
    for row in rows:
        profile = row["profile"]
        coefficient = minimal_block(profile, False)
        cumulative = minimal_block(profile, True)
        ell = (profile[1] - 1).bit_length()
        mu = mean(profile)
        if mu < ell - 3 * cumulative:
            raise AssertionError(("mean consequence", profile[1]))
        result.append(
            {
                "n": profile[1],
                "coefficient_minimal_block": coefficient,
                "cumulative_minimal_block": cumulative,
                "mean": str(mu),
                "sources": row["sources"],
            }
        )
    return {
        "count": len(result),
        "maximum_coefficient_minimal_block": max(
            row["coefficient_minimal_block"] for row in result
        ),
        "maximum_cumulative_minimal_block": max(
            row["cumulative_minimal_block"] for row in result
        ),
        "rows": result,
    }


def pascal_audit(maximum_parameter: int = 50) -> dict[str, object]:
    count = 0
    maximum_coefficient = 0
    maximum_cumulative = 0
    witnesses: list[dict[str, int]] = []
    for parameter in range(3, maximum_parameter + 1):
        for cell, (n, _caps, _cups, convex) in enumerate(
            pascal_row(parameter, parameter)
        ):
            if n < 4:
                continue
            ell = math.ceil(math.log2(n))
            profile = [1] + convex[1 : ell + 1]
            coefficient = minimal_block(profile, False)
            cumulative = minimal_block(profile, True)
            count += 1
            if coefficient > maximum_coefficient or cumulative > maximum_cumulative:
                witnesses.append(
                    {
                        "parameter": parameter,
                        "cell": cell,
                        "n": n,
                        "ell": ell,
                        "coefficient_minimal_block": coefficient,
                        "cumulative_minimal_block": cumulative,
                    }
                )
            maximum_coefficient = max(maximum_coefficient, coefficient)
            maximum_cumulative = max(maximum_cumulative, cumulative)
    return {
        "maximum_parameter": maximum_parameter,
        "cells": count,
        "maximum_coefficient_minimal_block": maximum_coefficient,
        "maximum_cumulative_minimal_block": maximum_cumulative,
        "record_witnesses": witnesses,
    }


def vertical_kill_audit(maximum_depth: int = 8) -> list[dict[str, int]]:
    points = tuple((index, value) for index, value in enumerate(BLOCK_KILL_Y))
    profile = list(matrix_profile(points))
    caps, cups = cap_cup_profiles(points)
    template = (len(points), list(caps), list(cups), [0] + profile[1:])
    rows = []
    for depth in range(1, maximum_depth + 1):
        ell = math.ceil(depth * math.log2(len(points)))
        n, _caps, _cups, convex = vertical_iterate(template, depth, ell)
        iterate_profile = [1] + convex[1 : ell + 1]
        rows.append(
            {
                "depth": depth,
                "n": n,
                "ell": ell,
                "coefficient_minimal_block": minimal_block(iterate_profile, False),
                "cumulative_minimal_block": minimal_block(iterate_profile, True),
            }
        )
    if rows[0]["cumulative_minimal_block"] != 2:
        raise AssertionError("base cumulative kill disappeared")
    if any(row["cumulative_minimal_block"] != 1 for row in rows[1:]):
        raise AssertionError("vertical stress regression")
    return rows


def dyadic_resonance_audit() -> list[dict[str, object]]:
    """Audit block conclusions from the independently verified profiles."""
    source = json.loads(
        (HERE / "block_search" / "block_resonance_certificate.json").read_text()
    )
    rows = []
    for case in source["cases"]:
        profile = case["profile"]
        coefficient = minimal_block(profile, False)
        cumulative = minimal_block(profile, True)
        if coefficient != 2 or cumulative != 2:
            raise AssertionError((case["name"], coefficient, cumulative))
        rows.append(
            {
                "name": case["name"],
                "n": case["n"],
                "ell": case["ell"],
                "coefficient_minimal_block": coefficient,
                "cumulative_minimal_block": cumulative,
                "cumulative_block_1_failures": block_failures(profile, 1, True),
            }
        )
    return rows


def main() -> None:
    points = tuple((index, value) for index, value in enumerate(BLOCK_KILL_Y))
    if not general_position(points):
        raise AssertionError("block counterexample is not in general position")
    if direct_profile(points) != BLOCK_KILL_PROFILE:
        raise AssertionError("direct block profile mismatch")
    if circuit_profile(points) != BLOCK_KILL_PROFILE:
        raise AssertionError("circuit block profile mismatch")
    coefficient_failures = block_failures(BLOCK_KILL_PROFILE, 1, False)
    cumulative_failures = block_failures(BLOCK_KILL_PROFILE, 1, True)
    if coefficient_failures != [{"rank": 3, "lhs": 824, "rhs": 1360}]:
        raise AssertionError(coefficient_failures)
    if cumulative_failures != [{"rank": 3, "lhs": 1658, "rhs": 1668}]:
        raise AssertionError(cumulative_failures)

    certificate = {
        "description": "exact block-doubling and cumulative-window audit",
        "finite_stretchable_counterexample": {
            "points": [list(point) for point in points],
            "profile": list(BLOCK_KILL_PROFILE),
            "ell": 5,
            "coefficient_block_1_failures": coefficient_failures,
            "cumulative_block_1_failures": cumulative_failures,
            "coefficient_minimal_block": minimal_block(BLOCK_KILL_PROFILE, False),
            "cumulative_minimal_block": minimal_block(BLOCK_KILL_PROFILE, True),
            "mean": str(mean(BLOCK_KILL_PROFILE)),
        },
        "saved_profile_audit": saved_audit(),
        "pascal_cell_audit": pascal_audit(),
        "vertical_iteration_of_counterexample": vertical_kill_audit(),
        "dyadic_resonance_audit": dyadic_resonance_audit(),
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(
        json.dumps(
            {
                "finite_coefficient_failure": coefficient_failures,
                "finite_cumulative_failure": cumulative_failures,
                "saved_profiles": certificate["saved_profile_audit"]["count"],
                "saved_max_cumulative_block": certificate["saved_profile_audit"][
                    "maximum_cumulative_minimal_block"
                ],
                "pascal_cells": certificate["pascal_cell_audit"]["cells"],
                "pascal_max_cumulative_block": certificate["pascal_cell_audit"][
                    "maximum_cumulative_minimal_block"
                ],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
