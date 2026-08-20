#!/usr/bin/env python3
"""Fixed-T structural/mixed-inertia lock for the D=6999893 CM record."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import re
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_hostile_quadratic821453_cm as base  # noqa: E402
import verify_quadratic821453_cm_mixed_assignment_lock as mixed  # noqa: E402


D = 6_999_893
T_COUNT = 219
SAFE_ALPHA = Decimal("0.49368416")
WINNER_RANK = 217
WINNER_USEFUL = 11_335
WINNER_ANCHOR = Decimal("40670.9061212898227878623498934")


@dataclass
class StructuralCase:
    name: str
    mode: str
    subspace: frozenset[int]
    odd_coset: frozenset[int] | None
    generator_rank: int
    selected_rows: list[tuple[int, int, int | None, int, int]]


def configure() -> None:
    getcontext().prec = 85
    base.D = D
    base.C = (D - 1) // 4
    base.T_COUNT = T_COUNT
    base.GENERATOR_RANK = WINNER_RANK
    base.USEFUL_COUNT = WINNER_USEFUL
    base.ALPHA = SAFE_ALPHA
    base.SAFE_C = Fraction(71_603, 64_935)
    base.elementary.FIELD_DISCRIMINANT = D
    base.elementary.OMEGA_CONSTANT = (D - 1) // 4
    base.elementary.RAMIFIED_IDEAL_COUNT = T_COUNT
    mixed.T_COUNT = T_COUNT
    mixed.ALPHA = SAFE_ALPHA
    mixed._LOCAL_CACHE.clear()


def bits(match: re.Match[str], offset: int) -> int:
    return sum(int(match.group(offset + index)) << index for index in range(4))


def exact_colored_ideals():
    """Return normalized C4 class labels and compatible exact ray colors."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);nf=b.nf;bid=idealstar(nf,[4,[1,1]],1,2);U=bnfunits(b);print("META,",bnfcertify(b),",",b.no,",",b.clgp[2],",",bnfnarrow(b)[1],",",bid.cyc);for(i=1,#U[1],z=nffactorback(nf,U[1][i]);print("UNIT,",concat(Vec(ideallog(nf,z,bid)))));L=List();forprime(p=3,20000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=20000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,#L,a=lift(bnfisprincipal(b,L[i][3],0)[1]);if(ref==0&&gcd(a,4)==1,ref=i));R=L[ref][3];ra=lift(bnfisprincipal(b,R,0)[1]);ri=lift(Mod(ra,4)^-1);h=bnfisprincipal(b,idealpow(nf,R,4))[2];print("REF,",ref,",",L[ref][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),R)),",",ra,",",concat(Vec(ideallog(nf,h,bid))));for(i=1,#L,P=L[i][3];a=lift(bnfisprincipal(b,P,0)[1]);aa=lift(Mod(a*ri,4));e=lift(-Mod(aa,4));z=bnfisprincipal(b,idealmul(nf,P,idealpow(nf,R,e)))[2];Q=L[i][1];p=L[i][2];rr=-1;if(Q==p,rr=lift(nfmodpr(nf,Mod(x,nf.pol),P)));print("IDEAL,",Q,",",p,",",rr,",",aa,",",concat(Vec(ideallog(nf,z,bid)))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    assert "META,1,4,[4],8,[2, 2, 2, 2]" in lines
    vector_pattern = r"\[([01]), ([01]), ([01]), ([01])\]"
    units: list[int] = []
    reference = None
    raw = []
    for line in lines:
        match = re.fullmatch("UNIT," + vector_pattern, line)
        if match:
            units.append(bits(match, 1))
            continue
        match = re.fullmatch(
            r"REF,(\d+),(\d+),(\d+),(\d+)," + vector_pattern, line
        )
        if match:
            reference = (
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                int(match.group(4)),
                bits(match, 5),
            )
            continue
        match = re.fullmatch(
            r"IDEAL,(\d+),(\d+),(-?\d+),(\d+)," + vector_pattern,
            line,
        )
        if match:
            norm_q, prime, root, ideal_class = map(
                int, match.group(1, 2, 3, 4)
            )
            raw.append(
                (
                    norm_q,
                    prime,
                    None if root < 0 else root,
                    ideal_class,
                    bits(match, 5),
                )
            )
    assert units == [12, 13]
    assert reference == (2, 13, 6, 1, 12)
    assert len(raw) == 2_200
    return units, reference, raw


def vector_span(generators: list[int]) -> set[int]:
    span = {0}
    for generator in generators:
        span |= {value ^ generator for value in list(span)}
    return span


def structural_cases(units, reference, raw):
    # If R has normalized C4 class one and (h)=R^4, then a class-a prime P
    # has a chosen color from a generator of P R^{-a}.  Here h already lies
    # in the global-unit ray span.
    base_span = vector_span(units + [reference[4]])
    assert base_span == {0, 1, 12, 13}
    base_rank = 2

    canonical = lambda value: min(value ^ element for element in base_span)
    quotient = sorted({canonical(value) for value in range(16)})
    assert quotient == [0, 2, 4, 6]
    add = lambda left, right: canonical(left ^ right)
    colored = [row[:-1] + (canonical(row[-1]),) for row in raw]

    subspaces = []
    for mask in range(1 << len(quotient)):
        subset = {
            quotient[index]
            for index in range(len(quotient))
            if (mask >> index) & 1
        }
        if 0 in subset and all(
            add(left, right) in subset for left in subset for right in subset
        ):
            subspaces.append(frozenset(subset))
    assert subspaces == [
        frozenset({0}),
        frozenset({0, 2}),
        frozenset({0, 4}),
        frozenset({0, 6}),
        frozenset({0, 2, 4, 6}),
    ]

    def quotient_rank(generators: list[int]) -> int:
        pivots: dict[int, int] = {}
        for row in generators:
            while row:
                pivot = row.bit_length() - 1
                if pivot in pivots:
                    row = add(row, pivots[pivot])
                else:
                    pivots[pivot] = row
                    break
        return len(pivots)

    cases = []
    for subspace in subspaces:
        # With only even C4 classes selected, Cl_S still has one 2-torsion
        # class.  The pre-ray squareclass dimension is T+3.
        selected = [
            row
            for row in colored
            if row[3] % 2 == 0 and row[4] in subspace
        ][:T_COUNT]
        if len(selected) == T_COUNT:
            qrank = quotient_rank([row[4] for row in selected])
            generator_rank = T_COUNT + 3 - (base_rank + qrank)
            cases.append(
                StructuralCase(
                    f"even_L{''.join(map(str, sorted(subspace)))}",
                    "even",
                    subspace,
                    None,
                    generator_rank,
                    selected,
                )
            )

        # Any odd C4 class kills the whole class group.  Relative to one odd
        # reference, the ray image is generated by all even colors and all
        # pairwise odd-color differences.  Thus the odd colors occupy one
        # affine coset of the even span.
        seen_cosets = set()
        for representative in quotient:
            coset = frozenset(
                add(representative, value) for value in subspace
            )
            if coset in seen_cosets:
                continue
            seen_cosets.add(coset)
            selected = [
                row
                for row in colored
                if (row[3] % 2 == 0 and row[4] in subspace)
                or (row[3] % 2 == 1 and row[4] in coset)
            ][:T_COUNT]
            odd_colors = [row[4] for row in selected if row[3] % 2]
            if len(selected) < T_COUNT or not odd_colors:
                continue
            odd_reference = odd_colors[0]
            generators = [
                row[4] for row in selected if row[3] % 2 == 0
            ]
            generators.extend(
                add(color, odd_reference) for color in odd_colors[1:]
            )
            qrank = quotient_rank(generators)
            generator_rank = T_COUNT + 2 - (base_rank + qrank)
            cases.append(
                StructuralCase(
                    "odd_L"
                    + "".join(map(str, sorted(subspace)))
                    + "_C"
                    + "".join(map(str, sorted(coset))),
                    "odd",
                    subspace,
                    coset,
                    generator_rank,
                    selected,
                )
            )

    assert len(cases) == 16
    signature = sorted(
        (
            case.generator_rank,
            case.selected_rows[-1][0],
            sum(row[3] % 2 for row in case.selected_rows),
        )
        for case in cases
    )
    assert signature == sorted(
        [
            (220, 17_117, 0),
            (219, 5_693, 0),
            (219, 5_927, 114),
            (219, 6_529, 110),
            (219, 6_709, 0),
            (219, 6_977, 106),
            (219, 7_057, 0),
            (219, 7_417, 100),
            (218, 2_551, 104),
            (218, 2_647, 104),
            (218, 2_707, 0),
            (218, 2_833, 100),
            (218, 2_837, 88),
            (218, 2_837, 94),
            (218, 2_837, 98),
            (217, 1_063, 110),
        ]
    )
    return cases, base_span


def weighted_gs_and_uncapped_dominance() -> None:
    for generator_rank in range(217, 221):
        maximum_quadratic = (generator_rank * generator_rank - 1) // 4
        point = Fraction(2, generator_rank)
        for square_count in range(T_COUNT + 1):
            useful_count = (
                maximum_quadratic - (generator_rank + 1) - square_count
            )
            assert useful_count > 0
            quadratic_count = generator_rank + 1 + square_count + useful_count
            assert quadratic_count == maximum_quadratic
            for fourth_count in range(T_COUNT - square_count + 1):
                polynomial = (
                    1
                    - generator_rank * point
                    + quadratic_count * point**2
                    + fourth_count * point**4
                )
                assert polynomial < 0
        # An uncapped inertia role has the same quadratic budget as a fourth
        # cap but a larger root-discriminant exponent (1/2 versus 3/8).
        # The check above shows the added quartic relator remains admissible.

    useful_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_upper = Fraction(729, 6_400)
    assert useful_lower > useful_upper


def exact_endpoint_lock(cases, universe):
    universe_by_key = {
        (row[0], row[1], row[3]): row for row in universe
    }
    canonical_keys = {
        (row[0], row[1], row[3]) for row in universe[:T_COUNT]
    }
    excluded_cells = 0
    worst = None
    summaries = []

    for case in cases:
        keys = {(row[0], row[1], row[2]) for row in case.selected_rows}
        selected = sorted(
            (universe_by_key[key] for key in keys),
            key=lambda row: (
                row[0], row[1], row[2],
                row[3] if row[3] is not None else -1,
            ),
        )
        assert len(selected) == T_COUNT
        candidates = [
            row
            for row in universe
            if (row[0], row[1], row[3]) not in keys
        ]
        case_is_canonical = (
            case.generator_rank == WINNER_RANK and keys == canonical_keys
        )
        assert case_is_canonical == (case.generator_rank == WINNER_RANK)
        case_worst = None

        for fourth_count in range(T_COUNT + 1):
            if case_is_canonical and fourth_count == 0:
                continue
            margin, anchor, records, _ = mixed.endpoint_exclusion(
                selected,
                fourth_count,
                case.generator_rank,
                candidates,
            )
            excluded_cells += 1
            assert margin < Decimal("-0.01")

            # These are the exact role-exchange hypotheses used to pass from
            # an arbitrary assignment in the cell to its smallest permitted
            # ramified roles, smallest fourth-cap roles, and first remaining
            # all-useful roles.
            minimum_log = Decimal(selected[0][0]).ln()
            first_useful = Decimal(candidates[0][0])
            tail = first_useful**-2 / (1 - first_useful**-2) ** 2
            for record in records:
                slope, rho = record[2], record[3]
                assert rho > Decimal(1) / minimum_log
                assert rho > Decimal(2) / (3 * minimum_log)
                assert slope > tail

            cell = (margin, case.name, fourth_count, anchor)
            case_worst = cell if case_worst is None else max(case_worst, cell)
            worst = cell if worst is None else max(worst, cell)
        summaries.append(case_worst)

    assert excluded_cells == 16 * (T_COUNT + 1) - 1 == 3_519
    assert worst is not None
    assert worst[1] == "odd_L0246_C0246"
    assert worst[2] == 1
    assert worst[0] < Decimal("-0.25")

    ramified = universe[:T_COUNT]
    useful = universe[T_COUNT : T_COUNT + WINNER_USEFUL]
    _, records, maximum_omitted = base.endpoint_data(
        ramified, useful, SAFE_ALPHA, WINNER_ANCHOR
    )
    assert min(record[0] for record in records) > Decimal("0.0004")
    assert maximum_omitted < min(record[2] for record in records)
    return excluded_cells, worst, summaries, records


def main() -> None:
    configure()
    weighted_gs_and_uncapped_dominance()
    units, reference, raw = exact_colored_ideals()
    cases, base_span = structural_cases(units, reference, raw)
    primes = base.elementary.prime_sieve(320_000)
    universe = base.elementary.prime_ideals(primes, 320_000)
    excluded, worst, summaries, baseline = exact_endpoint_lock(cases, universe)
    print("base ray span / reference:", base_span, reference)
    print("structural cases:")
    for case, summary in zip(cases, summaries):
        class_counts = {
            residue: sum(row[3] == residue for row in case.selected_rows)
            for residue in range(4)
        }
        print(
            " ",
            case.name,
            "d=", case.generator_rank,
            "last=", case.selected_rows[-1][0],
            "class-counts=", class_counts,
            "worst=", summary,
        )
    print("excluded structural/cap cells / worst:", excluded, worst)
    print("canonical adverse-upper-C records:", baseline)
    print("D=6999893 fixed-T mixed/assignment structural lock: CERTIFIED")


if __name__ == "__main__":
    main()
