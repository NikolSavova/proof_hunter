#!/usr/bin/env python3
"""Independent hostile audit of the D=3200972 CM candidate."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_hostile_quadratic821453_cm as endpoint  # noqa: E402


D = 3_200_972
RADICAND = 800_243
T_MIN = 211
T_MAX = 221
WINNER_T = 215
WINNER_D = 213
WINNER_N = 10_913
OLD_RECORD_ALPHA = Decimal("0.49368818")
ADVERTISED_ALPHA = Decimal("0.49368759")
SAFE_C = Fraction(71_603, 64_935)


@dataclass(frozen=True)
class CountResult:
    count: int
    generator_rank: int
    useful_count: int
    last_t: tuple[int, int, str, int | None]
    last_useful: tuple[int, int, str, int | None]
    rejections: int
    threshold: Decimal
    anchor: Decimal
    log_rd: Decimal


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            length = (limit - prime * prime) // prime + 1
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * length
    return [value for value in range(2, limit + 1) if sieve[value]]


def tonelli_shanks(value: int, prime: int) -> int:
    value %= prime
    assert value and pow(value, (prime - 1) // 2, prime) == 1
    if prime % 4 == 3:
        return pow(value, (prime + 1) // 4, prime)
    odd = prime - 1
    power = 0
    while odd % 2 == 0:
        odd //= 2
        power += 1
    nonresidue = 2
    while pow(nonresidue, (prime - 1) // 2, prime) != prime - 1:
        nonresidue += 1
    root = pow(value, (odd + 1) // 2, prime)
    test = pow(value, odd, prime)
    multiplier = pow(nonresidue, odd, prime)
    size = power
    while test != 1:
        index = 1
        square = test * test % prime
        while square != 1:
            square = square * square % prime
            index += 1
        correction = pow(multiplier, 1 << (size - index - 1), prime)
        root = root * correction % prime
        test = test * correction * correction % prime
        multiplier = correction * correction % prime
        size = index
    assert root * root % prime == value
    return root


def prime_ideals(primes: list[int], norm_limit: int):
    output: list[tuple[int, int, str, int | None]] = []
    for prime in primes:
        if prime == 2 or prime > norm_limit:
            continue
        if RADICAND % prime == 0:
            output.append((prime, prime, "ramified", 0))
            continue
        symbol = pow(RADICAND % prime, (prime - 1) // 2, prime)
        if symbol == 1:
            root = tonelli_shanks(RADICAND, prime)
            roots = sorted({root, (-root) % prime})
            assert len(roots) == 2
            output.extend((prime, prime, "split", value) for value in roots)
        else:
            assert symbol == prime - 1
            if prime * prime <= norm_limit:
                output.append((prime * prime, prime, "inert", None))
    output.sort(key=lambda row: (row[0], row[1], row[2], row[3] or -1))
    return output


def rowspace_basis(rows: list[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return pivots


def gf2_rank(rows: list[int]) -> int:
    return len(rowspace_basis(rows))


def nullspace_basis(rows: list[int], width: int) -> list[int]:
    pivots = rowspace_basis(rows)
    output = []
    for free in range(width):
        if free in pivots:
            continue
        vector = 1 << free
        for pivot in sorted(pivots):
            if ((pivots[pivot] ^ (1 << pivot)) & vector).bit_count() & 1:
                vector |= 1 << pivot
        assert all(not ((row & vector).bit_count() & 1) for row in rows)
        output.append(vector)
    assert gf2_rank(output) == len(output)
    return output


def exact_nested_s_unit_basis():
    """Construct the nested basis through T_MAX using Cl(E)=C15."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);M={RADICAND};b=bnfinit(x^2-M,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,{T_MAX},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&gcd(lift(cl[1]),15)==1,ref=i));R=L[ref][3];rclass=lift(bnfisprincipal(b,R,0)[1]);rinv=lift(Mod(rclass,15)^-1);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,15))[2];listput(G,z);for(i=1,{T_MAX},if(i!=ref,P=L[i][3];a=lift(bnfisprincipal(b,P,0)[1]);e=lift(-Mod(a*rinv,15));Jideal=idealmul(nf,P,idealpow(nf,R,e));z=bnfisprincipal(b,Jideal)[2];listput(G,z)));refroot=lift(nfmodpr(nf,Mod(x,nf.pol),R));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_MAX}][3]));S=vector({T_MIN},i,L[i][3]);su=bnfsunit(b,S);print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",L[ref][1],",",refroot,",",L[{T_MAX}][1],",",lastroot,",",#G);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    assert (
        "META,1,15,[15],30,[30],[2, 2, 2, 2],1,"
        "6,19,1,1217,862,223"
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


def norm(element: tuple[int, int]) -> int:
    a, b = element
    return a * a - RADICAND * b * b


def multiply(left: tuple[int, int], right: tuple[int, int]):
    a, b = left
    x, y = right
    return a * x + RADICAND * b * y, a * y + b * x


def negative_at_embedding(element: tuple[int, int], conjugate: bool) -> int:
    a, b = element
    radical = -b if conjugate else b
    if a >= 0 and radical >= 0:
        return 0
    if a <= 0 and radical <= 0:
        return 1
    left = a * a
    right = radical * radical * RADICAND
    assert left != right
    if a > 0:
        return int(left < right)
    return int(right < left)


def independent_local_rows(elements: list[tuple[int, int]]) -> list[int]:
    units = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if norm((a, b)) % 2
    ]

    def multiply_mod_four(left, right):
        product = multiply(left, right)
        return product[0] % 4, product[1] % 4

    squares = frozenset(multiply_mod_four(unit, unit) for unit in units)
    cosets: list[frozenset[tuple[int, int]]] = []
    for unit in units:
        coset = frozenset(multiply_mod_four(unit, square) for square in squares)
        if coset not in cosets:
            cosets.append(coset)
    assert len(units) == 8 and len(squares) == 2 and len(cosets) == 4
    identity = cosets.index(squares)
    nonidentity = [index for index in range(4) if index != identity]
    representatives = [next(iter(coset)) for coset in cosets]

    def coset_index(element):
        residue = element[0] % 4, element[1] % 4
        return next(index for index, coset in enumerate(cosets) if residue in coset)

    bits = {identity: 0, nonidentity[0]: 1, nonidentity[1]: 2}
    final = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert final == nonidentity[2]
    bits[final] = 3
    columns = []
    for element in elements:
        signs = negative_at_embedding(element, False)
        signs |= negative_at_embedding(element, True) << 1
        columns.append(signs | (bits[coset_index(element)] << 2))
    return [
        sum(((column >> bit) & 1) << index for index, column in enumerate(columns))
        for bit in range(4)
    ]


def useful_scan(ideals, count, elements, rows, kernel=None):
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
            accepted = gf2_rank(rows + [functional]) > 4
            if kernel is not None:
                assert accepted == any(
                    (functional & vector).bit_count() & 1 for vector in kernel
                )
        (useful if accepted else rejected).append(ideal)
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        if len(useful) == useful_count:
            return useful, rejected
    raise AssertionError("useful universe exhausted")


def configure_endpoint(count: int, generator_rank: int, useful_count: int):
    endpoint.D = D
    endpoint.T_COUNT = count
    endpoint.GENERATOR_RANK = generator_rank
    endpoint.USEFUL_COUNT = useful_count
    endpoint.SAFE_C = SAFE_C
    endpoint.ALPHA = ADVERTISED_ALPHA


def scan_counts(ideals, elements, independent_rows):
    results = []
    for count in range(T_MIN, T_MAX + 1):
        width = count + 2
        mask = (1 << width) - 1
        prefix_elements = elements[:width]
        rows = [row & mask for row in independent_rows]
        assert gf2_rank(rows) == 4
        generator_rank = width - 4
        assert generator_rank == count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        kernel = (
            nullspace_basis(rows, width) if count == WINNER_T else None
        )
        if kernel is not None:
            assert len(kernel) == WINNER_D
        useful, rejected = useful_scan(
            ideals, count, prefix_elements, rows, kernel
        )
        assert len(useful) == useful_count
        configure_endpoint(count, generator_rank, useful_count)
        threshold, anchor, _, log_rd = endpoint.optimize_diagnostic(
            ideals[:count], useful
        )
        results.append(
            CountResult(
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
    return results


def final_endpoint_audit(ramified, useful):
    outputs = []
    for precision in (100, 150):
        getcontext().prec = precision
        configure_endpoint(WINNER_T, WINNER_D, WINNER_N)
        threshold, anchor, records, log_rd = endpoint.optimize_diagnostic(
            ramified, useful
        )
        prepared_log_rd, frontier, omitted = endpoint.prepare_endpoint_data(
            ramified, useful
        )
        assert prepared_log_rd == log_rd
        assert ADVERTISED_ALPHA - Decimal("1e-8") < threshold
        assert threshold < ADVERTISED_ALPHA < OLD_RECORD_ALPHA
        assert min(record[0] for record in records) > Decimal("0.0001")
        assert records[0][1] > Decimal("0.001")
        assert records[1][1] < Decimal("-0.001")
        assert omitted < min(record[2] for record in records)

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
        outputs.append((threshold, anchor, records, log_rd, omitted, brackets))
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
    assert 2 * sqrt_three_upper / Fraction(333, 106) == SAFE_C

    primes = prime_sieve(220_000)
    assert D == 4 * RADICAND and RADICAND % 4 == 3
    assert all(
        RADICAND % prime for prime in primes if prime * prime <= RADICAND
    )
    ideals = prime_ideals(primes, 220_000)
    assert ideals[WINNER_T - 1] == (1_091, 1_091, "split", 605)

    elements, pari_columns = exact_nested_s_unit_basis()
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

    results = scan_counts(ideals, elements, independent_rows)
    winner = min(results, key=lambda result: result.threshold)
    assert winner.count == WINNER_T
    assert winner.generator_rank == WINNER_D
    assert winner.useful_count == WINNER_N
    assert winner.rejections == 0
    assert winner.last_useful == (119_359, 119_359, "split", 113_172)
    assert all(result.rejections == 0 for result in results)

    relation_bound = WINNER_D + 1 + WINNER_T + WINNER_N
    assert relation_bound == 11_342
    assert 4 * relation_bound == WINNER_D * WINNER_D - 1
    winner_width = WINNER_T + 2
    winner_mask = (1 << winner_width) - 1
    winner_rows = [row & winner_mask for row in independent_rows]
    winner_useful, winner_rejected = useful_scan(
        ideals,
        WINNER_T,
        elements[:winner_width],
        winner_rows,
        nullspace_basis(winner_rows, winner_width),
    )
    assert not winner_rejected and winner_useful[-1] == winner.last_useful
    endpoint_outputs = final_endpoint_audit(
        ideals[:WINNER_T], winner_useful
    )
    for result in results:
        print(result)
    print("winner:", winner)
    print("100/150-digit final endpoint outputs:")
    for output in endpoint_outputs:
        print(output)
    print("D=3200972 F_2(n) << n^0.49368759: CERTIFIED")


if __name__ == "__main__":
    main()
