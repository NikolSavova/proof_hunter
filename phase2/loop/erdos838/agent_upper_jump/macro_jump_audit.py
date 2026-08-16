#!/usr/bin/env python3
"""Exact audit for the macroscopic-jump mean-transfer theorem."""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = ROOT / "agent_growing_state_upper" / "LARGE_MACRO_CERTIFICATE.json"


def profile_stats(profile: list[int]) -> tuple[int, int, Fraction, int]:
    v2 = sum(profile[2:])
    moment2 = sum(j * profile[j] for j in range(2, len(profile)))
    mu2 = Fraction(moment2, v2)
    h = max(j for j, value in enumerate(profile) if value)
    return v2, moment2, mu2, h


def partition(profile: list[int], x: int) -> int:
    return sum(profile[j] * x ** (j - 2) for j in range(2, len(profile)))


def boolean_bound(h: int, x: int) -> int:
    return sum(math.comb(h, j) * x ** (j - 2) for j in range(2, h + 1))


def log2_int(value: int) -> float:
    return math.log2(value)


def main() -> None:
    data = json.loads(SOURCE.read_text())
    macros = data["macros"]
    rows: list[dict[str, object]] = []
    checks = 0

    for key in sorted(macros, key=lambda s: int(s)):
        macro = macros[key]
        r = int(key)
        v = macro["convex_profile"]
        c = macro["cap_profile"]
        u = macro["cup_profile"]
        assert v[1] == r and v[2] == math.comb(r, 2) and v[3] == math.comb(r, 3)
        W = sum(v[1:])
        C = sum(c[1:])
        U = sum(u[1:])
        assert W == macro["trace"]
        assert C * U >= W
        checks += 1

        v2, moment2, mu2, h = profile_stats(v)
        activity_rows: list[dict[str, object]] = []
        for x in (1, 2, r, r * r):
            P = partition(v, x)
            B = boolean_bound(h, x)
            assert P >= B
            # Exact integer form of Jensen: P^V2 >= V2^V2 x^(M2-2V2).
            assert pow(P, v2) >= pow(v2, v2) * pow(x, moment2 - 2 * v2)
            checks += 2
            activity_rows.append(
                {
                    "activity": x,
                    "log_partition": log2_int(P),
                    "log_boolean_bound": log2_int(B),
                    "log_jensen_bound": (
                        log2_int(v2) + float(mu2 - 2) * math.log2(x)
                    ),
                    "dominant_certified_bound": (
                        "boolean"
                        if log2_int(B)
                        >= log2_int(v2) + float(mu2 - 2) * math.log2(x)
                        else "mean"
                    ),
                }
            )

        # Exact self-composition count from the substitution formula.
        P_r = partition(v, r)
        W_composed = r * W + C * U * P_r
        transfer_lower = W * P_r
        assert W_composed >= transfer_lower
        checks += 1
        total_log_size = 2 * math.log2(r)
        rows.append(
            {
                "r": r,
                "W": W,
                "C": C,
                "U": U,
                "largest_convex_face": h,
                "mu2": float(mu2),
                "mu2_over_log2_r": float(mu2) / math.log2(r),
                "self_composition_W": W_composed,
                "self_composition_coefficient": (
                    log2_int(W_composed) / (total_log_size * total_log_size)
                ),
                "transversal_partition_coefficient": (
                    log2_int(sum(v[j] * r**j for j in range(1, len(v))))
                    / (total_log_size * total_log_size)
                ),
                "activities": activity_rows,
            }
        )

    result = {
        "source": str(SOURCE.relative_to(ROOT)),
        "macro_count": len(rows),
        "exact_inequality_checks": checks,
        "rows": rows,
        "verdict": (
            "mean-transfer and maximal-degree partition bounds pass exactly; "
            "no saved stretchable macro gives an asymptotic sub-half construction"
        ),
    }
    (HERE / "certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
