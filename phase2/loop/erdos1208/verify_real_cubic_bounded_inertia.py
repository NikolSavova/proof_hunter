#!/usr/bin/env python3
"""Certificate for the bounded-inertia Q(zeta_7)^+ reoptimization."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 90

RAMIFIED_RATIONAL_COUNT = 98
SAFE_GENERATOR_RANK = 3 * RAMIFIED_RATIONAL_COUNT - 3
BASE_RELATION_EXCESS = 2
INERTIA_CAPS = 3 * RAMIFIED_RATIONAL_COUNT
USEFUL_RATIONAL_COUNT = 6_861
ALPHA = Decimal(4_941_486) / Decimal(10_000_000)  # 0.4941486
W0 = Decimal(52_282)
NUMERICAL_ALLOWANCE = Decimal("1e-25")
PACKING_CONSTANT_UPPER = Decimal(424) / Decimal(333)


def certify_pi_lower_bound() -> None:
    x = Fraction(1, 5)
    atan_one_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_one_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)


def cubic_discriminant(a: int, b: int, c: int) -> int:
    return a * a * b * b - 4 * b**3 - 4 * a**3 * c - 27 * c * c + 18 * a * b * c


def rank_mod_2(rows: list[int]) -> int:
    basis: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def local_increment(q: int, depth: int) -> Decimal:
    qd = Decimal(q)
    z = Decimal(1) / (qd * qd)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= z
        total += power
    current_value = Decimal(depth + 1) / total
    previous_value = Decimal(depth) / previous_total
    return (current_value / previous_value).ln() / 2


def main() -> None:
    certify_pi_lower_bound()
    assert cubic_discriminant(1, -2, -1) == 49
    assert 6 * 7 < 2 * 27
    assert rank_mod_2([0b111, 0b110, 0b100]) == 3
    assert all((x**3 + x**2 + 1) % 2 for x in (0, 1))

    primes = prime_sieve(600_000)
    split = [p for p in primes if p != 7 and p % 7 in (1, 6)]
    ramified = split[:RAMIFIED_RATIONAL_COUNT]
    ramified_set = set(ramified)
    useful = [
        q for q in primes if q not in ramified_set and q % 28 in (1, 13)
    ][:USEFUL_RATIONAL_COUNT]

    assert len(ramified) == RAMIFIED_RATIONAL_COUNT
    assert ramified[-1] == 2_003
    assert len(useful) == USEFUL_RATIONAL_COUNT
    assert useful[-1] == 499_969
    assert not ramified_set.intersection(useful)
    assert all(p % 7 in (1, 6) for p in ramified)
    assert all(q % 7 in (1, 6) and q % 4 == 1 for q in useful)

    d0 = SAFE_GENERATOR_RANK
    r0 = d0 + BASE_RELATION_EXCESS
    relation_bound = r0 + INERTIA_CAPS + 3 * USEFUL_RATIONAL_COUNT
    assert d0 == 291 and r0 == 293
    assert INERTIA_CAPS == 294
    assert relation_bound == 21_170
    assert 4 * relation_bound == 84_680 < 84_681 == d0 * d0
    assert 4 * (relation_bound + 3) > d0 * d0

    # rd(E)=49^(1/3).  Three order-two inertia caps over each split p
    # contribute p^(3*(1/2)/3)=p^(1/2).
    log_d = Decimal(49).ln() / 3
    for p in ramified:
        log_d += Decimal(p).ln() / 2

    increments: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for q in useful:
        cost = Decimal(q).ln()
        previous_gain: Decimal | None = None
        for depth in range(1, 5):
            gain = local_increment(q, depth)
            if previous_gain is not None:
                assert previous_gain > gain
            previous_gain = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, q, depth))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(key=lambda row: row[0], reverse=True)

    seen = {q: 0 for q in useful}
    for _, _, _, q, depth in increments:
        assert depth == seen[q] + 1
        seen[q] = depth

    def envelope(target: Decimal) -> tuple[Decimal, int, Decimal, Decimal]:
        cost_sum = Decimal(0)
        gain_sum = Decimal(0)
        for index, (slope, cost, gain, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                fraction = (target - cost_sum) / cost
                return gain_sum + fraction * gain, index, fraction, slope
            cost_sum += cost
            gain_sum += gain
        raise AssertionError("target exceeds certified envelope")

    def correction(w: Decimal) -> Decimal:
        exponent = 2 * (2 * ALPHA - 1) * w - log_d
        return (Decimal(1) + exponent.exp() / PACKING_CONSTANT_UPPER).ln()

    def rhs(w: Decimal) -> Decimal:
        return (
            PACKING_CONSTANT_UPPER.ln()
            + log_d
            + (2 - 4 * ALPHA) * w
            + correction(w)
        )

    left_gain, left_index, left_fraction, left_slope = envelope(2 * ALPHA * W0)
    right_gain, right_index, right_fraction, right_slope = envelope(
        4 * ALPHA * W0
    )
    assert maximum_fourth_slope < right_slope
    margins = [
        left_gain - rhs(W0) - NUMERICAL_ALLOWANCE,
        right_gain - rhs(2 * W0) - NUMERICAL_ALLOWANCE,
    ]
    assert min(margins) > Decimal("0.02")

    def depth_profile(stop: int) -> dict[int, int]:
        profile: dict[int, int] = {}
        for _, _, _, _, depth in increments[: stop + 1]:
            profile[depth] = profile.get(depth, 0) + 1
        return profile

    print("ramified rational primes / last:", len(ramified), ramified[-1])
    print("useful rational primes / last:", len(useful), useful[-1])
    print("safe d / base r / inertia caps / final r:", d0, r0, INERTIA_CAPS, relation_bound)
    print("log bounded-inertia root discriminant:", log_d)
    print("left boundary:", left_index, left_fraction, depth_profile(left_index))
    print("right boundary:", right_index, right_fraction, depth_profile(right_index))
    print("right / maximum fourth slopes:", right_slope, maximum_fourth_slope)
    print("certified margins:", *margins)
    print("cubic bounded-inertia F_2(n) << n^0.4941486: CERTIFIED")


if __name__ == "__main__":
    main()
