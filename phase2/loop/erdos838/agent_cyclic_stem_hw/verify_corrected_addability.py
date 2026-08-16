#!/usr/bin/env python3
"""Exact corrected near-maximal/addability census on key records.

The earlier low_addable_audit used only rooted points lying inside conv(A),
so its alleged up-degree was q=u+e. This verifier uses the actual condition
that A+p itself is convex.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
APA = ROOT / "agent_apa_rank"
GENERAL = ROOT / "agent_generalized_deletion"
GRADED = ROOT / "agent_graded_supersat"
sys.path[:0] = [str(APA), str(GENERAL), str(GRADED)]

from verify_half_weight_counterexample import (  # noqa: E402
    EXPECTED_PROFILE as PROFILE_58,
    points as points_58,
)
from graded_trace import pascal_cell  # noqa: E402
from low_addable_audit import guarded_template, vertical_compose  # noqa: E402
from verify_apa_counterexample import matrix_profile  # noqa: E402
from verify_optimized_hull_activity import ceil_log2_int, circuit_masks  # noqa: E402


def audit(points, profile, old_low_counts=None):
    points = tuple(points)
    profile = list(profile)
    n = len(points)
    ell = ceil_log2_int(n)
    total = sum(profile)
    roots, bad_extensions = circuit_masks(points)
    full_mask = (1 << n) - 1
    rows = []
    near_potential = 0
    for rank in range(ell):
        faces = up_sum = near = exterior_sum = low_q = 0
        for face in itertools.combinations(range(n), rank):
            mask = sum(1 << label for label in face)
            interior = 0
            bad = 0
            for triple in itertools.combinations(face, 3):
                interior |= roots[triple]
                bad |= bad_extensions[triple]
            if interior & mask:
                continue
            faces += 1
            q = n - rank - (interior & ~mask).bit_count()
            up_degree = (full_mask & ~mask & ~bad).bit_count()
            up_sum += up_degree
            if q <= 4 * (rank + 1):
                low_q += 1
            if up_degree <= 4 * (rank + 1):
                near += 1
                exterior_sum += q - up_degree
        if faces != profile[rank]:
            raise AssertionError((rank, faces, profile[rank]))
        if up_sum != (rank + 1) * profile[rank + 1]:
            raise AssertionError('cover identity failed')
        near_potential += (ell - rank) * near
        row = {
            "rank": rank,
            "face_count": faces,
            "actual_low_addable_count": near,
            "low_q_count": low_q,
            "exterior_incidence_sum_on_low_addable_faces": exterior_sum,
            "exterior_incidence_over_V": exterior_sum / total,
            "RNP_term": str(Fraction((1 << (ell - rank)) * near, total)),
            "RNP_term_decimal": (1 << (ell - rank)) * near / total,
        }
        if old_low_counts is not None:
            row["old_reported_low_count"] = old_low_counts[rank]
            if low_q != old_low_counts[rank]:
                raise AssertionError((rank, low_q, old_low_counts[rank]))
        rows.append(row)
    maximum = max(rows, key=lambda row: row["RNP_term_decimal"])
    return {
        "n": n,
        "ell": ell,
        "V": total,
        "ranks_below_ell": rows,
        "corrected_NPM_over_V": str(Fraction(near_potential, total)),
        "corrected_NPM_over_V_decimal": near_potential / total,
        "corrected_RNP_K": maximum["RNP_term"],
        "corrected_RNP_K_decimal": maximum["RNP_term_decimal"],
        "corrected_RNP_maximizing_rank": maximum["rank"],
    }


def n24_record():
    source = json.loads(
        (ROOT / "agent_generalized_deletion" / "planar_rnp_record.json").read_text()
    )
    points = tuple(
        (Fraction(index), Fraction(value))
        for index, value in enumerate(source["y_coordinates"])
    )
    return points, source["search_profile"]


def directional_iterates():
    base = tuple(sorted(pascal_cell(4, 2, Fraction(1, 97))))
    epsilon = Fraction(1, 16384)
    central_square = tuple(
        sorted(
            (
                macro_x + epsilon * epsilon * micro_x,
                macro_y + epsilon * micro_y,
            )
            for macro_x, macro_y in base
            for micro_x, micro_y in base
        )
    )
    guard = guarded_template(3)
    guarded_square = vertical_compose(guard, Fraction(1, 10**8))
    return {
        "central_T42_vertical_square": central_square,
        "guarded_k3_vertical_square": guarded_square,
    }


def main():
    old = json.loads(
        (ROOT / "agent_generalized_deletion" / "low_addable_certificate.json").read_text()
    )["records"]
    points24, profile24 = n24_record()
    records = {
        "n24_RNP_coordinate_record": audit(points24, profile24),
        "n58_half_weight_record": audit(
            points_58(),
            PROFILE_58,
            old["half_weight_counterexample_n58"]["low_addable_counts_below_L"],
        ),
    }
    for name, points in directional_iterates().items():
        records[name] = audit(points, matrix_profile(points))
    output = {
        "mode": "corrected_actual_addability_census",
        "records": records,
        "status": "PASS",
    }
    (HERE / "corrected_addability_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    for name, row in records.items():
        print(
            name,
            "K=",
            f"{row['corrected_RNP_K_decimal']:.9f}",
            "rank=",
            row["corrected_RNP_maximizing_rank"],
            "NPM/V=",
            f"{row['corrected_NPM_over_V_decimal']:.9f}",
        )
    print("PASS corrected addability")


if __name__ == "__main__":
    main()
