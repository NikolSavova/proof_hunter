#!/usr/bin/env python3
"""Exact-arithmetic certificate for the CM/Eisenstein Q(sqrt(43133)) record.

Requires PARI/GP (tested with GP 2.17.4) for the exact BNF/S-unit/ray-group
calculation.  All prime enumeration, Frobenius tests, Golod--Shafarevich
budgeting, and 90/150-digit endpoint checks are independently redone here.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from math import isqrt
import re
import shutil
import subprocess


FIELD_DISCRIMINANT = 43_133
OMEGA_CONSTANT = (FIELD_DISCRIMINANT - 1) // 4
RAMIFIED_IDEAL_COUNT = 223
SAFE_GENERATOR_RANK = 221
USEFUL_IDEAL_COUNT = 11_765
ALPHA = Decimal(49_369_772) / Decimal(100_000_000)  # 0.49369772
W0 = Decimal("42282.88")
NUMERICAL_ALLOWANCE = Decimal("1e-25")
PACKING_CONSTANT_FRACTION = Fraction(71_603, 64_935)


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [n for n in range(2, limit + 1) if sieve[n]]


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
    a, b = element
    return a * a + a * b - OMEGA_CONSTANT * b * b


def multiply(
    left: tuple[int, int], right: tuple[int, int]
) -> tuple[int, int]:
    a, b = left
    x, y = right
    return (
        a * x + OMEGA_CONSTANT * b * y,
        a * y + b * x + b * y,
    )


def negative_at_embedding(element: tuple[int, int], conjugate_place: bool) -> int:
    """Exact sign of a+b(1+/-sqrt(D))/2."""
    a, b = element
    rational_part = 2 * a + b
    radical_part = -b if conjugate_place else b
    if rational_part >= 0 and radical_part >= 0:
        return 0
    if rational_part <= 0 and radical_part <= 0:
        return 1
    rational_square = rational_part * rational_part
    radical_square = radical_part * radical_part * FIELD_DISCRIMINANT
    assert rational_square != radical_square
    if rational_part > 0:
        return int(rational_square < radical_square)
    return int(radical_square < rational_square)


def tonelli_shanks(value: int, p: int) -> int:
    value %= p
    assert value and pow(value, (p - 1) // 2, p) == 1
    if p % 4 == 3:
        return pow(value, (p + 1) // 4, p)
    odd_part = p - 1
    power_of_two = 0
    while odd_part % 2 == 0:
        power_of_two += 1
        odd_part //= 2
    nonresidue = 2
    while pow(nonresidue, (p - 1) // 2, p) != p - 1:
        nonresidue += 1
    m = power_of_two
    c = pow(nonresidue, odd_part, p)
    t = pow(value, odd_part, p)
    root = pow(value, (odd_part + 1) // 2, p)
    while t != 1:
        index = 1
        test = t * t % p
        while test != 1:
            test = test * test % p
            index += 1
        multiplier = pow(c, 1 << (m - index - 1), p)
        root = root * multiplier % p
        t = t * multiplier * multiplier % p
        c = multiplier * multiplier % p
        m = index
    assert root * root % p == value
    return root


def prime_ideals(primes: list[int], norm_limit: int):
    ideals: list[tuple[int, int, str, int | None]] = []
    for p in primes:
        if p == 2 or p > norm_limit:
            continue
        if FIELD_DISCRIMINANT % p == 0:
            ideals.append((p, p, "ramified", (p + 1) // 2))
            continue
        symbol = pow(FIELD_DISCRIMINANT % p, (p - 1) // 2, p)
        if symbol == 1:
            square_root = tonelli_shanks(FIELD_DISCRIMINANT, p)
            inverse_two = (p + 1) // 2
            roots = sorted(
                {
                    (1 + square_root) * inverse_two % p,
                    (1 - square_root) * inverse_two % p,
                }
            )
            assert len(roots) == 2
            ideals.extend((p, p, "split", root) for root in roots)
        else:
            assert symbol == p - 1
            if p * p <= norm_limit:
                ideals.append((p * p, p, "inert", None))
    ideals.sort(key=lambda row: (row[0], row[1], row[2], row[3] or -1))
    return ideals


def exact_kummer_kernel() -> tuple[list[tuple[int, int]], tuple[int, ...]]:
    """Ask GP for a rigorously certified BNF and exact ray-square kernel."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    # GP parses standard input one complete expression per line, so every
    # loop/vector expression is deliberately kept on one physical line.
    script = rf"""D={FIELD_DISCRIMINANT};c=(D-1)/4;bnf=bnfinit(x^2-x-c,1);cert=bnfcertify(bnf);nf=bnf.nf;
ideals=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(ideals,[Q,p,dec[i]]))));
ideals=vecsort(Vec(ideals),[1,2]);S=ideals[1..{RAMIFIED_IDEAL_COUNT}];units=bnfunits(bnf,vector(#S,i,S[i][3]));bid=idealstar(nf,[4,[1,1]],1,2);mm=Mat(vector(#units[1],i,ideallog(nf,units[1][i],bid)));kk=matker(Mod(mm,2));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),S[#S][3]));
print("META,",cert,",",bnf.no,",",#units[1],",",matrank(Mod(mm,2)),",",matsize(kk)[2],",",S[#S][1],",",lastroot);
elements=vector(matsize(kk)[2],j,my(indices=select(i->lift(kk[i,j])==1,[1..#units[1]]),factorization=units[1][indices[1]]);for(z=2,#indices,factorization=matconcat([factorization;units[1][indices[z]]]));nffactorback(nf,factorization));
for(j=1,#elements,if(type(elements[j])=="t_INT",print(elements[j],",0"),print(elements[j][1],",",elements[j][2])));
"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "2G"], input=script, text=True
    )
    lines = output.splitlines()
    metadata_line = next(line for line in lines if line.startswith("META,"))
    metadata = tuple(map(int, metadata_line.split(",")[1:]))
    elements = [
        tuple(map(int, line.split(",")))
        for line in lines
        if re.fullmatch(r"-?\d+,-?\d+", line)
    ]
    return elements, metadata


def local_increment(norm_q: int, depth: int) -> Decimal:
    q = Decimal(norm_q)
    parameter = Decimal(1) / (q * q)
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


def endpoint_certificate(
    ramified_ideals: list[tuple[int, int, str, int | None]],
    useful_ideals: list[tuple[int, int, str, int | None]],
    precision: int,
):
    getcontext().prec = precision
    packing_constant = Decimal(PACKING_CONSTANT_FRACTION.numerator) / Decimal(
        PACKING_CONSTANT_FRACTION.denominator
    )
    log_root_discriminant = Decimal(FIELD_DISCRIMINANT).ln() / 2
    for norm_q, _, _, _ in ramified_ideals:
        log_root_discriminant += Decimal(norm_q).ln() / 4

    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_fourth_slope = Decimal(0)
    for ideal_index, (norm_q, _, _, _) in enumerate(useful_ideals):
        cost = Decimal(norm_q).ln() / 2
        previous_gain: Decimal | None = None
        for depth in range(1, 5):
            gain = local_increment(norm_q, depth) / 2
            if previous_gain is not None:
                assert previous_gain > gain
            previous_gain = gain
            slope = gain / cost
            if depth <= 3:
                increments.append(
                    (slope, cost, gain, norm_q, depth, ideal_index)
                )
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    increments.sort(reverse=True)

    seen = {index: 0 for index in range(USEFUL_IDEAL_COUNT)}
    for _, _, _, _, depth, ideal_index in increments:
        assert depth == seen[ideal_index] + 1
        seen[ideal_index] = depth

    def envelope(target: Decimal) -> tuple[Decimal, int, Decimal, Decimal]:
        cost_sum = Decimal(0)
        gain_sum = Decimal(0)
        for index, (slope, cost, gain, _, _, _) in enumerate(increments):
            if cost_sum + cost >= target:
                fraction = (target - cost_sum) / cost
                assert 0 <= fraction <= 1
                return gain_sum + fraction * gain, index, fraction, slope
            cost_sum += cost
            gain_sum += gain
        raise AssertionError("target exceeds certified frontier")

    def rhs(alpha: Decimal, w: Decimal) -> Decimal:
        exponent = 2 * (2 * alpha - 1) * w - log_root_discriminant
        correction = (Decimal(1) + exponent.exp() / packing_constant).ln()
        return (
            packing_constant.ln()
            + log_root_discriminant
            + (2 - 4 * alpha) * w
            + correction
        )

    left = envelope(2 * ALPHA * W0)
    right = envelope(4 * ALPHA * W0)
    assert maximum_fourth_slope < right[3]
    margins = (
        left[0] - rhs(ALPHA, W0) - NUMERICAL_ALLOWANCE,
        right[0] - rhs(ALPHA, 2 * W0) - NUMERICAL_ALLOWANCE,
    )
    assert min(margins) > Decimal("0.0001")

    def endpoint_margin(alpha: Decimal, endpoint: int) -> Decimal:
        if endpoint == 1:
            return envelope(2 * alpha * W0)[0] - rhs(alpha, W0)
        assert endpoint == 2
        return envelope(4 * alpha * W0)[0] - rhs(alpha, 2 * W0)

    brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (1, 2):
        # ALPHA is the advertised rounded endpoint.  Certify that the true
        # crossing lies in the final two units of its eighth decimal place.
        low = ALPHA - Decimal("0.00000002")
        high = ALPHA
        assert endpoint_margin(low, endpoint) < 0
        assert endpoint_margin(high, endpoint) > 0
        for _ in range(120):
            middle = (low + high) / 2
            if endpoint_margin(middle, endpoint) > 0:
                high = middle
            else:
                low = middle
        assert high - low < Decimal("1e-40")
        brackets.append((low, high))
    return (
        packing_constant,
        log_root_discriminant,
        left,
        right,
        maximum_fourth_slope,
        margins,
        brackets,
    )


def main() -> None:
    # Exact rational upper bound for the effective Eisenstein disk constant.
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
        == PACKING_CONSTANT_FRACTION
    )

    primes = prime_sieve(200_000)
    assert all(
        FIELD_DISCRIMINANT % p
        for p in primes
        if p * p <= FIELD_DISCRIMINANT
    )
    assert FIELD_DISCRIMINANT % 4 == 1
    assert FIELD_DISCRIMINANT % 8 == 5
    assert 1 + 4 * OMEGA_CONSTANT == FIELD_DISCRIMINANT

    ideals = prime_ideals(primes, 200_000)
    ramified_ideals = ideals[:RAMIFIED_IDEAL_COUNT]
    assert ramified_ideals[-1] == (1_163, 1_163, "split", 646)

    kernel_elements, metadata = exact_kummer_kernel()
    # cert, class number, S-unit generators, ray-square rank, kernel rank,
    # last T norm, and the residue of omega at the final prime.
    assert metadata == (1, 1, 225, 4, 221, 1_163, 646)
    assert len(kernel_elements) == SAFE_GENERATOR_RANK

    # Independently audit that every displayed kernel element is totally
    # positive and square modulo 4.  Since D=5 mod 8, O_E/4 has 12 units and
    # three unit squares.
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

    square_residues = {
        multiply_mod_four(unit, unit) for unit in units_mod_four
    }
    assert len(units_mod_four) == 12 and len(square_residues) == 3
    for element in kernel_elements:
        assert negative_at_embedding(element, False) == 0
        assert negative_at_embedding(element, True) == 0
        assert (element[0] % 4, element[1] % 4) in square_residues

    # Correct CM useful-prime criterion.  For Q=2 mod 3, one exhibited
    # nonresidue kernel element proves that the Frobenius functional is
    # nonzero; the square cap then forces exact relative residue degree two.
    useful_ideals: list[tuple[int, int, str, int | None]] = []
    rejected_ideals: list[tuple[int, int, str, int | None]] = []
    maximum_kernel_trials = 0
    base_ramified_position: int | None = None
    for ideal in ideals[RAMIFIED_IDEAL_COUNT:]:
        norm_q, p, kind, root = ideal
        if p == 3:
            continue
        useful = True
        if norm_q % 3 == 2:
            assert norm_q == p and root is not None
            useful = False
            trials = 0
            for a, b in kernel_elements:
                trials += 1
                residue = (a + b * root) % p
                assert residue
                if pow(residue, (p - 1) // 2, p) == p - 1:
                    useful = True
                    break
            maximum_kernel_trials = max(maximum_kernel_trials, trials)
        if useful:
            useful_ideals.append(ideal)
            if p == FIELD_DISCRIMINANT and kind == "ramified":
                base_ramified_position = len(useful_ideals)
        else:
            rejected_ideals.append(ideal)
        if len(useful_ideals) == USEFUL_IDEAL_COUNT:
            break
    assert len(useful_ideals) == USEFUL_IDEAL_COUNT
    assert not rejected_ideals
    assert useful_ideals[-1] == (129_629, 129_629, "split", 2_193)
    assert base_ramified_position == 4_191
    assert maximum_kernel_trials == 12

    relation_bound = (
        SAFE_GENERATOR_RANK
        + 1
        + RAMIFIED_IDEAL_COUNT
        + USEFUL_IDEAL_COUNT
    )
    assert relation_bound == 12_210
    assert 4 * relation_bound == SAFE_GENERATOR_RANK**2 - 1

    outputs = [
        endpoint_certificate(ramified_ideals, useful_ideals, precision)
        for precision in (90, 150)
    ]
    high_precision = outputs[-1]
    print("PARI BNF / class-number certification: PASS")
    print("ramified ideals / last:", len(ramified_ideals), ramified_ideals[-1])
    print("S-units / ray rank / d:", metadata[2], metadata[3], metadata[4])
    print(
        "useful / rejected / last:",
        len(useful_ideals),
        len(rejected_ideals),
        useful_ideals[-1],
    )
    print("base-ramified useful position:", base_ramified_position)
    print("maximum sparse-kernel trials:", maximum_kernel_trials)
    print("generator / relations:", SAFE_GENERATOR_RANK, relation_bound)
    print("safe CM constant:", high_precision[0])
    print("log real-tower root discriminant:", high_precision[1])
    print("left / right:", high_precision[2], high_precision[3])
    print(
        "right / maximum fourth slopes:",
        high_precision[3][3],
        high_precision[4],
    )
    print("90-digit margins:", *outputs[0][5])
    print("150-digit margins:", *high_precision[5])
    print("fixed-anchor threshold brackets:", *high_precision[6])
    print("CM quadratic-43133 F_2(n) << n^0.49369772: CERTIFIED")


if __name__ == "__main__":
    main()
