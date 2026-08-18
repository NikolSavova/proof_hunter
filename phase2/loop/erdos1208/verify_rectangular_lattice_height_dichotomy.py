#!/usr/bin/env python3
"""Exact checks for RECTANGULAR_LATTICE_HEIGHT_DICHOTOMY.md."""

from __future__ import annotations


def radially_unique(r: int, s: int, u: int, v: int) -> bool:
    seen: dict[int, tuple[int, int]] = {}
    for i in range(r):
        for j in range(s):
            point = (u + i, v + j)
            norm = point[0] ** 2 + point[1] ** 2
            if norm in seen and seen[norm] != (-point[0], -point[1]):
                return False
            seen[norm] = point
    return True


def exhaustive_minimum(r: int, s: int) -> tuple[int, int, int]:
    for height in range(s * s + 1):
        for u in range(-height, height + 1):
            for v in range(-height, height + 1):
                if max(abs(u), abs(v)) != height:
                    continue
                if radially_unique(r, s, u, v):
                    return height, u, v
    raise AssertionError("the explicit height-squared construction was missed")


def main() -> None:
    for r in (2, 3, 5, 10, 30, 100, 200):
        for s in (2, 3, 5, 8, 12):
            if s > r:
                continue
            assert radially_unique(r, s, s * s, 0)
    print("explicit thin rectangles: PASS")

    expected_heights = {
        (4, 2): 1,
        (4, 3): 2,
        (4, 4): 4,
        (6, 2): 1,
        (6, 3): 2,
        (6, 4): 5,
        (8, 2): 1,
        (8, 3): 2,
        (8, 4): 5,
        (10, 2): 1,
        (10, 3): 2,
        (10, 4): 5,
    }
    for dimensions, target_height in expected_heights.items():
        height, u, v = exhaustive_minimum(*dimensions)
        assert height == target_height
        assert radially_unique(*dimensions, u, v)
    print("small rectangular optima: PASS")

    # The construction can beat an area-height bound by an arbitrary factor.
    for r in (100, 1_000, 10_000):
        s = 5
        translation_height = s * s
        assert translation_height < r * s
        assert radially_unique(r, s, translation_height, 0)
    print("area-height obstruction: PASS")
    print("rectangular lattice height dichotomy: PASS")


if __name__ == "__main__":
    main()
