#!/usr/bin/env python3
"""Exact rational audit for MARKED_TURN_CIRCUIT_FLIP_MUTATION_GATE."""

from fractions import Fraction
from itertools import combinations


X_VALUES = (-10, -8, -5, -2, 1, 4, 7, 10)
Q = tuple((Fraction(x), Fraction(100 - x * x)) for x in X_VALUES)
X_PLUS = (Fraction(0), Fraction(1))
X_MINUS = (Fraction(0), Fraction(-1))
A_INDEX = 0
B_INDEX = len(Q) - 1


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points, indices):
    ordered = sorted(indices, key=lambda i: (points[i][0], points[i][1]))
    if len(ordered) <= 1:
        return ordered

    def chain(sequence):
        out = []
        for index in sequence:
            while (len(out) >= 2
                   and orient(points[out[-2]], points[out[-1]],
                              points[index]) <= 0):
                out.pop()
            out.append(index)
        return out

    lower = chain(ordered)
    upper = chain(reversed(ordered))
    return lower[:-1] + upper[:-1]


def convex(points, indices):
    if len(indices) <= 3:
        return True
    return len(hull(points, indices)) == len(indices)


def all_masks(n):
    return range(1 << n)


def indices(mask, n):
    return tuple(i for i in range(n) if mask >> i & 1)


def face_masks(points):
    n = len(points)
    return {mask for mask in all_masks(n)
            if convex(points, indices(mask, n))}


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def orientation_changes(plus, minus):
    changes = []
    for triple in combinations(range(len(plus)), 3):
        sp = orient(*(plus[i] for i in triple))
        sm = orient(*(minus[i] for i in triple))
        if (sp > 0) != (sm > 0):
            changes.append(triple)
    return changes


def edge_star_masks():
    m = len(Q)
    plus = set()
    minus = set()
    for mask in all_masks(m):
        chosen = indices(mask, m)
        if A_INDEX not in chosen or B_INDEX not in chosen or len(chosen) < 3:
            continue
        assert convex(Q, chosen)
        other = [i for i in chosen if i not in (A_INDEX, B_INDEX)]
        signs = {orient(Q[A_INDEX], Q[B_INDEX], Q[i]) > 0 for i in other}
        assert len(signs) == 1
        target = plus if next(iter(signs)) else minus
        target.add(mask)
    return plus, minus


def main():
    plus_points = Q + (X_PLUS,)
    minus_points = Q + (X_MINUS,)
    assert general_position(plus_points)
    assert general_position(minus_points)
    assert orientation_changes(plus_points, minus_points) == [
        (A_INDEX, B_INDEX, len(Q))
    ]

    q_faces = face_masks(Q)
    assert len(q_faces) == 1 << len(Q)
    plus_faces = face_masks(plus_points)
    minus_faces = face_masks(minus_points)
    gained = minus_faces - plus_faces
    lost = plus_faces - minus_faces

    star_plus, star_minus = edge_star_masks()
    x_bit = 1 << len(Q)
    expected_gained = {mask | x_bit for mask in star_plus}
    expected_lost = {mask | x_bit for mask in star_minus}
    assert gained == expected_gained
    assert lost == expected_lost
    assert len(star_plus) == (1 << (len(Q) - 2)) - 1 == 63
    assert len(star_minus) == 0
    assert len(minus_faces) - len(plus_faces) == 63

    # Rank-generating-function derivative, coefficient by coefficient.
    plus_profile = {}
    minus_profile = {}
    gained_profile = {}
    lost_profile = {}
    for mask in star_plus:
        rank = mask.bit_count()
        plus_profile[rank] = plus_profile.get(rank, 0) + 1
    for mask in star_minus:
        rank = mask.bit_count()
        minus_profile[rank] = minus_profile.get(rank, 0) + 1
    for mask in gained:
        rank = mask.bit_count()
        gained_profile[rank] = gained_profile.get(rank, 0) + 1
    for mask in lost:
        rank = mask.bit_count()
        lost_profile[rank] = lost_profile.get(rank, 0) + 1
    ranks = set(gained_profile) | set(lost_profile)
    for rank in ranks:
        assert (gained_profile.get(rank, 0) - lost_profile.get(rank, 0)
                == plus_profile.get(rank - 1, 0)
                - minus_profile.get(rank - 1, 0))

    # The retag literally recovers its Q-source by deleting x.
    assert {mask & ~x_bit for mask in gained} == star_plus

    print("PASS: marked-turn circuit flip; Vplus=%d Vminus=%d "
          "Eplus=%d Eminus=%d changed-triples=1"
          % (len(plus_faces), len(minus_faces),
             len(star_plus), len(star_minus)))


if __name__ == "__main__":
    main()
