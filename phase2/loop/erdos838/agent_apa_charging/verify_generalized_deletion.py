#!/usr/bin/env python3
"""Exact audit of the surviving generalized deletion envelope.

The coordinates and two independent parent-profile checks live in the
agent_apa_rank certificate.  This script independently replays all deletion
profiles and checks the sharp existential and averaged constants quoted in
REPORT.md.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RANK = ROOT / "agent_apa_rank"
sys.path.insert(0, str(RANK))

import verify_half_weight_counterexample as hw  # noqa: E402
from verify_apa_counterexample import half_value, matrix_profile  # noqa: E402


def main() -> None:
    pts = hw.points()
    profile = hw.EXPECTED_PROFILE
    n = len(pts)
    assert n == 58
    value = sum(profile)
    half = half_value(profile)
    assert Fraction(n) * half / value == Fraction(33_994_061, 16_990_512) > 2

    rows = []
    total_rooted_value = 0
    total_rooted_half = Fraction()
    for label in range(n):
        child = matrix_profile(pts[:label] + pts[label + 1 :])
        rooted_value = value - sum(child)
        rooted_half = half - half_value(child)
        threshold = (half + (n - 1) * rooted_half) / rooted_value
        margin_two = 2 * rooted_value - half - (n - 1) * rooted_half
        assert margin_two < 0
        total_rooted_value += rooted_value
        total_rooted_half += rooted_half
        rows.append(
            {
                "label": label,
                "C_threshold": str(threshold),
                "C_threshold_decimal": float(threshold),
                "constant_two_margin": str(margin_two),
            }
        )

    best = min(
        ((Fraction(row["C_threshold"]), row["label"]) for row in rows),
        key=lambda item: item[0],
    )
    assert best == (Fraction(223_780_817, 111_243_264), 37)

    moment_one = sum(rank * count for rank, count in enumerate(profile))
    moment_half = sum(
        (Fraction(rank * count, 2**rank) for rank, count in enumerate(profile)),
        Fraction(),
    )
    assert total_rooted_value == moment_one
    assert total_rooted_half == moment_half
    average_threshold = (
        n * half + (n - 1) * moment_half
    ) / moment_one
    assert average_threshold == Fraction(5_935_970_545, 2_824_041_984)

    layers = hw.onion_layers(pts)
    assert layers[-1] == [53]
    deepest = rows[53]
    assert deepest["constant_two_margin"] == "-1695735/512"

    result = {
        "description": "exact generalized arbitrary-deletion threshold audit",
        "n": n,
        "H": str(Fraction(n) * half / value),
        "existential_C_threshold": str(best[0]),
        "existential_minimizer_label": best[1],
        "averaged_C_threshold": str(average_threshold),
        "all_constant_two_margins_negative": True,
        "unique_deepest_label": layers[-1][0],
        "unique_deepest_constant_two_margin": deepest["constant_two_margin"],
        "rows": rows,
    }
    certificate = HERE / "certificate.json"
    certificate.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("generalized deletion audit: PASS")
    print(f"H={float(Fraction(n) * half / value):.12f}")
    print(f"C_exist={float(best[0]):.12f} at label {best[1]}")
    print(f"C_average={float(average_threshold):.12f}")


if __name__ == "__main__":
    main()
