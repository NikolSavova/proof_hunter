#!/usr/bin/env python3
"""Deletion-path probes for the integrated-activity attack on Erdos 838.

The reflection-order evaluator is polynomial rather than a subset census.  It
computes Z(t) and its logarithmic derivative at t=1 and t=1/2, so deletion
paths of moderately large realizable point sets can be tested directly.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from random import Random
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

from reflection_trace import pascal_cell  # noqa: E402


Point = tuple[int | Fraction, int | Fraction]


def slope_roots(points: Sequence[Point]) -> tuple[tuple[int, int], ...]:
    """Increasing-slope reflection order, after sorting by x."""
    points = sorted(points)
    edges = sorted(
        (
            Fraction(points[j][1] - points[i][1], points[j][0] - points[i][0]),
            i,
            j,
        )
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    for left, right in zip(edges, edges[1:]):
        if left[0] == right[0] and set(left[1:]) & set(right[1:]):
            raise ValueError("collinear triple")
    return tuple((i, j) for _, i, j in edges)


def value_and_log_derivative(
    n: int, roots: Sequence[tuple[int, int]], z: float
) -> tuple[float, float]:
    """Return the empty-inclusive Z(z) and z Z'(z).

    For each transvection, rows obey

        V_j <- V_j + z V_i,
        D_j <- D_j + z(D_i+V_i),

    where D is the logarithmic derivative.  Applying this in the forward and
    reverse reflection orders and taking their Frobenius product gives the
    convex-subset polynomial and derivative.
    """

    def product(order: Iterable[tuple[int, int]]) -> tuple[list[list[float]], list[list[float]]]:
        values = [[float(i == j) for j in range(n)] for i in range(n)]
        derivs = [[0.0] * n for _ in range(n)]
        for i, j in order:
            vi, vj = values[i], values[j]
            di, dj = derivs[i], derivs[j]
            values[j] = [b + z * a for a, b in zip(vi, vj)]
            derivs[j] = [b + z * (a + c) for a, b, c in zip(di, dj, vi)]
        return values, derivs

    cups, dcups = product(roots)
    caps, dcaps = product(reversed(roots))
    inner = dinner = 0.0
    for a, da, b, db in zip(cups, dcups, caps, dcaps):
        inner += sum(x * y for x, y in zip(a, b))
        dinner += sum(dx * y + x * dy for x, dx, y, dy in zip(a, da, b, db))
    partition = 1.0 + n * z + inner - n
    moment = n * z + dinner
    return partition, moment


def local_term(points: Sequence[Point]) -> tuple[float, float, float]:
    n = len(points)
    roots = slope_roots(points)
    z1, m1 = value_and_log_derivative(n, roots, 1.0)
    zh, mh = value_and_log_derivative(n, roots, 0.5)
    mu1, muh = m1 / z1, mh / zh
    r = math.log((n - muh) / (n - mu1))
    return r, mu1, muh


def fixed_deletion_path(points: Sequence[Point], order: Sequence[int]) -> dict[str, object]:
    """Evaluate a path whose order uses original point labels."""
    remaining = list(range(len(points)))
    rows: list[dict[str, float | int]] = []
    total = 0.0
    for deleted in order:
        current = [points[i] for i in remaining]
        r, mu1, muh = local_term(current)
        total += r
        rows.append({"m": len(current), "r": r, "m_r": len(current) * r,
                     "mu1": mu1, "muh": muh})
        remaining.remove(deleted)
    if remaining:
        raise ValueError("order did not delete every point")
    n = len(points)
    return {
        "n": n,
        "X": total,
        "log_n": math.log(n),
        "log_n_over_2": math.log(n / 2),
        "X_over_log_n": total / math.log(n),
        "rows": rows,
    }


def random_permutation_points(n: int, seed: int) -> list[Point]:
    """A generic integer perturbation of a permutation plot."""
    rng = Random(seed)
    ys = list(range(n))
    rng.shuffle(ys)
    # The quadratic term breaks all possible repeated incident slopes while a
    # large multiplier preserves the order-type of the permutation plot.
    scale = 10 * n * n + 1
    return [(i, scale * ys[i] + i * i) for i in range(n)]


def endpoint_orders(n: int) -> dict[str, list[int]]:
    return {
        "left_to_right": list(range(n)),
        "right_to_left": list(reversed(range(n))),
        "alternating_ends": [x for k in range((n + 1) // 2) for x in (k, n - 1 - k)
                              if k <= x < n - k],
    }


def main() -> None:
    saved = json.loads(
        (ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text()
    )["exact_records"]
    path_certificate = json.loads(
        (ROOT / "agent_integrated_activity" / "certificate.json").read_text()
    )["pointwise_path_counterexample"]
    points24 = list(enumerate(map(int, saved["24"]["y_at_x_0_through_23"])))
    order24 = path_certificate["deleted_original_labels"] + [
        path_certificate["last_remaining_original_label"]
    ]
    exact_replay = fixed_deletion_path(points24, order24)
    if abs(exact_replay["X"] - path_certificate["path_sum"]) > 2e-12:
        raise AssertionError("reflection evaluator disagrees with exact subset replay")

    probes: dict[str, object] = {"saved_n24_bad_path": exact_replay}

    points30 = list(enumerate(map(int, saved["30"]["y_at_x_0_through_29"])))
    greedy30 = [
        28, 1, 16, 22, 4, 23, 20, 11, 21, 8, 9, 14, 17, 12, 29,
        6, 18, 2, 7, 5, 15, 25, 0, 10, 13, 19, 3, 24, 26, 27,
    ]
    probes["saved_n30_greedy_path"] = fixed_deletion_path(points30, greedy30)

    pascal70 = sorted(pascal_cell(8, 4, Fraction(1, 1_000_003)))
    greedy70 = [
        31, 35, 32, 36, 28, 39, 33, 37, 29, 40, 25, 42, 26, 38, 22, 45,
        23, 46, 27, 41, 19, 48, 20, 47, 0, 1, 5, 2, 6, 3, 9, 7, 10, 30,
        34, 12, 65, 66, 61, 67, 62, 58, 68, 63, 59, 51, 52, 55, 53, 56,
        57, 60, 49, 64, 50, 43, 44, 15, 54, 21, 16, 4, 8, 11, 13, 17, 14,
        18, 24, 69,
    ]
    probes["central_pascal_T_8_4_greedy_path"] = fixed_deletion_path(pascal70, greedy70)

    for n in (16, 24, 32, 48, 64):
        points = random_permutation_points(n, 838 + n)
        for name, order in endpoint_orders(n).items():
            probes[f"random_permutation_n{n}_{name}"] = fixed_deletion_path(points, order)

    output = {
        "mode": "reflection_order_deletion_path_asymptotic_probe",
        "convention": "empty face included; natural logarithms",
        "probes": probes,
    }
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "certificate.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    for name, row in probes.items():
        print(name, f"X={row['X']:.9f}", f"X/log n={row['X_over_log_n']:.6f}")


if __name__ == "__main__":
    main()
