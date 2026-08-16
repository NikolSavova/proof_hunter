#!/usr/bin/env python3
"""Exact verifier for RENYI3_CONTINUATION_COLLISION_OR_DENSE_FACE_CORE."""

from fractions import Fraction as F
from itertools import combinations
from math import comb


def prune_core(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total = sum(sum(row) for row in matrix)
    active_r = {i for i in range(rows) if any(matrix[i][j] for j in range(cols))}
    active_c = {j for j in range(cols) if any(matrix[i][j] for i in range(rows))}
    row_support, col_support = len(active_r), len(active_c)
    if total == 0:
        return active_r, active_c, F(0)
    row_cut = F(total, 4 * row_support)
    col_cut = F(total, 4 * col_support)

    changed = True
    while changed:
        changed = False
        for i in list(active_r):
            degree = sum(matrix[i][j] for j in active_c)
            if degree < row_cut:
                active_r.remove(i)
                changed = True
        for j in list(active_c):
            degree = sum(matrix[i][j] for i in active_r)
            if degree < col_cut:
                active_c.remove(j)
                changed = True
    core = sum(matrix[i][j] for i in active_r for j in active_c)
    assert core >= total / 2
    assert all(sum(matrix[i][j] for j in active_c) >= row_cut
               for i in active_r)
    assert all(sum(matrix[i][j] for i in active_r) >= col_cut
               for j in active_c)
    return active_r, active_c, core


def audit_weighted_matrices():
    checked = 0
    # Exhaust all 2x3 matrices with entries in {0,1,2,3}.
    for code in range(4 ** 6):
        digits, x = [], code
        for _ in range(6):
            digits.append(F(x % 4))
            x //= 4
        matrix = [digits[:3], digits[3:]]
        total = sum(digits)
        if total == 0:
            continue
        columns = [sum(matrix[i][j] for i in range(2)) for j in range(3)]
        cube_sum = sum(d ** 3 for d in columns)
        k3_squared = total ** 3 / cube_sum
        support = sum(d > 0 for d in columns)
        assert k3_squared <= support ** 2

        rows, cols, core = prune_core(matrix)
        core_columns = [sum(matrix[i][j] for i in rows) for j in cols]
        core_cube = sum(d ** 3 for d in core_columns)
        core_k3_squared = core ** 3 / core_cube
        # This is (9) with alpha=1, squared.
        assert core_k3_squared >= k3_squared / 8
        checked += 1
    return checked


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 2:
        return points

    def half(seq):
        out = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(list(reversed(points)))[:-1]


def ordinary(points):
    return len(hull(points)) == len(set(points))


def subsets(points):
    for mask in range(1, 1 << len(points)):
        yield tuple(points[i] for i in range(len(points)) if mask >> i & 1)


G0 = (F(1, 100), F(50099, 10000))
X0 = (F(0), F(-4))


def cloud(center, size, sign):
    epsilon = F(1, 100000 * size * size)
    return [
        (center[0] + epsilon * i,
         center[1] + epsilon * epsilon * sign * i * i)
        for i in range(1, size + 1)
    ]


def audit_two_cloud_regression():
    checked = 0
    last = None
    for p in range(3, 8):
        Y = cloud(G0, p, 1)
        Z = cloud(X0, p, -1)
        assert all(ordinary(face) for face in subsets(Y))
        assert all(ordinary(face) for face in subsets(Z))

        y_faces, z_faces = list(subsets(Y)), list(subsets(Z))
        crossing = sum(ordinary(left + right)
                       for left in y_faces for right in z_faces)
        small = p + comb(p, 2)
        total = (1 << p) - 1
        assert crossing == small * small
        assert 2 * total + crossing == 2 * total + small * small

        r = max(3, p // 2)
        if r <= p:
            left_layer = list(combinations(Y, r))
            right_layer = list(combinations(Z, r))
            assert all(not ordinary(left + right)
                       for left in left_layer for right in right_layer)
            m = comb(p, r)
            weight = m * m
            column_masses = [m] * m
            k3_squared = F(weight ** 3,
                            sum(d ** 3 for d in column_masses))
            assert k3_squared == m * m
            last = (p, r, m, weight, 2 * total + small * small)
        checked += 1
    return checked, last


def main():
    matrices = audit_weighted_matrices()
    clouds, last = audit_two_cloud_regression()
    print(
        "PASS: weighted-matrices=%d; cloud-sizes=%d; "
        "last(p,r,M,W,V)=%s"
        % (matrices, clouds, last)
    )


if __name__ == "__main__":
    main()
