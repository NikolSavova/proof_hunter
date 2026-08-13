#!/usr/bin/env python3
"""Exact-integer audit for the candidate Erdős #838 row-count bound.

This script verifies the combinatorial recurrence numerically; it does not
certify the geometric gluing lemmas.  All large counts are Python integers.
"""

from __future__ import annotations

import argparse
import math


ROW_TARGET = 1.0 / (2.0 * math.log(2.0))
CENTRAL_TARGET = 1.0 - 1.0 / (4.0 * math.log(2.0))


def log2_int(value: int) -> float:
    """Return log2(value) without converting a huge integer to float."""
    if value <= 0:
        raise ValueError("log2_int expects a positive integer")
    bits = value.bit_length()
    kept = min(bits, 53)
    top = value >> (bits - kept)
    return (bits - kept) + math.log2(top)


def cap_table(max_m: int) -> list[list[int]]:
    """Upper bounds C[m][i] from recurrence (1) in proof_draft.md."""
    table: list[list[int]] = [[1]]
    for m in range(1, max_m + 1):
        row = [1]
        for i in range(1, m):
            right_only = table[m - 1][i]
            crossing = (1 + math.comb(m - 1, i)) * table[m - 1][i - 1]
            row.append(right_only + crossing)
        row.append(1)
        table.append(row)
    return table


def convex_cell_table(max_m: int, caps: list[list[int]]) -> list[list[int]]:
    """Exact nonempty convex-subset counts for the strong-glue cells."""
    table: list[list[int]] = [[1]]
    for m in range(1, max_m + 1):
        row = [1]
        for i in range(1, m):
            cup_right = caps[m - 1][(m - 1) - i]
            row.append(
                table[m - 1][i - 1]
                + table[m - 1][i]
                + caps[m - 1][i - 1] * cup_right
            )
        row.append(1)
        table.append(row)
    return table


def row_bound(m: int, caps: list[list[int]]) -> int:
    """The exact integer on the right side of row bound (6)."""
    total = 1  # empty subset
    for first in range(m + 1):
        middle_product = 1
        for last in range(first, m + 1):
            if last > first + 1:
                middle_product *= 1 + math.comb(m, last - 1)
            cups_last = caps[m][m - last]
            total += caps[m][first] * cups_last * middle_product
    return total


def entropy(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def simpson_entropy(steps: int = 100_000) -> float:
    if steps % 2:
        steps += 1
    width = 1.0 / steps
    odd = sum(entropy(j * width) for j in range(1, steps, 2))
    even = sum(entropy(j * width) for j in range(2, steps, 2))
    return width * (4.0 * odd + 2.0 * even) / 3.0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=200)
    parser.add_argument(
        "--rows",
        default="4,8,10,20,40,80,120,160,200",
        help="comma-separated m values to print (values above --max-m are skipped)",
    )
    args = parser.parse_args()
    if args.max_m < 1:
        raise SystemExit("--max-m must be positive")

    caps = cap_table(args.max_m)
    convex_cells = convex_cell_table(args.max_m, caps)
    requested = sorted({int(item) for item in args.rows.split(",") if item})

    print("m  log2(row_bound)  log2(row_bound)/m^2")
    for m in requested:
        if 1 <= m <= args.max_m:
            bound = row_bound(m, caps)
            log_bound = log2_int(bound)
            print(f"{m:3d} {log_bound:17.9f} {log_bound / (m*m):22.12f}")

    print()
    print("m  central N  exact/log2(N)^2  cap*cup/log2(N)^2")
    for m in requested:
        if 1 <= m <= args.max_m:
            i = m // 2
            size = math.comb(m, i)
            log_size = log2_int(size)
            exact = 1 + convex_cells[m][i]
            product_bound = 1 + caps[m][i] * caps[m][m - i]
            print(
                f"{m:3d} {size:10d} "
                f"{log2_int(exact) / (log_size * log_size):16.12f} "
                f"{log2_int(product_bound) / (log_size * log_size):21.12f}"
            )

    integral = simpson_entropy()
    print()
    print(f"Simpson integral of H_2 on [0,1] : {integral:.12f}")
    print(f"Exact 1/(2 ln 2)                : {ROW_TARGET:.12f}")
    print(f"Absolute quadrature error        : {abs(integral - ROW_TARGET):.3e}")
    print(f"Central target 1-1/(4 ln 2)      : {CENTRAL_TARGET:.12f}")
    if abs(integral - ROW_TARGET) > 2e-8:
        raise SystemExit("entropy integral audit failed")


if __name__ == "__main__":
    main()
