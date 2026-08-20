#!/usr/bin/env python3
"""Mixed-inertia and arbitrary-assignment lock for D=821453."""

from __future__ import annotations

import bisect
from decimal import Decimal, getcontext
from fractions import Fraction
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_hostile_quadratic821453_cm as base  # noqa: E402


T_COUNT = 219
ALPHA = Decimal("0.49369313")
C_LOWER_FRACTION = Fraction(11_978, 10_863)


_LOCAL_CACHE: dict[
    int, tuple[list[tuple[Decimal, Decimal, Decimal, int, int, int]], Decimal]
] = {}


def local_items(norm_q: int, ideal_index: int):
    if norm_q not in _LOCAL_CACHE:
        cost = Decimal(norm_q).ln() / 2
        raw: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
        previous: Decimal | None = None
        for depth in range(1, 100):
            gain = base.local_gain(norm_q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if slope < Decimal("0.01"):
                _LOCAL_CACHE[norm_q] = (raw, slope)
                break
            raw.append((slope, cost, gain, norm_q, depth, -1))
        else:
            raise AssertionError("local depth did not terminate")
    raw, omitted = _LOCAL_CACHE[norm_q]
    return [row[:-1] + (ideal_index,) for row in raw], omitted


def frontier(candidates: list[tuple[int, int, str, int | None]]):
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_omitted = Decimal(0)
    for index, ideal in enumerate(candidates):
        items, omitted = local_items(ideal[0], index)
        increments.extend(items)
        maximum_omitted = max(maximum_omitted, omitted)
    increments.sort(reverse=True)
    costs = [Decimal(0)]
    gains = [Decimal(0)]
    for _, cost, gain, _, _, _ in increments:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
    return increments, costs, gains, maximum_omitted


def endpoint_exclusion(
    selected: list[tuple[int, int, str, int | None]],
    fourth_count: int,
    generator_rank: int,
    candidates: list[tuple[int, int, str, int | None]],
):
    constant = Decimal(C_LOWER_FRACTION.numerator) / Decimal(
        C_LOWER_FRACTION.denominator
    )
    maximum_quadratic = (generator_rank * generator_rank - 1) // 4
    useful_count = (
        maximum_quadratic - (generator_rank + 1) - T_COUNT + fourth_count
    )
    useful = candidates[:useful_count]
    increments, costs, gains, maximum_omitted = frontier(useful)
    log_rd = Decimal(base.D).ln() / 2
    for index, ideal in enumerate(selected):
        exponent = Decimal(3) / 8 if index < fourth_count else Decimal(1) / 4
        log_rd += exponent * Decimal(ideal[0]).ln()

    def envelope(target: Decimal):
        index = bisect.bisect_left(costs, target)
        assert 0 < index < len(costs)
        fraction = (target - costs[index - 1]) / (
            costs[index] - costs[index - 1]
        )
        item = increments[index - 1]
        return gains[index - 1] + fraction * item[2], item[0]

    def records(anchor: Decimal):
        output = []
        for endpoint in (1, 2):
            scale = Decimal(endpoint)
            w = scale * anchor
            value, slope = envelope(2 * ALPHA * w)
            exponent = 2 * (2 * ALPHA - 1) * w - log_rd
            ratio = exponent.exp() / constant
            rhs = (
                constant.ln()
                + log_rd
                + (2 - 4 * ALPHA) * w
                + (1 + ratio).ln()
            )
            margin = value - rhs
            derivative = (
                2 * ALPHA * scale * slope
                - (2 - 4 * ALPHA) * scale
                - 2 * (2 * ALPHA - 1) * scale * ratio / (1 + ratio)
            )
            rho = Decimal(1) / (1 + ratio)
            output.append((margin, derivative, slope, rho))
        return output

    low, high = Decimal("25000"), Decimal("80000")
    low_difference = records(low)[0][0] - records(low)[1][0]
    high_difference = records(high)[0][0] - records(high)[1][0]
    assert low_difference * high_difference < 0
    for _ in range(75):
        middle = (low + high) / 2
        difference = records(middle)[0][0] - records(middle)[1][0]
        if low_difference * difference <= 0:
            high = middle
        else:
            low, low_difference = middle, difference
    anchor = (low + high) / 2
    data = records(anchor)
    assert maximum_omitted < min(row[2] for row in data)
    assert data[0][0] < Decimal("-0.01")
    assert data[1][0] < Decimal("-0.01")
    assert data[0][1] > Decimal("0.001")
    assert data[1][1] < Decimal("-0.001")
    assert all(row[3] > Decimal(1) / Decimal(9).ln() for row in data)
    return max(data[0][0], data[1][0]), anchor, data, log_rd


def exact_weighted_gs() -> None:
    for generator_rank in (217, 218, 219):
        maximum_quadratic = (generator_rank * generator_rank - 1) // 4
        point = Fraction(2, generator_rank)
        for fourth_count in range(T_COUNT + 1):
            polynomial = (
                1
                - generator_rank * point
                + maximum_quadratic * point**2
                + fourth_count * point**4
            )
            assert polynomial < 0
        # One extra quadratic relator makes the quadratic discriminant
        # nonpositive, and a nonnegative quartic term cannot repair it.
        assert generator_rank**2 - 4 * (maximum_quadratic + 1) in (-3, 0)

    useful_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_upper = Fraction(729, 6_400)
    assert useful_lower > useful_upper


def main() -> None:
    getcontext().prec = 85
    base.configure_elementary_module()
    exact_weighted_gs()

    # A favorable lower bound for the true Eisenstein constant is used in
    # every exclusion.  Smaller C makes the endpoint RHS smaller.
    sqrt_three_lower = Fraction(265, 153)
    assert sqrt_three_lower**2 < 3
    fifth = Fraction(1, 5)
    atan_fifth_upper = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(5)
    )
    q = Fraction(1, 239)
    pi_upper = 16 * atan_fifth_upper - 4 * (q - q**3 / 3)
    assert pi_upper < Fraction(355, 113)
    assert 2 * sqrt_three_lower / Fraction(355, 113) == C_LOWER_FRACTION

    primes = base.elementary.prime_sieve(250_000)
    universe = base.elementary.prime_ideals(primes, 250_000)
    units, colored = base.exact_ray_rows()
    assert base.gf2_rank(units) == 2
    unit_span = {0, units[0], units[1], units[0] ^ units[1]}
    functionals = [
        ell
        for ell in range(1, 16)
        if all(base.parity_dot(ell, unit) == 0 for unit in units)
    ]
    assert len(functionals) == 3
    case_specs: list[tuple[str, list[tuple[int, int, int | None, int]], int]] = [
        ("rank4", colored, 4)
    ]
    case_specs.extend(
        (
            f"rank3_ell{ell}",
            [row for row in colored if base.parity_dot(ell, row[3]) == 0],
            3,
        )
        for ell in functionals
    )
    case_specs.append(
        ("rank2", [row for row in colored if row[3] in unit_span], 2)
    )

    universe_by_key = {
        (row[0], row[1], row[3]): row for row in universe
    }
    results: dict[str, list[tuple]] = {}
    for name, allowed, constraint_rank in case_specs:
        chosen = allowed[:T_COUNT]
        assert base.gf2_rank(units + [row[3] for row in chosen]) == constraint_rank
        keys = {(row[0], row[1], row[2]) for row in chosen}
        selected = sorted(
            (universe_by_key[key] for key in keys),
            key=lambda row: (
                row[0], row[1], row[2],
                row[3] if row[3] is not None else -1,
            ),
        )
        candidates = [
            row for row in universe
            if (row[0], row[1], row[3]) not in keys
        ]
        generator_rank = T_COUNT + 2 - constraint_rank
        case_results = []
        for fourth_count in range(T_COUNT + 1):
            if name == "rank4" and fourth_count == 0:
                continue
            value = endpoint_exclusion(
                selected, fourth_count, generator_rank, candidates
            )
            case_results.append((value[0], fourth_count, *value[1:]))
        results[name] = case_results

    # Independently retain the already certified winner at its safe upper-C
    # anchor.  This is the sole skipped cell above.
    baseline = universe[:T_COUNT]
    baseline_useful = universe[T_COUNT : T_COUNT + base.USEFUL_COUNT]
    _, baseline_records, _ = base.endpoint_data(
        baseline, baseline_useful, base.ALPHA, base.W0
    )
    assert min(row[0] for row in baseline_records) > Decimal("0.001")

    # The first mixed cell is the closest competitor; the remaining
    # rank-four mixed thresholds worsen monotonically in the floating
    # diagnostic, while every cell has its own exact all-anchor exclusion.
    rank4 = results["rank4"]
    assert rank4[0][1] == 1
    assert rank4[0][0] < Decimal("-0.01")
    print("weighted GS for all ranks/cap counts: CERTIFIED")
    print("baseline margins:", baseline_records[0][0], baseline_records[1][0])
    for name, values in results.items():
        worst = max(values)
        print(name, "worst excluded / j / anchor:", worst[:3])
    print("D=821453 mixed inertia + rank-aware assignment: LOCKED")


if __name__ == "__main__":
    main()
