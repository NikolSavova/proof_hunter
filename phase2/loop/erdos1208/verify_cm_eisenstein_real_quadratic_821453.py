#!/usr/bin/env python3
"""Certificate for the CM/Eisenstein Q(sqrt(821453)) record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess

import verify_cm_eisenstein_real_quadratic_43133 as common


FIELD_DISCRIMINANT = 821_453
OMEGA_CONSTANT = (FIELD_DISCRIMINANT - 1) // 4
RAMIFIED_IDEAL_COUNT = 219
SAFE_GENERATOR_RANK = 217
USEFUL_IDEAL_COUNT = 11_335
ALPHA = Decimal(49_369_313) / Decimal(100_000_000)  # 0.49369313
W0 = Decimal("40752.95")

# The imported arithmetic functions read their defining module's globals.
common.FIELD_DISCRIMINANT = FIELD_DISCRIMINANT
common.OMEGA_CONSTANT = OMEGA_CONSTANT
common.RAMIFIED_IDEAL_COUNT = RAMIFIED_IDEAL_COUNT
common.SAFE_GENERATOR_RANK = SAFE_GENERATOR_RANK
common.USEFUL_IDEAL_COUNT = USEFUL_IDEAL_COUNT
common.ALPHA = ALPHA
common.W0 = W0


def exact_s_units() -> tuple[list[tuple[int, int]], tuple[int, ...]]:
    """Return exact fundamental S-units and certified BNF/ray metadata."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    script = rf"""D={FIELD_DISCRIMINANT};c=(D-1)/4;bnf=bnfinit(x^2-x-c,1);cert=bnfcertify(bnf);nf=bnf.nf;
ideals=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(ideals,[Q,p,dec[i]]))));
ideals=vecsort(Vec(ideals),[1,2]);S=ideals[1..{RAMIFIED_IDEAL_COUNT}];units=bnfunits(bnf,vector(#S,i,S[i][3]));bid=idealstar(nf,[4,[1,1]],1,2);mm=Mat(vector(#units[1],i,ideallog(nf,units[1][i],bid)));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),S[#S][3]));
print("META,",cert,",",bnf.no,",",#units[1],",",matrank(Mod(mm,2)),",",#units[1]-matrank(Mod(mm,2)),",",S[#S][1],",",lastroot);
for(j=1,#units[1],z=nffactorback(nf,units[1][j]);if(type(z)=="t_INT",print(z,",0"),print(z[1],",",z[2])));
"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "2G"], input=script, text=True, timeout=90
    )
    lines = output.splitlines()
    metadata = tuple(
        map(
            int,
            next(line for line in lines if line.startswith("META,")).split(",")[
                1:
            ],
        )
    )
    elements = [
        tuple(map(int, line.split(",")))
        for line in lines
        if re.fullmatch(r"-?\d+,-?\d+", line)
    ]
    return elements, metadata


def main() -> None:
    getcontext().prec = 90
    sqrt_three_upper = Fraction(1_351, 780)
    assert sqrt_three_upper * sqrt_three_upper > 3
    x = Fraction(1, 5)
    atan_fifth_lower = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(4)
    )
    pi_lower = 16 * atan_fifth_lower - 4 * Fraction(1, 239)
    assert pi_lower > Fraction(333, 106)
    assert (
        2 * sqrt_three_upper / Fraction(333, 106)
        == common.PACKING_CONSTANT_FRACTION
    )

    primes = common.prime_sieve(180_000)
    assert FIELD_DISCRIMINANT % 4 == 1
    assert FIELD_DISCRIMINANT % 8 == 5
    assert 1 + 4 * OMEGA_CONSTANT == FIELD_DISCRIMINANT
    # A positive D congruent to 1 mod 4 is a fundamental discriminant here
    # exactly when it is squarefree.  D need not itself be prime.
    assert all(
        FIELD_DISCRIMINANT % (p * p)
        for p in primes
        if p * p <= FIELD_DISCRIMINANT
    )

    ideals = common.prime_ideals(primes, 180_000)
    ramified_ideals = ideals[:RAMIFIED_IDEAL_COUNT]
    assert ramified_ideals[-1] == (1_213, 1_213, "split", 395)

    s_units, metadata = exact_s_units()
    # cert, class number, S-unit count, ray-square rank, kernel rank,
    # final T norm, and omega residue at that prime.
    assert metadata == (1, 1, 221, 4, 217, 1_213, 395)
    assert len(s_units) == 221

    # Independently reconstruct the four sign/square-mod-4 constraints.
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if common.norm((a, b)) % 2
    ]

    def multiply_mod_four(
        left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        product = common.multiply(left, right)
        return product[0] % 4, product[1] % 4

    squares = frozenset(
        multiply_mod_four(unit, unit) for unit in units_mod_four
    )
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units_mod_four:
        coset = frozenset(
            multiply_mod_four(unit, square) for square in squares
        )
        if coset not in cosets:
            cosets.append(coset)
    assert len(units_mod_four) == 12
    assert len(squares) == 3 and len(cosets) == 4

    def coset_index(element: tuple[int, int]) -> int:
        residue = element[0] % 4, element[1] % 4
        return next(index for index, coset in enumerate(cosets) if residue in coset)

    identity = cosets.index(squares)
    nonidentity = [index for index in range(4) if index != identity]
    bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    last_index = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert last_index == nonidentity[2]
    bits[last_index] = 3

    columns = []
    for element in s_units:
        signs = common.negative_at_embedding(element, False)
        signs |= common.negative_at_embedding(element, True) << 1
        columns.append(signs | (bits[coset_index(element)] << 2))
    constraint_rows = [
        sum(((column >> bit) & 1) << index for index, column in enumerate(columns))
        for bit in range(4)
    ]
    assert common.gf2_rank(constraint_rows) == 4
    assert len(s_units) - 4 == SAFE_GENERATOR_RANK

    # Exact mod-3 useful-prime scan on the full Kummer kernel.  A functional
    # is nonzero on ker(C) iff appending it increases the row rank of C.
    useful_ideals: list[tuple[int, int, str, int | None]] = []
    rejected_ideals: list[tuple[int, int, str, int | None]] = []
    for ideal in ideals[RAMIFIED_IDEAL_COUNT:]:
        norm_q, p, _, root = ideal
        if p == 3:
            continue
        useful = True
        if norm_q % 3 == 2:
            assert norm_q == p and root is not None
            functional = 0
            for index, (a, b) in enumerate(s_units):
                residue = (a + b * root) % p
                assert residue
                if pow(residue, (p - 1) // 2, p) == p - 1:
                    functional |= 1 << index
            useful = (
                common.gf2_rank(constraint_rows + [functional]) > 4
            )
        if useful:
            useful_ideals.append(ideal)
        else:
            rejected_ideals.append(ideal)
        if len(useful_ideals) == USEFUL_IDEAL_COUNT:
            break
    assert len(useful_ideals) == USEFUL_IDEAL_COUNT
    assert not rejected_ideals
    assert useful_ideals[-1] == (122_527, 122_527, "split", 3_683)

    relation_bound = (
        SAFE_GENERATOR_RANK
        + 1
        + RAMIFIED_IDEAL_COUNT
        + USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 11_772
    assert 4 * relation_bound == SAFE_GENERATOR_RANK**2 - 1

    outputs = [
        common.endpoint_certificate(ramified_ideals, useful_ideals, precision)
        for precision in (90, 150)
    ]
    result = outputs[-1]
    print("PARI BNF / class-number certification: PASS")
    print("T / last:", len(ramified_ideals), ramified_ideals[-1])
    print("S-units / ray rank / d:", metadata[2], metadata[3], metadata[4])
    print(
        "useful / rejected / last:",
        len(useful_ideals),
        len(rejected_ideals),
        useful_ideals[-1],
    )
    print("generator / relations:", SAFE_GENERATOR_RANK, relation_bound)
    print("safe CM constant:", result[0])
    print("log real-tower root discriminant:", result[1])
    print("left / right:", result[2], result[3])
    print("right / maximum fourth slopes:", result[3][3], result[4])
    print("90-digit margins:", *outputs[0][5])
    print("150-digit margins:", *result[5])
    print("fixed-anchor threshold brackets:", *result[6])
    print("CM quadratic-821453 F_2(n) << n^0.49369313: CERTIFIED")


if __name__ == "__main__":
    main()
