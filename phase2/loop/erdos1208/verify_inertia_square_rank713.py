#!/usr/bin/env python3
"""Certificate for the inertia-square rank-713 Erdős 1208 bound."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

from verify_frobenius_all_depth_rank713 import (
    gf2_rank,
    local_increment,
    prime_sieve,
)
from verify_positive_disk_rank713 import (
    PACKING_CONSTANT_UPPER,
    certify_pi_lower_bound,
)


getcontext().prec = 90

RANK = 713
RAMIFIED_COUNT = 714
INERTIA_CAP_COUNT = 714
USEFUL_COUNT = 125_665
ALPHA = Decimal(493_984) / Decimal(1_000_000)  # 0.493984
W0 = Decimal(873_770)
NUMERICAL_ALLOWANCE = Decimal("1e-25")


def main() -> None:
    certify_pi_lower_bound()

    # Refined Golod--Shafarevich audit for the stronger order-four variant.
    # Base and useful-prime relations have depth >=2; inertia fourth powers
    # have depth >=4.  At t=2/713 the polynomial is strictly negative.
    t = Fraction(2, RANK)
    refined_order_four = (
        1 - RANK * t + (RANK + 126_379) * t * t
        + RAMIFIED_COUNT * t**4
    )
    assert refined_order_four < 0
    assert 16 * RAMIFIED_COUNT == 11_424 < RANK * RANK

    # In the mixed family, x order-two upgrades replace x useful square
    # caps.  The quadratic coefficient stays fixed and the quartic
    # coefficient falls from 714 to 714-x, so every mixture also passes.
    for upgrades in range(RAMIFIED_COUNT + 1):
        mixed = (
            1 - RANK * t + (RANK + 126_379) * t * t
            + (RAMIFIED_COUNT - upgrades) * t**4
        )
        assert mixed < 0

    primes = prime_sieve(2_100_000)
    ramified = [p for p in primes if p != 2][:RAMIFIED_COUNT]
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

    assert ramified[-1] == 5_417
    assert len(useful) == USEFUL_COUNT and useful[-1] == 1_674_889
    assert not rejected
    assert not ramified_set.intersection(useful)

    relation_bound = RANK + INERTIA_CAP_COUNT + USEFUL_COUNT
    assert relation_bound == 127_092
    assert 4 * relation_bound == RANK * RANK - 1

    discriminant_product = 1
    for p in ramified:
        discriminant_product *= p
    # Inertia order at most two gives normalized tame discriminant exponent
    # 1-1/e_p <= 1/2 at every ramified prime.
    log_d = Decimal(discriminant_product).ln() / 2

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
    assert min(margins) > Decimal(3)

    def depth_profile(stop: int) -> dict[int, int]:
        profile: dict[int, int] = {}
        for _, _, _, _, depth in increments[: stop + 1]:
            profile[depth] = profile.get(depth, 0) + 1
        return profile

    print("ramified / inertia caps:", RAMIFIED_COUNT, INERTIA_CAP_COUNT)
    print("useful primes / last:", len(useful), useful[-1])
    print("generator/relation bound:", RANK, relation_bound)
    print("log root-discriminant bound:", log_d)
    print("left boundary:", left_index, left_fraction, depth_profile(left_index))
    print("right boundary:", right_index, right_fraction, depth_profile(right_index))
    print("right / maximum fourth slopes:", right_slope, maximum_fourth_slope)
    print("certified margins:", *margins)
    print("target F_2(n) << n^0.493984: CERTIFIED")


if __name__ == "__main__":
    main()
