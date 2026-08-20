#!/usr/bin/env python3
"""Dual certificate for mixed Frobenius 2-power caps at rank 713."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 90

RANK = 713
ORDER_TWO_CAP = 126_379
ALPHA = Decimal("0.49458538428")

# These are the two active square-cap slopes at the balanced rank-713
# endpoints.  They are recomputed below rather than trusted as data.
LEFT_ACTIVE_Q = 1_029_481
LEFT_ACTIVE_DEPTH = 1
RIGHT_ACTIVE_Q = 370_477
RIGHT_ACTIVE_DEPTH = 2


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def local_increment(q: int, depth: int, residue_cap: int) -> Decimal:
    """Worst normalized kth gain for residue degree dividing residue_cap."""
    t = Decimal(1) / (Decimal(q) ** residue_cap)
    numerator = (Decimal(depth + 1) / Decimal(depth)) * (
        Decimal(1) - t**depth
    )
    denominator = Decimal(1) - t ** (depth + 1)
    return (numerator / denominator).ln() / Decimal(residue_cap)


def dual_value(
    q: int,
    residue_cap: int,
    mu_left: Decimal,
    mu_right: Decimal,
    theta: Decimal,
) -> Decimal:
    cost = Decimal(q).ln()
    total = Decimal(0)
    for depth in range(1, 20):
        gain = local_increment(q, depth, residue_cap)
        left = max(Decimal(0), gain - mu_left * cost)
        right = max(Decimal(0), gain - mu_right * cost)
        contribution = theta * left + (Decimal(1) - theta) * right
        total += contribution
        if contribution == 0 and gain < min(mu_left, mu_right) * cost:
            break
    else:
        raise AssertionError("positive dual support persisted past depth 19")
    return total


def main() -> None:
    primes = prime_sieve(2_100_000)
    odd_primes = [p for p in primes if p != 2]
    ramified = odd_primes[: RANK + 1]
    useful = odd_primes[RANK + 1 :]
    assert ramified[-1] == 5_417
    assert useful[ORDER_TWO_CAP - 1] == 1_685_119
    assert useful[ORDER_TWO_CAP] == 1_685_153

    # Any weighted GS polynomial
    # 1-dt+d t^2+N_2 t^2+sum_{s>=2} N_s t^(2^s)<0
    # has N_2 < d^2/4-d.  The exact integer maximum is 126379.
    assert Fraction(RANK * RANK, 4) - RANK == Fraction(505_517, 4)
    assert ORDER_TWO_CAP == 126_379

    # At the square-optimal t=2/d the remaining one-quarter relation of
    # weighted slack admits exactly 31,773 appended fourth-power relators.
    t = Fraction(2, RANK)
    base = 1 - RANK * t + (RANK + ORDER_TWO_CAP) * t * t
    fourth_cap = (-base.numerator * t.denominator**4 - 1) // (
        base.denominator * t.numerator**4
    )
    while base + (fourth_cap + 1) * t**4 < 0:
        fourth_cap += 1
    while base + fourth_cap * t**4 >= 0:
        fourth_cap -= 1
    assert fourth_cap == 31_773

    mu_left = local_increment(
        LEFT_ACTIVE_Q, LEFT_ACTIVE_DEPTH, 2
    ) / Decimal(LEFT_ACTIVE_Q).ln()
    mu_right = local_increment(
        RIGHT_ACTIVE_Q, RIGHT_ACTIVE_DEPTH, 2
    ) / Decimal(RIGHT_ACTIVE_Q).ln()
    lam = (Decimal(2) - Decimal(4) * ALPHA) / (Decimal(2) * ALPHA)
    theta = (Decimal(2) * lam - Decimal(2) * mu_right) / (
        mu_left - Decimal(2) * mu_right + lam
    )
    assert Decimal(0) < theta < Decimal(1)
    assert (
        theta * mu_left
        + Decimal(2) * (Decimal(1) - theta) * mu_right
        == lam * (Decimal(2) - theta)
    )

    # A free order-four cap is granted at every useful prime.  An order-two
    # cap is an upgrade worth W_2(q)-W_4(q).  This dominates every genuine
    # mixed assignment because higher caps have no larger local gains.
    values_two: list[Decimal] = []
    values_four: list[Decimal] = []
    upgrades: list[Decimal] = []
    last_positive_four = -1
    for index, q in enumerate(useful[: ORDER_TWO_CAP + 1]):
        value_two = dual_value(q, 2, mu_left, mu_right, theta)
        value_four = dual_value(q, 4, mu_left, mu_right, theta)
        values_two.append(value_two)
        values_four.append(value_four)
        upgrades.append(value_two - value_four)
        if value_four > 0:
            last_positive_four = index

    # The finite exceptional range is monotone exactly; beyond it W_4=0.
    assert last_positive_four < ORDER_TWO_CAP
    assert all(
        upgrades[index] > upgrades[index + 1]
        for index in range(ORDER_TWO_CAP)
    )
    assert values_four[ORDER_TWO_CAP - 1] == 0

    # For q beyond this boundary each supported summand in W_2 decreases:
    # the proof note bounds d/d(log q) of its gain by 1/(q^2-1)<mu_right.
    assert Decimal(1) / (
        Decimal(useful[ORDER_TWO_CAP - 1]) ** 2 - Decimal(1)
    ) < mu_right

    # Thus the top ORDER_TWO_CAP upgrades are precisely the prefix.  Since
    # W_4 is already zero after that prefix, the generous mixed upper bound
    # collapses to the pure-square dual sum.
    free_four_total = sum(values_four, Decimal(0))
    relaxed_mixed_upper = free_four_total + sum(
        upgrades[:ORDER_TWO_CAP], Decimal(0)
    )
    mixed_upper = sum(values_two[:ORDER_TWO_CAP], Decimal(0))
    assert abs(relaxed_mixed_upper - mixed_upper) < Decimal("1e-75")
    log_d = sum((Decimal(p).ln() for p in ramified), Decimal(0))
    required_constant = Decimal(4).ln() + log_d
    margin = mixed_upper - required_constant
    assert margin < Decimal("-0.000002")

    # The literal appended fourth-power block also lies below the old active
    # right slope, explaining why direct frontier optimization ignores it.
    first_appended = useful[ORDER_TWO_CAP]
    assert local_increment(first_appended, 1, 4) / Decimal(first_appended).ln() < mu_right

    print("rank / order-two maximum / appended fourth maximum:", RANK, ORDER_TWO_CAP, fourth_cap)
    print("dual lambda / theta:", lam, theta)
    print("active slopes:", mu_left, mu_right)
    print("last positive free-four index:", last_positive_four)
    print("mixed dual margin:", margin)
    print("CERTIFIED: mixed 2/4/8/... caps do not beat 0.49458538428 at rank 713")


if __name__ == "__main__":
    main()
