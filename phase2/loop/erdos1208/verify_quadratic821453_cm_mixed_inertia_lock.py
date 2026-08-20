#!/usr/bin/env python3
"""Lock the D=821453 fixed prefix against mixed tame-inertia caps."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction

import verify_hostile_quadratic821453_cm as base
import verify_quadratic43133_cm_mixed_assignment_lock as engine


getcontext().prec = 100

RAMIFIED_COUNT = 219
GENERATOR_RANK = 217
BASE_RELATIONS = 218
USEFUL_COUNT = 11_335
MAXIMUM_QUADRATIC_RELATIONS = 11_772


def configure_engine() -> None:
    """Point the field-independent weighted-GS/endpoint engine at D=821453."""
    base.configure_elementary_module()
    base.FIELD_DISCRIMINANT = base.D
    base.C_UPPER = Decimal(base.SAFE_C.numerator) / Decimal(base.SAFE_C.denominator)
    base.local_increment = base.local_gain
    base.prime_sieve = base.elementary.prime_sieve
    base.prime_ideals = base.elementary.prime_ideals
    engine.base = base
    engine.RAMIFIED_COUNT = RAMIFIED_COUNT
    engine.GENERATOR_RANK = GENERATOR_RANK
    engine.BASE_RELATIONS = BASE_RELATIONS
    engine.USEFUL_COUNT = USEFUL_COUNT
    engine.MAXIMUM_QUADRATIC_RELATIONS = MAXIMUM_QUADRATIC_RELATIONS
    engine.EXPECTED_RANK_USEFUL_COUNTS = (11_335, 11_442, 11_551)


def exact_ray_colors() -> list[tuple[int, int, int | None, int]]:
    """Quotient exact ray columns by the two-dimensional unit span."""
    units, raw_ideals = base.exact_ray_rows()
    assert base.gf2_rank(units) == 2
    unit_span = [0, units[0], units[1], units[0] ^ units[1]]
    canonical = [
        (norm_q, p, root, min(vector ^ unit for unit in unit_span))
        for norm_q, p, root, vector in raw_ideals
    ]
    # Here the four quotient representatives are 0,2,4,6.  Division by two
    # is an F_2-linear identification with the standard two-bit quotient.
    assert {row[3] for row in canonical} == {0, 2, 4, 6}
    colored = [
        (norm_q, p, root, quotient // 2)
        for norm_q, p, root, quotient in canonical
    ]
    colored.sort()
    assert {row[3] for row in colored} == {0, 1, 2, 3}
    return colored


def exact_weighted_gs_check() -> None:
    """Check every square/fourth/uncapped count with exact fractions."""
    assert MAXIMUM_QUADRATIC_RELATIONS == (GENERATOR_RANK**2 - 1) // 4
    assert 4 * MAXIMUM_QUADRATIC_RELATIONS == GENERATOR_RANK**2 - 1
    z = Fraction(2, GENERATOR_RANK)
    for square_count in range(RAMIFIED_COUNT + 1):
        useful_count = (
            MAXIMUM_QUADRATIC_RELATIONS - BASE_RELATIONS - square_count
        )
        assert useful_count == 11_554 - square_count
        quadratic_count = BASE_RELATIONS + square_count + useful_count
        assert quadratic_count == MAXIMUM_QUADRATIC_RELATIONS
        for fourth_count in range(RAMIFIED_COUNT - square_count + 1):
            polynomial = (
                1
                - GENERATOR_RANK * z
                + quadratic_count * z**2
                + fourth_count * z**4
            )
            assert polynomial < 0
        assert GENERATOR_RANK**2 - 4 * (quadratic_count + 1) == -3
    assert 16 * RAMIFIED_COUNT < GENERATOR_RANK**2
    assert 11_554 - RAMIFIED_COUNT == USEFUL_COUNT

    # Field-independent all-depth useful-role monotonicity for Q>=9.
    useful_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_upper = Fraction(729, 6_400)
    assert useful_lower > useful_upper


def main() -> None:
    configure_engine()
    # Rerun the independent BNF/Kummer/usefulness/endpoint and all-square
    # rank-aware assignment audit before adding the mixed-cap layer.
    base.main()
    exact_weighted_gs_check()

    primes = base.prime_sieve(300_000)
    ideals = base.prime_ideals(primes, 300_000)
    ramified = ideals[:RAMIFIED_COUNT]
    candidates = ideals[
        RAMIFIED_COUNT : RAMIFIED_COUNT + USEFUL_COUNT + RAMIFIED_COUNT
    ]
    assert ramified[-1] == (1_213, 1_213, "split", 395)
    assert candidates[0] == (1_213, 1_213, "split", 819)
    assert candidates[USEFUL_COUNT - 1] == (
        122_527,
        122_527,
        "split",
        3_683,
    )
    assert candidates[-1] == (125_669, 125_669, "split", 65_745)

    gaps, parameters, maximum_fourth = engine.exact_endpoint_dual(
        ramified, candidates
    )
    engine.exact_ray_colors = exact_ray_colors
    rank_diagnostics, rank_metadata, joint_all_anchor_slacks = (
        engine.rank_aware_all_assignment_lock(ideals)
    )
    diagnostics = rank_diagnostics["rank2"]
    all_anchor_slacks = engine.exact_no_reoptimized_mixed_improvement(
        ramified, candidates, diagnostics
    )
    assert maximum_fourth == Decimal(str(maximum_fourth))
    assert float(maximum_fourth) < diagnostics[0][2]

    assert abs(diagnostics[0][0] - 0.493693124444) < 2e-12
    assert abs(diagnostics[1][0] - 0.493694341339) < 2e-12
    assert abs(diagnostics[-1][0] - 0.494321568607) < 2e-12
    assert all(
        diagnostics[j][0] > diagnostics[j - 1][0]
        for j in range(1, len(diagnostics))
    )

    representative = [0, 1, 2, 10, 50, 100, 150, 200, 219]
    print("mixed GS N=11554-s2 for every s2,s4: CERTIFIED")
    print("fixed-prefix endpoint-dual gaps:", *gaps)
    print("assignment lambda/rho bounds:", *parameters)
    print("rank-aware ray metadata:", rank_metadata)
    print(
        "rank-aware all-square diagnostics:",
        {name: values[0] for name, values in rank_diagnostics.items()},
    )
    print(
        "representative mixed thresholds:",
        [(j, diagnostics[j][0], diagnostics[j][1]) for j in representative],
    )
    print("all-anchor mixed exclusion slacks:", *all_anchor_slacks)
    print("joint rank/mixed exclusion slacks:", *joint_all_anchor_slacks)
    print("maximum fourth slope:", maximum_fourth)
    print("D=821453 fixed-prefix mixed-inertia lock: CERTIFIED")


if __name__ == "__main__":
    main()
