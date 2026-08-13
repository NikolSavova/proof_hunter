#!/usr/bin/env python3
"""Finite arithmetic certificate for the multiscale endpoint-reset proof.

This is not a substitute for the symbolic proof in NEXT_ENDPOINT_ATTACK.md.
It checks the two reset inequalities on exhaustive integer states in a
user-selected box, and prints the explicit asymptotic bound delivered by
the proof's chosen parameters.
"""

from __future__ import annotations

import argparse
import math


def check_reset_box(limit: int) -> tuple[int, int, int]:
    first_checked = 0
    increment_checked = 0
    closed_checked = 0
    for F in range(limit + 1):
        for mu in range(limit + 1):
            for L in range(limit + 1):
                ell = F - mu - L
                if ell < 0:
                    continue
                for xa in range(ell, mu + L + 1):
                    for ya in range(ell, mu + L + 1):
                        if xa + ya < F:
                            continue
                        for xb in range(ell, mu + L + 1):
                            for yb in range(ell, mu + L + 1):
                                if xb + yb < F or xa + yb > mu:
                                    continue
                                assert xb >= 2 * (F - mu) - L
                                assert ya >= 2 * (F - mu) - L
                                first_checked += 1

                # Later event, in the orientation H=left and Q=right.
                # The reflected orientation is identical after swapping x,y.
                for xh in range(limit + 1):
                    for yh in range(limit + 1):
                        for xq in range(ell, mu + L + 1):
                            for yq in range(ell, mu + L + 1):
                                if xq + yq < F or xh + yq > mu:
                                    continue
                                assert xq >= xh + (F - mu)
                                increment_checked += 1

                # Equation (13), cleared of denominators.
                D = F - mu
                for q in range(1, limit + 1):
                    if mu < (q + 2) * D - 2 * L:
                        continue
                    assert (q + 3) * mu >= (q + 2) * F - 2 * L
                    closed_checked += 1
    return first_checked, increment_checked, closed_checked


def printed_bound(L: float) -> tuple[float, float, float, int]:
    """Return (lower bound, target half-square, deficit, event count)."""
    R = math.ceil(math.sqrt(L))
    lam = math.log2(L)
    delta = 4 * R + 2 * lam + 1
    F = 0.5 * (L - delta) ** 2 - 3 * L
    q = math.ceil((R - 1) / 2)
    reset = (q + 2) / (q + 3) * F - 2 * L / (q + 3)
    immediate = F - L
    lower = min(immediate, reset)
    target = 0.5 * L * L
    return lower, target, target - lower, R


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--box", type=int, default=8)
    parser.add_argument(
        "--logs",
        type=float,
        nargs="*",
        default=[10**3, 10**4, 10**5, 10**6],
        help="values of L=log2(n) at which to print the certified formula",
    )
    args = parser.parse_args()

    first, increment, closed = check_reset_box(args.box)
    print(
        f"reset states checked: first={first} "
        f"increment={increment} closed={closed}"
    )
    for L in args.logs:
        lower, target, deficit, events = printed_bound(L)
        print(
            f"L={L:g} R={events} lower={lower:.6f} "
            f"halfL2={target:.6f} deficit/L^1.5={deficit/L**1.5:.6f}"
        )


if __name__ == "__main__":
    main()
