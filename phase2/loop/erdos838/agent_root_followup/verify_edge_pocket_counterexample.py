#!/usr/bin/env python3
"""Exact certificate killing static edge-pocket link factorization."""

from itertools import combinations

P = [
    (0, -83154),
    (1, 56327),
    (2, 28007),
    (3, 67474),
    (4, -91970),
]


def orient(i: int, j: int, k: int) -> int:
    a, b, c = P[i], P[j], P[k]
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(indices):
    ordered = sorted(indices, key=lambda i: P[i])
    if len(ordered) <= 1:
        return ordered
    lower = []
    for i in ordered:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def convex(indices) -> bool:
    indices = tuple(indices)
    return len(indices) <= 2 or len(hull(indices)) == len(indices)


assert all(orient(*triple) != 0 for triple in combinations(range(5), 3))

A = (0, 2, 4)
assert hull(A) == [0, 4, 2]
assert convex(A + (1,))
assert convex(A + (3,))

# In the cyclic hull [0,4,2], point 1 is inserted between 2 and 0, while
# point 3 is inserted between 4 and 2: they belong to different original
# edge pockets.
assert hull(A + (1,)) == [0, 4, 2, 1]
assert hull(A + (3,)) == [0, 4, 3, 2]

# Simultaneous insertion makes point 2 interior.
assert not convex(A + (1, 3))
assert hull(A + (1, 3)) == [0, 4, 3, 1]

print("PASS: static edge-pocket link factorization is false")
