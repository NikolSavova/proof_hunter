#!/usr/bin/env python3
"""Exact coefficient audit for the strict-subhalf linear-pocket gate."""

from fractions import Fraction
from math import floor, log2


def source_exponent(b: Fraction) -> Fraction:
    return b * (1 - b)


def pocket_exponent(a: Fraction) -> Fraction:
    # Uses only the established unconditional quarter coefficient.
    return a * a / 4


def target_exponent(delta: Fraction) -> Fraction:
    return Fraction(1, 2) - delta


def exact_gap(delta: Fraction) -> Fraction:
    a = 1 - delta * delta
    b = Fraction(1, 2)
    return source_exponent(b) + pocket_exponent(a) - target_exponent(delta)


def check_symbolic_grid() -> int:
    rows = 0
    for denominator in range(3, 101):
        for numerator in range(1, (denominator + 1) // 2):
            delta = Fraction(numerator, denominator)
            if not (0 < delta < Fraction(1, 2)):
                continue
            expected = delta - delta * delta / 2 + delta ** 4 / 4
            assert exact_gap(delta) == expected
            assert expected > 0
            a = 1 - delta * delta
            assert Fraction(1, 2) <= a < 1

            # b=1/2 maximizes b(1-b) on the admissible interval b<=a.
            best = Fraction(-1)
            for j in range(0, 1001):
                b = a * j / 1000
                best = max(best, source_exponent(b))
            assert best <= Fraction(1, 4)
            assert source_exponent(Fraction(1, 2)) == Fraction(1, 4)
            rows += 1
    return rows


def check_finite_budgets() -> int:
    rows = 0
    for delta in (Fraction(1, 100), Fraction(1, 50), Fraction(1, 20),
                  Fraction(1, 10), Fraction(1, 5), Fraction(2, 5)):
        eta = exact_gap(delta)
        for L in (1 << 20, 1 << 22, 1 << 24):
            s = floor(float(eta * L / 64))
            assert s >= 1
            d = 8 * s
            # Leading coefficient bounds used in (15)--(16).
            deletion_coefficient = Fraction(d, L)
            localization_coefficient = Fraction(4 * s, L)
            assert deletion_coefficient <= eta / 8
            assert localization_coefficient <= eta / 16
            assert eta - deletion_coefficient >= 7 * eta / 8
            assert eta - localization_coefficient >= 15 * eta / 16

            # A direct finite upper bound log S_d(n) <= d log_2(en/d).
            # Divide by L^2; its excess over d/L vanishes with L.
            finite_sd = (d * (L + log2(2.718281828459045) - log2(d))) / (L * L)
            assert finite_sd < float(eta) / 7  # room above eta/8
            rows += 1
    return rows


def check_all_delete_barrier() -> int:
    rows = 0
    for denominator in range(2, 101):
        for numerator in range(1, denominator):
            b = Fraction(numerator, denominator)
            assert source_exponent(b) < b
            # The missing amount is exactly b^2 at quadratic scale.
            assert b - source_exponent(b) == b * b
            rows += 1
    return rows


def check_rectangle_completion() -> int:
    # If R is any subrelation, its row-column completion has at least |R|
    # pairs and preserves every fixed crossing circuit contained in each row
    # and column. Audit the cardinality statement exhaustively for small grids.
    rows = 0
    for m in range(1, 5):
        for n in range(1, 5):
            total = m * n
            for mask in range(1, 1 << total):
                left = set()
                right = set()
                count = 0
                for i in range(m):
                    for j in range(n):
                        bit = i * n + j
                        if (mask >> bit) & 1:
                            left.add(i)
                            right.add(j)
                            count += 1
                assert len(left) * len(right) >= count
                rows += 1
    return rows


def main() -> None:
    symbolic = check_symbolic_grid()
    budgets = check_finite_budgets()
    all_delete = check_all_delete_barrier()
    rectangles = check_rectangle_completion()
    sample_delta = Fraction(1, 100)
    print(
        "PASS: strict-subhalf linear pocket coefficient, deletion/localization "
        "budget, rectangle completion, and all-delete barrier; "
        f"symbolic={symbolic}, budgets={budgets}, all_delete={all_delete}, "
        f"rectangles={rectangles}, "
        f"eta(1/100)={exact_gap(sample_delta)}"
    )


if __name__ == "__main__":
    main()
