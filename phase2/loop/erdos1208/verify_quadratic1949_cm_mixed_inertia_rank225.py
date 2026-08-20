#!/usr/bin/env python3
"""Certificate for the rank-225 CM record and mixed-inertia audit."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

import verify_real_quadratic_1949_bounded_inertia as base


getcontext().prec = 90

RAMIFIED_COUNT = 227
GENERATOR_RANK = 225
BASE_RELATIONS = 226
USEFUL_COUNT = 12_203
ALPHA = Decimal("0.493711480")
W0 = Decimal("43932.44")
EPSILON = Decimal("1e-25")
C_FRACTION = Fraction(71_603, 64_935)
C_UPPER = Decimal(C_FRACTION.numerator) / Decimal(C_FRACTION.denominator)


def certify_constant() -> None:
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper**2 > 3
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == C_FRACTION


def main() -> None:
    certify_constant()
    primes = base.prime_sieve(300_000)
    ideals = base.prime_ideals(primes, 300_000)
    ramified = ideals[:RAMIFIED_COUNT]
    assert ramified[-1] == (1_297, 1_297, "split", 84)

    # Principal T-generators.
    generator_cache: dict[int, tuple[int, int]] = {}
    ramified_generators: list[tuple[int, int]] = []
    for _, p, kind, root in ramified:
        if kind == "inert":
            generator = (p, 0)
        else:
            first = generator_cache.setdefault(p, base.generator_of_prime(p))
            if kind == "ramified":
                generator = first
            else:
                assert root is not None
                second = base.conjugate(first)
                generator = (
                    first if (first[0] + first[1] * root) % p == 0 else second
                )
                assert (generator[0] + generator[1] * root) % p == 0
        ramified_generators.append(generator)

    fundamental_unit = (81_333, 3_770)
    assert base.norm(fundamental_unit) == -1

    # The exact two-sign/two-dyadic constraint matrix.
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

    squares = frozenset(multiply_mod_four(u, u) for u in units_mod_four)
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units_mod_four:
        coset = frozenset(multiply_mod_four(unit, square) for square in squares)
        if coset not in cosets:
            cosets.append(coset)
    assert len(units_mod_four) == 12 and len(squares) == 3 and len(cosets) == 4

    def coset_index(element: tuple[int, int]) -> int:
        residue = element[0] % 4, element[1] % 4
        return next(i for i, coset in enumerate(cosets) if residue in coset)

    identity = cosets.index(squares)
    nonidentity = [i for i in range(4) if i != identity]
    bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    last = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert last == nonidentity[2]
    bits[last] = 3
    for left in units_mod_four:
        for right in units_mod_four:
            assert bits[coset_index(multiply_mod_four(left, right))] == (
                bits[coset_index(left)] ^ bits[coset_index(right)]
            )

    def constraint_column(element: tuple[int, int]) -> int:
        signs = base.negative_at_embedding(element, False)
        signs |= base.negative_at_embedding(element, True) << 1
        return signs | (bits[coset_index(element)] << 2)

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
    assert len(columns) == 229
    assert constraint_rank == 4
    assert len(columns) - constraint_rank == GENERATOR_RANK

    def frobenius_functional(
        ideal: tuple[int, int, str, int | None]
    ) -> int:
        norm_q, p, kind, root = ideal
        assert norm_q == p and kind in ("split", "ramified")
        if kind == "ramified":
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

    # We retain extra candidates for the mixed-cap dual comparison.
    useful: list[tuple[int, int, str, int | None]] = []
    rejected: list[tuple[int, int, str, int | None]] = []
    base_ideal_position: int | None = None
    needed_candidates = USEFUL_COUNT + RAMIFIED_COUNT
    for ideal in ideals[RAMIFIED_COUNT:]:
        norm_q, p, _, _ = ideal
        eligible = True
        if norm_q % 3 == 2:
            functional = frobenius_functional(ideal)
            eligible = base.gf2_rank(constraint_rows + [functional]) > 4
        else:
            assert norm_q % 3 == 1
        if eligible:
            if p == base.FIELD_DISCRIMINANT:
                assert ideal == (1_949, 1_949, "ramified", None)
                base_ideal_position = len(useful)
            useful.append(ideal)
        else:
            rejected.append(ideal)
        if len(useful) == needed_candidates:
            break
    assert not rejected
    assert base_ideal_position == 78
    assert useful[USEFUL_COUNT - 1][:2] == (134_129, 134_129)

    # Exact mixed-inertia GS optimization.  If s2 inertia squares and s4
    # inertia fourth powers are imposed, then
    # P(x)=1-225x+(226+s2+N)x^2+s4*x^4.
    # Every s4 <= 227-s2 permits exactly N=12430-s2 useful squares.
    maximum_quadratic_only_caps = 12_430
    x_gs = Fraction(2, GENERATOR_RANK)
    for square_count in range(RAMIFIED_COUNT + 1):
        for fourth_count in (0, RAMIFIED_COUNT - square_count):
            useful_count = maximum_quadratic_only_caps - square_count
            quadratic_count = BASE_RELATIONS + square_count + useful_count
            gs_value = (
                1
                - GENERATOR_RANK * x_gs
                + quadratic_count * x_gs**2
                + fourth_count * x_gs**4
            )
            assert gs_value < 0
            # One more useful square makes even the quadratic truncation
            # positive for every real x: its discriminant is -3.
            next_quadratic_count = quadratic_count + 1
            assert GENERATOR_RANK**2 - 4 * next_quadratic_count == -3

    assert maximum_quadratic_only_caps - RAMIFIED_COUNT == USEFUL_COUNT
    # Fourth-power caps are therefore free at the integer GS boundary, so
    # an uncapped inertia ideal is strictly dominated by fourth-capping it.

    relation_bound = BASE_RELATIONS + RAMIFIED_COUNT + USEFUL_COUNT
    assert relation_bound == 12_656
    assert 4 * relation_bound == GENERATOR_RANK**2 - 1

    log_root_discriminant = Decimal(base.FIELD_DISCRIMINANT).ln() / 2
    for norm_q, _, _, _ in ramified:
        log_root_discriminant += Decimal(norm_q).ln() / 4

    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, (norm_q, _, _, _) in enumerate(useful[:USEFUL_COUNT]):
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        for depth in range(1, 5):
            gain = base.local_increment(norm_q, depth) / 2
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if depth <= 3:
                increments.append((slope, cost, gain, norm_q, depth, ideal_index))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)

    seen = {index: 0 for index in range(USEFUL_COUNT)}
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
        raise AssertionError("target exceeds frontier")

    def rhs(alpha: Decimal, w: Decimal) -> Decimal:
        exponent = 2 * (2 * alpha - 1) * w - log_root_discriminant
        correction = (Decimal(1) + exponent.exp() / C_UPPER).ln()
        return C_UPPER.ln() + log_root_discriminant + (2 - 4 * alpha) * w + correction

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert maximum_fourth_slope < right[3]
    margins = [
        left[0] - rhs(ALPHA, W0) - EPSILON,
        right[0] - rhs(ALPHA, 2 * W0) - EPSILON,
    ]
    assert min(margins) > Decimal("0.0001")

    # At each certified endpoint, an exact fractional-knapsack dual shows
    # that changing any number of the smallest ramified square caps to
    # fourth-power caps lowers the margin.  The j-th change adds the j-th
    # post-frontier useful ideal and costs log(N p_j)/8 in log RD.
    def active_value(norm_q: int, lam: Decimal) -> tuple[Decimal, int]:
        cost = Decimal(norm_q).ln() / 2
        value = Decimal(0)
        depth = 1
        while True:
            gain = base.local_increment(norm_q, depth) / 2
            excess = gain - lam * cost
            if excess <= 0:
                return value, depth - 1
            value += excess
            depth += 1
            assert depth < 100

    dual_gaps: list[Decimal] = []
    assignment_data: list[tuple[Decimal, Decimal]] = []
    for scale, endpoint in ((Decimal(1), left), (Decimal(2), right)):
        w = scale * W0
        lam = endpoint[3]
        correction_exponent = (
            2 * (2 * ALPHA - 1) * w - log_root_discriminant
        )
        assert correction_exponent < Decimal(-10)
        # Use a deliberately weak rigorous lower bound; direct 90-digit
        # Decimal evaluation rounds the true derivative to one.
        rho = Decimal(1) / (
            Decimal(1) + Decimal(-10).exp() / C_UPPER
        )

        minimum_gap: Decimal | None = None
        for j, ramified_ideal in enumerate(ramified):
            added_norm = useful[USEFUL_COUNT + j][0]
            value, _ = active_value(added_norm, lam)
            penalty = rho * Decimal(ramified_ideal[0]).ln() / 8
            gap = penalty - value
            minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
        assert minimum_gap is not None and minimum_gap > Decimal("0.13")
        dual_gaps.append(minimum_gap)

        # Prime-ideal prefix dominance hypotheses.  Here the ramification
        # weight is log(Np)/4 and useful cost is log(Nq)/2.
        first_useful_norm = useful[0][0]
        tail = Decimal(1) / Decimal(first_useful_norm) ** 2
        tail /= (Decimal(1) - Decimal(1) / Decimal(first_useful_norm) ** 2) ** 2
        assert rho > Decimal(1) / Decimal(5).ln()
        assert lam > tail
        assignment_data.append((lam, rho))

    def endpoint_margin(alpha: Decimal, endpoint: int) -> Decimal:
        if endpoint == 1:
            return envelope(2 * alpha * W0)[0] - rhs(alpha, W0)
        assert endpoint == 2
        return envelope(4 * alpha * W0)[0] - rhs(alpha, 2 * W0)

    brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (1, 2):
        low = Decimal("0.49371147")
        high = ALPHA
        assert endpoint_margin(low, endpoint) < 0
        assert endpoint_margin(high, endpoint) > 0
        for _ in range(120):
            middle = (low + high) / 2
            if endpoint_margin(middle, endpoint) > 0:
                high = middle
            else:
                low = middle
        brackets.append((low, high))

    print("Kummer columns / constraints / rank:", len(columns), constraint_rank, GENERATOR_RANK)
    print("ramified / useful / rejected:", len(ramified), USEFUL_COUNT, len(rejected))
    print("last ramified / useful:", ramified[-1], useful[USEFUL_COUNT - 1])
    print("base ideal useful position:", base_ideal_position)
    print("mixed GS: N=12430-s2 for every 0<=s4<=227-s2: CERTIFIED")
    print("relation count / log RD:", relation_bound, log_root_discriminant)
    print("left / right margins:", *margins)
    print("right / max fourth slopes:", right[3], maximum_fourth_slope)
    print("mixed-cap endpoint dual gaps:", *dual_gaps)
    print("assignment lambda/rho:", *assignment_data)
    print("fixed-anchor threshold brackets:", *brackets)
    print("F_2(n) << n^0.493711480: CERTIFIED")


if __name__ == "__main__":
    main()
