#!/usr/bin/env python3
"""Exact certificate for the Q(sqrt(1949)) CM/Eisenstein refinement."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

import verify_real_quadratic_1949_bounded_inertia as base


getcontext().prec = 90

ALPHA = Decimal(49_371_149) / Decimal(100_000_000)  # 0.49371149
W0 = Decimal("44698.7")
EPSILON = Decimal("1e-25")
C_UPPER_FRACTION = Fraction(71_603, 64_935)
C_UPPER = Decimal(C_UPPER_FRACTION.numerator) / Decimal(
    C_UPPER_FRACTION.denominator
)


def certify_constant() -> None:
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == C_UPPER_FRACTION


def main() -> None:
    certify_constant()
    primes = base.prime_sieve(200_000)
    assert all(
        base.FIELD_DISCRIMINANT % p
        for p in primes
        if p * p <= base.FIELD_DISCRIMINANT
    )
    assert base.FIELD_DISCRIMINANT % 8 == 5
    assert base.FIELD_DISCRIMINANT < 46 * 46
    assert [base.norm(x) for x in [(-151, -7), (43, 2), (-23, 1)]] == [
        -5,
        -13,
        19,
    ]
    ideals = base.prime_ideals(primes, 200_000)
    ramified_ideals = ideals[: base.RAMIFIED_IDEAL_COUNT]
    assert ramified_ideals[-1][:2] == (1_303, 1_303)

    # Reconstruct the principal generators for every ideal in T.
    prime_generator_cache: dict[int, tuple[int, int]] = {}
    ramified_generators: list[tuple[int, int]] = []
    for _, p, kind, root in ramified_ideals:
        if kind == "inert":
            generator = (p, 0)
        else:
            base_generator = prime_generator_cache.setdefault(
                p, base.generator_of_prime(p)
            )
            if kind == "ramified":
                generator = base_generator
            else:
                assert root is not None
                other_generator = base.conjugate(base_generator)
                generator = (
                    base_generator
                    if (base_generator[0] + base_generator[1] * root) % p == 0
                    else other_generator
                )
                assert (generator[0] + generator[1] * root) % p == 0
        ramified_generators.append(generator)

    fundamental_unit = (81_333, 3_770)
    assert base.norm(fundamental_unit) == -1
    assert base.negative_at_embedding(fundamental_unit, False) == 0
    assert base.negative_at_embedding(fundamental_unit, True) == 1

    # Reconstruct the exact two-sign/two-dyadic constraint row space.
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if base.norm((a, b)) % 2
    ]

    def multiply_mod_four(
        left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        product = base.multiply(left, right)
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
        return next(i for i, coset in enumerate(cosets) if residue in coset)

    identity_index = cosets.index(square_residues)
    nonidentity = [i for i in range(4) if i != identity_index]
    coset_bits = {identity_index: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    final_index = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert final_index == nonidentity[2]
    coset_bits[final_index] = 3
    for left in units_mod_four:
        for right in units_mod_four:
            assert coset_bits[coset_index(multiply_mod_four(left, right))] == (
                coset_bits[coset_index(left)] ^ coset_bits[coset_index(right)]
            )

    def constraint_column(element: tuple[int, int]) -> int:
        signs = base.negative_at_embedding(element, False)
        signs |= base.negative_at_embedding(element, True) << 1
        return signs | (coset_bits[coset_index(element)] << 2)

    kummer_generators = [(-1, 0), fundamental_unit] + ramified_generators
    columns = [constraint_column(element) for element in kummer_generators]
    constraint_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(columns)
        )
        for bit in range(4)
    ]
    constraint_rank = base.gf2_rank(constraint_rows)
    assert len(columns) == 231
    assert constraint_rank == 4
    assert len(columns) - constraint_rank == base.SAFE_GENERATOR_RANK == 227

    def frobenius_functional(
        ideal: tuple[int, int, str, int | None]
    ) -> int:
        norm_q, p, kind, root = ideal
        assert norm_q == p and kind in ("split", "ramified")
        if kind == "ramified":
            # At the unique base ideal above 1949, sqrt(1949)=0 and hence
            # omega=(1+sqrt(1949))/2 maps to 1/2.
            assert p == base.FIELD_DISCRIMINANT
            root = (p + 1) // 2
        assert root is not None
        functional = 0
        for index, (a, b) in enumerate(kummer_generators):
            residue = (a + b * root) % p
            assert residue
            if pow(residue, (p - 1) // 2, p) == p - 1:
                functional |= 1 << index
        return functional

    # An ideal of norm 1 mod 3 splits automatically in the Eisenstein CM
    # extension.  Norm 2 mod 3 requires exact relative residue degree two,
    # certified by a nonzero Frobenius functional on the Kummer kernel.
    useful_ideals: list[tuple[int, int, str, int | None]] = []
    rejected_ideals: list[tuple[int, int, str, int | None]] = []
    base_ideal_position: int | None = None
    for ideal in ideals[base.RAMIFIED_IDEAL_COUNT :]:
        norm_q, p, _, _ = ideal
        useful = True
        if norm_q % 3 == 2:
            functional = frobenius_functional(ideal)
            useful = (
                base.gf2_rank(constraint_rows + [functional]) > constraint_rank
            )
        else:
            assert norm_q % 3 == 1
        if useful:
            if p == base.FIELD_DISCRIMINANT:
                assert ideal == (1_949, 1_949, "ramified", None)
                base_ideal_position = len(useful_ideals)
            useful_ideals.append(ideal)
        else:
            rejected_ideals.append(ideal)
        if len(useful_ideals) == base.USEFUL_IDEAL_COUNT:
            break

    assert len(useful_ideals) == 12_425
    assert useful_ideals[-1][:2] == (136_693, 136_693)
    assert not rejected_ideals
    assert base_ideal_position == 76

    relation_bound = (
        base.SAFE_GENERATOR_RANK
        + base.BASE_RELATION_EXCESS
        + base.RAMIFIED_IDEAL_COUNT
        + base.USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 12_882
    assert 4 * relation_bound == base.SAFE_GENERATOR_RANK**2 - 1

    log_root_discriminant = Decimal(base.FIELD_DISCRIMINANT).ln() / 2
    for norm_q, _, _, _ in ramified_ideals:
        log_root_discriminant += Decimal(norm_q).ln() / 4

    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, (norm_q, _, _, _) in enumerate(useful_ideals):
        cost = Decimal(norm_q).ln() / 2
        previous_gain: Decimal | None = None
        for depth in range(1, 5):
            gain = base.local_increment(norm_q, depth) / 2
            if previous_gain is not None:
                assert previous_gain > gain
            previous_gain = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, norm_q, depth, ideal_index))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)

    seen = {index: 0 for index in range(base.USEFUL_IDEAL_COUNT)}
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
        correction = (Decimal(1) + exponent.exp() / C_UPPER).ln()
        return (
            C_UPPER.ln()
            + log_root_discriminant
            + (2 - 4 * alpha) * w
            + correction
        )

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert maximum_fourth_slope < right[3]
    margins = [
        left[0] - rhs(ALPHA, W0) - EPSILON,
        right[0] - rhs(ALPHA, 2 * W0) - EPSILON,
    ]
    assert min(margins) > Decimal("0.001")

    def endpoint_margin(alpha: Decimal, endpoint: int) -> Decimal:
        if endpoint == 1:
            return envelope(2 * alpha * W0)[0] - rhs(alpha, W0)
        assert endpoint == 2
        return envelope(4 * alpha * W0)[0] - rhs(alpha, 2 * W0)

    threshold_brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (1, 2):
        low = Decimal("0.49371147")
        high = Decimal("0.49371149")
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

    print("field / Kummer kernel:", base.FIELD_DISCRIMINANT, len(columns) - constraint_rank)
    print("safe CM constant:", C_UPPER)
    print("ramified ideals / last:", len(ramified_ideals), ramified_ideals[-1])
    print("useful / rejected / last:", len(useful_ideals), len(rejected_ideals), useful_ideals[-1])
    print("base ideal useful position:", base_ideal_position)
    print("generator / relations:", base.SAFE_GENERATOR_RANK, relation_bound)
    print("log real-tower root discriminant:", log_root_discriminant)
    print("left:", left[1], left[2], depth_profile(left[1]))
    print("right:", right[1], right[2], depth_profile(right[1]))
    print("right / maximum fourth slopes:", right[3], maximum_fourth_slope)
    print("certified margins:", *margins)
    print("fixed-anchor threshold brackets:", *threshold_brackets)
    print("Q(sqrt1949) CM/Eisenstein F_2(n) << n^0.49371149: CERTIFIED")


if __name__ == "__main__":
    main()
