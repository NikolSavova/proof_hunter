#!/usr/bin/env python3
"""Verifier for the small degree Eisenstein-CM base screen and finalist kill."""

from __future__ import annotations

import argparse
import ast
import bisect
import itertools
import json
import math
import shutil
import subprocess
import urllib.request
from dataclasses import dataclass


LEGACY_ALPHA = 0.49371148
LIVE_ALPHA = 0.49369772
CM_CONSTANT = 2 * math.sqrt(3) / math.pi
GP_LIMIT = 220_000


@dataclass(frozen=True)
class Field:
    degree: int
    discriminant: int
    coefficients: tuple[int, ...]  # ascending
    narrow_group: tuple[int, ...] = ()


FINALISTS = (
    Field(3, 4_729, (-29, -19, 0, 1), (2,)),
    Field(3, 5_521, (-11, -13, 0, 1), (2,)),
)


def polynomial(field: Field) -> str:
    return "+".join(
        f"({coefficient})*x^{power}"
        for power, coefficient in enumerate(field.coefficients)
        if coefficient
    )


def run_gp(source: str) -> list[str]:
    result = subprocess.run(
        ["gp", "-q"], input=source + "\n", text=True,
        capture_output=True, check=True,
    )
    lines = result.stdout.strip().splitlines()
    if not lines:
        raise AssertionError(result.stderr)
    return lines


def parse_gp(line: str):
    return ast.literal_eval(line.replace("~", ""))


def prime_stream(field: Field) -> list[tuple[int, int]]:
    source = "allocatemem(120000000)\n" + (
        f"nf=nfinit({polynomial(field)});v=List();"
        f"forprime(p=3,{GP_LIMIT},d=idealprimedec(nf,p);"
        "for(i=1,#d,listput(v,[p,p^d[i][4]])));"
        "v=vecsort(Vec(v),(a,b)->if(a[2]==b[2],a[1]-b[1],a[2]-b[2]));"
        "print(v)"
    )
    return [tuple(row) for row in parse_gp(run_gp(source)[-1])]


def local_increment(norm: int, depth: int) -> float:
    z = norm ** -2
    return 0.5 * (
        math.log((depth + 1) / depth)
        + math.log1p(-(z ** depth))
        - math.log1p(-(z ** (depth + 1)))
    )


def best_margin(
    field: Field,
    stream: list[tuple[int, int]],
    t_values,
    rank_shift: int,
    relation_excess: int,
    alpha: float,
) -> tuple[float, tuple]:
    best = (-1.0e100, ())
    s = field.degree
    for t in t_values:
        d = t + rank_shift
        useful_count = (d * d - 1) // 4 - (d + relation_excess) - t
        useful = [row for row in stream[t:] if row[0] != 3][:useful_count]
        assert len(useful) == useful_count

        items: list[tuple[float, float, float, int]] = []
        maximum_seventh_slope = 0.0
        for _, norm in useful:
            cost = math.log(norm) / s
            for depth in range(1, 8):
                gain = local_increment(norm, depth) / s
                slope = gain / cost
                if depth <= 6:
                    items.append((slope, cost, gain, depth))
                else:
                    maximum_seventh_slope = max(maximum_seventh_slope, slope)
        items.sort(reverse=True)
        cumulative_cost = [0.0]
        cumulative_gain = [0.0]
        for _, cost, gain, _ in items:
            cumulative_cost.append(cumulative_cost[-1] + cost)
            cumulative_gain.append(cumulative_gain[-1] + gain)

        def envelope(target: float) -> tuple[float, float]:
            index = bisect.bisect_right(cumulative_cost, target) - 1
            assert 0 <= index < len(items)
            value = cumulative_gain[index] + (
                target - cumulative_cost[index]
            ) * items[index][0]
            return value, items[index][0]

        log_d = math.log(field.discriminant) / s + sum(
            math.log(norm) for _, norm in stream[:t]
        ) / (2 * s)

        def rhs(w: float) -> float:
            exponent = 2 * (2 * alpha - 1) * w - log_d
            return (
                math.log(CM_CONSTANT) + log_d + (2 - 4 * alpha) * w
                + math.log1p(math.exp(exponent) / CM_CONSTANT)
            )

        def score(w: float) -> float:
            return min(
                envelope(2 * alpha * w)[0] - rhs(w),
                envelope(4 * alpha * w)[0] - rhs(2 * w),
            )

        # Search the entire interval supported by the retained depths.  The
        # score is concave.  Once these depths are exhausted, all omitted
        # slopes are at most the first omitted slope checked below, so the
        # concave tail cannot create a later maximum.
        low = 1.0e-9
        high = cumulative_cost[-1] / (4 * alpha) * (1 - 1.0e-12)
        # Both margins are concave in w, hence so is their pointwise minimum.
        for _ in range(90):
            left = (2 * low + high) / 3
            right = (low + 2 * high) / 3
            if score(left) < score(right):
                low = left
            else:
                high = right
        w = (low + high) / 2
        margin = score(w)
        right_slope = envelope(4 * alpha * w)[1]
        assert maximum_seventh_slope < right_slope
        record = (t, d, useful_count, w, log_d, right_slope)
        if margin > best[0]:
            best = margin, record
    return best


def multiplication_and_kummer(field: Field, maximum_t: int = 280):
    source = "allocatemem(120000000)\n" + f"""
nf=nfinit({polynomial(field)});b=bnfinit({polynomial(field)},1);
print(abs(nf.disc));print(b.no);print(bnfnarrow(b)[2]);
print(#idealprimedec(nf,2));print(idealprimedec(nf,2)[1][4]);
print(vector(3,i,vector(3,j,Vec(nfalgtobasis(nf,nf.zk[i]*nf.zk[j])))));
u=concat([[-1,0,0]~],vector(#b.fu,i,nfalgtobasis(nf,lift(b.fu[i]))));print(u);
print(vector(#u,i,vector(3,j,sign(nfeltembed(nf,u[i])[j]))));
v=List();forprime(p=3,5000,d=idealprimedec(nf,p);for(i=1,#d,g=bnfisprincipal(b,d[i])[2];listput(v,[p,p^d[i][4],Vec(g),vector(3,j,sign(nfeltembed(nf,g)[j]))])));
v=vecsort(Vec(v),(a,c)->if(a[2]==c[2],a[1]-c[1],a[2]-c[2]));
print(vector({maximum_t},i,v[i]))
"""
    lines = run_gp(source)
    assert int(lines[0]) == field.discriminant
    assert int(lines[1]) == 1
    assert parse_gp(lines[2]) == [2]
    assert int(lines[3]) == 1 and int(lines[4]) == 3
    table = parse_gp(lines[5])
    units = parse_gp(lines[6])
    unit_signs = parse_gp(lines[7])
    generators = parse_gp(lines[8])

    def multiply(left, right, modulus=4):
        answer = [0, 0, 0]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    answer[k] = (
                        answer[k] + left[i] * right[j] * table[i][j][k]
                    ) % modulus
        return tuple(answer)

    # Inertness makes precisely the nonzero reductions modulo 2 units.
    residues = list(itertools.product(range(4), repeat=3))
    units_mod_four = [r for r in residues if any(value % 2 for value in r)]
    squares = {multiply(value, value) for value in units_mod_four}
    assert len(units_mod_four) == 56 and len(squares) == 7

    unseen = set(units_mod_four)
    cosets = []
    while unseen:
        representative = next(iter(unseen))
        coset = {multiply(representative, square) for square in squares}
        cosets.append(coset)
        unseen -= coset
    assert len(cosets) == 8
    coset_index = {value: i for i, coset in enumerate(cosets) for value in coset}
    representatives = [next(iter(coset)) for coset in cosets]
    identity = coset_index[(1, 0, 0)]
    span = {identity: 0}
    basis = []
    for index in range(8):
        if index in span:
            continue
        bit = 1 << len(basis)
        basis.append(index)
        for old_index, mask in list(span.items()):
            product_index = coset_index[
                multiply(representatives[old_index], representatives[index])
            ]
            span[product_index] = mask | bit
    assert len(basis) == 3 and len(span) == 8

    def dyadic_bits(vector) -> int:
        residue = tuple(value % 4 for value in vector)
        return span[coset_index[residue]]

    def column(vector, signs) -> int:
        sign_bits = sum((signs[index] < 0) << index for index in range(3))
        return sign_bits | (dyadic_bits(vector) << 3)

    columns = [column(vector, signs) for vector, signs in zip(units, unit_signs)]
    columns.extend(column(row[2], row[3]) for row in generators)

    def gf2_rank(rows) -> int:
        pivots = {}
        for row in rows:
            while row:
                pivot = row.bit_length() - 1
                if pivot in pivots:
                    row ^= pivots[pivot]
                else:
                    pivots[pivot] = row
                    break
        return len(pivots)

    for t in range(180, maximum_t + 1):
        prefix = columns[: 3 + t]
        rows = [
            sum(((value >> bit) & 1) << index for index, value in enumerate(prefix))
            for bit in range(6)
        ]
        assert gf2_rank(rows) == 6
        assert len(prefix) - gf2_rank(rows) == t - 3
    return len(units_mod_four), len(squares)


def fetch_screen_fields(degree: int) -> list[Field]:
    records = []
    for offset in (0, 100):
        url = (
            "https://www.lmfdb.org/api/nf_fields/"
            f"?degree=i{degree}&r2=i0&_sort=disc_abs&_limit=100"
            f"&_offset={offset}&_format=json"
        )
        with urllib.request.urlopen(url, timeout=30) as response:
            records.extend(json.load(response)["data"])
    assert len(records) == 200
    return [
        Field(
            degree,
            int(record["disc_abs"]),
            tuple(int(value) for value in record["coeffs"]),
            tuple(int(value) for value in record["narrow_class_group"]),
        )
        for record in records
    ]


def full_screen() -> None:
    rows = []
    for degree in (3, 4):
        fields = fetch_screen_fields(degree)
        assert fields[-1].discriminant == (5_624 if degree == 3 else 29_237)
        for index, field in enumerate(fields, 1):
            h2 = sum(value % 2 == 0 for value in field.narrow_group)
            margin, data = best_margin(
                field, prime_stream(field), range(190, 251, 5), h2, 0,
                LEGACY_ALPHA,
            )
            rows.append((margin, field, data))
            if index % 25 == 0:
                print("screen progress:", degree, index)
    positive = {(row[1].degree, row[1].discriminant) for row in rows if row[0] > 0}
    assert positive == {(3, 4_729), (3, 5_521)}
    quartic_best = max(row[0] for row in rows if row[1].degree == 4)
    assert quartic_best < -1.1
    print("full 400-field optimistic screen: REPRODUCED")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-screen", action="store_true")
    args = parser.parse_args()
    assert shutil.which("gp"), "PARI/GP is required"

    for field in FINALISTS:
        assert multiplication_and_kummer(field) == (56, 7)
        stream = prime_stream(field)
        optimistic = best_margin(
            field, stream, range(190, 251, 5), 1, 0, LEGACY_ALPHA
        )
        actual_legacy = best_margin(
            field, stream, range(180, 281), -3, 2, LEGACY_ALPHA
        )
        actual_live = best_margin(
            field, stream, range(180, 281), -3, 2, LIVE_ALPHA
        )
        assert optimistic[0] > 0.7
        assert actual_legacy[0] < -4.0
        assert actual_live[0] < actual_legacy[0] - 1.0
        print(
            "field / old optimistic / old exact-safe / live exact-safe:",
            field.discriminant, optimistic, actual_legacy, actual_live,
        )

    if args.full_screen:
        full_screen()
    print("small degree CM-base candidates: EXACTLY KILLED")


if __name__ == "__main__":
    main()
