#!/usr/bin/env python3
"""Exact arithmetic audit for the total-V-capped cut-kernel lane.

The mathematical report separates proved statements from the square-root
collision conjecture.  This script verifies the numerical constants and
tests that conjecture on several exact stretchable and reflection-order
families.  It is evidence only for the conjectural inequality.
"""

from __future__ import annotations

import itertools
import json
import math
import random
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT_838 = HERE.parent
sys.path.insert(0, str(ROOT_838 / "agent_tangent_pruning"))
sys.path.insert(0, str(ROOT_838 / "agent_reflection_gate"))
sys.path.insert(0, str(ROOT_838 / "agent_capped_collision"))

from attack_search import (  # noqa: E402
    alternating_least_index,
    cut_summary,
    product,
    random_integral_points,
    slope_order,
    trace,
)
from reflection_order_gate import random_reduced_word, root_sequence  # noqa: E402
import capped_counterfamily as padded  # noqa: E402


def entropy_mass(a: float, b: float) -> float:
    """The homogeneous binary entropy E(a,b), with base-two logarithms."""
    total = a + b
    if total == 0:
        return 0.0
    answer = 0.0
    if a:
        answer += a * math.log2(total / a)
    if b:
        answer += b * math.log2(total / b)
    return answer


def directional_floor(alpha: float, global_cap: float) -> float:
    """Solve E(global_cap,beta)=alpha^2/4 for beta in [0,global_cap]."""
    target = alpha * alpha / 4
    if entropy_mass(global_cap, global_cap) < target:
        raise ValueError("the proposed cap is below the cap-cup entropy bound")
    low, high = 0.0, global_cap
    for _ in range(120):
        middle = (low + high) / 2
        if entropy_mass(global_cap, middle) < target:
            low = middle
        else:
            high = middle
    return high


def solve_cut_fixed_point(multiplier: float) -> float:
    """Solve w=multiplier*beta_1(w), for the arithmetic audit."""
    low, high = 0.125, 0.5
    for _ in range(120):
        middle = (low + high) / 2
        if multiplier * directional_floor(1.0, middle) > middle:
            low = middle
        else:
            high = middle
    return high


def full_trace(n: int, order: list[tuple[int, int, int]]) -> int:
    cups = product(n, order)
    caps = product(n, reversed(order))
    return trace(cups, caps, range(n), range(n))


def orientation(points: list[tuple[Fraction, Fraction]], i: int, j: int, k: int) -> int:
    value = (
        (points[j][0] - points[i][0]) * (points[k][1] - points[i][1])
        - (points[j][1] - points[i][1]) * (points[k][0] - points[i][0])
    )
    if value == 0:
        raise ValueError("collinear certificate")
    return 1 if value > 0 else -1


def is_convex(points: list[tuple[Fraction, Fraction]], indices: set[int]) -> bool:
    """Check whether every selected point is a vertex of the strict hull."""
    if len(indices) <= 3:
        return True
    ordered = sorted((points[i][0], points[i][1], i) for i in indices)

    def cross(a: tuple[Fraction, Fraction, int], b: tuple[Fraction, Fraction, int],
              c: tuple[Fraction, Fraction, int]) -> Fraction:
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    lower: list[tuple[Fraction, Fraction, int]] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[tuple[Fraction, Fraction, int]] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return len(lower[:-1] + upper[:-1]) == len(indices)


def naive_uncrossing_counterexample() -> dict[str, object]:
    ys = [780092246, 375868377, 732272728, -441108479, 718948642]
    points = [(Fraction(i), Fraction(y)) for i, y in enumerate(ys)]
    cup = [0, 1, 4]
    cap = [0, 2, 3]
    assert orientation(points, *cup) == 1
    assert orientation(points, *cap) == -1
    union = set(cup) | set(cap)
    assert not is_convex(points, union)
    assert not is_convex(points, union - {cup[-1]})
    assert not is_convex(points, union - {cap[-1]})
    return {
        "ys": ys,
        "cut": 3,
        "cup": cup,
        "cap": cap,
        "union_convex": False,
        "delete_cup_terminal_convex": False,
        "delete_cap_terminal_convex": False,
    }


def collision_record(
    family: str, n: int, order: list[tuple[int, int, int]], cut: int
) -> dict[str, object]:
    summary = cut_summary(n, order, cut)
    value = full_trace(n, order)
    rho = Fraction(int(summary["collision_num"]), int(summary["collision_den"]))
    square_root_bits = (
        math.log2(rho.numerator) - math.log2(rho.denominator)
        + 0.5 * math.log2(value)
    )
    return {
        "family": family,
        "n": n,
        "cut": cut,
        "V": value,
        "rho": str(rho),
        "log2_rho_sqrt_V": square_root_bits,
    }


def permutation_minima(max_n: int = 7) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for n in range(4, max_n + 1):
        best: dict[str, object] | None = None
        accepted = 0
        for ys in itertools.permutations(range(n)):
            points = [(Fraction(i), Fraction(y)) for i, y in enumerate(ys)]
            try:
                order = slope_order(points)
            except ValueError:
                continue
            accepted += 1
            candidate = collision_record("permutation_height", n, order, n // 2)
            if best is None or candidate["log2_rho_sqrt_V"] < best["log2_rho_sqrt_V"]:
                best = {**candidate, "ys": list(ys)}
        assert best is not None
        assert float(best["log2_rho_sqrt_V"]) > 0
        records.append({**best, "accepted": accepted})
    return records


def reflection_samples() -> list[dict[str, object]]:
    rng = random.Random(838_2026)
    records: list[dict[str, object]] = []
    for n, trials in ((8, 500), (10, 500), (12, 500), (16, 250)):
        best: dict[str, object] | None = None
        for _ in range(trials):
            roots = root_sequence(n, random_reduced_word(n, rng))
            order = [(rank, i, j) for rank, (i, j) in enumerate(roots)]
            candidate = collision_record("reflection_order", n, order, n // 2)
            if best is None or candidate["log2_rho_sqrt_V"] < best["log2_rho_sqrt_V"]:
                best = candidate
        assert best is not None
        assert float(best["log2_rho_sqrt_V"]) > 0
        records.append({**best, "trials": trials})
    return records


def alternating_records() -> list[dict[str, object]]:
    records = []
    for n in (8, 12, 20, 30, 40, 60, 80):
        points = alternating_least_index(n)
        record = collision_record("least_index_alternating", n, slope_order(points), n // 2)
        assert float(record["log2_rho_sqrt_V"]) > 0
        records.append(record)
    return records


def padded_records() -> list[dict[str, object]]:
    records = []
    for h, r in ((4, 3), (6, 4), (8, 5)):
        points, _, _ = padded.realize(h, r)
        order = slope_order(points)
        record = collision_record("padded_alternating", len(points), order, len(points) // 2)
        assert float(record["log2_rho_sqrt_V"]) > 0
        records.append({**record, "h": h, "r": r})
    return records


def main() -> None:
    beta_half = directional_floor(1.0, 0.5)
    assert abs(entropy_mass(0.5, beta_half) - 0.25) < 1e-14
    arithmetic = {
        "beta_alpha1_global_cap_half": beta_half,
        "polynomial_collision_entropy_fixed_point": solve_cut_fixed_point(2.0),
        "sqrtV_collision_entropy_fixed_point": solve_cut_fixed_point(4.0 / 3.0),
        "hypothetical_half_marginal_plus_polynomial_collision": 1.0 / 3.0,
        "hypothetical_half_marginal_plus_sqrtV_collision": 2.0 / 7.0,
    }
    evidence = {
        "permutation_height_exhaustive": permutation_minima(),
        "reflection_order_random": reflection_samples(),
        "least_index_alternating": alternating_records(),
        "padded_alternating": padded_records(),
    }
    output = {
        "status": "PASS",
        "arithmetic": arithmetic,
        "square_root_collision_is_conjectural": True,
        "naive_uncrossing_counterexample": naive_uncrossing_counterexample(),
        "evidence": evidence,
    }
    path = HERE / "certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": "PASS",
        "beta_half": beta_half,
        "minimum_evidence_bits": min(
            float(item["log2_rho_sqrt_V"])
            for group in evidence.values()
            for item in group
        ),
        "certificate": str(path),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
