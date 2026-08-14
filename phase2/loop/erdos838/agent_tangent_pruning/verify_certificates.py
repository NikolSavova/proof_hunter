#!/usr/bin/env python3
"""Verify the exact certificates in TANGENT_PRUNING_REPORT.md."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT_838 = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT_838 / "agent_cut_reset"))

from attack_search import (  # noqa: E402
    alternating_least_index,
    cut_summary,
    slope_order,
)
from cut_kernel import analyze_points  # noqa: E402


def main() -> None:
    records = []
    for n in range(6, 32, 2):
        m = n // 2
        points = alternating_least_index(n)
        fast = cut_summary(n, slope_order(points), m)

        # Cross-check the independently aggregated calculation against the
        # entrywise two-bridge kernel at sizes where the latter is cheap.
        if n <= 16:
            slow = analyze_points(points, m)
            assert fast["X"] == slow["cross_trace"]
            assert fast["S_L"] == slow["left_kernel_sum"]
            assert fast["S_R"] == slow["right_kernel_sum"]

        plus_between = (m - 2) // 2
        assert fast["S_L"] >= m * m * 2**plus_between
        plus_left = (m + 1) // 2
        minus_left = m // 2
        assert fast["S_R"] >= plus_left * minus_left * 2 ** (m - 2)
        assert fast["X"] <= 2 * n * n * 2**m

        rho = Fraction(int(fast["collision_num"]), int(fast["collision_den"]))
        analytic_upper = Fraction(1024 * m * m, 2 ** (m // 2))
        assert rho <= analytic_upper
        records.append({
            "n": n,
            "m": m,
            "X": fast["X"],
            "S_L": fast["S_L"],
            "S_R": fast["S_R"],
            "collision_ratio": fast["collision_ratio"],
            "analytic_upper": str(analytic_upper),
        })

    # Small exact stretchable counterexample to the lossless version of (T).
    tangent_points = [
        (Fraction(i), Fraction(y))
        for i, y in enumerate([3, 2, 5, 4, 6, 1, 0])
    ]
    tangent = cut_summary(7, slope_order(tangent_points), 3)
    assert tangent["S_R"] == 98
    assert (tangent["C_R"], tangent["U_R"]) == (12, 12)
    assert Fraction(str(tangent["tangent_right_ratio"])) == Fraction(49, 54)

    output = {
        "alternating_least_index": records,
        "lossless_T_counterexample": {
            "points": [[i, y] for i, y in enumerate([3, 2, 5, 4, 6, 1, 0])],
            "summary": tangent,
        },
        "status": "PASS",
    }
    certificate_path = HERE / "verified_certificates.json"
    certificate_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "alternating_sizes": len(records),
        "largest_n": records[-1]["n"],
        "lossless_T_ratio": tangent["tangent_right_ratio"],
        "certificate": str(certificate_path),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
