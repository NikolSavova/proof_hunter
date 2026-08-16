#!/usr/bin/env python3
"""Exact deletion data for the integrated-activity attack on Erdos 838.

All evaluations of Z, its moments, and deletion distributions are rational.
Floating point is used only to display logarithms and relative entropies.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path[:0] = [str(ROOT / "agent_half_weight"), str(ROOT / "agent_reflection_gate")]

import half_weight_audit as half  # noqa: E402


def frac(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def stats(profile: tuple[int, ...]) -> dict[str, object]:
    z1 = Fraction(sum(profile))
    zh = sum((Fraction(a, 2**k) for k, a in enumerate(profile)), Fraction(0))
    m1 = sum((Fraction(k * a) for k, a in enumerate(profile)), Fraction(0))
    mh = sum((Fraction(k * a, 2**k) for k, a in enumerate(profile)), Fraction(0))
    s1 = sum((Fraction(k * k * a) for k, a in enumerate(profile)), Fraction(0))
    sh = sum((Fraction(k * k * a, 2**k) for k, a in enumerate(profile)), Fraction(0))
    mu1, muh = m1 / z1, mh / zh
    return {
        "profile": list(profile),
        "Z1": z1,
        "Zh": zh,
        "mu1": mu1,
        "muh": muh,
        "var1": s1 / z1 - mu1 * mu1,
        "varh": sh / zh - muh * muh,
    }


def analyze(points: list[tuple[int, int]]) -> dict[str, object]:
    n = len(points)
    parent = stats(half.profile_from_points(points))
    children = [
        stats(half.profile_from_points(points[:p] + points[p + 1 :]))
        for p in range(n)
    ]
    sum1 = sum((c["Z1"] for c in children), Fraction(0))
    sumh = sum((c["Zh"] for c in children), Fraction(0))
    q1 = [c["Z1"] / sum1 for c in children]
    qh = [c["Zh"] / sumh for c in children]

    # Exact omitted-point and differentiated omitted-point identities.
    if sum1 != (n - parent["mu1"]) * parent["Z1"]:
        raise AssertionError("Z1 deletion identity")
    if sumh != (n - parent["muh"]) * parent["Zh"]:
        raise AssertionError("Zh deletion identity")
    mean_child_muh = sum((q * c["muh"] for q, c in zip(qh, children)), Fraction(0))
    if parent["muh"] - mean_child_muh != parent["varh"] / (n - parent["muh"]):
        raise AssertionError("half-activity variance deletion identity")

    # The likelihood-ratio identity is the algebraic content of the
    # KL-corrected recursion; taking qh-expectations of its logarithm gives
    # L=E_qh L_child+r+D(qh||q1).
    ratio_constant = sum1 / sumh
    for x, y, child in zip(qh, q1, children):
        if x / y != child["Zh"] / child["Z1"] * ratio_constant:
            raise AssertionError("deletion likelihood-ratio identity")

    def L(row: dict[str, object]) -> float:
        return math.log(float(row["Z1"] / row["Zh"]))

    lp = L(parent)
    child_l = [L(c) for c in children]
    q1f, qhf = [float(x) for x in q1], [float(x) for x in qh]
    d_h1 = sum(x * math.log(x / y) for x, y in zip(qhf, q1f))
    d_1h = sum(y * math.log(y / x) for x, y in zip(qhf, q1f))
    r = math.log(float((n - parent["muh"]) / (n - parent["mu1"])))
    drift_h = lp - sum(x * y for x, y in zip(qhf, child_l))
    drift_1 = lp - sum(x * y for x, y in zip(q1f, child_l))
    if abs(drift_h - (r + d_h1)) > 2e-13:
        raise AssertionError("forward KL recursion")
    if abs(drift_1 - (r - d_1h)) > 2e-13:
        raise AssertionError("reverse KL recursion")

    log2 = math.log(2.0)
    dh_parent = lp - log2 * float(parent["muh"])
    dr_parent = log2 * float(parent["mu1"]) - lp
    dh_children = [l - log2 * float(c["muh"]) for l, c in zip(child_l, children)]
    dr_children = [log2 * float(c["mu1"]) - l for l, c in zip(child_l, children)]
    gap_parent = parent["mu1"] - parent["muh"]
    gap_children = [c["mu1"] - c["muh"] for c in children]
    gap_drift = gap_parent - sum((q * g for q, g in zip(qh, gap_children)), Fraction(0))
    gap_drift_q1 = gap_parent - sum((q * g for q, g in zip(q1, gap_children)), Fraction(0))
    target = math.log(n / (n - 1))

    def public(row: dict[str, object]) -> dict[str, object]:
        return {
            "profile": row["profile"],
            "Z1": int(row["Z1"]),
            "Zh": frac(row["Zh"]),
            "mu1": frac(row["mu1"]),
            "muh": frac(row["muh"]),
            "var1": frac(row["var1"]),
            "varh": frac(row["varh"]),
        }

    return {
        "n": n,
        "parent": public(parent),
        "children": [
            {
                "deleted_index": p,
                "Z1": int(c["Z1"]),
                "Zh": frac(c["Zh"]),
                "mu1": frac(c["mu1"]),
                "muh": frac(c["muh"]),
                "q1": frac(q1[p]),
                "qh": frac(qh[p]),
            }
            for p, c in enumerate(children)
        ],
        "natural_log_L": lp,
        "deletion_log_ratio_r": r,
        "KL_qh_q1": d_h1,
        "KL_q1_qh": d_1h,
        "L_drift_under_qh": drift_h,
        "L_drift_under_q1": drift_1,
        "target_log_n_over_n_minus_1": target,
        "one_step_shortfall_under_qh": target - drift_h,
        "face_entropy_divergence_Dh": dh_parent,
        "reverse_face_divergence_D1": dr_parent,
        "Dh_drift_under_qh": dh_parent - sum(x * y for x, y in zip(qhf, dh_children)),
        "D1_drift_under_qh": dr_parent - sum(x * y for x, y in zip(qhf, dr_children)),
        "Dh_drift_under_q1": dh_parent - sum(x * y for x, y in zip(q1f, dh_children)),
        "D1_drift_under_q1": dr_parent - sum(x * y for x, y in zip(q1f, dr_children)),
        "activity_gap_mu1_minus_muh": frac(gap_parent),
        "activity_gap_drift_under_qh": frac(gap_drift),
        "activity_gap_drift_under_q1": frac(gap_drift_q1),
    }


def fixed_path_counterexample(
    points: list[tuple[int, int]], deletion_order: tuple[int, ...]
) -> dict[str, object]:
    """Replay a fixed original-label deletion path using exact profiles."""
    remaining = list(range(len(points)))
    last_label = ({*remaining} - set(deletion_order)).pop()
    rows = []
    total = 0.0
    for deleted in deletion_order + (last_label,):
        current_points = [points[i] for i in remaining]
        row = stats(half.profile_from_points(current_points))
        m = len(remaining)
        r = math.log(float((m - row["muh"]) / (m - row["mu1"])))
        total += r
        rows.append(
            {
                "m": m,
                "r": r,
                "Z1": int(row["Z1"]),
                "Zh": frac(row["Zh"]),
                "mu1": frac(row["mu1"]),
                "muh": frac(row["muh"]),
            }
        )
        if deleted not in remaining:
            raise AssertionError("repeated deletion label")
        remaining.remove(deleted)
        if not remaining:
            break
    target = math.log(len(points) / 2)
    if not total < target - 1e-4:
        raise AssertionError("saved path no longer refutes the pointwise target")
    return {
        "n": len(points),
        "deleted_original_labels": list(deletion_order),
        "last_remaining_original_label": last_label,
        "path_sum": total,
        "target_log_n_over_2": target,
        "deficit": total - target,
        "states": rows,
    }


def main() -> None:
    direct = json.loads((ROOT / "agent_lex_minimizer_search" / "direct_hull_certificates.json").read_text())
    records = json.loads((ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text())["exact_records"]
    cases: dict[str, list[tuple[int, int]]] = {
        "n8_exact_minimizer": [tuple(x) for x in direct["8"]["coordinates"]],
        "n9_exact_minimizer": [tuple(x) for x in direct["9"]["coordinates"]],
    }
    for n in (20, 24, 30):
        ys = records[str(n)][f"y_at_x_0_through_{n-1}"]
        cases[f"n{n}_half_weight_record"] = list(enumerate(map(int, ys)))
    output = {
        "mode": "exact_integrated_activity_deletion_audit",
        "convention": "empty convex subset included; h=1/2; natural logarithms",
        "cases": {name: analyze(points) for name, points in cases.items()},
        "pointwise_path_counterexample": fixed_path_counterexample(
            cases["n24_half_weight_record"],
            (4, 12, 16, 1, 14, 9, 18, 2, 10, 11, 15, 5, 22, 13, 19, 17, 20, 3, 6, 7, 0, 8, 21),
        ),
    }
    path = HERE / "certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {path}")
    for name, row in output["cases"].items():
        print(
            name,
            f"drift={row['L_drift_under_qh']:.12f}",
            f"target={row['target_log_n_over_n_minus_1']:.12f}",
            f"KL={row['KL_qh_q1']:.12g}",
            f"gap-drift={float(Fraction(*row['activity_gap_drift_under_qh'])):+.12f}",
        )


if __name__ == "__main__":
    main()
