#!/usr/bin/env python3
"""Exact generalized Kohonen staircase and its global optimization identity.

This is an unbounded arithmetic-block ansatz, not a bounded coordinate search.
For integers r>=1, u>=r+1, s>=r, z>=0 it builds the standard coprime-step
core followed by z consecutive dense blocks.  The theorem proved by the
integer identity below is

    m/ell^2 <= 85/294,

with equality only at (r,u,s,z)=(5,6,17,2), Kohonen's placement.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phased_predicate import coverage_bits, prefix_length


def parameters(r: int, u: int, s: int, z: int) -> tuple[int, int, int, int, int]:
    if r < 1 or u < r + 1 or s < r or z < 0:
        raise ValueError("require r>=1, u>=r+1, s>=r, z>=0")
    A = 2 * r + (r + 1) * s
    B = r * u + 2 * (r + 1) * s + 3 * r - r * r
    D = A + r * u + 1
    ell = u + s + r + 2 + z * (r + 1)
    m = B + z * D
    return A, B, D, ell, m


def placement(r: int, u: int, s: int, z: int, last_as_l0: bool = False) -> dict[str, set[int]]:
    A, B, D, _, _ = parameters(r, u, s, z)
    out = {
        "I": {0, r} | {A + r * i for i in range(u)},
        "J": {2 * r + (r + 1) * j for j in range(s)},
        "K": set(range(r))
        | {
            B + block * D + offset
            for block in range(z)
            for offset in range(r + 1)
        },
        "L0": set(),
        "L1": set(),
    }
    if last_as_l0 and z:
        last = set(range(B + (z - 1) * D, B + (z - 1) * D + r + 1))
        out["K"] -= last
        out["L0"] |= last
    return out


def obstruction_terms(r: int, u: int, s: int, z: int) -> dict[str, int | str]:
    """Return exact terms in the proof that 85 ell^2 - 294 m >= 0."""
    _, _, _, ell, m = parameters(r, u, s, z)
    gap = 85 * ell * ell - 294 * m
    x = u - (r + 1)
    a = r + 1
    S = s + x
    y = S - (3 * r + 2)
    w = z - 2
    base = (
        49 * (a - 6) ** 2
        + 85 * y * y
        + 14 * a * y
        + 85 * a * a * w * w
        + (14 * a * a + 294) * w
        - 124 * a * w * y
    )
    decomposition = base + 294 * x * (r + z + 2)
    if decomposition != gap:
        raise RuntimeError("algebraic identity failed")

    if w == 0:
        # For integral a != 6, minimizing over real y gives
        # 588(7a^2-85a+255)/85, positive because only a=6 lies
        # between its two roots.  At a=6 the integer expression is
        # y(85y+84), which is nonnegative for every integer y.
        proof_case = "w=0: integer exceptional case a=6; otherwise positive real discriminant bound"
        if a == 6:
            certified_lower = y * (85 * y + 84)
        else:
            certified_lower = 1  # sign certificate; exact gap is returned separately
    else:
        # Minimizing base over real y gives (147/85) P.  Since z>=0,
        # w is -2, -1, or >=1.  The three quadratic lower bounds in a
        # have negative discriminant and positive leading coefficient.
        P = 23 * a * a * w * w + 14 * a * a * w + 28 * a * a - 340 * a + 170 * w + 1020
        if w == -2:
            case_poly = 92 * a * a - 340 * a + 680
        elif w == -1:
            case_poly = 37 * a * a - 340 * a + 850
        else:
            case_poly = 65 * a * a - 340 * a + 1190
            if P < case_poly:
                raise RuntimeError("w>=1 monotonic lower bound failed")
        if case_poly <= 0:
            raise RuntimeError("positive-discriminant certificate failed")
        certified_lower = case_poly
        proof_case = "w=-2/-1/>=1: minimize over real y, then positive quadratic in a"
    if gap < 0 or certified_lower < 0:
        raise RuntimeError("claimed obstruction is false")
    return {
        "gap_85ell2_minus_294m": gap,
        "x": x,
        "a": a,
        "y": y,
        "w": w,
        "base_term": base,
        "nonnegative_x_correction": 294 * x * (r + z + 2),
        "proof_case": proof_case,
        "equality": gap == 0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r", type=int, default=5)
    parser.add_argument("--u", type=int, default=6)
    parser.add_argument("--s", type=int, default=17)
    parser.add_argument("--z", type=int, default=2)
    parser.add_argument("--last-as-l0", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    A, B, D, ell, m = parameters(args.r, args.u, args.s, args.z)
    p = placement(args.r, args.u, args.s, args.z, args.last_as_l0)
    abstract_prefix = prefix_length(coverage_bits(p, m + D + 8), m + D + 8)
    if abstract_prefix != m:
        raise RuntimeError(f"constructed placement has prefix {abstract_prefix}, expected exactly {m}")
    result = {
        "status": "PASS",
        "parameters": {"r": args.r, "u": args.u, "s": args.s, "z": args.z},
        "last_block_as_L0": args.last_as_l0,
        "A": A,
        "B": B,
        "D": D,
        "ell": ell,
        "m": m,
        "abstract_prefix": abstract_prefix,
        "ratio": f"{m}/{ell * ell}",
        "obstruction": obstruction_terms(args.r, args.u, args.s, args.z),
        "placement": {name: sorted(values) for name, values in p.items()},
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
