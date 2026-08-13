#!/usr/bin/env python3
"""Search adaptive prime-power sieves for the fixed explicit 2-tower.

For a dyadic field degree m, put s=log(n)/m.  Unlike the single-sieve proof,
we may choose the prime-power depths as a function of s.  This script builds
the natural chain of depth vectors obtained by sorting their marginal
log(H)/log(M) gains, and searches the lower envelope of their master-bound
exponents over a full dyadic phase interval [S,2S].

The floating-point search is exploratory.  A claimed theorem must use a
separate interval certificate with outward rounding or explicit slack.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from verify_explicit import RAMIFIED_PRIMES, SPLIT_PRIMES


def configurations(split_primes, max_depth: int = 20):
    increments = []
    for i, q in enumerate(split_primes):
        for k in range(max_depth):
            gain = math.log((k + 2) / (k + 1)) / math.log(q)
            increments.append((gain, i, k))
    increments.sort(reverse=True)

    depths = [0] * len(split_primes)
    answer = []
    for _, i, old_depth in increments:
        if depths[i] != old_depth:
            continue
        depths[i] += 1
        log_m = sum(k * math.log(q) for q, k in zip(split_primes, depths))
        log_h = sum(math.log(k + 1) for k in depths)
        log_lambda = sum(
            math.log(sum(q ** (-e) for e in range(k + 1)))
            for q, k in zip(split_primes, depths)
        )
        answer.append((log_m, log_h, log_lambda, tuple(depths)))
    return answer


def exponent(s: float, config, d: int) -> float:
    log_m, log_h, log_lambda, _ = config
    log_d = math.log(d)
    # R>=M is exactly 2 log(M)<=log(D)+s.
    if 2 * log_m > log_d + s:
        return math.inf
    z = 2 * log_m - log_d - s
    log_bracket = math.log(4 + math.exp(z))
    first = log_m / s
    second = 0.5 + (log_d + log_lambda - log_h + log_bracket) / (2 * s)
    return max(first, second)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--split-primes-file", type=Path)
    parser.add_argument("--extra-ramified-prime", type=int)
    args = parser.parse_args()

    split_primes = SPLIT_PRIMES
    ramified_primes = RAMIFIED_PRIMES
    if args.split_primes_file is not None:
        split_primes = tuple(
            int(q) for q in args.split_primes_file.read_text().split()
        )
    if args.extra_ramified_prime is not None:
        ramified_primes = (*ramified_primes, args.extra_ramified_prime)
    d = math.prod(ramified_primes)
    configs = configurations(split_primes)
    best = (math.inf, None)
    # Coarse discovery search only.
    for base in range(7_800, 8_501, 20):
        worst = max(
            min(exponent(base * (1 + j / 400), c, d) for c in configs)
            for j in range(401)
        )
        if worst < best[0]:
            best = (worst, base)
    print(f"exploratory worst exponent = {best[0]:.15f}")
    print(f"exploratory phase base S = {best[1]}")
    print("NOT A CERTIFICATE: rigorous interval covering is still required")


if __name__ == "__main__":
    main()
