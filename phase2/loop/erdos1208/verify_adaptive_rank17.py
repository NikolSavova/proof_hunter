#!/usr/bin/env python3
"""Exact arithmetic + 80-digit adaptive-envelope certificate for Erdős 1208.

This checks the finite data in the rank-17 Golod--Shafarevich tower and the
adaptive prime-power estimate F_2(n) << n^0.49815.  The class-tower
relation-rank theorem and the symbolic sieve proof remain mathematical
inputs, not machine-checked here.
"""

from decimal import Decimal, getcontext

getcontext().prec = 80

ALPHA = Decimal(9963) / Decimal(20000)
RAMIFIED_PRIMES = [
    3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67,
]
RADICANDS = [
    5, 13, 17, 29, 37, 41, 53, 61,
    21, 33, 57, 69, 93, 129, 141, 177, 201,
]
SPLIT_PRIMES = [
    1133681, 7932209, 30529061, 43030381, 47039849, 50266061,
    50726381, 63169721, 78749789, 78827381, 85124441, 112129709,
    113626301, 118676549, 151475561, 162387749, 163384621,
    165163909, 167300129, 170390321, 175244281, 177916909,
    188980601, 192945749, 196650341, 198062861, 199942181,
    218495681, 219918401, 231858329, 245495381, 249623581,
    251342701, 263452901, 271329341, 280061129, 293211701,
    293406629, 296359829, 323480429, 327286049, 327801029,
    332297741, 341249009, 346477069, 346624409, 349047761,
    362047981, 367183781, 397193449, 406054861, 406964749,
    410294849, 427733329, 435184369,
]


def run_lengths(*parts: tuple[int, int]) -> list[int]:
    out = [value for value, count in parts for _ in range(count)]
    assert len(out) == len(SPLIT_PRIMES) == 55
    return out


# Safe interval followed by run lengths (depth, multiplicity), assigned in
# the displayed order of SPLIT_PRIMES.
ROWS = [
    ("4365.9", "4389.1", run_lengths((6, 1), (5, 9), (4, 45))),
    ("4384.2", "4413.7", run_lengths((6, 1), (5, 10), (4, 44))),
    ("4402.8", "4438.4", run_lengths((6, 1), (5, 11), (4, 43))),
    ("4421.4", "4463.0", run_lengths((6, 1), (5, 12), (4, 42))),
    ("4459.0", "4512.3", run_lengths((6, 1), (5, 14), (4, 40))),
    ("4497.0", "4561.6", run_lengths((6, 1), (5, 16), (4, 38))),
    ("4554.0", "4635.5", run_lengths((6, 1), (5, 19), (4, 35))),
    ("4630.4", "4734.0", run_lengths((6, 1), (5, 23), (4, 31))),
    ("4726.5", "4857.2", run_lengths((6, 1), (5, 28), (4, 26))),
    ("4843.0", "5005.0", run_lengths((6, 1), (5, 34), (4, 20))),
    ("4996.2", "5198.3", run_lengths((6, 2), (5, 40), (4, 13))),
    ("5194.1", "5444.7", run_lengths((6, 2), (5, 50), (4, 3))),
    ("5429.0", "5724.2", run_lengths((7, 1), (6, 10), (5, 44))),
    ("5705.1", "6028.9", run_lengths((8, 1), (7, 1), (6, 22), (5, 31))),
    ("6015.6", "6362.2", run_lengths((8, 1), (7, 1), (6, 38), (5, 15))),
    ("6347.6", "6710.8", run_lengths((8, 1), (7, 3), (6, 51))),
    ("6692.5", "7047.7", run_lengths((9, 1), (8, 1), (7, 19), (6, 34))),
    ("7040.7", "7372.5", run_lengths((9, 1), (8, 1), (7, 37), (6, 16))),
    ("7357.4", "7661.2", run_lengths((9, 1), (8, 1), (7, 53))),
    ("7661.2", "7927.1", run_lengths((10, 1), (9, 1), (8, 15), (7, 38))),
    ("7910.1", "8134.0", run_lengths((10, 1), (9, 1), (8, 28), (7, 25))),
    ("8116.8", "8303.3", run_lengths((11, 1), (9, 2), (8, 36), (7, 16))),
    ("8294.2", "8446.5", run_lengths((11, 1), (9, 2), (8, 45), (7, 7))),
    ("8433.5", "8557.9", run_lengths((11, 1), (9, 2), (8, 52))),
    ("8556.7", "8656.2", run_lengths((11, 1), (10, 1), (9, 7), (8, 46))),
    ("8649.2", "8727.4", run_lengths((11, 1), (10, 1), (9, 12), (8, 41))),
    ("8720.0", "8780.9", run_lengths((12, 1), (10, 1), (9, 15), (8, 38))),
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


def invariants(depths: list[int]):
    log_m = sum(
        Decimal(k) * Decimal(q).ln() for q, k in zip(SPLIT_PRIMES, depths)
    )
    log_h = sum(Decimal(k + 1).ln() for k in depths)
    log_lambda = sum(
        sum(Decimal(q) ** Decimal(-e) for e in range(k + 1)).ln()
        for q, k in zip(SPLIT_PRIMES, depths)
    )
    return log_m, log_h, log_lambda


def main() -> None:
    assert len(RAMIFIED_PRIMES) == 18
    assert all(is_prime_u64(p) for p in RAMIFIED_PRIMES)
    assert len(RADICANDS) == 17
    for a in RADICANDS:
        assert a > 0 and a % 4 == 1
        assert all(a % (p * p) for p in RAMIFIED_PRIMES)
    assert len(SPLIT_PRIMES) == len(set(SPLIT_PRIMES)) == 55
    assert gf2_rank([square_class_vector(a) for a in RADICANDS]) == 17
    for q in SPLIT_PRIMES:
        assert q < 2**64 and is_prime_u64(q)
        assert q % 4 == 1
        for a in RADICANDS:
            assert pow(a, (q - 1) // 2, q) == 1

    generator_rank = 17
    relation_rank_bound = generator_rank + len(SPLIT_PRIMES)
    assert relation_rank_bound == 72
    assert 4 * relation_rank_bound < generator_rank**2
    root_discriminant_bound = 1
    for p in RAMIFIED_PRIMES:
        root_discriminant_bound *= p
    assert root_discriminant_bound == 3929160775540133527939545
    d_decimal = Decimal(root_discriminant_bound)

    previous_right = None
    minimum_margin_1 = Decimal(1)
    minimum_margin_2 = Decimal(1)
    for index, (left_s, right_s, depths) in enumerate(ROWS, 1):
        left, right = Decimal(left_s), Decimal(right_s)
        log_m, log_h, log_lambda = invariants(depths)
        margin_1 = ALPHA - log_m / (2 * left)
        assert margin_1 > 0

        # C(w)=log(D Lambda/H)+log(4+z), z=e^(2(log M-w))/D.
        # E_2(w)<=ALPHA iff C(w)<=(4 ALPHA-2)w.  The difference
        # C(w)-(4 ALPHA-2)w is increasing here, as certified at the left.
        z_left = (2 * (log_m - left)).exp() / d_decimal
        assert z_left / 2 < 2 - 4 * ALPHA
        assert z_left < 1  # Equivalently, R > M.
        z_right = (2 * (log_m - right)).exp() / d_decimal
        c_right = (
            d_decimal.ln()
            + log_lambda
            - log_h
            + (Decimal(4) + z_right).ln()
        )
        margin_2 = (4 * ALPHA - 2) * right - c_right
        assert margin_2 > 0
        if previous_right is not None:
            assert left <= previous_right
            assert right >= previous_right
        previous_right = right
        minimum_margin_1 = min(minimum_margin_1, margin_1)
        minimum_margin_2 = min(minimum_margin_2, margin_2)
        print(index, left, right, "margin1", margin_1, "margin2", margin_2)

    w0 = Decimal(ROWS[0][0])
    assert Decimal(ROWS[-1][1]) > 2 * w0
    print("split primes / residue checks:", len(SPLIT_PRIMES), 55 * 17)
    print("generator/relation bound:", generator_rank, relation_rank_bound)
    print("D =", root_discriminant_bound)
    print("covered:", w0, 2 * w0)
    print("minimum margins:", minimum_margin_1, minimum_margin_2)
    print("certified exponent:", ALPHA)


if __name__ == "__main__":
    main()
