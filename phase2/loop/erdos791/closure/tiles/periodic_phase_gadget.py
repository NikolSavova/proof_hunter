#!/usr/bin/env python3
"""Verify the perfect alternating-parity K/L macro gadget.

For k,h>=1, let K=2[0,k-1], L0=2k[0,h-1], and
L1=1+2k[0,h-1].  Then the phased S/T rule certifies every square
1,...,2kh-1: K+L0 is exactly the even positions and K+L1 the odd positions.
The gadget uses k+2h segments, and hence by itself has density at most 1/4.
"""

from __future__ import annotations

import argparse
import json

from phased_predicate import coverage_bits, prefix_length


def gadget(k: int, h: int) -> dict[str, set[int]]:
    if k < 1 or h < 1:
        raise ValueError("k,h must be positive")
    return {
        "I": set(),
        "J": set(),
        "K": {2 * i for i in range(k)},
        "L0": {2 * k * j for j in range(h)},
        "L1": {1 + 2 * k * j for j in range(h)},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", type=int, default=7)
    parser.add_argument("--h", type=int, default=5)
    args = parser.parse_args()
    p = gadget(args.k, args.h)
    bits = coverage_bits(p, 2 * args.k * args.h + 2)
    expected = set(range(1, 2 * args.k * args.h))
    certified = {q for q in range(2 * args.k * args.h + 2) if bits >> q & 1}
    if not expected <= certified:
        raise RuntimeError("parity gadget verification failed")
    ell = args.k + 2 * args.h
    # 2kh <= (k+2h)^2/4 is just (k-2h)^2 >= 0.
    density_gap_numerator = ell * ell - 8 * args.k * args.h
    if density_gap_numerator != (args.k - 2 * args.h) ** 2:
        raise RuntimeError("density identity failed")
    anchored = {name: set(values) for name, values in p.items()}
    anchored["I"] = {0}
    anchored["J"] = {0}
    anchored_prefix = prefix_length(coverage_bits(anchored, 2 * args.k * args.h + 2), 2 * args.k * args.h + 2)
    if anchored_prefix < 2 * args.k * args.h:
        raise RuntimeError("anchored periodic certificate failed")
    print(
        json.dumps(
            {
                "status": "PASS",
                "k": args.k,
                "h": args.h,
                "ell": ell,
                "certified_interval": [1, 2 * args.k * args.h - 1],
                "capacity_2kh": 2 * args.k * args.h,
                "m": 2 * args.k * args.h,
                "anchored_ell": ell + 2,
                "anchored_prefix": anchored_prefix,
                "quarter_bound_identity": f"(k-2h)^2={density_gap_numerator}",
                "placement": {name: sorted(values) for name, values in anchored.items()},
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
