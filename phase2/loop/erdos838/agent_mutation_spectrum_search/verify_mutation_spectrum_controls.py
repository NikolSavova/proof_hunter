#!/usr/bin/env python3
"""Exact ordered-bipartition mutation spectra for four 838 controls.

This is the cheap baseline required before a sampled/evolutionary search.
Every geometric predicate uses rational arithmetic.  The four controls are:

* the exact n=8 and n=9 realizable minimizers;
* the n=8 configuration which is stable under every ordered bipartition but
  is not globally minimal; and
* the unstable twelve-point Pascal wrapper.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402


Point = tuple[Fraction, Fraction]


def is_convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True
    points = sorted(points)

    def half(sequence: list[Point]) -> list[Point]:
        answer: list[Point] = []
        for point in sequence:
            while (
                len(answer) >= 2
                and rt.determinant(answer[-2], answer[-1], point) <= 0
            ):
                answer.pop()
            answer.append(point)
        return answer

    hull = half(points)[:-1] + half(list(reversed(points)))[:-1]
    return len(hull) == len(points)


def is_chain(points: list[Point], sign: int) -> bool:
    points = sorted(points)
    return all(
        (rt.determinant(points[i], points[j], points[k]) > 0) == (sign > 0)
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def families(points: list[Point]) -> tuple[list[int], list[int], list[int]]:
    faces: list[int] = []
    caps: list[int] = []
    cups: list[int] = []
    for mask in range(1, 1 << len(points)):
        subset = [points[index] for index in range(len(points)) if mask >> index & 1]
        if is_convex(subset):
            faces.append(mask)
        if is_chain(subset, -1):
            caps.append(mask)
        if is_chain(subset, +1):
            cups.append(mask)
    return faces, caps, cups


def zeta_counts(family: list[int], n: int) -> tuple[list[int], list[int]]:
    counts = [0] * (1 << n)
    ranks = [0] * (1 << n)
    for mask in family:
        counts[mask] = 1
        ranks[mask] = mask.bit_count()
    for bit in range(n):
        flag = 1 << bit
        for mask in range(1 << n):
            if mask & flag:
                counts[mask] += counts[mask ^ flag]
                ranks[mask] += ranks[mask ^ flag]
    return counts, ranks


def quantile(sorted_values: list[int], numerator: int, denominator: int) -> int:
    index = (len(sorted_values) - 1) * numerator // denominator
    return sorted_values[index]


def spectrum(name: str, raw_points: list[Point]) -> dict:
    points = sorted(raw_points)
    n = len(points)
    assert all(
        rt.determinant(points[i], points[j], points[k]) != 0
        for i, j, k in itertools.combinations(range(n), 3)
    )
    faces, caps, cups = families(points)
    face_count, _ = zeta_counts(faces, n)
    cap_count, cap_rank = zeta_counts(caps, n)
    cup_count, cup_rank = zeta_counts(cups, n)
    value = len(faces)
    full = (1 << n) - 1

    rows = []
    by_balance: dict[int, list[int]] = defaultdict(list)
    for left in range(1 << n):
        right = full ^ left
        internal = face_count[left] + face_count[right]
        cross = cap_count[left] * cup_count[right]
        mutation = internal + cross
        slack = mutation - value
        balance = min(left.bit_count(), right.bit_count())
        by_balance[balance].append(slack)
        rows.append(
            {
                "left_mask": left,
                "left_size": left.bit_count(),
                "right_size": right.bit_count(),
                "mutation": mutation,
                "slack": slack,
                "internal": internal,
                "cross": cross,
                "cap_count": cap_count[left],
                "cup_count": cup_count[right],
                "cap_mean_rank": (
                    cap_rank[left] / cap_count[left] if cap_count[left] else 0.0
                ),
                "cup_mean_rank": (
                    cup_rank[right] / cup_count[right] if cup_count[right] else 0.0
                ),
            }
        )

    rows.sort(key=lambda row: (row["slack"], abs(row["left_size"] - n / 2), row["left_mask"]))
    slacks = sorted(row["slack"] for row in rows)
    minimum = slacks[0]
    minimum_rows = [row for row in rows if row["slack"] == minimum]
    proper_rows = [
        row for row in rows if row["left_size"] and row["right_size"]
    ]
    deep_rows = [
        row for row in rows if min(row["left_size"], row["right_size"]) >= 2
    ]
    proper_minimum = min(row["slack"] for row in proper_rows)
    deep_minimum = min(row["slack"] for row in deep_rows)
    near_rows = [row for row in rows if row["slack"] <= minimum + n]
    near_balance_histogram = Counter(
        min(row["left_size"], row["right_size"]) for row in near_rows
    )

    balance_summary = {}
    for balance, values in sorted(by_balance.items()):
        values.sort()
        balance_summary[str(balance)] = {
            "count": len(values),
            "minimum_slack": values[0],
            "median_slack": quantile(values, 1, 2),
            "decreasing": sum(value < 0 for value in values),
            "tight": sum(value == 0 for value in values),
        }

    return {
        "name": name,
        "n": n,
        "coordinates": [[str(x), str(y)] for x, y in points],
        "V_nonempty": value,
        "C_full": len(caps),
        "U_full": len(cups),
        "partition_count": 1 << n,
        "minimum_mutation": value + minimum,
        "minimum_slack": minimum,
        "decreasing_count": sum(value < 0 for value in slacks),
        "tight_count": sum(value == 0 for value in slacks),
        "proper_minimum_slack": proper_minimum,
        "proper_decreasing_count": sum(row["slack"] < 0 for row in proper_rows),
        "proper_tight_count": sum(row["slack"] == 0 for row in proper_rows),
        "deep_minimum_slack": deep_minimum,
        "deep_decreasing_count": sum(row["slack"] < 0 for row in deep_rows),
        "deep_tight_count": sum(row["slack"] == 0 for row in deep_rows),
        "near_minimum_count_within_n": len(near_rows),
        "near_minimum_balance_histogram": dict(sorted(near_balance_histogram.items())),
        "slack_quantiles": {
            "q0": slacks[0],
            "q25": quantile(slacks, 1, 4),
            "q50": quantile(slacks, 1, 2),
            "q75": quantile(slacks, 3, 4),
            "q100": slacks[-1],
        },
        "minimum_rows": minimum_rows[:32],
        "proper_minimum_rows": [
            row for row in proper_rows if row["slack"] == proper_minimum
        ][:32],
        "deep_minimum_rows": [
            row for row in deep_rows if row["slack"] == deep_minimum
        ][:32],
        "balance_summary": balance_summary,
    }


def q_block_spectrum(raw_points: list[Point], q: int) -> dict:
    """Exhaust every ordered q-colouring without materializing the rows."""
    if q < 2:
        raise ValueError("q must be at least two")
    points = sorted(raw_points)
    n = len(points)
    faces, caps, cups = families(points)
    face_count, _ = zeta_counts(faces, n)
    cap_count, _ = zeta_counts(caps, n)
    cup_count, _ = zeta_counts(cups, n)
    value = len(faces)
    masks = [0] * q
    sizes = [0] * q
    minimum: int | None = None
    decreasing = 0
    tight = 0
    deep_minimum: int | None = None
    deep_decreasing = 0
    deep_tight = 0
    minimizer_size_histogram: Counter[tuple[int, int, int]] = Counter()

    def visit(label: int) -> None:
        nonlocal minimum, decreasing, tight
        nonlocal deep_minimum, deep_decreasing, deep_tight
        if label < n:
            flag = 1 << label
            for colour in range(q):
                masks[colour] |= flag
                sizes[colour] += 1
                visit(label + 1)
                sizes[colour] -= 1
                masks[colour] ^= flag
            return
        mutation = sum(face_count[mask] for mask in masks)
        for left in range(q):
            middle = 1
            for right in range(left + 1, q):
                if right > left + 1:
                    middle *= 1 + sizes[right - 1]
                mutation += cap_count[masks[left]] * cup_count[masks[right]] * middle
        slack = mutation - value
        if minimum is None or slack < minimum:
            minimum = slack
            minimizer_size_histogram.clear()
        if slack == minimum:
            minimizer_size_histogram[tuple(sizes)] += 1
        decreasing += int(slack < 0)
        tight += int(slack == 0)
        if min(sizes) >= 1:
            if deep_minimum is None or slack < deep_minimum:
                deep_minimum = slack
            deep_decreasing += int(slack < 0)
            deep_tight += int(slack == 0)

    visit(0)
    assert minimum is not None and deep_minimum is not None
    return {
        "q": q,
        "partition_count": q**n,
        "minimum_slack": minimum,
        "decreasing_count": decreasing,
        "tight_count": tight,
        "all_blocks_nonempty_minimum_slack": deep_minimum,
        "all_blocks_nonempty_decreasing_count": deep_decreasing,
        "all_blocks_nonempty_tight_count": deep_tight,
        "minimum_size_histogram": {
            ",".join(map(str, sizes)): count
            for sizes, count in sorted(minimizer_size_histogram.items())
        },
    }


def three_block_spectrum(raw_points: list[Point]) -> dict:
    return q_block_spectrum(raw_points, 3)


def minimizer_points() -> tuple[list[Point], list[Point]]:
    source = json.loads(
        (ERDOS / "agent_lex_minimizer_search" / "certificates_and_deletions.json").read_text()
    )
    answer = []
    for key in ("n8", "n9"):
        answer.append(
            [(Fraction(x), Fraction(y)) for x, y in source[key]["coordinates_sorted"]]
        )
    return answer[0], answer[1]


def stable_trap_points() -> list[Point]:
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    wrapper = sorted(rt.strong_glue(q, q, Fraction(1, 16384)))
    carrier = [wrapper[index] for index in (0, 1, 2, 9, 6, 7)]
    padding = [
        (Fraction(89, 11), Fraction(-173, 11)),
        (Fraction(-116, 11), Fraction(49, 11)),
    ]
    return carrier + padding


def pascal_wrapper_points() -> list[Point]:
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    return sorted(rt.strong_glue(q, q, Fraction(1, 16384)))


def main() -> None:
    points8, points9 = minimizer_points()
    controls = [
        ("global_minimizer_n8", points8),
        ("global_minimizer_n9", points9),
        ("bipartition_stable_nonminimal_n8", stable_trap_points()),
        ("unstable_pascal_wrapper_n12", pascal_wrapper_points()),
    ]
    results = []
    for name, points in controls:
        row = spectrum(name, points)
        row["three_block"] = three_block_spectrum(points)
        results.append(row)

    by_name = {row["name"]: row for row in results}
    assert by_name["global_minimizer_n8"]["V_nonempty"] == 113
    assert by_name["global_minimizer_n9"]["V_nonempty"] == 168
    assert by_name["bipartition_stable_nonminimal_n8"]["V_nonempty"] == 121
    assert by_name["unstable_pascal_wrapper_n12"]["V_nonempty"] == 1061
    assert by_name["global_minimizer_n8"]["minimum_slack"] >= 0
    assert by_name["global_minimizer_n9"]["minimum_slack"] >= 0
    assert by_name["bipartition_stable_nonminimal_n8"]["minimum_slack"] == 0
    assert by_name["unstable_pascal_wrapper_n12"]["minimum_mutation"] == 688
    assert by_name["unstable_pascal_wrapper_n12"]["decreasing_count"] == 2249
    assert by_name["unstable_pascal_wrapper_n12"]["three_block"]["minimum_slack"] == -445

    for row in results:
        print(
            "%s: n=%d V=%d min=%d slack=%d decreasing=%d tight=%d "
            "proper=(%d,%d,%d) deep=(%d,%d,%d) near=%d q3=(%d,%d,%d)"
            % (
                row["name"],
                row["n"],
                row["V_nonempty"],
                row["minimum_mutation"],
                row["minimum_slack"],
                row["decreasing_count"],
                row["tight_count"],
                row["proper_minimum_slack"],
                row["proper_decreasing_count"],
                row["proper_tight_count"],
                row["deep_minimum_slack"],
                row["deep_decreasing_count"],
                row["deep_tight_count"],
                row["near_minimum_count_within_n"],
                row["three_block"]["minimum_slack"],
                row["three_block"]["decreasing_count"],
                row["three_block"]["all_blocks_nonempty_minimum_slack"],
            )
        )
    print("PASS: four exact mutation-spectrum controls")


if __name__ == "__main__":
    main()
