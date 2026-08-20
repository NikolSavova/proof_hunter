#!/usr/bin/env python3
"""Exact wrapper for the D=6999893 broad norm-prefix count lock.

The C++ companion exhausts T=50,...,600 under the favorable all-useful
relaxation.  This wrapper certifies the C4 class/ray rank behavior, weighted
GS bookkeeping, rational packing constants, and the closest excluded and
retained cells with high-precision Decimal arithmetic.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic6999893_cm as hostile  # noqa: E402


D = 6_999_893
T_MIN = 50
T_MAX = 600
WINNER = 219
RUNNER_UP = 217
ALPHA_LOCK = Decimal("0.49368416")
C_LOWER = Fraction(11_978, 10_863)
C_UPPER = Fraction(71_603, 64_935)


def configure() -> None:
    hostile.configure_field()
    hostile.core.T_COUNT = WINNER
    hostile.core.GENERATOR_RANK = WINNER - 2
    hostile.core.USEFUL_COUNT = 11_335
    hostile.core.ADVERTISED_ALPHA = ALPHA_LOCK
    hostile.core.endpoint.D = D
    hostile.core.endpoint.C = (D - 1) // 4
    hostile.core.endpoint.T_COUNT = WINNER
    hostile.core.endpoint.GENERATOR_RANK = WINNER - 2
    hostile.core.endpoint.USEFUL_COUNT = 11_335
    hostile.core.endpoint.ALPHA = ALPHA_LOCK
    hostile.core.endpoint.SAFE_C = C_UPPER


def exact_nested_basis() -> tuple[list[tuple[int, int]], list[int], str]:
    """Build a nested C4-aware S-unit basis through the 600th ideal."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,10000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=10000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);if(#L<{T_MAX},error("ideal list too short"));ref=0;for(i=1,{T_MAX},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&gcd(lift(cl[1]),4)==1,ref=i));R=L[ref][3];rclass=lift(bnfisprincipal(b,R,0)[1]);rinv=lift(Mod(rclass,4)^-1);S=vector({T_MIN},i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,4))[2];listput(G,z);for(i=1,{T_MAX},if(i!=ref,P=L[i][3];a=lift(bnfisprincipal(b,P,0)[1]);e=lift(-Mod(a*rinv,4));Jideal=idealmul(nf,P,idealpow(nf,R,e));z=bnfisprincipal(b,Jideal)[2];listput(G,z)));refroot=lift(nfmodpr(nf,Mod(x,nf.pol),R));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_MAX}][3]));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",L[ref][1],",",refroot,",",L[{T_MAX}][1],",",lastroot,",",#G);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "6G"], input=script, text=True, timeout=300
    )
    lines = output.splitlines()
    metadata = next(line for line in lines if line.startswith("META,"))
    assert metadata.startswith(
        "META,1,4,[4],8,[4, 2],[2, 2, 2, 2],1,2,13,6,"
    )
    assert metadata.endswith(f",{T_MAX + 2}")

    pattern = re.compile(
        r"ELEMENT,(-?\d+),(-?\d+),"
        r"\[([01]), ([01]), ([01]), ([01])\]"
    )
    elements: list[tuple[int, int]] = []
    columns: list[int] = []
    for line in lines:
        match = pattern.fullmatch(line)
        if match:
            elements.append(tuple(map(int, match.group(1, 2))))
            columns.append(
                sum(int(match.group(3 + bit)) << bit for bit in range(4))
            )
    assert len(elements) == T_MAX + 2 == len(columns)
    return elements, columns, metadata


def exact_rank_and_gs_audit() -> tuple[int, int, int]:
    elements, pari_columns, metadata = exact_nested_basis()
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = hostile.core.independent_local_rows(elements)
    assert hostile.core.gf2_rank(pari_rows) == 4
    assert hostile.core.gf2_rank(independent_rows) == 4
    assert hostile.core.gf2_rank(pari_rows + independent_rows) == 4

    first_full = next(
        count
        for count in range(1, T_MAX + 1)
        if hostile.core.gf2_rank(
            [row & ((1 << (count + 2)) - 1) for row in independent_rows]
        )
        == 4
    )
    ranks = []
    for count in range(T_MIN, T_MAX + 1):
        width = count + 2
        rank = hostile.core.gf2_rank(
            [row & ((1 << width) - 1) for row in independent_rows]
        )
        ranks.append(rank)
        generator_rank = width - rank
        assert rank == 4 and generator_rank == count - 2
        maximum_relations = (generator_rank * generator_rank - 1) // 4
        useful_count = maximum_relations - (generator_rank + 1) - count
        assert useful_count > 0
        point = Fraction(2, generator_rank)
        assert (
            1
            - generator_rank * point
            + maximum_relations * point * point
        ) < 0
    assert "[4]" in metadata and set(ranks) == {4}
    return min(ranks), max(ranks), first_full


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


def evaluate(
    log_rd: Decimal,
    frontier,
    packing_constant: Fraction,
    anchor: Decimal,
):
    endpoint = hostile.core.endpoint
    constant = Decimal(packing_constant.numerator) / Decimal(
        packing_constant.denominator
    )
    output = []
    for endpoint_number in (1, 2):
        scale = Decimal(endpoint_number)
        w = scale * anchor
        value, index, fraction, slope = endpoint.fast_envelope(
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
        margin = value - rhs - endpoint.EPSILON
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
    endpoint = hostile.core.endpoint
    generator_rank = count - 2
    useful_count = (
        (generator_rank * generator_rank - 1) // 4
        - (generator_rank + 1)
        - count
    )
    ramified = ideals[:count]
    useful = ideals[count : count + useful_count]
    log_rd, frontier, maximum_omitted = endpoint.prepare_endpoint_data(
        ramified, useful
    )

    low = Decimal("30000")
    high = Decimal("50000")

    def difference(anchor: Decimal) -> Decimal:
        records = evaluate(log_rd, frontier, constant, anchor)
        return records[0][0] - records[1][0]

    low_difference = difference(low)
    assert low_difference * difference(high) < 0
    for _ in range(130):
        middle = (low + high) / 2
        middle_difference = difference(middle)
        if low_difference * middle_difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = middle_difference
    anchor = (low + high) / 2
    records = evaluate(log_rd, frontier, constant, anchor)
    assert abs(records[0][0] - records[1][0]) < Decimal("1e-35")
    assert records[0][1] > Decimal("0.004")
    assert records[1][1] < Decimal("-0.012")
    assert maximum_omitted < min(record[2] for record in records)
    return generator_rank, useful_count, anchor, records, maximum_omitted


def run_broad_companion() -> str:
    source = Path(__file__).with_suffix(".cpp")
    compiler = shutil.which("c++")
    if compiler is None:
        raise RuntimeError("a C++17 compiler is required")
    with tempfile.TemporaryDirectory(prefix="verify_6999893_prefix_") as folder:
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
    assert "2 T=217 d=215 N=11123" in output
    return output


def main() -> None:
    getcontext().prec = 100
    configure()
    packing_constant_audit()
    ray_data = exact_rank_and_gs_audit()
    broad_output = run_broad_companion()

    arithmetic = hostile.core.elementary
    primes = arithmetic.prime_sieve(180_000)
    ideals = arithmetic.prime_ideals(primes, 180_000)
    assert ideals[WINNER - 1] == (1_063, 1_063, "split", 335)
    runner = equal_endpoint_certificate(ideals, RUNNER_UP, C_LOWER)
    winner = equal_endpoint_certificate(ideals, WINNER, C_UPPER)
    assert runner[0:2] == (215, 11_123)
    assert winner[0:2] == (217, 11_335)
    assert ideals[WINNER : WINNER + 11_335][-1] == (
        124_951,
        124_951,
        "split",
        98_332,
    )
    assert max(record[0] for record in runner[3]) < Decimal("-0.001")
    assert min(record[0] for record in winner[3]) > Decimal("0.0001")

    print(broad_output, end="")
    print("exact ray ranks / first full prefix:", ray_data)
    print("runner T=217 / d / N / anchor:", *runner[:3])
    print("runner favorable-lower-C records:", runner[3])
    print("winner T=219 / d / N / anchor:", *winner[:3])
    print("winner adverse-upper-C records:", winner[3])
    print("D=6999893 broad prefix-count lock: CERTIFIED")


if __name__ == "__main__":
    main()
