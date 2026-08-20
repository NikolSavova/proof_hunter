#!/usr/bin/env python3
"""Rank-aware genus audit for D=963480 and D=937365.

PARI/GP certifies the class, narrow-class, prefix S-class, and ray data.
The finite color-subspace and endpoint exclusion machinery is imported from
the independently verified D=880440 audit.  Proper ray spans receive a
deliberately optimistic generator-rank bound needing no delicate exact-rank
formula.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
import verify_genus_bonus_880440_rank_aware_no_go as core  # noqa: E402


@dataclass(frozen=True)
class FieldCase:
    discriminant: int
    polynomial: str
    class_number: int
    class_cycles: str
    narrow_number: int
    narrow_cycles: str
    ray_cycles: str
    unit_local_rank: int


CASES = (
    FieldCase(
        963_480,
        "x^2-240870",
        32,
        "[4, 2, 2, 2]",
        64,
        "[4, 2, 2, 2, 2]",
        "[8, 2, 2, 2, 2, 2]",
        2,
    ),
    FieldCase(
        937_365,
        "x^2-x-234341",
        16,
        "[2, 2, 2, 2]",
        32,
        "[2, 2, 2, 2, 2]",
        "[12, 2, 2, 2, 2, 2]",
        1,
    ),
)


def exact_colored_ideals(
    case: FieldCase,
) -> list[tuple[int, int, int | None, int, int]]:
    """Return exact class/ray Frattini colors for small odd prime ideals."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,300);b=bnfinit({case.polynomial},1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);br=bnrinit(b,[4,[1,1]],1);u=bnfunits(b);bid=idealstar(nf,[4,[1,1]],1,2);um=Mat(vector(#u[1],i,ideallog(nf,u[1][i],bid)));ideals=List();forprime(p=3,50000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=50000,listput(ideals,[Q,p,dec[i]]))));ideals=vecsort(Vec(ideals),[1,2]);S=vector({core.T_MIN},i,ideals[i][3]);su=bnfsunit(b,S);uu=bnfunits(b,S);sm=Mat(vector(#uu[1],i,ideallog(nf,uu[1][i],bid)));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",br.cyc,",",matrank(Mod(um,2)),",",su[5][1],",",#uu[1],",",matrank(Mod(sm,2)),",",matsize(matker(Mod(sm,2)))[2]);for(j=1,#ideals,my(pr=ideals[j][3],e=bnfisprincipal(b,pr,0),v=bnrisprincipal(br,pr,0),r=-1);if(ideals[j][1]==ideals[j][2],r=lift(nfmodpr(nf,Mod(x,nf.pol),pr)));print("IDEAL,",ideals[j][1],",",ideals[j][2],",",r,",",concat(Vec(e)),",",concat(Vec(v))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=180
    )
    lines = output.splitlines()
    expected = (
        f"META,1,{case.class_number},{case.class_cycles},"
        f"{case.narrow_number},{case.narrow_cycles},{case.ray_cycles},"
        f"{case.unit_local_rank},1,207,4,203"
    )
    assert expected in lines

    pattern = re.compile(
        r"IDEAL,(\d+),(\d+),(-?\d+),"
        r"\[([0-3]), ([01]), ([01]), ([01])\],"
        r"\[([0-9]+), ([01]), ([01]), ([01]), ([01]), ([01])\]"
    )
    rows: list[tuple[int, int, int | None, int, int]] = []
    for line in lines:
        match = pattern.fullmatch(line)
        if not match:
            continue
        norm_q, prime, root = map(int, match.group(1, 2, 3))
        class_color = sum(
            (int(match.group(4 + index)) & 1) << index
            for index in range(4)
        )
        ray_color = sum(
            (int(match.group(8 + index)) & 1) << index
            for index in range(6)
        )
        rows.append(
            (norm_q, prime, None if root < 0 else root, class_color, ray_color)
        )
    rows.sort()
    assert len(rows) > 5_000
    assert core.gf2_rank([row[3] for row in rows[: core.T_MIN]]) == 4
    assert core.gf2_rank([row[4] for row in rows[: core.T_MIN]]) == 6
    return rows


def endpoint_categories(
    case: FieldCase,
    rows: list[tuple[int, int, int | None, int, int]],
    norms: list[int],
):
    minima = core.minimum_products(rows)
    category_outputs: dict[tuple[str, int], tuple] = {}

    # If the selected ordinary classes have Frattini span c<4, the exact
    # pre-local S-unit dimension is T+6-c.  We charge only one local
    # condition, even when the global units already have rank two.
    for kind, parameter in [
        ("class", 0),
        ("class", 1),
        ("class", 2),
        ("class", 3),
        ("ray", 4),
        ("ray", 5),
    ]:
        outputs = []
        for count in range(core.T_MIN, core.T_MAX + 1):
            product, overall_index, last, subspace = minima[
                (kind, parameter, count)
            ]
            if kind == "class":
                generator_rank = count + 5 - parameter
            else:
                # Full ordinary span gives pre-local dimension T+2.  On a
                # proper ray span we subtract only the independently
                # certified global-unit image and ignore every further local
                # obstruction.  This is favorable to the competitor.
                generator_rank = count + 2 - case.unit_local_rank
            useful_count = (
                (generator_rank * generator_rank - 1) // 4
                - (generator_rank + 1)
                - count
            )
            # Reuse the globally smallest ideals in the useful role,
            # including T itself: another favorable relaxation.
            useful = norms[:useful_count]
            anchor, data, log_rd = core.endpoint_exclusion(
                product, count, generator_rank, useful, False
            )
            outputs.append(
                (
                    max(data[0][0], data[1][0]),
                    count,
                    generator_rank,
                    overall_index,
                    last,
                    log_rd,
                    anchor,
                    subspace,
                )
            )
        category_outputs[(kind, parameter)] = max(outputs)

    # Full Frattini span generates the entire finite ray group.  Its kernel
    # over the ordinary class group therefore realizes the entire quotient
    # of the four local conditions by the global-unit image.  Hence the
    # exact safe rank is T-2.  The all-depth exchange theorem then makes the
    # norm prefix optimal.
    prefix_outputs = []
    prefix_product = 1
    for count, norm_q in enumerate(norms[: core.T_MAX], 1):
        prefix_product *= norm_q
        if count < core.T_MIN:
            continue
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        useful = norms[count : count + useful_count]
        anchor, data, log_rd = core.endpoint_exclusion(
            prefix_product, count, generator_rank, useful, True
        )
        prefix_outputs.append(
            (
                max(data[0][0], data[1][0]),
                count,
                generator_rank,
                norms[count - 1],
                log_rd,
                anchor,
            )
        )
    return category_outputs, max(prefix_outputs)


def main() -> None:
    getcontext().prec = 90
    outputs = {}
    primes = core.prime_sieve(200_000)
    for case in CASES:
        if case.discriminant % 4 == 0:
            radicand = case.discriminant // 4
            assert radicand % 4 in (2, 3)
        else:
            radicand = case.discriminant
            assert case.discriminant % 4 == 1
        assert all(
            radicand % (prime * prime)
            for prime in primes
            if prime * prime <= radicand
        )

        core.D = case.discriminant
        rows = exact_colored_ideals(case)
        norms = core.prime_ideal_norms()
        assert [row[0] for row in rows[:1_000]] == norms[:1_000]
        categories, prefix = endpoint_categories(case, rows, norms)
        outputs[case.discriminant] = (categories, prefix)

    for discriminant, (categories, prefix) in outputs.items():
        print("D=", discriminant)
        print(" proper/ray optimistic worst cases:")
        for key, value in categories.items():
            print("  ", key, value)
        print(" full-ray prefix worst case:", prefix)
    print("D=963480 and D=937365 rank-aware genus audit: CERTIFIED")


if __name__ == "__main__":
    main()
