#!/usr/bin/env python3
"""Rational-interval endpoint certificate for the rank-20 placewise sieve.

Unlike the Decimal exploratory verifier, every sign decision here is made
with exact rational bounds.  Logarithms use

    log x = k log 2 + 2 sum_{j>=0} z^(2j+1)/(2j+1),

after writing x=2^k y with 1 <= y < 2 and z=(y-1)/(y+1).
The omitted positive tail is bounded by a geometric series.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction

from verify_placewise_rank20 import (
    ALPHA,
    SPLIT_PRIMES,
    W0,
    exact_checks,
)


# Twenty terms already give an error below 3^(-41), far smaller than the
# certified slope gaps and endpoint margins in this finite dataset.
TERMS = 20


def pow2(k: int) -> Fraction:
    return Fraction(2**k, 1) if k >= 0 else Fraction(1, 2 ** (-k))


def floor_log2(x: Fraction) -> int:
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k + 1):
        k += 1
    return k


def atanh_log_unit_bounds(y: Fraction) -> tuple[Fraction, Fraction]:
    assert 1 <= y <= 2
    z = (y - 1) / (y + 1)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(TERMS):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    # power is now z^(2 TERMS+1).  Bound every remaining denominator by
    # the first omitted denominator and sum the powers geometrically.
    remainder = 2 * power / ((2 * TERMS + 1) * (1 - z2))
    return lower, lower + remainder


LOG2 = atanh_log_unit_bounds(Fraction(2))


def log_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    assert x > 0
    if x == 1:
        return Fraction(0), Fraction(0)
    if x < 1:
        lo, hi = log_bounds(1 / x)
        return -hi, -lo
    k = floor_log2(x)
    y = x / pow2(k)
    lo_y, hi_y = atanh_log_unit_bounds(y)
    if k >= 0:
        return k * LOG2[0] + lo_y, k * LOG2[1] + hi_y
    return k * LOG2[1] + lo_y, k * LOG2[0] + hi_y


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale_nonnegative(a, c: int):
    assert c >= 0
    return c * a[0], c * a[1]


def ratio_bounds_positive(a, b):
    assert a[0] > 0 and b[0] > 0
    return a[0] / b[1], a[1] / b[0]


def product_bounds_positive(a, b):
    assert a[0] >= 0 and b[0] >= 0
    return a[0] * b[0], a[1] * b[1]


def gain_value(q: int, depth: int) -> Fraction:
    if depth == 0:
        return Fraction(1)
    lam = sum(Fraction(1, q**e) for e in range(depth + 1))
    return Fraction(depth + 1) / lam


def build_items():
    cost_logs = {q: log_bounds(Fraction(q)) for q in SPLIT_PRIMES}
    gain_logs = {}
    values = {}
    items = []
    with localcontext() as ctx:
        ctx.prec = 100
        for prime_index, q in enumerate(SPLIT_PRIMES):
            previous = Fraction(1)
            for depth in range(1, 21):
                current = gain_value(q, depth)
                increment = current / previous
                increment_log = log_bounds(increment)
                gain_logs[(prime_index, depth)] = increment_log
                values[(prime_index, depth)] = current
                midpoint_gain = (
                    Decimal(increment.numerator).ln()
                    - Decimal(increment.denominator).ln()
                )
                midpoint_cost = Decimal(q).ln()
                items.append(
                    (
                        midpoint_gain / midpoint_cost,
                        prime_index,
                        depth,
                    )
                )
                previous = current
    items.sort(reverse=True)
    return items, cost_logs, gain_logs, values


def locate_endpoint(items, cost_logs, target: Fraction):
    target_decimal = Decimal(target.numerator) / Decimal(target.denominator)
    running = Decimal(0)
    depths = [0] * len(SPLIT_PRIMES)
    for position, (_, prime_index, depth) in enumerate(items):
        q = SPLIT_PRIMES[prime_index]
        cost_mid = (
            Decimal(cost_logs[q][0].numerator) / Decimal(cost_logs[q][0].denominator)
            + Decimal(cost_logs[q][1].numerator) / Decimal(cost_logs[q][1].denominator)
        ) / 2
        if running + cost_mid > target_decimal:
            return position, depths, prime_index, depth
        assert depth == depths[prime_index] + 1
        depths[prime_index] = depth
        running += cost_mid
    raise AssertionError("depth cap too small")


def certify_endpoint(
    items,
    cost_logs,
    gain_logs,
    values,
    discriminant_bound: int,
    w: Fraction,
):
    target = 2 * ALPHA * w
    position, depths, active_prime, active_depth = locate_endpoint(
        items, cost_logs, target
    )

    prefix_cost = (Fraction(0), Fraction(0))
    prefix_gain = (Fraction(0), Fraction(0))
    for prime_index, depth in enumerate(depths):
        if depth == 0:
            continue
        q = SPLIT_PRIMES[prime_index]
        prefix_cost = add(prefix_cost, scale_nonnegative(cost_logs[q], depth))
        prefix_gain = add(prefix_gain, log_bounds(values[(prime_index, depth)]))

    active_q = SPLIT_PRIMES[active_prime]
    active_cost = cost_logs[active_q]
    active_gain = gain_logs[(active_prime, active_depth)]
    assert prefix_cost[1] < target
    assert prefix_cost[0] + active_cost[0] > target

    remaining = (target - prefix_cost[1], target - prefix_cost[0])
    efficiency = ratio_bounds_positive(active_gain, active_cost)
    fractional_gain = product_bounds_positive(remaining, efficiency)
    gain_lower = prefix_gain[0] + fractional_gain[0]

    c0_upper = log_bounds(Fraction(4 * discriminant_bound))[1]
    affine = (2 - 4 * ALPHA) * w
    x = 2 * (w - target)
    assert x > 0
    # e > 2 implies exp(-x) < 2^(-floor(x)); log(1+t) < t.
    correction_upper = Fraction(1, 4 * discriminant_bound * 2 ** (x.numerator // x.denominator))
    required_upper = c0_upper + affine + correction_upper
    margin_lower = gain_lower - required_upper
    assert margin_lower > 0
    return position, active_prime, active_depth, margin_lower


def as_decimal(x: Fraction, digits: int = 50) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = digits
        return Decimal(x.numerator) / Decimal(x.denominator)


def main() -> None:
    discriminant_bound = exact_checks()
    items, cost_logs, gain_logs, values = build_items()

    # The chosen fractional-knapsack path must be feasible (depth prefixes)
    # and concave (nonincreasing exact interval slopes) through the right
    # endpoint.  Determine that endpoint first.
    right_target = 2 * ALPHA * (2 * W0)
    right_position, _, _, _ = locate_endpoint(items, cost_logs, right_target)
    used_depth = [0] * len(SPLIT_PRIMES)
    previous_efficiency = None
    for _, prime_index, depth in items[: right_position + 1]:
        assert depth == used_depth[prime_index] + 1
        used_depth[prime_index] = depth
        q = SPLIT_PRIMES[prime_index]
        efficiency = ratio_bounds_positive(
            gain_logs[(prime_index, depth)], cost_logs[q]
        )
        if previous_efficiency is not None:
            assert previous_efficiency[0] >= efficiency[1]
        previous_efficiency = efficiency

    left = certify_endpoint(
        items, cost_logs, gain_logs, values, discriminant_bound, W0
    )
    right = certify_endpoint(
        items, cost_logs, gain_logs, values, discriminant_bound, 2 * W0
    )
    print("exact arithmetic tower checks: PASS")
    print("certified monotone frontier items:", right_position + 1)
    print("left segment:", left[:3], "margin lower:", as_decimal(left[3]))
    print("right segment:", right[:3], "margin lower:", as_decimal(right[3]))
    print("rational interval certificate: PASS")


if __name__ == "__main__":
    main()
