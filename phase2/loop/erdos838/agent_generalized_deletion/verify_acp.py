#!/usr/bin/env python3
"""Exact identities and deterministic stress tests for generalized deletion."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RANK = ROOT / "agent_apa_rank"
GRADED = ROOT / "agent_graded_supersat"
sys.path[:0] = [str(RANK), str(GRADED)]

import verify_half_weight_counterexample as hw  # noqa: E402
from graded_balanced import central_template  # noqa: E402
from verify_apa_counterexample import matrix_profile, orient  # noqa: E402


def stats(profile: tuple[int, ...]) -> dict[str, Q]:
    n = profile[1]
    value = Q(sum(profile))
    half = sum((Q(a, 2**k) for k, a in enumerate(profile)), Q())
    moment = sum((Q(k * a) for k, a in enumerate(profile)), Q())
    half_moment = sum((Q(k * a, 2**k) for k, a in enumerate(profile)), Q())
    h_value = n * half / value
    mu_one = moment / value
    mu_half = half_moment / half
    delta = mu_one - mu_half
    acp = h_value * max(Q(), 1 - delta)
    return {
        "V": value,
        "W": half,
        "M": moment,
        "Mh": half_moment,
        "H": h_value,
        "mu_one": mu_one,
        "mu_half": mu_half,
        "delta": delta,
        "ACP": acp,
    }


def exact_record() -> dict[str, object]:
    data = json.loads((HERE / "planar_acp_record.json").read_text())
    points = tuple(
        (Q(x), Q(y)) for x, y in enumerate(data["y_coordinates"])
    )
    determinants = [
        orient(points[i], points[j], points[k])
        for i, j, k in combinations(range(len(points)), 3)
    ]
    assert all(determinants)
    profile = matrix_profile(points)
    row = stats(profile)
    assert Q(88, 100) < row["ACP"] < Q(89, 100) < 1

    # Under q_(1/2), E[2^K]=V/W and the 2^K-size-biased mean is mu_1.
    expectation_two_k = row["V"] / row["W"]
    expectation_k = row["mu_half"]
    expectation_k_two_k = row["mu_one"] * expectation_two_k
    assert row["H"] == len(points) / expectation_two_k
    assert row["delta"] == (
        expectation_k_two_k / expectation_two_k - expectation_k
    )
    assert row["ACP"] == Q(len(points)) * (
        expectation_two_k * (1 + expectation_k) - expectation_k_two_k
    ) / expectation_two_k**2

    # If F(t)=t Z(t/2)/Z(t), then n F'(1) is precisely ACP whenever
    # 1-Delta is positive.
    z_one = row["V"]
    z_half = row["W"]
    f_one = z_half / z_one
    logarithmic_derivative = 1 - row["delta"]
    assert row["ACP"] == len(points) * f_one * logarithmic_derivative
    return {
        "profile": list(profile),
        "minimum_abs_determinant": str(min(map(abs, determinants))),
        **{key: str(value) for key, value in row.items()},
    }


def exact_58() -> dict[str, object]:
    row = stats(hw.EXPECTED_PROFILE)
    assert row["H"] == Q(33_994_061, 16_990_512)
    assert row["delta"] == Q(4_376_001_835_655, 6_638_810_360_336)
    assert row["ACP"] == Q(21_873_815_738_583, 32_075_277_558_016) < 1

    # The tempting exponential strengthening H exp(-Delta)<=1 is false.
    exponential_score = float(row["H"]) * math.exp(-float(row["delta"]))
    assert exponential_score > 1.03
    children = []
    weighted_peak_numerator = Q()
    points = hw.points()
    for deleted in range(58):
        child = stats(matrix_profile(points[:deleted] + points[deleted + 1 :]))
        assert child["H"] < row["H"]
        weighted_peak_numerator += child["V"] * (row["H"] - child["H"])
        children.append(child["H"])
    weighted_peak = weighted_peak_numerator / row["V"]
    record_derivative = (
        1 - row["delta"] - row["mu_half"] / 58
    )
    assert weighted_peak == row["H"] * record_derivative
    assert row["ACP"] == row["Mh"] / row["V"] + weighted_peak
    local_peak = row["H"] - max(children)
    return {
        **{key: str(value) for key, value in row.items()},
        "H_exp_minus_delta": exponential_score,
        "all_58_children_below_parent": True,
        "weighted_local_peak_derivative": str(weighted_peak),
        "largest_child_H": str(max(children)),
        "n_times_parent_minus_largest_child": str(58 * local_peak),
        "Mh_over_V_direct_budget": str(row["Mh"] / row["V"]),
    }


def logsum(terms: list[tuple[float, float]]) -> tuple[float, float]:
    top = max(value for value, _ in terms)
    weights = [math.exp(value - top) for value, _ in terms]
    total = sum(weights)
    return (
        top + math.log(total),
        sum(weight * mean for weight, (_, mean) in zip(weights, terms)) / total,
    )


def polynomial_log_eval(
    profile: list[int], log_argument: float, shift: int
) -> tuple[float, float]:
    return logsum(
        [
            (math.log(value) + (degree - shift) * log_argument, degree - shift)
            for degree, value in enumerate(profile)
            if degree >= shift and value
        ]
    )


def vertical_rows(template, depth: int) -> list[tuple[float, float, float]]:
    """Return (log n, log Z, mu) for a homogeneous directional iterate."""
    r, cap_profile, cup_profile, convex_profile = template

    def at(activity: float) -> list[tuple[float, float, float]]:
        log_n = 0.0
        log_t = math.log(activity)
        cap = (log_t, 1.0)
        cup = cap
        convex = cap
        answer = []
        for _ in range(depth):
            cap_factor = polynomial_log_eval(cap_profile, log_n + log_t, 1)
            cup_factor = polynomial_log_eval(cup_profile, log_n + log_t, 1)
            cross_factor = polynomial_log_eval(convex_profile, log_n + log_t, 2)
            cross = (
                cap[0] + cup[0] + cross_factor[0],
                cap[1] + cup[1] + cross_factor[1],
            )
            cap = (cap[0] + cap_factor[0], cap[1] + cap_factor[1])
            cup = (cup[0] + cup_factor[0], cup[1] + cup_factor[1])
            convex = logsum([(math.log(r) + convex[0], convex[1]), cross])
            log_n += math.log(r)
            partition = logsum([(0.0, 0.0), convex])
            answer.append((log_n, partition[0], partition[1]))
        return answer

    one = at(1.0)
    half = at(0.5)
    rows = []
    for (log_n, log_v, mu_one), (_, log_w, mu_half) in zip(one, half):
        h_value = math.exp(log_n + log_w - log_v)
        delta = mu_one - mu_half
        rows.append((h_value * max(0.0, 1.0 - delta), h_value, delta))
    return rows


def composition_stress() -> dict[str, object]:
    # Central Pascal templates approach the sharp construction regime.  The
    # scan is logarithmic, avoiding overflow even when n is astronomical.
    central_best = (-1.0, None)
    for h in range(3, 31):
        template = central_template(h)
        for depth, row in enumerate(vertical_rows(template, 20), 1):
            if row[0] > central_best[0]:
                central_best = row[0], (h, depth, row)
    assert abs(central_best[0] - 0.75) < 1e-12

    # For the 58-point template, obtain the two directional profiles from the
    # same exact rooted-path evaluator used by its certificate.
    from amplification_probe import cap_cup_profiles  # local heavy import

    caps, cups = cap_cup_profiles(hw.points())
    template_58 = (
        58,
        list(caps),
        list(cups),
        list(hw.EXPECTED_PROFILE),
    )
    rows_58 = vertical_rows(template_58, 8)
    assert abs(rows_58[0][0] - float(stats(hw.EXPECTED_PROFILE)["ACP"])) < 1e-12
    assert all(row[0] == 0.0 for row in rows_58[1:])
    return {
        "central_Pascal_h_3_through_30_depth_20_max": central_best,
        "homogeneous_58_template_rows_ACP_H_Delta": rows_58,
    }


def main() -> None:
    output = {
        "description": "ACP exact identities and composition stress",
        "planar_record": exact_record(),
        "exact_58": exact_58(),
        "composition_stress": composition_stress(),
    }
    (HERE / "certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("generalized deletion ACP audit: PASS")
    print(f"planar record ACP={float(Q(output['planar_record']['ACP'])):.12f}")
    print(f"58-point ACP={float(Q(output['exact_58']['ACP'])):.12f}")
    print(
        "central/composition maximum=",
        output["composition_stress"]["central_Pascal_h_3_through_30_depth_20_max"],
    )


if __name__ == "__main__":
    main()
