#!/usr/bin/env python3
"""Continuous relaxation for placewise prime-power depths in Erdős 1208.

This is an optimizer, not a proof certificate.  It treats the degree as large
enough that any fraction of the prime ideals above a completely split rational
prime may receive the next depth increment.  The resulting cost/gain frontier
is piecewise linear.  We optimize the two exponents from the prime-power master
bound over that frontier and then over the dyadic phase interval [w0, 2 w0].
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from verify_adaptive_rank17 import SPLIT_PRIMES, RAMIFIED_PRIMES


D = 0
C0 = 0.0


def local_log_gain(q: int, depth: int) -> float:
    lam = sum(q ** (-e) for e in range(depth + 1))
    return math.log((depth + 1) / lam)


def frontier(max_depth: int = 40):
    """Return cumulative (cost, gain, metadata) vertices of the LP frontier."""
    increments = []
    for prime_index, q in enumerate(SPLIT_PRIMES):
        previous = local_log_gain(q, 0)
        for depth in range(1, max_depth + 1):
            current = local_log_gain(q, depth)
            gain = current - previous
            cost = math.log(q)
            increments.append((gain / cost, cost, gain, prime_index, depth))
            previous = current
    increments.sort(reverse=True)

    # Decreasing marginal efficiency should automatically respect the prefix
    # constraint for every fixed prime.  Assert this rather than assuming it.
    used_depth = [0] * len(SPLIT_PRIMES)
    vertices = [(0.0, 0.0, None)]
    total_cost = total_gain = 0.0
    for efficiency, cost, gain, prime_index, depth in increments:
        assert depth == used_depth[prime_index] + 1
        used_depth[prime_index] = depth
        total_cost += cost
        total_gain += gain
        vertices.append(
            (
                total_cost,
                total_gain,
                (efficiency, prime_index, depth),
            )
        )
    return vertices


FRONTIER = []


def optimum_at_w(w: float):
    """Optimize max(E1,E2) on the piecewise-linear gain frontier."""
    best = (1.0, None)
    for index in range(1, len(FRONTIER)):
        l0, g0, _ = FRONTIER[index - 1]
        l1, g1, meta = FRONTIER[index]
        slope = (g1 - g0) / (l1 - l0)
        # Intersection 2L = 2w + C0 - G(L).
        candidate_l = (2 * w + C0 - g0 + slope * l0) / (2 + slope)
        for ell in (l0, min(max(candidate_l, l0), l1), l1):
            gain = g0 + slope * (ell - l0)
            e1 = ell / (2 * w)
            e2 = 0.5 + (math.log(D) + math.log(4) - gain) / (4 * w)
            alpha = max(e1, e2)
            if alpha < best[0]:
                fraction = 0.0 if l1 == l0 else (ell - l0) / (l1 - l0)
                best = (
                    alpha,
                    {
                        "cost": ell,
                        "gain": gain,
                        "e1": e1,
                        "e2": e2,
                        "segment": index,
                        "fraction": fraction,
                        "increment": meta,
                    },
                )
    return best


def worst_phase(w0: float, samples: int = 2001):
    worst = (-1.0, None, None)
    for i in range(samples):
        w = w0 * (1 + i / (samples - 1))
        alpha, data = optimum_at_w(w)
        if alpha > worst[0]:
            worst = (alpha, w, data)
    return worst


def main() -> None:
    global D, C0, FRONTIER, SPLIT_PRIMES
    parser = argparse.ArgumentParser()
    parser.add_argument("--split-primes-file", type=Path)
    parser.add_argument("--extra-ramified-prime", type=int, action="append")
    args = parser.parse_args()
    ramified_primes = list(RAMIFIED_PRIMES)
    if args.split_primes_file is not None:
        SPLIT_PRIMES = [int(q) for q in args.split_primes_file.read_text().split()]
    if args.extra_ramified_prime is not None:
        ramified_primes.extend(args.extra_ramified_prime)
    D = math.prod(ramified_primes)
    C0 = math.log(4 * D)
    FRONTIER = frontier()
    print("D", D, "log(4D)", C0)
    for w0 in (3000, 3500, 4000, 4365.9, 4800, 5200, 6000):
        alpha, w, data = worst_phase(w0, samples=101)
        print("w0", w0, "worst", alpha, "at", w, data)

    # Around the optimum the lower endpoint is on the decreasing part of the
    # envelope and the upper endpoint is on the increasing part.  Equalize
    # those two endpoint values, then separately sample the full interval.
    lo, hi = 3500.0, 8000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        low_alpha = optimum_at_w(mid)[0]
        high_alpha = optimum_at_w(2 * mid)[0]
        if low_alpha > high_alpha:
            lo = mid
        else:
            hi = mid
    w0 = (lo + hi) / 2
    low = optimum_at_w(w0)
    high = optimum_at_w(2 * w0)
    sampled = worst_phase(w0, samples=401)
    print("balanced w0", w0)
    print("lower endpoint", low)
    print("upper endpoint", high)
    print("sampled full interval worst", sampled)


if __name__ == "__main__":
    main()
