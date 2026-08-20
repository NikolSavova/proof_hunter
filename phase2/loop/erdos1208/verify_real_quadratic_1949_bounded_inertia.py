#!/usr/bin/env python3
"""Certificate for the bounded-inertia Q(sqrt(1949)) disk construction."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt


getcontext().prec = 90

FIELD_DISCRIMINANT = 1_949
OMEGA_CONSTANT = (FIELD_DISCRIMINANT - 1) // 4
RAMIFIED_IDEAL_COUNT = 229
SAFE_GENERATOR_RANK = 227
BASE_RELATION_EXCESS = 1
USEFUL_IDEAL_COUNT = 12_425
ALPHA = Decimal(49_371_211) / Decimal(100_000_000)  # 0.49371211
W0 = Decimal("44705.08")
NUMERICAL_ALLOWANCE = Decimal("1e-25")
PACKING_CONSTANT_UPPER = Decimal(424) / Decimal(333)


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


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


def norm(element: tuple[int, int]) -> int:
    a, b = element
    return a * a + a * b - OMEGA_CONSTANT * b * b


def conjugate(element: tuple[int, int]) -> tuple[int, int]:
    a, b = element
    return a + b, -b


def multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    a, b = left
    x, y = right
    return (
        a * x + OMEGA_CONSTANT * b * y,
        a * y + b * x + b * y,
    )


def negative_at_embedding(element: tuple[int, int], conjugate_place: bool) -> int:
    """Exact sign of a+b(1+/-sqrt(D))/2."""
    a, b = element
    rational_part = 2 * a + b
    radical_part = -b if conjugate_place else b
    if rational_part >= 0 and radical_part >= 0:
        return 0
    if rational_part <= 0 and radical_part <= 0:
        return 1
    rational_square = rational_part * rational_part
    radical_square = radical_part * radical_part * FIELD_DISCRIMINANT
    assert rational_square != radical_square
    if rational_part > 0:
        return int(rational_square < radical_square)
    return int(radical_square < rational_square)


def generator_of_prime(p: int) -> tuple[int, int]:
    """Find a generator of a principal prime above split/ramified p."""
    for absolute_b in range(10_001):
        candidates = (absolute_b, -absolute_b) if absolute_b else (0,)
        for b in candidates:
            for target in (p, -p):
                square = FIELD_DISCRIMINANT * b * b + 4 * target
                if square < 0:
                    continue
                x = isqrt(square)
                if x * x != square:
                    continue
                for signed_x in {x, -x}:
                    if (signed_x - b) % 2 == 0:
                        result = ((signed_x - b) // 2, b)
                        assert abs(norm(result)) == p
                        return result
    raise AssertionError(f"prime generator search exhausted at {p}")


def tonelli_shanks(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    assert pow(value, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        return pow(value, (p + 1) // 4, p)
    odd_part = p - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        power_of_two += 1
        odd_part //= 2
    nonresidue = 2
    while pow(nonresidue, (p - 1) // 2, p) != p - 1:
        nonresidue += 1
    m = power_of_two
    c = pow(nonresidue, odd_part, p)
    t = pow(value, odd_part, p)
    root = pow(value, (odd_part + 1) // 2, p)
    while t != 1:
        i = 1
        test = t * t % p
        while test != 1:
            test = test * test % p
            i += 1
        multiplier = pow(c, 1 << (m - i - 1), p)
        root = root * multiplier % p
        t = t * multiplier * multiplier % p
        c = multiplier * multiplier % p
        m = i
    assert root * root % p == value
    return root


def prime_ideals(primes: list[int], norm_limit: int):
    ideals: list[tuple[int, int, str, int | None]] = []
    for p in primes:
        if p == 2 or p > norm_limit:
            continue
        if FIELD_DISCRIMINANT % p == 0:
            ideals.append((p, p, "ramified", None))
            continue
        symbol = pow(FIELD_DISCRIMINANT % p, (p - 1) // 2, p)
        if symbol == 1:
            square_root = tonelli_shanks(FIELD_DISCRIMINANT, p)
            inverse_two = (p + 1) // 2
            roots = sorted(
                {
                    (1 + square_root) * inverse_two % p,
                    (1 - square_root) * inverse_two % p,
                }
            )
            assert len(roots) == 2
            ideals.extend((p, p, "split", root) for root in roots)
        else:
            assert symbol == p - 1
            if p * p <= norm_limit:
                ideals.append((p * p, p, "inert", None))
    ideals.sort(key=lambda row: (row[0], row[1], row[2], row[3] or -1))
    return ideals


def local_increment(norm_q: int, depth: int) -> Decimal:
    q = Decimal(norm_q)
    t = Decimal(1) / (q * q)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= t
        total += power
    current_value = Decimal(depth + 1) / total
    previous_value = Decimal(depth) / previous_total
    return (current_value / previous_value).ln() / 2


def main() -> None:
    # A rational lower bound for pi, hence 4/pi < 424/333.
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    assert 16 * atan_fifth_lower - 4 * Fraction(1, 239) > Fraction(333, 106)

    primes = prime_sieve(200_000)
    assert all(FIELD_DISCRIMINANT % p for p in primes if p * p <= FIELD_DISCRIMINANT)
    assert 1 + 4 * OMEGA_CONSTANT == FIELD_DISCRIMINANT
    assert FIELD_DISCRIMINANT % 8 == 5  # the dyadic prime is inert and unramified

    # Minkowski gives an ideal of norm <23 in every class.  The only
    # nontrivial prime ideals below 23 lie over 5, 13, and 19, and the
    # displayed elements generate them (and their conjugates).
    assert FIELD_DISCRIMINANT < 46 * 46
    class_generators = [(-151, -7), (43, 2), (-23, 1)]
    assert [norm(element) for element in class_generators] == [-5, -13, 19]
    small_ideal_norms: list[tuple[int, int]] = []
    for p in primes:
        if p >= 23:
            break
        if p == 2:
            local_norm = 4
        elif FIELD_DISCRIMINANT % p == 0:
            local_norm = p
        elif pow(FIELD_DISCRIMINANT % p, (p - 1) // 2, p) == 1:
            local_norm = p
        else:
            local_norm = p * p
        if local_norm < 23:
            small_ideal_norms.append((p, local_norm))
    assert small_ideal_norms == [(2, 4), (3, 9), (5, 5), (13, 13), (19, 19)]

    # -1 and this norm-minus-one unit have full signature rank.
    fundamental_unit = (81_333, 3_770)
    assert norm(fundamental_unit) == -1
    assert negative_at_embedding(fundamental_unit, False) == 0
    assert negative_at_embedding(fundamental_unit, True) == 1

    ideals = prime_ideals(primes, 200_000)
    ramified_ideals = ideals[:RAMIFIED_IDEAL_COUNT]
    assert ramified_ideals[-1][:2] == (1_303, 1_303)

    prime_generator_cache: dict[int, tuple[int, int]] = {}
    ramified_generators: list[tuple[int, int]] = []
    for _, p, kind, root in ramified_ideals:
        if kind == "inert":
            generator = (p, 0)
        else:
            base_generator = prime_generator_cache.setdefault(p, generator_of_prime(p))
            if kind == "ramified":
                generator = base_generator
            else:
                assert root is not None
                other_generator = conjugate(base_generator)
                generator = (
                    base_generator
                    if (base_generator[0] + base_generator[1] * root) % p == 0
                    else other_generator
                )
                assert (generator[0] + generator[1] * root) % p == 0
        ramified_generators.append(generator)

    # Compute the four sign/mod-4 constraints on S-unit squareclasses.
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if norm((a, b)) % 2
    ]

    def multiply_mod_four(left: tuple[int, int], right: tuple[int, int]):
        product = multiply(left, right)
        return product[0] % 4, product[1] % 4

    square_residues = frozenset(
        multiply_mod_four(unit, unit) for unit in units_mod_four
    )
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units_mod_four:
        coset = frozenset(
            multiply_mod_four(unit, square) for square in square_residues
        )
        if coset not in cosets:
            cosets.append(coset)
    assert len(units_mod_four) == 12
    assert len(square_residues) == 3
    assert len(cosets) == 4

    def coset_index(element: tuple[int, int]) -> int:
        residue = element[0] % 4, element[1] % 4
        return next(index for index, coset in enumerate(cosets) if residue in coset)

    identity_index = cosets.index(square_residues)
    nonidentity = [index for index in range(4) if index != identity_index]
    coset_bits = {identity_index: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    product_index = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert product_index == nonidentity[2]
    coset_bits[product_index] = 3
    for left in units_mod_four:
        for right in units_mod_four:
            assert coset_bits[coset_index(multiply_mod_four(left, right))] == (
                coset_bits[coset_index(left)] ^ coset_bits[coset_index(right)]
            )

    def constraint_column(element: tuple[int, int]) -> int:
        signs = negative_at_embedding(element, False)
        signs |= negative_at_embedding(element, True) << 1
        return signs | (coset_bits[coset_index(element)] << 2)

    kummer_generators = [(-1, 0), fundamental_unit] + ramified_generators
    columns = [constraint_column(element) for element in kummer_generators]
    constraint_rows = [
        sum(((column >> bit) & 1) << index for index, column in enumerate(columns))
        for bit in range(4)
    ]
    constraint_rank = gf2_rank(constraint_rows)
    assert len(kummer_generators) == RAMIFIED_IDEAL_COUNT + 2
    assert constraint_rank == 4
    assert len(kummer_generators) - constraint_rank == SAFE_GENERATOR_RANK

    # Select useful ideals.  For norm 3 modulo 4, certify that Frobenius is
    # nonzero on the explicit 227-dimensional Kummer kernel.
    useful_ideals: list[tuple[int, int, str, int | None]] = []
    rejected_ideals: list[tuple[int, int, str, int | None]] = []
    for ideal in ideals[RAMIFIED_IDEAL_COUNT:]:
        norm_q, p, kind, root = ideal
        useful = True
        if norm_q % 4 == 3:
            assert kind == "split" and root is not None and norm_q == p
            functional = 0
            for index, (a, b) in enumerate(kummer_generators):
                residue = (a + b * root) % p
                assert residue
                if pow(residue, (p - 1) // 2, p) == p - 1:
                    functional |= 1 << index
            useful = gf2_rank(constraint_rows + [functional]) > constraint_rank
        if useful:
            useful_ideals.append(ideal)
        else:
            rejected_ideals.append(ideal)
        if len(useful_ideals) == USEFUL_IDEAL_COUNT:
            break
    assert len(useful_ideals) == USEFUL_IDEAL_COUNT
    assert useful_ideals[-1][:2] == (136_693, 136_693)
    assert not rejected_ideals

    relation_bound = (
        SAFE_GENERATOR_RANK
        + BASE_RELATION_EXCESS
        + RAMIFIED_IDEAL_COUNT
        + USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 12_882
    assert 4 * relation_bound == SAFE_GENERATOR_RANK**2 - 1
    # d^2-4(d+12655) is increasing for every possible d>=227.
    assert 2 * SAFE_GENERATOR_RANK - 4 > 0

    log_root_discriminant = Decimal(FIELD_DISCRIMINANT).ln() / 2
    for norm_q, _, _, _ in ramified_ideals:
        log_root_discriminant += Decimal(norm_q).ln() / 4

    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, (norm_q, _, _, _) in enumerate(useful_ideals):
        cost = Decimal(norm_q).ln() / 2
        previous_gain: Decimal | None = None
        for depth in range(1, 5):
            gain = local_increment(norm_q, depth) / 2
            if previous_gain is not None:
                assert previous_gain > gain
            previous_gain = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, norm_q, depth, ideal_index))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)

    seen = {index: 0 for index in range(USEFUL_IDEAL_COUNT)}
    for _, _, _, _, depth, ideal_index in increments:
        assert depth == seen[ideal_index] + 1
        seen[ideal_index] = depth

    def envelope(target: Decimal) -> tuple[Decimal, int, Decimal, Decimal]:
        cost_sum = Decimal(0)
        gain_sum = Decimal(0)
        for index, (slope, cost, gain, _, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                fraction = (target - cost_sum) / cost
                assert 0 <= fraction <= 1
                return gain_sum + fraction * gain, index, fraction, slope
            cost_sum += cost
            gain_sum += gain
        raise AssertionError("target exceeds certified frontier")

    def rhs(alpha: Decimal, w: Decimal) -> Decimal:
        exponent = 2 * (2 * alpha - 1) * w - log_root_discriminant
        correction = (
            Decimal(1) + exponent.exp() / PACKING_CONSTANT_UPPER
        ).ln()
        return (
            PACKING_CONSTANT_UPPER.ln()
            + log_root_discriminant
            + (2 - 4 * alpha) * w
            + correction
        )

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert maximum_fourth_slope < right[3]
    margins = [
        left[0] - rhs(ALPHA, W0) - NUMERICAL_ALLOWANCE,
        right[0] - rhs(ALPHA, 2 * W0) - NUMERICAL_ALLOWANCE,
    ]
    assert min(margins) > Decimal("0.0005")

    def endpoint_margin(alpha: Decimal, endpoint: int) -> Decimal:
        if endpoint == 1:
            return envelope(2 * alpha * W0)[0] - rhs(alpha, W0)
        assert endpoint == 2
        return envelope(4 * alpha * W0)[0] - rhs(alpha, 2 * W0)

    threshold_brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (1, 2):
        low = Decimal("0.49371210")
        high = Decimal("0.49371211")
        assert endpoint_margin(low, endpoint) < 0
        assert endpoint_margin(high, endpoint) > 0
        for _ in range(120):
            middle = (low + high) / 2
            if endpoint_margin(middle, endpoint) > 0:
                high = middle
            else:
                low = middle
        assert high - low < Decimal("1e-40")
        threshold_brackets.append((low, high))

    def depth_profile(stop: int) -> dict[int, int]:
        profile: dict[int, int] = {}
        for _, _, _, _, depth, _ in increments[: stop + 1]:
            profile[depth] = profile.get(depth, 0) + 1
        return profile

    print("field discriminant / class-number test: PASS", FIELD_DISCRIMINANT)
    print("ramified ideals / last:", len(ramified_ideals), ramified_ideals[-1])
    print("Kummer columns / constraint rank / safe d:", len(columns), constraint_rank, SAFE_GENERATOR_RANK)
    print("useful ideals / last / rejected:", len(useful_ideals), useful_ideals[-1], len(rejected_ideals))
    print("generator / relations:", SAFE_GENERATOR_RANK, relation_bound)
    print("log bounded-inertia root discriminant:", log_root_discriminant)
    print("left:", left[1], left[2], depth_profile(left[1]))
    print("right:", right[1], right[2], depth_profile(right[1]))
    print("right / maximum fourth slopes:", right[3], maximum_fourth_slope)
    print("certified margins:", *margins)
    print("fixed-anchor threshold brackets:", *threshold_brackets)
    print("quadratic-1949 bounded-inertia F_2(n) << n^0.49371211: CERTIFIED")


if __name__ == "__main__":
    main()
