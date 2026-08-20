#!/usr/bin/env python3
"""Independent exact certificate for the D=11235917 quadratic-CM record."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import re
import shutil
import subprocess
import sys


sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic2278757_cm as core  # noqa: E402
import verify_hostile_quadratic821453_cm as endpoint  # noqa: E402


D = 11_235_917
OMEGA_CONSTANT = (D - 1) // 4
T_COUNT = 217
GENERATOR_RANK = 215
USEFUL_COUNT = 11_123
SAFE_ALPHA = Decimal("0.49368323")
OLD_RECORD_ALPHA = Decimal("0.49368416")
SAFE_C = Fraction(71_603, 64_935)


def configure() -> None:
    core.D = D
    core.OMEGA_CONSTANT = OMEGA_CONSTANT
    core.T_COUNT = T_COUNT
    core.GENERATOR_RANK = GENERATOR_RANK
    core.USEFUL_COUNT = USEFUL_COUNT
    core.SAFE_C = SAFE_C
    core.configure_shared_arithmetic()
    endpoint.D = D
    endpoint.C = OMEGA_CONSTANT
    endpoint.T_COUNT = T_COUNT
    endpoint.GENERATOR_RANK = GENERATOR_RANK
    endpoint.USEFUL_COUNT = USEFUL_COUNT
    endpoint.SAFE_C = SAFE_C
    endpoint.ALPHA = SAFE_ALPHA
    endpoint.elementary.FIELD_DISCRIMINANT = D
    endpoint.elementary.OMEGA_CONSTANT = OMEGA_CONSTANT
    endpoint.elementary.RAMIFIED_IDEAL_COUNT = T_COUNT


def exact_s_unit_basis():
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);S=vector({T_COUNT},i,L[i][3]);su=bnfsunit(b,S);U=bnfunits(b,S);M=Mat(vector(#U[1],i,ideallog(nf,U[1][i],bid)));lr=-1;if(L[{T_COUNT}][1]==L[{T_COUNT}][2],lr=lift(nfmodpr(nf,Mod(x,nf.pol),L[{T_COUNT}][3])));print("META,",bnfcertify(b),",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",#su[5][2],",",#U[1],",",matrank(Mod(M,2)),",",L[{T_COUNT}][1],",",lr);for(i=1,#U[1],z=nffactorback(nf,U[1][i]);v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    expected = (
        "META,1,28,[14, 2],56,[14, 2, 2],"
        "[2, 2, 2, 2],1,0,219,4,1063,963"
    )
    assert expected in lines
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
    assert max(len(str(abs(value))) for pair in elements for value in pair) > 7_000
    return elements, columns, expected


def exact_kernel_and_usefulness(ideals, elements, columns):
    pari_rows = [
        sum(
            ((column >> bit) & 1) << index
            for index, column in enumerate(columns)
        )
        for bit in range(4)
    ]
    independent_rows = core.independent_local_rows(elements)
    assert core.gf2_rank(pari_rows) == 4
    assert core.gf2_rank(independent_rows) == 4
    assert core.gf2_rank(pari_rows + independent_rows) == 4
    kernel = core.nullspace_basis(independent_rows, len(elements))
    assert len(kernel) == GENERATOR_RANK

    useful, rejected = core.useful_scan(
        ideals, elements, independent_rows, kernel
    )
    assert len(useful) == USEFUL_COUNT
    assert not rejected
    assert useful[-1] == (121_951, 121_951, "split", 70_091)
    return independent_rows, kernel, useful, rejected


def equal_endpoint(log_rd, frontier, alpha: Decimal, iterations: int):
    def records(anchor: Decimal):
        return endpoint.evaluate_prepared(log_rd, frontier, alpha, anchor)

    low, high = Decimal("30000"), Decimal("60000")
    low_data = records(low)
    high_data = records(high)
    low_difference = low_data[0][0] - low_data[1][0]
    high_difference = high_data[0][0] - high_data[1][0]
    assert low_difference * high_difference < 0
    for _ in range(iterations):
        middle = (low + high) / 2
        data = records(middle)
        difference = data[0][0] - data[1][0]
        if low_difference * difference <= 0:
            high = middle
        else:
            low = middle
            low_difference = difference
    anchor = (low + high) / 2
    data = records(anchor)
    return anchor, data


def endpoint_certificate(ramified, useful, precision: int):
    getcontext().prec = precision
    log_rd, frontier, maximum_omitted = endpoint.prepare_endpoint_data(
        ramified, useful
    )

    low = Decimal("0.49368")
    high = OLD_RECORD_ALPHA
    low_anchor, low_data = equal_endpoint(log_rd, frontier, low, 150)
    high_anchor, high_data = equal_endpoint(log_rd, frontier, high, 150)
    assert min(record[0] for record in low_data) < 0
    assert min(record[0] for record in high_data) > 0
    for _ in range(155):
        middle = (low + high) / 2
        _, data = equal_endpoint(log_rd, frontier, middle, 150)
        if min(record[0] for record in data) > 0:
            high = middle
        else:
            low = middle
    threshold = (low + high) / 2
    anchor, threshold_data = equal_endpoint(
        log_rd, frontier, threshold, 170
    )
    safe_data = endpoint.evaluate_prepared(
        log_rd, frontier, SAFE_ALPHA, anchor
    )
    assert Decimal("0.49368321993088") < threshold
    assert threshold < Decimal("0.49368321993090") < SAFE_ALPHA
    assert min(record[0] for record in safe_data) > Decimal("0.0015")
    assert safe_data[0][1] > Decimal("0.005")
    assert safe_data[1][1] < Decimal("-0.012")
    assert maximum_omitted < min(record[2] for record in safe_data)
    assert abs(threshold_data[0][0] - threshold_data[1][0]) < Decimal("1e-40")
    return threshold, anchor, safe_data, log_rd, maximum_omitted


def nearby_thresholds(ideals):
    getcontext().prec = 65
    output = {}
    for count in (211, 213, 215, 216, 217, 218, 219, 221, 223):
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        log_rd, frontier, maximum_omitted = endpoint.prepare_endpoint_data(
            ideals[:count], ideals[count : count + useful_count]
        )
        low, high = Decimal("0.49367"), Decimal("0.49369")
        for _ in range(72):
            middle = (low + high) / 2
            _, data = equal_endpoint(log_rd, frontier, middle, 80)
            if min(record[0] for record in data) > 0:
                high = middle
            else:
                low = middle
        threshold = (low + high) / 2
        anchor, data = equal_endpoint(log_rd, frontier, threshold, 90)
        assert data[0][1] > Decimal("0.004")
        assert data[1][1] < Decimal("-0.012")
        assert maximum_omitted < min(record[2] for record in data)
        output[count] = (threshold, anchor, generator_rank, useful_count)
    assert min(output, key=lambda count: output[count][0]) == T_COUNT
    assert output[217][0] + Decimal("1e-8") < output[215][0]
    assert output[217][0] + Decimal("1e-7") < output[221][0]
    return output


def packing_constant_audit() -> None:
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


def main() -> None:
    getcontext().prec = 100
    configure()
    packing_constant_audit()
    assert D == 7 * 11 * 337 * 433
    assert D % 8 == 5

    primes = core.elementary.prime_sieve(230_000)
    assert all(prime in primes for prime in (7, 11, 337, 433))
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = core.elementary.prime_ideals(primes, 230_000)
    assert ideals[T_COUNT - 1] == (1_063, 1_063, "split", 963)

    elements, columns, metadata = exact_s_unit_basis()
    rows, kernel, useful, rejected = exact_kernel_and_usefulness(
        ideals, elements, columns
    )

    maximum_relations = (GENERATOR_RANK * GENERATOR_RANK - 1) // 4
    relation_bound = GENERATOR_RANK + 1 + T_COUNT + USEFUL_COUNT
    assert maximum_relations == relation_bound == 11_556
    point = Fraction(2, GENERATOR_RANK)
    assert (
        1
        - GENERATOR_RANK * point
        + relation_bound * point * point
    ) < 0

    outputs = [
        endpoint_certificate(ideals[:T_COUNT], useful, precision)
        for precision in (100, 150)
    ]
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-45")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-40")
    nearby = nearby_thresholds(ideals)

    print("field / S-unit metadata:", metadata)
    print(
        "basis / ray rows / kernel / useful / rejected / last:",
        len(elements), len(rows), len(kernel), len(useful), len(rejected), useful[-1]
    )
    print("generator / relation ceiling:", GENERATOR_RANK, relation_bound)
    print("100-digit endpoint:", outputs[0])
    print("150-digit endpoint:", outputs[1])
    print("nearby all-useful thresholds:")
    for count, record in nearby.items():
        print(" ", count, record)
    print("D=11235917 CM F_2(n) << n^0.49368323: CERTIFIED")


if __name__ == "__main__":
    main()
