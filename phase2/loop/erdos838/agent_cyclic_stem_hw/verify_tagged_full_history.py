#!/usr/bin/env python3
"""Exact arithmetic audits for the tagged full-history Carleson report."""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import ceil, comb, factorial
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
GRADED = ERDOS / "agent_graded_supersat"
sys.path.insert(0, str(GRADED))

from graded_balanced import pascal_row  # noqa: E402


def integer_nth_root(value: int, degree: int) -> int:
    assert value >= 1 and degree >= 1
    low = 1
    high = 1 << ((value.bit_length() + degree - 1) // degree)
    while low + 1 < high:
        middle = (low + high) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle
    assert low**degree <= value < (low + 1) ** degree
    return low


def log2_fraction(value: Fraction) -> float:
    assert value > 0
    return math.log2(value.numerator) - math.log2(value.denominator)


def pascal_modal_audit(parameters: tuple[int, ...]) -> list[dict[str, object]]:
    """Exact activity lower bound for all exterior records at a modal rank."""
    rows = []
    last_exponent = 0.0
    for parameter in parameters:
        n, _, _, profile = pascal_row(parameter, parameter)[parameter // 2]
        volume = 1 + sum(profile)
        rank = max(range(1, len(profile)), key=lambda index: (profile[index], index))
        sources = profile[rank]
        assert sources * (parameter + 1) >= volume
        assert rank <= parameter
        root = integer_nth_root(sources, rank)
        up_sum = (rank + 1) * (
            profile[rank + 1] if rank + 1 < len(profile) else 0
        )
        # Since e<3 and S^(1/r) >= root, the optimized hull identity gives
        # qbar > r(root/3-1).  Subtract the exact ordinary up-incidence sum.
        numerator = sources * rank * (root - 3) - 3 * up_sum
        exterior_over_volume = Fraction(max(0, numerator), 3 * volume)
        pair_fibre_lower = exterior_over_volume**2
        exponent = (
            log2_fraction(exterior_over_volume) / math.log2(n)
            if exterior_over_volume > 1 else 0.0
        )
        if parameter >= 16:
            assert exponent > 0.6
        if parameter >= 20:
            # Finite exponents need not be monotone all the way to their
            # asymptotic limit, but remain uniformly polynomial.
            assert exponent > 0.64
        last_exponent = exponent
        rows.append(
            {
                "parameter_m": parameter,
                "n": n,
                "modal_rank": rank,
                "maximum_convex_rank": parameter,
                "V": str(volume),
                "modal_sources": str(sources),
                "floor_S_to_1_over_r": root,
                "ordinary_up_incidence_sum": str(up_sum),
                "exact_exterior_over_V_lower": str(exterior_over_volume),
                "log_lower_over_log_n": exponent,
                "exact_two_face_fibre_lower": str(pair_fibre_lower),
            }
        )
    assert last_exponent > 0.65
    return rows


def global_history_bounds() -> list[dict[str, object]]:
    """Robust two-history inverse bound with unordered chronology."""
    rows = []
    previous_ratio = None
    for length in (16, 32, 64, 128, 256, 512, 1024):
        depth = length
        # Per reverse step: at most four ordered visible-vertex choices and
        # eight constant transition types.  Two unmarked chronological orders
        # cost (h!)^2.  This intentionally overcounts the actual decoder.
        fibre = factorial(depth) ** 2 * (8 * length**4) ** depth
        log_fibre = math.log2(fibre)
        ratio = log_fibre / (length * length)
        if previous_ratio is not None:
            assert ratio < previous_ratio
        previous_ratio = ratio
        rows.append(
            {
                "L": length,
                "history_depth": depth,
                "exact_fibre_bit_length": fibre.bit_length(),
                "log2_fibre_over_L_squared": ratio,
                "symbolic_bound": "(L!)^2 (8 L^4)^L",
            }
        )
    return rows


def product_endpoint_audit() -> list[dict[str, object]]:
    rows = []
    for size in (2, 3, 4, 8, 16, 64, 256, 4096):
        reservoir = 1 + size + comb(size, 2)
        local_fibre = ceil(size**4 / reservoir**2)
        assert local_fibre <= 4
        rows.append(
            {
                "alphabet_M": size,
                "endpoint_reservoir_per_side": reservoir,
                "exact_local_fibre": local_fibre,
            }
        )
    return rows


def subsets_at_most_two(size: int) -> list[tuple[int, ...]]:
    return [item for rank in range(3) for item in combinations(range(size), rank)]


def symmetric_endpoint_audit() -> list[dict[str, object]]:
    """Exact two-output code: one pair-compatible reservoir per history."""
    parameters = [
        (2, 3, 2, 4),
        (3, 5, 4, 4),
        (4, 6, 5, 7),
        (8, 8, 8, 8),
        (16, 16, 16, 16),
        (32, 64, 16, 128),
    ]
    rows = []
    for q1, q2, y1, y2 in parameters:
        left = subsets_at_most_two(q1)
        right = subsets_at_most_two(q2)
        domain_size = q1 * q2 * y1 * y2
        codomain_size = len(left) * len(right)
        fibre = ceil(domain_size / codomain_size)
        if domain_size <= 200_000:
            codomain = list(product(left, right))
            loads = Counter(
                codomain[index % codomain_size] for index in range(domain_size)
            )
            assert max(loads.values()) == fibre
        if q1 == q2 == y1 == y2:
            assert fibre <= 4
        rows.append(
            {
                "q1": q1,
                "q2": q2,
                "blockers_y1": y1,
                "blockers_y2": y2,
                "domain_symbols": domain_size,
                "joint_endpoint_codewords": codomain_size,
                "exact_maximum_fibre": fibre,
            }
        )
    return rows


def dominance_poset_reservoir_audit() -> list[dict[str, object]]:
    """Compatible subsets are empty, singletons, and incomparable pairs."""
    families: dict[str, list[tuple[int, int]]] = {}
    for size in (4, 8, 16, 32):
        families[f"chain_{size}"] = [(index, index) for index in range(size)]
        families[f"antichain_{size}"] = [
            (index, size - index) for index in range(size)
        ]
    for side in (3, 4, 6, 8):
        families[f"grid_{side}x{side}"] = [
            (first, second) for first in range(side) for second in range(side)
        ]

    rows = []
    for name, points in families.items():
        size = len(points)
        comparable = [[False] * size for _ in range(size)]
        incomparable_pairs = 0
        for i, j in combinations(range(size), 2):
            first, second = points[i], points[j]
            relation = (
                (first[0] <= second[0] and first[1] <= second[1])
                or (second[0] <= first[0] and second[1] <= first[1])
            )
            comparable[i][j] = comparable[j][i] = relation
            incomparable_pairs += not relation
        ordered = sorted(range(size), key=lambda index: (sum(points[index]), points[index]))
        longest = [1] * size
        for later_position, later in enumerate(ordered):
            for earlier in ordered[:later_position]:
                if (points[earlier][0] <= points[later][0]
                        and points[earlier][1] <= points[later][1]
                        and points[earlier] != points[later]):
                    longest[later] = max(longest[later], longest[earlier] + 1)
        height = max(longest)
        reservoir = 1 + size + incomparable_pairs
        assert 2 * height * reservoir >= size * size
        rows.append(
            {
                "family": name,
                "endpoint_points": size,
                "height": height,
                "incomparable_pairs": incomparable_pairs,
                "compatible_subset_reservoir": reservoir,
                "height_lower_bound_floor": size * size // (2 * height),
            }
        )
    return rows


def ceil_fraction(value: Fraction) -> int:
    return (value.numerator + value.denominator - 1) // value.denominator


def global_joint_code_audit() -> list[dict[str, object]]:
    """Global enumeration rounds once, allowing endpoint surplus to telescope."""
    profiles: list[tuple[str, list[int], list[int]]] = []
    profiles.append(("balanced_constant", [16] * 32, [16] * 32))
    profiles.append(
        (
            "successor_handoff",
            [2 ** (1 + (index % 8)) for index in range(40)],
            [2 ** (1 + ((index + 1) % 8)) for index in range(40)],
        )
    )
    ramp_exponents = [1, 2, 4, 8, 16, 16, 16, 16, 8, 4, 2, 1]
    ramp_q = [2**exponent for exponent in ramp_exponents]
    profiles.append(("ramp_successor_handoff", ramp_q, ramp_q[1:] + ramp_q[:1]))
    profiles.append(
        (
            "oscillating_local_deficit",
            [2, 2**32] * 8,
            [2**32, 2] * 8,
        )
    )

    rows = []
    for name, q_values, y_values in profiles:
        assert len(q_values) == len(y_values)
        # Use the same alphabets on the two history sides.  The domain and
        # codomain below already account for both output faces.
        numerator = 1
        denominator = 1
        local_rounded = 1
        for q, y in zip(q_values, y_values):
            sigma = 1 + q + comb(q, 2)
            local_ratio = Fraction(q * q * y * y, sigma * sigma)
            numerator *= q * q * y * y
            denominator *= sigma * sigma
            local_rounded *= max(1, ceil_fraction(local_ratio))
        global_fibre = max(1, ceil_fraction(Fraction(numerator, denominator)))
        assert global_fibre <= local_rounded
        rows.append(
            {
                "family": name,
                "levels": len(q_values),
                "log2_endpoint_product": sum(math.log2(value) for value in q_values),
                "log2_blocker_product": sum(math.log2(value) for value in y_values),
                "global_joint_fibre_bit_length": global_fibre.bit_length(),
                "product_of_local_ceilings_bit_length": local_rounded.bit_length(),
                "global_no_worse_than_local": True,
            }
        )
    oscillating = rows[-1]
    assert oscillating["global_joint_fibre_bit_length"] < 100
    assert oscillating["product_of_local_ceilings_bit_length"] > 400
    return rows


def variable_core_reuse_audit() -> list[dict[str, object]]:
    """Guess <=2 open slots per output, then the labelled core is forced."""
    rows = []
    previous_ratio = None
    for rank in (16, 32, 64, 128, 256, 512, 1024):
        slots = sum(comb(rank + 2, size) for size in range(3))
        # Two outputs, two insertion edges, two directed tangent chords, and
        # eight constant transition types.  This is a generous overcount.
        local_state_fibre = 8 * slots**2 * rank**6
        depth = rank
        full_fibre = factorial(depth) ** 2 * local_state_fibre**depth
        ratio = math.log2(full_fibre) / (rank * rank)
        if previous_ratio is not None:
            assert ratio < previous_ratio
        previous_ratio = ratio
        rows.append(
            {
                "rank": rank,
                "open_slot_guesses_per_output": slots,
                "local_variable_core_state_fibre": str(local_state_fibre),
                "full_history_fibre_bit_length": full_fibre.bit_length(),
                "log2_full_fibre_over_rank_squared": ratio,
            }
        )
    return rows


def nested_prefix_audit() -> dict[str, object]:
    maximum = Fraction()
    sharp_depths = []
    for depth in range(513):
        ratio = Fraction((depth + 1) ** 2, 2**depth)
        if ratio > maximum:
            maximum = ratio
            sharp_depths = [depth]
        elif ratio == maximum:
            sharp_depths.append(depth)
    assert maximum == Fraction(9, 4)
    return {
        "depths_checked": 513,
        "maximum_ordered_pair_to_Boolean_bank_ratio": str(maximum),
        "sharp_depths": sharp_depths,
    }


def n58_audit() -> dict[str, object]:
    source = json.loads((HERE / "corrected_addability_certificate.json").read_text())
    record = source["records"]["n58_half_weight_record"]
    rank = next(row for row in record["ranks_below_ell"] if row["rank"] == 5)
    incidence = int(rank["exterior_incidence_sum_on_low_addable_faces"])
    volume = int(record["V"])
    pair_ratio = Fraction(incidence**2, volume**2)
    minimum_fibre = ceil(pair_ratio)
    assert incidence == 15_731_969
    assert volume == 1_061_907
    assert minimum_fibre == 220
    return {
        "n": 58,
        "rank": 5,
        "selected_exterior_records": incidence,
        "V": volume,
        "exact_pair_demand_over_V_squared": str(pair_ratio),
        "minimum_two_face_fibre": minimum_fibre,
        "interpretation": (
            "kills a small universal constant, but is harmless at the "
            "2^{o((log n)^2)} full-history scale"
        ),
    }


def insertion_transfer_audit() -> dict[str, object]:
    source = json.loads(
        (HERE / "insertion_chain_universality_certificate.json").read_text()
    )
    names = [row["family"] for row in source["records"]]
    required = {
        "central_Pascal_T_6_3",
        "saved_half_weight_n20",
        "saved_half_weight_n24",
        "saved_half_weight_n30",
        "saved_half_weight_n58",
    }
    assert required <= set(names)
    return {
        "verified_transferred_families": names,
        "ambient_base_cost": (
            "adding the three-point insertion base multiplies V by at most 8"
        ),
    }


def main() -> None:
    result = {
        "claim_boundary": (
            "rank-local 2^o(r) reuse is false for all exterior records; "
            "a label-faithful O(log n)-level decoder has total fibre "
            "2^O(log n log log n)"
        ),
        "central_pascal_local_counterfamily": pascal_modal_audit(
            (8, 12, 16, 20, 24, 32, 40, 48, 64, 80)
        ),
        "global_full_history_fibre": global_history_bounds(),
        "balanced_product_endpoint": product_endpoint_audit(),
        "symmetric_one_endpoint_per_output": symmetric_endpoint_audit(),
        "dominance_poset_compatible_reservoir": dominance_poset_reservoir_audit(),
        "global_joint_endpoint_code": global_joint_code_audit(),
        "variable_outer_core_reuse": variable_core_reuse_audit(),
        "nested_parabola_prefix": nested_prefix_audit(),
        "insertion_chain_transfer": insertion_transfer_audit(),
        "n58_exact_regression": n58_audit(),
    }
    output = HERE / "tagged_full_history_certificate.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
