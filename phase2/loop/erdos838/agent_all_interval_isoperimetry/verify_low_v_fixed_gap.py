#!/usr/bin/env python3
"""Integer/rational audit for LOW_V_FIXED_GAP.md."""

from __future__ import annotations

from math import ceil, comb, isqrt, log2, sqrt


def ceil_sqrt(x: int) -> int:
    y = isqrt(x)
    return y if y * y == x else y + 1


def least_endpoint_mass(mass: int, activity: int, triples: int) -> int:
    """Least R with R^2 >= (mass+2R)activity+triples."""
    # R^2-2 A R-(M A+T)>=0 has positive root
    # A+sqrt(A^2+M A+T).
    r = activity + ceil_sqrt(activity * activity + mass * activity + triples)
    assert r * r >= (mass + 2 * r) * activity + triples
    if r:
        assert (r - 1) * (r - 1) < (mass + 2 * (r - 1)) * activity + triples
    return r


def scalar_instance(L: int, delta_num: int, delta_den: int) -> None:
    # Use c=(1/2-delta) exactly and M=floor(2^(cL^2)).  The selected
    # parameters make the exponent integral in the audited cases.
    exponent_num = (delta_den - 2 * delta_num) * L * L
    exponent_den = 2 * delta_den
    assert exponent_num % exponent_den == 0
    exponent = exponent_num // exponent_den
    n = 1 << L
    h = ceil((L + log2(L)) / 2) + 3
    activity = 1 << h
    mass = 1 << exponent
    triples = sum(comb(n, j) for j in range(4))
    endpoint = least_endpoint_mass(mass, activity, triples)
    generators = mass + 2 * endpoint

    assert generators <= comb(n, h)
    total_upper = generators * activity + triples
    assert endpoint * endpoint >= total_upper
    assert mass <= total_upper
    assert comb(2 * h - 2, h - 1) >= n

    low = log2(mass) / (L * L)
    high = log2(total_upper) / (L * L)
    endpoint_coeff = log2(endpoint) / (L * L)
    c = 0.5 - delta_num / delta_den
    assert abs(low - c) < 1e-15
    assert high <= c + (h + 2) / (L * L)
    print(
        f"scalar L={L:3d} delta={delta_num}/{delta_den} h={h:3d} "
        f"logV/L^2 in [{low:.8f},{high:.8f}] "
        f"logC/L^2>={endpoint_coeff:.8f} PASS"
    )


def threshold_audit() -> None:
    for delta in (0.01, 0.05, 0.10, 0.20, 0.24):
        alpha = sqrt(1 - 2 * delta)
        eta = (3 - sqrt(9 - 8 * delta)) / 2
        assert abs(alpha * alpha / 2 - (0.5 - delta)) < 1e-14
        assert abs(eta * eta - 3 * eta + 2 * delta) < 1e-14
        assert 0 < eta < 1
        print(
            f"delta={delta:.2f} extraction_threshold={alpha:.10f} "
            f"macro_mesh_threshold={eta:.10f} PASS"
        )


if __name__ == "__main__":
    threshold_audit()
    # Denominators divide the chosen L^2, so M is an exact power of two.
    for args in ((40, 1, 20), (40, 1, 10), (48, 1, 8), (40, 1, 5)):
        scalar_instance(*args)
