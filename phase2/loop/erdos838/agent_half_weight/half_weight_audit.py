#!/usr/bin/env python3
"""Exact audits for the half-weight route to Erdos 838.

The script uses the saved integer fixed-x configurations from the independent
half-weight search.  It reconstructs their reflection orders from exact
rational slopes, evaluates the full rank polynomial, and verifies:

* the reported half-weight ratio H=n Z(1/2)/Z(1);
* the n=24 and n=30 counterexamples to mu_(1/2) >= log_2(n)-1;
* the activity-weighted deletion recursion for the n=20 record; and
* the random-prefix (truncated-binomial mixture) identity for every profile.

All partition functions include the empty face.  Floating point is used only
for display and for comparison with log_2(n); all algebraic identities use
Fraction arithmetic.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT838 = HERE.parent
GATE = ROOT838 / "agent_reflection_gate"
DUAL = ROOT838 / "agent_dual_number_amortization"
sys.path.insert(0, str(GATE))

import reflection_order_gate as gate  # noqa: E402


Point = tuple[int, int]


def roots_from_points(points: list[Point]) -> tuple[tuple[int, int], ...]:
    points = sorted(points)
    slopes = sorted(
        (
            Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    for left, right in zip(slopes, slopes[1:]):
        if left[0] == right[0] and set(left[1:]) & set(right[1:]):
            raise AssertionError("collinear triple")
    return tuple((i, j) for _, i, j in slopes)


def profile_from_points(points: list[Point]) -> tuple[int, ...]:
    evaluation = gate.evaluate_roots(
        len(points), roots_from_points(points), graded=True
    )
    nonempty = evaluation.graded
    if nonempty is None:
        raise AssertionError("graded evaluator returned no profile")
    return (1,) + tuple(nonempty[1:])


def profile_stats(profile: tuple[int, ...]) -> dict[str, object]:
    n = profile[1]
    q = Fraction(1, 2)
    z1 = sum(profile)
    zq = sum(Fraction(value, 2**k) for k, value in enumerate(profile))
    mq = sum(Fraction(k * value, 2**k) for k, value in enumerate(profile))
    sq = sum(Fraction(k * k * value, 2**k) for k, value in enumerate(profile))
    muq = mq / zq
    varianceq = sq / zq - muq * muq
    return {
        "n": n,
        "profile": list(profile),
        "Z_1": z1,
        "Z_half": [zq.numerator, zq.denominator],
        "H": [(n * zq / z1).numerator, (n * zq / z1).denominator],
        "H_decimal": float(n * zq / z1),
        "mu_half": [muq.numerator, muq.denominator],
        "mu_half_decimal": float(muq),
        "mu_half_minus_log2_n_plus_1": float(muq) - math.log2(n) + 1,
        "variance_half": [varianceq.numerator, varianceq.denominator],
        "variance_half_decimal": float(varianceq),
    }


def prefix_mixture(profile: tuple[int, ...]) -> dict[str, object]:
    """Verify Z(z)=E sum_(k<=R) binom(n,k) z^k coefficientwise."""
    n = profile[1]
    padded = profile + (0,) * (n + 1 - len(profile))
    tails = [Fraction(padded[k], comb(n, k)) for k in range(n + 1)]
    tails.append(Fraction(0))
    masses = [tails[k] - tails[k + 1] for k in range(n + 1)]
    if any(mass < 0 for mass in masses) or sum(masses) != 1:
        raise AssertionError("normalized face counts are not a survival law")
    rebuilt = [
        comb(n, k) * sum(masses[r] for r in range(k, n + 1))
        for k in range(n + 1)
    ]
    if rebuilt != list(padded):
        raise AssertionError("prefix mixture failed")
    return {
        "tail_probabilities_Pr_R_ge_k": [
            [value.numerator, value.denominator] for value in tails[:-1]
        ],
        "point_masses_Pr_R_eq_r": [
            [value.numerator, value.denominator] for value in masses
        ],
    }


def deletion_recursion(points: list[Point]) -> dict[str, object]:
    n = len(points)
    parent = profile_from_points(points)
    parent_stats = profile_stats(parent)
    z1 = Fraction(parent_stats["Z_1"])
    zq = Fraction(*parent_stats["Z_half"])
    mu1 = Fraction(
        sum(k * value for k, value in enumerate(parent)), sum(parent)
    )
    muq = Fraction(*parent_stats["mu_half"])
    h_parent = Fraction(*parent_stats["H"])

    weighted_numerator = Fraction(0)
    weighted_denominator = Fraction(0)
    child_rows = []
    for omitted in range(n):
        child_profile = profile_from_points(points[:omitted] + points[omitted + 1 :])
        child_stats = profile_stats(child_profile)
        child_v = Fraction(child_stats["Z_1"])
        child_h = Fraction(*child_stats["H"])
        weighted_numerator += child_v * child_h
        weighted_denominator += child_v
        child_rows.append(
            {
                "omitted_original_x": points[omitted][0],
                "H": child_stats["H"],
                "H_decimal": child_stats["H_decimal"],
            }
        )
    lhs = weighted_numerator / weighted_denominator
    rhs = (
        Fraction(n - 1, n)
        * (n - muq)
        / (n - mu1)
        * h_parent
    )
    if lhs != rhs:
        raise AssertionError("half-weight deletion recursion failed")
    # These are the underlying two omitted-point identities.
    if weighted_denominator != (n - mu1) * z1:
        raise AssertionError("lambda=1 deletion mass failed")
    sum_child_half = weighted_numerator / (n - 1)
    if sum_child_half != (n - muq) * zq:
        raise AssertionError("lambda=1/2 deletion mass failed")
    return {
        "weighted_child_H": [lhs.numerator, lhs.denominator],
        "recursion_rhs": [rhs.numerator, rhs.denominator],
        "children": child_rows,
    }


def main() -> None:
    source = json.loads((DUAL / "half_weight_search_records.json").read_text())
    exact = source["exact_records"]
    expected_profiles = {
        20: (1, 20, 190, 1140, 2415, 866, 135, 8),
        24: (1, 24, 276, 2024, 5378, 2679, 413, 43, 3),
        30: (1, 30, 435, 4060, 13975, 10607, 3158, 481, 30),
    }
    rows: dict[str, object] = {}
    points20: list[Point] | None = None
    for n, expected in expected_profiles.items():
        ys = exact[str(n)][f"y_at_x_0_through_{n - 1}"]
        points = list(enumerate(map(int, ys)))
        profile = profile_from_points(points)
        if profile != expected:
            raise AssertionError((n, profile, expected))
        stats = profile_stats(profile)
        stats["prefix_mixture"] = prefix_mixture(profile)
        rows[str(n)] = stats
        if n == 20:
            points20 = points

    # Rigorous counterexamples use the sign of an exact rational minus a
    # transcendental display threshold; the strict numerical margins are
    # over 0.02 and 0.08 respectively, far beyond float uncertainty.
    if not rows["24"]["mu_half_decimal"] < math.log2(24) - 1:
        raise AssertionError("n=24 no longer refutes the activity-half target")
    if not rows["30"]["mu_half_decimal"] < math.log2(30) - 1:
        raise AssertionError("n=30 no longer refutes the activity-half target")
    if points20 is None:
        raise AssertionError("missing n=20 points")

    output = {
        "mode": "exact_half_weight_audit",
        "convention": "empty face included",
        "records": rows,
        "n20_deletion_recursion": deletion_recursion(points20),
    }
    out = HERE / "certificate.json"
    out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {out}")
    for n in (20, 24, 30):
        row = rows[str(n)]
        print(
            n,
            f"H={row['H_decimal']:.12f}",
            f"mu_half-(log2 n-1)={row['mu_half_minus_log2_n_plus_1']:+.12f}",
            f"Var_half={row['variance_half_decimal']:.12f}",
        )


if __name__ == "__main__":
    main()
