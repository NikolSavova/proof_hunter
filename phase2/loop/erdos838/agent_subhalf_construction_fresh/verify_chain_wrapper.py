#!/usr/bin/env python3
"""Exact audit of universal-chain wrappers for the upper-construction route.

The theorem being checked is elementary but useful: if X is embedded as a
strict fixed-edge insertion chain over u,v and a generic point a is put below
uv, then

    Z(X) + 2(|X|+1) <= Z({u,v,a} union X)
                         <= 6 Z(X) + 2(|X|+1).

Here Z includes the empty face.  The two exact ``|X|+1`` terms are the faces
whose guard intersection is {u,v} or {u,v,a}.  The script also iterates this
wrapper on the exact nine-point low-trace record and recomputes every profile
with rational arithmetic.  The finite rows are evidence only; the displayed
sandwich is proved for every input order type.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
CHAIN = ERDOS / "agent_cyclic_stem_hw"
APA = ERDOS / "agent_apa_rank"
for directory in (CHAIN, APA):
    sys.path.insert(0, str(directory))

from verify_insertion_chain_universality import (  # noqa: E402
    choose_lower_vertex,
    strict_shear,
    transform,
)
from verify_apa_counterexample import matrix_profile, orient, slope_roots  # noqa: E402
import reflection_order_gate as gate  # noqa: E402


Point = tuple[Fraction, Fraction]


def low_trace_nine() -> tuple[Point, ...]:
    data = json.loads(
        (ERDOS / "agent_lex_minimizer_search" / "exact_realizable_n9.json").read_text()
    )
    return tuple(sorted(tuple(map(Fraction, p)) for p in data["coordinates_as_stored"]))


def wrapper(points: tuple[Point, ...]) -> tuple[Point, ...]:
    """Projectively chain the input and add the rational three-point guard."""
    _, _, image, _ = transform(tuple(sorted(points)))
    lower = choose_lower_vertex(image)
    out = ((Fraction(-1), Fraction(0)), (Fraction(1), Fraction(0)), lower, *image)
    out = tuple(sorted(out))
    assert len(out) == len(set(out))
    assert all(orient(*triple) for triple in combinations(out, 3))
    return out


def ordered_transform(points: tuple[Point, ...]) -> tuple[Point, ...]:
    """Universality map with source and image x-orders identical.

    The usual proof is free to choose the two positive shifts C,D.  Taking
    C sufficiently large relative to D makes L_i/R_i strictly increase,
    hence x_i=(L_i-R_i)/(L_i+R_i) strictly increase.  This removes the final
    generic shear and gives an exact all-depth boundary recurrence.
    """
    ordered = tuple(sorted(points))
    _, rows = strict_shear(ordered)
    # strict_shear's returned L,R use minimal shifts.  Recover the increasing
    # a,c data, then choose our own D and search an integer C.
    # Its shear M is returned separately, so recompute directly.
    shear, _ = strict_shear(ordered)
    lifted = [(a, b + shear * a) for a, b in ordered]
    d_shift = max(c for _, c in lifted) + 1
    c_shift = max(a for a, _ in lifted) + 1
    while True:
        left_right = [(c_shift - a, d_shift - c) for a, c in lifted]
        image = tuple(
            ((left - right) / (left + right), Fraction(2, left + right))
            for left, right in left_right
        )
        if all(image[i][0] < image[i + 1][0] for i in range(len(image) - 1)):
            break
        c_shift = 2 * c_shift + 1
    assert all(
        left_right[i][0] > left_right[i + 1][0]
        and left_right[i][1] > left_right[i + 1][1]
        for i in range(len(left_right) - 1)
    )
    assert all(orient(*triple) for triple in combinations(image, 3))
    # The projective map reverses every orientation and preserves labels.
    assert all(
        (orient(image[i], image[j], image[k]) > 0)
        != (orient(ordered[i], ordered[j], ordered[k]) > 0)
        for i, j, k in combinations(range(len(image)), 3)
    )
    return image


def edge_wrapper(points: tuple[Point, ...]) -> tuple[Point, ...]:
    image = ordered_transform(points)
    out = ((Fraction(-1), Fraction(0)), *image, (Fraction(1), Fraction(0)))
    assert tuple(sorted(out)) == out
    assert all(orient(*triple) for triple in combinations(out, 3))
    return out


def boundary_totals(points: tuple[Point, ...]) -> tuple[int, int]:
    evaluation = gate.evaluate_roots(len(points), slope_roots(points), graded=False)
    # Hats include the empty chain.
    return evaluation.cap_total + 1, evaluation.cup_total + 1


def coherent_edge_rows(seed: tuple[Point, ...], depth: int = 8) -> list[dict[str, int]]:
    """Check the exact coherent-wrapper recurrence through ``depth``."""
    current = seed
    rows: list[dict[str, int]] = []
    for level in range(depth + 1):
        profile = matrix_profile(current)
        cap_hat, cup_hat = boundary_totals(current)
        row = {
            "depth": level,
            "n": len(current),
            "Z": sum(profile),
            "cap_hat": cap_hat,
            "cup_hat": cup_hat,
        }
        if rows:
            old = rows[-1]
            assert row["n"] == old["n"] + 2
            assert row["Z"] == old["Z"] + old["cap_hat"] + old["cup_hat"] + old["n"] + 1
            assert row["cap_hat"] == 2 * old["cup_hat"] + 2 * (old["n"] + 1)
            assert row["cup_hat"] == 2 * old["cap_hat"] + old["n"] + 2
        rows.append(row)
        if level < depth:
            current = edge_wrapper(current)
    return rows


def projection_chambers(points: tuple[Point, ...]) -> list[Fraction]:
    """One exact shear representative from every generic projection chamber."""
    walls = sorted({
        -(points[j][0] - points[i][0]) / (points[j][1] - points[i][1])
        for i, j in combinations(range(len(points)), 2)
        if points[j][1] != points[i][1]
    })
    if not walls:
        return [Fraction(0)]
    return [walls[0] - 1, *(
        (left + right) / 2 for left, right in zip(walls, walls[1:])
    ), walls[-1] + 1]


def shear_projection(points: tuple[Point, ...], amount: Fraction) -> tuple[Point, ...]:
    out = tuple((x + amount * y, y) for x, y in points)
    assert len({x for x, _ in out}) == len(out)
    return out


def cap_cup_hats_in_order(points: tuple[Point, ...], order: tuple[int, ...]) -> tuple[int, int]:
    """Boundary-chain totals from a projection order and cached chirotope."""
    n = len(order)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for right in range(1, n):
        for middle in range(right):
            cap[middle][right] = 1
            cup[middle][right] = 1
            for left in range(middle):
                value = orient(points[order[left]], points[order[middle]], points[order[right]])
                if value < 0:
                    cap[middle][right] += cap[left][middle]
                else:
                    cup[middle][right] += cup[left][middle]
    # Add n singletons and the empty chain.
    return 1 + n + sum(map(sum, cap)), 1 + n + sum(map(sum, cup))


def chamber_orders(points: tuple[Point, ...]) -> list[tuple[Fraction, tuple[int, ...]]]:
    """All shear-projection chambers, sorting the rational walls only once."""
    walls = sorted(
        (
            -(points[j][0] - points[i][0]) / (points[j][1] - points[i][1]),
            i,
            j,
        )
        for i, j in combinations(range(len(points)), 2)
        if points[j][1] != points[i][1]
    )
    if not walls:
        return [(Fraction(0), tuple(range(len(points))))]
    first_amount = walls[0][0] - 1
    order = sorted(
        range(len(points)), key=lambda i: points[i][0] + first_amount * points[i][1]
    )
    positions = {label: place for place, label in enumerate(order)}
    out = [(first_amount, tuple(order))]
    for index, (wall, first, second) in enumerate(walls):
        p, q = positions[first], positions[second]
        assert abs(p - q) == 1
        if p > q:
            p, q = q, p
            first, second = second, first
        order[p], order[q] = order[q], order[p]
        positions[first], positions[second] = q, p
        next_wall = walls[index + 1][0] if index + 1 < len(walls) else wall + 2
        # Equal walls come only from disjoint commuting pairs.  Wait until the
        # whole simultaneous packet has crossed before recording a chamber.
        if next_wall == wall:
            continue
        out.append(((wall + next_wall) / 2, tuple(order)))
    return out


def greedy_direction_reset_rows(seed: tuple[Point, ...], depth: int = 3) -> list[dict[str, int]]:
    """Finite kill-search: reset to the direction minimizing C_hat+U_hat."""
    current = seed
    rows: list[dict[str, int]] = []
    for level in range(depth + 1):
        profile = matrix_profile(current)
        candidates: list[tuple[int, Fraction, int, int, tuple[int, ...]]] = []
        for amount, order in chamber_orders(current):
            cap_hat, cup_hat = cap_cup_hats_in_order(current, order)
            candidates.append((cap_hat + cup_hat, amount, cap_hat, cup_hat, order))
        _, amount, cap_hat, cup_hat, _ = min(candidates, key=lambda row: row[:2])
        chosen = shear_projection(current, amount)
        assert boundary_totals(chosen) == (cap_hat, cup_hat)
        rows.append({
            "depth": level,
            "n": len(current),
            "Z": sum(profile),
            "min_cap_plus_cup_hat": cap_hat + cup_hat,
            "chosen_shear_numerator": amount.numerator,
            "chosen_shear_denominator": amount.denominator,
            "projection_chambers": len(candidates),
        })
        if level < depth:
            current = edge_wrapper(chosen)
    return rows


def guard_partition_counts(points: tuple[Point, ...]) -> dict[str, int]:
    """Directly enumerate guard intersections for a small wrapped record."""
    # wrapper() sorts its output.  Identify the guards by their exact values:
    # u,v have y=0 and the third guard is the unique point with y<0.
    guards = {i for i, (_, y) in enumerate(points) if y <= 0}
    assert len(guards) == 3
    profile_total = matrix_profile(points)

    # Direct hull test is affordable for the audited sizes (up to 15 here).
    counts: dict[str, int] = {}
    n = len(points)
    for mask in range(1 << n):
        chosen = [i for i in range(n) if mask >> i & 1]
        if len(chosen) >= 4:
            # A set is convex iff none of its points is in the convex hull of
            # the others.  Equivalently in the plane, its cyclic hull has the
            # same size.  Use the monotone-chain hull with exact orientations.
            ordered = sorted((points[i], i) for i in chosen)
            lower: list[tuple[Point, int]] = []
            for item in ordered:
                while len(lower) >= 2 and orient(lower[-2][0], lower[-1][0], item[0]) <= 0:
                    lower.pop()
                lower.append(item)
            upper: list[tuple[Point, int]] = []
            for item in reversed(ordered):
                while len(upper) >= 2 and orient(upper[-2][0], upper[-1][0], item[0]) <= 0:
                    upper.pop()
                upper.append(item)
            hull = lower[:-1] + upper[:-1]
            if len(hull) != len(chosen):
                continue
        label = ",".join(map(str, sorted(guards.intersection(chosen)))) or "none"
        counts[label] = counts.get(label, 0) + 1
    assert sum(counts.values()) == sum(profile_total)
    return counts


def main() -> None:
    current = low_trace_nine()
    rows: list[dict[str, object]] = []
    # Two wrappers keep direct enumeration modest; a third exact profile is
    # still computed by the reflection-order matrix evaluator.
    for depth in range(4):
        profile = matrix_profile(current)
        row: dict[str, object] = {
            "wrapper_depth": depth,
            "n": len(current),
            "profile_including_empty": list(profile),
            "Z": sum(profile),
        }
        if depth:
            previous_Z = rows[-1]["Z"]
            previous_n = rows[-1]["n"]
            assert isinstance(previous_Z, int) and isinstance(previous_n, int)
            lower_bound = previous_Z + 2 * (previous_n + 1)
            upper_bound = 6 * previous_Z + 2 * (previous_n + 1)
            assert lower_bound <= sum(profile) <= upper_bound
            row["universal_lower_bound"] = lower_bound
            row["universal_upper_bound"] = upper_bound
            if len(current) <= 15:
                row["guard_intersection_counts"] = guard_partition_counts(current)
        rows.append(row)
        if depth < 3:
            current = wrapper(current)

    output = {
        "claim": "strict-chain guard wrapper sandwich and finite exact iteration",
        "rows": rows,
        "coherent_edge_wrapper_rows": coherent_edge_rows(low_trace_nine()),
        "greedy_direction_reset_rows": greedy_direction_reset_rows(low_trace_nine()),
    }
    (HERE / "chain_wrapper_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
