#!/usr/bin/env python3
"""Certificate for the positive-disk rank-713 Erdős 1208 bound."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

from verify_frobenius_all_depth_rank713 import (
    gf2_rank,
    local_increment,
    prime_sieve,
)


getcontext().prec = 90

RANK = 713
USEFUL_COUNT = 126_379
ALPHA = Decimal(49_458_516) / Decimal(100_000_000)  # 0.49458516
W0 = Decimal(1_034_254)
NUMERICAL_ALLOWANCE = Decimal("1e-25")

# The geometric constant is 4/pi.  The classical rational lower bound
# pi>333/106 gives the safe upper bound 4/pi<424/333 used numerically.
PACKING_CONSTANT_UPPER = Decimal(424) / Decimal(333)


def certify_pi_lower_bound() -> None:
    """Prove pi>333/106 from Machin's formula and alternating series."""
    x = Fraction(1, 5)
    # Four terms, ending in a negative term, lower-bound arctan(1/5).
    atan_one_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    # arctan(x)<x for x>0.  Machin: pi=16 atan(1/5)-4 atan(1/239).
    pi_lower = 16 * atan_one_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)


def main() -> None:
    certify_pi_lower_bound()

    primes = prime_sieve(2_100_000)
    ramified = [p for p in primes if p != 2][: RANK + 1]
    ramified_set = set(ramified)

    p3 = [p for p in ramified if p % 4 == 3]
    radicands = [p for p in ramified if p % 4 == 1]
    radicands.extend(p3[0] * p for p in p3[1:])

    def square_class_vector(a: int) -> int:
        vector = 0
        for index, p in enumerate(ramified):
            if a % p == 0:
                vector ^= 1 << index
                a //= p
        assert a == 1
        return vector

    assert len(radicands) == RANK
    assert gf2_rank([square_class_vector(a) for a in radicands]) == RANK

    useful: list[int] = []
    rejected: list[int] = []
    for q in primes:
        if q == 2 or q in ramified_set:
            continue
        if q % 4 == 1:
            useful.append(q)
        elif any(pow(a, (q - 1) // 2, q) == q - 1 for a in radicands):
            useful.append(q)
        else:
            rejected.append(q)
        if len(useful) == USEFUL_COUNT:
            break

    assert len(ramified) == RANK + 1 and ramified[-1] == 5_417
    assert len(useful) == USEFUL_COUNT and useful[-1] == 1_685_119
    assert not rejected
    assert not ramified_set.intersection(useful)

    relation_bound = RANK + USEFUL_COUNT
    assert relation_bound == 127_092
    assert 4 * relation_bound == RANK * RANK - 1

    discriminant_bound = 1
    for p in ramified:
        discriminant_bound *= p
    log_d = Decimal(discriminant_bound).ln()

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
        return (
            Decimal(1) + exponent.exp() / PACKING_CONSTANT_UPPER
        ).ln()

    def rhs(w: Decimal) -> Decimal:
        return (
            PACKING_CONSTANT_UPPER.ln()
            + log_d
            + (2 - 4 * ALPHA) * w
            + correction(w)
        )

    left_gain, left_index, left_fraction, left_slope = envelope(
        2 * ALPHA * W0
    )
    right_gain, right_index, right_fraction, right_slope = envelope(
        4 * ALPHA * W0
    )
    assert maximum_fourth_slope < right_slope

    margins = [
        left_gain - rhs(W0) - NUMERICAL_ALLOWANCE,
        right_gain - rhs(2 * W0) - NUMERICAL_ALLOWANCE,
    ]
    assert min(margins) > Decimal("0.008")

    def depth_profile(stop: int) -> dict[int, int]:
        profile: dict[int, int] = {}
        for _, _, _, _, depth in increments[: stop + 1]:
            profile[depth] = profile.get(depth, 0) + 1
        return profile

    print("safe packing constant:", PACKING_CONSTANT_UPPER)
    print("ramified primes / last:", len(ramified), ramified[-1])
    print("useful primes / last:", len(useful), useful[-1])
    print("generator/relation bound:", RANK, relation_bound)
    print("log D:", log_d)
    print("left boundary:", left_index, left_fraction, depth_profile(left_index))
    print("right boundary:", right_index, right_fraction, depth_profile(right_index))
    print("right / maximum fourth slopes:", right_slope, maximum_fourth_slope)
    print("certified margins:", *margins)
    print("target F_2(n) << n^0.49458516: CERTIFIED")


if __name__ == "__main__":
    main()
