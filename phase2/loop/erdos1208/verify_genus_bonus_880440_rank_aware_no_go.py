#!/usr/bin/env python3
"""Exact rank-aware no-go for the D=880440 genus-bonus candidate.

PARI/GP certifies the class, narrow-class, S-class, and ray data.  Python
then enumerates every relevant class/ray color subspace and proves endpoint
infeasibility in the full 205 <= |T| <= 250 candidate window.
"""

from __future__ import annotations

import bisect
from decimal import Decimal, getcontext
from fractions import Fraction
import re
import shutil
import subprocess
import sys


sys.path.insert(0, str(__file__.rsplit("/", 1)[0]))
from verify_cm_eisenstein_real_quadratic_43133 import prime_sieve  # noqa: E402


D = 880_440
RADICAND = 220_110
ALPHA = Decimal("0.49369313")
C_LOWER_FRACTION = Fraction(11_978, 10_863)
T_MIN = 205
T_MAX = 250


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


def exact_colored_ideals() -> list[tuple[int, int, int | None, int, int]]:
    """Class colors in F2^4 and ray colors in B/2B = F2^6."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,200);b=bnfinit(x^2-{RADICAND},1);cert=bnfcertify(b);nf=b.nf;nar=bnfnarrow(b);br=bnrinit(b,[4,[1,1]],1);u=bnfunits(b);bid=idealstar(nf,[4,[1,1]],1,2);um=Mat(vector(#u[1],i,ideallog(nf,u[1][i],bid)));ideals=List();forprime(p=3,50000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=50000,listput(ideals,[Q,p,dec[i]]))));ideals=vecsort(Vec(ideals),[1,2]);S=vector({T_MIN},i,ideals[i][3]);su=bnfsunit(b,S);uu=bnfunits(b,S);sm=Mat(vector(#uu[1],i,ideallog(nf,uu[1][i],bid)));print("META,",cert,",",b.no,",",b.clgp[2],",",nar[1],",",nar[2],",",br.cyc,",",matrank(Mod(um,2)),",",su[5][1],",",#uu[1],",",matrank(Mod(sm,2)),",",matsize(matker(Mod(sm,2)))[2]);for(j=1,#ideals,my(pr=ideals[j][3],e=bnfisprincipal(b,pr,0),v=bnrisprincipal(br,pr,0),r=-1);if(ideals[j][1]==ideals[j][2],r=lift(nfmodpr(nf,Mod(x,nf.pol),pr)));print("IDEAL,",ideals[j][1],",",ideals[j][2],",",r,",",concat(Vec(e)),",",concat(Vec(v))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True
    )
    lines = output.splitlines()
    expected = (
        "META,1,16,[2, 2, 2, 2],32,[2, 2, 2, 2, 2],"
        "[4, 2, 2, 2, 2, 2],2,1,207,4,203"
    )
    assert expected in lines
    pattern = re.compile(
        r"IDEAL,(\d+),(\d+),(-?\d+),"
        r"\[([01]), ([01]), ([01]), ([01])\],"
        r"\[([0-3]), ([01]), ([01]), ([01]), ([01]), ([01])\]"
    )
    rows: list[tuple[int, int, int | None, int, int]] = []
    for line in lines:
        match = pattern.fullmatch(line)
        if not match:
            continue
        norm_q, prime, root = map(int, match.group(1, 2, 3))
        class_color = sum(
            int(match.group(4 + index)) << index for index in range(4)
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
    assert gf2_rank([row[3] for row in rows[:T_MIN]]) == 4
    assert gf2_rank([row[4] for row in rows[:T_MIN]]) == 6
    return rows


def all_subspaces(dimension: int) -> list[frozenset[int]]:
    elements = 1 << dimension
    output: set[frozenset[int]] = set()
    for mask in range(1 << elements):
        if not mask & 1:
            continue
        subset = frozenset(
            value for value in range(elements) if mask >> value & 1
        )
        if all(left ^ right in subset for left in subset for right in subset):
            output.add(subset)
    return sorted(output, key=lambda subset: (len(subset), tuple(subset)))


def ray_subspaces() -> dict[int, set[frozenset[int]]]:
    output: dict[int, set[frozenset[int]]] = {4: set(), 5: set()}
    for functional in range(1, 64):
        output[5].add(
            frozenset(
                value
                for value in range(64)
                if (functional & value).bit_count() % 2 == 0
            )
        )
    for first in range(1, 64):
        for second in range(first + 1, 64):
            subset = frozenset(
                value
                for value in range(64)
                if (first & value).bit_count() % 2 == 0
                and (second & value).bit_count() % 2 == 0
            )
            if len(subset) == 16:
                output[4].add(subset)
    assert len(output[5]) == 63 and len(output[4]) == 651
    return output


def prime_ideal_norms(limit: int = 200_000) -> list[int]:
    output: list[int] = []
    for prime in prime_sieve(limit):
        if prime == 2:
            continue
        if D % prime == 0:
            output.append(prime)
            continue
        symbol = pow(D % prime, (prime - 1) // 2, prime)
        if symbol == 1:
            output.extend((prime, prime))
        else:
            assert symbol == prime - 1
            if prime * prime <= limit:
                output.append(prime * prime)
    output.sort()
    return output


def minimum_products(
    rows: list[tuple[int, int, int | None, int, int]],
) -> dict[tuple[str, int, int], tuple[int, int, tuple, frozenset[int]]]:
    """Exact minimum T-products inside every relevant color family."""
    minima: dict[tuple[str, int, int], tuple[int, int, tuple, frozenset[int]]] = {}
    class_subspaces = all_subspaces(4)
    assert len(class_subspaces) == 67
    for class_dimension in range(4):
        for subspace in class_subspaces:
            if len(subspace) != 1 << class_dimension:
                continue
            allowed = [row for row in rows if row[3] in subspace][:T_MAX]
            if len(allowed) < T_MAX:
                continue
            product = 1
            products: list[int] = []
            for row in allowed:
                product *= row[0]
                products.append(product)
            for count in range(T_MIN, T_MAX + 1):
                if gf2_rank([row[3] for row in allowed[:count]]) != class_dimension:
                    continue
                key = ("class", class_dimension, count)
                value = (
                    products[count - 1],
                    rows.index(allowed[count - 1]) + 1,
                    allowed[count - 1],
                    subspace,
                )
                if key not in minima or value[0] < minima[key][0]:
                    minima[key] = value

    for ray_dimension, subspaces in ray_subspaces().items():
        for subspace in subspaces:
            allowed = [row for row in rows if row[4] in subspace][:T_MAX]
            if len(allowed) < T_MAX:
                continue
            product = 1
            products = []
            for row in allowed:
                product *= row[0]
                products.append(product)
            for count in range(T_MIN, T_MAX + 1):
                prefix = allowed[:count]
                if gf2_rank([row[3] for row in prefix]) != 4:
                    continue
                if gf2_rank([row[4] for row in prefix]) != ray_dimension:
                    continue
                key = ("ray", ray_dimension, count)
                value = (
                    products[count - 1],
                    rows.index(allowed[count - 1]) + 1,
                    allowed[count - 1],
                    subspace,
                )
                if key not in minima or value[0] < minima[key][0]:
                    minima[key] = value
    return minima


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


_LOCAL_ITEM_CACHE: dict[
    int, tuple[list[tuple[Decimal, Decimal, Decimal, int, int]], Decimal]
] = {}


def local_items(norm_q: int):
    if norm_q in _LOCAL_ITEM_CACHE:
        return _LOCAL_ITEM_CACHE[norm_q]
    cost = Decimal(norm_q).ln() / 2
    items: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    depth = 1
    previous: Decimal | None = None
    while True:
        gain = local_gain(norm_q, depth)
        if previous is not None:
            assert previous > gain
        previous = gain
        slope = gain / cost
        if slope < Decimal("0.01"):
            result = items, slope
            _LOCAL_ITEM_CACHE[norm_q] = result
            return result
        items.append((slope, cost, gain, norm_q, depth))
        depth += 1
        assert depth < 100


def build_frontier(norms: list[int]):
    increments: list[tuple[Decimal, Decimal, Decimal, int, int]] = []
    maximum_omitted = Decimal(0)
    for norm_q in norms:
        items, omitted = local_items(norm_q)
        increments.extend(items)
        maximum_omitted = max(maximum_omitted, omitted)
    increments.sort(reverse=True)
    costs = [Decimal(0)]
    gains = [Decimal(0)]
    for _, cost, gain, _, _ in increments:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
    return increments, costs, gains, maximum_omitted


def all_depth_value(norm_q: int, slope: Decimal) -> Decimal:
    cost = Decimal(norm_q).ln() / 2
    value = Decimal(0)
    for depth in range(1, 100):
        excess = local_gain(norm_q, depth) - slope * cost
        if excess <= 0:
            return value
        value += excess
    raise AssertionError("local depth did not terminate")


def endpoint_exclusion(
    ramified_product: int,
    count: int,
    generator_rank: int,
    useful_norms: list[int],
    check_prefix_exchange: bool,
):
    constant = Decimal(C_LOWER_FRACTION.numerator) / Decimal(
        C_LOWER_FRACTION.denominator
    )
    log_rd = Decimal(D).ln() / 2 + Decimal(ramified_product).ln() / 4
    increments, costs, gains, maximum_omitted = build_frontier(useful_norms)

    def envelope(target: Decimal):
        index = bisect.bisect_left(costs, target)
        assert 0 < index < len(costs)
        fraction = (target - costs[index - 1]) / (
            costs[index] - costs[index - 1]
        )
        item = increments[index - 1]
        return gains[index - 1] + fraction * item[2], item[0]

    def records(anchor: Decimal):
        output = []
        for endpoint in (1, 2):
            scale = Decimal(endpoint)
            w = scale * anchor
            value, slope = envelope(2 * ALPHA * w)
            exponent = 2 * (2 * ALPHA - 1) * w - log_rd
            ratio = exponent.exp() / constant
            rhs = (
                constant.ln()
                + log_rd
                + (2 - 4 * ALPHA) * w
                + (1 + ratio).ln()
            )
            margin = value - rhs
            derivative = (
                2 * ALPHA * scale * slope
                - (2 - 4 * ALPHA) * scale
                - 2 * (2 * ALPHA - 1) * scale * ratio / (1 + ratio)
            )
            rho = Decimal(1) / (1 + ratio)
            output.append((margin, derivative, slope, rho))
        return output

    low, high = Decimal("25000"), Decimal("70000")
    low_difference = records(low)[0][0] - records(low)[1][0]
    high_difference = records(high)[0][0] - records(high)[1][0]
    assert low_difference * high_difference < 0
    for _ in range(80):
        middle = (low + high) / 2
        difference = records(middle)[0][0] - records(middle)[1][0]
        if low_difference * difference <= 0:
            high = middle
        else:
            low, low_difference = middle, difference
    anchor = (low + high) / 2
    data = records(anchor)
    assert maximum_omitted < min(row[2] for row in data)
    assert data[0][0] < Decimal("-0.05")
    assert data[1][0] < Decimal("-0.05")
    assert data[0][1] > Decimal("0.001")
    assert data[1][1] < Decimal("-0.001")

    if check_prefix_exchange:
        # The universal derivative argument handles Q>=9.  The only smaller
        # available norms are 3,5,7, and the exact endpoint values below
        # check the remaining discrete monotonicity at both tangent slopes.
        for _, _, slope, rho in data:
            assert rho > Decimal(1) / Decimal(3).ln()
            values = [all_depth_value(q, slope) for q in (3, 5, 7, 9)]
            assert all(values[index] > values[index + 1] for index in range(3))
            role_costs = [
                rho * Decimal(q).ln() / 4 + value
                for q, value in zip((3, 5, 7, 9), values)
            ]
            assert all(
                role_costs[index] < role_costs[index + 1]
                for index in range(3)
            )
    maximum_relations = (generator_rank * generator_rank - 1) // 4
    useful_count = maximum_relations - (generator_rank + 1) - count
    assert useful_count == len(useful_norms)
    return anchor, data, log_rd


def main() -> None:
    getcontext().prec = 90
    assert D == 8 * 3 * 5 * 11 * 23 * 29
    assert RADICAND * 4 == D
    sqrt_three_lower = Fraction(265, 153)
    assert sqrt_three_lower * sqrt_three_lower < 3
    fifth = Fraction(1, 5)
    atan_fifth_upper = sum(
        (-1) ** index * fifth ** (2 * index + 1) / (2 * index + 1)
        for index in range(5)
    )
    two_hundred_thirty_ninth = Fraction(1, 239)
    atan_239_lower = (
        two_hundred_thirty_ninth
        - two_hundred_thirty_ninth**3 / 3
    )
    pi_upper = 16 * atan_fifth_upper - 4 * atan_239_lower
    assert pi_upper < Fraction(355, 113)
    assert (
        2 * sqrt_three_lower / Fraction(355, 113)
        == C_LOWER_FRACTION
    )
    useful_monotonicity_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_monotonicity_upper = Fraction(729, 6_400)
    assert useful_monotonicity_lower > useful_monotonicity_upper

    rows = exact_colored_ideals()
    norms = prime_ideal_norms()
    assert [row[0] for row in rows[:1_000]] == norms[:1_000]
    minima = minimum_products(rows)

    category_outputs: dict[tuple[str, int], tuple] = {}
    # Proper ordinary-class spans.  The exact pre-local dimension is
    # t+6-c.  We charge only one local condition (rather than the certified
    # unit rank two), hence d=t+5-c is deliberately favorable.
    for kind, parameter in [
        ("class", 0), ("class", 1), ("class", 2), ("class", 3),
        ("ray", 4), ("ray", 5),
    ]:
        outputs = []
        for count in range(T_MIN, T_MAX + 1):
            product, overall_index, last, subspace = minima[
                (kind, parameter, count)
            ]
            if kind == "class":
                generator_rank = count + 5 - parameter
            else:
                # Full ordinary class span and ray span h gives exact
                # quotient local rank h-4, so d=t-(h-4).
                generator_rank = count - (parameter - 4)
            useful_count = (
                (generator_rank * generator_rank - 1) // 4
                - (generator_rank + 1)
                - count
            )
            # This is stronger than any actual assignment: useful roles may
            # reuse the globally smallest ideals, including the T ideals.
            useful = norms[:useful_count]
            anchor, data, log_rd = endpoint_exclusion(
                product, count, generator_rank, useful, False
            )
            outputs.append(
                (max(data[0][0], data[1][0]), count, generator_rank,
                 overall_index, last, log_rd, anchor, subspace)
            )
        category_outputs[(kind, parameter)] = max(outputs)

    # Full six-dimensional ray span: d=t-2.  The exact all-depth role
    # exchange proves that the norm prefix T and first remaining useful
    # ideals are optimal, including the exceptional norms 3,5,7.
    prefix_outputs = []
    prefix_product = 1
    for count, norm_q in enumerate(norms[:T_MAX], 1):
        prefix_product *= norm_q
        if count < T_MIN:
            continue
        generator_rank = count - 2
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - count
        )
        useful = norms[count : count + useful_count]
        anchor, data, log_rd = endpoint_exclusion(
            prefix_product, count, generator_rank, useful, True
        )
        prefix_outputs.append(
            (max(data[0][0], data[1][0]), count, generator_rank,
             norms[count - 1], log_rd, anchor)
        )
    prefix_worst = max(prefix_outputs)
    assert prefix_worst[0] < Decimal("-0.5")

    print("D / class / narrow / ray arithmetic: CERTIFIED", D)
    print("proper/ray-subspace optimistic worst cases:")
    for key, value in category_outputs.items():
        print(" ", key, value)
    print("full-ray prefix worst case:", prefix_worst)
    print("D=880440 genus bonus in 205<=T<=250: RIGOROUSLY KILLED")


if __name__ == "__main__":
    main()
