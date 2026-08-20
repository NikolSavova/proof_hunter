#!/usr/bin/env python3
"""Checks the rank-221 all-depth prime-assignment dominance conditions."""

from __future__ import annotations

from decimal import Decimal, getcontext

from verify_bounded_inertia_rank221 import (
    ALPHA,
    PACKING_CONSTANT_UPPER,
    RANK,
    USEFUL_COUNT,
    W0,
    gf2_rank,
    local_increment,
    prime_sieve,
)


getcontext().prec = 90


def active_value(q: int, lam: Decimal) -> tuple[Decimal, int]:
    """Return sum_k (g_k-lambda log q)_+ and its prefix length."""
    cost = Decimal(q).ln()
    value = Decimal(0)
    depth = 1
    while True:
        gain = local_increment(q, depth)
        excess = gain - lam * cost
        if excess <= 0:
            return value, depth - 1
        value += excess
        depth += 1
        assert depth < 10_000


def main() -> None:
    primes = prime_sieve(300_000)
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
    assert not rejected
    assert useful[0] == 1_423 and useful[-1] == 128_047

    # Automatic usefulness is false.  For T={7,13}, positivity excludes the
    # lone 3 mod 4 generator 7, so the Frattini field is Q(sqrt(13)).  The
    # unramified q=3 splits in it, while -1 is nonsquare mod 3.
    assert 3 not in (7, 13)
    assert pow(13, (3 - 1) // 2, 3) == 1
    assert pow(3 - 1, (3 - 1) // 2, 3) == 3 - 1

    increments: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for q in useful:
        cost = Decimal(q).ln()
        for depth in range(1, 5):
            gain = local_increment(q, depth)
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, q, depth))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(key=lambda row: row[0], reverse=True)

    def active_slope(target: Decimal) -> tuple[Decimal, int]:
        cost_sum = Decimal(0)
        for index, (slope, cost, _, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                return slope, index
            cost_sum += cost
        raise AssertionError("target beyond frontier")

    discriminant_product = 1
    for p in ramified:
        discriminant_product *= p
    log_d = Decimal(discriminant_product).ln() / 2

    endpoint_data: list[tuple[Decimal, Decimal, Decimal, int]] = []
    for scale in (Decimal(1), Decimal(2)):
        w = scale * W0
        target = 2 * ALPHA * w
        lam, index = active_slope(target)
        exponent = 2 * (2 * ALPHA - 1) * w - log_d
        # Decimal would round the true derivative to 1 at this scale.  Use
        # the rigorous much weaker bound exponent<-10 instead.
        assert exponent < Decimal(-10)
        rho_lower = Decimal(1) / (
            Decimal(1) + Decimal(-10).exp() / PACKING_CONSTANT_UPPER
        )
        endpoint_data.append((lam, rho_lower, target, index))

    # Fourth and later depths of every prefix-useful prime are inactive at
    # both endpoints.  The analytic theorem itself allows arbitrary depths.
    assert maximum_fourth_slope < min(row[0] for row in endpoint_data)

    first_unramified = useful[0]
    t0 = Decimal(1) / Decimal(first_unramified) ** 2
    derivative_tail_bound = t0 / (Decimal(1) - t0) ** 2

    for lam, rho_lower, _, _ in endpoint_data:
        # These are the two hypotheses of the all-depth exchange theorem.
        assert rho_lower > Decimal(1) / Decimal(3).ln()
        assert lam > derivative_tail_bound

        # Finite adversarial stress of the analytic score monotonicities.
        # C_rho(p)=rho*log(p)/2+V_lambda(p) must increase everywhere;
        # V_lambda(p) must decrease after the ramified prefix.
        previous_c: Decimal | None = None
        previous_v: Decimal | None = None
        max_depth = 0
        for p in [q for q in primes if q != 2 and q <= 150_000]:
            value, depth = active_value(p, lam)
            max_depth = max(max_depth, depth)
            c_score = rho_lower * Decimal(p).ln() / 2 + value
            if previous_c is not None:
                assert c_score > previous_c
            previous_c = c_score
            if p >= first_unramified:
                if previous_v is not None:
                    assert value <= previous_v
                previous_v = value

        assert max_depth < 30

    print("automatic usefulness counterexample: T={7,13}, q=3: CHECKED")
    print("rank / ramified / useful:", RANK, len(ramified), len(useful))
    print("ramified/useful boundary:", ramified[-1], useful[0])
    print("tail derivative bound:", derivative_tail_bound)
    for label, (lam, rho_lower, target, index) in zip(
        ("left", "right"), endpoint_data
    ):
        print(
            label,
            "target/index/lambda/rho_lower:",
            target,
            index,
            lam,
            rho_lower,
        )
    print("all-depth arbitrary-prime prefix dominance conditions: CERTIFIED")


if __name__ == "__main__":
    main()
