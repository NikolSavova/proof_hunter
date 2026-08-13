#!/usr/bin/env python3
"""Exact verifier and census for the component/overlap collision bound."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import product
from math import floor
from pathlib import Path


def tile_coverage(I: tuple[int, ...], J: tuple[int, ...], K: tuple[int, ...]) -> set[int]:
    ij = {i + j for i in I for j in J}
    ik = {i + k for i in I for k in K}
    jk = {j + k for j in J for k in K}
    return ij | ik | {q for q in jk if q - 1 in jk}


def prefix_length(covered: set[int]) -> int:
    m = 0
    while m in covered:
        m += 1
    return m


def raw_capacity(a: int, b: int, c: int) -> int:
    """The old direct-plus-adjacency bound, with empty JK handled exactly."""
    return a * (b + c) + b * c - (1 if b and c else 0)


def collision_bound(a: int, b: int, c: int) -> int:
    """Universal type bound for the three-tile predicate."""
    return a * (b + c) + b * c - min(b, c)


def envelope(ell: int) -> int:
    """Maximum collision_bound over all type splits with total ell."""
    return floor(ell * ell / 3) - floor(ell / 3)


def canonical_positive_splits(ell: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, ell - a - b)
        for a in range(1, ell - 1)
        for b in range(1, ell - a)
        if b >= ell - a - b
    ]


def target(ell: int) -> int:
    return floor(85 * ell * ell / 294) + 1


def exhaustive_sets(radius: int) -> dict[str, object]:
    subsets = [
        tuple(x for x in range(radius) if mask & (1 << x))
        for mask in range(1 << radius)
    ]
    checked = 0
    equality_cases = 0
    first_equalities: list[dict[str, object]] = []
    for I, J, K in product(subsets, repeat=3):
        if 0 not in I or (0 not in J and 0 not in K):
            continue
        m = prefix_length(tile_coverage(I, J, K))
        bound = collision_bound(len(I), len(J), len(K))
        if m > bound:
            raise AssertionError((I, J, K, m, bound))
        checked += 1
        if m == bound:
            equality_cases += 1
            if len(first_equalities) < 12:
                first_equalities.append(
                    {"I": list(I), "J": list(J), "K": list(K), "m": m}
                )
    return {
        "coordinate_domain": [0, radius - 1],
        "normalized_triples_checked": checked,
        "equality_cases": equality_cases,
        "first_equality_cases": first_equalities,
        "status": "PASS",
    }


def exhaustive_both_zero(radius: int) -> dict[str, object]:
    """Stress the subtle 0-in-J-and-K branch on a larger coordinate box."""
    subsets = [
        tuple(x for x in range(radius) if mask & (1 << x))
        for mask in range(1 << radius)
        if mask & 1
    ]
    checked = 0
    for I, J, K in product(subsets, repeat=3):
        m = prefix_length(tile_coverage(I, J, K))
        bound = collision_bound(len(I), len(J), len(K))
        if m > bound:
            raise AssertionError((I, J, K, m, bound))
        checked += 1
    return {
        "coordinate_domain": [0, radius - 1],
        "description": "all triples with 0 in I intersect J intersect K",
        "triples_checked": checked,
        "status": "PASS",
    }


def envelope_check(limit: int) -> dict[str, object]:
    rows = []
    for ell in range(2, limit + 1):
        brute = max(
            collision_bound(a, b, ell - a - b)
            for a in range(1, ell)
            for b in range(ell - a + 1)
        )
        claimed = envelope(ell)
        if brute != claimed:
            raise AssertionError((ell, brute, claimed))
        rows.append([ell, claimed])
    payload = json.dumps(rows, separators=(",", ":")).encode()
    return {
        "ell_range": [2, limit],
        "cases": limit - 1,
        "sha256_of_ell_bound_pairs": hashlib.sha256(payload).hexdigest(),
        "status": "PASS",
    }


def prefix_relaxation_counterexample() -> dict[str, object]:
    # This realizes the cumulative count profile used by the relaxation, but
    # its true coverage is tiny.  It shows prefix count inequalities are far
    # from a completeness bridge.
    I = tuple(range(7))
    J = tuple(range(6))
    K = tuple(range(7))
    relaxed_m = collision_bound(7, 6, 7)
    for t in range(1, relaxed_m + 1):
        a = sum(x < t for x in I)
        b = sum(x < t for x in J)
        c = sum(x < t for x in K)
        if t > collision_bound(a, b, c):
            raise AssertionError((t, a, b, c))
    actual_m = prefix_length(tile_coverage(I, J, K))
    return {
        "I": list(I),
        "J": list(J),
        "K": list(K),
        "ell": 20,
        "all_prefix_count_inequalities_hold_through": relaxed_m,
        "actual_tile_prefix": actual_m,
        "conclusion": "prefix-count relaxation is necessary but not sufficient",
    }


def parity_relaxation_certificate() -> dict[str, object]:
    """Exact primal/dual certificate that the naive mod-2 model stalls at 1/3."""
    sixth = Fraction(1, 6)
    rho = Fraction(1, 3)
    # Each type has total mass 1/3 and is evenly divided between parities.
    ie = io = je = jo = ke = ko = sixth
    direct_even = ie * (je + ke) + io * (jo + ko)
    direct_odd = ie * (jo + ko) + io * (je + ke)
    jk_even = je * ke + jo * ko
    jk_odd = je * ko + jo * ke
    consecutive_even = min(jk_even, jk_odd)
    consecutive_odd = min(jk_even, jk_odd)
    if direct_even + consecutive_even != rho / 2:
        raise AssertionError
    if direct_odd + consecutive_odd != rho / 2:
        raise AssertionError
    return {
        "model": "two-state parity/carry capacity relaxation",
        "primal": {
            "rho": str(rho),
            "I_even": str(ie),
            "I_odd": str(io),
            "J_even": str(je),
            "J_odd": str(jo),
            "K_even": str(ke),
            "K_odd": str(ko),
            "direct_even_capacity": str(direct_even),
            "direct_odd_capacity": str(direct_odd),
            "JK_even_capacity": str(jk_even),
            "JK_odd_capacity": str(jk_odd),
            "consecutive_even_capacity": str(consecutive_even),
            "consecutive_odd_capacity": str(consecutive_odd),
            "required_each_parity": str(rho / 2),
        },
        "dual_sos": "1/3-(ij+ik+jk)=((i-j)^2+(i-k)^2+(j-k)^2)/6 >= 0",
        "status": "OPTIMUM_1/3_CERTIFIED",
        "conclusion": "parity/carry capacities alone cannot improve the asymptotic 1/3 ceiling",
    }


def sharp_family(rows: int = 12) -> dict[str, object]:
    examples = []
    for b in range(1, rows + 1):
        I = (0,)
        J = tuple(range(b))
        K = (b,)
        m = prefix_length(tile_coverage(I, J, K))
        bound = collision_bound(1, b, 1)
        if m != 2 * b or m != bound:
            raise AssertionError((b, m, bound))
        examples.append({"b": b, "ell": b + 2, "m": m})
    return {
        "family": "I={0}, J=[0,b-1], K={b}",
        "formula": "m=2b=collision_bound(1,b,1)",
        "verified_examples": examples,
        "consequence": "even one further universal unit of loss is false",
    }


def census(ell_min: int, ell_max: int) -> list[dict[str, object]]:
    rows = []
    for ell in range(ell_min, ell_max + 1):
        m = target(ell)
        splits = canonical_positive_splits(ell)
        old_killed = [s for s in splits if raw_capacity(*s) < m]
        new_killed = [s for s in splits if collision_bound(*s) < m]
        added = [
            {
                "counts": list(s),
                "raw_capacity": raw_capacity(*s),
                "collision_bound": collision_bound(*s),
            }
            for s in splits
            if raw_capacity(*s) >= m and collision_bound(*s) < m
        ]
        rows.append(
            {
                "ell": ell,
                "target_m": m,
                "canonical_positive_splits": len(splits),
                "raw_capacity_killed": len(old_killed),
                "collision_bound_killed": len(new_killed),
                "newly_killed": added,
                "remaining": len(splits) - len(new_killed),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--exhaustive-radius", type=int, default=6)
    parser.add_argument("--both-zero-radius", type=int, default=8)
    parser.add_argument("--envelope-limit", type=int, default=250)
    parser.add_argument("--ell-min", type=int, default=18)
    parser.add_argument("--ell-max", type=int, default=42)
    args = parser.parse_args()

    result = {
        "theorem": {
            "type_bound": "m <= ab+ac+bc-min(b,c)",
            "type_free_envelope": "m <= floor(ell^2/3)-floor(ell/3)",
            "scope": "all finite nonnegative I,J,K satisfying the three-tile prefix predicate",
        },
        "exhaustive_set_check": exhaustive_sets(args.exhaustive_radius),
        "extra_both_zero_check": exhaustive_both_zero(args.both_zero_radius),
        "envelope_check": envelope_check(args.envelope_limit),
        "sharpness_counterexample": sharp_family(),
        "prefix_relaxation_counterexample": prefix_relaxation_counterexample(),
        "parity_relaxation_certificate": parity_relaxation_certificate(),
        "record_target_census": census(args.ell_min, args.ell_max),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
