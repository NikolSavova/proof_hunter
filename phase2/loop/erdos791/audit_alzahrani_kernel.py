#!/usr/bin/env python3
"""Exact arithmetic audit of the kernel used in Alzahrani's 2016 thesis.

The thesis selects u(t)=9/4-100(t-1/2)^4.  Under the autocorrelation
construction indicated by its displayed endpoint values, this script checks
the hypotheses needed in the subsequent positivity argument.
"""

from fractions import Fraction as F


def multiply(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def integrate(poly: list[F], lower: F, upper: F) -> F:
    return sum(
        coefficient * (upper ** (degree + 1) - lower ** (degree + 1)) / F(degree + 1)
        for degree, coefficient in enumerate(poly)
    )


def main() -> None:
    # Low-degree-first coefficients of u(t).
    u = [F(-4), F(50), F(-150), F(200), F(-100)]
    # u(t+1/2) = 9/4 - 100 t^4.
    shifted = [F(9, 4), F(0), F(0), F(0), F(-100)]
    autocorrelation_half = integrate(multiply(u, shifted), F(0), F(1, 2))
    mean = integrate(u, F(0), F(1))

    assert u[0] == -4
    assert mean == 1
    assert autocorrelation_half == F(-1009, 4032)
    print(f"u(0) = {u[0]}")
    print(f"integral_0^1 u = {mean}")
    print(f"autocorrelation(1/2) = {autocorrelation_half}")
    print("PASS: the selected u and its autocorrelation violate the required nonnegativity.")


if __name__ == "__main__":
    main()
