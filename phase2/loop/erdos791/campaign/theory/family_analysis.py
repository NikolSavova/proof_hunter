#!/usr/bin/env python3
"""Exact analysis of the block family underlying Kohonen's 42/510 placement.

The parameters are h >= 1, b >= h+1, n >= h, and r >= 0.  The sets are

    I = {0,h} union (u + h*[0,b-1])
    J = 2h + (h+1)*[0,n-1]
    K = [0,h-1] union union_{s=0}^{r-1} [B_s,B_s+h]

where u=(h+1)n+2h, B_0=2u+h(b-h-1), and successive B_s differ by
D=u+hb+1.  The elementary interval calculation in THEORY_NOTES.md proves
that this placement certifies [0,m-1], with

    ell = n+b+h+2+r(h+1),
    m = 2u+h(b-h-1)+r(u+hb+1).

This script independently constructs every set and checks the tile predicate.
It also exhausts a user-selected finite parameter box and compares with 85/294.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from verifier import prefix_length, tile_coverage  # noqa: E402


def placement(h: int, b: int, n: int, r: int) -> dict[str, object]:
    if h < 1 or b < h + 1 or n < h or r < 0:
        raise ValueError("need h>=1, b>=h+1, n>=h, r>=0")
    u = (h + 1) * n + 2 * h
    first = 2 * u + h * (b - h - 1)
    delta = u + h * b + 1
    I = sorted({0, h} | {u + h * i for i in range(b)})
    J = [2 * h + (h + 1) * j for j in range(n)]
    K = list(range(h))
    for block in range(r):
        start = first + block * delta
        K.extend(range(start, start + h + 1))
    ell = len(I) + len(J) + len(K)
    claimed_m = first + r * delta
    actual_m = prefix_length(tile_coverage(I, J, K))
    if actual_m < claimed_m:
        raise AssertionError((h, b, n, r, claimed_m, actual_m))
    return {
        "I": I,
        "J": J,
        "K": K,
        "ell": ell,
        "m": claimed_m,
        "actual_tile_prefix": actual_m,
        "parameters": {"h": h, "b": b, "n": n, "r": r},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-ell", type=int, default=100)
    parser.add_argument("--emit-kohonen", type=Path)
    args = parser.parse_args()

    record = Fraction(85, 294)
    best: tuple[Fraction, dict[str, object]] | None = None
    wins: list[dict[str, object]] = []
    checked = 0
    for h in range(1, args.max_ell):
        for r in range(args.max_ell // (h + 1) + 1):
            for b in range(h + 1, args.max_ell):
                max_n = args.max_ell - b - h - 2 - r * (h + 1)
                if max_n < h:
                    break
                for n in range(h, max_n + 1):
                    ell = n + b + h + 2 + r * (h + 1)
                    u = (h + 1) * n + 2 * h
                    m = 2 * u + h * (b - h - 1) + r * (u + h * b + 1)
                    ratio = Fraction(m, ell * ell)
                    checked += 1
                    row = {
                        "h": h,
                        "b": b,
                        "n": n,
                        "r": r,
                        "ell": ell,
                        "m": m,
                        "ratio": str(ratio),
                    }
                    if best is None or ratio > best[0]:
                        best = ratio, row
                    if ratio > record:
                        wins.append(row)

    kohonen = placement(5, 6, 17, 2)
    if args.emit_kohonen:
        args.emit_kohonen.write_text(json.dumps(kohonen, indent=2) + "\n")
    print(json.dumps({
        "checked_parameter_tuples": checked,
        "max_ell": args.max_ell,
        "best": best[1] if best else None,
        "strict_improvements_over_85_294": wins,
        "kohonen_reconstruction": kohonen,
    }, indent=2))


if __name__ == "__main__":
    main()
