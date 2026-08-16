#!/usr/bin/env python3
"""Exact scalar checks for the restriction-peak/curvature attack on Erdős 838.

The script deliberately uses only rank profiles.  It certifies:

* the Bernoulli restriction inequality for the saved n=58 profile on all
  alpha in [0,1], by exact Bernstein subdivision;
* the stronger hypergeometric (fixed-size restriction) hierarchy for n=58;
* an exact interior-alpha failure for a central Pascal cell, despite its
  endpoint curvature inequality;
* global restriction-peak behavior of complete rank truncations, including
  a finite quarter-log example with H of order n^(3/4).

No profile-only assertion is promoted to a planar theorem here.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction as Q
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent

PROFILE_58 = (1, 58, 1653, 30856, 220958, 428915, 284982, 76995, 15100, 2179, 210)
PASCAL_20 = (1, 20, 190, 1140, 3225, 4260, 2116)


def z(profile: tuple[int, ...], t: Q) -> Q:
    return sum((Q(value) * t**rank for rank, value in enumerate(profile)), Q())


def tilted_moment(profile: tuple[int, ...], t: Q) -> Q:
    return sum(
        (Q(rank * value) * t**rank for rank, value in enumerate(profile)), Q()
    )


def mu(profile: tuple[int, ...], t: Q) -> Q:
    return tilted_moment(profile, t) / z(profile, t)


def h_value(profile: tuple[int, ...], n: int) -> Q:
    return Q(n) * z(profile, Q(1, 2)) / z(profile, Q(1))


def bernoulli_gap(profile: tuple[int, ...], n: int, alpha: Q) -> Q:
    """Return h Z(alpha) - E[V(X)H(X)]."""
    h = h_value(profile, n)
    return h * z(profile, alpha) - (
        n * alpha * z(profile, alpha / 2)
        + (1 - alpha) * tilted_moment(profile, alpha / 2)
    )


def bernoulli_gap_power_coefficients(
    profile: tuple[int, ...], n: int
) -> list[Q]:
    """Power coefficients of the Bernoulli gap polynomial."""
    h = h_value(profile, n)
    coefficients = [Q()] * (len(profile) + 1)
    for k in range(len(coefficients)):
        if k < len(profile):
            coefficients[k] += h * profile[k]
        if k >= 1:
            if k - 1 < len(profile):
                coefficients[k] -= Q(n * profile[k - 1], 2 ** (k - 1))
        if 1 <= k < len(profile):
            coefficients[k] -= Q(k * profile[k], 2**k)
        if 2 <= k and k - 1 < len(profile):
            coefficients[k] += Q((k - 1) * profile[k - 1], 2 ** (k - 1))
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return coefficients


def power_to_bernstein(coefficients: list[Q]) -> list[Q]:
    """Convert sum c_i x^i to degree-d Bernstein coefficients on [0,1]."""
    degree = len(coefficients) - 1
    return [
        sum(
            (
                coefficients[i] * Q(comb(k, i), comb(degree, i))
                for i in range(k + 1)
            ),
            Q(),
        )
        for k in range(degree + 1)
    ]


def subdivide_half(bernstein: list[Q]) -> tuple[list[Q], list[Q]]:
    """Exact de Casteljau subdivision at 1/2."""
    rows = [bernstein]
    while len(rows[-1]) > 1:
        old = rows[-1]
        rows.append([(old[i] + old[i + 1]) / 2 for i in range(len(old) - 1)])
    left = [row[0] for row in rows]
    right = [row[-1] for row in reversed(rows)]
    return left, right


def certify_nonnegative_bernstein(
    bernstein: list[Q], max_depth: int = 40
) -> dict[str, int]:
    """Certify nonnegativity by recursively finding nonnegative control nets."""
    stack = [(bernstein, 0)]
    leaves = 0
    deepest = 0
    while stack:
        control, depth = stack.pop()
        deepest = max(deepest, depth)
        if min(control) >= 0:
            leaves += 1
            continue
        if max(control) < 0:
            raise AssertionError("Bernoulli gap is negative on a certified interval")
        if depth >= max_depth:
            raise AssertionError("Bernstein subdivision did not resolve the sign")
        left, right = subdivide_half(control)
        stack.append((right, depth + 1))
        stack.append((left, depth + 1))
    return {"certified_intervals": leaves, "maximum_subdivision_depth": deepest}


def fixed_size_average_h(profile: tuple[int, ...], n: int, m: int) -> Q:
    """V-weighted average H over all m-subsets of an n-element ground set."""
    top = min(m, len(profile) - 1)
    denominator = sum(
        (Q(profile[k] * comb(n - k, m - k)) for k in range(top + 1)), Q()
    )
    numerator = Q(m) * sum(
        (
            Q(profile[k] * comb(n - k, m - k), 2**k)
            for k in range(top + 1)
        ),
        Q(),
    )
    return numerator / denominator


def n58_audit() -> dict[str, object]:
    h = h_value(PROFILE_58, 58)
    assert h == Q(33_994_061, 16_990_512)
    delta = mu(PROFILE_58, Q(1)) - mu(PROFILE_58, Q(1, 2))
    assert delta == Q(4_376_001_835_655, 6_638_810_360_336)
    endpoint_rhs = 1 - mu(PROFILE_58, Q(1, 2)) / 58
    assert delta < endpoint_rhs

    power = bernoulli_gap_power_coefficients(PROFILE_58, 58)
    assert sum(power) == 0  # equality at alpha=1
    for alpha in (Q(), Q(1, 8), Q(1, 2), Q(7, 8), Q(1)):
        evaluated = sum(
            (coefficient * alpha**k for k, coefficient in enumerate(power)), Q()
        )
        assert evaluated == bernoulli_gap(PROFILE_58, 58, alpha)
    sign_certificate = certify_nonnegative_bernstein(power_to_bernstein(power))

    fixed_size = [fixed_size_average_h(PROFILE_58, 58, m) for m in range(1, 59)]
    assert fixed_size[-1] == h
    assert max(fixed_size) == h
    second_value, second_m = max((value, m) for m, value in enumerate(fixed_size, 1) if m < 58)

    # This familiar false strengthening is retained as a hard regression.
    exponential_score = float(h) * math.exp(-float(delta))
    assert exponential_score > 1
    return {
        "H": str(h),
        "mu_one": str(mu(PROFILE_58, Q(1))),
        "mu_half": str(mu(PROFILE_58, Q(1, 2))),
        "delta": str(delta),
        "endpoint_upper_bound": str(endpoint_rhs),
        "endpoint_slack": str(endpoint_rhs - delta),
        "bernoulli_gap_all_alpha": sign_certificate,
        "fixed_size_hierarchy_maximizer_m": 58,
        "fixed_size_second_best_m": second_m,
        "fixed_size_second_best_over_H": str(second_value / h),
        "H_exp_minus_delta": exponential_score,
    }


def pascal_audit() -> dict[str, object]:
    h = h_value(PASCAL_20, 20)
    delta = mu(PASCAL_20, Q(1)) - mu(PASCAL_20, Q(1, 2))
    endpoint_rhs = 1 - mu(PASCAL_20, Q(1, 2)) / 20
    assert delta < endpoint_rhs

    alpha = Q(1, 8)
    gap = bernoulli_gap(PASCAL_20, 20, alpha)
    assert gap == Q(-37_467_223_311, 22_968_008_704) < 0
    weighted_h = h - gap / z(PASCAL_20, alpha)
    assert weighted_h == Q(195_011_719, 161_409_280) > h

    fixed = [fixed_size_average_h(PASCAL_20, 20, m) for m in range(1, 21)]
    fixed_max, fixed_m = max((value, m) for m, value in enumerate(fixed, 1))
    assert fixed_max > h and fixed_m == 4
    return {
        "profile": list(PASCAL_20),
        "H": str(h),
        "delta": str(delta),
        "endpoint_upper_bound": str(endpoint_rhs),
        "interior_witness_alpha": str(alpha),
        "bernoulli_gap_at_witness": str(gap),
        "weighted_restriction_H_at_witness": str(weighted_h),
        "fixed_size_maximizer_m": fixed_m,
        "fixed_size_maximum_H": str(fixed_max),
        "conclusion": "endpoint curvature is necessary but does not certify a global peak",
    }


def truncated_profile(n: int, rank: int) -> tuple[int, ...]:
    return tuple(comb(n, k) for k in range(min(n, rank) + 1))


def truncation_h(n: int, rank: int) -> Q:
    profile = truncated_profile(n, rank)
    return h_value(profile, n)


def truncation_global_peak(n: int, rank: int) -> tuple[int, Q, Q]:
    values = [(truncation_h(m, rank), m) for m in range(1, n + 1)]
    peak_h, peak_m = max(values)
    return peak_m, peak_h, values[-1][0]


def truncation_audit() -> dict[str, object]:
    # The complete 3-skeleton is an exact large-H global restriction peak.
    n3 = 256
    peak_m3, peak_h3, endpoint_h3 = truncation_global_peak(n3, 3)
    assert peak_m3 == n3 and peak_h3 == endpoint_h3
    profile3 = truncated_profile(n3, 3)
    delta3 = mu(profile3, Q(1)) - mu(profile3, Q(1, 2))
    assert peak_h3 > 30 and delta3 < Q(1, 50)

    # At n=2^16 and r=(log_2 n)/4, the exact finite profile already exhibits
    # the asymptotic n^(3/4) scalar obstruction.  Integer/rational arithmetic
    # is cheap here because r=4.
    quarter_n = 1 << 16
    quarter_rank = 4
    peak_m, peak_h, endpoint_h = truncation_global_peak(quarter_n, quarter_rank)
    assert peak_m == quarter_n and peak_h == endpoint_h
    quarter_profile = truncated_profile(quarter_n, quarter_rank)
    quarter_v = sum(quarter_profile)
    quarter_delta = mu(quarter_profile, Q(1)) - mu(quarter_profile, Q(1, 2))
    # Here n^(3/4)=4096 exactly.
    assert peak_h > 1024

    return {
        "complete_three_skeleton": {
            "n": n3,
            "global_peak_m": peak_m3,
            "H": str(peak_h3),
            "H_decimal": float(peak_h3),
            "delta": str(delta3),
            "ACP_scalar": str(peak_h3 * (1 - delta3)),
        },
        "quarter_log_truncation": {
            "n": quarter_n,
            "rank": quarter_rank,
            "global_peak_m": peak_m,
            "V": quarter_v,
            "log2_V_over_log2_n_squared": math.log2(quarter_v)
            / math.log2(quarter_n) ** 2,
            "H": str(peak_h),
            "H_decimal": float(peak_h),
            "log_n_H": math.log(float(peak_h), quarter_n),
            "delta": str(quarter_delta),
        },
    }


def main() -> None:
    certificate = {
        "description": "exact restriction-peak and curvature scalar audit",
        "n58_profile": n58_audit(),
        "central_pascal_twenty_point": pascal_audit(),
        "abstract_complete_rank_truncations": truncation_audit(),
    }
    output = HERE / "certificate.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print("restriction peak curvature audit: PASS")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
