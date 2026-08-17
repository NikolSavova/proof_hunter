#!/usr/bin/env python3
"""Count additive triples in a canonical radial transversal of Z^2.

This script needs NumPy.  In the Codex desktop workspace it can be run with
the bundled Python runtime returned by `load_workspace_dependencies`.
"""

from __future__ import annotations

import argparse

import numpy as np


def canonical_transversal(m: int) -> list[tuple[int, int]]:
    representatives: dict[int, tuple[int, int]] = {}
    for x in range(m + 1):
        ys = range(1, m + 1) if x == 0 else range(-m, m + 1)
        for y in ys:
            norm = x * x + y * y
            point = (x, y)
            if norm not in representatives or point > representatives[norm]:
                representatives[norm] = point

    result: list[tuple[int, int]] = []
    for x, y in representatives.values():
        result.append((x, y))
        result.append((-x, -y))
    return result


def triple_count(points: list[tuple[int, int]], m: int) -> int:
    side = 1
    while side < 4 * m + 1:
        side *= 2

    indicator = np.zeros((side, side), dtype=np.float64)
    for x, y in points:
        indicator[x + m, y + m] = 1

    convolution = np.rint(
        np.fft.ifft2(np.fft.fft2(indicator) ** 2).real
    ).astype(np.int64)
    return sum(int(convolution[x + 2 * m, y + 2 * m]) for x, y in points)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("m", nargs="*", type=int, default=[20, 40, 80, 120, 200])
    args = parser.parse_args()

    for m in args.m:
        points = canonical_transversal(m)
        triples = triple_count(points, m)
        print(
            f"m={m:4d} |D|={len(points):8d} triples={triples:14d} "
            f"triples/m^2={triples / (m * m):.6f}"
        )


if __name__ == "__main__":
    main()
