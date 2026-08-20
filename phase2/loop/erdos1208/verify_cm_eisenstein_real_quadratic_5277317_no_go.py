#!/usr/bin/env python3
"""Exact no-go audit for the CM/Eisenstein Q(sqrt(5277317)) candidate.

The default run certifies the exact arithmetic and the best prefix T=221.
Pass ``--dense`` to recompute every optimistic prefix 205 <= T <= 250.
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
import verify_hostile_quadratic2278757_cm as audit  # noqa: E402
import verify_hostile_quadratic821453_cm as endpoint  # noqa: E402


D = 5_277_317
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 221
GENERATOR_RANK = 219
USEFUL_COUNT = 11_549
CURRENT_RECORD_ALPHA = Decimal("0.49368416")
SAFE_CM_CONSTANT = Fraction(71_603, 64_935)
DENSE_MIN = 205
DENSE_MAX = 250
EXPECTED_THRESHOLD = Decimal(
    "0.493684649778186556120660238919"
)


def configure_shared_arithmetic() -> None:
    audit.D = D
    audit.OMEGA_CONSTANT = OMEGA_CONSTANT
    audit.T_COUNT = T_COUNT
    audit.GENERATOR_RANK = GENERATOR_RANK
    audit.USEFUL_COUNT = USEFUL_COUNT
    audit.ADVERTISED_ALPHA = CURRENT_RECORD_ALPHA
    audit.OLD_RECORD_ALPHA = Decimal("0.49368647")
    audit.SAFE_C = SAFE_CM_CONSTANT
    audit.configure_shared_arithmetic()
    endpoint.D = D
    endpoint.C = OMEGA_CONSTANT
    endpoint.SAFE_C = SAFE_CM_CONSTANT
    endpoint.ALPHA = CURRENT_RECORD_ALPHA


def exact_cyclic_twelve_basis(
) -> tuple[list[tuple[int, int]], list[int], tuple[int, ...]]:
    """Build a direct S-unit squareclass basis for the cyclic C12 field."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    # The norm-11 selected ideal R generates C12.  A generator of R^12,
    # together with generators of P R^e for all other selected P, kills the
    # class obstruction explicitly.  The two global units complete a basis.
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;T={T_COUNT};b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;g=0;for(i=1,T,cl=lift(bnfisprincipal(b,L[i][3],0)[1]);if(ref==0&&gcd(cl,12)==1,ref=i;g=cl));R=L[ref][3];S=vector(T,i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b);G=List();for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));z=bnfisprincipal(b,idealpow(nf,R,12))[2];listput(G,z);cnt=vector(12);for(i=1,T,if(i!=ref,P=L[i][3];cl=lift(bnfisprincipal(b,P,0)[1]);cnt[cl+1]++;e=lift(Mod(-cl/g,12));J=if(e==0,P,idealmul(nf,P,idealpow(nf,R,e)));z=bnfisprincipal(b,J)[2];listput(G,z)));M=Mat(vector(#G,i,ideallog(nf,G[i],bid)));M205=Mat(vector(207,i,ideallog(nf,G[i],bid)));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",#su[5][2],",",ref,",",g,",",L[ref][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),R)),",",cnt,",",L[T][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),L[T][3])),",",#G,",",matrank(Mod(M,2)),",",#G-matrank(Mod(M,2)),",",matrank(Mod(M205,2)));for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=240
    )
    lines = output.splitlines()
    expected = (
        "META,1,12,[12],12,[12],[2, 2, 2, 2],1,0,2,1,11,1,"
        "[22, 18, 18, 16, 17, 19, 21, 19, 17, 16, 18, 19],"
        "1031,848,223,4,219,4"
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
    metadata = (1, 12, 12, 1, 0, 2, 1, 11, 1, 1031, 848, 223, 4, 219, 4)
    return elements, columns, metadata


def optimistic_lists(ideals, ramified_count: int):
    generator_rank = ramified_count - 2
    relation_cap = (generator_rank * generator_rank - 1) // 4
    useful_count = relation_cap - (generator_rank + 1) - ramified_count
    useful = [
        ideal for ideal in ideals[ramified_count:] if ideal[1] != 3
    ][:useful_count]
    assert len(useful) == useful_count
    return generator_rank, useful_count, ideals[:ramified_count], useful


def optimize_prefix(ramified, useful):
    """Equalize the two disk endpoints inside a certified anchor bracket."""
    log_rd, frontier, maximum_omitted = endpoint.prepare_endpoint_data(
        ramified, useful
    )

    def endpoint_root(anchor: Decimal, endpoint_index: int) -> Decimal:
        low, high = Decimal("0.48"), Decimal("0.51")
        assert endpoint.evaluate_prepared(
            log_rd, frontier, low, anchor
        )[endpoint_index][0] < 0
        assert endpoint.evaluate_prepared(
            log_rd, frontier, high, anchor
        )[endpoint_index][0] > 0
        for _ in range(90):
            middle = (low + high) / 2
            if endpoint.evaluate_prepared(
                log_rd, frontier, middle, anchor
            )[endpoint_index][0] > 0:
                high = middle
            else:
                low = middle
        return (low + high) / 2

    low_w, high_w = Decimal("10000"), Decimal("60000")
    low_difference = endpoint_root(low_w, 0) - endpoint_root(low_w, 1)
    high_difference = endpoint_root(high_w, 0) - endpoint_root(high_w, 1)
    assert low_difference * high_difference < 0
    for _ in range(85):
        middle_w = (low_w + high_w) / 2
        difference = endpoint_root(middle_w, 0) - endpoint_root(middle_w, 1)
        if low_difference * difference <= 0:
            high_w, high_difference = middle_w, difference
        else:
            low_w, low_difference = middle_w, difference
    anchor = (low_w + high_w) / 2
    threshold = max(
        endpoint_root(anchor, 0), endpoint_root(anchor, 1)
    )
    records = endpoint.evaluate_prepared(
        log_rd, frontier, CURRENT_RECORD_ALPHA, anchor
    )
    assert maximum_omitted < min(record[2] for record in records)
    return threshold, anchor, records, log_rd, maximum_omitted


def dense_prefix_audit(ideals) -> list[tuple[Decimal, int]]:
    """Recompute the all-useful optimistic window (several minutes)."""
    scores: list[tuple[Decimal, int]] = []
    for ramified_count in range(DENSE_MIN, DENSE_MAX + 1):
        _, _, ramified, useful = optimistic_lists(ideals, ramified_count)
        threshold, _, _, _, _ = optimize_prefix(ramified, useful)
        assert threshold > CURRENT_RECORD_ALPHA
        scores.append((threshold, ramified_count))
    best = min(scores)
    assert best[1] == T_COUNT
    assert abs(best[0] - EXPECTED_THRESHOLD) < Decimal("1e-28")
    return scores


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
    assert 2 * sqrt_three_upper / Fraction(333, 106) == SAFE_CM_CONSTANT

    primes = elementary.prime_sieve(200_000)
    assert D == 613 * 8_609
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = elementary.prime_ideals(primes, 200_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_031, 1_031, "split", 848)

    elements, pari_columns, metadata = exact_cyclic_twelve_basis()
    assert metadata == (1, 12, 12, 1, 0, 2, 1, 11, 1, 1031, 848, 223, 4, 219, 4)
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(pari_columns)
        )
        for bit in range(4)
    ]
    independent_rows = audit.independent_local_rows(elements)
    assert audit.gf2_rank(pari_rows) == 4
    assert audit.gf2_rank(independent_rows) == 4
    assert audit.gf2_rank(pari_rows + independent_rows) == 4
    kernel = audit.nullspace_basis(independent_rows, len(elements))
    assert len(kernel) == GENERATOR_RANK

    useful, rejected = audit.useful_scan(
        ideals, elements, independent_rows, kernel
    )
    assert not rejected
    assert useful[-1] == (126_547, 126_547, "split", 111_660)
    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert relation_bound == 11_990
    assert relation_bound == (GENERATOR_RANK * GENERATOR_RANK - 1) // 4

    outputs = []
    for precision in (100, 150):
        getcontext().prec = precision
        outputs.append(optimize_prefix(ramified, useful))
    threshold, anchor, records, log_rd, omitted = outputs[-1]
    assert abs(outputs[0][0] - threshold) < Decimal("1e-55")
    assert abs(threshold - EXPECTED_THRESHOLD) < Decimal("1e-28")
    assert threshold > CURRENT_RECORD_ALPHA
    assert max(record[0] for record in records) < Decimal("-0.08")

    print("PARI BNF / C12 class / narrow / localized class: PASS")
    print("T / d / relations:", T_COUNT, GENERATOR_RANK, relation_bound)
    print("last T ideal:", ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("optimistic threshold / anchor:", threshold, anchor)
    print("current-record endpoint margins:", *(record[0] for record in records))
    print("log real-tower root discriminant:", log_rd)
    print("maximum omitted slope:", omitted)

    if "--dense" in sys.argv[1:]:
        getcontext().prec = 70
        scores = dense_prefix_audit(ideals)
        print("dense 205..250 best:", min(scores))
    print("D=5277317 does not improve alpha=0.49368416: CERTIFIED")


if __name__ == "__main__":
    main()
