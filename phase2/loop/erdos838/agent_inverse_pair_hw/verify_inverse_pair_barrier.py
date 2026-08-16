#!/usr/bin/env python3
"""Exact certificates for the inverse-pair barrier in the HW2 attack.

All arithmetic is rational.  A root (i,j,w), i<j, denotes the row
transvection I + w*z*E_{j,i}.  Processing the listed roots in order therefore
forms B by successive row updates, while processing the reversed list forms
A=B(-z)^(-1).
"""

from fractions import Fraction as Q
from itertools import permutations


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    out = [Q(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        out[i] += x
    for i, x in enumerate(q):
        out[i] += x
    return trim(out)


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def neg_argument(p):
    return [x if i % 2 == 0 else -x for i, x in enumerate(p)]


def evaluate(p, z):
    return sum((x * z**i for i, x in enumerate(p)), Q(0))


def identity(n):
    return [[[Q(i == j)] for j in range(n)] for i in range(n)]


def polynomial_matrix(coefficient_matrices):
    """Convert [M_0,M_1,...] to a matrix of coefficient lists."""
    n = len(coefficient_matrices[0])
    return [
        [
            trim([Q(matrix[i][j]) for matrix in coefficient_matrices])
            for j in range(n)
        ]
        for i in range(n)
    ]


def factor_product(n, roots):
    """Return the polynomial matrix made by the listed row updates."""
    matrix = identity(n)
    for i, j, weight in roots:
        assert 0 <= i < j < n and weight > 0
        for column in range(n):
            increment = [Q(0)] + [weight * x for x in matrix[i][column]]
            matrix[j][column] = add(matrix[j][column], increment)
    return matrix


def matrix_product(left, right):
    n = len(left)
    out = [[[Q(0)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            value = [Q(0)]
            for k in range(n):
                value = add(value, mul(left[i][k], right[k][j]))
            out[i][j] = value
    return out


def substitute_minus(matrix):
    return [[neg_argument(entry) for entry in row] for row in matrix]


def assert_inverse_pair(a, b):
    n = len(a)
    assert matrix_product(substitute_minus(b), a) == identity(n)
    assert matrix_product(a, substitute_minus(b)) == identity(n)
    for matrix in (a, b):
        for row in matrix:
            for entry in row:
                assert all(coefficient >= 0 for coefficient in entry)


def f_profile(n, roots, verify_inverse=True):
    b = factor_product(n, roots)
    a = factor_product(n, reversed(roots))
    if verify_inverse:
        assert_inverse_pair(a, b)
    frobenius = [Q(0)]
    for i in range(n):
        for j in range(n):
            frobenius = add(frobenius, mul(a[i][j], b[i][j]))
    # F(z) = 1+nz+<A,B>-n.
    frobenius[0] -= n - 1
    return add(frobenius, [Q(0), Q(n)])


def h_value(n, profile):
    return Q(n) * evaluate(profile, Q(1, 2)) / evaluate(profile, Q(1))


def unit_roots(root_pairs):
    return [(i, j, Q(1)) for i, j in root_pairs]


def reflection_violations(n, root_pairs):
    position = {root: k for k, root in enumerate(root_pairs)}
    assert len(position) == n * (n - 1) // 2
    bad = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x = position[i, j]
                y = position[i, k]
                z = position[j, k]
                if not (x < y < z or z < y < x):
                    bad.append((i, j, k))
    return bad


def certify_counterexamples():
    # IP0: even the identity pair has nonnegative coefficients, determinant
    # one, and A=B(-z)^(-1), but violates HW2 from n=4 onward.
    empty = f_profile(4, [])
    assert empty == [Q(1), Q(4)]
    assert h_value(4, empty) == Q(12, 5) > 2

    # IP1: using n-1 distinct unit positive-root factors is still insufficient.
    # These star factors commute and their pairwise products vanish.
    star = f_profile(5, unit_roots([(0, j) for j in range(1, 5)]))
    assert star == [Q(1), Q(5), Q(4)]
    assert h_value(5, star) == Q(9, 4) > 2

    # IP2: completeness without unit normalization is insufficient.  This is
    # the lexicographic reflection order; star weights are 1 and all six other
    # positive roots have weight epsilon=1/5.
    epsilon = Q(1, 5)
    weighted_lex = [
        (i, j, Q(1) if i == 0 else epsilon)
        for i in range(5)
        for j in range(i + 1, 5)
    ]
    weighted = f_profile(5, weighted_lex)
    assert reflection_violations(5, [(i, j) for i, j, _ in weighted_lex]) == []
    assert weighted == [
        Q(1), Q(5), Q(106, 25), Q(154, 125), Q(101, 625), Q(1, 125)
    ]
    assert h_value(5, weighted) == Q(472435, 232832) > 2
    assert 5 * evaluate(weighted, Q(1, 2)) - 2 * evaluate(weighted, Q(1)) == Q(6771, 20000)

    return empty, star, weighted


def certify_arbitrary_unit_orders():
    # A non-reflection order attaining the exhaustive n=5 arbitrary-order
    # maximum found by arbitrary_root_order.cpp.  It still satisfies HW2.
    max_pairs = [
        (0, 1), (0, 2), (0, 3), (0, 4), (1, 4),
        (2, 3), (2, 4), (1, 2), (3, 4), (1, 3),
    ]
    profile = f_profile(5, unit_roots(max_pairs))
    assert profile == [Q(1), Q(5), Q(10), Q(10), Q(1)]
    assert h_value(5, profile) == Q(65, 48) < 2
    assert reflection_violations(5, max_pairs) == [
        (1, 2, 3), (1, 2, 4), (1, 3, 4)
    ]

    # Outside reflection orders, the Frobenius coefficients need not be an
    # f-vector: the degree can exceed n and a coefficient can exceed C(n,k).
    nonsquarefree_pairs = [
        (0, 1), (1, 2), (2, 4), (3, 4), (2, 3),
        (0, 2), (0, 3), (0, 4), (1, 3), (1, 4),
    ]
    nonsquarefree = f_profile(5, unit_roots(nonsquarefree_pairs))
    assert nonsquarefree == [Q(1), Q(5), Q(10), Q(10), Q(7), Q(4), Q(1)]
    assert reflection_violations(5, nonsquarefree_pairs)

    # Exhaust all 6! orders at n=4.  Besides reproducing the exact arbitrary-
    # order maximum, this checks the order-independent q2 and q3 laws.
    roots4 = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    best_h = Q(-1)
    maximizers = 0
    for order in permutations(roots4):
        # The exact factor construction itself proves A=B(-z)^(-1); it has
        # already been checked explicitly above, so avoid 720 redundant full
        # polynomial matrix multiplications here.
        current = f_profile(4, unit_roots(order), verify_inverse=False)
        assert current[2] == Q(6)
        assert current[3] == Q(4)
        score = h_value(4, current)
        if score > best_h:
            best_h = score
            maximizers = 1
        elif score == best_h:
            maximizers += 1
    assert best_h == Q(4, 3)
    assert maximizers > 0

    return profile, nonsquarefree, best_h, maximizers


def certify_total_positivity_obstruction():
    # Lexicographic order is a genuine A2 reflection order.  At z=1 its B is
    # [[1,0,0],[1,1,0],[2,1,1]], whose indicated 2x2 minor is -1.
    roots = unit_roots([(0, 1), (0, 2), (1, 2)])
    b = factor_product(3, roots)
    value = [[evaluate(entry, Q(1)) for entry in row] for row in b]
    assert value == [[1, 0, 0], [1, 1, 0], [2, 1, 1]]
    minor = value[1][0] * value[2][1] - value[1][1] * value[2][0]
    assert minor == -1
    return value, minor


def certify_complete_linear_jet_obstruction():
    """An exact positive inverse pair with B_1=A_1=sum positive roots.

    This pair need not factor as a product containing every root transvection.
    It proves that coefficient positivity, inversion, and even the complete
    first-order type-A root datum do not imply the proposed graded p_3 bound.
    """
    n = 6
    zero = [[0] * n for _ in range(n)]
    one = [[int(i == j) for j in range(n)] for i in range(n)]
    s = [[int(i > j) for j in range(n)] for i in range(n)]
    a2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [3, 2, 1, 0, 0, 0],
        [0, 3, 0, 0, 0, 0],
    ]
    b2 = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [4, 0, 2, 1, 0, 0],
    ]
    a3 = [row[:] for row in zero]
    a3[4][1] = 1
    a = polynomial_matrix([one, s, a2, a3])
    b = polynomial_matrix([one, s, b2])
    assert_inverse_pair(a, b)

    frobenius = [Q(0)]
    for i in range(n):
        for j in range(n):
            frobenius = add(frobenius, mul(a[i][j], b[i][j]))
    frobenius[0] -= n - 1
    profile = add(frobenius, [Q(0), Q(n)])
    assert profile == [Q(1), Q(6), Q(15), Q(20), Q(1)]

    # p_r=(r+1)v_(r+1)/((n-r)v_r).  Thus p_3=1/15, whereas
    # the clean finite target 2^(-3) is 1/8.
    p3 = Q(4) * profile[4] / (Q(n - 3) * profile[3])
    assert p3 == Q(1, 15) < Q(1, 8)
    return profile, p3


def main():
    empty, star, weighted = certify_counterexamples()
    arbitrary, nonsquarefree, best4, count4 = certify_arbitrary_unit_orders()
    b3, minor = certify_total_positivity_obstruction()
    jet_profile, p3 = certify_complete_linear_jet_obstruction()
    print("exact inverse-pair barrier: PASS")
    print(f"identity n=4: profile={empty}, H={h_value(4, empty)}")
    print(f"unit star n=5: profile={star}, H={h_value(5, star)}")
    print(f"weighted complete reflection order n=5: profile={weighted}, H={h_value(5, weighted)}")
    print(f"arbitrary unit full order n=5: profile={arbitrary}, H={h_value(5, arbitrary)}")
    print(f"nonsquarefree arbitrary order: profile={nonsquarefree}")
    print(f"all 720 unit full orders n=4: max H={best4}, maximizers={count4}")
    print(f"valid A2 reflection-order B(1)={b3}, negative minor={minor}")
    print(f"complete-linear-data positive inverse pair: profile={jet_profile}, p3={p3}<1/8")


if __name__ == "__main__":
    main()
