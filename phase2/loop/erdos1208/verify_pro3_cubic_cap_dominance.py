#!/usr/bin/env python3
"""Exact finite certificate for the pro-3 cubic-cap dominance audit."""

from decimal import Decimal, getcontext
from fractions import Fraction

from verify_frobenius_all_depth_rank713 import prime_sieve


getcontext().prec = 90

D = 38
INERTIA_COUNT = D
USEFUL_COUNT = 7_138
ALPHA = Decimal(49_526_518) / Decimal(100_000_000)  # 0.49526518
W0 = Decimal(29_734)
C_UPPER = Decimal(424) / Decimal(333)
EPSILON = Decimal("1e-25")
MAX_DEPTH = 20


def local_increment(q: int, depth: int) -> Decimal:
    """Guaranteed full-orbit increment when residue degree divides three."""
    t = Decimal(1) / (Decimal(q) ** 3)
    total = Decimal(1)
    previous = Decimal(1)
    power = Decimal(1)
    for _ in range(1, depth + 1):
        previous = total
        power *= t
        total += power
    current_value = Decimal(depth + 1) / total
    previous_value = Decimal(depth) / previous
    return (current_value / previous_value).ln() / 3


def main() -> None:
    primes = prime_sieve(500_000)
    ramified = [p for p in primes if p % 3 == 1][:D]
    ramified_set = set(ramified)
    useful = [p for p in primes if p % 4 == 1 and p not in ramified_set][
        :USEFUL_COUNT
    ]

    assert len(ramified) == D and ramified[-1] == 409
    assert len(useful) == USEFUL_COUNT and useful[-1] == 155_797

    # Safe tame presentation: D base relations in degree two and all inertia
    # cubes plus useful Frobenius cubes in degree three.
    cubic_count = INERTIA_COUNT + USEFUL_COUNT
    t_gs = Fraction(403, 10_000)
    gs_value = 1 - D * t_gs + D * t_gs**2 + cubic_count * t_gs**3
    assert gs_value < 0

    discriminant_product = 1
    for p in ramified:
        discriminant_product *= p
    log_rd = Decimal(discriminant_product).ln() * Decimal(2) / Decimal(3)

    increments: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    max_next_slope = Decimal(0)
    for q in useful:
        cost = Decimal(q).ln()
        previous: Decimal | None = None
        for depth in range(1, MAX_DEPTH + 2):
            gain = local_increment(q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if depth <= MAX_DEPTH:
                increments.append((slope, cost, gain, q, depth))
            else:
                max_next_slope = max(max_next_slope, slope)

    increments.sort(reverse=True)
    seen = {q: 0 for q in useful}
    for _, _, _, q, depth in increments:
        assert depth == seen[q] + 1
        seen[q] = depth

    def envelope(target: Decimal) -> tuple[Decimal, int, Decimal, Decimal]:
        cost_sum = Decimal(0)
        gain_sum = Decimal(0)
        for i, (slope, cost, gain, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                fraction = (target - cost_sum) / cost
                assert 0 <= fraction <= 1
                return gain_sum + fraction * gain, i, fraction, slope
            cost_sum += cost
            gain_sum += gain
        raise AssertionError("target beyond cubic-cap frontier")

    def rhs(w: Decimal) -> Decimal:
        exponent = 2 * (2 * ALPHA - 1) * w - log_rd
        correction = (Decimal(1) + exponent.exp() / C_UPPER).ln()
        return C_UPPER.ln() + log_rd + (2 - 4 * ALPHA) * w + correction

    # Pro-3 normal layers give a ternary phase interval [w,3w].
    left = envelope(2 * ALPHA * W0)
    right = envelope(6 * ALPHA * W0)
    # Marginal gains decrease in the depth.  Thus exclusion of depth
    # MAX_DEPTH + 1 excludes every still deeper increment as well.
    assert max_next_slope < right[3]
    margins = [
        left[0] - rhs(W0) - EPSILON,
        right[0] - rhs(3 * W0) - EPSILON,
    ]
    assert min(margins) > Decimal("0.001")

    def profile(stop: int) -> dict[int, int]:
        out: dict[int, int] = {}
        for _, _, _, _, depth in increments[: stop + 1]:
            out[depth] = out.get(depth, 0) + 1
        return out

    print("rank / base relations / cubic relators:", D, D, cubic_count)
    print("GS point / value:", t_gs, gs_value)
    print("ramified / last:", len(ramified), ramified[-1])
    print("useful / last:", len(useful), useful[-1])
    print("log root discriminant:", log_rd)
    print("left:", left[1], left[2], profile(left[1]))
    print("right:", right[1], right[2], profile(right[1]))
    print("right / maximum next slopes:", right[3], max_next_slope)
    print("margins:", *margins)
    print("pro-3 safe threshold alpha=0.49526518: CERTIFIED (noncompetitive)")


if __name__ == "__main__":
    main()
