#!/usr/bin/env python3
"""Exact bounded-DP stress test for full exterior-incidence control.

For the central strong-glue Pascal cell at parameter ``m``, this computes
the *actual* ordinary up-degree distribution through the last rank below
``ceil(log2 n)``.  The DP discards no state which can later lead to an
ordinary up-degree at most ``4(r+1)``; see ``central_pascal_updegree_dp``.

The exterior-incidence lower bound is exact and avoids floating-point
entropy inversion.  If ``N`` is the number of low-up-degree rank-r faces,
``K=floor(N^(1/r))``, and ``U`` is their total up-degree, hull activity plus
Euler's numerical constant ``e<3`` gives

    sum e(A) > N*r*(K-3)/3 - U.

All claims recorded under ``exact_coarse_EIC_lower`` are therefore ratios
of explicit integers.  Numerical optimized-entropy values are supplemental.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from central_pascal_updegree_dp import (  # noqa: E402
    Cell,
    entropy_inverse,
    glue_bounded,
    graded_pascal_row,
    log2_int,
)


def integer_nth_root(value: int, degree: int) -> int:
    """Largest integer k with k**degree <= value."""
    if value < 0 or degree <= 0:
        raise ValueError((value, degree))
    if value <= 1:
        return value
    low = 1
    high = 1 << ((value.bit_length() + degree - 1) // degree)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    if not (low**degree <= value < (low + 1) ** degree):
        raise AssertionError("integer root regression")
    return low


def total_faces(parameter: int) -> int:
    _, _, _, profile = graded_pascal_row(parameter, parameter)[parameter // 2]
    return 1 + sum(profile)


def audit(parameter: int, cell: Cell) -> dict[str, object]:
    n = math.comb(parameter, parameter // 2)
    if cell.n != n:
        raise AssertionError((parameter, cell.n, n))
    ell = (n - 1).bit_length()
    rank = ell - 1
    threshold = 4 * (rank + 1)
    near_count = sum(
        count
        for (state_rank, degree), count in cell.faces.items()
        if state_rank == rank and degree <= threshold
    )
    up_sum = sum(
        degree * count
        for (state_rank, degree), count in cell.faces.items()
        if state_rank == rank and degree <= threshold
    )
    if near_count <= 0:
        raise AssertionError((parameter, "empty near family"))
    root = integer_nth_root(near_count, rank)
    # Since near_count >= root**rank and Euler's e<3, hull entropy implies
    # E q > r(root/3-1).  Clear the denominator three.
    lower_numerator = near_count * rank * (root - 3) - 3 * up_sum
    volume = total_faces(parameter)
    lower = Fraction(max(0, lower_numerator), 3 * volume)
    optimized_q = entropy_inverse(rank, log2_int(near_count), n)
    optimized_lower = max(0.0, near_count * optimized_q - up_sum) / volume
    return {
        "parameter": parameter,
        "n": n,
        "ell": ell,
        "rank": rank,
        "up_degree_threshold": threshold,
        "V": str(volume),
        "near_maximal_count": str(near_count),
        "near_density_log2": log2_int(near_count) - log2_int(volume),
        "near_up_degree_sum": str(up_sum),
        "near_mean_up_degree": up_sum / near_count,
        "floor_N_to_1_over_r": root,
        "exact_coarse_EIC_lower": {
            "numerator": str(lower.numerator),
            "denominator": str(lower.denominator),
            "decimal": float(lower),
        },
        "supplemental_optimized_entropy_q": optimized_q,
        "supplemental_optimized_EIC_over_V_lower": optimized_lower,
        "coarse_lower_log_over_log_n": (
            math.log2(float(lower)) / math.log2(n) if lower > 1 else 0.0
        ),
    }


def run(max_parameter: int, parameters: tuple[int, ...], verbose: bool) -> dict:
    max_n = math.comb(max_parameter, max_parameter // 2)
    max_ell = (max_n - 1).bit_length()
    rank_cutoff = max_ell - 1
    degree_cutoff = 4 * max_ell
    singleton = Cell(
        1,
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0): 1}),
    )
    row = [singleton]
    audits = []
    started = time.monotonic()
    requested = set(parameters)
    for level in range(1, max_parameter + 1):
        new = [singleton]
        for index in range(1, level):
            new.append(
                glue_bounded(
                    row[index - 1], row[index], rank_cutoff, degree_cutoff
                )
            )
        new.append(singleton)
        row = new
        if level in requested:
            audited = audit(level, row[level // 2])
            audits.append(audited)
            if verbose:
                print(
                    "m={} n={} exact_lower={:.6g} seconds={:.3f}".format(
                        level,
                        audited["n"],
                        audited["exact_coarse_EIC_lower"]["decimal"],
                        time.monotonic() - started,
                    ),
                    flush=True,
                )

    # Independent coordinate enumerations already banked in the companion
    # verifier give these terminal near counts.  They catch a recurrence or
    # cap/cup-direction convention error before the large integer claims.
    brute_regressions = {4: 15, 5: 120, 6: 3225, 7: 100371}
    small_row = [singleton]
    checked = {}
    for level in range(1, 8):
        new = [singleton]
        for index in range(1, level):
            n = math.comb(level, level // 2) if level >= 4 else 1
            ell = (n - 1).bit_length() if n > 1 else 1
            new.append(glue_bounded(small_row[index - 1], small_row[index], 8, 32))
        new.append(singleton)
        small_row = new
        if level in brute_regressions:
            n = math.comb(level, level // 2)
            rank = (n - 1).bit_length() - 1
            count = sum(
                value
                for (state_rank, degree), value in small_row[level // 2].faces.items()
                if state_rank == rank and degree <= 4 * (rank + 1)
            )
            if count != brute_regressions[level]:
                raise AssertionError((level, count, brute_regressions[level]))
            checked[str(level)] = count

    large = [row for row in audits if row["parameter"] >= 12]
    if any(
        large[index]["exact_coarse_EIC_lower"]["decimal"]
        >= large[index + 1]["exact_coarse_EIC_lower"]["decimal"]
        for index in range(len(large) - 1)
    ):
        raise AssertionError("selected coarse EIC lower bounds are not increasing")
    return {
        "description": "central Pascal actual-up-degree/full-EIC stress test",
        "logical_scope": (
            "finite exact lower bounds; they refute a small constant bound but "
            "do not alone refute an asymptotic n^o(1) bound"
        ),
        "bounded_DP_rank_cutoff": rank_cutoff,
        "bounded_DP_degree_cutoff": degree_cutoff,
        "coordinate_regression_near_counts": checked,
        "audits": audits,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-parameter", type=int, default=40)
    parser.add_argument(
        "--parameters", default="8,12,16,20,24,28,32,36,40"
    )
    parser.add_argument(
        "--output", type=Path, default=HERE / "pascal_eic_scaling_certificate.json"
    )
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    parameters = tuple(int(value) for value in args.parameters.split(",") if value)
    if max(parameters) > args.max_parameter:
        raise ValueError("requested parameter exceeds max parameter")
    result = run(args.max_parameter, parameters, args.verbose)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
