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

# Restrict the rotated triple map to a on the horizontal arm and distinct
# b,c on the vertical arm.  These triples already give fourth-power energy.
horizontal = [(u, 0) for u in R1]
vertical = [(0, C + v) for v in R2]
restricted_phi = Counter(
    (
        a[0] + rot(sub(b, c))[0],
        a[1] + rot(sub(b, c))[1],
    )
    for a in horizontal
    for b in vertical
    for c in vertical
    if b != c
)
restricted_phi_energy = sum(value * value for value in restricted_phi.values())
assert sum(restricted_phi.values()) == len(R1) * len(R2) * (len(R2) - 1)

full_phi = Counter(
    (
        a[0] + rot(sub(b, c))[0],
        a[1] + rot(sub(b, c))[1],
    )
    for a in A
    for b in A
    for c in A
    if b != c
)
full_phi_energy = sum(value * value for value in full_phi.values())
assert full_phi_energy >= restricted_phi_energy

print("marks", len(A))
print("distance_count", len(squared_distances))
print("max_overlap", overlap, "at", t)
print("ruler_pairs", sum(ruler_counts.values()))
print("ruler_support", len(ruler_counts))
print("restricted_phi_energy", restricted_phi_energy)
print("full_phi_energy", full_phi_energy)
print("PASS")
