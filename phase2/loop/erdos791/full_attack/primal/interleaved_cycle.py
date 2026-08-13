#!/usr/bin/env python3
"""A genuine interleaved finite-state phase cycle and its exact 1/4 bound.

The same L0/L1 placements first pair alternately with K, then pair with I in
the next macro block.  Thus this is not a serial/disjoint gadget: L is reused.
It nevertheless has density at most 1/4.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phased_predicate import coverage_bits, prefix_length


def construct(k: int, h: int) -> tuple[dict[str, set[int]], int, int]:
    if k < 1 or h < 2:
        raise ValueError("require k>=1 and h>=2")
    M = 2 * k * h
    p = {
        "I": {2 * i for i in range(k)},
        "J": set(),
        "K": {M + 2 * i for i in range(k)},
        "L0": {2 * k * j for j in range(h)},
        "L1": {1 + 2 * k * j for j in range(h)},
    }
    ell = 2 * k + 2 * h
    m = 2 * M
    return p, ell, m


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=10)
    parser.add_argument("--h", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    p, ell, m = construct(args.k, args.h)
    prefix = prefix_length(coverage_bits(p, m + 64), m + 64)
    if prefix != m:
        raise RuntimeError(f"expected exact prefix {m}, got {prefix}")
    # m/ell^2 <= 1/4 follows exactly from (k-h)^2>=0.
    quarter_gap = ell * ell - 4 * m
    if quarter_gap != 4 * (args.k - args.h) ** 2:
        raise RuntimeError("quarter-density identity failed")
    result = {
        "status": "PASS",
        "family": "interleaved-two-edge-phase-cycle",
        "k": args.k,
        "h": args.h,
        "M": 2 * args.k * args.h,
        "ell": ell,
        "m": m,
        "abstract_prefix": prefix,
        "ratio": f"{m}/{ell * ell}",
        "quarter_bound_identity": f"ell^2-4m=4(k-h)^2={quarter_gap}",
        "placement": {name: sorted(values) for name, values in p.items()},
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
