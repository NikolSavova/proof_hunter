#!/usr/bin/env python3
"""Exact-leader wrapper for the D=821453 broad prefix-count lock.

The companion C++ verifier exhausts all T=50,...,600 with a favorable
all-useful relaxation.  Here PARI/GP certifies the ray rank used in that
enumeration, and Decimal arithmetic recertifies the unique winner and the
closest excluded count using rational one-sided packing constants.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_hostile_quadratic821453_cm as base  # noqa: E402


T_MIN = 50
T_MAX = 600
WINNER = 219
RUNNER_UP = 217
ALPHA_LOCK = Decimal("0.4936931245")
C_LOWER = Fraction(11_978, 10_863)
C_UPPER = base.SAFE_C


def evaluate(
    log_rd: Decimal,
    frontier,
    packing_constant: Fraction,
    anchor: Decimal,
):
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
    for _ in range(100):
        middle = (low + high) / 2
        middle_difference = difference(middle)
        if low_difference * middle_difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = middle_difference
    anchor = (low + high) / 2
    records = evaluate(log_rd, frontier, constant, anchor)
    assert abs(records[0][0] - records[1][0]) < Decimal("1e-25")
    assert records[0][1] > Decimal("0.004")
    assert records[1][1] < Decimal("-0.012")
    assert maximum_omitted < min(record[2] for record in records)
    return generator_rank, useful_count, anchor, records


def exact_rank_and_gs_audit(ideals) -> None:
    unit_rows, colored = base.exact_ray_rows()
    assert len(colored) >= T_MAX
    assert [
        (ideal[0], ideal[1], ideal[3]) for ideal in ideals[:T_MAX]
    ] == [row[:3] for row in colored[:T_MAX]]
    ranks = [
        base.gf2_rank(unit_rows + [row[3] for row in colored[:count]])
        for count in range(T_MIN, T_MAX + 1)
    ]
    assert set(ranks) == {4}

    # All-square weighted GS at y=2/d, with the relation budget saturated.
    for count in range(T_MIN, T_MAX + 1):
        generator_rank = count - 2
        maximum_relations = (generator_rank * generator_rank - 1) // 4
        useful_count = (
            maximum_relations - (generator_rank + 1) - count
        )
        assert useful_count > 0
        point = Fraction(2, generator_rank)
        polynomial = (
            1
            - generator_rank * point
            + maximum_relations * point * point
        )
        assert polynomial < 0


def packing_constant_audit() -> None:
    # Lower bound used to favor every excluded competitor.
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

    # Upper bound used to retain the actual T=219 certificate.
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
    with tempfile.TemporaryDirectory(prefix="verify_821453_prefix_") as folder:
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
    assert "all-square/all-useful broad prefix count: UNIQUE T=219" in output
    return output


def main() -> None:
    getcontext().prec = 90
    base.configure_elementary_module()
    packing_constant_audit()

    primes = base.elementary.prime_sieve(250_000)
    ideals = base.elementary.prime_ideals(primes, 250_000)
    exact_rank_and_gs_audit(ideals)
    broad_output = run_broad_companion()

    runner = equal_endpoint_certificate(ideals, RUNNER_UP, C_LOWER)
    winner = equal_endpoint_certificate(ideals, WINNER, C_UPPER)
    assert runner[0:2] == (215, 11_123)
    assert winner[0:2] == (217, 11_335)
    assert max(record[0] for record in runner[3]) < Decimal("-0.0012")
    assert min(record[0] for record in winner[3]) > Decimal("0.000005")

    print(broad_output, end="")
    print("exact ray ranks T=50..600: all 4")
    print("runner T=217 / d / N / anchor:", *runner[:3])
    print("runner favorable-lower-C records:", runner[3])
    print("winner T=219 / d / N / anchor:", *winner[:3])
    print("winner adverse-upper-C records:", winner[3])
    print("D=821453 broad prefix-count lock: CERTIFIED")


if __name__ == "__main__":
    main()
