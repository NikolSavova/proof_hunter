#!/usr/bin/env python3
"""Exhaust the integrated-variance deletion path through seven wires."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path[:0] = [str(ROOT / "agent_reflection_gate"), str(ROOT / "agent_global_braid_plateau")]

import plateau_census as plateau  # noqa: E402
import reflection_order_gate as gate  # noqa: E402


def basic(n: int, roots: tuple[tuple[int, int], ...]) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    evaluation = gate.evaluate_roots(n, roots, graded=True)
    profile = (1,) + evaluation.graded[1:]
    z1 = Fraction(sum(profile))
    zh = sum((Fraction(a, 2**k) for k, a in enumerate(profile)), Fraction(0))
    mu1 = sum((Fraction(k * a) for k, a in enumerate(profile)), Fraction(0)) / z1
    muh = sum((Fraction(k * a, 2**k) for k, a in enumerate(profile)), Fraction(0)) / zh
    return z1, zh, mu1, muh


@lru_cache(maxsize=None)
def path_terms(n: int, roots: tuple[tuple[int, int], ...]) -> tuple[float, float, float, float, float]:
    """Return L, mean R, mean KL, minimum path sum, maximum path sum."""
    if n == 0:
        return 0.0, 0.0, 0.0, 0.0, 0.0
    z1, zh, mu1, muh = basic(n, roots)
    children = []
    for deleted in range(n):
        child_roots = tuple(
            (i - (i > deleted), j - (j > deleted))
            for i, j in roots
            if i != deleted and j != deleted
        )
        child_basic = basic(n - 1, child_roots) if n > 1 else (Fraction(1),) * 4
        children.append((child_roots, child_basic))
    sum1 = sum((row[1][0] for row in children), Fraction(0))
    sumh = sum((row[1][1] for row in children), Fraction(0))
    r = math.log(float((n - muh) / (n - mu1)))
    d = 0.0
    er = ek = 0.0
    path_min, path_max = math.inf, -math.inf
    for child_roots, row in children:
        q1 = float(row[0] / sum1)
        qh = float(row[1] / sumh)
        _, rr, kk, child_min, child_max = path_terms(n - 1, child_roots)
        d += qh * math.log(qh / q1)
        er += qh * rr
        ek += qh * kk
        path_min = min(path_min, child_min)
        path_max = max(path_max, child_max)
    L = math.log(float(z1 / zh))
    R, K = r + er, d + ek
    if abs(R + K - L) > 3e-12:
        raise AssertionError((n, R, K, L))
    return L, R, K, r + path_min, r + path_max


def main() -> None:
    rows = []
    for n in range(3, 8):
        words, _, _ = plateau.enumerate_graph(n)
        minimum = None
        minimum_word = None
        maximum_path_kl = 0.0
        minimum_over_orders_and_paths = None
        for word in words:
            roots = gate.root_sequence(n, word)
            L, R, K, path_min, _ = path_terms(n, roots)
            if minimum is None or R < minimum:
                minimum, minimum_word = R, word
            maximum_path_kl = max(maximum_path_kl, K)
            if minimum_over_orders_and_paths is None or path_min < minimum_over_orders_and_paths:
                minimum_over_orders_and_paths = path_min
        target = math.log(n / 2)
        if minimum is None or minimum < target - 3e-12:
            raise AssertionError("integrated path target failed in exhaustive range")
        if minimum_over_orders_and_paths is None or minimum_over_orders_and_paths < target - 3e-12:
            raise AssertionError("pointwise path target failed in exhaustive range")
        rows.append(
            {
                "n": n,
                "commutation_classes": len(words),
                "minimum_path_integrated_variance": minimum,
                "target_log_n_over_2": target,
                "slack": minimum - target,
                "maximum_path_KL": maximum_path_kl,
                "minimum_over_orders_and_deletion_paths": minimum_over_orders_and_paths,
                "minimizing_word_zero_based": list(minimum_word),
            }
        )
        print(n, len(words), f"minR={minimum:.12f}",
              f"minPath={minimum_over_orders_and_paths:.12f}", f"target={target:.12f}")
    output = {
        "mode": "exhaustive_type_A_integrated_variance_path",
        "scope": "all reflection-order commutation classes through n=7",
        "rows": rows,
        "cached_restriction_states": path_terms.cache_info().currsize,
    }
    path = HERE / "exhaustive_certificate.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
