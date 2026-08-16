#!/usr/bin/env python3
"""Finite arithmetic audit for the polynomial-frame RNP theorem.

The proof in RNP_POLYNOMIAL_FRAME.md is analytic.  This script checks its
explicit Erdos--Szekeres double-count lower bound, the coarse 1/10 exponent,
and the resulting margins for the common chain/apex obstruction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def log2_binom(n: int, k: int) -> float:
    # Summing only k logarithms is stable even when n is exponential in k.
    return sum(math.log2(n - i) - math.log2(i + 1) for i in range(k))


def es_log_lower(m: int) -> tuple[int, int, float]:
    """Return k,N,log2(C(m,k)/C(N,k)), with N=4^k."""
    L = m.bit_length() - 1
    k = L // 4
    if k < 4:
        return k, 4**k, 0.0
    N = 4**k
    assert N <= m
    value = log2_binom(m, k) - log2_binom(N, k)
    return k, N, value


def common_apex_row(r: int, g: int) -> dict[str, float | int]:
    n = 2 ** (r + g)
    frame = 5 * r
    pocket = n - frame
    k, threshold, log_v_lower = es_log_lower(pocket)
    log_sources = log2_binom(frame, r)
    log_rnp_ratio_upper = g + log_sources - log_v_lower
    return {
        "r": r,
        "g": g,
        "n_log2": r + g,
        "frame_size": frame,
        "pocket_size": pocket,
        "ES_face_rank_k": k,
        "ES_subset_threshold": threshold,
        "log2_source_count": log_sources,
        "log2_V_pocket_lower": log_v_lower,
        "log2_2_to_g_sources_over_V_upper": log_rnp_ratio_upper,
    }


def main() -> None:
    # Verify the convenient coarse corollary log_2 V >= L^2/10 whenever
    # L=floor(log_2 m)>=64, using the stronger exact binomial ratio.
    coarse_rows = []
    for L in range(64, 257):
        for offset in (0, 1, (1 << L) - 1):
            m = (1 << L) + offset
            _, _, exact = es_log_lower(m)
            assert exact >= L * L / 10
        if L in (64, 80, 128, 192, 256):
            _, _, exact = es_log_lower(1 << L)
            coarse_rows.append(
                {
                    "floor_log2_m": L,
                    "exact_ES_log2_lower": exact,
                    "coarse_L_squared_over_10": L * L / 10,
                }
            )

    # The common-apex obstruction has a 5r-point frame.  The exact ES lower
    # bound already beats its entire RNP demand for all sampled r>=64 and all
    # sampled deficits; the analytic proof handles every g, not only these.
    apex_rows = []
    for r in (64, 80, 128, 192, 256):
        for g in (1, max(2, r // 4), r, 3 * r):
            row = common_apex_row(r, g)
            assert row["log2_2_to_g_sources_over_V_upper"] < 0
            apex_rows.append(row)

    # Audit the fully explicit coarse exponent used in the proof.  For
    # |R|<=r^C and T frames, log_2 N <= log_2 T +
    # r(log_2 e +(C-1)log_2 r).  These rows show the quadratic pocket term.
    polynomial_rows = []
    for C in (1, 2, 3, 4):
        for r in (128, 256, 512, 1024):
            g = 1
            source_exponent = r * (math.log2(math.e) + (C - 1) * math.log2(r))
            pocket_exponent = (r + g - 2) ** 2 / 10
            polynomial_rows.append(
                {
                    "C": C,
                    "r": r,
                    "source_exponent_without_frame_count": source_exponent,
                    "coarse_pocket_exponent": pocket_exponent,
                    "quadratic_minus_source": pocket_exponent - source_exponent,
                }
            )

    output = {
        "mode": "RNP_polynomial_frame_arithmetic_audit",
        "ES_coarse_bound_rows": coarse_rows,
        "common_apex_rows": apex_rows,
        "polynomial_frame_asymptotic_rows": polynomial_rows,
        "statement": (
            "For fixed C and T=2^o(r^2), sources covered by T frames of "
            "size at most r^C have 2^g N_r/V -> 0 uniformly in g>=1."
        ),
    }
    path = HERE / "rnp_polynomial_frame_certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {path}")
    for row in apex_rows[::4]:
        print(
            "common-apex",
            f"r={row['r']}",
            f"g={row['g']}",
            f"log2-ratio-upper={row['log2_2_to_g_sources_over_V_upper']:.3f}",
        )


if __name__ == "__main__":
    main()
