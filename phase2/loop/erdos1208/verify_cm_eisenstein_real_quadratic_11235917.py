#!/usr/bin/env python3
"""Exact certificate for the CM/Eisenstein Q(sqrt(11235917)) record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.set_int_max_str_digits(30_000)
sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_cm_eisenstein_real_quadratic_43133 as elementary  # noqa: E402
import verify_hostile_quadratic821453_cm as endpoint  # noqa: E402


D = 11_235_917
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 217
GENERATOR_RANK = 215
USEFUL_COUNT = 11_123
ADVERTISED_ALPHA = Decimal("0.49368323")
OLD_RECORD_ALPHA = Decimal("0.49368416")
SAFE_CM_CONSTANT = Fraction(71_603, 64_935)
EXPECTED_THRESHOLD = Decimal(
    "0.4936832199308881880151091959337012970825801151476568"
)


def configure_shared_arithmetic() -> None:
    elementary.FIELD_DISCRIMINANT = D
    elementary.OMEGA_CONSTANT = OMEGA_CONSTANT
    elementary.RAMIFIED_IDEAL_COUNT = T_COUNT
    endpoint.D = D
    endpoint.C = OMEGA_CONSTANT
    endpoint.T_COUNT = T_COUNT
    endpoint.GENERATOR_RANK = GENERATOR_RANK
    endpoint.USEFUL_COUNT = USEFUL_COUNT
    endpoint.SAFE_C = SAFE_CM_CONSTANT
    endpoint.ALPHA = ADVERTISED_ALPHA
    endpoint.configure_elementary_module()


def exact_kummer_kernel() -> tuple[list[tuple[int, int]], tuple[int, ...]]:
    """Reconstruct a basis of the full sign/mod-4 Kummer kernel."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    script = rf"""default(nbthreads,1);default(realprecision,1000);D={D};c=(D-1)/4;T={T_COUNT};b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);S=vector(T,i,L[i][3]);su=bnfsunit(b,S);units=bnfunits(b,S);bid=idealstar(nf,[4,[1,1]],1,2);mm=Mat(vector(#units[1],i,ideallog(nf,units[1][i],bid)));kk=matker(Mod(mm,2));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),S[#S]));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",su[5][1],",",#su[5][2],",",#units[1],",",matrank(Mod(mm,2)),",",matsize(kk)[2],",",L[T][1],",",lastroot,",",bid.cyc);elements=vector(matsize(kk)[2],j,my(indices=select(i->lift(kk[i,j])==1,[1..#units[1]]),factorization=units[1][indices[1]]);for(z=2,#indices,factorization=matconcat([factorization;units[1][indices[z]]]));nffactorback(nf,factorization));for(j=1,#elements,if(type(elements[j])=="t_INT",print("ELEMENT,",elements[j],",0"),print("ELEMENT,",elements[j][1],",",elements[j][2])))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=300
    )
    lines = output.splitlines()
    expected = (
        "META,1,28,[14, 2],56,[14, 2, 2],1,0,219,4,215,"
        "1063,963,[2, 2, 2, 2]"
    )
    assert expected in lines
    pattern = re.compile(r"ELEMENT,(-?\d+),(-?\d+)")
    elements = [
        tuple(map(int, match.groups()))
        for line in lines
        if (match := pattern.fullmatch(line))
    ]
    assert len(elements) == GENERATOR_RANK
    metadata = (1, 28, 56, 1, 0, 219, 4, 215, 1063, 963)
    return elements, metadata


def useful_scan(ideals, kernel):
    """Test every mod-three Frobenius functional on the exact kernel."""
    useful = []
    rejected = []
    maximum_trials = 0
    for ideal in ideals[T_COUNT:]:
        norm_q, prime, _, root = ideal
        if prime == 3:
            continue
        accepted = True
        if norm_q % 3 == 2:
            assert norm_q == prime and root is not None
            accepted = False
            trials = 0
            for a, b in kernel:
                trials += 1
                residue = (a % prime + (b % prime) * root) % prime
                assert residue
                if pow(residue, (prime - 1) // 2, prime) == prime - 1:
                    accepted = True
                    break
            maximum_trials = max(maximum_trials, trials)
        (useful if accepted else rejected).append(ideal)
        if len(useful) == USEFUL_COUNT:
            break
    assert len(useful) == USEFUL_COUNT
    return useful, rejected, maximum_trials


def optimize_endpoint(ramified, useful):
    """Equalize and certify both all-depth product-disk endpoints."""
    log_rd, frontier, maximum_omitted = endpoint.prepare_endpoint_data(
        ramified, useful
    )

    def endpoint_root(anchor: Decimal, endpoint_index: int):
        low, high = Decimal("0.48"), Decimal("0.51")
        assert endpoint.evaluate_prepared(
            log_rd, frontier, low, anchor
        )[endpoint_index][0] < 0
        assert endpoint.evaluate_prepared(
            log_rd, frontier, high, anchor
        )[endpoint_index][0] > 0
        for _ in range(110):
            middle = (low + high) / 2
            if endpoint.evaluate_prepared(
                log_rd, frontier, middle, anchor
            )[endpoint_index][0] > 0:
                high = middle
            else:
                low = middle
        return low, high

    low_w, high_w = Decimal("10000"), Decimal("60000")

    def difference(anchor: Decimal) -> Decimal:
        first = endpoint_root(anchor, 0)
        second = endpoint_root(anchor, 1)
        return sum(first) / 2 - sum(second) / 2

    low_difference = difference(low_w)
    high_difference = difference(high_w)
    assert low_difference * high_difference < 0
    for _ in range(100):
        middle_w = (low_w + high_w) / 2
        middle_difference = difference(middle_w)
        if low_difference * middle_difference <= 0:
            high_w, high_difference = middle_w, middle_difference
        else:
            low_w, low_difference = middle_w, middle_difference
    anchor = (low_w + high_w) / 2
    brackets = [endpoint_root(anchor, index) for index in (0, 1)]
    threshold = max(sum(bracket) / 2 for bracket in brackets)
    records = endpoint.evaluate_prepared(
        log_rd, frontier, ADVERTISED_ALPHA, anchor
    )
    return threshold, anchor, brackets, records, log_rd, maximum_omitted


def main() -> None:
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

    primes = elementary.prime_sieve(180_000)
    assert D == 7 * 11 * 337 * 433
    assert D % 8 == 5 and 1 + 4 * OMEGA_CONSTANT == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = elementary.prime_ideals(primes, 180_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_063, 1_063, "split", 963)

    kernel, metadata = exact_kummer_kernel()
    assert metadata == (1, 28, 56, 1, 0, 219, 4, 215, 1063, 963)

    # Independently verify that every PARI kernel element is totally positive
    # and a square in the odd unit group modulo four.
    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if elementary.norm((a, b)) % 2
    ]
    square_residues = {
        tuple(value % 4 for value in elementary.multiply(unit, unit))
        for unit in units_mod_four
    }
    assert len(units_mod_four) == 12 and len(square_residues) == 3
    for element in kernel:
        assert elementary.negative_at_embedding(element, False) == 0
        assert elementary.negative_at_embedding(element, True) == 0
        assert (element[0] % 4, element[1] % 4) in square_residues

    useful, rejected, maximum_trials = useful_scan(ideals, kernel)
    assert not rejected
    assert useful[-1] == (121_951, 121_951, "split", 70_091)
    assert maximum_trials == 11

    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert relation_bound == 11_556
    assert 4 * relation_bound == GENERATOR_RANK * GENERATOR_RANK - 1

    outputs = []
    for precision in (100, 150):
        getcontext().prec = precision
        result = optimize_endpoint(ramified, useful)
        threshold, _, brackets, records, _, maximum_omitted = result
        assert ADVERTISED_ALPHA - Decimal("2e-8") < threshold
        assert threshold < ADVERTISED_ALPHA < OLD_RECORD_ALPHA
        assert abs(threshold - EXPECTED_THRESHOLD) < Decimal("1e-50")
        assert min(record[0] for record in records) > Decimal("0.001")
        assert records[0][1] > Decimal("0.001")
        assert records[1][1] < Decimal("-0.001")
        assert maximum_omitted < min(record[2] for record in records)
        assert all(
            ADVERTISED_ALPHA - Decimal("2e-8") < low < high < ADVERTISED_ALPHA
            for low, high in brackets
        )
        outputs.append(result)
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-90")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-85")

    result = outputs[-1]
    print("PARI BNF / class / narrow / localized class: PASS")
    print("T / d / relations:", T_COUNT, GENERATOR_RANK, relation_bound)
    print("last T ideal:", ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("maximum usefulness trials:", maximum_trials)
    print("threshold / anchor:", result[0], result[1])
    print("fixed-anchor threshold brackets:", *result[2])
    print("150-digit endpoint margins:", *(record[0] for record in result[3]))
    print("log real-tower root discriminant:", result[4])
    print("maximum omitted slope:", result[5])
    print("CM quadratic-11235917 F_2(n) << n^0.49368323: CERTIFIED")


if __name__ == "__main__":
    main()
