#!/usr/bin/env python3
"""Exact checks for GAP_BUDGETED_REPAIR_ALPHABET_MUTATION_GATE."""

from fractions import Fraction
from itertools import combinations


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def hull(points, chosen):
    ordered = sorted(chosen, key=lambda i: (points[i][0], points[i][1]))
    if len(ordered) <= 1:
        return ordered

    def chain(sequence):
        result = []
        for index in sequence:
            while (len(result) >= 2
                   and orient(points[result[-2]], points[result[-1]],
                              points[index]) <= 0):
                result.pop()
            result.append(index)
        return result

    lower = chain(ordered)
    upper = chain(reversed(ordered))
    return lower[:-1] + upper[:-1]


def ordinary(points, mask):
    chosen = [i for i in range(len(points)) if mask >> i & 1]
    return len(chosen) <= 3 or len(hull(points, chosen)) == len(chosen)


def rank_profile(points):
    profile = {}
    for mask in range(1 << len(points)):
        if ordinary(points, mask):
            rank = mask.bit_count()
            profile[rank] = profile.get(rank, 0) + 1
    return profile


def evaluate(profile):
    return sum(profile.values())


def coefficientwise_one_bit(left, right):
    """Check left(z) <= (1+z) right(z) coefficientwise."""
    for rank in range(max(left.keys() | right.keys()) + 1):
        assert left.get(rank, 0) <= (right.get(rank, 0)
                                     + right.get(rank - 1, 0))


def relocation_checks():
    q = tuple((Fraction(x), Fraction(25 - x * x))
              for x in (-5, -3, -1, 2, 4, 5))
    positions = (
        (Fraction(0), Fraction(1)),
        (Fraction(1, 3), Fraction(-2)),
        (Fraction(-2, 3), Fraction(17)),
    )
    profiles = []
    for point in positions:
        points = q + (point,)
        assert general_position(points)
        profiles.append(rank_profile(points))
    for left in profiles:
        for right in profiles:
            coefficientwise_one_bit(left, right)

    # Two arbitrary labels: the endpoint ratio is at most 2^2.
    start = q + ((Fraction(0), Fraction(1)),
                 (Fraction(1, 2), Fraction(3)))
    end = q + ((Fraction(-1, 2), Fraction(-3)),
               (Fraction(3, 2), Fraction(18)))
    assert general_position(start)
    assert general_position(end)
    v_start = evaluate(rank_profile(start))
    v_end = evaluate(rank_profile(end))
    assert v_end <= 4 * v_start
    assert v_start <= 4 * v_end
    return v_start, v_end


def ear_star_check():
    xs = (-5, -3, -1, 2, 4, 5)
    q = tuple((Fraction(x), Fraction(25 - x * x)) for x in xs)
    # The endpoint chord is the lower exposed edge; move the ear below it.
    ear = (Fraction(0), Fraction(-1))
    points = q + (ear,)
    assert general_position(points)
    last = len(q)
    checked = 0
    for mask in range(1 << len(q)):
        if not (mask & 1 and mask & (1 << (len(q) - 1))):
            continue
        if mask.bit_count() < 3:
            continue
        assert ordinary(q, mask)
        assert ordinary(points, mask | (1 << last))
        checked += 1
    assert checked == (1 << (len(q) - 2)) - 1
    return checked


def quadratic_wall_check(r=12):
    q = tuple((Fraction(i), Fraction(i * i)) for i in range(-r, r + 1))
    start = (Fraction(0), Fraction(r * r, 4) + Fraction(1, 3))
    epsilon = Fraction(1, 100 * r ** 4)
    target = (Fraction(1, 2), Fraction(1, 2) + epsilon)
    assert general_position(q + (start,))
    assert general_position(q + (target,))
    separating = []
    for i, j in combinations(range(len(q)), 2):
        if orient(q[i], q[j], start) * orient(q[i], q[j], target) < 0:
            separating.append((i, j))
    assert len(separating) == 91
    assert len(separating) >= (r // 3) ** 2
    return len(separating)


def main():
    v_start, v_end = relocation_checks()
    ears = ear_star_check()
    walls = quadratic_wall_check()
    print("PASS: repair alphabet; barVstart=%d barVend=%d ear-star=%d "
          "separating-walls=%d" % (v_start, v_end, ears, walls))


if __name__ == "__main__":
    main()
