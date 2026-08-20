#!/usr/bin/env python3
"""Independent hostile certificate for the D=2278757 CM candidate.

The class-number-two S-unit basis is constructed directly from principal
ideal generators.  PARI certifies the BNF and local columns; Python rebuilds
the safe kernel, performs every CM usefulness test, checks the GS budget, and
recomputes the all-depth endpoint.
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


D = 2_278_757
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 223
GENERATOR_RANK = 221
USEFUL_COUNT = 11_765
OLD_RECORD_ALPHA = Decimal("0.49369313")
ADVERTISED_ALPHA = Decimal("0.49368818")
SAFE_C = Fraction(71_603, 64_935)


def configure_shared_arithmetic() -> None:
    elementary.FIELD_DISCRIMINANT = D
    elementary.OMEGA_CONSTANT = OMEGA_CONSTANT
    elementary.RAMIFIED_IDEAL_COUNT = T_COUNT
    endpoint.D = D
    endpoint.C = OMEGA_CONSTANT
    endpoint.T_COUNT = T_COUNT
    endpoint.GENERATOR_RANK = GENERATOR_RANK
    endpoint.USEFUL_COUNT = USEFUL_COUNT
    endpoint.SAFE_C = SAFE_C
    endpoint.ALPHA = ADVERTISED_ALPHA
    endpoint.configure_elementary_module()


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
    """Exact basis of vectors annihilated by the given F2 rows."""
    pivots = rowspace_basis(rows)
    free = [index for index in range(width) if index not in pivots]
    output: list[int] = []
    for free_index in free:
        vector = 1 << free_index
        # Each echelon row has its pivot above all remaining terms, so the
        # pivot variables are solved from low to high.
        for pivot in sorted(pivots):
            row = pivots[pivot] ^ (1 << pivot)
            if (row & vector).bit_count() & 1:
                vector |= 1 << pivot
        assert all(not ((row & vector).bit_count() & 1) for row in rows)
        output.append(vector)
    assert gf2_rank(output) == len(output)
    return output


def exact_s_unit_basis(
) -> tuple[list[tuple[int, int]], list[int], tuple[int, ...]]:
    """Certified direct basis for O_{E,S}^*/squares and ray columns."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,{T_COUNT},cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&cl[1]!=0,ref=i));R=L[ref][3];S=vector({T_COUNT},i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,2))[2];listput(G,z);for(i=1,{T_COUNT},if(i!=ref,P=L[i][3];cl=bnfisprincipal(b,P,0);if(cl[1]==0,z=bnfisprincipal(b,P)[2],z=bnfisprincipal(b,idealmul(nf,P,R))[2]);listput(G,z)));refroot=lift(nfmodpr(nf,Mod(x,nf.pol),R));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_COUNT}][3]));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",ref,",",L[ref][1],",",refroot,",",L[{T_COUNT}][1],",",lastroot,",",#G);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    expected = (
        "META,1,2,[2],4,[2, 2],[2, 2, 2, 2],1,"
        "5,19,4,1109,152,225"
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
        if match:
            elements.append(tuple(map(int, match.group(1, 2))))
            columns.append(
                sum(int(match.group(3 + bit)) << bit for bit in range(4))
            )
    assert len(elements) == 225 == len(columns)
    metadata = (1, 2, 4, 1, 5, 19, 4, 1109, 152, 225)
    return elements, columns, metadata


def independent_local_rows(elements: list[tuple[int, int]]) -> list[int]:
    """Rebuild signs and square classes modulo four using integer arithmetic."""
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if elementary.norm((a, b)) % 2
    ]

    def multiply_mod_four(
        left: tuple[int, int], right: tuple[int, int]
    ) -> tuple[int, int]:
        product = elementary.multiply(left, right)
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
    last = coset_index(
        multiply_mod_four(
            representatives[nonidentity[0]], representatives[nonidentity[1]]
        )
    )
    assert last == nonidentity[2]
    bits[last] = 3

    columns = []
    for element in elements:
        signs = elementary.negative_at_embedding(element, False)
        signs |= elementary.negative_at_embedding(element, True) << 1
        columns.append(signs | (bits[coset_index(element)] << 2))
    return [
        sum(((column >> bit) & 1) << index for index, column in enumerate(columns))
        for bit in range(4)
    ]


def useful_scan(
    ideals: list[tuple[int, int, str, int | None]],
    elements: list[tuple[int, int]],
    constraint_rows: list[int],
    kernel: list[int],
):
    useful = []
    rejected = []
    for ideal in ideals[T_COUNT:]:
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
            rank_test = gf2_rank(constraint_rows + [functional]) > 4
            kernel_test = any(
                (functional & vector).bit_count() & 1 for vector in kernel
            )
            assert rank_test == kernel_test
            accepted = rank_test
        (useful if accepted else rejected).append(ideal)
        if len(useful) == USEFUL_COUNT:
            break
    assert len(useful) == USEFUL_COUNT
    return useful, rejected


def endpoint_audit(ramified, useful):
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
        assert ADVERTISED_ALPHA - Decimal("2e-8") < threshold
        assert threshold < ADVERTISED_ALPHA < OLD_RECORD_ALPHA
        assert min(record[0] for record in records) > Decimal("0.0001")
        assert records[0][1] > Decimal("0.001")
        assert records[1][1] < Decimal("-0.001")

        brackets = []
        for endpoint_index in (0, 1):
            low = ADVERTISED_ALPHA - Decimal("2e-8")
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
            (
                threshold,
                anchor,
                records,
                log_rd,
                maximum_omitted,
                brackets,
            )
        )
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-50")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-45")
    return outputs


def main() -> None:
    getcontext().prec = 100
    configure_shared_arithmetic()

    # Safe rational upper bound for 2 sqrt(3)/pi.
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

    primes = elementary.prime_sieve(220_000)
    assert D == 13 * 59 * 2_971
    assert all(prime in primes for prime in (13, 59, 2_971))
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = elementary.prime_ideals(primes, 220_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_109, 1_109, "split", 152)

    elements, pari_columns, metadata = exact_s_unit_basis()
    assert metadata == (1, 2, 4, 1, 5, 19, 4, 1109, 152, 225)
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = independent_local_rows(elements)
    assert gf2_rank(pari_rows) == 4 == gf2_rank(independent_rows)
    # The two computations may choose different F2 bases, but must define
    # the same four-dimensional row space.
    assert gf2_rank(pari_rows + independent_rows) == 4
    kernel = nullspace_basis(independent_rows, len(elements))
    assert len(kernel) == GENERATOR_RANK

    useful, rejected = useful_scan(
        ideals, elements, independent_rows, kernel
    )
    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert relation_bound == 12_210
    assert 4 * relation_bound == GENERATOR_RANK * GENERATOR_RANK - 1

    endpoint_outputs = endpoint_audit(ramified, useful)
    threshold, anchor, records, log_rd, omitted, brackets = endpoint_outputs[-1]
    print("PARI class/S-class/direct S-unit basis: CERTIFIED")
    print("T / last:", T_COUNT, ramified[-1])
    print("S-unit columns / ray rank / kernel:", len(elements), 4, len(kernel))
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("first rejected ideals:", rejected[:10])
    print("generator / relation bound:", GENERATOR_RANK, relation_bound)
    print("log root discriminant:", log_rd)
    print("equal-endpoint threshold / anchor:", threshold, anchor)
    print("records at advertised alpha:", records)
    print("maximum omitted slope:", omitted)
    print("fixed-anchor endpoint root brackets:", brackets)
    print("100/150-digit advertised margins:")
    for output in endpoint_outputs:
        print(" ", output[2][0][0], output[2][1][0])
    print("D=2278757 F_2(n) << n^0.49368818: CERTIFIED")


if __name__ == "__main__":
    main()
