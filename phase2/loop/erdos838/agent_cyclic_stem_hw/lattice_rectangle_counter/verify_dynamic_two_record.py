#!/usr/bin/env python3
"""Exact arithmetic stress tests for the dynamic two-record spend/reset gate."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from math import comb, log2
from pathlib import Path

sys.set_int_max_str_digits(0)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def log2_big(value: int) -> float:
    shift = max(0, value.bit_length() - 53)
    return shift + log2(value >> shift)


def product_pair_identity(sizes: list[int]) -> dict[str, int]:
    """Partition ordered word pairs by their first unequal coordinate."""
    total = 1
    for size in sizes:
        total *= size
    prefix = 1
    suffix = total
    spend = 0
    for size in sizes:
        suffix //= size
        spend += prefix * size * (size - 1) * suffix * suffix
        prefix *= size
    assert total * total == spend + total
    return {"records": total, "first_difference_pairs": spend, "diagonal_pairs": total}


def collision_kraft(sizes: list[int]) -> Fraction:
    """Sum of normalized squared cell masses over successive prefix partitions."""
    prefix = 1
    result = Fraction(1)
    for size in sizes:
        prefix *= size
        result += Fraction(1, prefix)
    return result


def proposition26_models() -> list[dict]:
    rows = []
    for a, b, m in ((4, 4, 16), (8, 8, 256), (16, 16, 65536)):
        s = a + b
        child_sources = m**s
        records = m * child_sources
        child_faces = (m + 1) ** s
        ratio = Fraction(records * records, child_faces * child_faces)
        assert 2 * s <= m + 1
        assert ratio >= Fraction(m * m, 4)

        # A partial transversal occupying t internal blocks is contained in
        # M^(s-t) full child sources and in M times as many outer records.
        reuse_by_occupied_blocks = [m ** (s - t + 1) for t in range(s + 1)]
        weighted_incidence = records * (1 << s)
        assert weighted_incidence == sum(
            comb(s, t) * (m**t) * reuse_by_occupied_blocks[t] for t in range(s + 1)
        )
        squared_reuse_incidence = sum(
            comb(s, t) * (m**t) * reuse_by_occupied_blocks[t] ** 2
            for t in range(s + 1)
        )
        assert Fraction(squared_reuse_incidence, child_faces) == m ** (s + 2)

        sizes = [m] * (s + 1)  # retained, hidden, and apex microcoordinates
        pair_identity = product_pair_identity(sizes)
        assert pair_identity["records"] == records
        tagged_collision = collision_kraft(sizes)
        assert tagged_collision < Fraction(m, m - 1)
        coordinate_reuse_kraft = Fraction(s + 1, m)

        rows.append(
            {
                "a": a,
                "b": b,
                "M": m,
                "internal_coordinate_count": s,
                "records_E": records,
                "untagged_child_faces_V": child_faces,
                "E_squared_over_V_squared": q(ratio),
                "log2_E_squared_over_V_squared": 2
                * (log2_big(records) - log2_big(child_faces)),
                "proved_lower_bound_M_squared_over_4": m * m // 4,
                "minimum_full_child_face_reuse": m,
                "maximum_empty_child_face_reuse": records,
                "mean_child_face_reuse": q(Fraction(weighted_incidence, child_faces)),
                "mean_squared_child_face_reuse": m ** (s + 2),
                "reuse_by_occupied_internal_blocks": reuse_by_occupied_blocks,
                "tagged_prefix_collision_kraft": q(tagged_collision),
                "tagged_prefix_collision_kraft_float": float(tagged_collision),
                "tagged_prefix_collision_kraft_upper_bound": q(Fraction(m, m - 1)),
                "single_coordinate_squared_reuse_kraft": q(coordinate_reuse_kraft),
                "ordered_pair_partition": pair_identity,
            }
        )
    return rows


def parabolic_prefix_models() -> list[dict]:
    rows = []
    for depth in (8, 16, 32, 64, 128):
        demand = (1 << (depth + 1)) - 1
        faces = 1 << depth
        reuse_square_sum = (depth + 1) ** 2
        for maximum in range(1, depth + 1):
            reuse = depth - maximum + 1
            reuse_square_sum += (1 << (maximum - 1)) * reuse * reuse
        reuse_sum = demand
        # Empty set has reuse depth+1; sets with maximum m have multiplicity 2^(m-1).
        assert reuse_sum == (depth + 1) + sum(
            (1 << (maximum - 1)) * (depth - maximum + 1)
            for maximum in range(1, depth + 1)
        )
        capacity_square_kraft = sum(4**j for j in range(depth + 1))
        rows.append(
            {
                "depth": depth,
                "weighted_demand_E": demand,
                "largest_prefix_face_bank_V": faces,
                "E_squared_over_V_squared": q(Fraction(demand * demand, faces * faces)),
                "E_squared_over_V_squared_float": float(
                    Fraction(demand * demand, faces * faces)
                ),
                "maximum_face_reuse": depth + 1,
                "mean_face_reuse": q(Fraction(reuse_sum, faces)),
                "mean_squared_face_reuse": q(Fraction(reuse_square_sum, faces)),
                "mean_squared_face_reuse_float": float(
                    Fraction(reuse_square_sum, faces)
                ),
                "nested_capacity_square_kraft": q(
                    Fraction(capacity_square_kraft, faces * faces)
                ),
            }
        )
        assert Fraction(demand * demand, faces * faces) < 4
        assert Fraction(reuse_square_sum, faces) < 7
        assert Fraction(capacity_square_kraft, faces * faces) < Fraction(4, 3)
    return rows


def ramp_exponents(h: int) -> list[int]:
    length = 1 << h
    plateau = length // 2
    ramp = [1 << j for j in range(h)]
    return ramp + [length] * plateau + list(reversed(ramp))


def ramp_plateau_model(h: int) -> dict:
    exponents = ramp_exponents(h)
    sizes = [1 << exponent for exponent in exponents]
    b = len(sizes)
    sources = 1
    for size in sizes:
        sources *= size

    optional_prefix = [1]
    for size in sizes:
        optional_prefix.append(optional_prefix[-1] * (size + 1))
    down_faces = optional_prefix[-1]
    interval_faces = 0
    for i in range(b):
        left_pairs = comb(sizes[i], 2)
        for j in range(i + 1, b):
            middle = optional_prefix[j] // optional_prefix[i + 1]
            interval_faces += left_pairs * comb(sizes[j], 2) * middle
    atomic_faces = down_faces + interval_faces

    ambient_labels = sum(sizes)
    ell = (ambient_labels - 1).bit_length()
    cap = 1 << (ell - b)
    capped_demand = cap * sources
    assert atomic_faces < 21 * (1 + comb(b, 2)) * sources
    assert capped_demand > atomic_faces

    pair_identity = product_pair_identity(sizes)
    tagged_collision = collision_kraft(sizes)
    assert tagged_collision < 2
    coordinate_reuse_kraft = sum((Fraction(1, size) for size in sizes), Fraction())
    assert coordinate_reuse_kraft < 2

    prefix = 1
    prefix_collision_rows = []
    for index, size in enumerate(sizes, start=1):
        prefix *= size
        prefix_collision_rows.append(
            {
                "depth": index,
                "cells": prefix,
                "records_per_cell": sources // prefix,
                "normalized_squared_mass": q(Fraction(1, prefix)),
            }
        )

    ratio = Fraction(capped_demand * capped_demand, atomic_faces * atomic_faces)
    return {
        "h": h,
        "L": 1 << h,
        "block_count_b": b,
        "exponents": exponents,
        "source_records_N": sources,
        "ambient_label_count_n0": ambient_labels,
        "ell": ell,
        "capped_multiplier_d": cap,
        "capped_demand_E": capped_demand,
        "atomic_face_bank_V": atomic_faces,
        "E_squared_over_V_squared_numerator": capped_demand * capped_demand,
        "E_squared_over_V_squared_denominator": atomic_faces * atomic_faces,
        "log2_E_squared_over_V_squared": 2
        * (log2_big(capped_demand) - log2_big(atomic_faces)),
        "maximum_raw_child_reuse": sources // 2,
        "maximum_capped_child_reuse": capped_demand // 2,
        "plateau_block_raw_child_reuse": sources // (1 << (1 << h)),
        "tagged_prefix_collision_kraft": q(tagged_collision),
        "tagged_prefix_collision_kraft_float": float(tagged_collision),
        "single_coordinate_squared_reuse_kraft": q(coordinate_reuse_kraft),
        "single_coordinate_squared_reuse_kraft_float": float(coordinate_reuse_kraft),
        "ordered_pair_partition": pair_identity,
        "first_six_prefix_collision_rows": prefix_collision_rows[:6],
        "last_prefix_collision_row": prefix_collision_rows[-1],
    }


def neutral_pair_potential_examples() -> dict:
    # For a partition of E records into child cells e_j, sum e_j^2 counts
    # ordered pairs which remain together.  The complement E^2-sum e_j^2
    # is precisely the pair mass released/spent at that refinement.
    examples = []
    for children in ((5, 3, 2), (7, 7, 1, 1), (16, 4, 4, 4, 4)):
        parent = sum(children)
        child_energy = sum(value * value for value in children)
        spend = parent * parent - child_energy
        assert parent * parent == spend + child_energy
        examples.append(
            {
                "child_sizes": list(children),
                "parent_pair_energy": parent * parent,
                "spent_cross_child_pairs": spend,
                "descending_child_pair_energy": child_energy,
            }
        )
    return {
        "identity": "E(parent)^2 = spent ordered cross-child pairs + sum_child E(child)^2",
        "examples": examples,
    }


def main() -> None:
    result = {
        "exact_gate_tested": (
            "Compatible ordered record pairs spend to injective cross-union faces; "
            "same-cell pairs descend to tagged children and charge their prefix/child face banks."
        ),
        "killed_untagged_claim": (
            "Forgetting an entropy-bearing blocker/apex coordinate before descent costs only "
            "2^o(r) cumulative child reuse."
        ),
        "proposition26_fixed_outer_long_ear": proposition26_models(),
        "parabolic_nested_prefix": parabolic_prefix_models(),
        "ramp_plateau": [ramp_plateau_model(6), ramp_plateau_model(7)],
        "neutral_ordered_pair_potential": neutral_pair_potential_examples(),
    }
    output = Path(__file__).with_name("dynamic_two_record_certificate.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("dynamic two-record audit: PASS")
    for row in result["proposition26_fixed_outer_long_ear"]:
        print(
            f"Prop26 M={row['M']}: log2(E^2/V^2)={row['log2_E_squared_over_V_squared']:.6f}, "
            f"tagged Kraft={row['tagged_prefix_collision_kraft_float']:.9f}"
        )
    for row in result["parabolic_nested_prefix"]:
        print(
            f"parabolic depth={row['depth']}: E^2/V^2={row['E_squared_over_V_squared_float']:.9f}, "
            f"mean reuse^2={row['mean_squared_face_reuse_float']:.9f}"
        )
    for row in result["ramp_plateau"]:
        print(
            f"ramp h={row['h']}: log2(E^2/V^2)={row['log2_E_squared_over_V_squared']:.6f}, "
            f"tagged Kraft={row['tagged_prefix_collision_kraft_float']:.9f}"
        )


if __name__ == "__main__":
    main()
