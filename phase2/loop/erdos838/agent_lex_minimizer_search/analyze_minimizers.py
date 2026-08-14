#!/usr/bin/env python3
"""Independently verify the n=8,9 lex minima and analyze their deletions.

The input n=8 core certificate comes from ``exact_bruhat.cpp``.  The n=9
coordinates come from the exhaustive realizable-order-type scan.  All slopes,
partition functions, moments, variances, and deletion identities below use
Python integers/Fractions and the independent reflection-order evaluator.
"""

from __future__ import annotations

import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402


KNOWN_LEX = {
    2: (3, 4),
    3: (7, 12),
    4: (14, 28),
    5: (26, 59),
    6: (44, 108),
    7: (72, 190),
    8: (113, 316),
    9: (168, 492),
}


def frac(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def evaluate_coordinates(raw_points: list[tuple[Fraction, Fraction]]) -> dict:
    points = sorted(raw_points)
    n = len(points)
    slopes = sorted(
        (
            (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(n)
        for j in range(i + 1, n)
    )
    roots = tuple((i, j) for _, i, j in slopes)
    word = gate.word_from_roots(n, roots)
    evaluation = gate.evaluate_word(n, word, graded=True)
    profile = list(evaluation.graded or ())
    raw2 = sum(k * k * count for k, count in enumerate(profile))
    V, M = evaluation.trace, evaluation.first_moment
    variance = Fraction(raw2, V) - Fraction(M, V) ** 2
    weighted_deletion_mean = Fraction(n * M - raw2, n * V - M)
    variance_gap = Fraction(M, V) - weighted_deletion_mean
    if variance_gap != variance / (Fraction(n) - Fraction(M, V)):
        raise AssertionError("variance/deletion identity failed")
    return {
        "n": n,
        "coordinates_sorted": [[str(x), str(y)] for x, y in points],
        "word_zero_based": list(word),
        "root_sequence_zero_based": [list(root) for root in roots],
        "evaluation": evaluation.summary(),
        "second_raw_moment_sum_k2_vk": raw2,
        "variance": frac(variance),
        "variance_decimal": float(variance),
        "weighted_deletion_mean": frac(weighted_deletion_mean),
        "mu_minus_weighted_deletion_mean": frac(variance_gap),
    }


def with_deletions(points: list[tuple[Fraction, Fraction]]) -> dict:
    result = evaluate_coordinates(points)
    n = len(points)
    rows = []
    for omitted in range(n):
        child_points = sorted(points)[:omitted] + sorted(points)[omitted + 1 :]
        child = evaluate_coordinates(child_points)
        evaluation = child["evaluation"]
        V, M = int(evaluation["trace"]), int(evaluation["first_moment"])
        rows.append(
            {
                "omitted_sorted_index": omitted,
                "omitted_point": [str(x) for x in sorted(points)[omitted]],
                "trace": V,
                "first_moment": M,
                "profile": evaluation["graded"],
                "excess_over_global_minimum": V - KNOWN_LEX[n - 1][0],
                "is_lex_minimum_child": (V, M) == KNOWN_LEX[n - 1],
            }
        )
    V, M = int(result["evaluation"]["trace"]), int(result["evaluation"]["first_moment"])
    raw2 = int(result["second_raw_moment_sum_k2_vk"])
    if sum(row["trace"] for row in rows) != n * V - M:
        raise AssertionError("zeroth deletion identity failed")
    if sum(row["first_moment"] for row in rows) != n * M - raw2:
        raise AssertionError("first deletion identity failed")
    result["deletions"] = rows
    result["deletion_summary"] = {
        "trace_histogram": dict(sorted(Counter(row["trace"] for row in rows).items())),
        "lex_pair_histogram": {
            f"{v},{m}": c
            for (v, m), c in sorted(
                Counter((row["trace"], row["first_moment"]) for row in rows).items()
            )
        },
        "sum_deletion_traces": sum(row["trace"] for row in rows),
        "minimum_possible_sum": n * KNOWN_LEX[n - 1][0],
        "total_excess_over_minimum": sum(
            row["excess_over_global_minimum"] for row in rows
        ),
        "lex_minimum_child_count": sum(row["is_lex_minimum_child"] for row in rows),
    }
    return result


def main() -> None:
    core8 = json.loads((HERE / "exact_n8_core.json").read_text())
    word8 = tuple(core8["word_zero_based"])
    cert8 = gate.make_certificate(8, word8)
    if cert8["fixed_x_status"] != "rational_certificate":
        raise AssertionError("n=8 lex winner lost its realization certificate")
    points8 = [
        (Fraction(i), Fraction(y))
        for i, y in enumerate(cert8["fixed_x_rational_y"])
    ]
    data9 = json.loads((HERE / "exact_realizable_n9.json").read_text())
    points9 = [tuple(map(Fraction, point)) for point in data9["coordinates_as_stored"]]
    result8 = with_deletions(points8)
    result9 = with_deletions(points9)
    assert (result8["evaluation"]["trace"], result8["evaluation"]["first_moment"]) == KNOWN_LEX[8]
    assert (result9["evaluation"]["trace"], result9["evaluation"]["first_moment"]) == KNOWN_LEX[9]
    output = {
        "mode": "exact_rational_certificate_and_deletion_analysis",
        "known_lex_minima_V_M": {str(n): list(pair) for n, pair in KNOWN_LEX.items()},
        "n8": result8,
        "n9": result9,
    }
    (HERE / "certificates_and_deletions.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    for key, result in [("n8", result8), ("n9", result9)]:
        print(
            key,
            result["evaluation"]["trace"],
            result["evaluation"]["first_moment"],
            result["variance"],
            result["deletion_summary"],
        )


if __name__ == "__main__":
    main()
