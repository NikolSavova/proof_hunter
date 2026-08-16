#!/usr/bin/env python3
"""Exact linear algebra for the hull-curve and planar beta constraints."""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
from math import comb
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ERDOS838 = HERE.parent


def variables(n: int, maximum_hull: int = 4) -> list[tuple[int, int]]:
    return [
        (h, i)
        for h in range(3, maximum_hull + 1)
        for i in range(n - h + 1)
    ]


def constraint_system(n: int, maximum_hull: int = 4):
    """Return A,b for the hull partition and beta-reflection identities.

    The fixed general-position rows are g_(0,0)=1, g_(1,0)=n and
    g_(2,0)=binom(n,2).  Variables begin at hull size three.
    """

    labels = variables(n, maximum_hull)
    fixed = {(0, 0): 1, (1, 0): n, (2, 0): comb(n, 2)}
    matrix: list[list[Fraction]] = []
    rhs: list[Fraction] = []

    # G(x,1+x)=(1+x)^n, coefficient by coefficient.
    for degree in range(n + 1):
        matrix.append(
            [
                Fraction(comb(i, degree - h) if 0 <= degree - h <= i else 0)
                for h, i in labels
            ]
        )
        value = Fraction(comb(n, degree))
        for (h, i), count in fixed.items():
            if 0 <= degree - h <= i:
                value -= count * comb(i, degree - h)
        rhs.append(value)

    # For a Bernoulli-p restriction, the beta/free-set identity is
    #
    # p G_x(-p,1-p) + E(number of hull vertices)
    #   = np + np(1-p)^(n-1).
    #
    # The last term is the singleton-restriction correction.
    for degree in range(n + 1):
        row = []
        for h, i in labels:
            exterior = n - h - i
            offset = degree - h
            coefficient = 0
            if 0 <= offset <= i:
                coefficient += h * (-1) ** (h - 1 + offset) * comb(i, offset)
            if 0 <= offset <= exterior:
                coefficient += h * (-1) ** offset * comb(exterior, offset)
            row.append(Fraction(coefficient))
        matrix.append(row)

        value = Fraction(n if degree == 1 else 0)
        if 0 <= degree - 1 <= n - 1:
            value += n * comb(n - 1, degree - 1) * (-1) ** (degree - 1)
        for (h, i), count in fixed.items():
            exterior = n - h - i
            offset = degree - h
            coefficient = 0
            if 0 <= offset <= i:
                coefficient += h * (-1) ** (h - 1 + offset) * comb(i, offset)
            if 0 <= offset <= exterior:
                coefficient += h * (-1) ** offset * comb(exterior, offset)
            value -= count * coefficient
        rhs.append(value)
    return labels, matrix, rhs


def rref(matrix: list[list[Fraction]], rhs: list[Fraction]):
    augmented = [row[:] + [value] for row, value in zip(matrix, rhs)]
    rows = len(augmented)
    columns = len(augmented[0]) - 1
    pivots: list[int] = []
    active = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(active, rows) if augmented[row][column]), None
        )
        if pivot is None:
            continue
        augmented[active], augmented[pivot] = augmented[pivot], augmented[active]
        scale = augmented[active][column]
        augmented[active] = [entry / scale for entry in augmented[active]]
        for row in range(rows):
            if row != active and augmented[row][column]:
                scale = augmented[row][column]
                augmented[row] = [
                    left - scale * right
                    for left, right in zip(augmented[row], augmented[active])
                ]
        pivots.append(column)
        active += 1
    for row in augmented:
        if not any(row[:columns]) and row[-1]:
            raise AssertionError("inconsistent constraint system")
    return augmented, pivots


def affine_solution(n: int, maximum_hull: int = 4):
    labels, matrix, rhs = constraint_system(n, maximum_hull)
    reduced, pivots = rref(matrix, rhs)
    free = [column for column in range(len(labels)) if column not in pivots]
    base = [Fraction(0) for _ in labels]
    directions = [[Fraction(0) for _ in free] for _ in labels]
    for index, column in enumerate(free):
        directions[column][index] = 1
    for row, column in enumerate(pivots):
        base[column] = reduced[row][-1]
        for index, free_column in enumerate(free):
            directions[column][index] = -reduced[row][free_column]
    return labels, base, directions, free


def rank_four_formal_solution(n: int) -> dict[tuple[int, int], Fraction]:
    """Construct the canonical nonnegative rank-four formal solution.

    The RREF has adjacent-difference directions on the potentially negative
    hull-three rows.  Set each such difference to the least value which makes
    the row nonnegative, working from the right.  The mirrored row then stays
    nonnegative; this is audited exactly below for every requested n.
    """

    labels, base, directions, free = affine_solution(n, 4)
    dimension = len(free)
    differences = [Fraction(0) for _ in range(max(0, dimension - 1))]
    for label, value, direction in zip(labels, base, directions):
        if label[0] != 3 or value >= 0:
            continue
        nonzero = [(index, entry) for index, entry in enumerate(direction) if entry]
        if len(nonzero) != 2:
            raise AssertionError((n, label, value, nonzero))
        (left, plus), (right, minus) = nonzero
        if right != left + 1 or plus != 1 or minus != -1:
            raise AssertionError((n, label, value, nonzero))
        differences[left] = max(differences[left], -value)

    parameters = [Fraction(0) for _ in range(dimension)]
    for index in range(dimension - 2, -1, -1):
        parameters[index] = parameters[index + 1] + differences[index]

    values = []
    for value, direction in zip(base, directions):
        values.append(value + sum(a * b for a, b in zip(direction, parameters)))
    if any(value < 0 or value.denominator != 1 for value in values):
        raise AssertionError((n, min(values)))

    result = {(0, 0): Fraction(1), (1, 0): Fraction(n), (2, 0): Fraction(comb(n, 2))}
    result.update(dict(zip(labels, values)))
    return result


def rank_four_explicit_table(n: int) -> dict[tuple[int, int], Fraction]:
    """Closed-form nonnegative table satisfying both analytic identities.

    Hull-three entries are chosen to put the entire beta-reflection pair on
    its lower-interior member.  Hull-four entries are then the unique running
    sums required by the Boolean-interval diagonal.
    """

    if n < 5:
        raise ValueError("the rank-four family is stated for n>=5")
    hull_three = [0] * (n - 2)
    if n % 2 == 0:
        half = n // 2
        for interior in range(half - 1):
            distance = half - 2 - interior
            hull_three[interior] = n + 4 * distance * (distance + 1)
    else:
        half = (n - 3) // 2
        for interior in range(half):
            distance = half - interior
            hull_three[interior] = n - 1 + 4 * distance * distance
        hull_three[half] = (n - 1) // 2

    hull_four = []
    running = 0
    for interior in range(n - 3):
        running += hull_three[interior] - comb(n - interior - 1, 2)
        hull_four.append(running)
    if min(hull_four) < 0 or hull_four[-1] != 1:
        raise AssertionError((n, min(hull_four), hull_four[-1]))

    table = {
        (0, 0): Fraction(1),
        (1, 0): Fraction(n),
        (2, 0): Fraction(comb(n, 2)),
    }
    table.update({(3, i): Fraction(value) for i, value in enumerate(hull_three)})
    table.update({(4, i): Fraction(value) for i, value in enumerate(hull_four)})
    return table


def evaluate_constraints(n: int, table: dict[tuple[int, int], Fraction]) -> None:
    """Check both polynomial identities coefficientwise."""

    for degree in range(n + 1):
        hull = sum(
            count * comb(i, degree - h)
            for (h, i), count in table.items()
            if 0 <= degree - h <= i
        )
        if hull != comb(n, degree):
            raise AssertionError(("hull", n, degree, hull, comb(n, degree)))

        beta_hull = Fraction(0)
        for (h, i), count in table.items():
            exterior = n - h - i
            offset = degree - h
            if 0 <= offset <= i:
                beta_hull += (
                    count * h * (-1) ** (h - 1 + offset) * comb(i, offset)
                )
            if 0 <= offset <= exterior:
                beta_hull += count * h * (-1) ** offset * comb(exterior, offset)
        target = Fraction(n if degree == 1 else 0)
        if 0 <= degree - 1 <= n - 1:
            target += n * comb(n - 1, degree - 1) * (-1) ** (degree - 1)
        if beta_hull != target:
            raise AssertionError(("beta", n, degree, beta_hull, target))


def actual_hull_table(points) -> dict[tuple[int, int], Fraction]:
    sys.path[:0] = [
        str(ERDOS838 / "agent_planar_lattice_mean"),
        str(ERDOS838 / "agent_graded_supersat"),
    ]
    from planar_lattice_mean import closure_mask, is_convex

    table: dict[tuple[int, int], Fraction] = {}
    n = len(points)
    for hull_size in range(n + 1):
        for face in itertools.combinations(range(n), hull_size):
            if not is_convex(points, face):
                continue
            interior = closure_mask(points, face).bit_count() - hull_size
            table[(hull_size, interior)] = table.get((hull_size, interior), Fraction(0)) + 1
    return table


def actual_stress_rows() -> list[dict[str, object]]:
    sys.path[:0] = [str(ERDOS838 / "agent_graded_supersat")]
    from graded_trace import pascal_cell

    examples = {
        "central_pascal_T_4_2": tuple(sorted(pascal_cell(4, 2, Fraction(1, 97)))),
        "central_pascal_T_5_2": tuple(sorted(pascal_cell(5, 2, Fraction(1, 97)))),
        "dyadic_cliff_n17": tuple(
            (index, height)
            for index, height in enumerate(
                (
                    -610766, -553100, -480898, -445553, -319263, -72366,
                    270063, 589685, 996351, -299655, 2060498, -384200,
                    4986319, -526183, -679887, -723778, -808443,
                )
            )
        ),
    }
    rows = []
    for name, points in examples.items():
        n = len(points)
        table = actual_hull_table(points)
        evaluate_constraints(n, table)
        value = sum(table.values())
        first = sum(h * count for (h, _i), count in table.items())
        ratios = []
        for numerator in range(1, 16):
            probability = Fraction(numerator, 16)
            beta = sum(
                count * h * (-1) ** (h - 1) * probability**h
                * (1 - probability) ** interior
                for (h, interior), count in table.items()
            )
            assert 0 <= beta <= n * probability
            ratios.append(beta / (n * probability))
        rows.append(
            {
                "name": name,
                "n": n,
                "V": int(value),
                "mean_rank": str(first / value),
                "mean_rank_decimal": float(first / value),
                "maximum_beta_over_np_on_sixteenths": str(max(ratios)),
                "minimum_beta_over_np_on_sixteenths": str(min(ratios)),
            }
        )
    return rows


if __name__ == "__main__":
    rows = []
    for size in list(range(5, 65)) + [80, 96, 128, 192, 256]:
        table = rank_four_explicit_table(size)
        evaluate_constraints(size, table)
        value = sum(table.values())
        mean = sum(h * count for (h, _i), count in table.items()) / value
        half_weight = sum(count * Fraction(1, 2) ** h for (h, _i), count in table.items())
        assert mean <= 4
        assert size * half_weight >= Fraction(size, 16) * value
        if size in {5, 8, 10, 12, 16, 20, 32, 64, 96, 128, 192, 256}:
            row = {
                "n": size,
                "V": int(value),
                "mean_numerator": mean.numerator,
                "mean_denominator": mean.denominator,
                "mean_decimal": float(mean),
                "v3": int(sum(count for (h, _i), count in table.items() if h == 3)),
                "v4": int(sum(count for (h, _i), count in table.items() if h == 4)),
                "n_Zhalf_over_V_numerator": (size * half_weight / value).numerator,
                "n_Zhalf_over_V_denominator": (size * half_weight / value).denominator,
                "n_Zhalf_over_V_decimal": float(size * half_weight / value),
            }
            rows.append(row)
            print(size, "V", value, "mean", float(mean), "H", row["n_Zhalf_over_V_decimal"])

    # The RREF discovery and the explicit formula describe points in the same
    # affine solution space; check this independently on modest sizes.
    for size in range(5, 25):
        labels, matrix, rhs = constraint_system(size, 4)
        table = rank_four_explicit_table(size)
        vector = [table[label] for label in labels]
        assert all(
            sum(left * right for left, right in zip(row, vector)) == target
            for row, target in zip(matrix, rhs)
        )

    certificate = {
        "description": "formal rank-four barrier to hull-diagonal plus planar-beta inference",
        "checked_all_n": [5, 64],
        "additional_n": [80, 96, 128, 192, 256],
        "rows": rows,
        "actual_planar_stress": actual_stress_rows(),
        "full_tables": {
            str(size): {
                f"{h},{i}": int(value)
                for (h, i), value in rank_four_explicit_table(size).items()
                if value
            }
            for size in (12, 20)
        },
    }
    output = HERE / "beta_hull_constraints_certificate.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("beta/hull constraint audit: PASS")
    print("certificate:", output)
