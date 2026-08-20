#!/usr/bin/env python3
"""Verifier for the optimistic real-cubic pro-2 dominance audit."""

from __future__ import annotations

from bisect import bisect_left
from math import log, log1p


TARGET_ALPHA = 0.49458539
COMPETITIVE_S = 243


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def polynomial_value(x: int) -> int:
    return x**3 + x**2 - 2 * x - 1


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def local_increment(q: int, depth: int) -> float:
    t = q ** -2
    return (
        log1p(1 / depth)
        + log1p(-(t**depth))
        - log1p(-(t ** (depth + 1)))
    ) / 2


def build_frontier(split_primes: list[int], s: int):
    d = 3 * s
    relation_budget = (d * d - 1) // 4 - d
    full_orbits, remainder = divmod(relation_budget, 3)
    ramified = split_primes[:s]
    needed_q = full_orbits + (1 if remainder else 0)
    useful = split_primes[s : s + needed_q]
    assert len(useful) == needed_q

    items: list[tuple[float, float, float, int, int]] = []
    for index, q in enumerate(useful):
        multiplicity = 3 if index < full_orbits else remainder
        cost = log(q) / 3
        for _ in range(multiplicity):
            for depth in range(1, 5):
                gain = local_increment(q, depth) / 3
                items.append((gain / cost, cost, gain, q, depth))
    items.sort(reverse=True)

    costs: list[float] = []
    gains: list[float] = []
    cost_sum = 0.0
    gain_sum = 0.0
    for _, cost, gain, _, _ in items:
        cost_sum += cost
        gain_sum += gain
        costs.append(cost_sum)
        gains.append(gain_sum)

    log_d = log(49) / 3 + sum(log(p) for p in ramified)
    return d, relation_budget, ramified, useful, items, costs, gains, log_d


def envelope(
    target: float,
    items: list[tuple[float, float, float, int, int]],
    costs: list[float],
    gains: list[float],
) -> float:
    index = bisect_left(costs, target)
    if index >= len(items):
        return -1e100
    if index == 0:
        return target * items[0][0]
    return gains[index - 1] + (target - costs[index - 1]) * items[index][0]


def best_margin(split_primes: list[int], s: int, alpha: float):
    data = build_frontier(split_primes, s)
    _, _, _, _, items, costs, gains, log_d = data
    constant = log(4) + log_d

    def margin(w: float) -> tuple[float, float, float]:
        first = envelope(2 * alpha * w, items, costs, gains)
        first -= constant + (2 - 4 * alpha) * w
        second = envelope(4 * alpha * w, items, costs, gains)
        second -= constant + (2 - 4 * alpha) * 2 * w
        return min(first, second), first, second

    low = max(1.0, log_d)
    high = costs[-1] / (4 * alpha) * 0.999
    best = (-1e100, 0.0, 0.0, 0.0)
    for _ in range(6):
        for step in range(251):
            w = low + (high - low) * step / 250
            value, first, second = margin(w)
            if value > best[0]:
                best = value, w, first, second
        mesh = (high - low) / 250
        low = max(1.0, best[1] - 3 * mesh)
        high = best[1] + 3 * mesh
    return best, data


def main() -> None:
    # Exact base-field checks requiring no computer algebra package.
    assert polynomial_value(-2) < 0 < polynomial_value(-1)
    assert polynomial_value(-1) > 0 > polynomial_value(0)
    assert polynomial_value(1) < 0 < polynomial_value(2)
    # disc(X^3+bX^2+cX+d) for b=1,c=-2,d=-1.
    b, c, d0 = 1, -2, -1
    discriminant = b * b * c * c - 4 * c**3 - 4 * b**3 * d0
    discriminant -= 27 * d0 * d0 - 18 * b * c * d0
    assert discriminant == 49
    assert 14 / 9 < 2  # Minkowski bound, hence class number one.
    # Norm(theta)=1 and Norm(theta+1)=-f(-1)=-1.
    assert 1 == 1 and -polynomial_value(-1) == -1
    # On the root intervals (-2,-1),(-1,0),(1,2), the signatures of
    # -1, theta, theta+1 are 111, 110, 100 and have full F_2-rank.
    assert gf2_rank([0b111, 0b110, 0b100]) == 3
    # f has no root modulo 2, hence it is irreducible cubic modulo 2.
    assert all(polynomial_value(x) % 2 for x in (0, 1))

    primes = prime_sieve(3_000_000)
    split_primes = [
        p for p in primes if p != 7 and p % 7 in (1, 6)
    ]
    assert split_primes[:6] == [13, 29, 41, 43, 71, 83]

    best, data = best_margin(
        split_primes, COMPETITIVE_S, TARGET_ALPHA
    )
    d, relation_budget, ramified, useful, items, costs, gains, log_d = data
    assert d == 729
    assert relation_budget == 132_131
    assert divmod(relation_budget, 3) == (44_043, 2)
    assert ramified[-1] == 5_573
    assert useful[-1] == 1_767_919
    assert best[0] < -10

    # Every omitted fifth-depth slope is below the active right slope at the
    # target optimizer, so four depths suffice for this failure certificate.
    right_target = 4 * TARGET_ALPHA * best[1]
    right_index = bisect_left(costs, right_target)
    active_right_slope = items[right_index][0]
    maximum_fifth_slope = max(
        local_increment(q, 5) / log(q) for q in useful
    )
    assert maximum_fifth_slope < active_right_slope

    # A coarse profile brackets the competitive window.  This is diagnostic,
    # while the s=243 failure above has a double-digit margin.
    profile_s = [20, 40, 80, 120, 160, 200, 220, 230, 237, 243, 250, 270, 300]
    profile = []
    for s in profile_s:
        row, _ = best_margin(split_primes, s, TARGET_ALPHA)
        profile.append((s, row[0]))
    assert max(value for _, value in profile) < -9

    print("base discriminant / inert dyadic polynomial: PASS", discriminant)
    print("competitive s / d / relation budget:", COMPETITIVE_S, d, relation_budget)
    print("last ramified / useful split primes:", ramified[-1], useful[-1])
    print("log root-discriminant bound:", log_d)
    print("target optimized margin / w:", best)
    print("right / maximum fifth slopes:", active_right_slope, maximum_fifth_slope)
    print("coarse target-margin profile:", profile)
    print("PASS: even the optimistic real-cubic model does not beat 0.49458539")


if __name__ == "__main__":
    main()
