#!/usr/bin/env python3
"""Certificate for the order-two-Frobenius Erdős 1208 bound.

Exact integer arithmetic checks the prime lists and Golod--Shafarevich
inequality.  Python Decimal's correctly rounded ln/exp operations at 80 digits
check the three phase margins.  The final printed margins subtract a vastly
conservative numerical allowance.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


getcontext().prec = 80

RANK = 400
USEFUL_COUNT = 39599
ALPHA = Decimal(4947) / Decimal(10000)  # 0.4947
W0 = Decimal(345000)
NUMERICAL_ALLOWANCE = Decimal("1e-30")


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
    for index, (dcost, dgain) in enumerate(zip(costs, gains), start=1):
        if cost + dcost >= target:
            fraction = (target - cost) / dcost
            return gain + fraction * dgain, index, fraction
        cost += dcost
        gain += dgain
    assert target <= cost
    return gain, len(costs), Decimal(1)


def main() -> None:
    # The last useful prime is 479,939, so this limit has slack.
    primes = prime_sieve(600_000)
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
    rejected_nonresidue_test: list[int] = []
    for q in primes:
        if q == 2 or q in ramified_set:
            continue
        if q % 4 == 1:
            useful.append(q)
        else:
            # A nonzero Frattini class guarantees that the order-two
            # Frobenius relator leaves an actual involution.
            if any(pow(a, (q - 1) // 2, q) == q - 1 for a in radicands):
                useful.append(q)
            else:
                rejected_nonresidue_test.append(q)
        if len(useful) == USEFUL_COUNT:
            break

    assert len(ramified) == 401 and ramified[-1] == 2753
    assert len(useful) == USEFUL_COUNT and useful[-1] == 479_939
    assert len(set(ramified)) == len(ramified)
    assert len(set(useful)) == len(useful)
    assert not ramified_set.intersection(useful)
    assert not rejected_nonresidue_test
    for q in useful:
        if q % 4 == 3:
            assert any(pow(a, (q - 1) // 2, q) == q - 1 for a in radicands)

    # One parity condition on the 3 mod 4 ramified primes gives rank 400.
    assert any(p % 4 == 3 for p in ramified)
    generator_rank = len(ramified) - 1
    relation_bound = generator_rank + len(useful)
    assert generator_rank == RANK
    assert relation_bound == 39_999
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

    l1 = sum(costs, Decimal(0))
    g1 = sum(first_gains, Decimal(0))
    w_star = l1 / (2 * ALPHA)
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

    target_left = 2 * ALPHA * W0
    gain_left, left_index, left_fraction = interpolate(
        costs, first_gains, target_left
    )

    target_right = 2 * ALPHA * (2 * W0)
    gain_right, right_index, right_fraction = interpolate(
        costs,
        second_gains,
        target_right,
        base_cost=l1,
        base_gain=g1,
    )

    margins = [
        gain_left - rhs(W0) - NUMERICAL_ALLOWANCE,
        g1 - rhs(w_star) - NUMERICAL_ALLOWANCE,
        gain_right - rhs(2 * W0) - NUMERICAL_ALLOWANCE,
    ]
    assert margins[0] > Decimal("76.38")
    assert margins[1] > Decimal("804.49")
    assert margins[2] > Decimal("106.25")

    # The f=1 versus f=2 inequalities reduce to the two positive
    # polynomial factorizations displayed in the proof note.  Check them at
    # every useful prime as a guard against a transcription error.
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
    print("target F_2(n) << n^0.4947: CERTIFIED")


if __name__ == "__main__":
    main()
