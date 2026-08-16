#!/usr/bin/env python3
"""Exact audit for MARKED_SHIELD_EXTERNAL_ALPHABET_GATE.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
import json
from math import comb, floor, log2
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def product_routing_audit() -> dict[str, object]:
    # Three tagged base outputs of different ranks, each saturated at the
    # same normalized load R.  Product decomposition is declared unique;
    # the arithmetic is exactly the proof of Theorem 1.
    base_ranks = (2, 3, 5)
    external_rank = 4
    base_load = Q(7)
    external_weight = Q(3, 2) ** external_rank
    normalized_product_loads = []
    routed_mass = Q(0)
    product_mass = Q(0)
    for rank in base_ranks:
        base_capacity = Q(1, 2**rank)  # common 1/F omitted
        mass = base_load * base_capacity
        routed_mass += mass
        for size in range(external_rank + 1):
            for _ in range(comb(external_rank, size)):
                share = Q(1, 2**size) / external_weight
                output_capacity = Q(1, 2 ** (rank + size))
                output_mass = mass * share
                product_mass += output_mass
                normalized_product_loads.append(output_mass / output_capacity)
    assert product_mass == routed_mass
    assert set(normalized_product_loads) == {base_load / external_weight}
    return {
        "base_load": str(base_load),
        "external_rank": external_rank,
        "external_half_weight": str(external_weight),
        "product_normalized_load": str(base_load / external_weight),
        "distinct_ranked_product_bins_checked": len(normalized_product_loads),
    }


def threshold_audit() -> dict[str, object]:
    alpha = log2(1.5)
    necessary = 1 / alpha
    full_interval_sufficient = 2 / alpha
    additive = 6 + 2 / alpha
    assert 1.7095 < necessary < 1.7096
    assert 3.4190 < full_interval_sufficient < 3.4191
    assert 9.4190 < additive < 9.4191

    # Exact integer-slope sanity: c=s does not beat an n-scale base load,
    # c=2s does; c=3s does not beat n^2, while c=4s does.
    s = 40
    e1 = Q(3, 2) ** s
    e2 = Q(3, 2) ** (2 * s)
    e3 = Q(3, 2) ** (3 * s)
    e4 = Q(3, 2) ** (4 * s)
    assert Q(2**s, s) / e1 > 1
    assert Q(2**s, s) / e2 < 1
    assert Q(4**s, 1) / e3 > 1
    assert Q(4**s, 1) / e4 < 1
    return {
        "alpha_log2_3_over_2": f"{alpha:.12f}",
        "necessary_conic_coefficient": f"{necessary:.12f}",
        "full_interval_product_sufficient_coefficient": f"{full_interval_sufficient:.12f}",
        "additive_alphabet_coefficient": f"{additive:.12f}",
        "integer_slope_checks_at_s": s,
    }


def conic_common_cage_audit() -> dict[str, object]:
    sys.path.insert(0, str(HERE))
    try:
        import verify_visible_hidden_interval_kraft_barrier as visible
    finally:
        sys.path.pop(0)

    a = (Q(-1), Q(0))
    b = (Q(1), Q(0))
    forced = tuple(visible.circle(Q(t)) for t in (-20, -15, -12, -10, -8))
    optional = tuple(visible.circle(Q(t)) for t in (-7, -6, -5, -4, -3, -2))
    upper = tuple(
        visible.circle(t)
        for t in (Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4))
    )
    w = (a, b, *forced, *optional[:2], *upper[:2])
    assert visible.convex(w)

    # A five-point rational conic scaled into the strict interior of the
    # fixed triangle {a,b,forced[0]}.  It is a common marked face, but every
    # nonempty part is hidden by every W containing that triangle.
    center = (
        (a[0] + b[0] + forced[0][0]) / 3,
        (a[1] + b[1] + forced[0][1]) / 3,
    )
    epsilon = Q(1, 10_000)
    parameters = (Q(0), Q(1, 2), Q(1), Q(2), Q(3))
    shield = tuple(
        (
            center[0] + epsilon * visible.circle(t)[0],
            center[1] + epsilon * visible.circle(t)[1],
        )
        for t in parameters
    )
    assert visible.convex(shield)
    assert all(
        visible.cross(*triple) != 0 for triple in combinations(w + shield, 3)
    )
    nonempty_subsets = 0
    for size in range(1, len(shield) + 1):
        for subset in combinations(shield, size):
            assert visible.convex(subset)
            assert not visible.convex(w + subset)
            nonempty_subsets += 1
    assert nonempty_subsets == 2 ** len(shield) - 1
    return {
        "interval_rank": len(w),
        "common_marked_shield_rank": len(shield),
        "mark": [str(coordinate) for coordinate in shield[0]],
        "nonempty_shield_subsets_checked": nonempty_subsets,
        "shield_downset_half_weight": str(Q(3, 2) ** len(shield)),
        "every_nonempty_interval_shield_union_is_bad": True,
    }


def actual_marked_alphabet_audit() -> dict[str, object]:
    common_dir = HERE.parent / "agent_common_shield_mixing"
    sys.path.insert(0, str(common_dir))
    try:
        import verify_marked_nested_shield_carleson as marked

        geometry = marked.check_geometry()
    finally:
        sys.path.pop(0)
    m, d, stars, shield_faces, marked_bins, incidences, total_faces = geometry
    assert geometry == (16, 4, 64, 15, 28, 448, 785)
    return {
        "completions": m,
        "repair_labels": d,
        "ordinary_repair_stars": stars,
        "shield_faces": shield_faces,
        "marked_bins": marked_bins,
        "marked_occurrences": incidences,
        "ambient_faces": total_faces,
        "load_of_every_marked_bin": m,
        "all_nontrivial_star_shield_unions_bad": True,
    }


def rank_extraction_audit() -> dict[str, object]:
    # Exact finite instance of (20): d=2^16, a=1/4, gamma=3/16<a.
    log_d = 16
    d = 2**log_d
    a_num, a_den = 1, 4
    rank_cutoff = 3  # (3/16) log_2 d
    low_rank_subsets = sum(comb(d, i) for i in range(rank_cutoff + 1))
    reservoir_lower_bound = 2 ** ((a_num * log_d * log_d) // a_den)
    assert low_rank_subsets < reservoir_lower_bound
    return {
        "d": d,
        "log2_d": log_d,
        "reservoir_coefficient": "1/4",
        "rank_cutoff": rank_cutoff,
        "low_rank_subset_count": low_rank_subsets,
        "reservoir_lower_bound": reservoir_lower_bound,
        "alpha_over_4_decimal": f"{log2(1.5) / 4:.12f}",
    }


def main() -> None:
    certificate = {
        "description": "conditional external-alphabet multiplication and marked-shield chronology barrier",
        "product_routing": product_routing_audit(),
        "thresholds": threshold_audit(),
        "rank_extraction": rank_extraction_audit(),
        "conic_common_cage": conic_common_cage_audit(),
        "actual_marked_common_alphabet": actual_marked_alphabet_audit(),
        "claims": [
            "a c-label coexisting external alphabet divides normalized load by exactly (3/2)^c before decoder overlap",
            "the sharp conic necessary coefficient is 1/log_2(3/2)",
            "the full-interval product sufficient coefficient is 2/log_2(3/2)",
            "the independent additive-alphabet coefficient is 6+2/log_2(3/2)",
            "the established quarter-coefficient reservoir is below the necessary conic scale",
            "a common marked shield can have a full ordinary downset while every nonempty interval-shield union is nonconvex",
            "the actual repair-star construction retains the marked shield with exact common overlap but no nontrivial coexistence",
        ],
    }
    output = Path(__file__).with_name("marked_shield_external_alphabet_gate_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
