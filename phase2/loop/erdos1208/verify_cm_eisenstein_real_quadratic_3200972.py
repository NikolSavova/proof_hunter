#!/usr/bin/env python3
"""Exact certificate for the CM/Eisenstein Q(sqrt(800243)) record.

The field discriminant is 3,200,972.  PARI certifies the class and ray
arithmetic, while Python independently reconstructs the four local rows,
tests every useful prime, checks the GS equality, and audits the all-depth
product-disk endpoint at 100 and 150 decimal digits.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_cm_eisenstein_real_quadratic_43133 as elementary  # noqa: E402
import verify_hostile_quadratic821453_cm as endpoint  # noqa: E402


FIELD_DISCRIMINANT = 3_200_972
RADICAND = 800_243
RAMIFIED_IDEAL_COUNT = 215
SAFE_GENERATOR_RANK = 213
USEFUL_IDEAL_COUNT = 10_913
ADVERTISED_ALPHA = Decimal("0.49368759")
PREVIOUS_ALPHA = Decimal("0.49368818")
SAFE_CM_CONSTANT = Fraction(71_603, 64_935)


def gf2_rank(rows: list[int]) -> int:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def norm(element: tuple[int, int]) -> int:
    """Norm of a+b sqrt(800243) in the integral basis (1,sqrt(d))."""
    a, b = element
    return a * a - RADICAND * b * b


def multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    a, b = left
    x, y = right
    return a * x + RADICAND * b * y, a * y + b * x


def negative_at_embedding(
    element: tuple[int, int], conjugate_place: bool
) -> int:
    a, b = element
    radical_coefficient = -b if conjugate_place else b
    if a >= 0 and radical_coefficient >= 0:
        return 0
    if a <= 0 and radical_coefficient <= 0:
        return 1
    rational_square = a * a
    radical_square = radical_coefficient * radical_coefficient * RADICAND
    assert rational_square != radical_square
    if a > 0:
        return int(rational_square < radical_square)
    return int(radical_square < rational_square)


def prime_ideals(
    primes: list[int], norm_limit: int
) -> list[tuple[int, int, str, int | None]]:
    ideals: list[tuple[int, int, str, int | None]] = []
    for prime in primes:
        if prime == 2 or prime > norm_limit:
            continue
        if FIELD_DISCRIMINANT % prime == 0:
            ideals.append((prime, prime, "ramified", 0))
            continue
        symbol = pow(RADICAND % prime, (prime - 1) // 2, prime)
        if symbol == 1:
            root = elementary.tonelli_shanks(RADICAND, prime)
            roots = sorted({root, -root % prime})
            assert len(roots) == 2
            ideals.extend(
                (prime, prime, "split", value) for value in roots
            )
        else:
            assert symbol == prime - 1
            if prime * prime <= norm_limit:
                ideals.append((prime * prime, prime, "inert", None))
    ideals.sort(
        key=lambda row: (
            row[0], row[1], row[2],
            row[3] if row[3] is not None else -1,
        )
    )
    return ideals


def exact_odd_class_basis(
) -> tuple[list[tuple[int, int]], list[int], tuple[int, ...]]:
    """Return a direct S-unit squareclass basis and its ray columns.

    The class group has odd order 15.  For each selected prime ideal P, the
    generator of P^ord([P]) has an odd P-valuation and zero valuation at the
    other selected primes.  Together with the two global-unit columns these
    215 diagonal odd-valuation elements form a basis modulo squares.
    """
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    script = rf"""default(nbthreads,1);default(realprecision,3000);d={RADICAND};T={RAMIFIED_IDEAL_COUNT};b=bnfinit(x^2-d,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);S=vector(T,i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));cnt=vector(4);ords=[1,3,5,15];for(i=1,T,P=L[i][3];cl=bnfisprincipal(b,P,0)[1];ord=if(cl==0,1,15/gcd(15,lift(cl)));cnt[vecsearch(ords,ord)]++;z=bnfisprincipal(b,idealpow(nf,P,ord))[2];listput(G,z));bid=idealstar(nf,[4,[1,1]],1,2);M=Mat(vector(#G,i,ideallog(nf,G[i],bid)));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",#su[5][2],",",cnt,",",#G,",",matrank(Mod(M,2)),",",#G-matrank(Mod(M,2)),",",L[T][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),L[T][3])));for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "2G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    expected = (
        "META,1,15,[15],30,[30],[2, 2, 2, 2],1,0,"
        "[17, 20, 54, 124],217,4,213,1091,605"
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
    assert len(elements) == RAMIFIED_IDEAL_COUNT + 2 == len(columns)
    metadata = (1, 15, 30, 1, 217, 4, 213, 1091, 605)
    return elements, columns, metadata


def independent_local_rows(elements: list[tuple[int, int]]) -> list[int]:
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if norm((a, b)) % 2
    ]

    def multiply_mod_four(
        left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        product = multiply(left, right)
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
    assert len(units_mod_four) == 8
    assert len(squares) == 2 and len(cosets) == 4

    def coset_index(element: tuple[int, int]) -> int:
        residue = element[0] % 4, element[1] % 4
        return next(index for index, coset in enumerate(cosets) if residue in coset)

    identity = cosets.index(squares)
    nonidentity = [index for index in range(4) if index != identity]
    bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    representatives = [next(iter(coset)) for coset in cosets]
    fourth = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert fourth == nonidentity[2]
    bits[fourth] = 3

    columns = []
    for element in elements:
        signs = negative_at_embedding(element, False)
        signs |= negative_at_embedding(element, True) << 1
        columns.append(signs | (bits[coset_index(element)] << 2))
    return [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(columns)
        )
        for bit in range(4)
    ]


def useful_scan(
    ideals: list[tuple[int, int, str, int | None]],
    elements: list[tuple[int, int]],
    constraint_rows: list[int],
) -> tuple[
    list[tuple[int, int, str, int | None]],
    list[tuple[int, int, str, int | None]],
]:
    useful = []
    rejected = []
    for ideal in ideals[RAMIFIED_IDEAL_COUNT:]:
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
            accepted = gf2_rank(constraint_rows + [functional]) > 4
        (useful if accepted else rejected).append(ideal)
        if len(useful) == USEFUL_IDEAL_COUNT:
            break
    assert len(useful) == USEFUL_IDEAL_COUNT
    return useful, rejected


def endpoint_audit(ramified, useful):
    endpoint.D = FIELD_DISCRIMINANT
    endpoint.T_COUNT = RAMIFIED_IDEAL_COUNT
    endpoint.GENERATOR_RANK = SAFE_GENERATOR_RANK
    endpoint.USEFUL_COUNT = USEFUL_IDEAL_COUNT
    endpoint.SAFE_C = SAFE_CM_CONSTANT
    endpoint.ALPHA = ADVERTISED_ALPHA
    outputs = []
    for precision in (100, 150):
        getcontext().prec = precision
        threshold, anchor, records, log_rd = endpoint.optimize_diagnostic(
            ramified, useful
        )
        prepared_log_rd, frontier, maximum_omitted = (
            endpoint.prepare_endpoint_data(ramified, useful)
        )
        assert prepared_log_rd == log_rd
        assert maximum_omitted < min(record[2] for record in records)
        assert ADVERTISED_ALPHA - Decimal("1e-8") < threshold
        assert threshold < ADVERTISED_ALPHA < PREVIOUS_ALPHA
        assert min(record[0] for record in records) > Decimal("0.0001")
        assert records[0][1] > Decimal("0.001")
        assert records[1][1] < Decimal("-0.001")

        brackets = []
        for endpoint_index in (0, 1):
            low = ADVERTISED_ALPHA - Decimal("1e-8")
            high = ADVERTISED_ALPHA
            assert endpoint.evaluate_prepared(
                log_rd, frontier, low, anchor
            )[endpoint_index][0] < 0
            assert endpoint.evaluate_prepared(
                log_rd, frontier, high, anchor
            )[endpoint_index][0] > 0
            for _ in range(140):
                middle = (low + high) / 2
                if endpoint.evaluate_prepared(
                    log_rd, frontier, middle, anchor
                )[endpoint_index][0] > 0:
                    high = middle
                else:
                    low = middle
            assert high - low < Decimal("1e-45")
            brackets.append((low, high))
        outputs.append(
            (threshold, anchor, records, log_rd, maximum_omitted, brackets)
        )
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-50")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-45")
    return outputs


def main() -> None:
    getcontext().prec = 100
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
    assert FIELD_DISCRIMINANT == 4 * RADICAND
    assert RADICAND % 4 == 3
    assert all(
        RADICAND % (prime * prime)
        for prime in primes
        if prime * prime <= RADICAND
    )
    ideals = prime_ideals(primes, 180_000)
    ramified = ideals[:RAMIFIED_IDEAL_COUNT]
    assert ramified[-1] == (1_091, 1_091, "split", 605)

    elements, pari_columns, metadata = exact_odd_class_basis()
    assert metadata == (1, 15, 30, 1, 217, 4, 213, 1091, 605)
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = independent_local_rows(elements)
    assert gf2_rank(pari_rows) == 4 == gf2_rank(independent_rows)
    assert gf2_rank(pari_rows + independent_rows) == 4
    assert len(elements) - 4 == SAFE_GENERATOR_RANK

    useful, rejected = useful_scan(ideals, elements, independent_rows)
    assert not rejected
    assert useful[-1] == (119_359, 119_359, "split", 113_172)

    relation_bound = (
        SAFE_GENERATOR_RANK + 1
        + RAMIFIED_IDEAL_COUNT
        + USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 11_342
    assert 4 * relation_bound == SAFE_GENERATOR_RANK**2 - 1

    outputs = endpoint_audit(ramified, useful)
    result = outputs[-1]
    print("PARI BNF / class / narrow / localized class: PASS")
    print("T / d / relations:", RAMIFIED_IDEAL_COUNT, SAFE_GENERATOR_RANK, relation_bound)
    print("last T ideal:", ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("threshold / anchor:", result[0], result[1])
    print("log real-tower root discriminant:", result[3])
    print("100-digit endpoint margins:", *(record[0] for record in outputs[0][2]))
    print("150-digit endpoint margins:", *(record[0] for record in result[2]))
    print("maximum omitted slope:", result[4])
    print("fixed-anchor threshold brackets:", *result[5])
    print("CM quadratic-3200972 F_2(n) << n^0.49368759: CERTIFIED")


if __name__ == "__main__":
    main()
