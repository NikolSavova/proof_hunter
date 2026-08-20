#!/usr/bin/env python3
"""Exact finite certificate for the rank-221 CM/Eisenstein disk bound."""

from decimal import Decimal, getcontext
from fractions import Fraction

from verify_frobenius_all_depth_rank713 import gf2_rank, local_increment, prime_sieve


getcontext().prec = 90

D = 221
RAMIFIED_COUNT = D + 1
USEFUL_COUNT = (D * D - 1) // 4 - 2 * D - 1
ALPHA = Decimal(49_371_364) / Decimal(100_000_000)  # 0.49371364
W0 = Decimal("84891.5")
EPSILON = Decimal("1e-25")

# sqrt(3) < 1351/780 and pi > 333/106, hence
# 2 sqrt(3)/pi < 71603/64935.
C_UPPER_FRACTION = Fraction(71_603, 64_935)
C_UPPER = Decimal(C_UPPER_FRACTION.numerator) / Decimal(
    C_UPPER_FRACTION.denominator
)


def certify_constant() -> None:
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3

    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert (
        2 * sqrt_three_upper / Fraction(333, 106)
        == C_UPPER_FRACTION
    )


def main() -> None:
    certify_constant()
    primes = prime_sieve(300_000)
    ramified = [p for p in primes if p != 2][:RAMIFIED_COUNT]
    ramified_set = set(ramified)

    # Positive squareclasses spanning the totally-real Frattini field.
    p3 = [p for p in ramified if p % 4 == 3]
    radicands = [p for p in ramified if p % 4 == 1]
    radicands.extend(p3[0] * p for p in p3[1:])

    def squareclass(a: int) -> int:
        row = 0
        for i, p in enumerate(ramified):
            if a % p == 0:
                row ^= 1 << i
                a //= p
        assert a == 1
        return row

    assert len(ramified) == 222 and ramified[-1] == 1_409
    assert len(radicands) == D
    assert gf2_rank([squareclass(a) for a in radicands]) == D

    # For q == 1 mod 3, every residue field of degree 1 or 2 contains a
    # primitive cube root.  For q == 2 mod 3, a nonzero Frattini Frobenius
    # survives the square cap and forces residue degree exactly two.
    useful: list[int] = []
    rejected: list[int] = []
    for q in primes:
        if q in (2, 3) or q in ramified_set:
            continue
        frobenius_nonzero = any(
            pow(a, (q - 1) // 2, q) == q - 1 for a in radicands
        )
        if q % 3 == 1 or frobenius_nonzero:
            useful.append(q)
        else:
            rejected.append(q)
        if len(useful) == USEFUL_COUNT:
            break

    assert USEFUL_COUNT == 11_767
    assert len(useful) == USEFUL_COUNT and useful[-1] == 128_047
    assert not rejected
    assert not ramified_set.intersection(useful)

    relation_bound = D + RAMIFIED_COUNT + USEFUL_COUNT
    assert relation_bound == 12_210
    assert 4 * relation_bound == D * D - 1

    discriminant_product = 1
    for p in ramified:
        discriminant_product *= p
    log_rd = Decimal(discriminant_product).ln() / 2

    increments: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    max_fourth_slope = Decimal(0)
    for q in useful:
        cost = Decimal(q).ln()
        previous: Decimal | None = None
        for depth in range(1, 5):
            gain = local_increment(q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, q, depth))
            else:
                max_fourth_slope = max(max_fourth_slope, slope)

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
        raise AssertionError("target beyond certified frontier")

    def rhs(w: Decimal) -> Decimal:
        exponent = 2 * (2 * ALPHA - 1) * w - log_rd
        correction = (Decimal(1) + exponent.exp() / C_UPPER).ln()
        return C_UPPER.ln() + log_rd + (2 - 4 * ALPHA) * w + correction

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert max_fourth_slope < right[3]
    margins = [
        left[0] - rhs(W0) - EPSILON,
        right[0] - rhs(2 * W0) - EPSILON,
    ]
    assert min(margins) > Decimal("0.003")

    def profile(stop: int) -> dict[int, int]:
        out: dict[int, int] = {}
        for _, _, _, _, depth in increments[: stop + 1]:
            out[depth] = out.get(depth, 0) + 1
        return out

    print("safe CM effective constant:", C_UPPER)
    print("ramified / last:", len(ramified), ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("generator / relations:", D, relation_bound)
    print("log real-tower root discriminant:", log_rd)
    print("left:", left[1], left[2], profile(left[1]))
    print("right:", right[1], right[2], profile(right[1]))
    print("right / max fourth slopes:", right[3], max_fourth_slope)
    print("margins:", *margins)
    print("target F_2(n) << n^0.49371364: CERTIFIED")


if __name__ == "__main__":
    main()
