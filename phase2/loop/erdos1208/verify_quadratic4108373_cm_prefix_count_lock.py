#!/usr/bin/env python3
"""Exact wrapper for the D=4108373 broad norm-prefix count lock.

The C++ companion exhausts T=50,...,600 under the favorable all-useful
relaxation.  This wrapper certifies the class/ray rank, weighted GS
bookkeeping, rational packing constants, and the closest excluded and retained
cells with high-precision Decimal arithmetic.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic821453_cm as base  # noqa: E402
import verify_quadratic4108373_cm_structural_lock as structural  # noqa: E402


D = 4_108_373
T_MIN = 50
T_MAX = 600
WINNER = 217
RUNNER_UP = 215
ALPHA_LOCK = Decimal("0.49368647")
C_LOWER = Fraction(11_978, 10_863)
C_UPPER = Fraction(71_603, 64_935)


def configure() -> None:
    base.D = D
    base.C = (D - 1) // 4
    base.T_COUNT = WINNER
    base.GENERATOR_RANK = WINNER - 2
    base.USEFUL_COUNT = 11_123
    base.ALPHA = ALPHA_LOCK
    base.SAFE_C = C_UPPER
    base.elementary.FIELD_DISCRIMINANT = D
    base.elementary.OMEGA_CONSTANT = (D - 1) // 4
    base.elementary.RAMIFIED_IDEAL_COUNT = WINNER
    structural.configure()


def evaluate(log_rd, frontier, packing_constant: Fraction, anchor: Decimal):
    constant = Decimal(packing_constant.numerator) / Decimal(
        packing_constant.denominator
    )
    output = []
    for endpoint in (1, 2):
        scale = Decimal(endpoint)
        w = scale * anchor
        value, index, fraction, slope = base.fast_envelope(
            frontier, 2 * ALPHA_LOCK * w
        )
        exponent = 2 * (2 * ALPHA_LOCK - 1) * w - log_rd
        ratio = exponent.exp() / constant
        rhs = (
            constant.ln()
            + log_rd
            + (2 - 4 * ALPHA_LOCK) * w
            + (1 + ratio).ln()
        )
        margin = value - rhs
        derivative = (
            2 * ALPHA_LOCK * scale * slope
            - (2 - 4 * ALPHA_LOCK) * scale
            - 2
            * (2 * ALPHA_LOCK - 1)
            * scale
            * ratio
            / (1 + ratio)
        )
        output.append((margin, derivative, slope, index, fraction))
    return output


def equal_endpoint_certificate(ideals, count: int, constant: Fraction):
    generator_rank = count - 2
    useful_count = (
        (generator_rank * generator_rank - 1) // 4
        - (generator_rank + 1)
        - count
    )
    ramified = ideals[:count]
    useful = ideals[count : count + useful_count]
    log_rd, frontier, maximum_omitted = base.prepare_endpoint_data(
        ramified, useful
    )

    low = Decimal("30000")
    high = Decimal("50000")

    def difference(anchor: Decimal) -> Decimal:
        records = evaluate(log_rd, frontier, constant, anchor)
        return records[0][0] - records[1][0]

    low_difference = difference(low)
    high_difference = difference(high)
    assert low_difference * high_difference < 0
    for _ in range(110):
        middle = (low + high) / 2
        middle_difference = difference(middle)
        if low_difference * middle_difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = middle_difference
    anchor = (low + high) / 2
    records = evaluate(log_rd, frontier, constant, anchor)
    assert abs(records[0][0] - records[1][0]) < Decimal("1e-28")
    assert records[0][1] > Decimal("0.004")
    assert records[1][1] < Decimal("-0.012")
    assert maximum_omitted < min(record[2] for record in records)
    return generator_rank, useful_count, anchor, records


def exact_rank_and_gs_audit() -> tuple[int, int]:
    units, reference, raw = structural.exact_colored_ideals()
    assert reference == (2, 11, 4, 12)
    assert len(raw) >= T_MAX

    # The first nonprincipal ideal occurs at index two, so Cl_S[2] is killed
    # throughout the audited interval.  The columns consist of the two global
    # units and one S-unit column for each selected prime ideal (the reference
    # column is the generator of R_0^2).  Full rank is reached by T=6 and is
    # then monotone.  We nevertheless check every audited prefix explicitly.
    ranks = [
        base.gf2_rank(units + [row[4] for row in raw[:count]])
        for count in range(T_MIN, T_MAX + 1)
    ]
    assert set(ranks) == {4}
    assert base.gf2_rank(units + [row[4] for row in raw[:5]]) < 4
    assert base.gf2_rank(units + [row[4] for row in raw[:6]]) == 4

    for count in range(T_MIN, T_MAX + 1):
        generator_rank = count - 2
        maximum_relations = (generator_rank * generator_rank - 1) // 4
        useful_count = maximum_relations - (generator_rank + 1) - count
        assert useful_count > 0
        point = Fraction(2, generator_rank)
        assert (
            1
            - generator_rank * point
            + maximum_relations * point * point
        ) < 0
    return min(ranks), max(ranks)


def packing_constant_audit() -> None:
    sqrt_three_lower = Fraction(265, 153)
    assert sqrt_three_lower * sqrt_three_lower < 3
    fifth = Fraction(1, 5)
    atan_fifth_upper = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(5)
    )
    q = Fraction(1, 239)
    pi_upper = 16 * atan_fifth_upper - 4 * (q - q**3 / 3)
    assert pi_upper < Fraction(355, 113)
    assert 2 * sqrt_three_lower / Fraction(355, 113) == C_LOWER

    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    atan_fifth_lower = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * q
    assert pi_lower > Fraction(333, 106)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == C_UPPER


def run_broad_companion() -> str:
    source = Path(__file__).with_suffix(".cpp")
    compiler = shutil.which("c++")
    if compiler is None:
        raise RuntimeError("a C++17 compiler is required")
    with tempfile.TemporaryDirectory(prefix="verify_4108373_prefix_") as folder:
        executable = Path(folder) / "verify"
        subprocess.check_call(
            [
                compiler,
                "-std=c++17",
                "-O3",
                "-Wall",
                "-Wextra",
                "-pedantic",
                str(source),
                "-o",
                str(executable),
            ]
        )
        output = subprocess.check_output([str(executable)], text=True)
    assert "range/count: 50..600 / 551" in output
    assert "all-square/all-useful broad prefix count: UNIQUE T=217" in output
    assert "2 T=215 d=213 N=10913" in output
    return output


def main() -> None:
    getcontext().prec = 100
    configure()
    packing_constant_audit()
    ray_range = exact_rank_and_gs_audit()
    broad_output = run_broad_companion()

    primes = base.elementary.prime_sieve(180_000)
    ideals = base.elementary.prime_ideals(primes, 180_000)
    runner = equal_endpoint_certificate(ideals, RUNNER_UP, C_LOWER)
    winner = equal_endpoint_certificate(ideals, WINNER, C_UPPER)
    assert runner[0:2] == (213, 10_913)
    assert winner[0:2] == (215, 11_123)
    assert max(record[0] for record in runner[3]) < Decimal("-0.003")
    assert min(record[0] for record in winner[3]) > Decimal("0.0015")

    print(broad_output, end="")
    print("exact ray ranks T=50..600:", ray_range)
    print("runner T=215 / d / N / anchor:", *runner[:3])
    print("runner favorable-lower-C records:", runner[3])
    print("winner T=217 / d / N / anchor:", *winner[:3])
    print("winner adverse-upper-C records:", winner[3])
    print("D=4108373 broad prefix-count lock: CERTIFIED")


if __name__ == "__main__":
    main()
