#!/usr/bin/env python3
"""Certificate for the CM/Eisenstein Q(sqrt(1949)) construction."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

from verify_real_quadratic_1949_bounded_inertia import (
    BASE_RELATION_EXCESS,
    FIELD_DISCRIMINANT,
    OMEGA_CONSTANT,
    conjugate,
    generator_of_prime,
    gf2_rank,
    local_increment,
    multiply,
    negative_at_embedding,
    norm,
    prime_ideals,
    prime_sieve,
)


getcontext().prec = 90

RAMIFIED_IDEAL_COUNT = 227
SAFE_GENERATOR_RANK = 225
USEFUL_IDEAL_COUNT = 12_203
ALPHA = Decimal(49_371_148) / Decimal(100_000_000)  # 0.49371148
W0 = Decimal("43932.44")
NUMERICAL_ALLOWANCE = Decimal("1e-25")

# sqrt(3)<1351/780 and pi>333/106 imply
# 2sqrt(3)/pi < 71603/64935.
PACKING_CONSTANT_FRACTION = Fraction(71_603, 64_935)
PACKING_CONSTANT_UPPER = Decimal(PACKING_CONSTANT_FRACTION.numerator) / Decimal(
    PACKING_CONSTANT_FRACTION.denominator
)


def main() -> None:
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert (
        2 * sqrt_three_upper / Fraction(333, 106)
        == PACKING_CONSTANT_FRACTION
    )

    primes = prime_sieve(200_000)
    ideals = prime_ideals(primes, 200_000)
    ramified_ideals = ideals[:RAMIFIED_IDEAL_COUNT]
    assert ramified_ideals[-1][:2] == (1_297, 1_297)

    # Repeat the base arithmetic rather than treating the Gaussian
    # certificate's output as an assumption.
    assert all(FIELD_DISCRIMINANT % p for p in primes if p * p <= FIELD_DISCRIMINANT)
    assert 1 + 4 * OMEGA_CONSTANT == FIELD_DISCRIMINANT
    assert FIELD_DISCRIMINANT % 8 == 5
    assert FIELD_DISCRIMINANT < 46 * 46
    assert [norm(element) for element in [(-151, -7), (43, 2), (-23, 1)]] == [
        -5,
        -13,
        19,
    ]
    fundamental_unit = (81_333, 3_770)
    assert norm(fundamental_unit) == -1
    assert negative_at_embedding(fundamental_unit, False) == 0
    assert negative_at_embedding(fundamental_unit, True) == 1

    prime_generator_cache: dict[int, tuple[int, int]] = {}
    ramified_generators: list[tuple[int, int]] = []
    for _, p, kind, root in ramified_ideals:
        if kind == "inert":
            generator = (p, 0)
        else:
            if p not in prime_generator_cache:
                prime_generator_cache[p] = generator_of_prime(p)
            base_generator = prime_generator_cache[p]
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
    assert len(units_mod_four) == 12 and len(square_residues) == 3
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
    assert len(kummer_generators) == 229
    assert constraint_rank == 4
    assert len(kummer_generators) - constraint_rank == SAFE_GENERATOR_RANK

    # Eisenstein criterion: Q=1 mod 3 is automatic; Q=2 mod 3 needs a
    # nonzero Frattini Frobenius so the square cap forces exact degree two.
    useful_ideals: list[tuple[int, int, str, int | None]] = []
    rejected_ideals: list[tuple[int, int, str, int | None]] = []
    for ideal in ideals[RAMIFIED_IDEAL_COUNT:]:
        norm_q, p, kind, root = ideal
        if p == 3:
            continue
        useful = True
        if norm_q % 3 == 2:
            assert norm_q == p
            if kind == "ramified":
                residue_root = (p + 1) // 2
            else:
                assert kind == "split" and root is not None
                residue_root = root
            functional = 0
            for index, (a, b) in enumerate(kummer_generators):
                residue = (a + b * residue_root) % p
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
    assert useful_ideals[-1][:2] == (134_129, 134_129)
    assert not rejected_ideals
    base_ramified_index = next(
        index
        for index, (_, p, kind, _) in enumerate(useful_ideals)
        if p == FIELD_DISCRIMINANT and kind == "ramified"
    )
    assert base_ramified_index == 78

    relation_bound = (
        SAFE_GENERATOR_RANK
        + BASE_RELATION_EXCESS
        + RAMIFIED_IDEAL_COUNT
        + USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 12_656
    assert 4 * relation_bound == SAFE_GENERATOR_RANK**2 - 1

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
    assert min(margins) > Decimal("0.0001")

    print("safe CM constant:", PACKING_CONSTANT_UPPER)
    print("ramified ideals / last:", len(ramified_ideals), ramified_ideals[-1])
    print("Kummer columns / constraints / d:", len(columns), constraint_rank, SAFE_GENERATOR_RANK)
    print("useful / rejected / last:", len(useful_ideals), len(rejected_ideals), useful_ideals[-1])
    print("base-ramified useful position:", base_ramified_index)
    print("generator / relations:", SAFE_GENERATOR_RANK, relation_bound)
    print("log real-tower root discriminant:", log_root_discriminant)
    print("left / right:", left, right)
    print("right / maximum fourth slopes:", right[3], maximum_fourth_slope)
    print("margins:", *margins)
    print("CM quadratic-1949 F_2(n) << n^0.49371148: CERTIFIED")


if __name__ == "__main__":
    main()
