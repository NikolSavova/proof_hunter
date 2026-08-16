#!/usr/bin/env python3
"""Exact/numerical audit for BOUNDED_RANK_SKEW_SUNFLOWER_GATE.md."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    lower: list[Point] = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: list[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points: list[Point]) -> bool:
    return len(hull(points)) == len(points)


def strictly_inside_triangle(p: Point, a: Point, b: Point, c: Point) -> bool:
    signs = [orient(a, b, p), orient(b, c, p), orient(c, a, p)]
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def frac_pair(p: Point) -> list[str]:
    return [str(p[0]), str(p[1])]


def skew_audit(max_p: int = 8) -> dict:
    checked_pairs = 0
    worst_ratio = float("inf")
    bin_counts: dict[int, int] = {}
    for p in range(1, max_p + 1):
        w = 2**p - 1
        profiles: list[tuple[int, int, float]] = []
        for cap in range(p, w + 1):
            for cup in range(p, w + 1):
                if cap * cup >= w:
                    sigma = 0.5 * math.log2(cup / cap)
                    assert abs(sigma) <= (p - math.log2(p)) / 2 + 1e-12
                    profiles.append((cap, cup, sigma))
        bins: dict[int, list[tuple[int, int, float]]] = {}
        for profile in profiles:
            bins.setdefault(math.floor(profile[2]), []).append(profile)
        # The occupied unit bins are at most p+1, as used in Lemma 1.
        assert len(bins) <= p + 1
        bin_counts[p] = len(bins)
        for members in bins.values():
            min_sigma = min(item[2] for item in members)
            max_sigma = max(item[2] for item in members)
            assert min_sigma - max_sigma > -1 - 1e-12
            # The two choices are independent, so the smallest endpoint
            # product in the bin is the product of the two marginal minima.
            min_cap = min(item[0] for item in members)
            min_cup = min(item[1] for item in members)
            ratio = (min_cap * min_cup) / (w / 2)
            assert ratio >= 1 - 1e-12
            worst_ratio = min(worst_ratio, ratio)
            checked_pairs += len(members) ** 2
    return {
        "max_p": max_p,
        "checked_profile_pairs": checked_pairs,
        "occupied_unit_bins": bin_counts,
        "minimum_ratio_to_W_over_2": worst_ratio,
    }


def asymptotic_audit() -> dict:
    # Check the leading exponent in the leftover bound from Lemma 2.
    a = 0.18
    kappa = 0.50
    rho = 0.25  # kappa*rho=0.125<a
    c = 3.0
    rows = []
    for log_d in (32, 64, 128, 256):
        q = max(2, int(kappa * log_d))
        log_h = rho * log_d
        log_leftover = (
            math.log2(q + 1)
            + math.log2(2 ** min(c * log_d, 1023) + 1)
            + math.lgamma(q + 1) / math.log(2)
            + q * log_h
        )
        # Avoid overflow in the Delta term: log2(D^c+1)=cL+o(1).
        if c * log_d > 1023:
            log_leftover = (
                math.log2(q + 1)
                + c * log_d
                + math.lgamma(q + 1) / math.log(2)
                + q * log_h
            )
        log_mass = a * log_d * log_d
        rows.append(
            {
                "log_D": log_d,
                "q": q,
                "log2_leftover_bound": log_leftover,
                "log2_mass": log_mass,
                "normalized_leftover_exponent": log_leftover / (log_d**2),
            }
        )
    assert rows[-1]["normalized_leftover_exponent"] < a

    # A finite check of Theorem 3's arithmetic.
    q = 12
    h = 4096
    groups = 100
    multiplicity = 64
    p = 4
    retained = h // (p + 1)
    exact_representation_lower = groups * math.comb(retained, 2) * (2**p - 1) / 2
    theorem_lower = groups * h * h / (8 * (q + 1) ** 2)
    assert exact_representation_lower >= theorem_lower
    union_lower = theorem_lower / multiplicity
    covered_mass = groups * h
    theorem_formula = covered_mass * h / (8 * (q + 1) ** 2 * multiplicity)
    assert abs(union_lower - theorem_formula) < 1e-9

    # Weighted Theorem 3W.  All completions lie in one dyadic band and all
    # extensions are good, so the weighted-good alternative applies.
    weighted_h = 64
    weighted_p = 3
    weighted_q = 12
    band_floor = 100
    weights = [band_floor + (17 * i) % band_floor for i in range(weighted_h)]
    assert all(band_floor <= value < 2 * band_floor for value in weights)
    weighted_total = sum(weights)
    possible_degree = (weighted_h - 1) * weighted_p
    weighted_representations = weighted_total * possible_degree
    weighted_bank_lower = weighted_total * possible_degree / (
        8 * band_floor * (weighted_q + 1)
    )
    # Directly applying the per-face weighted multiplicity 2w(q+1) is
    # stronger by a factor four because here all groups, not half, are good.
    direct_weighted_decoder_lower = weighted_representations / (
        2 * band_floor * (weighted_q + 1)
    )
    assert direct_weighted_decoder_lower >= weighted_bank_lower
    tagged_multiplicity = 7
    tagged_bank_lower = weighted_total * possible_degree / (4 * tagged_multiplicity)
    return {
        "parameters": {"a": a, "kappa": kappa, "rho": rho, "compatibility_power": c},
        "leftover_rows": rows,
        "bank_arithmetic": {
            "q": q,
            "h": h,
            "petal_rank": p,
            "groups": groups,
            "multiplicity": multiplicity,
            "retained_per_group": retained,
            "exact_representation_lower": exact_representation_lower,
            "theorem_representation_lower": theorem_lower,
            "theorem_union_lower": union_lower,
        },
        "weighted_interface": {
            "h": weighted_h,
            "petal_rank": weighted_p,
            "q": weighted_q,
            "dyadic_band_floor": band_floor,
            "total_weight": weighted_total,
            "possible_extension_degree": possible_degree,
            "weighted_representation_mass": weighted_representations,
            "theorem_3W_untagged_lower": weighted_bank_lower,
            "direct_all_good_decoder_lower": direct_weighted_decoder_lower,
            "tagged_decoder_multiplicity": tagged_multiplicity,
            "tagged_lower": tagged_bank_lower,
        },
    }


def geometry_audit() -> dict:
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    outer = [
        (Fraction(t, 4), Fraction(1) - Fraction(t * t, 16))
        for t in range(-3, 4)
    ]

    # The inverse tangent-coordinate map from the fixed edge uv.  Both
    # tangent coordinates increase with i, so z_j is inside triangle uvz_i
    # whenever i<j.  The mild asymmetry avoids collinearities.
    nested: list[Point] = []
    for i in range(6):
        left = Fraction(3 + i)
        right = Fraction(4 + i + i * i, 2)
        nested.append(
            ((left - right) / (left + right), Fraction(-2) / (left + right))
        )

    all_points = [u, *outer, v, *nested]
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))
    shield = [u, *outer, v]
    assert convex(shield)
    assert all(
        strictly_inside_triangle(nested[j], u, v, nested[i])
        for i, j in combinations(range(len(nested)), 2)
    )

    # Outer three are blockers, inner three are ears.
    blockers = nested[:3]
    ears = nested[3:]
    core_subsets = list(combinations(outer, 3))
    records = []
    sources = set()
    targets = set()
    pairs = set()
    core_ids = {}
    for core_id, subset in enumerate(core_subsets):
        core = (u, v, *subset)
        core_ids[frozenset(core)] = core_id
        for x in ears:
            assert convex([*core, x])
            for p in blockers:
                assert convex([*core, p])
                assert strictly_inside_triangle(x, u, v, p)
                repaired = [*core, p]
                assert convex(repaired)
                assert len(hull([*core, x, p])) == len(repaired)
                records.append((frozenset(core), x, p))
                sources.add((frozenset(core), x))
                targets.add((frozenset(core), p))
                pairs.add((x, p))

        # Same-side pairs are also nested and hence incompatible over core.
        for a, b in combinations(ears, 2):
            assert not convex([*core, a, b])
        for a, b in combinations(blockers, 2):
            assert not convex([*core, a, b])

    expected_cores = math.comb(len(outer), 3)
    assert expected_cores == len(core_subsets) == 35
    assert len(records) == expected_cores * len(ears) * len(blockers)
    assert len(sources) == expected_cores * len(ears)
    assert len(targets) == expected_cores * len(blockers)
    assert len(pairs) == len(ears) * len(blockers)

    source_degree = len(blockers)
    target_degree = len(ears)
    pair_degree = expected_cores
    assert len(records) // len(sources) == source_degree
    assert len(records) // len(targets) == target_degree
    assert len(records) // len(pairs) == pair_degree

    # Every untagged two-petal face is shared by every core history.
    untagged_pair_faces = {frozenset(pair) for pair in combinations(nested, 2)}
    assert all(convex(list(face)) for face in untagged_pair_faces)
    history_multiplicity = expected_cores
    shield_boolean_faces_including_empty = 2 ** len(shield)
    shield_nonempty_faces = shield_boolean_faces_including_empty - 1
    assert shield_nonempty_faces > len(records)

    # In each fixed-core sunflower, every whole-completion plus another
    # nested label is bad.  For the middle label z_2, the common carrier
    # triple {u,v,z_2} splits the five failures into two fixed-role classes;
    # the larger has three labels.
    good_mixed_extensions = 0
    tested_mixed_extensions = 0
    for subset in core_subsets:
        core = [u, v, *subset]
        for i, z_i in enumerate(nested):
            completion = [*core, z_i]
            for j, z_j in enumerate(nested):
                if i == j:
                    continue
                tested_mixed_extensions += 1
                if convex([*completion, z_j]):
                    good_mixed_extensions += 1
    assert good_mixed_extensions == 0
    carrier_index = 2
    carrier = [u, v, nested[carrier_index]]
    inward = [
        z for z in nested[carrier_index + 1 :]
        if strictly_inside_triangle(z, *carrier)
    ]
    outward = [
        z for z in nested[:carrier_index]
        if strictly_inside_triangle(nested[carrier_index], u, v, z)
    ]
    assert len(inward) == 3 and len(outward) == 2

    return {
        "points": {
            "u": frac_pair(u),
            "v": frac_pair(v),
            "outer": [frac_pair(p) for p in outer],
            "nested_outer_to_inner": [frac_pair(p) for p in nested],
        },
        "general_position": True,
        "outer_shield_size": len(shield),
        "outer_shield_boolean_faces_including_empty": shield_boolean_faces_including_empty,
        "outer_shield_nonempty_faces": shield_nonempty_faces,
        "core_rank": 2 + 3,
        "source_rank": 2 + 3 + 1,
        "cores": expected_cores,
        "ears": len(ears),
        "blockers": len(blockers),
        "records": len(records),
        "projection_degrees": {
            "source": source_degree,
            "target": target_degree,
            "mark_pair": pair_degree,
        },
        "untagged_two_petal_faces": len(untagged_pair_faces),
        "history_multiplicity_per_core_independent_pair_face": history_multiplicity,
        "mixed_whole_completion_extensions_tested": tested_mixed_extensions,
        "mixed_whole_completion_extensions_good": good_mixed_extensions,
        "common_carrier_triple": [frac_pair(point) for point in carrier],
        "common_role_container_sizes": {"new_label_hidden": len(inward), "old_label_hidden": len(outward)},
        "all_source_and_target_faces_convex": True,
        "all_repairs_hide_the_ear": True,
        "all_same_core_same_side_pairs_incompatible": True,
    }


def common_target_audit() -> dict:
    # Exact fixture for the exceptional active-endpoint star in Theorem 3C.
    # W={t,u,v} is fixed, z is the common left endpoint, and the b_i are
    # distinct right endpoints.  The first circuit ignores b_i and hides t;
    # the one-ended refinement W+b_i has a second common circuit hiding u.
    z = (Fraction(-1), Fraction(0))
    t = (Fraction(0), Fraction(0))
    u = (Fraction(1), Fraction(1))
    v = (Fraction(6, 5), Fraction(-1))
    right = [
        (Fraction(13, 10), Fraction(7, 5)),
        (Fraction(7, 5), Fraction(3, 2)),
        (Fraction(3, 2), Fraction(17, 10)),
        (Fraction(8, 5), Fraction(2)),
        (Fraction(17, 10), Fraction(19, 10)),
        (Fraction(9, 5), Fraction(21, 10)),
    ]
    target = [t, u, v]
    points = [z, *target, *right]
    assert len({point[0] for point in points}) == len(points)
    assert all(orient(*triple) != 0 for triple in combinations(points, 3))
    assert convex(target)
    for b in right:
        assert z[0] < min(point[0] for point in target)
        assert b[0] > max(point[0] for point in target)
        assert strictly_inside_triangle(t, z, u, v)
        assert not convex([*target, z, b])
        assert strictly_inside_triangle(u, t, v, b)
        assert not convex([*target, b])

    loads = [Fraction(i) for i in range(1, len(right) + 1)]
    total_load = sum(loads)
    max_load = max(loads)
    trace_types = math.comb(len(target), 2) + math.comb(len(target), 3)
    support_lower = Fraction(total_load, 16 * max_load * trace_types)
    assert len(right) >= support_lower
    detached_triple_half_mass = Fraction(math.comb(len(right), 3), 8)
    common_target_demand_before_global_normalization = total_load * Fraction(
        1, 2 ** (len(target) + 2)
    )
    assert detached_triple_half_mass >= common_target_demand_before_global_normalization
    return {
        "fixed_target_W": [frac_pair(point) for point in target],
        "common_left_endpoint": frac_pair(z),
        "right_endpoints": [frac_pair(point) for point in right],
        "loads": [str(value) for value in loads],
        "total_load_H_W": str(total_load),
        "maximum_endpoint_load_eta_star": str(max_load),
        "theorem_3C_support_lower": str(support_lower),
        "detached_endpoint_triple_half_mass": str(detached_triple_half_mass),
        "common_target_demand_before_global_normalization": str(
            common_target_demand_before_global_normalization
        ),
        "detached_endpoint_shield_pays_fixture": True,
        "rank_two_sunflower_type": "star centered at active endpoint",
        "first_common_circuit": "t inside conv{z,u,v}",
        "one_ended_refinement": "u inside conv{t,v,b_i} for every i",
        "all_W_union_endpoint_pairs_bad": True,
        "all_refined_W_union_b_i_bad": True,
    }


def main() -> None:
    certificate = {
        "skew": skew_audit(),
        "asymptotic_and_bank": asymptotic_audit(),
        "bounded_rank_acp_geometry": geometry_audit(),
        "common_target_circuit_sunflower": common_target_audit(),
    }
    out = Path(__file__).with_name("bounded_rank_skew_sunflower_certificate.json")
    out.write_text(json.dumps(certificate, indent=2) + "\n")
    print("bounded-rank skew/sunflower audit: PASS")
    print(json.dumps(certificate, indent=2))


if __name__ == "__main__":
    main()
