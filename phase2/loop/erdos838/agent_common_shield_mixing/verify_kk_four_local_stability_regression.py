#!/usr/bin/env python3
"""Exact audit for KK_FOUR_LOCAL_STABILITY_REGRESSION.md."""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


TANGENT = load_module(
    "tangent_for_kk_stability_regression",
    HERE / "verify_tangent_marked_shield_descent.py",
)


def fixed_tangent_geometry_audit() -> dict[str, object]:
    blocks, repairs, points = TANGENT.configuration()
    words = [
        bits
        for bits in product(range(2), repeat=8)
        if bits[7] == bits[0] == bits[1] == bits[2] == 0
    ]
    completions = [frozenset(TANGENT.completion_indices(bits)) for bits in words]
    base = frozenset((14, 0, 2, 4))
    petals = [completion - base for completion in completions]
    assert len(petals) == len(set(petals)) == 16
    assert all(len(petal) == 4 for petal in petals)

    # The marked repair occurrence and actual shield are fixed.
    mark = 16
    shield = frozenset((16, 18, 19))
    assert TANGENT.convex([points[i] for i in shield])
    for petal in petals:
        carrier = base | petal
        star = carrier | {mark}
        assert TANGENT.convex([points[i] for i in carrier])
        assert TANGENT.convex([points[i] for i in star])
        assert not TANGENT.convex([points[i] for i in star | shield])

    # Pairwise incompatibility forces any B-convex support to contain at
    # most one complete petal.
    for first, second in combinations(petals, 2):
        assert not TANGENT.convex([points[i] for i in base | first | second])

    active = sorted(set().union(*petals))
    convex_supports = []
    maximum_contained = 0
    for mask in range(1 << len(active)):
        support = frozenset(active[i] for i in range(len(active)) if mask >> i & 1)
        if TANGENT.convex([points[i] for i in base | support]):
            contained = sum(petal <= support for petal in petals)
            assert contained <= 1
            maximum_contained = max(maximum_contained, contained)
            convex_supports.append(support)
    assert maximum_contained == 1

    # Four-covering a group's union would force it convex.  Exhaust all
    # nonempty subfamilies and check that this happens only for a singleton.
    four_cover_groups = 0
    largest_four_cover_group = 0
    for mask in range(1, 1 << len(petals)):
        group = [petals[i] for i in range(len(petals)) if mask >> i & 1]
        support = set().union(*group)
        covers = all(
            any(set(trace) <= petal for petal in group)
            for trace in combinations(support, 4)
        )
        if covers:
            four_cover_groups += 1
            largest_four_cover_group = max(largest_four_cover_group, len(group))
            assert len(group) == 1
            assert TANGENT.convex([points[i] for i in base | support])
    assert four_cover_groups == len(petals)

    return {
        "blocks": len(blocks),
        "repairs": len(repairs),
        "active_points": len(active),
        "petals": len(petals),
        "convex_supports": len(convex_supports),
        "max_petals_in_convex_support": maximum_contained,
        "four_cover_groups": four_cover_groups,
        "largest_four_cover_group": largest_four_cover_group,
    }


def shadow_and_overlap_audit() -> dict[str, object]:
    _, _, points = TANGENT.configuration()
    words = [
        bits
        for bits in product(range(2), repeat=8)
        if bits[7] == bits[0] == bits[1] == bits[2] == 0
    ]
    base = frozenset((14, 0, 2, 4))
    petals = [frozenset(TANGENT.completion_indices(bits)) - base for bits in words]
    r, L, M = 4, 2, 16

    levels = []
    downclosure = set()
    for k in range(r + 1):
        degree = Counter()
        for petal in petals:
            for subset in combinations(sorted(petal), k):
                face = frozenset(subset)
                degree[face] += 1
                downclosure.add(face)
                assert TANGENT.convex([points[i] for i in base | face])
        assert len(degree) == comb(r, k) * L**k
        assert set(degree.values()) == {L ** (r - k)}
        assert sum(degree.values()) == M * comb(r, k)
        levels.append(
            {
                "rank": k,
                "outputs": len(degree),
                "load": L ** (r - k),
                "incidences": sum(degree.values()),
            }
        )

    assert len(downclosure) == (L + 1) ** r
    proper = downclosure - set(petals)
    assert len(proper) == (L + 1) ** r - L**r == 65

    return {
        "levels": levels,
        "boolean_bank_union": len(downclosure),
        "proper_downclosure": len(proper),
    }


def scalable_formula_audit() -> dict[str, object]:
    rows = []
    previous_ratio = None
    # log n=m, delta=kappa=1/4.  Hence L=2^(m/4), r=m/4,
    # and log |T|=m^2/16 exactly.
    for m in (16, 32, 64):
        r = m // 4
        L = 1 << (m // 4)
        family = L**r
        proper = (L + 1) ** r - family
        ratio = Q(proper, family)
        assert family.bit_length() - 1 == m * m // 16
        # An exact convenient version of (1+1/L)^r-1~r/L.
        assert Q(r, L) <= ratio <= Q(2 * r, L)
        if previous_ratio is not None:
            assert ratio < previous_ratio
        previous_ratio = ratio
        rows.append(
            {
                "log_n": m,
                "r": r,
                "L": L,
                "log2_family": family.bit_length() - 1,
                "proper_shadow_ratio": str(ratio),
                "cover_tags": family,
            }
        )
    return {"scales": rows, "quadratic_coefficient": "1/16"}


def main() -> None:
    result = {
        "fixed_tangent_geometry": fixed_tangent_geometry_audit(),
        "shadow_overlap": shadow_and_overlap_audit(),
        "scalable_formulas": scalable_formula_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: KK/four-local stability dichotomy killed by fixed-tangent radial transversals")


if __name__ == "__main__":
    main()
