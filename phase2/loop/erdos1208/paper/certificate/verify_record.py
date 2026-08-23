#!/usr/bin/env python3
"""Dependency-closed certificate for F_2(n) << n^0.49368323.

The only non-Python dependency is PARI/GP (tested with GP 2.17.4).  This
single-field script reconstructs the certified BNF, the sign/modulo-4 Kummer
kernel, the saturation group V_T, every useful Frobenius test, the exact
Golod--Shafarevich budget, the complete retained local frontier, and the two
endpoint inequalities at 100 and 150 decimal digits.  It also checks the
desaturated fallback exponents 0.4936834 and 0.4936837.
"""

from __future__ import annotations

import bisect
from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
import re
import shutil
import subprocess
import sys


sys.set_int_max_str_digits(30_000)

D = 11_235_917
C = (D - 1) // 4
T_COUNT = 217
GENERATOR_RANK = 215
USEFUL_COUNT = 11_123
SAFE_ALPHA = Decimal("0.49368323")
SAFE_C = Fraction(71_603, 64_935)
EPSILON = Decimal("1e-25")
EXPECTED_THRESHOLD = Decimal(
    "0.4936832199308881880151091959337012970825801151476568"
)
EXPECTED_SATURATION_ROWS = (114, 107, 114, 121)

Ideal = tuple[int, int, str, int | None]
Item = tuple[Decimal, Decimal, Decimal, int, int, int]
Frontier = tuple[list[Item], list[Decimal], list[Decimal]]


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if sieve[prime]:
            count = (limit - prime * prime) // prime + 1
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * count
    return [value for value in range(2, limit + 1) if sieve[value]]


def norm(element: tuple[int, int]) -> int:
    a, b = element
    return a * a + a * b - C * b * b


def multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    a, b = left
    x, y = right
    return a * x + C * b * y, a * y + b * x + b * y


def negative_at_embedding(
    element: tuple[int, int], conjugate_place: bool
) -> int:
    """Return the exact sign bit of a+b(1+/-sqrt(D))/2."""
    a, b = element
    rational_part = 2 * a + b
    radical_part = -b if conjugate_place else b
    if rational_part >= 0 and radical_part >= 0:
        return 0
    if rational_part <= 0 and radical_part <= 0:
        return 1
    rational_square = rational_part * rational_part
    radical_square = radical_part * radical_part * D
    assert rational_square != radical_square
    if rational_part > 0:
        return int(rational_square < radical_square)
    return int(radical_square < rational_square)


def tonelli_shanks(value: int, prime: int) -> int:
    value %= prime
    assert value and pow(value, (prime - 1) // 2, prime) == 1
    if prime % 4 == 3:
        return pow(value, (prime + 1) // 4, prime)
    odd_part = prime - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        power_of_two += 1
        odd_part //= 2
    nonresidue = 2
    while pow(nonresidue, (prime - 1) // 2, prime) != prime - 1:
        nonresidue += 1
    order_power = power_of_two
    coefficient = pow(nonresidue, odd_part, prime)
    test = pow(value, odd_part, prime)
    root = pow(value, (odd_part + 1) // 2, prime)
    while test != 1:
        index = 1
        square = test * test % prime
        while square != 1:
            square = square * square % prime
            index += 1
        multiplier = pow(coefficient, 1 << (order_power - index - 1), prime)
        root = root * multiplier % prime
        test = test * multiplier * multiplier % prime
        coefficient = multiplier * multiplier % prime
        order_power = index
    assert root * root % prime == value
    return root


def prime_ideals(primes: list[int], norm_limit: int) -> list[Ideal]:
    ideals: list[Ideal] = []
    for prime in primes:
        if prime == 2 or prime > norm_limit:
            continue
        if D % prime == 0:
            ideals.append((prime, prime, "ramified", (prime + 1) // 2))
            continue
        symbol = pow(D % prime, (prime - 1) // 2, prime)
        if symbol == 1:
            square_root = tonelli_shanks(D, prime)
            inverse_two = (prime + 1) // 2
            roots = sorted(
                {
                    (1 + square_root) * inverse_two % prime,
                    (1 - square_root) * inverse_two % prime,
                }
            )
            assert len(roots) == 2
            ideals.extend(
                (prime, prime, "split", root) for root in roots
            )
        else:
            assert symbol == prime - 1
            if prime * prime <= norm_limit:
                ideals.append((prime * prime, prime, "inert", None))
    ideals.sort(key=lambda row: (row[0], row[1], row[2], row[3] or -1))
    return ideals


def exact_kummer_kernel() -> tuple[list[tuple[int, int]], tuple[int, ...]]:
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


def exact_saturation_probe() -> tuple[tuple[int, ...], int]:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    script = rf"""default(nbthreads,1);D={D};c=(D-1)/4;T={T_COUNT};b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;g1=b.clgp[3][1];g2=b.clgp[3][2];a1=idealpow(nf,g1,7);x1v=bnfisprincipal(b,idealpow(nf,a1,2));x2v=bnfisprincipal(b,idealpow(nf,g2,2));x1=nfbasistoalg(nf,x1v[2]);x2=nfbasistoalg(nf,x2v[2]);gens=[Mod(-1,nf.pol),b.fu[1],x1,x2];L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);M=matrix(4,T);for(i=1,T,P=L[i][3];Q=L[i][1];pr=nfmodprinit(nf,P);for(j=1,4,z=gens[j];v=idealval(nf,z,P);if(v%2,print("ODDVAL,",j,",",i,",",v));if(v!=0,tw=idealtwoelt(nf,P);pi=nfbasistoalg(nf,tw[2]);if(idealval(nf,pi,P)!=1,pi=tw[1]);z=z/pi^v);res=nfmodpr(nf,z,pr);M[j,i]=if(res^((Q-1)/2)==1,0,1)));print("SATMETA,",cert,",",b.no,",",b.clgp[2],",",L[T][1]);print("SATROWS,",vector(4,j,vecsum(Vec(M[j,]))));print("SATRANK,",matrank(Mod(M,2)))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=300
    )
    lines = output.splitlines()
    assert "SATMETA,1,28,[14, 2],1063" in lines
    assert not any(line.startswith("ODDVAL") for line in lines)
    row_line = next(line for line in lines if line.startswith("SATROWS,"))
    rows = tuple(map(int, re.findall(r"\d+", row_line)))
    rank_line = next(line for line in lines if line.startswith("SATRANK,"))
    rank = int(rank_line.rsplit(",", 1)[1])
    assert rows == EXPECTED_SATURATION_ROWS and rank == 4
    return rows, rank


def useful_scan(
    ideals: list[Ideal], kernel: list[tuple[int, int]]
) -> tuple[list[Ideal], list[Ideal], int]:
    useful: list[Ideal] = []
    rejected: list[Ideal] = []
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


def local_increment(norm_q: int, depth: int) -> Decimal:
    parameter = Decimal(1) / Decimal(norm_q * norm_q)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= parameter
        total += power
    current_value = Decimal(depth + 1) / total
    previous_value = Decimal(depth) / previous_total
    return (current_value / previous_value).ln() / 2


def build_frontier(
    ideals: list[Ideal], slope_floor: Decimal = Decimal("0.01")
) -> tuple[list[Item], Decimal]:
    increments: list[Item] = []
    maximum_omitted = Decimal(0)
    for ideal_index, ideal in enumerate(ideals):
        norm_q = ideal[0]
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        depth = 1
        while True:
            gain = local_increment(norm_q, depth) / 2
            if previous is not None:
                assert previous > gain
            previous = gain
            slope = gain / cost
            if slope < slope_floor:
                maximum_omitted = max(maximum_omitted, slope)
                break
            increments.append(
                (slope, cost, gain, norm_q, depth, ideal_index)
            )
            depth += 1
            assert depth < 100
    increments.sort(reverse=True)
    return increments, maximum_omitted


def cumulative_frontier(increments: list[Item]) -> Frontier:
    costs = [Decimal(0)]
    gains = [Decimal(0)]
    for _, cost, gain, _, _, _ in increments:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
    return increments, costs, gains


def fast_envelope(
    frontier: Frontier, target: Decimal
) -> tuple[Decimal, int, Decimal, Decimal]:
    increments, costs, gains = frontier
    index = bisect.bisect_left(costs, target)
    assert 0 < index < len(costs)
    fraction = (target - costs[index - 1]) / (
        costs[index] - costs[index - 1]
    )
    assert 0 <= fraction <= 1
    item = increments[index - 1]
    value = gains[index - 1] + fraction * item[2]
    return value, index - 1, fraction, item[0]


def prepare_endpoint_data(
    ramified: list[Ideal], useful: list[Ideal]
) -> tuple[Decimal, Frontier, Decimal]:
    log_rd = Decimal(D).ln() / 2 + sum(
        Decimal(ideal[0]).ln() / 4 for ideal in ramified
    )
    increments, maximum_omitted = build_frontier(useful)
    return log_rd, cumulative_frontier(increments), maximum_omitted


def evaluate_prepared(
    log_rd: Decimal,
    frontier: Frontier,
    alpha: Decimal,
    anchor: Decimal,
) -> list[tuple[Decimal, Decimal, Decimal, int, Decimal, Decimal]]:
    constant = Decimal(SAFE_C.numerator) / Decimal(SAFE_C.denominator)
    records = []
    for endpoint in (1, 2):
        scale = Decimal(endpoint)
        w = scale * anchor
        value, index, fraction, slope = fast_envelope(
            frontier, 2 * alpha * w
        )
        exponent = 2 * (2 * alpha - 1) * w - log_rd
        ratio = exponent.exp() / constant
        rhs = (
            constant.ln()
            + log_rd
            + (2 - 4 * alpha) * w
            + (1 + ratio).ln()
        )
        margin = value - rhs - EPSILON
        derivative = (
            2 * alpha * scale * slope
            - (2 - 4 * alpha) * scale
            - 2 * (2 * alpha - 1) * scale * ratio / (1 + ratio)
        )
        records.append(
            (margin, derivative, slope, index, fraction, value)
        )
    return records


def optimize_endpoint(
    ramified: list[Ideal], useful: list[Ideal], advertised_alpha: Decimal
):
    log_rd, frontier, maximum_omitted = prepare_endpoint_data(
        ramified, useful
    )

    def endpoint_root(anchor: Decimal, endpoint_index: int):
        low, high = Decimal("0.48"), Decimal("0.51")
        assert evaluate_prepared(log_rd, frontier, low, anchor)[
            endpoint_index
        ][0] < 0
        assert evaluate_prepared(log_rd, frontier, high, anchor)[
            endpoint_index
        ][0] > 0
        for _ in range(110):
            middle = (low + high) / 2
            if evaluate_prepared(log_rd, frontier, middle, anchor)[
                endpoint_index
            ][0] > 0:
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
            high_w = middle_w
        else:
            low_w, low_difference = middle_w, middle_difference
    anchor = (low_w + high_w) / 2
    brackets = [endpoint_root(anchor, index) for index in (0, 1)]
    threshold = max(sum(bracket) / 2 for bracket in brackets)
    records = evaluate_prepared(log_rd, frontier, advertised_alpha, anchor)
    return threshold, anchor, brackets, records, log_rd, maximum_omitted


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
    packing_constant_audit()
    primes = prime_sieve(180_000)
    assert D == 7 * 11 * 337 * 433
    assert D % 8 == 5 and 1 + 4 * C == D
    assert all(D % (prime * prime) for prime in primes if prime * prime <= D)
    ideals = prime_ideals(primes, 180_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_063, 1_063, "split", 963)

    kernel, metadata = exact_kummer_kernel()
    assert metadata == (1, 28, 56, 1, 0, 219, 4, 215, 1063, 963)
    saturation_rows, saturation_rank = exact_saturation_probe()

    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if norm((a, b)) % 2
    ]
    square_residues = {
        tuple(value % 4 for value in multiply(unit, unit))
        for unit in units_mod_four
    }
    assert len(units_mod_four) == 12 and len(square_residues) == 3
    for element in kernel:
        assert negative_at_embedding(element, False) == 0
        assert negative_at_embedding(element, True) == 0
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
        result = optimize_endpoint(ramified, useful, SAFE_ALPHA)
        threshold, _, brackets, records, _, maximum_omitted = result
        assert SAFE_ALPHA - Decimal("2e-8") < threshold < SAFE_ALPHA
        assert abs(threshold - EXPECTED_THRESHOLD) < Decimal("1e-50")
        assert min(record[0] for record in records) > Decimal("0.001")
        assert records[0][1] > Decimal("0.001")
        assert records[1][1] < Decimal("-0.001")
        assert maximum_omitted < min(record[2] for record in records)
        assert all(
            SAFE_ALPHA - Decimal("2e-8") < low < high < SAFE_ALPHA
            for low, high in brackets
        )
        outputs.append(result)
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-90")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-85")

    fallbacks = []
    getcontext().prec = 80
    for excess, safe_alpha in (
        (1, Decimal("0.4936834")),
        (5, Decimal("0.4936837")),
    ):
        fallback = optimize_endpoint(
            ramified, useful[:-excess], safe_alpha
        )
        threshold, _, _, records, _, maximum_omitted = fallback
        relation_bound_fallback = (
            GENERATOR_RANK + 1 + excess + T_COUNT + USEFUL_COUNT - excess
        )
        assert relation_bound_fallback == relation_bound
        assert threshold < safe_alpha
        assert min(record[0] for record in records) > 0
        assert maximum_omitted < min(record[2] for record in records)
        fallbacks.append((excess, safe_alpha, threshold))

    result = outputs[-1]
    print("PARI BNF / class / narrow / localized class: PASS")
    print("V_T saturation rows / rank:", saturation_rows, saturation_rank)
    print("T / d / relations:", T_COUNT, GENERATOR_RANK, relation_bound)
    print("last T ideal:", ramified[-1])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("maximum usefulness trials:", maximum_trials)
    print("threshold / anchor:", result[0], result[1])
    print("150-digit endpoint margins:", *(record[0] for record in result[3]))
    print("log real-tower root discriminant:", result[4])
    print("maximum omitted slope:", result[5])
    print("desaturated fallbacks (relation excess, safe, threshold):")
    for fallback in fallbacks:
        print(" ", fallback)
    print("CM quadratic-11235917 F_2(n) << n^0.49368323: CERTIFIED")


if __name__ == "__main__":
    main()
