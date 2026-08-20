#!/usr/bin/env python3
"""Lock the D=43133 CM record against mixed inertia and reassignment.

The canonical arithmetic certificate is rerun first.  This file then checks
the weighted Golod--Shafarevich formula independently, proves the exact
endpoint dual inequalities for every mixed cap count and every prime-ideal
assignment (in the optimistic all-useful relaxation), and performs a full
floating reoptimization as a diagnostic.
"""

from __future__ import annotations

import bisect
from decimal import Decimal, getcontext
from fractions import Fraction
import math
import re
import shutil
import subprocess

import verify_hostile_quadratic43133_cm as base


getcontext().prec = 100

RAMIFIED_COUNT = 223
GENERATOR_RANK = 221
BASE_RELATIONS = 222
USEFUL_COUNT = 11_765
MAXIMUM_QUADRATIC_RELATIONS = 12_210


def exact_ray_colors() -> list[tuple[int, int, int | None, int]]:
    """Compute prime-ideal colors modulo the two unit constraint columns."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required for the rank-aware assignment lock")
    script = r"""D=43133;c=(D-1)/4;bnf=bnfinit(x^2-x-c,1);cert=bnfcertify(bnf);nf=bnf.nf;bid=idealstar(nf,[4,[1,1]],1,2);print("META,",cert,",",bnf.no,",",bid.cyc);print("UNIT,",concat(Vec(ideallog(nf,-1,bid))));eps=11516800325138112653+111443097178087930*x;print("UNIT,",concat(Vec(ideallog(nf,eps,bid))));forprime(p=3,7000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=7000,my(z=bnfisprincipal(bnf,dec[i])[2],v=ideallog(nf,z,bid),r=-1);if(Q==p,r=lift(nfmodpr(nf,Mod(x,nf.pol),dec[i])));print("IDEAL,",Q,",",p,",",r,",",concat(Vec(v))))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True
    )
    lines = output.splitlines()
    assert "META,1,1,[2, 2, 2, 2]" in lines

    vector_pattern = r"\[([01]), ([01]), ([01]), ([01])\]"
    unit_rows: list[int] = []
    raw_ideals: list[tuple[int, int, int | None, int]] = []
    for line in lines:
        unit_match = re.fullmatch(r"UNIT," + vector_pattern, line)
        if unit_match:
            unit_rows.append(
                sum(int(unit_match.group(1 + i)) << i for i in range(4))
            )
            continue
        ideal_match = re.fullmatch(
            r"IDEAL,(\d+),(\d+),(-?\d+)," + vector_pattern, line
        )
        if ideal_match:
            norm_q, p, root = map(int, ideal_match.group(1, 2, 3))
            vector = sum(
                int(ideal_match.group(4 + i)) << i for i in range(4)
            )
            raw_ideals.append(
                (norm_q, p, None if root < 0 else root, vector)
            )

    assert len(unit_rows) == 2 and base.gf2_rank(unit_rows) == 2
    unit_span = [0, unit_rows[0], unit_rows[1], unit_rows[0] ^ unit_rows[1]]
    colored = [
        (norm_q, p, root, min(vector ^ unit for unit in unit_span))
        for norm_q, p, root, vector in raw_ideals
    ]
    colored.sort()
    assert {row[3] for row in colored} == {0, 1, 2, 3}
    assert colored[0] == (9, 3, None, 1)
    return colored


def exact_weighted_gs_check() -> None:
    """Check every square/fourth/uncapped inertia count exactly."""
    assert MAXIMUM_QUADRATIC_RELATIONS == (GENERATOR_RANK**2 - 1) // 4
    assert MAXIMUM_QUADRATIC_RELATIONS * 4 == GENERATOR_RANK**2 - 1
    x = Fraction(2, GENERATOR_RANK)

    for square_count in range(RAMIFIED_COUNT + 1):
        useful_count = (
            MAXIMUM_QUADRATIC_RELATIONS - BASE_RELATIONS - square_count
        )
        assert useful_count == 11_988 - square_count
        quadratic_count = BASE_RELATIONS + square_count + useful_count
        assert quadratic_count == MAXIMUM_QUADRATIC_RELATIONS

        # P(x)=1-dx+(r0+s2+N)x^2+s4*x^4.  This checks every
        # 0 <= s4 <= 223-s2, not just the two extreme values.
        for fourth_count in range(RAMIFIED_COUNT - square_count + 1):
            polynomial = (
                1
                - GENERATOR_RANK * x
                + quadratic_count * x**2
                + fourth_count * x**4
            )
            assert polynomial < 0

        # One more quadratic relator makes the quadratic truncation
        # positive on the whole real line; a nonnegative quartic term cannot
        # repair it.
        assert GENERATOR_RANK**2 - 4 * (quadratic_count + 1) == -3

    assert 16 * RAMIFIED_COUNT < GENERATOR_RANK**2
    assert 11_988 - RAMIFIED_COUNT == USEFUL_COUNT

    # Uniform all-depth monotonicity of the useful-role dual value.  For
    # Q>=9, t=Q^-2 and K>=1, the proof compares
    #   2K*g_{K+1} >= 1/6-1/(2*81^2)
    # with
    #   log(Q)*mu_K <= 729/6400.
    # The strict rational gap makes V_lambda(Q) nonincreasing for every
    # lambda, including beyond the convenient large-lambda regime.
    useful_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_upper = Fraction(729, 6_400)
    assert useful_lower > useful_upper


def frontier(
    ideals: list[tuple[int, int, str, int | None]],
) -> tuple[
    list[tuple[Decimal, Decimal, Decimal, int, int, int]], Decimal
]:
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, ideal in enumerate(ideals):
        norm_q = ideal[0]
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        for depth in range(1, 5):
            gain = base.local_increment(norm_q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if depth <= 3:
                increments.append(
                    (slope, cost, gain, norm_q, depth, ideal_index)
                )
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)
    seen = {index: 0 for index in range(len(ideals))}
    for _, _, _, _, depth, ideal_index in increments:
        assert depth == seen[ideal_index] + 1
        seen[ideal_index] = depth
    return increments, maximum_fourth_slope


def adaptive_all_depth_frontier(
    ideals: list[tuple[int, int, str, int | None]],
    slope_floor: Decimal = Decimal("0.01"),
) -> tuple[
    list[tuple[Decimal, Decimal, Decimal, int, int, int]], Decimal
]:
    """Retain every depth above a safe global active-slope floor."""
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_omitted_slope = Decimal(0)
    for ideal_index, ideal in enumerate(ideals):
        norm_q = ideal[0]
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        depth = 1
        while True:
            gain = base.local_increment(norm_q, depth)
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if slope < slope_floor:
                maximum_omitted_slope = max(maximum_omitted_slope, slope)
                break
            increments.append(
                (slope, cost, gain, norm_q, depth, ideal_index)
            )
            depth += 1
            assert depth < 100
    increments.sort(reverse=True)
    return increments, maximum_omitted_slope


def envelope(
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]],
    target: Decimal,
) -> tuple[Decimal, int, Decimal, Decimal]:
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


def active_dual_value(norm_q: int, slope: Decimal) -> tuple[Decimal, int]:
    """All-depth V_lambda(Q), stopping only at the first inactive depth."""
    cost = Decimal(norm_q).ln() / 2
    value = Decimal(0)
    depth = 1
    while True:
        gain = base.local_increment(norm_q, depth)
        excess = gain - slope * cost
        if excess <= 0:
            return value, depth - 1
        value += excess
        depth += 1
        assert depth < 100


def exact_endpoint_dual(
    ramified: list[tuple[int, int, str, int | None]],
    candidates: list[tuple[int, int, str, int | None]],
) -> tuple[list[Decimal], list[tuple[Decimal, Decimal]], Decimal]:
    """Prove joint mixed-cap/nonprefix dominance at both endpoints."""
    baseline_useful = candidates[:USEFUL_COUNT]
    increments, maximum_fourth_slope = frontier(baseline_useful)
    log_rd = Decimal(base.FIELD_DISCRIMINANT).ln() / 2
    log_rd += sum(Decimal(row[0]).ln() / 4 for row in ramified)
    assert base.ALPHA < Decimal("0.5") and log_rd > 100
    # For every w>=0, the correction exponent is at most -logRD<-100.
    global_rho_lower = Decimal(1) / (
        Decimal(1) + Decimal(-100).exp() / base.C_UPPER
    )
    minimum_norm_log = Decimal(ramified[0][0]).ln()
    assert global_rho_lower > Decimal(1) / minimum_norm_log
    assert global_rho_lower > Decimal(2) / (3 * minimum_norm_log)

    def rhs(alpha: Decimal, w: Decimal) -> Decimal:
        exponent = 2 * (2 * alpha - 1) * w - log_rd
        correction = (Decimal(1) + exponent.exp() / base.C_UPPER).ln()
        return (
            base.C_UPPER.ln()
            + log_rd
            + (2 - 4 * alpha) * w
            + correction
        )

    left = envelope(increments, 2 * base.ALPHA * base.W0)
    right = envelope(increments, 4 * base.ALPHA * base.W0)
    assert maximum_fourth_slope < right[3]
    margins = [
        left[0] - rhs(base.ALPHA, base.W0) - base.EPSILON,
        right[0] - rhs(base.ALPHA, 2 * base.W0) - base.EPSILON,
    ]
    assert min(margins) > Decimal("0.001")

    # The exact tangent derivative is
    # rho=1/(1+exp(B-logRD)/C).  At both endpoints B-logRD<-100,
    # so the following is a rigorous common lower bound (and avoids rounding
    # the true derivative to exactly one).
    rho_lower = Decimal(1) / (
        Decimal(1) + Decimal(-100).exp() / base.C_UPPER
    )

    minimum_pair_gaps: list[Decimal] = []
    assignment_parameters: list[tuple[Decimal, Decimal]] = []
    for scale, endpoint in ((Decimal(1), left), (Decimal(2), right)):
        w = scale * base.W0
        correction_exponent = 2 * (2 * base.ALPHA - 1) * w - log_rd
        assert correction_exponent < -100
        lam = endpoint[3]

        # For j fourth caps, the optimistic best assignment puts them on the
        # j smallest ramified ideals and adds the next j raw prime ideals as
        # useful.  The displayed gap is penalty minus all-depth dual value.
        gaps: list[Decimal] = []
        cumulative = Decimal(0)
        for j in range(RAMIFIED_COUNT):
            added_norm = candidates[USEFUL_COUNT + j][0]
            value, _ = active_dual_value(added_norm, lam)
            penalty = rho_lower * Decimal(ramified[j][0]).ln() / 8
            gap = penalty - value
            assert gap > 0
            gaps.append(gap)
            cumulative -= gap
            assert cumulative < 0
        minimum_pair_gaps.append(min(gaps))

        # These inequalities prove the pairwise exchanges used by the
        # assignment theorem.  For y=log Q and K active depths,
        # V'_lambda(y)>-1/(4y).  Consequently rho*y/4+V and
        # 3rho*y/8+V increase through all available ideal norms.  The exact
        # rational lemma in exact_weighted_gs_check proves V itself is
        # nonincreasing for every lambda.  The last inequality below is a
        # redundant endpoint-specific check with enormous slack.
        minimum_norm = Decimal(ramified[0][0])
        first_useful_norm = Decimal(candidates[0][0])
        tail = first_useful_norm**-2 / (
            Decimal(1) - first_useful_norm**-2
        ) ** 2
        assert rho_lower > Decimal(1) / minimum_norm.ln()
        assert rho_lower > Decimal(2) / (3 * minimum_norm.ln())
        assert lam > tail
        assignment_parameters.append((lam, rho_lower))

    return minimum_pair_gaps, assignment_parameters, maximum_fourth_slope


def floating_reoptimization(
    ramified: list[tuple[int, int, str, int | None]],
    candidates: list[tuple[int, int, str, int | None]],
) -> tuple[list[tuple[float, float, float]], float]:
    """Diagnostic all-j optimization; exact endpoint dual is the proof."""
    constant = float(base.C_UPPER)
    all_items: list[tuple[float, float, float, int, int]] = []
    maximum_fourth_slope = 0.0
    for ideal_index, ideal in enumerate(candidates):
        q = ideal[0]
        parameter = q**-2
        totals = [1.0]
        for depth in range(1, 5):
            totals.append(totals[-1] + parameter**depth)
        cost = math.log(q) / 2
        for depth in range(1, 5):
            gain = math.log(
                ((depth + 1) / totals[depth])
                / (depth / totals[depth - 1])
            ) / 4
            slope = gain / cost
            if depth <= 3:
                all_items.append(
                    (slope, cost, gain, ideal_index, depth)
                )
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)

    results: list[tuple[float, float, float]] = []
    minimum_active_slope = float("inf")
    for fourth_count in range(RAMIFIED_COUNT + 1):
        useful_count = USEFUL_COUNT + fourth_count
        items = [row for row in all_items if row[3] < useful_count]
        items.sort(reverse=True)
        costs = [0.0]
        gains = [0.0]
        for _, cost, gain, _, _ in items:
            costs.append(costs[-1] + cost)
            gains.append(gains[-1] + gain)

        log_rd = math.log(base.FIELD_DISCRIMINANT) / 2
        for index, ideal in enumerate(ramified):
            exponent = 3 / 8 if index < fourth_count else 1 / 4
            log_rd += exponent * math.log(ideal[0])

        def float_envelope(target: float) -> tuple[float, float]:
            index = bisect.bisect_left(costs, target)
            assert 0 < index < len(costs)
            fraction = (target - costs[index - 1]) / (
                costs[index] - costs[index - 1]
            )
            value = gains[index - 1] + fraction * (
                gains[index] - gains[index - 1]
            )
            return value, items[index - 1][0]

        def margin(alpha: float, w0: float, endpoint: int) -> float:
            w = endpoint * w0
            value, _ = float_envelope(2 * alpha * w)
            rhs = (
                math.log(constant)
                + log_rd
                + (2 - 4 * alpha) * w
                + math.log1p(
                    math.exp(2 * (2 * alpha - 1) * w - log_rd)
                    / constant
                )
            )
            return value - rhs

        def alpha_root(w0: float, endpoint: int) -> float:
            low, high = 0.49, 0.497
            assert margin(low, w0, endpoint) < 0
            assert margin(high, w0, endpoint) > 0
            for _ in range(55):
                middle = (low + high) / 2
                if margin(middle, w0, endpoint) > 0:
                    high = middle
                else:
                    low = middle
            return (low + high) / 2

        def difference(w0: float) -> float:
            return alpha_root(w0, 1) - alpha_root(w0, 2)

        low_w, high_w = 30_000.0, 60_000.0
        low_value, high_value = difference(low_w), difference(high_w)
        assert low_value * high_value < 0
        for _ in range(50):
            middle_w = (low_w + high_w) / 2
            middle_value = difference(middle_w)
            if low_value * middle_value <= 0:
                high_w, high_value = middle_w, middle_value
            else:
                low_w, low_value = middle_w, middle_value
        optimum_w = (low_w + high_w) / 2
        threshold = max(alpha_root(optimum_w, 1), alpha_root(optimum_w, 2))
        _, right_slope = float_envelope(4 * threshold * optimum_w)
        minimum_active_slope = min(minimum_active_slope, right_slope)
        results.append((threshold, optimum_w, right_slope))

    assert results[0][0] < float(base.ALPHA)
    assert all(results[j][0] > float(base.ALPHA) for j in range(1, len(results)))
    assert all(
        results[j][0] > results[j - 1][0] for j in range(1, len(results))
    )
    assert maximum_fourth_slope < minimum_active_slope
    return results, maximum_fourth_slope


def exact_no_reoptimized_mixed_improvement(
    ramified: list[tuple[int, int, str, int | None]],
    candidates: list[tuple[int, int, str, int | None]],
    diagnostics: list[tuple[float, float, float]],
) -> tuple[Decimal, Decimal, Decimal, Decimal]:
    """Exclude every j>=1 and every anchor w at alpha=0.49369772.

    Each endpoint margin is concave in w.  At a rational separator near the
    floating crossing, the left margin is negative with positive derivative
    and the right margin is negative with negative derivative.  Concavity
    then makes simultaneous feasibility impossible on either side of the
    separator.  The uniform role-exchange lemma makes this prefix the
    optimistic optimum over every prime-ideal assignment for all w>=0.
    All inequalities have deliberately large Decimal slack.
    """
    all_increments, _ = frontier(candidates)
    log_rd = Decimal(base.FIELD_DISCRIMINANT).ln() / 2
    log_rd += sum(Decimal(row[0]).ln() / 4 for row in ramified)
    assert base.ALPHA < Decimal("0.5") and log_rd > 100
    global_rho_lower = Decimal(1) / (
        Decimal(1) + Decimal(-100).exp() / base.C_UPPER
    )
    minimum_norm_log = Decimal(ramified[0][0]).ln()
    assert global_rho_lower > Decimal(1) / minimum_norm_log
    assert global_rho_lower > Decimal(2) / (3 * minimum_norm_log)

    largest_left_margin = Decimal("-Infinity")
    largest_right_margin = Decimal("-Infinity")
    smallest_left_derivative = Decimal("Infinity")
    largest_right_derivative = Decimal("-Infinity")

    for fourth_count in range(1, RAMIFIED_COUNT + 1):
        # The optimal mixed assignment changes the next smallest ramified
        # ideal from exponent 1/4 to 3/8.
        log_rd += Decimal(ramified[fourth_count - 1][0]).ln() / 8
        useful_count = USEFUL_COUNT + fourth_count
        increments = [
            row for row in all_increments if row[5] < useful_count
        ]
        separator = Decimal(str(diagnostics[fourth_count][1]))

        endpoint_data: list[tuple[Decimal, Decimal]] = []
        for endpoint in (1, 2):
            scale = Decimal(endpoint)
            w = scale * separator
            value, _, fraction, slope = envelope(
                increments, 2 * base.ALPHA * w
            )
            assert Decimal("1e-8") < fraction < Decimal(1) - Decimal("1e-8")
            exponent = 2 * (2 * base.ALPHA - 1) * w - log_rd
            ratio = exponent.exp() / base.C_UPPER
            rho = Decimal(1) / (Decimal(1) + ratio)
            assert rho > Decimal(1) / minimum_norm_log
            assert rho > Decimal(2) / (3 * minimum_norm_log)
            rhs = (
                base.C_UPPER.ln()
                + log_rd
                + (2 - 4 * base.ALPHA) * w
                + (Decimal(1) + ratio).ln()
            )
            margin = value - rhs

            # Derivative with respect to the unscaled anchor separator.
            exponent_derivative = 2 * (2 * base.ALPHA - 1) * scale
            derivative = (
                2 * base.ALPHA * scale * slope
                - (2 - 4 * base.ALPHA) * scale
                - exponent_derivative * ratio / (Decimal(1) + ratio)
            )
            endpoint_data.append((margin, derivative))

        left_data, right_data = endpoint_data
        assert left_data[0] < Decimal("-0.1")
        assert right_data[0] < Decimal("-0.1")
        assert left_data[1] > Decimal("0.001")
        assert right_data[1] < Decimal("-0.001")
        largest_left_margin = max(largest_left_margin, left_data[0])
        largest_right_margin = max(largest_right_margin, right_data[0])
        smallest_left_derivative = min(
            smallest_left_derivative, left_data[1]
        )
        largest_right_derivative = max(
            largest_right_derivative, right_data[1]
        )

    return (
        largest_left_margin,
        largest_right_margin,
        smallest_left_derivative,
        largest_right_derivative,
    )


def rank_aware_all_assignment_lock(
    universe: list[tuple[int, int, str, int | None]],
) -> tuple[
    dict[str, list[tuple[float, float, float]]],
    dict[str, tuple[int, int, tuple[int, int, int | None, int], Decimal]],
    tuple[Decimal, Decimal, Decimal, Decimal],
]:
    """Include every possible quotient constraint rank 0, 1, or 2."""
    colored = exact_ray_colors()
    cases = [
        ("rank2", {0, 1, 2, 3}, 2),
        ("rank1_a", {0, 1}, 1),
        ("rank1_b", {0, 2}, 1),
        ("rank1_c", {0, 3}, 1),
        ("rank0", {0}, 0),
    ]
    constant_float = float(base.C_UPPER)
    diagnostics_by_case: dict[str, list[tuple[float, float, float]]] = {}
    metadata: dict[
        str, tuple[int, int, tuple[int, int, int | None, int], Decimal]
    ] = {}
    largest_left_margin = Decimal("-Infinity")
    largest_right_margin = Decimal("-Infinity")
    smallest_left_derivative = Decimal("Infinity")
    largest_right_derivative = Decimal("-Infinity")

    for name, allowed_colors, quotient_rank in cases:
        selected_colored = [
            row for row in colored if row[3] in allowed_colors
        ][:RAMIFIED_COUNT]
        assert len(selected_colored) == RAMIFIED_COUNT
        assert base.gf2_rank([row[3] for row in selected_colored]) == quotient_rank
        selected_keys = {
            (norm_q, p, root) for norm_q, p, root, _ in selected_colored
        }
        selected = [
            row
            for row in universe
            if (row[0], row[1], row[3]) in selected_keys
        ]
        assert len(selected) == RAMIFIED_COUNT

        generator_rank = RAMIFIED_COUNT - quotient_rank
        maximum_quadratic = (generator_rank**2 - 1) // 4
        useful_base = (
            maximum_quadratic
            - (generator_rank + 1)
            - RAMIFIED_COUNT
        )
        assert useful_base in (11_765, 11_874, 11_985)
        gs_point = Fraction(2, generator_rank)
        assert generator_rank**2 - 4 * (maximum_quadratic + 1) in (-3, 0)
        for fourth_count in range(RAMIFIED_COUNT + 1):
            assert (
                1
                - generator_rank * gs_point
                + maximum_quadratic * gs_point**2
                + fourth_count * gs_point**4
            ) < 0

        # This is deliberately more favorable than the arithmetic problem:
        # every ideal outside T, even the CM-ramified ideal above 3, is given
        # the formal useful local gain.
        candidates = [
            row
            for row in universe
            if (row[0], row[1], row[3]) not in selected_keys
        ][: useful_base + RAMIFIED_COUNT]
        assert len(candidates) == useful_base + RAMIFIED_COUNT
        all_increments, maximum_omitted = adaptive_all_depth_frontier(
            candidates
        )

        log_rd = Decimal(base.FIELD_DISCRIMINANT).ln() / 2
        log_rd += sum(Decimal(row[0]).ln() / 4 for row in selected)
        metadata[name] = (
            generator_rank,
            useful_base,
            selected_colored[-1],
            log_rd,
        )
        results: list[tuple[float, float, float]] = []

        for fourth_count in range(RAMIFIED_COUNT + 1):
            if fourth_count:
                log_rd += Decimal(selected[fourth_count - 1][0]).ln() / 8
            useful_count = useful_base + fourth_count
            increments = [
                row for row in all_increments if row[5] < useful_count
            ]
            float_items = [
                (float(row[0]), float(row[1]), float(row[2]))
                for row in increments
            ]
            costs = [0.0]
            gains = [0.0]
            for _, cost, gain in float_items:
                costs.append(costs[-1] + cost)
                gains.append(gains[-1] + gain)
            log_rd_float = float(log_rd)

            def float_envelope(target: float) -> tuple[float, float]:
                index = bisect.bisect_left(costs, target)
                assert 0 < index < len(costs)
                fraction = (target - costs[index - 1]) / (
                    costs[index] - costs[index - 1]
                )
                value = gains[index - 1] + fraction * (
                    gains[index] - gains[index - 1]
                )
                return value, float_items[index - 1][0]

            def float_margin(alpha: float, anchor: float, endpoint: int) -> float:
                w = endpoint * anchor
                value, _ = float_envelope(2 * alpha * w)
                rhs = (
                    math.log(constant_float)
                    + log_rd_float
                    + (2 - 4 * alpha) * w
                    + math.log1p(
                        math.exp(2 * (2 * alpha - 1) * w - log_rd_float)
                        / constant_float
                    )
                )
                return value - rhs

            def alpha_root(anchor: float, endpoint: int) -> float:
                low, high = 0.49, 0.499
                assert float_margin(low, anchor, endpoint) < 0
                assert float_margin(high, anchor, endpoint) > 0
                for _ in range(55):
                    middle = (low + high) / 2
                    if float_margin(middle, anchor, endpoint) > 0:
                        high = middle
                    else:
                        low = middle
                return (low + high) / 2

            def root_difference(anchor: float) -> float:
                return alpha_root(anchor, 1) - alpha_root(anchor, 2)

            low_w, high_w = 30_000.0, 60_000.0
            low_value, high_value = root_difference(low_w), root_difference(high_w)
            assert low_value * high_value < 0
            for _ in range(50):
                middle_w = (low_w + high_w) / 2
                middle_value = root_difference(middle_w)
                if low_value * middle_value <= 0:
                    high_w, high_value = middle_w, middle_value
                else:
                    low_w, low_value = middle_w, middle_value
            separator_float = (low_w + high_w) / 2
            threshold = max(
                alpha_root(separator_float, 1),
                alpha_root(separator_float, 2),
            )
            _, active_right_slope = float_envelope(
                4 * threshold * separator_float
            )
            assert active_right_slope > float(maximum_omitted)
            results.append((threshold, separator_float, active_right_slope))

            # The canonical all-square case is the certified winner.  Every
            # other cap/rank configuration is excluded for all anchors by a
            # 100-digit concavity separator.
            if name == "rank2" and fourth_count == 0:
                continue
            separator = Decimal(str(separator_float))
            endpoint_data: list[tuple[Decimal, Decimal]] = []
            for endpoint in (1, 2):
                scale = Decimal(endpoint)
                w = scale * separator
                value, _, fraction, slope = envelope(
                    increments, 2 * base.ALPHA * w
                )
                assert Decimal("1e-8") < fraction < Decimal(1) - Decimal("1e-8")
                assert slope > maximum_omitted
                exponent = 2 * (2 * base.ALPHA - 1) * w - log_rd
                ratio = exponent.exp() / base.C_UPPER
                rhs = (
                    base.C_UPPER.ln()
                    + log_rd
                    + (2 - 4 * base.ALPHA) * w
                    + (Decimal(1) + ratio).ln()
                )
                margin = value - rhs
                exponent_derivative = 2 * (2 * base.ALPHA - 1) * scale
                derivative = (
                    2 * base.ALPHA * scale * slope
                    - (2 - 4 * base.ALPHA) * scale
                    - exponent_derivative * ratio / (Decimal(1) + ratio)
                )
                endpoint_data.append((margin, derivative))

            left_data, right_data = endpoint_data
            assert left_data[0] < Decimal("-0.1")
            assert right_data[0] < Decimal("-0.1")
            assert left_data[1] > Decimal("0.001")
            assert right_data[1] < Decimal("-0.001")
            largest_left_margin = max(largest_left_margin, left_data[0])
            largest_right_margin = max(largest_right_margin, right_data[0])
            smallest_left_derivative = min(
                smallest_left_derivative, left_data[1]
            )
            largest_right_derivative = max(
                largest_right_derivative, right_data[1]
            )

        diagnostics_by_case[name] = results

    global_slacks = (
        largest_left_margin,
        largest_right_margin,
        smallest_left_derivative,
        largest_right_derivative,
    )
    return diagnostics_by_case, metadata, global_slacks


def main() -> None:
    # First rerun the separate hostile arithmetic certificate: class number,
    # signatures, 221-dimensional Kummer kernel, all 11,765 useful tests,
    # exceptional ideal above 43,133, root discriminant, and endpoints.
    base.main()

    exact_weighted_gs_check()
    primes = base.prime_sieve(300_000)
    ideals = base.prime_ideals(primes, 300_000)
    ramified = ideals[:RAMIFIED_COUNT]
    candidates = ideals[
        RAMIFIED_COUNT : RAMIFIED_COUNT + USEFUL_COUNT + RAMIFIED_COUNT
    ]
    assert ramified[-1] == (1_163, 1_163, "split", 646)
    assert candidates[0] == (1_187, 1_187, "split", 473)
    assert candidates[USEFUL_COUNT - 1] == (
        129_629,
        129_629,
        "split",
        2_193,
    )
    assert candidates[-1] == (132_383, 132_383, "split", 118_381)

    gaps, parameters, exact_max_fourth = exact_endpoint_dual(
        ramified, candidates
    )
    rank_diagnostics, rank_metadata, global_mixed_slacks = (
        rank_aware_all_assignment_lock(ideals)
    )
    diagnostics = rank_diagnostics["rank2"]
    assert float(exact_max_fourth) < diagnostics[0][2]

    representative = [0, 1, 2, 10, 50, 100, 150, 200, 223]
    print("mixed GS N=11988-s2 for every s2,s4: CERTIFIED")
    print("joint mixed/nonprefix endpoint dual gaps:", *gaps)
    print("assignment lambda/rho lower bounds:", *parameters)
    print("rank-aware ray metadata:", rank_metadata)
    print(
        "rank-aware all-square diagnostics:",
        {name: values[0] for name, values in rank_diagnostics.items()},
    )
    print("all-j diagnostic best:", min(enumerate(diagnostics), key=lambda x: x[1][0]))
    print(
        "representative mixed thresholds:",
        [(j, diagnostics[j][0], diagnostics[j][1]) for j in representative],
    )
    print("exact all-anchor mixed exclusion slacks:", *global_mixed_slacks)
    print("maximum omitted fourth slope:", exact_max_fourth)
    print("D=43133 mixed-inertia and assignment lock: CERTIFIED")


if __name__ == "__main__":
    main()
