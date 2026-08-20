#!/usr/bin/env python3
"""Exact independent certificate for the D=4108373, T=217 CM record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic821453_cm as base  # noqa: E402


D = 4_108_373
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 217
GENERATOR_RANK = 215
USEFUL_COUNT = 11_123
SAFE_ALPHA = Decimal("0.49368647")
SAFE_C = Fraction(71_603, 64_935)


def configure() -> None:
    base.D = D
    base.C = OMEGA_CONSTANT
    base.T_COUNT = T_COUNT
    base.GENERATOR_RANK = GENERATOR_RANK
    base.USEFUL_COUNT = USEFUL_COUNT
    base.ALPHA = SAFE_ALPHA
    base.SAFE_C = SAFE_C
    base.elementary.FIELD_DISCRIMINANT = D
    base.elementary.OMEGA_CONSTANT = OMEGA_CONSTANT
    base.elementary.RAMIFIED_IDEAL_COUNT = T_COUNT


def exact_localization_metadata() -> tuple[int, ...]:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);nf=b.nf;L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);bid=idealstar(nf,[4,[1,1]],1,2);nar=bnfnarrow(b);T={T_COUNT};S=L[1..T];su=bnfsunit(b,vector(#S,i,S[i][3]));u=bnfunits(b,vector(#S,i,S[i][3]));M=Mat(vector(#u[1],i,ideallog(nf,u[1][i],bid)));T0=213;S0=L[1..T0];su0=bnfsunit(b,vector(#S0,i,S0[i][3]));u0=bnfunits(b,vector(#S0,i,S0[i][3]));M0=Mat(vector(#u0[1],i,ideallog(nf,u0[1][i],bid)));print("META,",bnfcertify(b),",",b.no,",",b.cyc[1],",",nar[1],",",nar[2][1],",",su[5][1],",",#su[5][2],",",#u[1],",",#bid.cyc,",",bid.cyc[1],",",bid.cyc[2],",",bid.cyc[3],",",bid.cyc[4],",",matrank(Mod(M,2)),",",#u[1]-matrank(Mod(M,2)),",",L[T][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),L[T][3])),",",su0[5][1],",",#su0[5][2],",",#u0[1],",",matrank(Mod(M0,2)),",",L[T0][1]);"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "2G"], input=script, text=True, timeout=60
    )
    line = next(row for row in output.splitlines() if row.startswith("META,"))
    metadata = tuple(map(int, line.split(",")[1:]))
    assert metadata == (
        1,
        2,
        2,
        4,
        2,
        1,
        0,
        219,
        4,
        2,
        2,
        2,
        2,
        4,
        215,
        1_117,
        1_020,
        1,
        0,
        215,
        4,
        1_091,
    )
    return metadata


def exact_kernel_and_usefulness(ideals):
    kernel, metadata = base.exact_kummer_kernel()
    assert metadata == (1, 2, 219, 4, 215, 1_117, 1_020)
    assert len(kernel) == GENERATOR_RANK

    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if base.elementary.norm((a, b)) % 2
    ]
    square_residues = {
        tuple(value % 4 for value in base.elementary.multiply(unit, unit))
        for unit in units_mod_four
    }
    assert len(units_mod_four) == 12 and len(square_residues) == 3
    for element in kernel:
        assert base.elementary.negative_at_embedding(element, False) == 0
        assert base.elementary.negative_at_embedding(element, True) == 0
        assert (element[0] % 4, element[1] % 4) in square_residues

    useful = []
    rejected = []
    maximum_trials = 0
    nonautomatic = 0
    for ideal in ideals[T_COUNT:]:
        norm_q, prime, _, root = ideal
        accepted = True
        trials = 0
        if norm_q % 3 == 2:
            nonautomatic += 1
            assert norm_q == prime and root is not None
            accepted = False
            for a, b in kernel:
                trials += 1
                residue = (a + b * root) % prime
                assert residue
                if pow(residue, (prime - 1) // 2, prime) == prime - 1:
                    accepted = True
                    break
            maximum_trials = max(maximum_trials, trials)
        (useful if accepted else rejected).append(ideal)
        if len(useful) == USEFUL_COUNT:
            break
    assert len(useful) == USEFUL_COUNT
    assert not rejected
    assert useful[-1] == (121_367, 121_367, "split", 69_978)
    return kernel, useful, rejected, nonautomatic, maximum_trials


def endpoint_certificate(ramified, useful, precision: int):
    getcontext().prec = precision
    threshold, anchor, _, log_rd = base.optimize_diagnostic(ramified, useful)
    checked_log_rd, records, maximum_omitted = base.endpoint_data(
        ramified, useful, SAFE_ALPHA, anchor
    )
    assert checked_log_rd == log_rd
    maximum_fourth_slope = max(
        base.local_gain(ideal[0], 4) / (Decimal(ideal[0]).ln() / 2)
        for ideal in useful
    )
    assert maximum_fourth_slope < min(record[2] for record in records)
    assert maximum_omitted < min(record[2] for record in records)
    assert min(record[0] for record in records) > Decimal("0.0015")
    assert records[0][1] > Decimal("0.005")
    assert records[1][1] < Decimal("-0.012")
    return threshold, anchor, log_rd, records, maximum_fourth_slope


def nearby_thresholds(ideals):
    getcontext().prec = 80
    output = {}
    for count in (213, 215, 217, 219, 221, 223, 225):
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        threshold, _, _, _ = base.optimize_diagnostic(
            ideals[:count], ideals[count : count + useful_count]
        )
        output[count] = threshold
    assert min(output, key=output.get) == T_COUNT
    assert output[217] + Decimal("2e-8") < output[215]
    assert output[217] + Decimal("5e-8") < output[219]
    return output


def main() -> None:
    getcontext().prec = 100
    configure()
    primes = base.elementary.prime_sieve(180_000)
    assert D == 17 * 67 * 3_607
    assert D % 8 == 5 and D % 3 == 2
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)

    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    fifth = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert 2 * sqrt_three_upper / Fraction(333, 106) == SAFE_C

    ideals = base.elementary.prime_ideals(primes, 180_000)
    assert ideals[T_COUNT - 1] == (1_117, 1_117, "split", 1_020)
    localization = exact_localization_metadata()
    kernel, useful, rejected, nonautomatic, maximum_trials = (
        exact_kernel_and_usefulness(ideals)
    )
    ramified = ideals[:T_COUNT]

    maximum_relations = (GENERATOR_RANK * GENERATOR_RANK - 1) // 4
    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert maximum_relations == relation_bound == 11_556
    point = Fraction(2, GENERATOR_RANK)
    assert 1 - GENERATOR_RANK * point + relation_bound * point**2 < 0

    outputs = [
        endpoint_certificate(ramified, useful, precision)
        for precision in (90, 150)
    ]
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-70")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-65")
    assert Decimal("0.4936864598") < outputs[1][0] < Decimal("0.4936864599")
    nearby = nearby_thresholds(ideals)

    print("field / localized ray metadata:", localization)
    print("kernel / useful / rejected / nonautomatic / max trials / last:", len(kernel), len(useful), len(rejected), nonautomatic, maximum_trials, useful[-1])
    print("generator / relation ceiling:", GENERATOR_RANK, relation_bound)
    print("90-digit endpoint:", outputs[0])
    print("150-digit endpoint:", outputs[1])
    print("nearby all-useful thresholds:")
    for count, threshold in nearby.items():
        print(" ", count, threshold)
    print("Q(sqrt(4108373)) CM F_2(n) << n^0.49368647: CERTIFIED")


if __name__ == "__main__":
    main()
