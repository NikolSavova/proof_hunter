#!/usr/bin/env python3
"""Exact diagnostics for the sharp diagonal supersaturation target.

The script has three deliberately separate checks.

1. It exhausts reduced words for w_0 through n=6 and records the minimum
   graded coefficient v_k for every k.  The reverse-product evaluator is
   imported from the independently written Gate-A code.
2. It scans balanced Pascal templates and their vertical iterates at
   k=round(log_2(n)/2), using exact integer graded recurrences.
3. It solves the finite weighted-capacity problem behind the fine-tower
   theorem in REPORT.md.  A level of log-size ell contributes at least ell
   cap/cup increment slots at the preceding prefix weight.

Only the final logarithms are floating point; all enumerators and minima are
computed over Python integers.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GATE = ROOT / "phase2" / "loop" / "erdos838" / "agent_reflection_gate"
GRADED = ROOT / "phase2" / "loop" / "erdos838" / "agent_graded_supersat"
sys.path.insert(0, str(GATE))
sys.path.insert(0, str(GRADED))

from reflection_order_gate import (  # noqa: E402
    evaluate_roots,
    fixed_x_realization,
    verify_fixed_x,
)
from graded_balanced import central_template, vertical_iterate  # noqa: E402


Root = tuple[int, int]


def exhaustive_coefficient_minima(n: int) -> dict[str, object]:
    permutation = list(range(n))
    roots: list[Root] = []
    target = n * (n - 1) // 2
    count = 0
    minima: list[int | None] = [None] * (n + 1)
    certificates: list[tuple[Root, ...] | None] = [None] * (n + 1)

    def visit(inversions: int) -> None:
        nonlocal count
        if inversions == target:
            count += 1
            evaluation = evaluate_roots(n, roots, graded=True)
            assert evaluation.graded is not None
            for k, value in enumerate(evaluation.graded):
                if value and (minima[k] is None or value < minima[k]):
                    minima[k] = value
                    certificates[k] = tuple(roots)
            return
        for position in range(n - 1):
            if permutation[position] >= permutation[position + 1]:
                continue
            left, right = permutation[position], permutation[position + 1]
            permutation[position], permutation[position + 1] = right, left
            roots.append((left, right))
            visit(inversions + 1)
            roots.pop()
            permutation[position], permutation[position + 1] = left, right

    visit(0)
    rows = []
    for k, value in enumerate(minima):
        if value is None:
            continue
        certificate = certificates[k]
        assert certificate is not None
        ys = fixed_x_realization(n, certificate)
        if ys is not None:
            assert verify_fixed_x(n, certificate, ys)
        rows.append(
            {
                "k": k,
                "minimum_v_k": value,
                "root_sequence_zero_based": [list(root) for root in certificate],
                "fixed_x_rational_y": (
                    [str(coordinate) for coordinate in ys] if ys is not None else None
                ),
            }
        )
    return {"n": n, "reduced_words": count, "coefficient_minima": rows}


def pascal_scan(max_h: int, max_depth: int) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    best: dict[str, object] | None = None
    for h in range(4, max_h + 1):
        r = math.comb(2 * h - 4, h - 2)
        for depth in range(1, max_depth + 1):
            log_n = depth * math.log2(r)
            k = round(log_n / 2)
            if k < 3:
                continue
            template = central_template(h, k)
            n, _, _, convex = vertical_iterate(template, depth, k)
            value = convex[k]
            assert n == r**depth and value > 0
            row = {
                "h": h,
                "depth": depth,
                "r": r,
                "n": n,
                "log2_n": log_n,
                "k": k,
                "log2_v_k": math.log2(value),
                "sigma": math.log2(value) / (k * k),
                "offset_k_minus_half_log2_n": k - log_n / 2,
            }
            rows.append(row)
            if best is None or float(row["sigma"]) < float(best["sigma"]):
                best = row
    assert best is not None
    return {"max_h": max_h, "max_depth": max_depth, "minimum_sigma": best, "rows": rows}


def top_slot_sum(parts: tuple[int, ...]) -> int:
    """Sum the largest L/2 prefix weights, with part ell giving ell slots."""
    total = sum(parts)
    assert total % 2 == 0
    slots: list[int] = []
    prefix = 0
    for part in parts:
        slots.extend([prefix] * part)
        prefix += part
    return sum(sorted(slots, reverse=True)[: total // 2])


def capacity_minimum(total_log: int, max_step: int) -> dict[str, object]:
    """Exhaust ordered integer compositions and minimize the top-slot sum."""
    if total_log % 2:
        raise ValueError("total_log must be even")
    best_value: int | None = None
    best_parts: tuple[int, ...] | None = None
    parts: list[int] = []

    def visit(remaining: int) -> None:
        nonlocal best_value, best_parts
        if remaining == 0:
            value = top_slot_sum(tuple(parts))
            if best_value is None or value < best_value:
                best_value = value
                best_parts = tuple(parts)
            return
        for step in range(1, min(max_step, remaining) + 1):
            parts.append(step)
            visit(remaining - step)
            parts.pop()

    visit(total_log)
    assert best_value is not None and best_parts is not None
    k = total_log // 2
    return {
        "total_log": total_log,
        "k": k,
        "max_step": max_step,
        "minimum_weight": best_value,
        "minimum_over_k_squared": best_value / (k * k),
        "minimizing_parts": list(best_parts),
        "continuum_target": 1.5,
        "deficit_from_three_halves_times_k_squared": 1.5 * k * k - best_value,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-reflection-n", type=int, default=6)
    parser.add_argument("--max-h", type=int, default=18)
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--capacity-log", type=int, default=16)
    parser.add_argument("--capacity-max-step", type=int, default=4)
    parser.add_argument("--output", type=Path, default=HERE / "certificate.json")
    args = parser.parse_args()

    result = {
        "claim_boundary": "exact finite evidence only; no unrestricted asymptotic proof",
        "reflection_orders": [
            exhaustive_coefficient_minima(n)
            for n in range(3, args.max_reflection_n + 1)
        ],
        "pascal_diagonal": pascal_scan(args.max_h, args.max_depth),
        "capacity_optimization": [
            capacity_minimum(args.capacity_log, step)
            for step in range(1, args.capacity_max_step + 1)
        ],
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "output": str(args.output),
        "reflection_last": result["reflection_orders"][-1],
        "pascal_minimum": result["pascal_diagonal"]["minimum_sigma"],
        "capacity": result["capacity_optimization"],
    }, indent=2))


if __name__ == "__main__":
    main()
