#!/usr/bin/env python3
"""Exact finite probe for nonstationary central-cell compositions.

The Pascal-cell cap/cup/convex profiles are generated from the exact strong
glue identities.  A sequence ``m1,m2,...`` denotes

    T(m_last,floor(m_last/2))[ ... [T(m1,floor(m1/2))] ... ].

Only Python integers are used for counts.  The script is evidence, not the
proof of the nonstationary barrier in NEW_HALF_AUDIT.md.
"""

from __future__ import annotations

import argparse

from dp_audit import log2_int


Poly = list[int]
Profile = tuple[int, Poly, Poly, Poly]


def add(a: Poly, b: Poly) -> Poly:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return out


def one_plus_nz(a: Poly, n: int) -> Poly:
    out = a + [0]
    for i, value in enumerate(a):
        out[i + 1] += n * value
    return out


def multiply(a: Poly, b: Poly) -> Poly:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def evaluate(a: Poly, n: int, shift: int) -> int:
    return sum(
        value * n ** (degree - shift)
        for degree, value in enumerate(a)
        if degree >= shift
    )


def central_profiles(max_m: int) -> dict[int, Profile]:
    singleton: Profile = (1, [0, 1], [0, 1], [0, 1])
    previous = [singleton]
    central: dict[int, Profile] = {0: singleton}
    for m in range(1, max_m + 1):
        current: list[Profile] = []
        for i in range(m + 1):
            if i in (0, m):
                state = singleton
            else:
                left = previous[i - 1]
                right = previous[i]
                state = (
                    left[0] + right[0],
                    add(right[1], one_plus_nz(left[1], right[0])),
                    add(left[2], one_plus_nz(right[2], left[0])),
                    add(add(left[3], right[3]), multiply(left[1], right[2])),
                )
            current.append(state)
        previous = current
        central[m] = current[m // 2]
    return central


def compose(sequence: list[int], central: dict[int, Profile]) -> None:
    size = caps = cups = convex = 1
    print(f"sequence={','.join(map(str, sequence))}")
    print(" step  macro_m     log2(size)    log2(C)/L^2    log2(W)/L^2")
    for step, m in enumerate(sequence, 1):
        r, cap_profile, cup_profile, convex_profile = central[m]
        next_caps = caps * evaluate(cap_profile, size, 1)
        next_cups = cups * evaluate(cup_profile, size, 1)
        next_convex = (
            r * convex
            + caps * cups * evaluate(convex_profile, size, 2)
        )
        size, caps, cups, convex = (
            size * r,
            next_caps,
            next_cups,
            next_convex,
        )
        log_size = log2_int(size)
        print(
            f"{step:5d}  {m:7d}  {log_size:13.6f}"
            f"  {log2_int(caps) / log_size**2:13.9f}"
            f"  {log2_int(convex) / log_size**2:13.9f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sequences",
        nargs="*",
        default=["2,4,8,16,32,64", "64,32,16,8,4,2", "4,16,64"],
        help="comma-separated central-cell parameters",
    )
    args = parser.parse_args()
    sequences = [[int(x) for x in item.split(",")] for item in args.sequences]
    central = central_profiles(max(max(sequence) for sequence in sequences))
    for sequence in sequences:
        compose(sequence, central)
        print()


if __name__ == "__main__":
    main()
