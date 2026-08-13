#!/usr/bin/env python3
"""Exact/numerical checks for HEREDITARY_MULTIPLICITY_BARRIER.md.

The exact part verifies that every chain of hereditary double counts
telescopes to the direct binomial factor.  The floating-point part checks the
quadratic profile identities and the local-supersaturation formula on a grid.
It is a smoke test, not a premise of any proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def exact_chain_factor(chain: list[int], k: int) -> Fraction:
    out = Fraction(1)
    for large, small in zip(chain, chain[1:]):
        out *= Fraction(comb(large, k), comb(small, k))
    return out


def check_exact_telescoping() -> int:
    checked = 0
    for n in range(6, 31):
        for a in range(5, n + 1):
            for b in range(4, a + 1):
                for m in range(3, b + 1):
                    for k in range(1, m + 1):
                        chain = [n, a, b, m]
                        got = exact_chain_factor(chain, k)
                        want = Fraction(comb(n, k), comb(m, k))
                        assert got == want
                        checked += 1
    return checked


def check_profile_fixed_point() -> int:
    checked = 0
    for ai in range(1, 100):
        alpha = ai / 100
        for ti in range(1, 100):
            theta = ti / 100
            y = alpha * theta
            lifted = theta * (1 - theta) * alpha**2 + theta * alpha * (1 - alpha)
            direct = y * (1 - y)
            assert abs(lifted - direct) < 1e-12
            checked += 1
    return checked


def check_standard_supersaturation_profile() -> int:
    checked = 0
    for rhoi in range(101, 501):
        rho = rhoi / 100
        sigma = rho - 1
        for bi in range(1, int(100 / rho) + 1):
            beta = bi / 100
            local = beta - (rho - sigma) * beta**2
            direct = beta * (1 - beta)
            assert abs(local - direct) < 1e-12
            checked += 1
    return checked


def check_phi_formula() -> int:
    checked = 0
    for rhoi in range(101, 501, 3):
        rho = rhoi / 100
        for sigmai in range(0, 2 * rhoi + 1, 5):
            sigma = sigmai / 100
            if sigma <= rho / 2:
                formula = 1 / (4 * (rho - sigma))
            else:
                formula = sigma / rho**2
            # The concave quadratic has its maximum at the critical point or
            # at the right endpoint.  Evaluate those candidates directly.
            candidates = [1 / rho]
            if rho > sigma:
                critical = 1 / (2 * (rho - sigma))
                if critical <= 1 / rho:
                    candidates.append(critical)
            direct = max(beta - (rho - sigma) * beta**2 for beta in candidates)
            assert abs(formula - direct) < 1e-12
            checked += 1
    return checked


def main() -> None:
    exact = check_exact_telescoping()
    profile = check_profile_fixed_point()
    local = check_standard_supersaturation_profile()
    phi = check_phi_formula()
    print(f"exact nested chains checked: {exact}")
    print(f"profile grid points checked: {profile}")
    print(f"local supersaturation grid points checked: {local}")
    print(f"piecewise local-target formulas checked: {phi}")
    print("all multiplicity-barrier checks: PASS")


if __name__ == "__main__":
    main()
