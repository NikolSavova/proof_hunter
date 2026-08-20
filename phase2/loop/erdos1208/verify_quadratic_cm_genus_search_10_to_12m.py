#!/usr/bin/env python3
"""Genus-bonus screen of 10m < D <= 12m and exact leader audits.

The default mode compiles four independent copies of the repository scanner,
runs the half-million intervals concurrently, checks their complete summaries,
then performs exact PARI localization and favorable all-useful endpoint no-go
audits for the four interval leaders.  ``--exact-only`` skips the long finite
enumeration and reruns just the theorem-level leader checks.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_ordinary_cm_next_leaders_exact_no_go as endpoint  # noqa: E402


ALPHA = Decimal("0.49368416")
C_LOWER = Fraction(11_978, 10_863)
T_MIN = 205
T_MAX = 250


@dataclass(frozen=True)
class Interval:
    low: int
    high: int
    fundamental_count: int
    broad_positive_count: int
    leader: int
    relaxed_t: int
    relaxed_d: int
    relaxed_useful: int
    relaxed_margin: str


@dataclass(frozen=True)
class Leader:
    discriminant: int
    factorization: tuple[int, ...]
    polynomial: str
    metadata: str
    ordinary_best_t: int
    ordinary_margin_upper: Decimal


INTERVALS = (
    Interval(
        10_000_001,
        10_500_000,
        151_974,
        3_153,
        10_078_365,
        207,
        209,
        10_503,
        "6.4318049749",
    ),
    Interval(
        10_500_001,
        11_000_000,
        151_970,
        3_181,
        10_737_573,
        214,
        217,
        11_340,
        "7.86033508636",
    ),
    Interval(
        11_000_001,
        11_500_000,
        151_984,
        3_246,
        11_352_572,
        214,
        217,
        11_340,
        "7.25993014655",
    ),
    Interval(
        11_500_001,
        12_000_000,
        151_990,
        3_231,
        11_897_340,
        206,
        209,
        10_504,
        "6.56086952831",
    ),
)


LEADERS = (
    Leader(
        10_078_365,
        (3, 5, 11, 17, 3_593),
        "x^2-x-2519591",
        "META,1,24,[6, 2, 2],48,[6, 2, 2, 2],"
        "[2, 2, 2, 2],1,[],207,4,1093",
        209,
        Decimal("-0.94"),
    ),
    Leader(
        10_737_573,
        (3, 7, 11, 23, 43, 47),
        "x^2-x-2684393",
        "META,1,64,[8, 2, 2, 2],128,[8, 2, 2, 2, 2],"
        "[2, 2, 2, 2],1,[],207,4,1049",
        217,
        Decimal("-1.34"),
    ),
    Leader(
        11_352_572,
        (2, 2, 7, 11, 29, 31, 41),
        "x^2-2838143",
        "META,1,32,[4, 2, 2, 2],64,[4, 2, 2, 2, 2],"
        "[2, 2, 2, 2],1,[],207,4,1069",
        217,
        Decimal("-1.98"),
    ),
    Leader(
        11_897_340,
        (2, 2, 3, 5, 7, 13, 2_179),
        "x^2-2974335",
        "META,1,16,[2, 2, 2, 2],32,[2, 2, 2, 2, 2],"
        "[2, 2, 2, 2],1,[],207,4,1163",
        205,
        Decimal("-2.67"),
    ),
)


def packing_constant_audit() -> None:
    sqrt_three_lower = Fraction(265, 153)
    assert sqrt_three_lower * sqrt_three_lower < 3
    fifth = Fraction(1, 5)
    atan_fifth_upper = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(5)
    )
    q = Fraction(1, 239)
    pi_upper = 16 * atan_fifth_upper - 4 * (q - q**3 / 3)
    assert pi_upper < Fraction(355, 113)
    assert 2 * sqrt_three_lower / Fraction(355, 113) == C_LOWER


def trial_factor(number: int) -> tuple[int, ...]:
    output = []
    candidate = 2
    while candidate * candidate <= number:
        while number % candidate == 0:
            output.append(candidate)
            number //= candidate
        candidate = 3 if candidate == 2 else candidate + 2
    if number > 1:
        output.append(number)
    return tuple(output)


def compile_and_run_screen(
    case: Interval, compiler: str, folder: Path, index: int
) -> str:
    source = HERE / "scan_cm_eisenstein_real_quadratic_bases_fast.cpp"
    executable = folder / f"screen_{index}"
    subprocess.check_call(
        [
            compiler,
            "-O3",
            "-std=c++20",
            "-Wall",
            "-Wextra",
            "-Wpedantic",
            f"-DSCREEN_D_MIN={case.low}",
            f"-DSCREEN_D_LIMIT={case.high}",
            "-DSCREEN_NORM_LIMIT=200000",
            "-DSCREEN_ALPHA=0.49368416",
            "-DSCREEN_BROAD_T_MIN=215",
            "-DSCREEN_BROAD_T_MAX=243",
            "-DSCREEN_BROAD_T_STEP=4",
            "-DSCREEN_FINALISTS=100",
            "-DSCREEN_GRANT_GENUS_BONUS=1",
            str(source),
            "-o",
            str(executable),
        ]
    )
    output = subprocess.check_output([str(executable)], text=True)
    assert (
        f"fundamental discriminants scanned: {case.fundamental_count}"
        in output
    )
    assert f"discriminant interval: [{case.low},{case.high}]" in output
    assert "broad T grid: 215..243 step 4" in output
    assert "optimistic genus bonus: 1" in output
    assert (
        "broad-grid all-useful candidates at alpha=0.49368416: "
        f"{case.broad_positive_count}"
    ) in output
    leader = (
        f"1 D={case.leader} margin={case.relaxed_margin} "
        f"t={case.relaxed_t} d={case.relaxed_d} "
        f"useful={case.relaxed_useful}"
    )
    assert leader in output
    return output


def full_screen() -> tuple[str, ...]:
    compiler = shutil.which("c++")
    if compiler is None:
        raise RuntimeError("a C++20 compiler is required")
    with tempfile.TemporaryDirectory(prefix="genus_10m_12m_") as raw:
        folder = Path(raw)
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [
                pool.submit(compile_and_run_screen, case, compiler, folder, i)
                for i, case in enumerate(INTERVALS)
            ]
            outputs = tuple(future.result() for future in futures)
    assert sum(case.fundamental_count for case in INTERVALS) == 607_918
    assert sum(case.broad_positive_count for case in INTERVALS) == 12_811
    return outputs


def exact_localization(leader: Leader) -> str:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    if leader.discriminant % 4 == 1:
        column_builder = r"""Cols=List();for(i=1,#u[1],listput(Cols,flog(u[1][i])));M=matrix(4,#u[1],i,j,Cols[j][i]);"""
    else:
        # In an even-discriminant integral basis, a compact S-unit can contain
        # individually non-dyadic-unit factors whose valuations cancel.  Such
        # a factor cannot be sent separately through ideallog, so reconstruct
        # each complete S-unit exactly before applying the ray logarithm.
        column_builder = r"""G=vector(#u[1],i,nffactorback(nf,u[1][i]));M=Mat(vector(#G,i,ideallog(nf,G[i],bid)));"""
    script = rf"""default(nbthreads,1);D={leader.discriminant};b=bnfinit({leader.polynomial},1);nf=b.nf;nar=bnfnarrow(b);bid=idealstar(nf,[4,[1,1]],1,2);
flog(F)={{my(v=vector(4,i,0));for(j=1,matsize(F)[1],v=v+F[j,2]*concat(Vec(ideallog(nf,F[j,1],bid))));v}};
L=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(L,[Q,p,dec[i]]))));L=vecsort(Vec(L),[1,2]);S=vector({T_MIN},i,L[i][3]);su=bnfsunit(b,S);u=bnfunits(b,S);{column_builder}print("META,",bnfcertify(b),",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",bid.cyc,",",su[5][1],",",su[5][2],",",#u[1],",",matrank(Mod(M,2)),",",L[{T_MIN}][1]);
"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "8G"], input=script, text=True, timeout=240
    )
    lines = output.splitlines()
    assert leader.metadata in lines
    # S-class triviality and ray rank four at T=205 persist on adding ideals.
    # Hence the Kummer rank is (T+2)-4=T-2 on the entire dense window.
    return output


def exact_endpoint_no_go(leader: Leader, primes: list[int]):
    for count in range(T_MIN, T_MAX + 1):
        generator_rank = count - 2
        maximum_relations = (generator_rank * generator_rank - 1) // 4
        useful_count = maximum_relations - (generator_rank + 1) - count
        assert useful_count > 0
        point = Fraction(2, generator_rank)
        assert (
            1
            - generator_rank * point
            + maximum_relations * point * point
        ) < 0
    case = endpoint.FieldCase(
        leader.discriminant,
        leader.ordinary_best_t,
        0,
        0,
        (0, 0, "unused", None),
    )
    ideals = endpoint.prime_ideals(case, primes, 200_000)
    record = endpoint.optimistic_no_go(case, ideals)
    assert record[0] == leader.ordinary_best_t
    assert record[1] < leader.ordinary_margin_upper
    return record


def exact_leader_audits() -> tuple[tuple[int, str, tuple], ...]:
    packing_constant_audit()
    for leader in LEADERS:
        assert trial_factor(leader.discriminant) == leader.factorization
        if leader.discriminant % 4 == 1:
            assert len(set(leader.factorization)) == len(leader.factorization)
        else:
            radicand_factors = list(leader.factorization)
            radicand_factors.remove(2)
            radicand_factors.remove(2)
            assert len(set(radicand_factors)) == len(radicand_factors)

    endpoint.ALPHA = ALPHA
    endpoint.C_UPPER = Decimal(C_LOWER.numerator) / Decimal(
        C_LOWER.denominator
    )
    primes = endpoint.elementary.prime_sieve(220_000)
    output = []
    for leader in LEADERS:
        localization = exact_localization(leader)
        record = exact_endpoint_no_go(leader, primes)
        output.append((leader.discriminant, localization, record))
    return tuple(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--exact-only",
        action="store_true",
        help="skip the 10--12m finite enumeration and rerun leader audits",
    )
    args = parser.parse_args()
    getcontext().prec = 100

    if not args.exact_only:
        outputs = full_screen()
        for case, output in zip(INTERVALS, outputs):
            print(f"===== [{case.low},{case.high}] =====")
            print(output, end="")

    exact = exact_leader_audits()
    for discriminant, localization, record in exact:
        print(f"===== exact D={discriminant} =====")
        print(localization, end="")
        print("favorable all-useful ordinary-rank best:", record)
    print("10--12m genus-bonus screen and leader no-go: CERTIFIED")


if __name__ == "__main__":
    main()
