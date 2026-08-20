#!/usr/bin/env python3
"""Exact finite no-go audit for the remaining 5--6m screen candidates.

PARI certifies each BNF, localized class group, compact S-unit basis, and
sign/mod-4 ray rank.  A 100-digit all-useful endpoint computation then gives
every count 205 <= T <= 250 a favorable packing constant and still excludes
the target exponent 0.49368416.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from math import gcd
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_ordinary_cm_next_leaders_exact_no_go as screen  # noqa: E402


T_MIN = 205
T_MAX = 250
ALPHA = Decimal("0.49368416")
C_LOWER = Fraction(11_978, 10_863)


@dataclass(frozen=True)
class Case:
    discriminant: int
    best_t: int
    class_number: int
    class_cyclic: str
    narrow_number: int
    narrow_cyclic: str
    reference_index: int
    reference_norm: int
    expected_best_margin_upper: Decimal

    @property
    def polynomial(self) -> str:
        return f"x^2-x-{(self.discriminant - 1) // 4}"


CASES = (
    Case(
        5_872_397,
        217,
        1,
        "[]",
        1,
        "[]",
        0,
        0,
        Decimal("-0.24"),
    ),
    Case(
        5_182_973,
        207,
        10,
        "[10]",
        20,
        "[10, 2]",
        2,
        11,
        Decimal("-0.35"),
    ),
    Case(
        5_963_613,
        219,
        2,
        "[2]",
        4,
        "[2, 2]",
        1,
        3,
        Decimal("-0.64"),
    ),
)


def trial_factor(number: int) -> list[int]:
    output = []
    candidate = 2
    while candidate * candidate <= number:
        while number % candidate == 0:
            output.append(candidate)
            number //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if number > 1:
        output.append(number)
    return output


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


def exact_localized_rank(case: Case) -> tuple[int, int, int]:
    """Return min/max ray rank and the pre-ray basis size.

    Compact factorizations (bnfisprincipal flag 5) are essential for the
    D=5182973 fundamental unit: expanding it is both unnecessary and huge.
    The helper ``flog`` applies ideallog factor by factor, with exact integer
    exponents, so no numerical unit expansion enters the certificate.
    """
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")

    if case.class_number == 1:
        basis_builder = rf"""ref=0;refnorm=0;rclass=0;U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,U[1][i]));for(i=1,{T_MAX},z=bnfisprincipal(b,L[i][3],5)[2];listput(G,z));"""
    else:
        basis_builder = rf"""H=b.no;ref=0;for(i=1,{T_MAX},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&gcd(lift(cl[1]),H)==1,ref=i));R=L[ref][3];refnorm=L[ref][1];rclass=lift(bnfisprincipal(b,R,0)[1]);rinv=lift(Mod(rclass,H)^-1);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,U[1][i]));z=bnfisprincipal(b,idealpow(nf,R,H),5)[2];listput(G,z);for(i=1,{T_MAX},if(i!=ref,P=L[i][3];a=lift(bnfisprincipal(b,P,0)[1]);e=lift(-Mod(a*rinv,H));J=idealmul(nf,P,idealpow(nf,R,e));z=bnfisprincipal(b,J,5)[2];listput(G,z)));"""

    script = rf"""default(nbthreads,1);D={case.discriminant};b=bnfinit({case.polynomial},1);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);
flog(F)={{my(v=vector(4,i,0));for(j=1,matsize(F)[1],v=v+F[j,2]*concat(Vec(ideallog(nf,F[j,1],bid))));v}};
L=List();forprime(p=3,8000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=8000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);if(#L<{T_MAX},error("ideal list too short"));S=vector({T_MIN},i,L[i][3]);su=bnfsunit(b,S);{basis_builder}Cols=List();for(i=1,#G,listput(Cols,flog(G[i])));M=matrix(4,#G,i,j,Cols[j][i]);print("META,",bnfcertify(b),",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",refnorm,",",rclass,",",#G);for(T={T_MIN},{T_MAX},print("RANK,",T,",",matrank(Mod(M[,1..T+2],2))));
"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "2G"], input=script, text=True, timeout=120
    )
    lines = output.splitlines()
    metadata = next(line for line in lines if line.startswith("META,"))
    expected = (
        f"META,1,{case.class_number},{case.class_cyclic},"
        f"{case.narrow_number},{case.narrow_cyclic},[2, 2, 2, 2],1,"
        f"{case.reference_index},{case.reference_norm},"
    )
    assert metadata.startswith(expected)
    assert metadata.endswith(f",{T_MAX + 2}")
    if case.class_number == 1:
        assert metadata == expected + f"0,{T_MAX + 2}"
    else:
        class_coordinate = int(metadata.split(",")[-2])
        assert gcd(class_coordinate, case.class_number) == 1

    rank_pattern = re.compile(r"RANK,(\d+),(\d+)")
    ranks = [
        tuple(map(int, match.groups()))
        for line in lines
        if (match := rank_pattern.fullmatch(line))
    ]
    assert [count for count, _ in ranks] == list(range(T_MIN, T_MAX + 1))
    assert {rank for _, rank in ranks} == {4}
    return min(rank for _, rank in ranks), max(rank for _, rank in ranks), T_MAX + 2


def endpoint_no_go(case: Case, primes: list[int]):
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
    field_case = screen.FieldCase(
        case.discriminant,
        case.best_t,
        case.class_number,
        case.narrow_number,
        (0, 0, "unused", None),
    )
    ideals = screen.prime_ideals(field_case, primes, 200_000)
    assert len(ideals) > 16_000
    record = screen.optimistic_no_go(field_case, ideals)
    assert record[0] == case.best_t
    assert record[1] < case.expected_best_margin_upper
    return record


def main() -> None:
    getcontext().prec = 100
    packing_constant_audit()
    assert trial_factor(5_872_397) == [5_872_397]
    assert trial_factor(5_182_973) == [59, 107, 821]
    assert trial_factor(5_963_613) == [3, 53, 37_507]
    for case in CASES:
        assert case.discriminant % 4 == 1
        factors = trial_factor(case.discriminant)
        assert len(set(factors)) == len(factors)

    # The endpoint helper is deliberately put in the favorable exclusion
    # regime: all primes useful and C_LOWER < 2sqrt(3)/pi.
    screen.ALPHA = ALPHA
    screen.C_UPPER = Decimal(C_LOWER.numerator) / Decimal(C_LOWER.denominator)
    primes = screen.elementary.prime_sieve(200_000)

    for case in CASES:
        ranks = exact_localized_rank(case)
        endpoint = endpoint_no_go(case, primes)
        print("D / exact ray ranks / basis size:", case.discriminant, ranks)
        print("best favorable all-useful endpoint:", endpoint)
    print("5--6m quadratic candidates exact finite no-go: CERTIFIED")


if __name__ == "__main__":
    main()
