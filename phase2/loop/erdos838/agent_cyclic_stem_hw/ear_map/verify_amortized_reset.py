#!/usr/bin/env python3
"""Exact regressions for the amortized cumulative-pocket reduction.

This checks the finite instances only.  The cumulative-envelope theorem and
the coherent rectangle-chain identity in AMORTIZED_RESET.md are symbolic.
"""

from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent
EAR = HERE / "verify_ear_map.py"


def load_ear_module():
    spec = importlib.util.spec_from_file_location("ear_verify", EAR)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cumulative_envelope(profile: list[int]) -> dict[str, object]:
    n = profile[1]
    ell = math.ceil(math.log2(n))
    value = sum(profile)
    prefix = []
    running = 0
    for count in profile:
        running += count
        prefix.append(running)
    terms = [2 ** (ell - k) * prefix[k] for k in range(ell)]
    maximum = max(terms)
    rank = terms.index(maximum)
    return {
        "n": n,
        "ell": ell,
        "profile": profile,
        "prefix": prefix,
        "value": value,
        "maximizing_rank": rank,
        "K_numerator": maximum,
        "K_denominator": value,
        "K_decimal": maximum / value,
        "mean_lower_bound_from_envelope": ell
        - math.ceil(math.log2(max(1, maximum / value)))
        - 1,
    }


def exact_low_addable_slice() -> dict[str, object]:
    ear = load_ear_module()
    ys = (
        -610766,
        -553100,
        -480898,
        -445553,
        -319263,
        -72366,
        270063,
        589685,
        996351,
        -299655,
        2060498,
        -384200,
        4986319,
        -526183,
        -679887,
        -723778,
        -808443,
    )
    points = tuple((i, y) for i, y in enumerate(ys))
    n = len(points)
    assert ear.general_position(points)
    profile = [0] * (n + 1)
    faces_by_rank: list[list[tuple[int, ...]]] = [[] for _ in range(n + 1)]
    for mask in range(1 << n):
        labels = tuple(i for i in range(n) if mask >> i & 1)
        if ear.convex(points, labels):
            profile[len(labels)] += 1
            faces_by_rank[len(labels)].append(labels)
    assert profile == [
        1,
        17,
        136,
        680,
        824,
        645,
        349,
        142,
        33,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    envelope = cumulative_envelope(profile)
    k = int(envelope["maximizing_rank"])
    assert k >= 3
    prefix = list(envelope["prefix"])
    value = int(envelope["value"])
    ell = int(envelope["ell"])
    assert prefix[k - 3] * 8 <= prefix[k]
    assert prefix[k + 1] <= 2 * prefix[k]

    addable_sum = 0
    low_by_rank: dict[int, int] = {}
    strict_low_by_rank: dict[int, int] = {}
    for r in range(k + 1):
        low = 0
        strict_low = 0
        for face in faces_by_rank[r]:
            used = set(face)
            u = sum(
                ear.convex(points, tuple(sorted(face + (p,))))
                for p in range(n)
                if p not in used
            )
            addable_sum += u
            if r >= k - 2 and u <= 24 * (r + 1):
                low += 1
            if r >= k - 2 and u <= 8 * (k + 1):
                strict_low += 1
        if r >= k - 2:
            low_by_rank[r] = low
            strict_low_by_rank[r] = strict_low
    assert addable_sum == sum(s * profile[s] for s in range(1, k + 2))
    assert addable_sum <= 2 * (k + 1) * prefix[k]
    low_total = sum(low_by_rank.values())
    strict_low_total = sum(strict_low_by_rank.values())
    assert strict_low_total * 8 >= 5 * prefix[k]
    assert low_total * 8 >= 5 * prefix[k]
    best_rank = max(low_by_rank, key=low_by_rank.get)
    best_count = low_by_rank[best_rank]
    assert best_count * 24 >= 5 * prefix[k]

    cumulative_num = 2 ** (ell - k) * prefix[k]
    rankwise_num = 2 ** (ell - best_rank) * best_count
    assert 24 * rankwise_num >= 5 * cumulative_num
    return {
        "envelope": envelope,
        "addable_cover_sum_through_k": addable_sum,
        "top_three_low_addable_counts": low_by_rank,
        "top_three_strict_8k_addable_counts": strict_low_by_rank,
        "top_three_strict_8k_addable_total": strict_low_total,
        "top_three_low_addable_total": low_total,
        "selected_rank": best_rank,
        "selected_count": best_count,
        "rankwise_K24_numerator": rankwise_num,
        "rankwise_K24_denominator": value,
        "ratio_KF_to_selected_rankwise": cumulative_num / rankwise_num,
    }


def saved_profile_envelopes() -> dict[str, object]:
    certificate = json.loads(
        (HERE.parent / "fvector_shape_certificate.json").read_text()
    )
    profiles: set[tuple[int, ...]] = set()

    def visit(item) -> None:
        if isinstance(item, dict):
            for value in item.values():
                visit(value)
        elif isinstance(item, list):
            if (
                len(item) >= 4
                and all(isinstance(x, int) for x in item)
                and item[0] == 1
                and item[2] == item[1] * (item[1] - 1) // 2
                and item[3] == item[1] * (item[1] - 1) * (item[1] - 2) // 6
            ):
                profiles.add(tuple(item))
            for value in item:
                visit(value)

    visit(certificate)
    rows = [cumulative_envelope(list(profile)) for profile in profiles]
    rows.sort(key=lambda row: (row["n"], row["K_decimal"]))
    worst = max(rows, key=lambda row: row["K_decimal"])
    return {
        "number_of_profiles": len(rows),
        "maximum_KF": worst,
        "all_KF_at_most_two": all(row["K_decimal"] <= 2 for row in rows),
    }


def product_projection_obstruction() -> dict[str, object]:
    rows = []
    for r in (8, 16, 32, 64):
        m = 2**r
        for s in (1, math.isqrt(r), r // 2):
            fibre = (m - 1) ** s
            rank_credit = 2**s
            rows.append(
                {
                    "r": r,
                    "s": s,
                    "M": m,
                    "projection_fibre": fibre,
                    "allowed_rank_credit": rank_credit,
                    "excess_bits_lower_bound": s * (r - 1) - s,
                }
            )
            assert fibre >= 2 ** (s * (r - 1))
    finite = json.loads(
        (
            HERE.parent.parent
            / "agent_two_ended_hall"
            / "certificate.json"
        ).read_text()
    )["finite_exact_geometry"]
    assert finite["one_target_inverse_fibre"] == 8
    assert finite["one_target_inverse_fibre_formula"] == "(3-1)^3"
    return {
        "scalable_rows": rows,
        "finite_exact_r8_M3": {
            "repair_blocks": finite["simultaneous_repair_blocks"],
            "inverse_fibre": finite["one_target_inverse_fibre"],
            "formula": finite["one_target_inverse_fibre_formula"],
        },
    }


def main() -> None:
    output = {
        "exact_low_addable_slice": exact_low_addable_slice(),
        "saved_profile_envelopes": saved_profile_envelopes(),
        "product_projection_obstruction": product_projection_obstruction(),
    }
    path = HERE / "amortized_reset_certificate.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print("wrote", path)
    row = output["exact_low_addable_slice"]
    print("exact K_F", row["envelope"]["K_decimal"])
    print("selected rank/count", row["selected_rank"], row["selected_count"])
    print("saved profiles", output["saved_profile_envelopes"]["number_of_profiles"])


if __name__ == "__main__":
    main()
