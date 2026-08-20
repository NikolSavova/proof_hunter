#!/usr/bin/env python3
"""Exact certificate for the CM/Eisenstein Q(sqrt(6999893)) record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_cm_eisenstein_real_quadratic_43133 as elementary  # noqa: E402
import verify_hostile_quadratic2278757_cm as audit  # noqa: E402


D = 6_999_893
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 219
GENERATOR_RANK = 217
USEFUL_COUNT = 11_335
ADVERTISED_ALPHA = Decimal("0.49368416")
OLD_RECORD_ALPHA = Decimal("0.49368647")
SAFE_CM_CONSTANT = Fraction(71_603, 64_935)


def configure_shared_arithmetic() -> None:
    audit.D = D
    audit.OMEGA_CONSTANT = OMEGA_CONSTANT
    audit.T_COUNT = T_COUNT
    audit.GENERATOR_RANK = GENERATOR_RANK
    audit.USEFUL_COUNT = USEFUL_COUNT
    audit.ADVERTISED_ALPHA = ADVERTISED_ALPHA
    audit.OLD_RECORD_ALPHA = OLD_RECORD_ALPHA
    audit.SAFE_C = SAFE_CM_CONSTANT
    audit.configure_shared_arithmetic()


def exact_cyclic_four_basis(
) -> tuple[list[tuple[int, int]], list[int], tuple[int, ...]]:
    """Construct a direct S-unit squareclass basis for the cyclic C4 field."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    # Choose a selected ideal R whose class generates C4.  A generator of
    # R^4 supplies the even-valuation class.  For every P != R of class c,
    # multiply P by R^e with c+e[R]=0 in C4, and take the resulting principal
    # generator.  These T elements and the two global units give the full
    # T+2 dimensional S-unit squareclass basis.
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;T={T_COUNT};b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;g=0;for(i=1,T,cl=lift(bnfisprincipal(b,L[i][3],0)[1]);if(ref==0&&gcd(cl,4)==1,ref=i;g=cl));R=L[ref][3];S=vector(T,i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,4))[2];listput(G,z);cnt=vector(4);for(i=1,T,if(i!=ref,P=L[i][3];cl=lift(bnfisprincipal(b,P,0)[1]);cnt[cl+1]++;e=lift(Mod(-cl*g,4));J=if(e==0,P,idealmul(nf,P,idealpow(nf,R,e)));z=bnfisprincipal(b,J)[2];listput(G,z)));M=Mat(vector(#G,i,ideallog(nf,G[i],bid)));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",#su[5][2],",",ref,",",g,",",L[ref][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),R)),",",cnt,",",L[T][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),L[T][3])),",",#G,",",matrank(Mod(M,2)),",",#G-matrank(Mod(M,2)));for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    expected = (
        "META,1,4,[4],8,[4, 2],[2, 2, 2, 2],1,0,2,1,13,6,"
        "[57, 54, 52, 55],1063,335,221,4,217"
    )
    assert expected in lines

    pattern = re.compile(
        r"ELEMENT,(-?\d+),(-?\d+),"
        r"\[([01]), ([01]), ([01]), ([01])\]"
    )
    elements: list[tuple[int, int]] = []
    columns: list[int] = []
    for line in lines:
        match = pattern.fullmatch(line)
        if not match:
            continue
        elements.append(tuple(map(int, match.group(1, 2))))
        columns.append(
            sum(int(match.group(3 + bit)) << bit for bit in range(4))
        )
    assert len(elements) == T_COUNT + 2 == len(columns)
    metadata = (1, 4, 8, 1, 2, 13, 6, 1063, 335, 221, 4, 217)
    return elements, columns, metadata


def main() -> None:
    getcontext().prec = 100
    configure_shared_arithmetic()

    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    fifth = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert (
        2 * sqrt_three_upper / Fraction(333, 106) == SAFE_CM_CONSTANT
    )

    primes = elementary.prime_sieve(180_000)
    assert D == 31 * 349 * 647
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = elementary.prime_ideals(primes, 180_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_063, 1_063, "split", 335)

    elements, pari_columns, metadata = exact_cyclic_four_basis()
    assert metadata == (1, 4, 8, 1, 2, 13, 6, 1063, 335, 221, 4, 217)
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = audit.independent_local_rows(elements)
    assert audit.gf2_rank(pari_rows) == 4 == audit.gf2_rank(independent_rows)
    assert audit.gf2_rank(pari_rows + independent_rows) == 4
    kernel = audit.nullspace_basis(independent_rows, len(elements))
    assert len(kernel) == GENERATOR_RANK

    useful, rejected = audit.useful_scan(
        ideals, elements, independent_rows, kernel
    )
    assert not rejected
    assert useful[-1] == (124_951, 124_951, "split", 98_332)

    relation_bound = (GENERATOR_RANK + 1) + T_COUNT + USEFUL_COUNT
    assert relation_bound == 11_772
    assert 4 * relation_bound == GENERATOR_RANK**2 - 1

    outputs = audit.endpoint_audit(ramified, useful)
    result = outputs[-1]
    print("PARI BNF / C4 class / narrow / localized class: PASS")
    print("T / d / relations:", T_COUNT, GENERATOR_RANK, relation_bound)
    print("last T ideal:", ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("threshold / anchor:", result[0], result[1])
    print("log real-tower root discriminant:", result[3])
    print("100-digit endpoint margins:", *(record[0] for record in outputs[0][2]))
    print("150-digit endpoint margins:", *(record[0] for record in result[2]))
    print("maximum omitted slope:", result[4])
    print("fixed-anchor threshold brackets:", *result[5])
    print("CM quadratic-6999893 F_2(n) << n^0.49368416: CERTIFIED")


if __name__ == "__main__":
    main()
