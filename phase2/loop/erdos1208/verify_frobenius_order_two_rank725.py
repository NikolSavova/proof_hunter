#!/usr/bin/env python3
"""Certificate for the rank-725 quadratic-Frobenius Erdős 1208 bound."""

from __future__ import annotations

from decimal import Decimal, getcontext


getcontext().prec = 80

RANK = 725
USEFUL_COUNT = 130_681
ALPHA = Decimal(49459) / Decimal(100000)  # 0.49459
W0 = Decimal(1_069_500)
NUMERICAL_ALLOWANCE = Decimal("1e-29")


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def dlog(n: int) -> Decimal:
    return Decimal(n).ln()


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


def local_gains(q: int) -> tuple[Decimal, Decimal]:
    qd = Decimal(q)
    t = Decimal(1) / (qd * qd)
    h1 = ((Decimal(2) / (Decimal(1) + t)).ln()) / 2
    h2 = (
        (
            Decimal(3)
            * (Decimal(1) + t)
            / (Decimal(2) * (Decimal(1) + t + t * t))
        ).ln()
        / 2
    )
    return h1, h2


def interpolate(
    costs: list[Decimal],
    gains: list[Decimal],
    target: Decimal,
    base_cost: Decimal = Decimal(0),
    base_gain: Decimal = Decimal(0),
) -> tuple[Decimal, int, Decimal]:
    cost = base_cost
    gain = base_gain
    for index, (delta_cost, delta_gain) in enumerate(
        zip(costs, gains), start=1
    ):
        if cost + delta_cost >= target:
            fraction = (target - cost) / delta_cost
            return gain + fraction * delta_gain, index, fraction
        cost += delta_cost
        gain += delta_gain
    raise AssertionError("target exceeds the two-stage path")


def main() -> None:
    primes = prime_sieve(2_200_000)
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

    assert len(ramified) == RANK + 1 and ramified[-1] == 5503
    assert len(useful) == USEFUL_COUNT and useful[-1] == 1_747_247
    assert not rejected
    assert not ramified_set.intersection(useful)

    generator_rank = len(ramified) - 1
    relation_bound = generator_rank + len(useful)
    assert generator_rank == RANK
    assert relation_bound == 131_406
    assert 4 * relation_bound < generator_rank * generator_rank

    discriminant_bound = 1
    for p in ramified:
        discriminant_bound *= p
    log_d = dlog(discriminant_bound)

    costs: list[Decimal] = []
    first_gains: list[Decimal] = []
    second_gains: list[Decimal] = []
    first_slopes: list[Decimal] = []
    second_slopes: list[Decimal] = []
    for q in useful:
        cost = dlog(q)
        h1, h2 = local_gains(q)
        costs.append(cost)
        first_gains.append(h1)
        second_gains.append(h2)
        first_slopes.append(h1 / cost)
        second_slopes.append(h2 / cost)

    assert all(a > b for a, b in zip(first_slopes, first_slopes[1:]))
    assert all(a > b for a, b in zip(second_slopes, second_slopes[1:]))

    first_cost = sum(costs, Decimal(0))
    first_gain = sum(first_gains, Decimal(0))
    w_star = first_cost / (2 * ALPHA)
    assert W0 < w_star < 2 * W0

    def correction(w: Decimal) -> Decimal:
        exponent = 2 * (2 * ALPHA - 1) * w - log_d
        return (Decimal(1) + exponent.exp() / 4).ln()

    def rhs(w: Decimal) -> Decimal:
        return (
            Decimal(4).ln()
            + log_d
            + (2 - 4 * ALPHA) * w
            + correction(w)
        )

    gain_left, left_index, left_fraction = interpolate(
        costs, first_gains, 2 * ALPHA * W0
    )
    gain_right, right_index, right_fraction = interpolate(
        costs,
        second_gains,
        2 * ALPHA * (2 * W0),
        base_cost=first_cost,
        base_gain=first_gain,
    )

    margins = [
        gain_left - rhs(W0) - NUMERICAL_ALLOWANCE,
        first_gain - rhs(w_star) - NUMERICAL_ALLOWANCE,
        gain_right - rhs(2 * W0) - NUMERICAL_ALLOWANCE,
    ]
    assert margins[0] > Decimal(23)
    assert margins[1] > Decimal(1800)
    assert margins[2] > Decimal(23)

    for q in useful:
        t = Decimal(1) / Decimal(q)
        assert 2 * (1 + t * t) - (1 + t) ** 2 >= 0
        assert (
            3 * (1 + t) ** 2 * (1 + t * t + t**4)
            - 2 * (1 + t + t * t) ** 2 * (1 + t * t)
            >= 0
        )

    print("ramified primes / last:", len(ramified), ramified[-1])
    print("useful primes / last:", len(useful), useful[-1])
    print("generator/relation bound:", generator_rank, relation_bound)
    print("root-discriminant product digits:", len(str(discriminant_bound)))
    print("log D:", log_d)
    print("w*:", w_star)
    print("left boundary increment:", left_index, left_fraction)
    print("right boundary increment:", right_index, right_fraction)
    print("certified margins:", *margins)
    print("target F_2(n) << n^0.49459: CERTIFIED")


if __name__ == "__main__":
    main()
