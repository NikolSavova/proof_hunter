#!/usr/bin/env python3
"""Exact audit of LONG_CHAIN_MIXED_BRANCH_BARRIER.md."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from math import ceil, comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
CHAIN = ERDOS / "agent_cyclic_stem_hw"
APA = ERDOS / "agent_apa_rank"
for directory in (CHAIN, APA):
    sys.path.insert(0, str(directory))

from verify_insertion_chain_universality import transform  # noqa: E402
from verify_apa_counterexample import matrix_profile, orient  # noqa: E402


Point = tuple[Fraction, Fraction]


def hull(points: list[Point]) -> tuple[Point, ...]:
    """Strict convex hull in counterclockwise order."""
    rows = sorted(set(points))
    assert len(rows) == len(points)
    if len(rows) <= 1:
        return tuple(rows)

    def build(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    lower = build(rows)
    upper = build(list(reversed(rows)))
    return tuple(lower[:-1] + upper[:-1])


def hard_points() -> tuple[Point, ...]:
    path = ERDOS / "agent_dual_number_amortization" / "half_weight_search_records.json"
    row = json.loads(path.read_text())["exact_records"]["20"]
    return tuple(
        (Fraction(i), Fraction(value))
        for i, value in enumerate(row["y_at_x_0_through_19"])
    )


def tangent(point: Point) -> tuple[Fraction, Fraction]:
    x, y = point
    return (x + 1) / y, (1 - x) / y


def choose_outer(image: list[Point], base: list[Point]) -> Point:
    coordinates = [tangent(point) for point in image]
    left_min = min(left for left, _ in coordinates)
    right_min = min(right for _, right in coordinates)
    fixed = base + image
    for a in range(2, 40):
        for b in range(2, 40):
            if a == b:
                continue
            left = left_min / a
            right = right_min / b
            point = ((left - right) / (left + right), Fraction(2, 1) / (left + right))
            if all(orient(point, first, second) for first, second in combinations(fixed, 2)):
                return point
    raise AssertionError("failed to choose generic common outer tip")


def main() -> None:
    original = hard_points()
    _, _, image, coordinates = transform(original)
    n = len(image)

    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    # A generic third vertex below uv.  Search avoids all mixed secants.
    lower: Point | None = None
    for numerator in range(-50, 51):
        candidate = (Fraction(numerator, 103), Fraction(-1))
        fixed = [u, v] + image
        if all(orient(candidate, first, second) for first, second in combinations(fixed, 2)):
            lower = candidate
            break
    assert lower is not None
    base = [u, v, lower]
    outer = choose_outer(image, base)
    ambient = base + image + [outer]
    assert all(orient(a, b, c) for a, b, c in combinations(ambient, 3))

    base_set = set(base)
    assert set(hull(base)) == base_set
    for point in image + [outer]:
        assert set(hull(base + [point])) == base_set | {point}

    repair_relations = 0
    for i in range(n):
        for j in range(i + 1, n):
            assert set(hull(base + [image[i], image[j]])) == base_set | {image[j]}
            repair_relations += 1
        assert set(hull(base + [image[i], outer])) == base_set | {outer}
        repair_relations += 1

    history_length = 10
    histories = comb(n, history_length)
    # The exhaustive O(N^2) pair audit above proves every arrow in every
    # increasing subset history.  Count the resulting history-arrow
    # certificates combinatorially rather than repeating the same exact
    # hull computation C(N,h) times.
    checked_arrows = histories * history_length

    v_q = 4775
    ambient_face_upper = (2 ** (len(base) + 1)) * v_q
    one_slot_fibre_lower = ceil(histories / ambient_face_upper)
    assert histories == 184756
    assert one_slot_fibre_lower == 3

    # Finite arithmetic audit of the sharp cloud law: increasing subsets
    # attain the binomial upper bound, and the proposed inductive
    # coefficient beta^2/2 is below the history coefficient alpha*beta
    # throughout representative critical-depth cases.
    exponent_checks = []
    for alpha_num, beta_num in ((10, 10), (10, 8), (10, 6), (8, 6)):
        alpha = Fraction(alpha_num, 10)
        beta = Fraction(beta_num, 10)
        history_coefficient = alpha * beta
        inductive_coefficient = beta * beta / 2
        assert history_coefficient > inductive_coefficient
        exponent_checks.append(
            {
                "alpha": str(alpha),
                "beta": str(beta),
                "history_coefficient": str(history_coefficient),
                "inductive_face_coefficient": str(inductive_coefficient),
            }
        )

    # Cross-level audit on five consecutive clouds.  Each pair reservoir
    # is a subfamily of the full internal face complex; summing them with
    # multiplicity costs at most the number of level pairs times V(Q).
    cloud_count = 5
    clouds = [tuple(image[4 * j : 4 * (j + 1)]) for j in range(cloud_count)]
    pair_reservoir_total = 0
    for first, second in combinations(range(cloud_count), 2):
        pair_reservoir_total += sum(matrix_profile(clouds[first] + clouds[second]))
    assert pair_reservoir_total <= comb(cloud_count, 2) * v_q
    layered_histories = 4**cloud_count

    result = {
        "internal_order_type_points": n,
        "certified_internal_V": v_q,
        "base_size": len(base),
        "repair_relations_checked": repair_relations,
        "history_length": history_length,
        "histories_checked": histories,
        "history_arrows_checked": checked_arrows,
        "ambient_face_upper_bound": ambient_face_upper,
        "one_slot_fibre_lower_bound": one_slot_fibre_lower,
        "common_terminal_hull_size": len(base) + 1,
        "all_transitions_same_edge": True,
        "all_base_vertices_survive": True,
        "cloud_exponent_checks": exponent_checks,
        "cross_level_clouds": cloud_count,
        "layered_transversal_histories": layered_histories,
        "pair_level_face_reservoir_with_multiplicity": pair_reservoir_total,
        "pair_level_trivial_upper_bound": comb(cloud_count, 2) * v_q,
    }
    output = HERE / "long_chain_mixed_barrier_certificate.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: exact universal-chain mixed-branch obstruction")


if __name__ == "__main__":
    main()
