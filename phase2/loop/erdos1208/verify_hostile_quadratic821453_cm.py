#!/usr/bin/env python3
"""Hostile exact audit of the Q(sqrt(821453)) CM construction.

The arithmetic kernel is rebuilt with a certified PARI/GP BNF.  The rest of
the calculation uses integer or high-precision Decimal arithmetic.  The last
section also audits the dependence of the Kummer rank on a non-prefix choice
of ramified prime ideals.
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
import verify_cm_eisenstein_real_quadratic_43133 as elementary  # noqa: E402


D = 821_453
C = (D - 1) // 4
T_COUNT = 219
GENERATOR_RANK = 217
USEFUL_COUNT = 11_335
ALPHA = Decimal("0.49369313")
W0 = Decimal("40752.9517")
SAFE_C = Fraction(71_603, 64_935)
EPSILON = Decimal("1e-25")

# Conjugate of the exact fundamental unit printed by the certified BNF.
FUNDAMENTAL_UNIT = (
    186316454240240950831996254189678995764007199093900246424632249492099634587644508360923159008655904997844,
    -410686981983501954093912456556896671752434792917187266777243157371242664969263912021729490616671611015,
)


def configure_elementary_module() -> None:
    """Point the already-audited elementary routines at this field."""
    elementary.FIELD_DISCRIMINANT = D
    elementary.OMEGA_CONSTANT = C
    elementary.RAMIFIED_IDEAL_COUNT = T_COUNT


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


def parity_dot(left: int, right: int) -> int:
    return (left & right).bit_count() & 1


def exact_ray_rows() -> tuple[list[int], list[tuple[int, int, int | None, int]]]:
    """Return exact full sign/mod-4 ray columns for small prime ideals."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,500);D={D};c=(D-1)/4;b=bnfinit(x^2-x-c,1);cert=bnfcertify(b);nf=b.nf;bid=idealstar(nf,[4,[1,1]],1,2);nar=bnfnarrow(b);print("META,",cert,",",b.no,",",nar[1],",",bid.cyc);units=bnfunits(b);for(i=1,#units[1],print("UNIT,",concat(Vec(ideallog(nf,units[1][i],bid)))));forprime(p=3,12000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=12000,my(z=bnfisprincipal(b,dec[i])[2],v=ideallog(nf,z,bid),r=-1);if(Q==p,r=lift(nfmodpr(nf,Mod(x,nf.pol),dec[i])));print("IDEAL,",Q,",",p,",",r,",",concat(Vec(v))))));"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True
    )
    lines = output.splitlines()
    assert "META,1,1,2,[2, 2, 2, 2]" in lines
    vector_pattern = r"\[([01]), ([01]), ([01]), ([01])\]"
    units: list[int] = []
    rows: list[tuple[int, int, int | None, int]] = []
    for line in lines:
        match = re.fullmatch("UNIT," + vector_pattern, line)
        if match:
            units.append(
                sum(int(match.group(index + 1)) << index for index in range(4))
            )
            continue
        match = re.fullmatch(
            r"IDEAL,(\d+),(\d+),(-?\d+)," + vector_pattern, line
        )
        if match:
            norm_q, prime, root = map(int, match.group(1, 2, 3))
            column = sum(
                int(match.group(index + 4)) << index for index in range(4)
            )
            rows.append(
                (norm_q, prime, None if root < 0 else root, column)
            )
    rows.sort()
    assert len(units) == 2 and gf2_rank(units) == 2
    assert len(rows) > 1_000
    return units, rows


def exact_kummer_kernel() -> tuple[list[tuple[int, int]], tuple[int, ...]]:
    """Certified single-thread GP reconstruction of the full kernel."""
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required")
    script = rf"""default(nbthreads,1);default(realprecision,500);D={D};c=(D-1)/4;bnf=bnfinit(x^2-x-c,1);cert=bnfcertify(bnf);nf=bnf.nf;
ideals=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(ideals,[Q,p,dec[i]]))));
ideals=vecsort(Vec(ideals),[1,2]);S=ideals[1..{T_COUNT}];units=bnfunits(bnf,vector(#S,i,S[i][3]));bid=idealstar(nf,[4,[1,1]],1,2);mm=Mat(vector(#units[1],i,ideallog(nf,units[1][i],bid)));kk=matker(Mod(mm,2));lastroot=lift(nfmodpr(nf,Mod(x,nf.pol),S[#S][3]));
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


def local_gain(norm_q: int, depth: int) -> Decimal:
    # elementary.local_increment has the real-place factor 1/2; the
    # quadratic-base / prime-ideal normalization supplies the second 1/2.
    return elementary.local_increment(norm_q, depth) / 2


def build_frontier(
    ideals: list[tuple[int, int, str, int | None]],
    slope_floor: Decimal = Decimal("0.01"),
) -> tuple[
    list[tuple[Decimal, Decimal, Decimal, int, int, int]], Decimal
]:
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]] = []
    maximum_omitted = Decimal(0)
    for ideal_index, ideal in enumerate(ideals):
        norm_q = ideal[0]
        cost = Decimal(norm_q).ln() / 2
        previous: Decimal | None = None
        depth = 1
        while True:
            gain = local_gain(norm_q, depth)
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


def envelope(
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]],
    target: Decimal,
) -> tuple[Decimal, int, Decimal, Decimal]:
    cost_sum = Decimal(0)
    gain_sum = Decimal(0)
    for index, (slope, cost, gain, _, _, _) in enumerate(increments):
        if cost_sum + cost >= target:
            fraction = (target - cost_sum) / cost
            assert 0 <= fraction <= 1
            return gain_sum + fraction * gain, index, fraction, slope
        cost_sum += cost
        gain_sum += gain
    raise AssertionError("target exceeds the retained frontier")


def cumulative_frontier(
    increments: list[tuple[Decimal, Decimal, Decimal, int, int, int]],
) -> tuple[
    list[tuple[Decimal, Decimal, Decimal, int, int, int]],
    list[Decimal],
    list[Decimal],
]:
    costs = [Decimal(0)]
    gains = [Decimal(0)]
    for _, cost, gain, _, _, _ in increments:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
    return increments, costs, gains


def fast_envelope(
    frontier: tuple[
        list[tuple[Decimal, Decimal, Decimal, int, int, int]],
        list[Decimal],
        list[Decimal],
    ],
    target: Decimal,
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
    ramified: list[tuple[int, int, str, int | None]],
    useful: list[tuple[int, int, str, int | None]],
) -> tuple[
    Decimal,
    tuple[
        list[tuple[Decimal, Decimal, Decimal, int, int, int]],
        list[Decimal],
        list[Decimal],
    ],
    Decimal,
]:
    log_rd = Decimal(D).ln() / 2 + sum(
        Decimal(row[0]).ln() / 4 for row in ramified
    )
    increments, maximum_omitted = build_frontier(useful)
    return log_rd, cumulative_frontier(increments), maximum_omitted


def evaluate_prepared(
    log_rd: Decimal,
    frontier: tuple[
        list[tuple[Decimal, Decimal, Decimal, int, int, int]],
        list[Decimal],
        list[Decimal],
    ],
    alpha: Decimal,
    anchor: Decimal,
) -> list[tuple[Decimal, Decimal, Decimal, int, Decimal, Decimal]]:
    constant = Decimal(SAFE_C.numerator) / Decimal(SAFE_C.denominator)
    records: list[tuple[Decimal, Decimal, Decimal, int, Decimal, Decimal]] = []
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
        records.append((margin, derivative, slope, index, fraction, value))
    return records


def endpoint_data(
    ramified: list[tuple[int, int, str, int | None]],
    useful: list[tuple[int, int, str, int | None]],
    alpha: Decimal,
    anchor: Decimal,
) -> tuple[
    Decimal,
    list[tuple[Decimal, Decimal, Decimal, int, Decimal, Decimal]],
    Decimal,
]:
    log_rd, frontier, maximum_omitted = prepare_endpoint_data(
        ramified, useful
    )
    return (
        log_rd,
        evaluate_prepared(log_rd, frontier, alpha, anchor),
        maximum_omitted,
    )


def fixed_anchor_roots(
    ramified: list[tuple[int, int, str, int | None]],
    useful: list[tuple[int, int, str, int | None]],
    anchor: Decimal,
) -> list[tuple[Decimal, Decimal]]:
    log_rd, frontier, _ = prepare_endpoint_data(ramified, useful)
    brackets: list[tuple[Decimal, Decimal]] = []
    for endpoint in (0, 1):
        low = Decimal("0.49369312")
        high = Decimal("0.49369313")
        assert evaluate_prepared(log_rd, frontier, low, anchor)[endpoint][0] < 0
        assert evaluate_prepared(log_rd, frontier, high, anchor)[endpoint][0] > 0
        for _ in range(100):
            middle = (low + high) / 2
            if evaluate_prepared(log_rd, frontier, middle, anchor)[endpoint][0] > 0:
                high = middle
            else:
                low = middle
        brackets.append((low, high))
    return brackets


def optimize_diagnostic(
    ramified: list[tuple[int, int, str, int | None]],
    useful: list[tuple[int, int, str, int | None]],
) -> tuple[Decimal, Decimal, list[tuple[Decimal, Decimal, Decimal, int, Decimal, Decimal]], Decimal]:
    """Find the equal-endpoint anchor, then recertify at ALPHA."""
    log_rd, frontier, _ = prepare_endpoint_data(ramified, useful)

    def endpoint_root(anchor: Decimal, endpoint: int) -> Decimal:
        low, high = Decimal("0.48"), Decimal("0.51")
        assert evaluate_prepared(log_rd, frontier, low, anchor)[endpoint][0] < 0
        assert evaluate_prepared(log_rd, frontier, high, anchor)[endpoint][0] > 0
        for _ in range(75):
            middle = (low + high) / 2
            if evaluate_prepared(log_rd, frontier, middle, anchor)[endpoint][0] > 0:
                high = middle
            else:
                low = middle
        return (low + high) / 2

    low_w, high_w = Decimal("10000"), Decimal("100000")
    low_difference = endpoint_root(low_w, 0) - endpoint_root(low_w, 1)
    high_difference = endpoint_root(high_w, 0) - endpoint_root(high_w, 1)
    assert low_difference * high_difference < 0
    for _ in range(70):
        middle_w = (low_w + high_w) / 2
        difference = endpoint_root(middle_w, 0) - endpoint_root(middle_w, 1)
        if low_difference * difference <= 0:
            high_w, high_difference = middle_w, difference
        else:
            low_w, low_difference = middle_w, difference
    anchor = (low_w + high_w) / 2
    threshold = max(endpoint_root(anchor, 0), endpoint_root(anchor, 1))
    records = evaluate_prepared(log_rd, frontier, ALPHA, anchor)
    return threshold, anchor, records, log_rd


def ray_assignment_audit(
    universe: list[tuple[int, int, str, int | None]],
) -> tuple[
    dict[str, tuple], tuple[int, int], tuple[int, int, int | None, int]
]:
    """Audit every possible rank drop under an arbitrary 219-ideal set."""
    units, colored = exact_ray_rows()
    prefix = colored[:T_COUNT]
    assert prefix[-1] == (1_213, 1_213, 395, 6)
    assert gf2_rank(units + [row[3] for row in prefix]) == 4
    assert all(
        gf2_rank(units + [row[3] for row in colored[:stop]]) == 4
        for stop in range(205, 251)
    )

    # The canonical rank is locally stable: all 219*81 one-for-one swaps
    # with the next ideals retain full ray rank.
    swap_ranks: dict[int, int] = {}
    for removed in range(T_COUNT):
        remainder = prefix[:removed] + prefix[removed + 1 :]
        for added in colored[T_COUNT : T_COUNT + 81]:
            rank = gf2_rank(units + [row[3] for row in remainder] + [added[3]])
            swap_ranks[rank] = swap_ranks.get(rank, 0) + 1
    assert swap_ranks == {4: 17_739}

    # A rank-three set lies in one of the three hyperplanes containing the
    # two-dimensional unit span.  Rank two means every prime column lies in
    # the unit span itself.  These four cases, plus full rank, exhaust all
    # possible spans in the four-dimensional ray quotient.
    functionals = [
        ell
        for ell in range(1, 16)
        if all(parity_dot(ell, unit) == 0 for unit in units)
    ]
    assert len(functionals) == 3
    unit_span = {0, units[0], units[1], units[0] ^ units[1]}
    case_specs: list[tuple[str, list[tuple[int, int, int | None, int]], int]] = [
        ("rank4", colored, 4)
    ]
    case_specs.extend(
        (
            f"rank3_ell{ell}",
            [row for row in colored if parity_dot(ell, row[3]) == 0],
            3,
        )
        for ell in functionals
    )
    case_specs.append(
        ("rank2", [row for row in colored if row[3] in unit_span], 2)
    )

    universe_by_key = {
        (norm_q, prime, root): row
        for row in universe
        for norm_q, prime, _, root in [row]
    }
    output: dict[str, tuple] = {}
    for name, allowed, constraint_rank in case_specs:
        selected_colored = allowed[:T_COUNT]
        assert len(selected_colored) == T_COUNT
        assert gf2_rank(
            units + [row[3] for row in selected_colored]
        ) == constraint_rank
        selected_keys = {
            (norm_q, prime, root)
            for norm_q, prime, root, _ in selected_colored
        }
        ramified = [universe_by_key[key] for key in selected_keys]
        ramified.sort(
            key=lambda row: (
                row[0], row[1], row[2],
                row[3] if row[3] is not None else -1,
            )
        )
        generator_rank = T_COUNT + 2 - constraint_rank
        useful_count = (
            (generator_rank * generator_rank - 1) // 4
            - (generator_rank + 1)
            - T_COUNT
        )
        useful = [
            row
            for row in universe
            if (row[0], row[1], row[3]) not in selected_keys
        ][:useful_count]
        threshold, anchor, records, log_rd = optimize_diagnostic(
            ramified, useful
        )
        if name != "rank4":
            assert threshold > Decimal("0.49386")
            assert records[0][0] < Decimal("-20")
            assert records[1][0] < Decimal("-40")
            assert records[0][1] > Decimal("0.001")
            assert records[1][1] < Decimal("-0.001")
        output[name] = (
            generator_rank,
            useful_count,
            selected_colored[-1],
            colored.index(selected_colored[-1]) + 1,
            sum(row not in selected_colored for row in prefix),
            log_rd,
            threshold,
            anchor,
            records[0][:3],
            records[1][:3],
        )

    rank_three = sorted(
        (value[4], value[3], value[2][0])
        for name, value in output.items()
        if name.startswith("rank3")
    )
    assert rank_three == [(95, 425, 3_089), (108, 464, 3_389), (117, 472, 3_467)]
    assert output["rank2"][3:5] == (979, 160)
    assert output["rank2"][2][0] == 8_009

    # D-independent all-depth exchange inequalities.  They certify that the
    # smallest allowed T and first remaining formal-useful ideals used above
    # are optimistic among every assignment with the same ray-color span.
    useful_lower = Fraction(1, 6) - Fraction(1, 2 * 81**2)
    useful_upper = Fraction(729, 6_400)
    assert useful_lower > useful_upper
    minimum_log_rd = min(value[5] for value in output.values())
    constant = Decimal(SAFE_C.numerator) / Decimal(SAFE_C.denominator)
    rho_lower = Decimal(1) / (1 + (-minimum_log_rd).exp() / constant)
    assert rho_lower > Decimal(1) / Decimal(9).ln()
    return output, (units[0], units[1]), colored[220]


def main() -> None:
    getcontext().prec = 100
    configure_elementary_module()

    primes = elementary.prime_sieve(250_000)
    assert D == 467 * 1_759
    assert D % 8 == 5 and D % 3 == 2
    assert all(D % (p * p) for p in primes if p * p <= D)
    assert elementary.norm(FUNDAMENTAL_UNIT) == 1
    assert elementary.negative_at_embedding(FUNDAMENTAL_UNIT, False) == 0
    assert elementary.negative_at_embedding(FUNDAMENTAL_UNIT, True) == 0

    ideals = elementary.prime_ideals(primes, 250_000)
    ramified = ideals[:T_COUNT]
    assert ramified[-1] == (1_213, 1_213, "split", 395)
    assert ideals[114] == (467, 467, "ramified", 234)
    assert ideals[278] == (1_759, 1_759, "ramified", 880)

    kernel, metadata = exact_kummer_kernel()
    assert metadata == (1, 1, 221, 4, 217, 1_213, 395)
    assert len(kernel) == GENERATOR_RANK

    units_mod_four = [
        (a, b)
        for a in range(4)
        for b in range(4)
        if elementary.norm((a, b)) % 2
    ]
    square_residues = {
        tuple(value % 4 for value in elementary.multiply(unit, unit))
        for unit in units_mod_four
    }
    assert len(units_mod_four) == 12 and len(square_residues) == 3
    for element in kernel:
        assert elementary.negative_at_embedding(element, False) == 0
        assert elementary.negative_at_embedding(element, True) == 0
        assert (element[0] % 4, element[1] % 4) in square_residues

    useful: list[tuple[int, int, str, int | None]] = []
    rejected: list[tuple[int, int, str, int | None]] = []
    maximum_trials = 0
    base_ramified_position: int | None = None
    for ideal in ideals[T_COUNT:]:
        norm_q, prime, kind, root = ideal
        if prime == 3:
            continue
        is_useful = True
        if norm_q % 3 == 2:
            assert norm_q == prime and root is not None
            is_useful = False
            trials = 0
            for a, b in kernel:
                trials += 1
                residue = (a + b * root) % prime
                assert residue
                if pow(residue, (prime - 1) // 2, prime) == prime - 1:
                    is_useful = True
                    break
            maximum_trials = max(maximum_trials, trials)
        if is_useful:
            useful.append(ideal)
            if prime == 1_759 and kind == "ramified":
                base_ramified_position = len(useful)
        else:
            rejected.append(ideal)
        if len(useful) == USEFUL_COUNT:
            break
    assert not rejected
    assert useful[-1] == (122_527, 122_527, "split", 3_683)
    assert base_ramified_position == 60
    assert maximum_trials == 12

    relation_bound = (GENERATOR_RANK + 1) + T_COUNT + USEFUL_COUNT
    assert relation_bound == 11_772
    assert 4 * relation_bound == GENERATOR_RANK**2 - 1

    log_rd, records, maximum_omitted = endpoint_data(
        ramified, useful, ALPHA, W0
    )
    maximum_fourth_slope = max(
        local_gain(ideal[0], 4) / (Decimal(ideal[0]).ln() / 2)
        for ideal in useful
    )
    assert log_rd > Decimal("322.22549")
    assert log_rd < Decimal("322.22550")
    assert min(record[0] for record in records) > Decimal("0.001")
    assert maximum_fourth_slope < records[1][2]
    assert maximum_omitted < records[1][2]
    roots = fixed_anchor_roots(ramified, useful, W0)
    assert max(high for _, high in roots) < ALPHA

    ray_cases, unit_columns, neighbor_row = ray_assignment_audit(ideals)
    # Neighboring T=221 cross-check: the ray rank stays four, hence d=219;
    # its exact all-square relation budget is again saturated by N=11549.
    assert ray_cases["rank4"][0] == GENERATOR_RANK
    unit_rows = list(unit_columns)
    assert neighbor_row[:3] == (1_223, 1_223, 34)
    neighbor_d = 221 + 2 - 4
    neighbor_n = (
        (neighbor_d * neighbor_d - 1) // 4 - (neighbor_d + 1) - 221
    )
    assert (neighbor_d, neighbor_n) == (219, 11_549)

    print("field / class / narrow class: CERTIFIED", D, 1, 2)
    print("T last / S-unit columns / ray rank / d:", ramified[-1], *metadata[2:5])
    print("useful / rejected / last:", len(useful), len(rejected), useful[-1])
    print("base-ramified useful position / max trials:", base_ramified_position, maximum_trials)
    print("relations / log RD:", relation_bound, log_rd)
    print("endpoint records:", records)
    print("maximum omitted slope:", maximum_omitted)
    print("maximum fourth-depth slope:", maximum_fourth_slope)
    print("fixed-anchor threshold brackets:", roots)
    print("ray unit columns:", unit_columns)
    print("rank-aware assignment cases:")
    for name, value in ray_cases.items():
        print(" ", name, value)
    print("neighbor T=221 / d / N:", neighbor_row, neighbor_d, neighbor_n)
    print("hostile audit F_2(n) << n^0.49369313: CERTIFIED")


if __name__ == "__main__":
    main()
