#!/usr/bin/env python3
"""Certificate for the rank-20 placewise-depth bound for Erdos 1208.

The exact part checks the tower's ramification data, Frattini basis, split
primes, and Golod--Shafarevich inequality.  The high-precision part checks the
two endpoint inequalities for the concave continuous-depth envelope at
alpha=0.49806.  The symbolic sieve inequality and the standard tame
Shafarevich presentation theorem remain mathematical inputs.
"""

from __future__ import annotations

from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path


ALPHA = Fraction(24903, 50000)  # 0.49806
W0 = Fraction(29076, 5)  # 5815.2
RAMIFIED_PRIMES = [
    3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
]
RADICANDS = [
    5, 13, 17, 29, 37, 41, 53, 61, 73,
    21, 33, 57, 69, 93, 129, 141, 177, 201, 213, 237,
]
SPLIT_PRIMES = [
    int(line)
    for line in Path(__file__).with_name("rank20_split_primes.txt").read_text().split()
]


def is_prime_u64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def gf2_rank(rows: list[int]) -> int:
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


def square_class_vector(a: int) -> int:
    vector, remainder = 0, a
    for i, p in enumerate(RAMIFIED_PRIMES):
        while remainder % p == 0:
            vector ^= 1 << i
            remainder //= p
    assert remainder == 1
    return vector


def exact_checks() -> int:
    assert len(RAMIFIED_PRIMES) == 21
    assert len(RADICANDS) == 20
    assert all(is_prime_u64(p) for p in RAMIFIED_PRIMES)
    for a in RADICANDS:
        assert a > 0 and a % 4 == 1
        assert all(a % (p * p) for p in RAMIFIED_PRIMES)
    assert gf2_rank([square_class_vector(a) for a in RADICANDS]) == 20

    assert len(SPLIT_PRIMES) == len(set(SPLIT_PRIMES)) == 79
    for q in SPLIT_PRIMES:
        assert q < 2**64 and is_prime_u64(q) and q % 4 == 1
        for a in RADICANDS:
            assert pow(a, (q - 1) // 2, q) == 1

    generator_rank = 20
    relation_rank_bound = generator_rank + len(SPLIT_PRIMES)
    assert relation_rank_bound == 99
    assert 4 * relation_rank_bound < generator_rank**2

    discriminant_bound = 1
    for p in RAMIFIED_PRIMES:
        discriminant_bound *= p
    assert discriminant_bound == 1608822383670336453949542277065
    return discriminant_bound


def decimal_certificate(precision: int, discriminant_bound: int):
    with localcontext() as ctx:
        ctx.prec = precision
        alpha = Decimal(ALPHA.numerator) / Decimal(ALPHA.denominator)
        w0 = Decimal(W0.numerator) / Decimal(W0.denominator)
        d_bound = Decimal(discriminant_bound)

        increments = []
        for prime_index, q_int in enumerate(SPLIT_PRIMES):
            q = Decimal(q_int)
            previous = Decimal(0)
            for depth in range(1, 21):
                lam = sum(q ** Decimal(-e) for e in range(depth + 1))
                current = Decimal(depth + 1).ln() - lam.ln()
                gain = current - previous
                cost = q.ln()
                increments.append((gain / cost, cost, gain, prime_index, depth))
                previous = current
        increments.sort(key=lambda item: item[0], reverse=True)

        used_depth = [0] * len(SPLIT_PRIMES)
        for _, _, _, prime_index, depth in increments:
            assert depth == used_depth[prime_index] + 1
            used_depth[prime_index] = depth

        def frontier_gain(cost_target: Decimal):
            cost = gain = Decimal(0)
            for efficiency, increment_cost, increment_gain, prime_index, depth in increments:
                if cost + increment_cost <= cost_target:
                    cost += increment_cost
                    gain += increment_gain
                    continue
                fraction = (cost_target - cost) / increment_cost
                assert 0 <= fraction <= 1
                gain += fraction * increment_gain
                return gain, (prime_index, depth, fraction, increment_gain)
            raise AssertionError("frontier depth cap too small")

        c0 = (Decimal(4) * d_bound).ln()
        endpoint_data = []
        for w in (w0, 2 * w0):
            target_cost = 2 * alpha * w
            gain, active = frontier_gain(target_cost)
            # With L=2 alpha w, z=M^2/R^2 exactly equals the expression below.
            z = (2 * (target_cost - w)).exp() / d_bound
            correction = (Decimal(1) + z / 4).ln()
            required_gain = c0 + (2 - 4 * alpha) * w + correction
            margin = gain - required_gain
            assert z < 1
            assert margin > Decimal("1e-8")
            endpoint_data.append((w, target_cost, gain, margin, z, active))

        # The checked margin must dwarf a conservative accumulation allowance
        # for correctly-rounded Decimal transcendental calls at this precision.
        numerical_allowance = Decimal(100000) * (Decimal(10) ** (-(precision - 10)))
        assert min(row[3] for row in endpoint_data) > numerical_allowance
        return endpoint_data


def main() -> None:
    discriminant_bound = exact_checks()
    low = decimal_certificate(90, discriminant_bound)
    high = decimal_certificate(150, discriminant_bound)
    for row_low, row_high in zip(low, high):
        # Independent-precision stability check for every printed real value.
        for x, y in zip(row_low[:5], row_high[:5]):
            assert abs(x - y) < Decimal("1e-75")

    print("split primes / residue checks:", len(SPLIT_PRIMES), 79 * 20)
    print("generator/relation bound:", 20, 99)
    print("D =", discriminant_bound)
    print("alpha =", Decimal(ALPHA.numerator) / Decimal(ALPHA.denominator))
    for label, row in zip(("left", "right"), high):
        w, cost, gain, margin, z, active = row
        print(label, "w", w, "cost", cost, "gain", gain)
        print(label, "margin", margin, "z", z, "active", active)
    print("continuous endpoint certificate: PASS")


if __name__ == "__main__":
    main()
