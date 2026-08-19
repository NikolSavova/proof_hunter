#!/usr/bin/env python3
"""Exact checks for THREE_PROJECTION_FIBRE_BARRIER.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations


Point = tuple[int, int]
Triple = tuple[int, int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def verify_real_fibres(size: int = 9) -> None:
    # Powers of two form an integral one-dimensional Golomb ruler.
    points = [(1 << index, 0) for index in range(size)]
    positive_differences = {
        right[0] - left[0]
        for left, right in combinations(points, 2)
    }
    assert len(positive_differences) == size * (size - 1) // 2

    fibres: dict[Point, list[tuple[Point, Point, Point]]] = defaultdict(list)
    for first in points:
        for second in points:
            for third in points:
                if second == third:
                    continue
                output = add(first, rotate(subtract(second, third)))
                fibres[output].append((first, second, third))

    for fibre in fibres.values():
        for coordinate in range(3):
            assert len({record[coordinate] for record in fibre}) == len(fibre)

    for first_coordinate, second_coordinate in ((0, 1), (0, 2), (1, 2)):
        owners: dict[tuple[Point, Point], set[Point]] = defaultdict(set)
        for output, fibre in fibres.items():
            for record in fibre:
                cell = record[first_coordinate], record[second_coordinate]
                owners[cell].add(output)

        common_cells: Counter[tuple[Point, Point]] = Counter()
        for outputs in owners.values():
            for left, right in combinations(sorted(outputs), 2):
                common_cells[left, right] += 1
        assert max(common_cells.values(), default=0) <= 1

    print("real three-projection fibre linearity", size, len(fibres))


def projection(record: Triple, coordinates: tuple[int, int]) -> tuple[int, int]:
    return record[coordinates[0]], record[coordinates[1]]


def verify_prime(prime: int) -> None:
    slopes = range(1, (prime - 1) // 2 + 1)
    fibres: dict[tuple[int, int], set[Triple]] = {}
    all_records: set[Triple] = set()

    for slope in slopes:
        for intercept in range(prime):
            raw = {
                (
                    parameter,
                    (slope * parameter + intercept) % prime,
                    (
                        slope * slope * parameter
                        + (slope + 1) * intercept
                    )
                    % prime,
                )
                for parameter in range(prime)
            }
            assert len(raw) == prime
            for coordinate in range(3):
                assert len({record[coordinate] for record in raw}) == prime

            if slope != 1:
                raw = {
                    record
                    for record in raw
                    if not (record[0] == record[1] == record[2])
                }
                assert len(raw) == prime - 1
            fibres[slope, intercept] = raw
            assert not all_records.intersection(raw)
            all_records.update(raw)

    number_slopes = (prime - 1) // 2
    assert len(fibres) == number_slopes * prime
    assert len(all_records) == (
        number_slopes * prime**2 - (number_slopes - 1) * prime
    )

    for coordinates in ((0, 1), (0, 2), (1, 2)):
        projected = {
            label: {projection(record, coordinates) for record in fibre}
            for label, fibre in fibres.items()
        }
        for left, right in combinations(projected, 2):
            assert len(projected[left].intersection(projected[right])) <= 1

    print(
        prime,
        "three-projection profile",
        (len(fibres), len(all_records), min(map(len, fibres.values()))),
    )


def main() -> None:
    verify_real_fibres()
    for prime in (5, 7, 11, 13, 17, 19):
        verify_prime(prime)
    print("three-projection fibre barrier: PASS")


if __name__ == "__main__":
    main()
