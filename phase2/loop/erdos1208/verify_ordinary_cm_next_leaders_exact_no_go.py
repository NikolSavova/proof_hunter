#!/usr/bin/env python3
"""Exact no-go audit for the next ordinary CM screen leaders.

Fields: 979277, 994733, and 544268.  PARI/GP certifies the class/S-unit/ray
data.  Python independently enumerates prime ideals, performs the exact
mod-3 useful test at the optimistic best T, and gives an all-anchor
all-useful exclusion for every 205 <= T <= 250.
"""

from __future__ import annotations

import bisect
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys

import verify_hostile_quadratic43133_cm as elementary


sys.set_int_max_str_digits(100_000)
getcontext().prec = 100

ALPHA = Decimal("0.49369313")
SAFE_C = Fraction(71_603, 64_935)
C_UPPER = Decimal(SAFE_C.numerator) / Decimal(SAFE_C.denominator)


@dataclass(frozen=True)
class FieldCase:
    discriminant: int
    best_t: int
    expected_class_number: int
    expected_narrow_number: int
    expected_last: tuple[int, int, str, int | None]

    @property
    def even(self) -> bool:
        return self.discriminant % 4 == 0

    @property
    def radicand(self) -> int:
        return self.discriminant // 4 if self.even else self.discriminant

    @property
    def polynomial(self) -> str:
        if self.even:
            return f"x^2-{self.radicand}"
        return f"x^2-x-{(self.discriminant - 1) // 4}"


CASES = (
    FieldCase(979_277, 209, 2, 2, (1_217, 1_217, "split", 776)),
    FieldCase(994_733, 211, 1, 2, (1_201, 1_201, "split", 880)),
    FieldCase(544_268, 221, 1, 2, (1_117, 1_117, "split", 567)),
)


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


def prime_ideals(
    case: FieldCase, primes: list[int], norm_limit: int
) -> list[tuple[int, int, str, int | None]]:
    ideals: list[tuple[int, int, str, int | None]] = []
    for p in primes:
        if p == 2 or p > norm_limit:
            continue
        if case.radicand % p == 0:
            root = 0 if case.even else (p + 1) // 2
            ideals.append((p, p, "ramified", root))
            continue
        residue = case.radicand % p if case.even else case.discriminant % p
        symbol = pow(residue, (p - 1) // 2, p)
        if symbol == 1:
            square_root = elementary.tonelli_shanks(residue, p)
            if case.even:
                roots = sorted({square_root, (-square_root) % p})
            else:
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
    ideals.sort(
        key=lambda row: (
            row[0],
            row[1],
            row[2],
            row[3] if row[3] is not None else -1,
        )
    )
    return ideals


def exact_gp_data(
    case: FieldCase,
) -> tuple[list[tuple[int, int]], list[int], tuple[int, int, int, int]]:
    """Certify the nested ray ranks and return an exact S-unit basis.

    Calling ``bnfunits`` on a 200-prime set is needlessly expensive in fields
    with a huge fundamental unit.  Instead we construct the squareclass basis
    directly.  In class number one it consists of the two global unit classes
    and one principal generator per S-prime.  For D=979277, Cl=C2 is generated
    by the ramified ideal R above 13: add a generator of R^2, use a principal
    generator for each principal P, and a generator of PR for every other
    nonprincipal P.  These are independent by their valuation vectors and the
    exact Kummer sequence.

    The ray image has ambient dimension four.  Rank four on the first 207
    basis elements (the basis for S_205) forces rank four for all larger
    nested S_T.
    """
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    class_check = ""
    basis_builder = (
        "U=bnfunits(b);G=List();"
        "for(i=1,#U[1],listput(G,nffactorback(nf,U[1][i])));"
    )
    if case.discriminant == 979_277:
        # The ramified ideal above 13 is the generator of Cl(E)=C2, hence
        # localization at every audited T kills the S-class 2-torsion.
        class_check = (
            'P13=idealprimedec(nf,13)[1];'
            'print("CLASS13,",concat(Vec(bnfisprincipal(b,P13,0))));'
        )
        basis_builder += (
            "z=bnfisprincipal(b,idealpow(nf,P13,2))[2];listput(G,z);"
            f"for(i=1,{case.best_t},P=L[i][3];"
            "if(!(L[i][1]==13&&L[i][2]==13),"
            "cl=bnfisprincipal(b,P,0);"
            "if(cl[1]==0,z=bnfisprincipal(b,P)[2],"
            "z=bnfisprincipal(b,idealmul(nf,P,P13))[2]);"
            "listput(G,z)));"
        )
    else:
        basis_builder += (
            f"for(i=1,{case.best_t},P=L[i][3];"
            "z=bnfisprincipal(b,P)[2];listput(G,z));"
        )
    script = rf"""default(nbthreads,1);default(realprecision,2000);D={case.discriminant};b=bnfinit({case.polynomial},1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);print("HEADER,",cert,",",b.no,",",nar[1],",",bid.cyc);{class_check}L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);{basis_builder}S=L[1..{case.best_t}];lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),S[#S][3]));print("BEST,",#G,",",S[#S][1],",",lastroot);for(i=1,#G,z=G[i];v=ideallog(nf,z,bid);print("ELEMENT,",if(type(z)=="t_INT",z,z[1]),",",if(type(z)=="t_INT",0,z[2]),",",concat(Vec(v))))"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=90
    )
    lines = output.splitlines()
    assert (
        f"HEADER,1,{case.expected_class_number},{case.expected_narrow_number},"
        "[2, 2, 2, 2]"
    ) in lines
    if case.discriminant == 979_277:
        assert "CLASS13,1" in lines

    elements: list[tuple[int, int]] = []
    columns: list[int] = []
    best_metadata: tuple[int, int, int, int] | None = None
    vector_pattern = r"\[([01]), ([01]), ([01]), ([01])\]"
    for line in lines:
        match = re.fullmatch(r"BEST,(\d+),(\d+),(-?\d+)", line)
        if match:
            count, norm_q, root = map(int, match.groups())
            best_metadata = (count, 0, norm_q, root)
            continue
        match = re.fullmatch(
            r"ELEMENT,(-?\d+),(-?\d+)," + vector_pattern, line
        )
        if match:
            elements.append(tuple(map(int, match.group(1, 2))))
            columns.append(
                sum(int(match.group(3 + index)) << index for index in range(4))
            )

    assert best_metadata is not None
    assert gf2_rank(columns[:207]) == 4
    assert gf2_rank(columns) == 4
    best_metadata = (
        best_metadata[0],
        gf2_rank(columns),
        best_metadata[2],
        best_metadata[3],
    )
    assert best_metadata[:2] == (case.best_t + 2, 4)
    assert best_metadata[2:] == (
        case.expected_last[0],
        case.expected_last[3],
    )
    assert len(elements) == case.best_t + 2 == len(columns)
    return elements, columns, best_metadata


def local_gain(norm_q: int, depth: int) -> Decimal:
    q = Decimal(norm_q)
    parameter = Decimal(1) / (q * q)
    power = Decimal(1)
    total = Decimal(1)
    previous_total = Decimal(1)
    for _ in range(1, depth + 1):
        previous_total = total
        power *= parameter
        total += power
    current = Decimal(depth + 1) / total
    previous = Decimal(depth) / previous_total
    return (current / previous).ln() / 4


def optimistic_no_go(
    case: FieldCase,
    ideals: list[tuple[int, int, str, int | None]],
) -> tuple[int, Decimal, Decimal, Decimal, Decimal, Decimal]:
    """Exclude every anchor for every 205<=T<=250 under all-useful data."""
    # Split primes occur twice, and the T-frontiers overlap almost completely.
    # Cache the high-precision transcendental data by ideal norm; recomputing it
    # inside all 46 frontiers makes this exact verifier unnecessarily slow.
    profiles: dict[int, tuple[Decimal, tuple[Decimal, ...]]] = {}

    def profile(norm_q: int) -> tuple[Decimal, tuple[Decimal, ...]]:
        if norm_q not in profiles:
            cost = Decimal(norm_q).ln() / 2
            profiles[norm_q] = (
                cost,
                tuple(local_gain(norm_q, depth) for depth in range(1, 5)),
            )
        return profiles[norm_q]

    best: tuple[int, Decimal, Decimal, Decimal, Decimal, Decimal] | None = None
    for t in range(205, 251):
        d = t - 2
        useful_count = (d * d - 1) // 4 - (d + 1) - t
        useful = ideals[t : t + useful_count]
        assert len(useful) == useful_count

        increments: list[tuple[Decimal, Decimal, Decimal]] = []
        maximum_fourth = Decimal(0)
        for norm_q, _, _, _ in useful:
            cost, depth_gains = profile(norm_q)
            previous: Decimal | None = None
            for depth, gain in enumerate(depth_gains, start=1):
                if previous is not None:
                    assert previous > gain
                previous = gain
                slope = gain / cost
                if depth <= 3:
                    increments.append((slope, cost, gain))
                else:
                    maximum_fourth = max(maximum_fourth, slope)
        increments.sort(reverse=True)
        costs = [Decimal(0)]
        gains = [Decimal(0)]
        for _, cost, gain in increments:
            costs.append(costs[-1] + cost)
            gains.append(gains[-1] + gain)

        log_rd = Decimal(case.discriminant).ln() / 2
        log_rd += sum(profile(row[0])[0] / 2 for row in ideals[:t])

        def envelope(target: Decimal) -> tuple[Decimal, Decimal]:
            index = bisect.bisect_left(costs, target)
            assert 0 < index < len(costs)
            fraction = (target - costs[index - 1]) / (
                costs[index] - costs[index - 1]
            )
            value = gains[index - 1] + fraction * (
                gains[index] - gains[index - 1]
            )
            return value, increments[index - 1][0]

        def endpoint(anchor: Decimal, scale: int) -> tuple[Decimal, Decimal, Decimal]:
            scale_decimal = Decimal(scale)
            w = scale_decimal * anchor
            value, slope = envelope(2 * ALPHA * w)
            exponent = 2 * (2 * ALPHA - 1) * w - log_rd
            ratio = exponent.exp() / C_UPPER
            rhs = (
                C_UPPER.ln()
                + log_rd
                + (2 - 4 * ALPHA) * w
                + (Decimal(1) + ratio).ln()
            )
            margin = value - rhs
            derivative = (
                2 * ALPHA * scale_decimal * slope
                - (2 - 4 * ALPHA) * scale_decimal
                - 2
                * (2 * ALPHA - 1)
                * scale_decimal
                * ratio
                / (Decimal(1) + ratio)
            )
            return margin, derivative, slope

        low, high = Decimal("20000"), Decimal("70000")
        low_difference = endpoint(low, 1)[0] - endpoint(low, 2)[0]
        high_difference = endpoint(high, 1)[0] - endpoint(high, 2)[0]
        # On the left the scale-one endpoint is the smaller constraint; on
        # the right the scale-two endpoint is smaller.
        assert low_difference < 0 < high_difference
        for _ in range(90):
            middle = (low + high) / 2
            difference = endpoint(middle, 1)[0] - endpoint(middle, 2)[0]
            if low_difference * difference <= 0:
                high = middle
            else:
                low, low_difference = middle, difference
        anchor = (low + high) / 2
        left = endpoint(anchor, 1)
        right = endpoint(anchor, 2)
        assert left[0] < Decimal("-0.1") and right[0] < Decimal("-0.1")
        assert left[1] > Decimal("0.001") and right[1] < Decimal("-0.001")
        assert maximum_fourth < right[2]
        record = (t, min(left[0], right[0]), anchor, left[1], right[1], log_rd)
        if best is None or record[1] > best[1]:
            best = record
    assert best is not None and best[0] == case.best_t
    return best


def useful_scan(
    case: FieldCase,
    ideals: list[tuple[int, int, str, int | None]],
    elements: list[tuple[int, int]],
    columns: list[int],
) -> tuple[int, tuple[int, int, str, int | None], list[tuple[int, int, str, int | None]]]:
    constraint_rows = [
        sum(((column >> bit) & 1) << index for index, column in enumerate(columns))
        for bit in range(4)
    ]
    assert gf2_rank(constraint_rows) == 4
    d = len(elements) - 4
    assert d == case.best_t - 2
    useful_count = (d * d - 1) // 4 - (d + 1) - case.best_t

    useful: list[tuple[int, int, str, int | None]] = []
    rejected: list[tuple[int, int, str, int | None]] = []
    for ideal in ideals[case.best_t :]:
        norm_q, p, _, root = ideal
        if p == 3:
            continue
        is_useful = True
        if norm_q % 3 == 2:
            assert norm_q == p and root is not None
            functional = 0
            for index, (a, b) in enumerate(elements):
                residue = (a + b * root) % p
                assert residue
                if pow(residue, (p - 1) // 2, p) == p - 1:
                    functional |= 1 << index
            is_useful = gf2_rank(constraint_rows + [functional]) > 4
        if is_useful:
            useful.append(ideal)
        else:
            rejected.append(ideal)
        if len(useful) == useful_count:
            break
    assert len(useful) == useful_count
    return useful_count, useful[-1], rejected


def main() -> None:
    primes = elementary.prime_sieve(180_000)
    results = {}
    for case in CASES:
        assert case.discriminant > 0
        if case.even:
            assert case.radicand % 4 in (2, 3)
        else:
            assert case.discriminant % 4 == 1
        assert all(
            case.radicand % (p * p)
            for p in primes
            if p * p <= case.radicand
        )
        ideals = prime_ideals(case, primes, 180_000)
        assert ideals[case.best_t - 1] == case.expected_last
        elements, columns, metadata = exact_gp_data(case)
        no_go = optimistic_no_go(case, ideals)
        useful = useful_scan(case, ideals, elements, columns)
        results[case.discriminant] = (metadata, no_go, useful)

    for discriminant, result in results.items():
        print("D=", discriminant)
        print("  best metadata:", result[0])
        print("  all-useful all-anchor no-go:", result[1])
        print("  exact useful count / last / rejects:", result[2])
    print("ordinary next-leader exact no-go: CERTIFIED")


if __name__ == "__main__":
    main()
