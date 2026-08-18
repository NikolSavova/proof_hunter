#!/usr/bin/env python3
"""Exact checks for RADIAL_ORTHOGONAL_PRODUCT_BARRIER.md."""

from __future__ import annotations

Point = tuple[int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def canonical_transversal(side: int) -> list[Point]:
    representatives: dict[int, Point] = {}
    for x in range(side + 1):
        ys = range(1, side + 1) if x == 0 else range(-side, side + 1)
        for y in ys:
            norm = x * x + y * y
            point = (x, y)
            if norm not in representatives or point > representatives[norm]:
                representatives[norm] = point

    result: list[Point] = []
    for x, y in representatives.values():
        result.extend(((x, y), (-x, -y)))
    return result


def radial_set(side: int) -> set[Point]:
    return {(0, 0), *canonical_transversal(side)}


def verify_radial_structure(points: set[Point]) -> None:
    assert all((-x, -y) in points for x, y in points)

    norm_fibres: dict[int, set[Point]] = {}
    for point in points:
        norm = point[0] ** 2 + point[1] ** 2
        norm_fibres.setdefault(norm, set()).add(point)

    assert norm_fibres[0] == {(0, 0)}
    for norm, fibre in norm_fibres.items():
        if norm == 0:
            continue
        assert len(fibre) == 2
        first, second = tuple(fibre)
        assert first == (-second[0], -second[1])

    rotated = {rotate(point) for point in points}
    assert points & rotated == {(0, 0)}


def profile(side: int) -> tuple[int, int, int]:
    points = radial_set(side)
    verify_radial_structure(points)
    ordinary = {add(left, right) for left in points for right in points}
    orthogonal = {
        add(left, rotate(right))
        for left in points
        for right in points
    }
    return len(points), len(ordinary), len(orthogonal)


def main() -> None:
    expected = {
        3: (19, 73, 109),
        5: (39, 181, 281),
        8: (83, 431, 685),
        12: (165, 935, 1_509),
        20: (395, 2_515, 4_101),
        30: (815, 5_569, 9_141),
    }
    previous_ratio: float | None = None
    for side, target in expected.items():
        actual = profile(side)
        assert actual == target
        number, ordinary, orthogonal = actual
        ratio = ordinary * orthogonal / number**3
        if side >= 5 and previous_ratio is not None:
            assert ratio < previous_ratio
        previous_ratio = ratio
        print(side, actual, "normalized_product", ratio)

    print("radial orthogonal product barrier: PASS")


if __name__ == "__main__":
    main()
