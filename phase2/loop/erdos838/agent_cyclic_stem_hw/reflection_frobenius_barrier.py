#!/usr/bin/env python3
"""Exact audit of the alternating reflection-order Frobenius barrier.

The construction has chirotope chi(i,j,k)=(-1)^i.  It is realized by
fixed-x integer points.  Every positive root occurs once, and the resulting
root order satisfies type-A reflection betweenness.
"""

from __future__ import annotations

from fractions import Fraction
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def determinant(points, i: int, j: int, k: int) -> int:
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]
    return (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)


def alternating_points(n: int) -> list[tuple[int, int]]:
    """Integral realization of chi(i,j,k)=(-1)^i."""

    if n < 4:
        raise ValueError("use n>=4")
    multiplier = 4 * n + 1
    heights = [
        ((-1) ** index) * multiplier ** (n - index)
        for index in range(n - 2)
    ] + [0, 0]
    points = list(enumerate(heights))
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                value = determinant(points, i, j, k)
                assert value != 0
                assert (value > 0) == (i % 2 == 0)
    return points


def root_order(points) -> tuple[tuple[int, int], ...]:
    roots = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            numerator = points[j][1] - points[i][1]
            denominator = points[j][0] - points[i][0]
            roots.append((Fraction(numerator, denominator), i, j))
    roots.sort()
    result = tuple((i, j) for _slope, i, j in roots)
    assert len(result) == n * (n - 1) // 2
    assert len(set(result)) == len(result)
    position = {root: rank for rank, root in enumerate(result)}
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                packet = (
                    position[(i, j)],
                    position[(i, k)],
                    position[(j, k)],
                )
                assert packet[0] < packet[1] < packet[2] or (
                    packet[2] < packet[1] < packet[0]
                )
    return result


def poly_add_shift(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * max(len(left), len(right) + 1)
    for degree, value in enumerate(left):
        result[degree] += value
    for degree, value in enumerate(right):
        result[degree + 1] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def polynomial_matrix(
    n: int, roots: tuple[tuple[int, int], ...]
) -> list[list[tuple[int, ...]]]:
    matrix = [
        [(1,) if row == column else (0,) for column in range(n)]
        for row in range(n)
    ]
    for i, j in roots:
        matrix[j] = [
            poly_add_shift(matrix[j][column], matrix[i][column])
            for column in range(n)
        ]
    return matrix


def rich_polynomial(distance: int) -> tuple[int, ...]:
    """R_d(z)=z+z^2 sum_(s<d)(1+z)^floor((s-1)/2)."""

    if distance < 1:
        raise ValueError("distance must be positive")
    result = [0, 1]
    for step in range(1, distance):
        exponent = (step - 1) // 2
        for degree in range(exponent + 1):
            while len(result) <= degree + 2:
                result.append(0)
            result[degree + 2] += math.comb(exponent, degree)
    return tuple(result)


def check_entry_formula(n: int) -> dict[str, object]:
    points = alternating_points(n)
    roots = root_order(points)
    forward = polynomial_matrix(n, roots)
    reverse = polynomial_matrix(n, tuple(reversed(roots)))
    direct = (0, 1)
    for i in range(n):
        for j in range(i + 1, n):
            rich = rich_polynomial(j - i)
            if i % 2 == 0:
                assert forward[j][i] == rich
                assert reverse[j][i] == direct
            else:
                assert forward[j][i] == direct
                assert reverse[j][i] == rich
    return {
        "n": n,
        "positive_roots": len(roots),
        "entry_formula": "PASS",
        "reflection_betweenness": "PASS",
        "general_position": "PASS",
    }


def rich_value(distance: int, activity: Fraction) -> Fraction:
    q = 1 + activity
    return activity + activity * activity * sum(
        q ** ((step - 1) // 2) for step in range(1, distance)
    )


def exact_statistics(n: int, activity: Fraction) -> dict[str, Fraction]:
    """Return F, off-diagonal Q and the two marginal energies."""

    q_off = Fraction(0)
    energy_forward = Fraction(0)
    energy_reverse = Fraction(0)
    for i in range(n):
        for j in range(i + 1, n):
            rich = rich_value(j - i, activity)
            q_off += activity * rich
            if i % 2 == 0:
                energy_forward += rich * rich
                energy_reverse += activity * activity
            else:
                energy_forward += activity * activity
                energy_reverse += rich * rich
    partition = 1 + n * activity + q_off
    return {
        "F": partition,
        "Q_off": q_off,
        "E_forward": energy_forward,
        "E_reverse": energy_reverse,
        "cosine_squared": q_off * q_off / (energy_forward * energy_reverse),
    }


def fraction_record(value: Fraction) -> dict[str, object]:
    return {
        "exact": str(value),
        "decimal": float(value),
        "log2": math.log2(value.numerator) - math.log2(value.denominator),
    }


def asymptotic_rows() -> list[dict[str, object]]:
    rows = []
    for n in (8, 12, 20, 30, 40, 60, 80, 120, 160, 240):
        one = exact_statistics(n, Fraction(1))
        half = exact_statistics(n, Fraction(1, 2))
        alignment_ratio_squared = (
            one["cosine_squared"] / half["cosine_squared"]
        )
        energy_dilation_squared = (
            one["E_forward"] * one["E_reverse"]
            / (half["E_forward"] * half["E_reverse"])
        )
        pairing_dilation = one["Q_off"] / half["Q_off"]
        half_weight = n * half["F"] / one["F"]
        rows.append(
            {
                "n": n,
                "log2_alignment_ratio": (
                    math.log2(alignment_ratio_squared.numerator)
                    - math.log2(alignment_ratio_squared.denominator)
                ) / 2,
                "log2_marginal_energy_dilation": (
                    math.log2(energy_dilation_squared.numerator)
                    - math.log2(energy_dilation_squared.denominator)
                ) / 2,
                "pairing_dilation": fraction_record(pairing_dilation),
                "half_weight": fraction_record(half_weight),
            }
        )
    return rows


COLLISION_WORDS = (
    (0, 2, 1, 3, 2, 1, 4, 3, 2, 1, 0, 1, 2, 4, 3),
    (0, 3, 2, 1, 2, 4, 3, 2, 1, 0, 1, 4, 3, 2, 3),
)


def roots_from_word(n: int, word: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    wires = list(range(n))
    roots = []
    for generator in word:
        left, right = wires[generator], wires[generator + 1]
        assert left < right
        roots.append((left, right))
        wires[generator], wires[generator + 1] = right, left
    assert wires == list(reversed(range(n)))
    return tuple(roots)


def entry_multiset_collision() -> dict[str, object]:
    matrices = []
    profiles = []
    for word in COLLISION_WORDS:
        roots = roots_from_word(6, word)
        forward = polynomial_matrix(6, roots)
        reverse = polynomial_matrix(6, tuple(reversed(roots)))
        matrices.append(
            (
                tuple(sorted(value for row in forward for value in row)),
                tuple(sorted(value for row in reverse for value in row)),
            )
        )
        profile = [0]
        for row in range(6):
            for column in range(6):
                left, right = forward[row][column], reverse[row][column]
                product = [0] * (len(left) + len(right) - 1)
                for i, a in enumerate(left):
                    for j, b in enumerate(right):
                        product[i + j] += a * b
                while len(profile) < len(product):
                    profile.append(0)
                for degree, value in enumerate(product):
                    profile[degree] += value
        profile[0] -= 6
        profile[1] += 6
        profiles.append(tuple(profile))
    assert matrices[0][0] == matrices[1][1]
    assert matrices[0][1] == matrices[1][0]
    assert profiles == [(0, 6, 15, 20, 8, 1), (0, 6, 15, 20, 8)]
    return {
        "word_1": list(COLLISION_WORDS[0]),
        "word_2": list(COLLISION_WORDS[1]),
        "unordered_entry_polynomial_multisets_equal": True,
        "nonempty_profiles": [list(profile) for profile in profiles],
    }


def main() -> None:
    finite_checks = [check_entry_formula(n) for n in range(4, 15)]
    certificate = {
        "status": "PASS",
        "claim_boundary": (
            "scalable counterexample to polynomial/activity-stable "
            "Frobenius alignment; not a counterexample to HW"
        ),
        "finite_entry_checks": finite_checks,
        "asymptotic_rows": asymptotic_rows(),
        "entry_multiset_collision": entry_multiset_collision(),
    }
    output = HERE / "reflection_frobenius_barrier_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("reflection/Frobenius barrier audit: PASS")
    print("certificate:", output)


if __name__ == "__main__":
    main()
