#!/usr/bin/env python3
"""Exact finite check for the adjacent-corner quadratic-fibre barrier."""

from __future__ import annotations

from collections import Counter


S = [0, 1, 4, 9, 15, 22, 32, 34]
R1 = S[:4]
R2 = S[4:]
C = 1
A = [(u, 0) for u in R1] + [(0, C + v) for v in R2]


def sub(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] - right[0], left[1] - right[1]


def rot(point: tuple[int, int]) -> tuple[int, int]:
    return -point[1], point[0]


H = [(u, 0) for u in R1]
V = [(0, C + v) for v in R2]

D = {sub(left, right) for left in A for right in A if left != right}
B = {
    (left[0] + rot(right)[0], left[1] + rot(right)[1])
    for left in A
    for right in A
}
assert len(D) == len(A) * (len(A) - 1)
assert len(B) == len(A) ** 2
norms = Counter(
    (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2
    for index, left in enumerate(A)
    for right in A[:index]
)
assert len(norms) == len(A) * (len(A) - 1) // 2

full_profile = Counter(
    (difference[0] - pair_sum[0], difference[1] - pair_sum[1])
    for difference in D
    for pair_sum in B
)

restricted_profile = Counter(
    (
        (r - r_prime) - (u - C - v),
        0,
    )
    for r in R1
    for r_prime in R1
    if r != r_prime
    for u in R1
    for v in R2
)

assert sum(restricted_profile.values()) == len(R1) ** 3 * (len(R1) - 1)
assert len(restricted_profile) <= 4 * (max(R1 + R2) - min(R1 + R2)) + 1

t, restricted_peak = max(restricted_profile.items(), key=lambda item: item[1])
assert restricted_peak == 8
assert full_profile[t] >= restricted_peak

intersection = D & {
    (t[0] + pair_sum[0], t[1] + pair_sum[1])
    for pair_sum in B
}
assert len(intersection) == full_profile[t]
assert len(intersection) >= restricted_peak

print(
    "marks",
    len(A),
    "translation",
    t,
    "restricted-peak",
    restricted_peak,
    "full-intersection",
    len(intersection),
)
print("adjacent-corner fibre barrier: PASS")
