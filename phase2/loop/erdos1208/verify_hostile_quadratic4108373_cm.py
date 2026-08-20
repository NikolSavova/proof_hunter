#!/usr/bin/env python3
"""Independent hostile certificate for the D=4108373 CM record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_hostile_quadratic2278757_cm as core  # noqa: E402


D = 4_108_373
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 217
GENERATOR_RANK = 215
USEFUL_COUNT = 11_123
ADVERTISED_ALPHA = Decimal("0.49368647")
OLD_RECORD_ALPHA = Decimal("0.49368759")
SAFE_C = Fraction(71_603, 64_935)


def configure() -> None:
    core.D = D
    core.OMEGA_CONSTANT = OMEGA_CONSTANT
    core.T_COUNT = T_COUNT
    core.GENERATOR_RANK = GENERATOR_RANK
    core.USEFUL_COUNT = USEFUL_COUNT
    core.ADVERTISED_ALPHA = ADVERTISED_ALPHA
    core.OLD_RECORD_ALPHA = OLD_RECORD_ALPHA
    core.SAFE_C = SAFE_C
    core.configure_shared_arithmetic()
    core.endpoint.ALPHA = ADVERTISED_ALPHA


def exact_s_unit_basis():
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,{T_COUNT},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&cl[1]!=0,ref=i));R=L[ref][3];S=vector({T_COUNT},i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,2))[2];listput(G,z);for(i=1,{T_COUNT},if(i!=ref,P=L[i][3];cl=bnfisprincipal(b,P,0);if(cl[1]==0,z=bnfisprincipal(b,P)[2],z=bnfisprincipal(b,idealmul(nf,P,R))[2]);listput(G,z)));refroot=lift(nfmodpr(nf,Mod(x,nf.pol),R));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_COUNT}][3]));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",L[ref][1],",",refroot,",",L[{T_COUNT}][1],",",lastroot,",",#G);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    assert (
        "META,1,2,[2],4,[2, 2],[2, 2, 2, 2],1,"
        "2,11,4,1117,1020,219"
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
    assert len(elements) == T_COUNT + 2 == len(columns)
    return elements, columns


def main() -> None:
    getcontext().prec = 100
    configure()

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

    primes = core.elementary.prime_sieve(220_000)
    assert D == 17 * 67 * 3_607
    assert all(prime in primes for prime in (17, 67, 3_607))
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = core.elementary.prime_ideals(primes, 220_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_117, 1_117, "split", 1_020)

    elements, pari_columns = exact_s_unit_basis()
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
    kernel = core.nullspace_basis(independent_rows, len(elements))
    assert len(kernel) == GENERATOR_RANK

    useful, rejected = core.useful_scan(
        ideals, elements, independent_rows, kernel
    )
    assert len(useful) == USEFUL_COUNT
    assert not rejected

    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert relation_bound == 11_556
    assert 4 * relation_bound == GENERATOR_RANK * GENERATOR_RANK - 1

    endpoint_outputs = core.endpoint_audit(ramified, useful)
    threshold, anchor, records, log_rd, omitted, brackets = endpoint_outputs[-1]
    print("PARI class/S-class/direct S-unit basis: CERTIFIED")
    print("T / last:", T_COUNT, ramified[-1])
    print("S-unit columns / ray rank / kernel:", len(elements), 4, len(kernel))
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("generator / relation bound:", GENERATOR_RANK, relation_bound)
    print("log root discriminant:", log_rd)
    print("equal-endpoint threshold / anchor:", threshold, anchor)
    print("records at advertised alpha:", records)
    print("maximum omitted slope:", omitted)
    print("fixed-anchor roots:", brackets)
    print("100/150-digit margins:")
    for output in endpoint_outputs:
        print(" ", output[2][0][0], output[2][1][0])
    print("D=4108373 F_2(n) << n^0.49368647: CERTIFIED")


if __name__ == "__main__":
    main()
