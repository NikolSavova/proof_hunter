#!/usr/bin/env python3
"""Fixed-T structural/mixed-inertia lock for the D=4108373 CM record."""

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


D = 4_108_373
T_COUNT = 217
SAFE_ALPHA = Decimal("0.49368647")
WINNER_RANK = 215
WINNER_USEFUL = 11_123
WINNER_ANCHOR = Decimal(
    "39963.8976671829913854190301637607507512228721680003218352794647216796875"
)


@dataclass
class StructuralCase:
    name: str
    mode: str
    subspace: frozenset[int]
    nonprincipal_coset: frozenset[int] | None
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
    base.elementary.FIELD_DISCRIMINANT = D
    base.elementary.OMEGA_CONSTANT = (D - 1) // 4
    base.elementary.RAMIFIED_IDEAL_COUNT = T_COUNT
    mixed.T_COUNT = T_COUNT
    mixed.ALPHA = SAFE_ALPHA
    mixed._LOCAL_CACHE.clear()


def bits(match: re.Match[str], offset: int) -> int:
    return sum(int(match.group(offset + index)) << index for index in range(4))


def exact_colored_ideals():
    """Class/ray colors relative to the first nonprincipal ideal R0."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,3000);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);nf=b.nf;bid=idealstar(nf,[4,[1,1]],1,2);U=bnfunits(b);print("META,",bnfcertify(b),",",b.no,",",bnfnarrow(b)[1],",",bid.cyc);for(i=1,#U[1],z=nffactorback(nf,U[1][i]);print("UNIT,",concat(Vec(ideallog(nf,z,bid)))));L=List();forprime(p=3,16000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=16000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);ref=0;for(i=1,#L,cl=bnfisprincipal(b,L[i][3],0);if(ref==0&&cl[1]!=0,ref=i));R=L[ref][3];h=bnfisprincipal(b,idealpow(nf,R,2))[2];print("REF,",ref,",",L[ref][1],",",lift(nfmodpr(nf,Mod(x,nf.pol),R)),",",concat(Vec(ideallog(nf,h,bid))));for(i=1,#L,P=L[i][3];cl=bnfisprincipal(b,P,0);cc=if(cl[1]==0,0,1);if(cc==0,z=bnfisprincipal(b,P)[2],z=bnfisprincipal(b,idealmul(nf,P,R))[2]);Q=L[i][1];p=L[i][2];rr=-1;if(Q==p,rr=lift(nfmodpr(nf,Mod(x,nf.pol),P)));print("IDEAL,",Q,",",p,",",rr,",",cc,",",concat(Vec(ideallog(nf,z,bid)))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=90
    )
    lines = output.splitlines()
    assert "META,1,2,4,[2, 2, 2, 2]" in lines
    vector_pattern = r"\[([01]), ([01]), ([01]), ([01])\]"
    units = []
    reference = None
    raw = []
    for line in lines:
        match = re.fullmatch("UNIT," + vector_pattern, line)
        if match:
            units.append(bits(match, 1))
            continue
        match = re.fullmatch(
            r"REF,(\d+),(\d+),(\d+)," + vector_pattern, line
        )
        if match:
            reference = (
                int(match.group(1)),
                int(match.group(2)),
                int(match.group(3)),
                bits(match, 4),
            )
            continue
        match = re.fullmatch(
            r"IDEAL,(\d+),(\d+),(-?\d+),([01])," + vector_pattern,
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
    assert units == [1, 13]
    assert reference == (2, 11, 4, 12)
    assert len(raw) > 1_700
    return units, reference, raw


def vector_span(generators: list[int]) -> set[int]:
    span = {0}
    for generator in generators:
        span |= {value ^ generator for value in list(span)}
    return span


def structural_cases(units, reference, raw) -> tuple[list[StructuralCase], set[int]]:
    # If R0 is the fixed nonprincipal reference and (h)=R0^2, then h is
    # already in the two-dimensional global-unit ray span in this field.
    unit_span = vector_span(units)
    assert reference[3] in unit_span and len(unit_span) == 4

    canonical = lambda value: min(value ^ unit for unit in unit_span)
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
        # No selected nonprincipal ideal: Cl_S[2] survives, so the pre-ray
        # Kummer dimension is T+3 rather than T+2.
        selected = [
            row
            for row in colored
            if row[3] == 0 and row[4] in subspace
        ][:T_COUNT]
        if len(selected) == T_COUNT:
            qrank = quotient_rank([row[4] for row in selected])
            generator_rank = T_COUNT + 3 - (2 + qrank)
            cases.append(
                StructuralCase(
                    f"principal_L{''.join(map(str, sorted(subspace)))}",
                    "principal",
                    subspace,
                    None,
                    generator_rank,
                    selected,
                )
            )

        # Some nonprincipal ideal is selected.  Modulo the global units, the
        # extra columns are principal colors a_P and differences b_P+b_R.
        seen_cosets = set()
        for representative in quotient:
            coset = frozenset(add(representative, value) for value in subspace)
            if coset in seen_cosets:
                continue
            seen_cosets.add(coset)
            selected = [
                row
                for row in colored
                if (row[3] == 0 and row[4] in subspace)
                or (row[3] == 1 and row[4] in coset)
            ][:T_COUNT]
            nonprincipal = [row[4] for row in selected if row[3] == 1]
            if len(selected) < T_COUNT or not nonprincipal:
                continue
            reference_color = nonprincipal[0]
            generators = [row[4] for row in selected if row[3] == 0]
            generators.extend(
                add(color, reference_color) for color in nonprincipal[1:]
            )
            qrank = quotient_rank(generators)
            generator_rank = T_COUNT + 2 - (2 + qrank)
            cases.append(
                StructuralCase(
                    "nonprincipal_L"
                    + "".join(map(str, sorted(subspace)))
                    + "_C"
                    + "".join(map(str, sorted(coset))),
                    "nonprincipal",
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
            sum(row[3] for row in case.selected_rows),
        )
        for case in cases
    )
    assert signature == sorted(
        [
            (218, 14_561, 0),
            (217, 6_241, 110),
            (217, 6_469, 0),
            (217, 6_469, 0),
            (217, 6_701, 106),
            (217, 6_889, 105),
            (217, 6_947, 103),
            (217, 7_013, 0),
            (216, 2_617, 111),
            (216, 2_617, 101),
            (216, 2_657, 101),
            (216, 2_741, 107),
            (216, 2_843, 0),
            (216, 2_879, 102),
            (216, 3_119, 96),
            (215, 1_117, 109),
        ]
    )
    return cases, unit_span


def weighted_gs_and_uncapped_dominance() -> None:
    for generator_rank in range(215, 219):
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
        # An uncapped inertia generator and a fourth-power cap cost the same
        # quadratic budget.  The fourth cap strictly lowers its asymptotic RD
        # exponent from 1/2 to 3/8, and the preceding check shows the quartic
        # relation remains GS-admissible.  Hence uncapped cells are dominated.

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
        assert case_is_canonical == (case.generator_rank == 215)
        case_worst = None

        for fourth_count in range(T_COUNT + 1):
            if case_is_canonical and fourth_count == 0:
                continue
            value = mixed.endpoint_exclusion(
                selected,
                fourth_count,
                case.generator_rank,
                candidates,
            )
            margin, anchor, records, _ = value
            excluded_cells += 1
            assert margin < Decimal("-0.01")

            # Exact role-exchange hypotheses: the norm-prefix selected set,
            # smallest fourth-cap roles, and first remaining useful roles are
            # jointly optimistic inside this structural color cell.
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

    assert excluded_cells == 16 * (T_COUNT + 1) - 1 == 3_487
    assert worst is not None
    assert worst[1] == "nonprincipal_L0246_C0246"
    assert worst[2] == 1
    assert worst[0] < Decimal("-0.25")

    # Retain the actual canonical all-square record using the adverse upper
    # packing constant, rather than the favorable lower constant above.
    ramified = universe[:T_COUNT]
    useful = universe[T_COUNT : T_COUNT + WINNER_USEFUL]
    _, records, maximum_omitted = base.endpoint_data(
        ramified, useful, SAFE_ALPHA, WINNER_ANCHOR
    )
    assert min(record[0] for record in records) > Decimal("0.0015")
    assert maximum_omitted < min(record[2] for record in records)
    return excluded_cells, worst, summaries, records


def main() -> None:
    configure()
    weighted_gs_and_uncapped_dominance()
    units, reference, raw = exact_colored_ideals()
    cases, unit_span = structural_cases(units, reference, raw)
    primes = base.elementary.prime_sieve(300_000)
    universe = base.elementary.prime_ideals(primes, 300_000)
    excluded, worst, summaries, baseline = exact_endpoint_lock(cases, universe)
    print("unit span / reference:", unit_span, reference)
    print("structural cases:")
    for case, summary in zip(cases, summaries):
        print(
            " ",
            case.name,
            "d=", case.generator_rank,
            "last=", case.selected_rows[-1][0],
            "nonprincipal=", sum(row[3] for row in case.selected_rows),
            "worst=", summary,
        )
    print("excluded structural/cap cells / worst:", excluded, worst)
    print("canonical adverse-upper-C records:", baseline)
    print("D=4108373 fixed-T mixed/assignment structural lock: CERTIFIED")


if __name__ == "__main__":
    main()
