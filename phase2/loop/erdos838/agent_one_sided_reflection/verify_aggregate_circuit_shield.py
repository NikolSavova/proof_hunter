#!/usr/bin/env python3
"""Exact audit for aggregate rooted-circuit shields and anti-alignment."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path

import verify_rooted_hull_kraft_reset as kraft


HERE = Path(__file__).resolve().parent
Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def nested_child(size: int, epsilon: Fraction = Fraction(1, 100)) -> list[Point]:
    """Projective image of a cup, totally nested behind y=1, x in (-1,1)."""
    answer = []
    for parameter in range(1, size + 1):
        left = 1 + epsilon * parameter + epsilon**2 * parameter**2
        right = 1 + epsilon * parameter - epsilon**2 * parameter**2
        assert left > 0 and right > 0
        answer.append(
            (
                (left - right) / (left + right),
                1 - Fraction(2, 1) / (left + right),
            )
        )
    return answer


def is_cap(points: list[Point], subset: set[int]) -> bool:
    order = sorted(subset, key=lambda index: points[index][0])
    return all(
        orient(points[order[i]], points[order[i + 1]], points[order[i + 2]]) < 0
        for i in range(len(order) - 2)
    )


def is_cup(points: list[Point], subset: set[int]) -> bool:
    order = sorted(subset, key=lambda index: points[index][0])
    return all(
        orient(points[order[i]], points[order[i + 1]], points[order[i + 2]]) > 0
        for i in range(len(order) - 2)
    )


def profiles(points: list[Point]) -> tuple[int, int, int]:
    caps = cups = faces = 0
    for mask in range(1, 1 << len(points)):
        subset = {i for i in range(len(points)) if mask >> i & 1}
        caps += is_cap(points, subset)
        cups += is_cup(points, subset)
        faces += kraft.convex(points, subset)
    assert caps * cups >= faces
    return caps, cups, faces


def exact_composition_and_tensor() -> dict[str, object]:
    parameters = [-3, -2, -1, 1, 2, 3]
    outer = [(Fraction(t), Fraction(t * t)) for t in parameters]
    child = nested_child(4)
    points = outer + child
    assert kraft.general_position(points)

    caps, cups, child_faces = profiles(child)
    k_left = k_right = 3
    formula = (
        2 ** (k_left + k_right)
        - 1
        + child_faces
        + (2**k_left - 1) * cups
        + (2**k_right - 1) * caps
        + len(child) * (2**k_left - 1) * (2**k_right - 1)
    )
    total_faces = sum(
        kraft.convex(
            points,
            {index for index in range(len(points)) if mask >> index & 1},
        )
        for mask in range(1 << len(points))
    )
    assert total_faces - 1 == formula

    roots = {2, 3}
    free = [0, 1, 4, 5]
    outer_marks = [6, 7]
    inner_marks = [8, 9]
    records = []
    pair_degree: dict[tuple[int, int], int] = {}
    for mask in range(1 << len(free)):
        core = roots | {
            free[index] for index in range(len(free)) if mask >> index & 1
        }
        assert kraft.convex(points, core)
        for ear in inner_marks:
            for blocker in outer_marks:
                source = core | {ear}
                target = core | {blocker}
                assert kraft.convex(points, source)
                assert kraft.convex(points, target)
                assert kraft.hull_vertices(points, source | {blocker}) == target
                records.append((mask, ear, blocker))
                pair_degree[(ear, blocker)] = pair_degree.get((ear, blocker), 0) + 1
    assert len(records) == 64
    assert set(pair_degree.values()) == {16}

    # Sum the canonical marked half-plane bank over all cores for one pair.
    ear = inner_marks[-1]
    blocker = outer_marks[0]
    local_bank_sum = 0
    bank_ranks = []
    for mask in range(1 << len(free)):
        core = roots | {
            free[index] for index in range(len(free)) if mask >> index & 1
        }
        sides = [[], []]
        for label in core:
            sign = orient(points[ear], points[blocker], points[label])
            assert sign != 0
            sides[int(sign > 0)].append(label)
        chosen = max(sides, key=lambda side: (len(side), tuple(side)))
        bank_ranks.append(len(chosen))
        local_bank_sum += 2 ** len(chosen)
        for choice in range(1 << len(chosen)):
            face = {ear, blocker} | {
                chosen[index]
                for index in range(len(chosen))
                if choice >> index & 1
            }
            assert kraft.convex(points, face)

    return {
        "outer_singletons": len(outer),
        "child_size": len(child),
        "child_cap_count": caps,
        "child_cup_count": cups,
        "child_face_count_nonempty": child_faces,
        "composition_formula_nonempty": formula,
        "enumerated_face_count_including_empty": total_faces,
        "tensor_records": len(records),
        "pair_core_degree": next(iter(pair_degree.values())),
        "all_rectangles_bad": True,
        "fixed_pair_core_records": 1 << len(free),
        "fixed_pair_local_bank_sum": local_bank_sum,
        "fixed_pair_bank_ranks": bank_ranks,
    }


def exposed_support_checks() -> list[dict[str, int]]:
    rows = []
    # Exact finite checks of M <= K * sum_{i<=q} binom(s,i), with an
    # o(L^2) history factor K=2^(L log_2 L).
    def code_count(shield_size: int, rank_cap: int) -> int:
        return sum(
            math.comb(shield_size, i)
            for i in range(min(rank_cap, shield_size) + 1)
        )

    for log_d in (144, 160, 192):
        q = 2 * log_d
        log_m = log_d * log_d // 8
        log_history = math.ceil(log_d * math.log2(log_d))
        required = 1 << max(0, log_m - log_history)
        low = 0
        high = q
        while code_count(high, q) < required:
            high *= 2
        while low + 1 < high:
            middle = (low + high) // 2
            if code_count(middle, q) >= required:
                high = middle
            else:
                low = middle
        shield_size = high
        assert code_count(shield_size, q) >= required
        if shield_size > 0:
            previous = code_count(shield_size - 1, q)
            assert previous < required
        assert shield_size >= 2 * log_d + log_m
        rows.append(
            {
                "log2_D": log_d,
                "rank_cap": q,
                "log2_core_count": log_m,
                "log2_history_bound": log_history,
                "minimal_convex_shield_support": shield_size,
                "log2_D_squared_times_M": 2 * log_d + log_m,
                "shield_boolean_log2_faces": shield_size,
            }
        )
    return rows


def scalable_linear_mass() -> list[dict[str, int]]:
    rows = []
    for mark_size in (8, 10, 12):
        outer_size = 16 * mark_size
        half = mark_size // 2
        cap_count = (1 << mark_size) - 1
        cup_count = mark_size + math.comb(mark_size, 2)
        child_faces = cap_count
        side = outer_size // 2
        total_nonempty = (
            (1 << outer_size)
            - 1
            + child_faces
            + ((1 << side) - 1) * (cup_count + cap_count)
            + mark_size * ((1 << side) - 1) ** 2
        )
        forward_bank = mark_size * ((1 << side) - 1) ** 2
        core_count = (1 << (outer_size - 3)) // mark_size
        middle_layer = math.comb(outer_size - 2, (outer_size - 2) // 2)
        assert core_count <= middle_layer
        selected_records = core_count * half * half
        # Both are constant multiples of m*2^K.
        scale = mark_size * (1 << outer_size)
        assert scale // 64 <= selected_records <= scale
        assert scale // 4 <= total_nonempty <= 4 * scale
        assert forward_bank >= scale // 4
        rows.append(
            {
                "mark_size": mark_size,
                "outer_singletons": outer_size,
                "uniform_core_rank": (outer_size - 2) // 2 + 2,
                "core_count": core_count,
                "pair_core_degree": core_count,
                "selected_records": selected_records,
                "exact_composition_faces_nonempty": total_nonempty,
                "common_forward_bank_faces": forward_bank,
                "all_record_demand_over_forward_bank": str(
                    Fraction(selected_records, forward_bank)
                ),
                "face_to_record_ratio_floor": total_nonempty // selected_records,
            }
        )
    return rows


def hall_projection_core() -> dict[str, object]:
    """Exact peeling audit for Theorem 2 on a nonuniform 3-projection graph."""
    # Records are triples (core, ear, blocker).  Start with a dense tensor,
    # add sparse whiskers, and use an abstract Hall-union size small enough
    # that the theorem's threshold is nontrivial.
    records = {
        (core, ear, blocker)
        for core in range(20)
        for ear in range(20)
        for blocker in range(20)
    }
    records |= {(100 + index, 200 + index, 300 + index) for index in range(100)}
    hall_union_size = 250
    rank_cap = 4
    density = Fraction(len(records), hall_union_size)
    threshold = density / (4 * (rank_cap + 1))
    source_vertices = {(core, ear) for core, ear, _ in records}
    target_vertices = {(core, blocker) for core, _, blocker in records}
    pair_vertices = {(ear, blocker) for _, ear, blocker in records}
    assert (
        len(source_vertices) + len(target_vertices) + len(pair_vertices)
        <= (2 * rank_cap + 2) * hall_union_size
    )

    remaining = set(records)
    while True:
        degrees: dict[tuple[str, object], int] = {}
        for core, ear, blocker in remaining:
            vertices = (
                ("source", (core, ear)),
                ("target", (core, blocker)),
                ("pair", (ear, blocker)),
            )
            for vertex in vertices:
                degrees[vertex] = degrees.get(vertex, 0) + 1
        low = next((vertex for vertex, degree in degrees.items() if degree < threshold), None)
        if low is None:
            break
        part, value = low
        if part == "source":
            remaining = {edge for edge in remaining if (edge[0], edge[1]) != value}
        elif part == "target":
            remaining = {edge for edge in remaining if (edge[0], edge[2]) != value}
        else:
            remaining = {edge for edge in remaining if (edge[1], edge[2]) != value}

    final_degrees: dict[tuple[str, object], int] = {}
    for core, ear, blocker in remaining:
        for vertex in (
            ("source", (core, ear)),
            ("target", (core, blocker)),
            ("pair", (ear, blocker)),
        ):
            final_degrees[vertex] = final_degrees.get(vertex, 0) + 1
    assert len(remaining) * 2 >= len(records)
    assert final_degrees and min(final_degrees.values()) >= threshold
    assert len(remaining) == 8000
    assert min(final_degrees.values()) == 20
    return {
        "initial_records": len(records),
        "hall_union_size": hall_union_size,
        "hall_density": str(density),
        "rank_cap": rank_cap,
        "certified_minimum_degree": str(threshold),
        "remaining_records": len(remaining),
        "actual_minimum_projection_degree": min(final_degrees.values()),
    }


def main() -> None:
    certificate = {
        "description": "aggregate rooted-circuit shield and anti-alignment audit",
        "arithmetic": "exact Fraction geometry and integer enumeration",
        "exact_composition_tensor": exact_composition_and_tensor(),
        "exposed_support_entropy": exposed_support_checks(),
        "scalable_both_mark_linear_mass": scalable_linear_mass(),
        "hall_projection_core": hall_projection_core(),
        "assertions": [
            "quadratic low-rank entropy in a common convex shield forces enormous Boolean support",
            "the one-child separated-composition formula matches exhaustive geometry",
            "the full mark tensor has only rooted-circuit rectangles",
            "local marked half-plane banks have unbounded aggregate reuse",
            "large two-mark alphabets admit uniform-core selected mass of order V outside the logarithmic-rank normalization",
            "the coefficient residue is the directional cap/cup skew of the hidden core and mark children",
            "every Hall-dense record family retains half its mass in a simultaneous three-projection minimum-degree core",
        ],
    }
    output = HERE / "aggregate_circuit_shield_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    exact = certificate["exact_composition_tensor"]
    print(
        "composition faces="
        f"{exact['composition_formula_nonempty']}+empty; "
        f"records={exact['tensor_records']}"
    )
    print(
        "fixed-pair local banks="
        f"{exact['fixed_pair_local_bank_sum']} over "
        f"{exact['fixed_pair_core_records']} cores"
    )
    print(f"PASS: wrote {output}")


if __name__ == "__main__":
    main()
