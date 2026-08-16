#!/usr/bin/env python3
"""Exact audit for SUPPORT_REDUNDANCY_ONE_THREE_FIBRE.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product
import json
from math import factorial, log2
from pathlib import Path
import random


HERE = Path(__file__).resolve().parent


def inherited_conic_geometry_audit() -> dict[str, object]:
    """Reuse the exact rational geometry behind the block restriction."""
    import verify_visible_hidden_interval_kraft_barrier as visible_hidden

    result = visible_hidden.conic_rectangle_audit()
    assert result["all_left_plus_three_lower_arc_sets_are_bad"] is True
    assert result["all_complement_reattachments_fail"] is True
    assert result["literal_depth_zero_tilt"] == "1"
    assert result["visible_layer_size"] == 15
    assert result["hidden_layer_size"] == 15

    # The same rational instance has the symmetric right/upper obstruction
    # used in the four-case record-subface capacity bound.
    upper = tuple(
        visible_hidden.circle(t)
        for t in (Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4))
    )
    epsilon = Q(1, 1_000_000)
    right = tuple(
        (
            Q(2) + i * epsilon,
            Q(7) + 2 * i * i * epsilon**2 + 3 * i * epsilon**3,
        )
        for i in range(1, 4)
    )
    assert all(
        not visible_hidden.convex((endpoint, *triple))
        for endpoint in right
        for triple in combinations(upper, 3)
    )
    return {
        "points": result["points"],
        "fixed_trace": result["fixed_trace"],
        "central_layer_interval_rank": result["interval_rank"],
        "central_layer_records": result["records"],
        "all_left_plus_three_lower_arc_sets_are_bad": True,
        "all_right_plus_three_upper_arc_sets_are_bad": True,
        "literal_depth_zero_tilt": "1",
    }


def role_colouring_audit() -> dict[str, object]:
    """Exhaust a small weighted exact-role colouring identity."""
    r = 3
    vertices = tuple(range(6))
    # Canonically ordered rank-three records, with nonuniform endpoint
    # multiplicities.  The expectation statement is linear in these weights.
    records = {
        (0, 1, 2): 5,
        (0, 3, 5): 2,
        (1, 3, 4): 7,
        (2, 4, 5): 3,
    }
    total = sum(records.values())
    retained_sum = 0
    best = 0
    colourings = 0
    for colours in product(range(r), repeat=len(vertices)):
        retained = sum(
            weight
            for word, weight in records.items()
            if tuple(colours[v] for v in word) == tuple(range(r))
        )
        retained_sum += retained
        best = max(best, retained)
        colourings += 1
    expected = Q(retained_sum, colourings)
    assert expected == Q(total, r**r)
    assert best >= expected

    rainbow_probability = Q(factorial(r), r**r)
    exact_role_probability = Q(1, r**r)
    return {
        "rank": r,
        "record_weight": total,
        "colourings_checked": colourings,
        "exact_role_probability": str(exact_role_probability),
        "rainbow_probability": str(rainbow_probability),
        "expected_retained_weight": str(expected),
        "best_retained_weight": best,
    }


def support_endpoint_inequality_audit() -> dict[str, object]:
    """Check the algebraic endpoint-degree version on integer samples."""
    rng = random.Random(838_815)
    samples = []
    for _ in range(80):
        r = rng.randint(2, 8)
        sizes = [rng.randint(1, 9) for _ in range(r)]
        p0 = 1
        for size in sizes:
            p0 *= size
        m = rng.randint(1, p0)
        delta = rng.randint(1, 30)
        gamma = rng.randint(1, 50)
        record_count = rng.randint(1, gamma * delta * m)
        ambient_bank = rng.randint(1, 10 * p0)
        v_lower = max(m, ambient_bank)
        # f(N) is represented here by ambient_bank.  Equation (3) is an
        # exact algebraic consequence of K <= Gamma Delta M.
        rhs = Q(1, gamma * delta) * max(Q(1), Q(ambient_bank, m))
        assert Q(v_lower, record_count) >= rhs
        samples.append(
            {
                "r": r,
                "P0": p0,
                "M": m,
                "Gamma": gamma,
                "Delta": delta,
                "records": record_count,
                "ambient_bank": ambient_bank,
            }
        )
    return {"random_exact_samples": len(samples), "all_passed": True}


def partial_transversal_audit() -> dict[str, object]:
    samples = []
    for sizes in ((1, 1, 1), (2, 3, 4), (3, 3, 3, 3), (1, 5, 2, 7)):
        raw = 1
        half = Q(1)
        full = 1
        for size in sizes:
            raw *= 1 + size
            half *= 1 + Q(size, 2)
            full *= size

        # Direct enumeration by a coordinate symbol 0=omitted,
        # 1,...,y_i=chosen local label.
        ranks: dict[int, int] = {}
        direct = 0
        for word in product(*(range(size + 1) for size in sizes)):
            rank = sum(value != 0 for value in word)
            direct += 1
            ranks[rank] = ranks.get(rank, 0) + 1
        direct_half = sum(Q(count, 2**rank) for rank, count in ranks.items())
        assert direct == raw
        assert direct_half == half
        assert Q(raw, full) == Q(1) * raw / full
        samples.append(
            {
                "sizes": list(sizes),
                "full_transversals": full,
                "partial_transversals": raw,
                "half_weight": str(half),
                "rank_distribution": {str(k): v for k, v in sorted(ranks.items())},
            }
        )
    return {"samples": samples}


def conic_block_product_audit() -> dict[str, object]:
    """Exact scalable arithmetic for the R=0 conic subproduct."""
    samples: dict[str, object] = {}
    for s in (1, 2, 4, 8, 12, 20):
        variable_roles = 2 * s
        role_size = 3
        fixed_labels = 7
        interval_faces = role_size**variable_roles
        endpoint_pairs = 4**s
        records = interval_faces * endpoint_pairs

        partial_raw = 2**fixed_labels * (1 + role_size) ** variable_roles
        boolean_raw = 2 ** (role_size * variable_roles + fixed_labels)
        assert interval_faces == 9**s
        assert records == 36**s
        assert partial_raw == 128 * 16**s
        assert boolean_raw == 128 * 64**s
        assert boolean_raw >= records

        demand_without_f = Q(records, 2 ** (2 * s + 9))
        assert demand_without_f == Q(9**s, 512)
        partial_half = Q(3, 2) ** fixed_labels * Q(5, 2) ** variable_roles
        boolean_half = Q(3, 2) ** (role_size * variable_roles + fixed_labels)
        boolean_capacity_ratio = boolean_half / demand_without_f
        expected_ratio = Q(512) * Q(3, 2) ** 7 * Q(81, 64) ** s
        assert boolean_capacity_ratio == expected_ratio

        def p2(m: int) -> Q:
            return sum(Q(factorial(m), factorial(i) * factorial(m - i) * 2**i)
                       for i in range(3))

        no_endpoint_capacity = Q(3, 2) ** 7 * Q(5, 2) ** (2 * s)
        left_only_capacity = (
            Q(2**s, 2) * Q(3, 2) ** 2 * Q(5, 2) ** s * p2(3 * s + 5)
        )
        right_only_capacity = (
            Q(2**s, 2) * Q(3, 2) ** 7 * Q(5, 2) ** s * p2(3 * s)
        )
        both_endpoint_capacity = (
            Q(4**s, 4)
            * Q(3, 2) ** 2
            * p2(3 * s + 5)
            * p2(3 * s)
        )
        record_subface_capacity_upper = (
            no_endpoint_capacity
            + left_only_capacity
            + right_only_capacity
            + both_endpoint_capacity
        )
        record_subface_load_lower = (
            demand_without_f / record_subface_capacity_upper
        )
        asymptotic_scale = Q(36, 25) ** s / s**4
        scaled_record_subface_load = record_subface_load_lower / asymptotic_scale
        if s >= 12:
            assert scaled_record_subface_load > Q(1, 10_000_000)

        # A k-block partial transversal extends to 3^(2s-k) W's and each
        # W has 4^s endpoint records.  The empty output has all records.
        overlap_by_occupied_roles = {
            str(k): endpoint_pairs * 3 ** (variable_roles - k)
            for k in range(variable_roles + 1)
        }
        assert overlap_by_occupied_roles["0"] == records

        samples[str(s)] = {
            "R": 0,
            "variable_roles": variable_roles,
            "interval_faces": interval_faces,
            "endpoint_pairs_per_interval": endpoint_pairs,
            "records": records,
            "partial_transversal_faces": partial_raw,
            "boolean_support_faces": boolean_raw,
            "boolean_raw_ratio_to_records": str(Q(boolean_raw, records)),
            "literal_demand_without_1_over_F": str(demand_without_f),
            "partial_half_weight": str(partial_half),
            "boolean_half_weight": str(boolean_half),
            "boolean_capacity_ratio": str(boolean_capacity_ratio),
            "all_record_subfaces_capacity_upper": str(
                record_subface_capacity_upper
            ),
            "all_record_subfaces_load_lower": str(record_subface_load_lower),
            "load_ratio_to_(36/25)^s_over_s^4": str(
                scaled_record_subface_load
            ),
            "empty_output_record_overlap": overlap_by_occupied_roles["0"],
            "full_partial_transversal_record_overlap": overlap_by_occupied_roles[
                str(variable_roles)
            ],
        }

    # The asymptotic bases are the exact factors in (15) and (17).
    return {
        "parameters": "2s variable roles of size 3, seven forced conic labels, |L|=|R|=2^s",
        "raw_gain_base_per_s": "16/9",
        "half_weight_gain_base_per_s": "81/64",
        "record_subface_congestion_base_per_s": "36/25 up to a polynomial factor",
        "samples": samples,
    }


def coefficient_tax_audit() -> dict[str, object]:
    values = []
    for r in (8, 16, 32, 64, 128, 256):
        gamma_log = r + 1 + (r + 1) * log2(r)
        values.append(
            {
                "r": r,
                "log2_Gamma_upper": f"{gamma_log:.12f}",
                "ratio_to_r_squared": f"{gamma_log/(r*r):.12f}",
            }
        )
    assert float(values[-1]["ratio_to_r_squared"]) < float(
        values[0]["ratio_to_r_squared"]
    )
    return {
        "values": values,
        "interpretation": "O(r log r)=o(r^2), but for r=Theta(log n) it is not n^o(1)",
    }


def main() -> None:
    certificate = {
        "description": "support-redundancy split for varying rank-r interval faces with endpoint reuse",
        "role_colouring": role_colouring_audit(),
        "support_endpoint_inequality": support_endpoint_inequality_audit(),
        "partial_transversal_bank": partial_transversal_audit(),
        "inherited_exact_conic_geometry": inherited_conic_geometry_audit(),
        "conic_R_zero_block_product": conic_block_product_audit(),
        "coefficient_role_tax": coefficient_tax_audit(),
        "claims": [
            "exact cyclic role colouring retains a 1/r^r share of arbitrary nonnegative record weight",
            "high support redundancy pays after the explicit Gamma Delta endpoint tax",
            "a homogeneous full-transversal product supplies exact raw and half-weight partial-transversal banks",
            "the fixed rooted 1+3 trace alone does not imply the desired endpoint-partial-transversal product",
            "the R=0 conic restriction has fixed-power record-subface congestion but is globally paid by the Boolean union-support bank",
            "partial outputs can still have exponentially large varying-W and quadratic endpoint overlap",
        ],
    }
    output = HERE / "support_redundancy_one_three_fibre_certificate.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
