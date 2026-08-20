#!/usr/bin/env python3
"""Hostile no-go audit for the D=5277317 quadratic CM screen hit.

The optimistic genus-bonus screen is feasible, but exact S-class localization
kills that bonus.  This verifier certifies the exact rank and then excludes
all norm-prefix counts 205..250 even after declaring every useful-role ideal
useful.
"""

from __future__ import annotations

import bisect
from decimal import Decimal, getcontext
from fractions import Fraction
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic821453_cm as base  # noqa: E402


D = 5_277_317
ALPHA = Decimal("0.49368416")
T_MIN = 205
T_MAX = 250
C_LOWER = Fraction(11_978, 10_863)


def configure() -> None:
    base.D = D
    base.C = (D - 1) // 4
    base.SAFE_C = C_LOWER
    base.ALPHA = ALPHA
    base.elementary.FIELD_DISCRIMINANT = D
    base.elementary.OMEGA_CONSTANT = (D - 1) // 4


def exact_localization_rank() -> str:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);nf=b.nf;bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,2000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=2000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);VV=[205,221,222,250];for(ii=1,#VV,T=VV[ii];S=vector(T,i,L[i][3]);su=bnfsunit(b,S);u=bnfunits(b,S);M=Mat(vector(#u[1],i,ideallog(nf,u[1][i],bid)));r=-1;if(L[T][1]==L[T][2],r=lift(nfmodpr(nf,Mod(x,nf.pol),L[T][3])));print("ROW,",T,",",su[5][1],",",#su[5][2],",",#u[1],",",matrank(Mod(M,2)),",",L[T][1],",",r));print("META,",bnfcertify(b),",",b.no,",",b.clgp[2],",",bnfnarrow(b)[1],",",bnfnarrow(b)[2],",",bid.cyc);"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=120
    )
    lines = output.splitlines()
    assert "META,1,12,[12],12,[12],[2, 2, 2, 2]" in lines
    expected = {
        205: (1, 0, 207, 4, 967, 732),
        221: (1, 0, 223, 4, 1031, 848),
        222: (1, 0, 224, 4, 1061, 23),
        250: (1, 0, 252, 4, 1307, 236),
    }
    found = {}
    for line in lines:
        match = re.fullmatch(
            r"ROW,(\d+),(\d+),(\d+),(\d+),(\d+),(\d+),(-?\d+)",
            line,
        )
        if match:
            values = tuple(map(int, match.groups()))
            found[values[0]] = values[1:]
    assert found == expected

    # At T=205 the S-class group is already trivial and the ray image already
    # has full rank four.  Both facts persist upon adding more prime ideals.
    # Thus every prefix in the interval has pre-ray dimension T+2 and safe
    # rank d=T+2-4=T-2.
    return output


def local_gain(norm_q: int, depth: int) -> float:
    parameter = 1.0 / (norm_q * norm_q)
    previous_sum = 1.0
    total = 1.0
    power = 1.0
    for _ in range(depth):
        previous_sum = total
        power *= parameter
        total += power
    return 0.25 * (
        math.log1p(1.0 / depth)
        + math.log(previous_sum)
        - math.log(total)
    )


def floating_score(ideals, count: int):
    generator_rank = count - 2
    useful_count = (
        (generator_rank * generator_rank - 1) // 4
        - (generator_rank + 1)
        - count
    )
    useful = ideals[count : count + useful_count]
    increments = []
    maximum_omitted = 0.0
    for ideal in useful:
        norm_q = ideal[0]
        cost = 0.5 * math.log(norm_q)
        for depth in range(1, 9):
            gain = local_gain(norm_q, depth)
            increments.append((gain / cost, cost, gain))
        maximum_omitted = max(
            maximum_omitted, local_gain(norm_q, 9) / cost
        )
    increments.sort(reverse=True)
    costs = [0.0]
    gains = [0.0]
    slopes = []
    for slope, cost, gain in increments:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
        slopes.append(slope)

    constant = C_LOWER.numerator / C_LOWER.denominator
    alpha = float(ALPHA)
    log_rd = 0.5 * math.log(D) + 0.25 * sum(
        math.log(ideal[0]) for ideal in ideals[:count]
    )

    def envelope(target: float):
        index = bisect.bisect_left(costs, target)
        assert 0 < index < len(costs)
        fraction = (target - costs[index - 1]) / (
            costs[index] - costs[index - 1]
        )
        return (
            gains[index - 1]
            + fraction * (gains[index] - gains[index - 1]),
            slopes[index - 1],
        )

    def records(anchor: float):
        output = []
        for endpoint in (1, 2):
            scale = float(endpoint)
            w = scale * anchor
            value, slope = envelope(2 * alpha * w)
            exponent = 2 * (2 * alpha - 1) * w - log_rd
            ratio = math.exp(exponent) / constant
            rhs = (
                math.log(constant)
                + log_rd
                + (2 - 4 * alpha) * w
                + math.log1p(ratio)
            )
            derivative = (
                2 * alpha * scale * slope
                - (2 - 4 * alpha) * scale
                - 2
                * (2 * alpha - 1)
                * scale
                * ratio
                / (1 + ratio)
            )
            output.append((value - rhs, derivative, slope))
        return output

    low, high = 30_000.0, 60_000.0
    low_records = records(low)
    high_records = records(high)
    low_difference = low_records[0][0] - low_records[1][0]
    high_difference = high_records[0][0] - high_records[1][0]
    assert low_difference * high_difference < 0
    for _ in range(90):
        middle = (low + high) / 2
        data = records(middle)
        difference = data[0][0] - data[1][0]
        if low_difference * difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = difference
    anchor = (low + high) / 2
    data = records(anchor)
    assert data[0][1] > 0 and data[1][1] < 0
    assert maximum_omitted < min(record[2] for record in data)
    return (
        max(record[0] for record in data),
        count,
        generator_rank,
        useful_count,
        anchor,
        data,
        maximum_omitted,
    )


def decimal_score(ideals, count: int, generator_rank: int):
    useful_count = (
        (generator_rank * generator_rank - 1) // 4
        - (generator_rank + 1)
        - count
    )
    log_rd, frontier, maximum_omitted = base.prepare_endpoint_data(
        ideals[:count], ideals[count : count + useful_count]
    )

    def records(anchor: Decimal):
        return base.evaluate_prepared(log_rd, frontier, ALPHA, anchor)

    low, high = Decimal("30000"), Decimal("60000")
    low_data = records(low)
    high_data = records(high)
    low_difference = low_data[0][0] - low_data[1][0]
    high_difference = high_data[0][0] - high_data[1][0]
    assert low_difference * high_difference < 0
    for _ in range(110):
        middle = (low + high) / 2
        data = records(middle)
        difference = data[0][0] - data[1][0]
        if low_difference * difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = difference
    anchor = (low + high) / 2
    data = records(anchor)
    assert abs(data[0][0] - data[1][0]) < Decimal("1e-25")
    assert data[0][1] > Decimal("0.004")
    assert data[1][1] < Decimal("-0.012")
    assert maximum_omitted < min(record[2] for record in data)
    return useful_count, anchor, data, maximum_omitted


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


def main() -> None:
    getcontext().prec = 100
    configure()
    packing_constant_audit()
    assert D == 613 * 8_609
    localization = exact_localization_rank()

    primes = base.elementary.prime_sieve(230_000)
    ideals = base.elementary.prime_ideals(primes, 230_000)
    sweep = [floating_score(ideals, count) for count in range(T_MIN, T_MAX + 1)]
    sweep.sort(reverse=True)
    assert sweep[0][1:4] == (221, 219, 11_549)
    assert sweep[1][1] == 223
    assert sweep[0][0] < -0.104
    assert all(record[0] < -0.10 for record in sweep)

    ordinary = decimal_score(ideals, 221, 219)
    assert ordinary[0] == 11_549
    assert max(record[0] for record in ordinary[2]) < Decimal("-0.1047")

    # This records the false-positive mechanism.  If one incorrectly grants
    # the genus dimension at T=222, then d=221 and the relaxed cell is strongly
    # feasible.  The exact localization certificate above proves d=220.
    genus_relaxation = decimal_score(ideals, 222, 221)
    assert genus_relaxation[0] == 11_766
    assert min(record[0] for record in genus_relaxation[2]) > Decimal("1.72")

    print(localization, end="")
    print("leading exact-rank all-useful prefix cells:")
    for record in sweep[:10]:
        print(" ", record[:5])
    print("T=221 favorable-lower-C Decimal:", ordinary)
    print("unrealizable T=222 genus relaxation:", genus_relaxation)
    print("D=5277317 genus-screen false positive: CERTIFIED")


if __name__ == "__main__":
    main()
