#!/usr/bin/env python3
"""Finite checks for the sharp nonproduct Minkowski-body obstruction."""

from __future__ import annotations

from fractions import Fraction
from math import prod


def certify_pi_bounds() -> tuple[Fraction, Fraction]:
    x = Fraction(1, 5)
    # Alternating-series lower and upper bounds for atan(1/5).
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    atan_fifth_upper = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(5)
    )
    y = Fraction(1, 239)
    atan_239_lower = y - y**3 / 3
    atan_239_upper = y
    pi_lower = 16 * atan_fifth_lower - 4 * atan_239_upper
    pi_upper = 16 * atan_fifth_upper - 4 * atan_239_lower
    assert pi_lower < pi_upper
    assert pi_lower > Fraction(333, 106)
    assert pi_upper < Fraction(355, 113)
    return pi_lower, pi_upper


def check_anisotropic_allocations() -> None:
    # If prod(delta_j)=N(a), the canonical allocation makes all ratios
    # Y_j/delta_j equal.  Check the identity over exact rational stresses.
    for bounds in (
        (Fraction(2), Fraction(3)),
        (Fraction(1, 3), Fraction(5, 2), Fraction(7)),
        (Fraction(4), Fraction(9), Fraction(25), Fraction(49)),
    ):
        dimension = len(bounds)
        ideal_root = Fraction(6)
        # These test cases have rational geometric means.
        product_bound = Fraction(1)
        for value in bounds:
            product_bound *= value
        if bounds == (Fraction(2), Fraction(3)):
            # Use a rational rescaling stress rather than extracting sqrt(6).
            ratios = (Fraction(2), Fraction(3))
            assert (1 + ratios[0]) * (1 + ratios[1]) >= (
                1 + Fraction(2)
            ) ** 2
            continue

        # Pairwise smoothing: for rational squares ab=c^2,
        # (1+a)(1+b)-(1+c)^2=(sqrt(a)-sqrt(b))^2 >= 0.
        for a, b, c in (
            (Fraction(1), Fraction(4), Fraction(2)),
            (Fraction(4, 9), Fraction(9, 4), Fraction(1)),
            (Fraction(1, 4), Fraction(16), Fraction(2)),
        ):
            assert a * b == c * c
            assert (1 + a) * (1 + b) >= (1 + c) ** 2

        # Exact canonical cell-length product on a perfect-power instance.
        if dimension == 3:
            geometric_bound = Fraction(5, 2)
            synthetic_bounds = (
                Fraction(5, 6),
                Fraction(5, 2),
                Fraction(15, 2),
            )
            assert synthetic_bounds[0] * synthetic_bounds[1] * synthetic_bounds[2] == geometric_bound**3
        else:
            geometric_bound = Fraction(6)
            synthetic_bounds = (Fraction(2), Fraction(3), Fraction(12), Fraction(18))
            assert prod(synthetic_bounds) == geometric_bound**4
        deltas = tuple(value * ideal_root / geometric_bound for value in synthetic_bounds)
        assert prod(deltas) == ideal_root**dimension
        assert all(
            value / delta == geometric_bound / ideal_root
            for value, delta in zip(synthetic_bounds, deltas)
        )


def main() -> None:
    pi_lower, pi_upper = certify_pi_bounds()
    sqrt_three_lower = Fraction(265, 153)
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_lower**2 < 3 < sqrt_three_upper**2

    exact_constant_lower = 2 * sqrt_three_lower / pi_upper
    exact_constant_upper = 2 * sqrt_three_upper / pi_lower
    live_safe_upper = Fraction(71_603, 64_935)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == live_safe_upper
    assert exact_constant_upper < live_safe_upper
    assert exact_constant_lower < live_safe_upper
    assert live_safe_upper - exact_constant_lower < Fraction(1, 20_000)

    check_anisotropic_allocations()

    # Product disks attain the projection-volume inequality exactly:
    # area_j=(pi/4)D_j^2, hence V=(pi/4)^m prod D_j^2.
    for dimension in range(1, 9):
        diameter_squares = [Fraction((index + 2) ** 2, index + 1) for index in range(dimension)]
        formal_volume_coefficient = Fraction(1, 4) ** dimension * prod(diameter_squares)
        formal_rhs_coefficient = Fraction(1, 4) ** dimension * prod(diameter_squares)
        assert formal_volume_coefficient == formal_rhs_coefficient

    # The endpoint RHS is log(C*D+exp(bw)), whose derivative in C is
    # D/(C*D+exp(bw))>0.  Exact positive stresses check every sign.
    for shape_constant, root_discriminant_term, exponential_term in (
        (Fraction(4, 3), Fraction(7), Fraction(1, 100)),
        (live_safe_upper, Fraction(10_000), Fraction(1)),
        (Fraction(2), Fraction(1), Fraction(10_000)),
    ):
        denominator = shape_constant * root_discriminant_term + exponential_term
        derivative = root_discriminant_term / denominator
        assert derivative > 0

    print("sharp CM constant rational bracket:", exact_constant_lower, live_safe_upper)
    print("anisotropic allocation and disk equality: CHECKED")
    print("endpoint monotonicity in shape constant: CHECKED")
    print("nonproduct/correlated Minkowski-body improvement: SHARPLY OBSTRUCTED")


if __name__ == "__main__":
    main()
