#!/usr/bin/env python3
"""Independent hostile audit of the D=6999893 CM candidate."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_hostile_quadratic2278757_cm as core  # noqa: E402


D = 6_999_893
OMEGA_CONSTANT = (D - 1) // 4
T_MIN = 215
T_MAX = 227
PRELIMINARY_T = 221
WINNER_T = 219
WINNER_D = 217
WINNER_N = 11_335
OLD_RECORD_ALPHA = Decimal("0.49368647")
ADVERTISED_ALPHA = Decimal("0.49368416")
SAFE_C = Fraction(71_603, 64_935)


@dataclass(frozen=True)
class Result:
    count: int
    generator_rank: int
    useful_count: int
    last_t: tuple[int, int, str, int | None]
    last_useful: tuple[int, int, str, int | None]
    rejections: int
    threshold: Decimal
    anchor: Decimal
    log_rd: Decimal


def configure_field() -> None:
    core.D = D
    core.OMEGA_CONSTANT = OMEGA_CONSTANT
    core.SAFE_C = SAFE_C
    core.elementary.FIELD_DISCRIMINANT = D
    core.elementary.OMEGA_CONSTANT = OMEGA_CONSTANT
    core.endpoint.D = D
    core.endpoint.C = OMEGA_CONSTANT
    core.endpoint.SAFE_C = SAFE_C
    core.endpoint.ALPHA = OLD_RECORD_ALPHA


def exact_nested_basis():
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,6000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=6000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,{T_MAX},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&gcd(lift(cl[1]),4)==1,ref=i));R=L[ref][3];rclass=lift(bnfisprincipal(b,R,0)[1]);rinv=lift(Mod(rclass,4)^-1);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,4))[2];listput(G,z);for(i=1,{T_MAX},if(i!=ref,P=L[i][3];a=lift(bnfisprincipal(b,P,0)[1]);e=lift(-Mod(a*rinv,4));Jideal=idealmul(nf,P,idealpow(nf,R,e));z=bnfisprincipal(b,Jideal)[2];listput(G,z)));S=vector({T_MIN},i,L[i][3]);su=bnfsunit(b,S);refroot=lift(nfmodpr(nf,Mod(x,nf.pol),R));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_MAX}][3]));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",L[ref][1],",",refroot,",",L[{T_MAX}][1],",",lastroot,",",#G);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    assert (
        "META,1,4,[4],8,[4, 2],[2, 2, 2, 2],1,"
        "2,13,6,1117,141,229"
    ) in lines
    pattern = re.compile(
        r"ELEMENT,(-?\d+),(-?\d+),"
        r"\[([01]), ([01]), ([01]), ([01])\]"
    )
    elements = []
    columns = []
    for line in lines:
        match = pattern.fullmatch(line)
        if match:
            elements.append(tuple(map(int, match.group(1, 2))))
            columns.append(
                sum(int(match.group(3 + bit)) << bit for bit in range(4))
            )
    assert len(elements) == T_MAX + 2 == len(columns)
    return elements, columns


def scan_counts(ideals, elements, local_rows):
    outputs = []
    for count in range(T_MIN, T_MAX + 1):
        width = count + 2
        mask = (1 << width) - 1
        rows = [row & mask for row in local_rows]
        assert core.gf2_rank(rows) == 4
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        kernel = (
            core.nullspace_basis(rows, width)
            if count == WINNER_T
            else None
        )
        core.T_COUNT = count
        core.GENERATOR_RANK = generator_rank
        core.USEFUL_COUNT = useful_count
        useful, rejected = core.useful_scan(
            ideals, elements[:width], rows, kernel or []
        ) if kernel is not None else _rank_only_scan(
            ideals, count, useful_count, elements[:width], rows
        )
        core.endpoint.T_COUNT = count
        core.endpoint.GENERATOR_RANK = generator_rank
        core.endpoint.USEFUL_COUNT = useful_count
        threshold, anchor, _, log_rd = core.endpoint.optimize_diagnostic(
            ideals[:count], useful
        )
        outputs.append(
            Result(
                count,
                generator_rank,
                useful_count,
                ideals[count - 1],
                useful[-1],
                len(rejected),
                threshold,
                anchor,
                log_rd,
            )
        )
    return outputs


def _rank_only_scan(ideals, count, useful_count, elements, rows):
    useful = []
    rejected = []
    for ideal in ideals[count:]:
        norm_q, prime, _, root = ideal
        if prime == 3:
            continue
        accepted = True
        if norm_q % 3 == 2:
            assert norm_q == prime and root is not None
            functional = 0
            for index, (a, b) in enumerate(elements):
                residue = (a + b * root) % prime
                assert residue
                if pow(residue, (prime - 1) // 2, prime) == prime - 1:
                    functional |= 1 << index
            accepted = core.gf2_rank(rows + [functional]) > 4
        (useful if accepted else rejected).append(ideal)
        if len(useful) == useful_count:
            return useful, rejected
    raise AssertionError("useful universe exhausted")


def main() -> None:
    getcontext().prec = 100
    configure_field()
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

    primes = core.elementary.prime_sieve(230_000)
    assert D == 31 * 349 * 647
    assert all(prime in primes for prime in (31, 349, 647))
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = core.elementary.prime_ideals(primes, 230_000)
    assert ideals[PRELIMINARY_T - 1] == (1_069, 1_069, "split", 5)

    elements, pari_columns = exact_nested_basis()
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = core.independent_local_rows(elements)
    assert core.gf2_rank(pari_rows) == 4 == core.gf2_rank(independent_rows)
    assert core.gf2_rank(pari_rows + independent_rows) == 4

    outputs = scan_counts(ideals, elements, independent_rows)
    winner = min(outputs, key=lambda result: result.threshold)
    assert winner.count == WINNER_T
    assert winner.generator_rank == WINNER_D
    assert winner.useful_count == WINNER_N
    assert winner.rejections == 0
    assert winner.last_useful == (124_951, 124_951, "split", 98_332)
    assert all(output.rejections == 0 for output in outputs)

    winner_width = WINNER_T + 2
    winner_mask = (1 << winner_width) - 1
    winner_rows = [row & winner_mask for row in independent_rows]
    winner_kernel = core.nullspace_basis(winner_rows, winner_width)
    assert len(winner_kernel) == WINNER_D
    core.T_COUNT = WINNER_T
    core.GENERATOR_RANK = WINNER_D
    core.USEFUL_COUNT = WINNER_N
    winner_useful, winner_rejected = core.useful_scan(
        ideals, elements[:winner_width], winner_rows, winner_kernel
    )
    assert not winner_rejected and winner_useful[-1] == winner.last_useful

    relation_bound = WINNER_D + 1 + WINNER_T + WINNER_N
    assert relation_bound == 11_772
    assert 4 * relation_bound == WINNER_D * WINNER_D - 1
    core.ADVERTISED_ALPHA = ADVERTISED_ALPHA
    core.OLD_RECORD_ALPHA = OLD_RECORD_ALPHA
    core.endpoint.ALPHA = ADVERTISED_ALPHA
    core.endpoint.T_COUNT = WINNER_T
    core.endpoint.GENERATOR_RANK = WINNER_D
    core.endpoint.USEFUL_COUNT = WINNER_N
    endpoint_outputs = core.endpoint_audit(
        ideals[:WINNER_T], winner_useful
    )
    for output in outputs:
        print(output)
    print("winner:", winner)
    print("generator / relations:", WINNER_D, relation_bound)
    print("100/150-digit final endpoint outputs:")
    for output in endpoint_outputs:
        print(output)
    print("D=6999893 F_2(n) << n^0.49368416: CERTIFIED")


if __name__ == "__main__":
    main()
