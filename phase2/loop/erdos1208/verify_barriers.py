#!/usr/bin/env python3
"""Numerical checks for the exponents in FULL_ATTACK.md.

This script verifies only the arithmetic consequences of the symbolic
arguments.  The local-lattice classification and alteration proof remain
mathematical inputs stated in the note.
"""

import math


def main() -> None:
    split_entropy = math.log(2.0) / math.log(5.0)

    # Section 1: dyadic implementation and idealized binary-sieve barriers.
    dyadic_x = split_entropy / 2.0
    dyadic_epsilon_ceiling = dyadic_x / (4.0 + 2.0 * dyadic_x)
    dyadic_exponent_floor = 0.5 - dyadic_epsilon_ceiling
    idealized_exponent_floor = 1.0 / (2.0 + split_entropy)

    assert 0.4513 < dyadic_exponent_floor < 0.4515
    assert 0.4113 < idealized_exponent_floor < 0.4115
    assert idealized_exponent_floor > 1.0 / 3.0

    # Section 2: Pach--Tardos triangle ceiling in the alteration argument.
    tau = (11.0 * math.e - 3.0) / (5.0 * math.e - 1.0)
    triangle_ceiling = (3.0 - tau) / 2.0
    crossover_delta = 3.0 * triangle_ceiling - 1.0

    assert 2.1364 < tau < 2.1365
    assert 0.4317 < triangle_ceiling < 0.4318
    assert 0.2952 < crossover_delta < 0.2954

    print(f"split entropy log(2)/log(5) = {split_entropy:.15f}")
    print(f"dyadic construction exponent floor = {dyadic_exponent_floor:.15f}")
    print(f"idealized binary-sieve exponent floor = {idealized_exponent_floor:.15f}")
    print(f"Pach--Tardos tau = {tau:.15f}")
    print(f"conditional lower-bound ceiling = {triangle_ceiling:.15f}")
    print(f"energy-saving crossover delta = {crossover_delta:.15f}")


if __name__ == "__main__":
    main()
