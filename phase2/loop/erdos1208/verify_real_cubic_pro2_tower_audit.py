#!/usr/bin/env python3
"""Finite certificate for the literal Q(zeta_7)^+ pro-2 tower audit.

This does not certify the Kummer/Shafarevich inputs, which are stated and
audited separately in REAL_CUBIC_PRO2_TOWER_AUDIT.md.  It checks the exact
prime sets, conservative Golod--Shafarevich budget, root-discriminant cost,
and the all-depth numerical envelope.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


getcontext().prec = 90

RAMIFIED_RATIONAL_COUNT = 269
SAFE_GENERATOR_RANK = 3 * RAMIFIED_RATIONAL_COUNT - 3
BASE_RELATION_EXCESS = 2
USEFUL_RATIONAL_COUNT = 53_599
ALPHA = Decimal(49_489) / Decimal(100_000)  # 0.49489
W0 = Decimal(461_600)
NUMERICAL_ALLOWANCE = Decimal("1e-25")


def cubic_discriminant(a: int, b: int, c: int) -> int:
    """Discriminant of x^3+a*x^2+b*x+c."""
    return a * a * b * b - 4 * b**3 - 4 * a**3 * c - 27 * c * c + 18 * a * b * c


def rank_mod_2(rows: list[int]) -> int:
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


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


def local_increment(q: int, depth: int) -> Decimal:
    qd = Decimal(q)
    z = Decimal(1) / (qd * qd)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= z
        total += power
    current_value = Decimal(depth + 1) / total
    previous_value = Decimal(depth) / previous_total
    return (current_value / previous_value).ln() / 2


def main() -> None:
    # E=Q(theta), theta^3+theta^2-2theta-1=0.  These exact checks give
    # disc(E)=49 and the class-number-one Minkowski bound 14/9<2.
    assert cubic_discriminant(1, -2, -1) == 49
    assert 6 * 7 < 2 * 27
    # The three roots lie in (-2,-1), (-1,0), (1,2).  Thus the negative-sign
    # vectors of -1, theta, theta+1 are 111, 110, 100 and have full rank.
    assert rank_mod_2([0b111, 0b110, 0b100]) == 3
    # x^3+x^2+1 has no F_2 root, so 2 is inert (and unramified) in E.
    assert all((x**3 + x**2 + 1) % 2 for x in (0, 1))

    primes = prime_sieve(4_700_000)

    # E/Q is cyclic of conductor 7.  Away from 7, complete splitting in E
    # is equivalent to p == +/-1 (mod 7).
    split = [p for p in primes if p != 7 and p % 7 in (1, 6)]
    ramified = split[:RAMIFIED_RATIONAL_COUNT]
    ramified_set = set(ramified)
    useful = [
        q
        for q in primes
        if q not in ramified_set and q % 28 in (1, 13)
    ][:USEFUL_RATIONAL_COUNT]

    assert len(ramified) == RAMIFIED_RATIONAL_COUNT
    assert ramified[-1] == 6_287
    assert len(useful) == USEFUL_RATIONAL_COUNT
    assert useful[-1] == 4_603_241
    assert not ramified_set.intersection(useful)
    assert all(p % 7 in (1, 6) for p in ramified)
    assert all(q % 7 in (1, 6) and q % 4 == 1 for q in useful)

    d0 = SAFE_GENERATOR_RANK
    r0 = d0 + BASE_RELATION_EXCESS
    relation_bound = r0 + 3 * USEFUL_RATIONAL_COUNT
    assert d0 == 804 and r0 == 806
    assert relation_bound == 161_603
    assert 4 * relation_bound == 646_412 < 646_416 == d0 * d0
    # One additional rational useful prime would cost its three conjugate
    # prime-ideal square relators and violate the conservative strict budget.
    assert 4 * (relation_bound + 3) > d0 * d0

    # Each selected split rational prime represents three prime ideals of
    # norm p.  Dividing their summed logarithmic discriminant cost by
    # [E:Q]=3 gives exactly log(p); the same cancellation holds for each
    # grouped local depth increment.
    assert 3 * RAMIFIED_RATIONAL_COUNT == 807
    assert 3 * USEFUL_RATIONAL_COUNT == 160_797

    # rd(E)=49^(1/3), and ramifying at all three primes over p contributes
    # at most p to the relative root discriminant.
    log_d = Decimal(49).ln() / 3
    for p in ramified:
        log_d += Decimal(p).ln()

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
        return (Decimal(1) + exponent.exp() / 4).ln()

    def rhs(w: Decimal) -> Decimal:
        return (
            Decimal(4).ln()
            + log_d
            + (2 - 4 * ALPHA) * w
            + correction(w)
        )

    left_gain, left_index, left_fraction, left_slope = envelope(2 * ALPHA * W0)
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

    print("ramified rational primes / last:", len(ramified), ramified[-1])
    print("useful rational primes / last:", len(useful), useful[-1])
    print("safe d / base r / final r:", d0, r0, relation_bound)
    print("log root-discriminant bound:", log_d)
    print("left boundary:", left_index, left_fraction, depth_profile(left_index))
    print("right boundary:", right_index, right_fraction, depth_profile(right_index))
    print("right / maximum fourth slopes:", right_slope, maximum_fourth_slope)
    print("certified margins:", *margins)
    print("literal cubic family F_2(n) << n^0.49489: CERTIFIED")


if __name__ == "__main__":
    main()
