#!/usr/bin/env python3
"""Exact verifier for the explicit constants in the Erdős 1208 attack.

The only floating-point operations are the final logarithmic evaluations.
All primality and quadratic-residue checks are exact integer computations.
The listed primes are below 2^32; deterministic Miller--Rabin is nevertheless
implemented with the standard bases valid below 2^64.
"""

from __future__ import annotations

import math


RAMIFIED_PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

# A basis for the maximal totally real multiquadratic extension of Q
# unramified outside RAMIFIED_PRIMES used in the certificate.
RADICANDS = [5, 13, 17, 29, 37, 41, 53, 61, 21, 33, 57, 69, 93, 129, 141, 177]

SPLIT_PRIMES = [
    1133681, 2184101, 7932209, 8869649, 16145221, 25584389,
    30529061, 30589961, 43030381, 46633109, 47039849, 48473881,
    50266061, 50726381, 53683769, 58553249, 63169721, 71960489,
    78749789, 78827381, 85124441, 93586249, 93656741, 94521041,
    97978981, 98291969, 105702341, 112129709, 113626301, 118676549,
    147493369, 151475561, 151562629, 162387749, 163384621, 165163909,
    167300129, 169920869, 170390321, 175244281, 177916909, 184204121,
    188980601, 191165729, 192945749, 196193609, 196650341,
]

# Prime-power depths: 9, 8, fifteen 7s, and thirty 6s.
DEPTHS = [9, 8] + [7] * 15 + [6] * 30


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller--Rabin for 0 <= n < 2^64."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
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
    """Rank of bit-vector rows over GF(2)."""
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
    """Parity vector of a over the certified ramification-prime basis."""
    vector = 0
    remainder = a
    for i, p in enumerate(RAMIFIED_PRIMES):
        while remainder % p == 0:
            vector ^= 1 << i
            remainder //= p
    assert remainder == 1, (a, remainder)
    return vector


def main() -> None:
    assert len(RADICANDS) == 16
    assert len(SPLIT_PRIMES) == len(DEPTHS) == 47
    assert len(set(SPLIT_PRIMES)) == 47
    assert gf2_rank([square_class_vector(a) for a in RADICANDS]) == 16

    for q in SPLIT_PRIMES:
        assert q < 2**64 and is_prime_u64(q), f"composite: {q}"
        assert q % 4 == 1, f"not 1 mod 4: {q}"
        for a in RADICANDS:
            assert math.gcd(a, q) == 1
            assert pow(a, (q - 1) // 2, q) == 1, (q, a)

    # Golod--Shafarevich certificate.  The 16 generators come from the
    # independent square classes above.  Killing the 47 split Frobenii adds at
    # most 47 relations, while leaving the Frattini quotient unchanged.
    generator_rank = 16
    relation_rank_bound = generator_rank + len(SPLIT_PRIMES)
    assert relation_rank_bound == 63
    assert 4 * relation_rank_bound < generator_rank**2

    D = math.prod(RAMIFIED_PRIMES)
    assert D == 58644190679703485491635

    H = math.prod(k + 1 for k in DEPTHS)
    assert H == 71372928188206730050754751756512652165120
    log_H = math.log(H)
    log_M = sum(k * math.log(q) for q, k in zip(SPLIT_PRIMES, DEPTHS))
    # Lambda = product_i sum_{e=0}^{K_i} q_i^{-e}.  Evaluate its log stably.
    log_Lambda = sum(
        math.log(sum(q ** (-e) for e in range(k + 1)))
        for q, k in zip(SPLIT_PRIMES, DEPTHS)
    )
    Lambda = math.exp(log_Lambda)
    H_over_Lambda = math.exp(log_H - log_Lambda)

    # y is the positive solution of 4D y^2 + y = H/Lambda.
    # The rationalized formula avoids cancellation.
    y = 2.0 * H_over_Lambda / (1.0 + math.sqrt(1.0 + 16.0 * D * H_over_Lambda))
    r = math.log(y)
    epsilon = r / (4.0 * log_M + 2.0 * r)

    assert y > 1.0
    assert epsilon > 0.000925
    assert 0.5 - epsilon < 0.4991

    # Method barrier from FULL_ATTACK.md.  For every admissible q_i and K_i,
    # q_i >= 5 and K_i + 1 <= 2**K_i.  Hence r/log(M) is universally below
    # log(2)/(2 log(5)), regardless of the tower or chosen depths.
    barrier_x = math.log(2.0) / (2.0 * math.log(5.0))
    barrier_epsilon = barrier_x / (4.0 + 2.0 * barrier_x)
    barrier_exponent = 0.5 - barrier_epsilon
    assert barrier_exponent > 0.4513
    assert barrier_exponent < 0.4515

    print(f"split primes checked: {len(SPLIT_PRIMES)}")
    print(f"quadratic-residue checks: {len(SPLIT_PRIMES) * len(RADICANDS)}")
    print(f"generator/relation bound: {generator_rank}/{relation_rank_bound}")
    print(f"D = {D}")
    print(f"H = {H}")
    print(f"log H = {log_H:.15f}")
    print(f"Lambda = {Lambda:.15f}")
    print(f"log M = {log_M:.15f}")
    print(f"r = log y = {r:.15f}")
    print(f"epsilon = {epsilon:.15f}")
    print(f"certified exponent 1/2-epsilon = {0.5 - epsilon:.15f}")
    print("safe statement: F_2(n) << n^0.4991")
    print(
        "prime-power-family exponent floor = "
        f"{barrier_exponent:.15f} (cannot reach 1/3)"
    )


if __name__ == "__main__":
    main()
