#!/usr/bin/env python3
"""Try to realize a prescribed K_{s,s} rotated-overlap graph generically.

Choose source labels a_i,c_j, arbitrary target first labels b_ij and a
translation t, then solve

    a_i + J c_j - (b_ij + J d_ij) = t

for d_ij.  Exact squared-distance checking determines whether the linear
constraints themselves force a repeated Euclidean distance.
"""

from random import Random


Point = tuple[int, int]


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def sub(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


def rot(x: Point) -> Point:
    return -x[1], x[0]


def random_point(rng: Random, bits: int) -> Point:
    return rng.randrange(1 << bits), rng.randrange(1 << bits)


def first_distance_collision(points: list[Point]) -> tuple[int, int, int, int] | None:
    seen: dict[int, tuple[int, int]] = {}
    for i, x in enumerate(points):
        for j, y in enumerate(points[:i]):
            delta = sub(x, y)
            norm = delta[0] * delta[0] + delta[1] * delta[1]
            if norm in seen:
                p, q = seen[norm]
                if {i, j} != {p, q}:
                    return p, q, i, j
            else:
                seen[norm] = (i, j)
    return None


def trial(side: int, seed: int, bits: int = 80) -> tuple[list[Point], object]:
    rng = Random(seed)
    left = [random_point(rng, bits) for _ in range(side)]
    right = [random_point(rng, bits) for _ in range(side)]
    target_first = [random_point(rng, bits) for _ in range(side * side)]
    translation = random_point(rng, bits)
    target_second: list[Point] = []
    for i in range(side):
        for j in range(side):
            # d = c - J a + J b + J t.
            value = add(
                sub(right[j], rot(left[i])),
                add(rot(target_first[i * side + j]), rot(translation)),
            )
            target_second.append(value)
    points = left + right + target_first + target_second
    return points, first_distance_collision(points)


if __name__ == "__main__":
    for size in [2, 3, 4]:
        for attempt in range(100):
            points, collision = trial(size, 1208000 + 1000 * size + attempt)
            if collision is None:
                print("distance-Sidon realization", "size", size, "points", len(points))
                break
        else:
            print("no realization", "size", size, "last collision", collision)
