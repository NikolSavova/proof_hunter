#!/usr/bin/env python3
"""Exact-integer audit of the proposed Pascal-row counting recurrence.

This does *not* certify the geometric decomposition.  It checks the algebraic
consequences of

    C[m,i] <= C[m-1,i] + (1 + binom(m-1,i)) C[m-1,i-1]

and of the row bound stated in the accompanying note.  All counts are Python
integers; floating point is used only when printing base-2 logarithms.
"""

from __future__ import annotations

import argparse
import math


TARGET = 1.0 / (2.0 * math.log(2.0))


def log2_int(n: int) -> float:
    """Accurate-enough log2 for a positive arbitrary-size integer."""
    if n <= 0:
        raise ValueError("log2_int expects a positive integer")
    b = n.bit_length()
    # Retain the leading 53 bits, so converting to float never overflows.
    shift = max(0, b - 53)
    return math.log2(n >> shift) + shift


def audit(max_m: int, sample: set[int] | None = None) -> list[dict[str, float | int]]:
    choose_prev = [1]
    cap_prev = [1]
    rows: list[dict[str, float | int]] = []

    for m in range(max_m + 1):
        if m == 0:
            choose = choose_prev
            cap = cap_prev
        else:
            choose = [1]
            for i in range(1, m):
                choose.append(choose_prev[i - 1] + choose_prev[i])
            choose.append(1)

            cap = [1] * (m + 1)
            for i in range(1, m):
                cap[i] = cap_prev[i] + (1 + choose_prev[i]) * cap_prev[i - 1]

        if m == 0 or (sample is not None and m not in sample):
            choose_prev, cap_prev = choose, cap
            continue

        # prefix[j] = product_{0 <= r < j} (1 + binom(m,r)).
        prefix = [1]
        for z in choose:
            prefix.append(prefix[-1] * (1 + z))

        row_bound = 0
        max_term = 0
        max_pair = (0, 0)
        for k in range(m + 1):
            middle = 1
            for ell in range(k, m + 1):
                if ell >= k + 2:
                    middle *= 1 + choose[ell - 1]
                term = cap[k] * cap[m - ell] * middle
                row_bound += term
                if term > max_term:
                    max_term = term
                    max_pair = (k, ell)

        # The endpoint term chooses at most one point in every internal block.
        endpoint = prefix[m] // prefix[1] if m >= 1 else 1
        rows.append(
            {
                "m": m,
                "log2_row": log2_int(row_bound),
                "row_rate": log2_int(row_bound) / (m * m),
                "max_rate": log2_int(max_term) / (m * m),
                "endpoint_rate": log2_int(endpoint) / (m * m),
                "max_k": max_pair[0],
                "max_l": max_pair[1],
                "cap_mid_rate": log2_int(cap[m // 2]) / (m * m),
            }
        )

        choose_prev, cap_prev = choose, cap

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=200)
    parser.add_argument(
        "--show",
        type=str,
        default="4,8,12,16,24,32,48,64,96,128,160,200",
        help="comma-separated rows to print",
    )
    args = parser.parse_args()
    wanted = {int(x) for x in args.show.split(",") if x.strip()}
    wanted.add(args.max_m)
    rows = audit(args.max_m, wanted)

    print(f"target base-2 coefficient = {TARGET:.12f}")
    print(
        " m    log2(Row)    /m^2       max/m^2    endpoint/m^2"
        "  maximizing(k,l)  log2 Cap(m,floor(m/2))/m^2"
    )
    for row in rows:
        m = int(row["m"])
        if m in wanted or m == args.max_m:
            print(
                f"{m:3d}  {row['log2_row']:12.5f}  {row['row_rate']:.9f}"
                f"  {row['max_rate']:.9f}  {row['endpoint_rate']:.9f}"
                f"       ({row['max_k']},{row['max_l']})"
                f"             {row['cap_mid_rate']:.9f}"
            )


if __name__ == "__main__":
    main()
