#!/usr/bin/env python3
"""Exact checks for the shear-averaged cubic-support theorem."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import gcd

from verify_adversarial_support_witnesses import WITNESSES


Point = tuple[int, int]
RPoint = tuple[Fraction, Fraction]


def sub(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def add_rational(left: RPoint, right: RPoint) -> RPoint:
    return left[0] + right[0], left[1] + right[1]


def shear(vector: Point, parameter: Fraction) -> RPoint:
    x, y = vector
    # (J+tI)(x,y)=(-y+tx,x+ty).
    return -Fraction(y) + parameter * x, Fraction(x) + parameter * y


def maximum_collinearity(points: list[Point]) -> int:
    answer = 1
    for index, point in enumerate(points):
        directions: Counter[Point] = Counter()
        for other_index, other in enumerate(points):
            if index == other_index:
                continue
            dx, dy = sub(other, point)
            divisor = gcd(abs(dx), abs(dy))
            dx, dy = dx // divisor, dy // divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            directions[dx, dy] += 1
        answer = max(answer, 1 + max(directions.values(), default=0))
    return answer


def line_sections(points: list[Point]) -> int:
    differences = {sub(left, right) for left in points for right in points}
    # Every affine line determined by two difference-set points is tested.
    lines: dict[tuple[int, int, int], int] = {}
    labels = sorted(differences)
    for left, right in combinations(labels, 2):
        dx, dy = sub(right, left)
        nx, ny = -dy, dx
        divisor = gcd(abs(nx), abs(ny))
        nx, ny = nx // divisor, ny // divisor
        if nx < 0 or (nx == 0 and ny < 0):
            nx, ny = -nx, -ny
        constant = nx * left[0] + ny * left[1]
        lines[nx, ny, constant] = sum(
            nx * point[0] + ny * point[1] == constant
            for point in differences
        )
    return max(lines.values(), default=1)


def energy(points: list[Point], parameter: Fraction) -> tuple[int, int]:
    fibres: Counter[RPoint] = Counter()
    for a in points:
        for b in points:
            for c in points:
                image = add_rational(
                    (Fraction(a[0]), Fraction(a[1])),
                    shear(sub(b, c), parameter),
                )
                fibres[image] += 1
    return sum(value * value for value in fibres.values()), len(fibres)


def main() -> None:
    points = WITNESSES[12]
    k = len(points)
    assert k == 12
    # The stored witness is distance-Sidon; its verifier checks this
    # independently.  Here we recompute the distinct squared norms.
    norms = {
        (points[i][0] - points[j][0]) ** 2
        + (points[i][1] - points[j][1]) ** 2
        for i in range(k)
        for j in range(i)
    }
    assert len(norms) == k * (k - 1) // 2

    collinearity = maximum_collinearity(points)
    maximum_section = line_sections(points)
    assert maximum_section <= k * collinearity

    parameters = [Fraction(value, 5) for value in range(-6, 7)]
    profiles = [energy(points, parameter) for parameter in parameters]
    total_energy = sum(value for value, _ in profiles)
    bound = (
        len(parameters) * (2 * k**3 - k**2)
        + k**5 * collinearity
    )
    assert total_energy <= bound

    for value, support in profiles:
        assert support * value >= k**6

    best = min(profiles)
    average_bound = 2 * k**3 - k**2 + Fraction(
        k**5 * collinearity, len(parameters)
    )
    assert best[0] <= average_bound

    print("points", k, "parameters", len(parameters))
    print("maximum_collinearity", collinearity)
    print("maximum_difference_line_section", maximum_section)
    print("total_energy", total_energy, "bound", bound)
    print("best_energy_support", best)
    print("PASS")


if __name__ == "__main__":
    main()
