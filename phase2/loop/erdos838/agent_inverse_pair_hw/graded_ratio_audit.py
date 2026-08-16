#!/usr/bin/env python3
"""Exact finite audit of normalized rank-extension ratios p_r.

The default run replays saved adversarial reflection orders and exact balanced
Pascal towers.  ``--exhaustive-small`` additionally scans every commutation
class through n=6 (908 classes at n=6).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


gate = load_module(
    "reflection_order_gate_for_ratio_audit",
    ROOT / "agent_reflection_gate" / "reflection_order_gate.py",
)
balanced = load_module(
    "graded_balanced_for_ratio_audit",
    ROOT / "agent_graded_supersat" / "graded_balanced.py",
)


def coefficient(profile, r):
    return profile[r] if r < len(profile) else 0


def p_ratio(n, profile, r):
    assert 0 <= r < n and coefficient(profile, r) > 0
    return Fraction((r + 1) * coefficient(profile, r + 1), (n - r) * coefficient(profile, r))


def exponent(p, r):
    if p == 0:
        return math.inf
    return -(math.log2(p.numerator) - math.log2(p.denominator)) / r


def saved_reflection_orders():
    expected = {
        20: [1, 20, 190, 1140, 2401, 853, 145, 8],
        24: [1, 24, 276, 2024, 5364, 2619, 418, 43, 3],
        30: [1, 30, 435, 4060, 13973, 10426, 3145, 484, 30],
    }
    print("saved exact adversarial reflection orders")
    for n in (20, 24, 30):
        path = ROOT / "agent_coxeter_half_weight" / f"seeded_n{n}.json"
        record = json.loads(path.read_text())
        evaluation = gate.evaluate_word(n, record["word_zero_based"], graded=True)
        profile = list(evaluation.graded)
        profile[0] += 1  # the gate normalization omits the empty set
        assert profile == expected[n]
        rows = []
        for r in range(3, math.floor(math.log2(n)) + 1):
            p = p_ratio(n, profile, r)
            rows.append(
                f"r={r}: p={p} ({float(p):.9g}), 2^r p={float((2**r)*p):.6g}, exponent={exponent(p,r):.6f}"
            )
        print(f"  n={n}, profile={profile}")
        print("    " + "; ".join(rows))


def balanced_towers():
    print("balanced Pascal towers at r=floor(log2 n)")
    for h, depth in ((6, 4), (10, 4), (16, 4)):
        template_size = math.comb(2 * h - 4, h - 2)
        n = template_size**depth
        r = math.floor(math.log2(n))
        template = balanced.central_template(h, r + 1)
        actual_n, _, _, profile = balanced.vertical_iterate(template, depth, r + 1)
        assert actual_n == n
        p = p_ratio(n, profile, r)
        capacity = 2 * (h - 2)
        predicted_exponent = math.log2(template_size) / capacity
        print(
            f"  h={h}, depth={depth}, r={r}, exponent={exponent(p,r):.6f}, "
            f"template log2(size)/capacity={predicted_exponent:.6f}, "
            f"log2(2^r p)/r={1-exponent(p,r):.6f}"
        )


def exhaustive_small():
    print("complete commutation-class scan")
    for n in range(4, 7):
        initial = gate.canonical_commutation_word(gate.bubble_word(n))
        queue = [initial]
        seen = {initial}
        cursor = 0
        minima = {r: None for r in range(3, n)}
        witnesses = {}
        while cursor < len(queue):
            word = queue[cursor]
            cursor += 1
            profile = gate.evaluate_word(n, word, graded=True).graded
            for r in minima:
                if coefficient(profile, r) == 0:
                    continue
                p = p_ratio(n, profile, r)
                if minima[r] is None or p < minima[r]:
                    minima[r] = p
                    witnesses[r] = profile
            for neighbor in gate.braid_neighbors_mod_commutation(n, word):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        print(f"  n={n}, classes={len(seen)}")
        for r, p in minima.items():
            print(f"    r={r}, min p={p}, 2^r p={2**r*p}, profile={witnesses[r]}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exhaustive-small", action="store_true")
    args = parser.parse_args()
    saved_reflection_orders()
    balanced_towers()
    if args.exhaustive_small:
        exhaustive_small()


if __name__ == "__main__":
    main()
