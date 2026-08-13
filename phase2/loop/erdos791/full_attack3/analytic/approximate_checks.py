#!/usr/bin/env python3
"""Finite checks for approximate tiling and rank-one absorption lemmas."""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter
from pathlib import Path


def sum_counter(left: set[int], right: set[int]) -> Counter[int]:
    return Counter(x + y for x in left for y in right)


def accounting_check(through: int) -> dict[str, int]:
    checked = 0
    universe = range(through + 1)
    subsets = [
        set(values)
        for size in range(1, through + 2)
        for values in itertools.combinations(universe, size)
    ]
    for X in subsets:
        for Y in subsets:
            reps = sum_counter(X, Y)
            P = len(X) * len(Y)
            for lo in range(2 * through + 1):
                for Q in range(1, 2 * through + 2 - lo):
                    I = set(range(lo, lo + Q))
                    occupied = sum(reps[s] > 0 for s in I)
                    if not occupied:
                        continue
                    h = Q - occupied
                    lhs = sum(abs(reps[s] / P - 1 / Q) for s in I)
                    lhs += sum(count / P for s, count in reps.items() if s not in I)
                    rhs = (P - occupied) / P + h / Q + abs(P - Q) / P
                    if lhs > rhs + 1e-12:
                        raise AssertionError((X, Y, lo, Q, lhs, rhs))
                    checked += 1
    return {"accounting_instances": checked}


def jitter_check(through: int) -> dict[str, int]:
    checked = 0
    for q in range(2, through + 1):
        X = set(range(q))
        partners = []
        for a in range(q):
            Y = {0} | {j * q + a for j in range(1, q)}
            reps = sum_counter(X, Y)
            expected = set(range(q)) | set(range(q + a, q * q + a))
            if set(reps) != expected or any(value != 1 for value in reps.values()):
                raise AssertionError((q, a))
            target = set(range(q * q))
            missing = target - set(reps)
            outside = set(reps) - target
            if missing != set(range(q, q + a)):
                raise AssertionError((q, a, "missing", missing))
            if outside != set(range(q * q, q * q + a)):
                raise AssertionError((q, a, "outside", outside))
            for old in partners:
                if len(old & Y) != 1 or len(old ^ Y) != 2 * (q - 1):
                    raise AssertionError((q, a, "partner distance"))
            partners.append(Y)
            checked += 1
    return {"jitter_instances": checked}


def carry_triangle_check(through: int) -> dict[str, int]:
    checked = 0
    for q in range(2, through + 1):
        d = q - 1
        B = q * q - q + 1
        X = {d * i for i in range(q)}
        Y = set(range(q))
        Z = {0} | {1 + q * j for j in range(q - 1)}
        target = set(range(B))
        if {x + y for x in X for y in Y} != target:
            raise AssertionError((q, "XY"))
        if {y + z for y in Y for z in Z} != target:
            raise AssertionError((q, "YZ"))
        xz = {x + z for x in X for z in Z}
        low = xz & target
        high = {value - B for value in xz if value >= B}
        described_low = {
            d * a + c
            for a in range(d + 2)
            for c in range(d)
            if (c == 0 and a <= d + 1)
            or (1 <= c <= d - 1 and c - 1 <= a <= d)
        }
        described_high = {
            d * a + c
            for c in range(1, d)
            for a in range(c)
        }
        if low != described_low or high != described_high:
            raise AssertionError((q, "digit description"))
        if low | high != target:
            raise AssertionError((q, "carry union", target - (low | high)))
        if len(target - low) != (q - 2) * (q - 3) // 2:
            raise AssertionError((q, "lower holes", len(target - low)))
        if len(high) != d * (d - 1) // 2 or len(low & high) != d - 1:
            raise AssertionError((q, "footprint sizes"))
        reps = sum_counter(X, Z)
        if len(reps) != q * q - 1 or sum(reps.values()) != q * q:
            raise AssertionError((q, "raw collision count"))
        values = sorted(xz)
        left = 0
        best_count = 0
        for right, value in enumerate(values):
            while values[left] < value - B + 1:
                left += 1
            best_count = max(best_count, right - left + 1)
        best_holes = B - best_count
        if best_holes != (q - 2) * (q - 2) // 4:
            raise AssertionError((q, "best window", best_holes))
        # Put one XZ macro sum at zero and one at one.  Their high and low
        # footprints must cover the full macro block one.
        literal = xz | {B + value for value in xz}
        if not set(range(B, 2 * B)) <= literal:
            raise AssertionError((q, "literal carry"))
        checked += 1
    return {"carry_triangle_instances": checked}


def rank_one_check(through: int, random_trials: int, seed: int) -> dict[str, int]:
    checked = 0
    universe = set(range(through + 1))
    subsets = [
        set(values)
        for size in range(through + 2)
        for values in itertools.combinations(range(through + 1), size)
    ]
    # Exhaust all B and use all small U,V; define T so its old holes lie in U+V.
    for B in subsets:
        old = {x + y for x in B for y in B}
        for U in subsets:
            for V in subsets:
                rectangle = {x + y for x in U for y in V}
                T = universe & (old | rectangle)
                A = B | U | V
                new = {x + y for x in A for y in A}
                if not T <= new:
                    raise AssertionError((B, U, V, T - new))
                checked += 1

    rng = random.Random(seed)
    block_checked = 0
    for _ in range(random_trials):
        Q = rng.randint(2, 30)
        S = {j for j in range(rng.randint(1, 20)) if rng.random() < 0.5}
        R = {r for r in range(Q) if rng.random() < 0.3}
        H = {Q * j + r for j in S for r in R if rng.random() < 0.8}
        U = {Q * j for j in S}
        if not H <= {u + r for u in U for r in R}:
            raise AssertionError((Q, S, R, H))
        block_checked += 1
    return {
        "rank_one_instances": checked,
        "block_residue_instances": block_checked,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=3)
    parser.add_argument("--jitter-through", type=int, default=100)
    parser.add_argument("--random-trials", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result: dict[str, object] = {
        "status": "PASS",
        "scope": "finite identities only; compactness/Fourier theorem is proved in markdown",
        "parameters": {
            "through": args.through,
            "jitter_through": args.jitter_through,
            "random_trials": args.random_trials,
            "seed": args.seed,
        },
    }
    result.update(accounting_check(args.through))
    result.update(jitter_check(args.jitter_through))
    result.update(carry_triangle_check(args.jitter_through))
    result.update(rank_one_check(args.through, args.random_trials, args.seed))
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
