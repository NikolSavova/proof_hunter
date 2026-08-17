#!/usr/bin/env python3
"""Exact small witness for the perpendicular-Golomb-ruler obstruction."""

from collections import Counter


S = [0, 1, 4, 9, 15, 22, 32, 34]
R1 = S[:4]
R2 = S[4:]
C = 1


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def rot(x: tuple[int, int]) -> tuple[int, int]:
    return -x[1], x[0]


positive_differences = [
    S[j] - S[i]
    for i in range(len(S))
    for j in range(i + 1, len(S))
]
assert len(set(positive_differences)) == len(positive_differences)

A = [(u, 0) for u in R1] + [(0, C + v) for v in R2]
squared_distances = Counter(
    (A[i][0] - A[j][0]) ** 2 + (A[i][1] - A[j][1]) ** 2
    for i in range(len(A))
    for j in range(i)
)
assert len(squared_distances) == len(A) * (len(A) - 1) // 2
assert max(squared_distances.values()) == 1

D = {
    sub(x, y)
    for x in A
    for y in A
    if x != y
}
assert len(D) == len(A) * (len(A) - 1)

overlap_counts = Counter(
    (x[0] + rot(y)[0], x[1] + rot(y)[1])
    for x in D
    for y in D
)
t, overlap = max(overlap_counts.items(), key=lambda item: item[1])
assert t != (0, 0)
assert overlap == 6

delta1 = {u - v for u in R1 for v in R1 if u != v}
delta2 = {u - v for u in R2 for v in R2 if u != v}
assert delta1.isdisjoint(delta2)
ruler_counts = Counter(u - v for u in delta1 for v in delta2)
assert sum(ruler_counts.values()) == len(delta1) * len(delta2)

print("marks", len(A))
print("distance_count", len(squared_distances))
print("max_overlap", overlap, "at", t)
print("ruler_pairs", sum(ruler_counts.values()))
print("ruler_support", len(ruler_counts))
print("PASS")
