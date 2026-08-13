#!/usr/bin/env python3
"""Exact checks for the obstructions in HISTORY_ATTACK.md.

All coordinates are integer.  No floating-point predicates are used.
"""

from itertools import combinations
from math import ceil


def orient(points, i, j, k):
    """Twice the signed area of points i,j,k."""
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]
    return (xj - xi) * (yk - yi) - (xk - xi) * (yj - yi)


def monochromatic(points, vertices, sign):
    return all(sign * orient(points, i, j, k) > 0
               for i, j, k in combinations(vertices, 3))


def hinged(points):
    signs = []
    for i in range(len(points) - 2):
        row = [orient(points, i, i + 1, j) for j in range(i + 2, len(points))]
        if 0 in row or min(row) < 0 < max(row):
            return None
        signs.append(1 if row[0] > 0 else -1)
    return signs


def has_cap_cup_partition(points):
    """Partition all vertices into two monochromatic chains, in either order."""
    n = len(points)
    for cap_sign, cup_sign in ((-1, 1), (1, -1)):
        for mask in range(1 << n):
            cap = [i for i in range(n) if (mask >> i) & 1]
            cup = [i for i in range(n) if not ((mask >> i) & 1)]
            if monochromatic(points, cap, cap_sign) and monochromatic(points, cup, cup_sign):
                return True
    return False


def has_shared_right_split(points):
    """Cover by opposite-sign chains sharing the rightmost vertex."""
    n = len(points)
    right = n - 1
    for cap_sign, cup_sign in ((-1, 1), (1, -1)):
        for mask in range(1 << (n - 1)):
            cap = [i for i in range(n - 1) if (mask >> i) & 1] + [right]
            cup = [i for i in range(n - 1) if not ((mask >> i) & 1)] + [right]
            if monochromatic(points, cap, cap_sign) and monochromatic(points, cup, cup_sign):
                return True
    return False


def hull(points, vertices):
    vertices = sorted(vertices, key=lambda i: points[i])
    if len(vertices) <= 1:
        return vertices

    def build(order):
        chain = []
        for k in order:
            while len(chain) >= 2 and orient(points, chain[-2], chain[-1], k) <= 0:
                chain.pop()
            chain.append(k)
        return chain

    lower = build(vertices)
    upper = build(reversed(vertices))
    return lower[:-1] + upper[:-1]


def convex(points, vertices):
    return len(hull(points, vertices)) == len(vertices)


def maximum_convex_size(points):
    n = len(points)
    for size in range(n, 2, -1):
        if any(convex(points, subset) for subset in combinations(range(n), size)):
            return size
    return min(n, 2)


def fixed_witnesses():
    same_sign = [(i, y) for i, y in enumerate((0, 93, 126, 199, 232, 255))]
    assert hinged(same_sign) == [-1, 1, -1, -1]
    assert orient(same_sign, 0, 2, 3) > 0

    nonsplit = [(i, y) for i, y in enumerate((0, 41, 42, 93, 134))]
    assert hinged(nonsplit) == [-1, 1, -1]
    assert not has_shared_right_split(nonsplit)

    uncolorable = [
        (i, y) for i, y in enumerate((-304, -291, -153, -180, -171, -36, -45))
    ]
    assert hinged(uncolorable) == [1, -1, 1, 1, -1]
    assert all(orient(uncolorable, i, j, k) != 0
               for i, j, k in combinations(range(7), 3))
    assert not has_cap_cup_partition(uncolorable)
    assert maximum_convex_size(uncolorable) == 6

    # Hinged structure alone need not improve even the seven-point
    # Erdos--Szekeres guarantee: this history has no convex 5-set.
    locally_extremal = [
        (i, y) for i, y in enumerate((26247, 14652, 13424, -8160, 2640, 2688, 1680))
    ]
    assert hinged(locally_extremal) == [1, -1, 1, -1, -1]
    assert all(orient(locally_extremal, i, j, k) != 0
               for i, j, k in combinations(range(7), 3))
    assert maximum_convex_size(locally_extremal) == 4

    # In fact the hinged class realizes the sharp eight-point obstruction
    # for a convex pentagon.
    pentagon_extremal = [
        (i, y) for i, y in enumerate((-10, -31, -11, -17, -5, -7, 3, -5))
    ]
    assert hinged(pentagon_extremal) == [1, -1, 1, -1, 1, -1]
    assert all(orient(pentagon_extremal, i, j, k) != 0
               for i, j, k in combinations(range(8), 3))
    assert maximum_convex_size(pentagon_extremal) == 4


def least_index_family(n):
    """Return integer points with chi(i,j,k)=sigma_i, sigma_i alternating."""
    m = 4 * n
    signs = [1 if i % 2 == 0 else -1 for i in range(n - 2)]
    points = [(i, signs[i] * m ** (n - i)) for i in range(n - 2)]
    points += [(n - 2, 0), (n - 1, 0)]
    for i, j, k in combinations(range(n), 3):
        assert signs[i] * orient(points, i, j, k) > 0
    assert hinged(points) == signs
    return points, signs


def infinite_family_checks():
    observed = []
    for n in range(4, 15):
        points, signs = least_index_family(n)
        observed.append(maximum_convex_size(points))
        assert observed[-1] == ceil(n / 2) + 1

        # An explicit cap/cup cover sharing the right endpoint.  Vertex n-2
        # can go into either chain because it is penultimate there.
        negative = [i for i, sign in enumerate(signs) if sign < 0] + [n - 2, n - 1]
        positive = [i for i, sign in enumerate(signs) if sign > 0] + [n - 1]
        assert set(negative) | set(positive) == set(range(n))
        assert monochromatic(points, negative, -1)
        assert monochromatic(points, positive, 1)

    assert observed == [3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]

    # Small exhaustive instance of the general balanced-history assertion:
    # every 6-set with three signs of each type has no contained convex
    # subset larger than 6/2+2=5.
    points, signs = least_index_family(12)
    labelled = range(10)
    for subset in combinations(labelled, 6):
        if sum(signs[i] > 0 for i in subset) == 3:
            assert not convex(points, subset)


if __name__ == "__main__":
    fixed_witnesses()
    infinite_family_checks()
    print("all exact history-obstruction checks passed")
