#!/usr/bin/env python3
"""Audit cap/cup counts in Aichholzer's small order-type database.

The script does not redistribute the database.  Download matching files named
``otypesNN.b08`` (or ``.b16``) and ``kgonsNN.b08`` and pass their containing
directory with ``--data-dir``.

For points in increasing x-order, a cap/cup is exactly a monochromatic
monotone path in the orientation coloring of triples.  Dynamic programming on
the last two vertices therefore counts all caps/cups in O(n^3) per order type.
"""

from __future__ import annotations

import argparse
import math
import struct
from pathlib import Path


def orientation(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if value == 0:
        raise ValueError("database record is not in general position")
    return 1 if value > 0 else -1


def cap_cup_counts(points: list[tuple[int, int]]) -> tuple[int, int]:
    """Return numbers of nonempty caps and cups (singletons included)."""
    points = sorted(points)
    n = len(points)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            # The edge (i,j) is the unique cap and cup of size two ending there.
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                if orientation(points[h], points[i], points[j]) < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def convex_count_by_endpoint_factorization(points: list[tuple[int, int]]) -> int:
    """Count nonempty convex subsets by their two monotone hull chains.

    For each pair of left/right endpoints ``s,t``, independently count caps
    and cups starting at ``s`` and ending at ``t``.  Their product counts the
    convex subsets with these extreme points.  This is deliberately separate
    from ``cap_cup_counts``: its two-index DP counts chains with arbitrary
    starting points, whereas endpoint factorization requires fixing both
    endpoints.
    """
    points = sorted(points)
    n = len(points)
    total = n
    for start in range(n):
        cap = [[0] * n for _ in range(n)]
        cup = [[0] * n for _ in range(n)]
        for end in range(start + 1, n):
            cap[start][end] = cup[start][end] = 1
        for middle in range(start + 1, n):
            for end in range(middle + 1, n):
                cap[middle][end] = sum(
                    cap[previous][middle]
                    for previous in range(start, middle)
                    if orientation(points[previous], points[middle], points[end]) < 0
                )
                cup[middle][end] = sum(
                    cup[previous][middle]
                    for previous in range(start, middle)
                    if orientation(points[previous], points[middle], points[end]) > 0
                )
        for end in range(start + 1, n):
            caps = sum(cap[previous][end] for previous in range(start, end))
            cups = sum(cup[previous][end] for previous in range(start, end))
            total += caps * cups
    return total


def coordinate_records(path: Path, n: int):
    width = 1 if path.suffix == ".b08" else 2
    code = "B" if width == 1 else "H"
    record_size = 2 * n * width
    data = path.read_bytes()
    if len(data) % record_size:
        raise ValueError(f"{path}: size is not a multiple of {record_size}")
    fmt = "<" + code * (2 * n)
    for offset in range(0, len(data), record_size):
        values = struct.unpack_from(fmt, data, offset)
        yield list(zip(values[0::2], values[1::2]))


def kgon_records(path: Path, n: int):
    record_size = n - 2
    data = path.read_bytes()
    if len(data) % record_size:
        raise ValueError(f"{path}: size is not a multiple of {record_size}")
    for offset in range(0, len(data), record_size):
        yield tuple(data[offset : offset + record_size])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()

    n = args.n
    candidates = [args.data_dir / f"otypes{n:02}.b08", args.data_dir / f"otypes{n:02}.b16"]
    coordinate_path = next((p for p in candidates if p.exists()), None)
    if coordinate_path is None:
        raise FileNotFoundError(f"no coordinate file among {candidates}")
    kgon_path = args.data_dir / f"kgons{n:02}.b08"
    if not kgon_path.exists():
        raise FileNotFoundError(kgon_path)

    base = 1 + n + math.comb(n, 2)
    best_convex: tuple[int, int, tuple[int, ...], list[tuple[int, int]]] | None = None
    best_chain: tuple[int, int, int, int, list[tuple[int, int]]] | None = None
    records = 0
    for index, (points, profile) in enumerate(
        zip(coordinate_records(coordinate_path, n), kgon_records(kgon_path, n), strict=True)
    ):
        caps, cups = cap_cup_counts(points)
        convex = base + sum(profile)
        # Caps and cups overlap exactly on sets of size one and two.
        chain_union = caps + cups - n - math.comb(n, 2)
        candidate_convex = (convex, index, profile, points)
        candidate_chain = (chain_union, index, caps, cups, points)
        if best_convex is None or candidate_convex < best_convex:
            best_convex = candidate_convex
        if best_chain is None or candidate_chain < best_chain:
            best_chain = candidate_chain
        records += 1

    assert best_convex is not None and best_chain is not None
    endpoint_product = convex_count_by_endpoint_factorization(best_convex[3])
    if endpoint_product != best_convex[0] - 1:
        raise AssertionError(
            f"chain factorization failed on convex minimizer: "
            f"{endpoint_product=} versus nonempty={best_convex[0] - 1}"
        )
    print(f"n={n} records={records}")
    print(
        "minimum all convex subsets (empty included): "
        f"{best_convex[0]}, index={best_convex[1]}, k-profile={best_convex[2]}"
    )
    print(f"  coordinates={best_convex[3]}")
    print(f"  endpoint cap/cup product identity={endpoint_product}")
    print(
        "minimum cap/cup union (empty excluded): "
        f"{best_chain[0]}, index={best_chain[1]}, caps={best_chain[2]}, cups={best_chain[3]}"
    )
    print(f"  coordinates={best_chain[4]}")


if __name__ == "__main__":
    main()
