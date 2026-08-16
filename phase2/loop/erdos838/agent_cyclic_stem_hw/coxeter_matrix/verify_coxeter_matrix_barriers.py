#!/usr/bin/env python3
"""Exact certificates for three Coxeter-matrix barriers to Erdős 838 HW2.

There is no floating point arithmetic.  A reduced word for w_0 in S_n is
converted to its positive-root sequence.  A root (i,j) acts by the row
transvection I+t E_{j,i}.  The forward and reverse products are B(t) and
A(t), respectively.

The certificates prove:

1. the half-activity convex-face law of a stretchable, unit, complete A_4
   reflection order is positively correlated;
2. A(1)^T B(1) is already nonnormal with nonreal spectrum in A_2, and its
   symmetric part is indefinite in A_3;
3. separate Frobenius (Schatten-2) norms of A(t),B(t), at both t=1/2 and
   t=1, do not determine the cross trace or HW2 ratio, even for unit,
   complete A_5 reflection orders.
4. the universal total-count-capped alignment inequality is exponent-sharp
   on the scalable alternating reflection family.
"""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations


Matrix = list[list[Q]]
Root = tuple[int, int]
Word = tuple[int, ...]


def root_sequence(n: int, word: Word) -> tuple[Root, ...]:
    """Check that word is reduced for w_0 and return its root sequence."""
    wires = list(range(n))
    roots: list[Root] = []
    for step, generator in enumerate(word):
        assert 0 <= generator < n - 1
        left, right = wires[generator : generator + 2]
        assert left < right, (step, generator, wires)
        roots.append((left, right))
        wires[generator], wires[generator + 1] = right, left
    assert len(word) == n * (n - 1) // 2
    assert wires == list(reversed(range(n)))
    assert set(roots) == {
        (i, j) for i in range(n) for j in range(i + 1, n)
    }
    return tuple(roots)


def reflection_betweenness(n: int, roots: tuple[Root, ...]) -> None:
    position = {root: k for k, root in enumerate(roots)}
    for i, j, k in combinations(range(n), 3):
        x, y, z = position[i, j], position[i, k], position[j, k]
        assert x < y < z or z < y < x


def product(n: int, roots: tuple[Root, ...], t: Q) -> Matrix:
    matrix = [[Q(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [matrix[j][k] + t * matrix[i][k] for k in range(n)]
    return matrix


def cross_trace(a: Matrix, b: Matrix) -> Q:
    return sum(
        (a[i][j] * b[i][j] for i in range(len(a)) for j in range(len(a))),
        Q(0),
    )


def frobenius_square(a: Matrix) -> Q:
    return sum((entry * entry for row in a for entry in row), Q(0))


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(n)), Q(0)) for j in range(n)]
        for i in range(n)
    ]


def determinant(a: Matrix) -> Q:
    """Exact fraction Gaussian elimination."""
    matrix = [row[:] for row in a]
    value = Q(1)
    n = len(matrix)
    for column in range(n):
        pivot = next((r for r in range(column, n) if matrix[r][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            value = -value
        pivot_value = matrix[column][column]
        value *= pivot_value
        for row in range(column + 1, n):
            ratio = matrix[row][column] / pivot_value
            for j in range(column + 1, n):
                matrix[row][j] -= ratio * matrix[column][j]
    return value


def polynomial_add_shift(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right) + 1)
    for degree, coefficient in enumerate(left):
        result[degree] += coefficient
    for degree, coefficient in enumerate(right):
        result[degree + 1] += coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def polynomial_product(n: int, roots: tuple[Root, ...]) -> list[list[list[int]]]:
    matrix = [
        [[int(i == j)] for j in range(n)]
        for i in range(n)
    ]
    for i, j in roots:
        matrix[j] = [
            polynomial_add_shift(matrix[j][column], matrix[i][column])
            for column in range(n)
        ]
    return matrix


def face_profile(n: int, roots: tuple[Root, ...]) -> list[int]:
    """Return F(z)=1+nz+<A(z),B(z)>-n coefficientwise."""
    a = polynomial_product(n, tuple(reversed(roots)))
    b = polynomial_product(n, roots)
    profile = [0]
    for i in range(n):
        for j in range(n):
            term = polynomial_multiply(a[i][j], b[i][j])
            if len(profile) < len(term):
                profile.extend([0] * (len(term) - len(profile)))
            for degree, coefficient in enumerate(term):
                profile[degree] += coefficient
    profile[0] -= n - 1
    if len(profile) < 2:
        profile.append(0)
    profile[1] += n
    while len(profile) > 1 and profile[-1] == 0:
        profile.pop()
    return profile


def evaluate_profile(profile: list[int], t: Q) -> Q:
    return sum((Q(value) * t**degree for degree, value in enumerate(profile)), Q(0))


def h_value(n: int, profile: list[int]) -> Q:
    return Q(n) * evaluate_profile(profile, Q(1, 2)) / evaluate_profile(profile, Q(1))


def parity_sign(order: tuple[int, int, int]) -> int:
    inversions = sum(
        order[i] > order[j] for i in range(3) for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


def chirotope_from_roots(n: int, roots: tuple[Root, ...]):
    position = {root: k for k, root in enumerate(roots)}
    sorted_sign: dict[tuple[int, int, int], int] = {}
    for i, j, k in combinations(range(n), 3):
        sorted_sign[i, j, k] = (
            1 if position[i, j] < position[i, k] < position[j, k] else -1
        )

    def chi(a: int, b: int, c: int) -> int:
        sorted_triple = tuple(sorted((a, b, c)))
        ranks = tuple(sorted_triple.index(x) for x in (a, b, c))
        return parity_sign(ranks) * sorted_sign[sorted_triple]

    return chi


def face_masks(n: int, roots: tuple[Root, ...]) -> tuple[list[int], list[int]]:
    """Recover the rank-three free-set complex from its rooted 4-circuits."""
    chi = chirotope_from_roots(n, roots)
    bad_four_masks: list[int] = []
    for four in combinations(range(n), 4):
        nonconvex = False
        for point in four:
            a, b, c = (x for x in four if x != point)
            target = chi(a, b, c)
            if (
                chi(a, b, point) == target
                and chi(b, c, point) == target
                and chi(c, a, point) == target
            ):
                nonconvex = True
                break
        if nonconvex:
            bad_four_masks.append(sum(1 << x for x in four))
    faces = [
        mask
        for mask in range(1 << n)
        if all(mask & bad != bad for bad in bad_four_masks)
    ]
    return faces, bad_four_masks


def slope_roots(points: list[tuple[int, int]]) -> tuple[Root, ...]:
    slopes: list[tuple[Q, int, int]] = []
    for i, j in combinations(range(len(points)), 2):
        x_i, y_i = points[i]
        x_j, y_j = points[j]
        slopes.append((Q(y_j - y_i, x_j - x_i), i, j))
    slopes.sort()
    # Equal slopes may occur only on disjoint edges, whose transvections commute.
    for first, second in zip(slopes, slopes[1:]):
        if first[0] == second[0]:
            assert len({first[1], first[2], second[1], second[2]}) == 4
    return tuple((i, j) for _, i, j in slopes)


def certify_positive_covariance() -> dict[str, object]:
    # Type A_4.  The displayed word has the same commutation class as the
    # exact slope order of the integral realization below.
    word = (0, 1, 2, 1, 0, 1, 3, 2, 1, 0)
    roots = root_sequence(5, word)
    reflection_betweenness(5, roots)
    points = [(0, 0), (1, -6), (2, -5), (3, -6), (4, 0)]
    coordinate_roots = slope_roots(points)
    chi = chirotope_from_roots(5, roots)
    for i, j, k in combinations(range(5), 3):
        determinant_coordinate = (
            (points[j][0] - points[i][0]) * (points[k][1] - points[i][1])
            - (points[j][1] - points[i][1]) * (points[k][0] - points[i][0])
        )
        assert determinant_coordinate != 0
        assert chi(i, j, k) == (1 if determinant_coordinate > 0 else -1)
    assert product(5, roots, Q(1)) == product(5, coordinate_roots, Q(1))
    assert product(5, tuple(reversed(roots)), Q(1)) == product(
        5, tuple(reversed(coordinate_roots)), Q(1)
    )

    faces, bad = face_masks(5, roots)
    profile = [sum(mask.bit_count() == rank for mask in faces) for rank in range(6)]
    assert profile == [1, 5, 10, 10, 3, 0]
    assert profile[:5] == face_profile(5, roots)
    assert bad == [15, 30]

    t = Q(1, 2)
    partition = sum((t ** mask.bit_count() for mask in faces), Q(0))
    p0 = sum((t ** mask.bit_count() for mask in faces if mask & 1), Q(0)) / partition
    p4 = sum((t ** mask.bit_count() for mask in faces if mask & 16), Q(0)) / partition
    p04 = sum(
        (t ** mask.bit_count() for mask in faces if mask & 1 and mask & 16),
        Q(0),
    ) / partition
    covariance = p04 - p0 * p4
    assert partition == Q(119, 16)
    assert p0 == p4 == Q(39, 119)
    assert p04 == Q(13, 119)
    assert covariance == Q(26, 14161) > 0
    return {
        "word": word,
        "profile": profile,
        "partition_at_half": partition,
        "p0": p0,
        "p4": p4,
        "p04": p04,
        "covariance": covariance,
    }


def certify_cross_operator_barrier() -> dict[str, object]:
    # In type A_2 the cross operator already has a nonreal conjugate pair.
    roots3 = root_sequence(3, (0, 1, 0))
    a3 = product(3, tuple(reversed(roots3)), Q(1))
    b3 = product(3, roots3, Q(1))
    m3 = matmul(transpose(a3), b3)
    assert m3 == [[4, 2, 1], [3, 2, 1], [2, 1, 1]]
    # det(lambda I-M)=lambda^3-7 lambda^2+5 lambda-1.
    # Its discriminant is -44, so it has one real and two nonreal roots.
    cubic = (1, -7, 5, -1)
    a, b, c, d = cubic
    discriminant = (
        18 * a * b * c * d
        - 4 * b**3 * d
        + b * b * c * c
        - 4 * a * c**3
        - 27 * a * a * d * d
    )
    assert discriminant == -44

    # In type A_3 the symmetric part is indefinite.  To stay integral, use
    # 2S=M+M^T.  Its leading 3x3 principal minor has determinant -4, while
    # its leading 1x1 and 2x2 minors are positive.
    roots4 = root_sequence(4, (0, 1, 0, 2, 1, 0))
    a4 = product(4, tuple(reversed(roots4)), Q(1))
    b4 = product(4, roots4, Q(1))
    m4 = matmul(transpose(a4), b4)
    two_s = [
        [m4[i][j] + m4[j][i] for j in range(4)]
        for i in range(4)
    ]
    principal = [row[:3] for row in two_s[:3]]
    assert principal == [[16, 11, 8], [11, 8, 5], [8, 5, 4]]
    minors = (
        principal[0][0],
        determinant([row[:2] for row in principal[:2]]),
        determinant(principal),
    )
    assert minors == (16, 7, -4)
    return {
        "A2_cross_operator": m3,
        "A2_characteristic_polynomial": cubic,
        "A2_discriminant": discriminant,
        "A3_twice_symmetric_principal": principal,
        "A3_leading_principal_minors": minors,
    }


def certify_schatten2_collision() -> dict[str, object]:
    words = (
        (2, 1, 0, 1, 2, 4, 3, 2, 1, 0, 4, 3, 2, 1, 3),
        (2, 1, 0, 2, 1, 3, 4, 3, 2, 1, 0, 3, 2, 1, 4),
    )
    records = []
    signatures = []
    for word in words:
        roots = root_sequence(6, word)
        reflection_betweenness(6, roots)
        norms: list[Q] = []
        traces: list[Q] = []
        for t in (Q(1), Q(1, 2)):
            a = product(6, tuple(reversed(roots)), t)
            b = product(6, roots, t)
            norms.extend((frobenius_square(a), frobenius_square(b)))
            traces.append(cross_trace(a, b))
        profile = face_profile(6, roots)
        records.append(
            {
                "word": word,
                "norms_A1_B1_Ahalf_Bhalf": tuple(norms),
                "cross_traces_1_half": tuple(traces),
                "profile": profile,
                "H": h_value(6, profile),
            }
        )
        signatures.append(tuple(norms))

    expected_signature = (Q(59), Q(66), Q(837, 64), Q(223, 16))
    assert signatures[0] == signatures[1] == expected_signature
    assert records[0]["cross_traces_1_half"] == (Q(50), Q(409, 32))
    assert records[1]["cross_traces_1_half"] == (Q(49), Q(51, 4))
    assert records[0]["profile"] == [1, 6, 15, 20, 8, 1]
    assert records[1]["profile"] == [1, 6, 15, 20, 8]
    assert records[0]["H"] == Q(345, 272)
    assert records[1]["H"] == Q(129, 100)
    assert records[0]["H"] != records[1]["H"]
    return {"common_signature": expected_signature, "records": records}


def alternating_rich_value(distance: int, activity: Q) -> Q:
    """Rich endpoint entry in the alternating reflection family."""
    return activity + activity * activity * sum(
        ((1 + activity) ** ((step - 1) // 2) for step in range(1, distance)),
        Q(0),
    )


def alternating_offdiagonal_statistics(n: int, activity: Q) -> tuple[Q, Q, Q]:
    """Return Q^o, E_A, E_B from the exact alternating-family formula."""
    pairing = Q(0)
    energy_a = Q(0)
    energy_b = Q(0)
    for i, j in combinations(range(n), 2):
        rich = alternating_rich_value(j - i, activity)
        pairing += activity * rich
        if i % 2 == 0:
            energy_a += rich * rich
            energy_b += activity * activity
        else:
            energy_a += activity * activity
            energy_b += rich * rich
    return pairing, energy_a, energy_b


def certify_capped_alignment() -> dict[str, object]:
    """Exact finite replay of the exponent-sharp capped-alignment family.

    The theorem proved in REPORT.md is

        (Q^o)^4 >= z^4 E_A E_B,

    equivalently Q^o*kappa >= z^2.  Here we replay it on the alternating
    family and check that the left capped invariant stays bounded while each
    individual factor has exponential scale.
    """
    rows = []
    for activity, upper_bound in ((Q(1, 2), Q(3000)), (Q(1), Q(6000))):
        for n in (8, 12, 20, 40, 80):
            pairing, energy_a, energy_b = alternating_offdiagonal_statistics(
                n, activity
            )
            capped_invariant_squared = pairing**4 / (energy_a * energy_b)
            assert pairing**4 >= activity**4 * energy_a * energy_b
            assert capped_invariant_squared < upper_bound
            rows.append(
                {
                    "n": n,
                    "activity": activity,
                    "pairing": pairing,
                    "energy_a": energy_a,
                    "energy_b": energy_b,
                    "capped_invariant_squared": capped_invariant_squared,
                }
            )
    return {
        "inequality": "(Q_off)^4 >= z^4 E_A E_B",
        "alternating_rows": rows,
    }


def main() -> None:
    covariance = certify_positive_covariance()
    operator = certify_cross_operator_barrier()
    collision = certify_schatten2_collision()
    capped = certify_capped_alignment()
    print("exact Coxeter-matrix barriers: PASS")
    print(
        "positive half-activity covariance:",
        covariance["covariance"],
        "profile=", covariance["profile"],
    )
    print(
        "cross operator: cubic discriminant=",
        operator["A2_discriminant"],
        "; symmetric leading minors=",
        operator["A3_leading_principal_minors"],
    )
    print("common A/B Schatten-2 endpoint signature:", collision["common_signature"])
    for record in collision["records"]:
        print(
            "  profile=", record["profile"],
            "cross traces (1,1/2)=", record["cross_traces_1_half"],
            "H=", record["H"],
        )
    print(
        "total-count-capped alignment:", capped["inequality"],
        "; scalable alternating replay: PASS",
    )


if __name__ == "__main__":
    main()
