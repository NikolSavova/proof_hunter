#!/usr/bin/env python3
"""Exact S-class/ray audit and all-useful endpoint kill for genus leaders."""

from __future__ import annotations

from bisect import bisect_left
from decimal import Decimal, getcontext
from fractions import Fraction
from math import exp, log, log1p, sqrt
import re
import shutil
import subprocess


ALPHA_FLOAT = 0.49369313
# Rigorous lower bound for 2 sqrt(3) / pi.  A smaller disk constant makes the
# endpoint RHS smaller and is therefore the hostile choice for a no-go.
PACKING_FRACTION = Fraction(11_978, 10_863)
PACKING_FLOAT = float(PACKING_FRACTION)
NORM_LIMIT = 250_000
FIELDS = {
    # D: (genus-screen T, exact h, ordinary 2-rank, narrow 2-rank,
    #     last norm at T=180, last norm at the genus-screen T)
    880_440: (216, 16, 4, 5, 829, 1_163),
    963_480: (220, 32, 4, 5, 907, 1_171),
    937_365: (220, 16, 4, 5, 887, 1_163),
    871_080: (218, 48, 4, 5, 877, 1_193),
    552_552: (218, 16, 4, 5, 853, 1_171),
}
EXPECTED_ENDPOINTS = {
    880_440: (217, -1.6761378027918),
    963_480: (223, -1.9991880031127494),
    937_365: (223, -2.0632359089140664),
    871_080: (219, -2.105011790591334),
    552_552: (221, -2.4321194445649326),
}


def prime_sieve(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = (limit - p * p) // p + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_ideal_norms(discriminant: int, primes: list[int]) -> list[int]:
    ideals: list[int] = []
    for p in primes:
        if p == 2 or p > NORM_LIMIT:
            continue
        if discriminant % p == 0:
            ideals.append(p)
            continue
        symbol = pow(discriminant % p, (p - 1) // 2, p)
        if symbol == 1:
            ideals.extend((p, p))
        else:
            assert symbol == p - 1
            if p * p <= NORM_LIMIT:
                ideals.append(p * p)
    ideals.sort()
    return ideals


def exact_pari_metadata() -> dict[int, tuple[int, ...]]:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP is required (tested with GP 2.17.4)")
    ds = ",".join(map(str, FIELDS))
    ts = ",".join(str(FIELDS[d][0]) for d in FIELDS)
    script = rf"""Ds=[{ds}];ts=[{ts}];
for(j=1,#Ds,D=Ds[j];if(D%4==1,pol=x^2-x-(D-1)/4,pol=x^2-D/4);bnf=bnfinit(pol,1);cert=bnfcertify(bnf);nf=bnf.nf;nar=bnrinit(bnf,[1,[1,1]],0,2);ideals=List();forprime(p=3,5000,dec=idealprimedec(nf,p);for(i=1,#dec,Q=idealnorm(nf,dec[i]);if(Q<=5000,listput(ideals,[Q,p,dec[i]]))));ideals=vecsort(Vec(ideals),[1,2]);S=ideals[1..180];su=bnfsunit(bnf,vector(#S,i,S[i][3]));u=bnfunits(bnf,vector(#S,i,S[i][3]));bid=idealstar(nf,[4,[1,1]],1,2);M=Mat(vector(#u[1],i,ideallog(nf,u[1][i],bid)));cr=sum(i=1,#bnf.cyc,bnf.cyc[i]%2==0);nr=#nar.cyc;print("META,",D,",",bnf.disc,",",cert,",",bnf.no,",",cr,",",nr,",",su[5][1],",",#su[5][2],",",#u[1],",",#bid.cyc,",",matrank(Mod(M,2)),",",ideals[180][1],",",ideals[ts[j]][1]));
"""
    output = subprocess.check_output(
        [gp, "-fq", "-s", "4G"], input=script, text=True, timeout=90
    )
    records: dict[int, tuple[int, ...]] = {}
    for line in output.splitlines():
        if line.startswith("META,"):
            values = tuple(map(int, line.split(",")[1:]))
            records[values[0]] = values[1:]
    return records


def local_gain_float(q: int, depth: int) -> float:
    x = 1.0 / (q * q)
    previous = 1.0
    total = 1.0
    power = 1.0
    for _ in range(depth):
        previous = total
        power *= x
        total += power
    return 0.25 * log(((depth + 1) / total) / (depth / previous))


def all_useful_score(discriminant: int, ideals: list[int], t: int):
    d = t - 2
    useful = (d * d - 1) // 4 - (d + 1) - t
    assert useful > 0 and t + useful <= len(ideals)
    items: list[tuple[float, float, float]] = []
    for q in ideals[t : t + useful]:
        cost = 0.5 * log(q)
        for depth in range(1, 4):
            gain = local_gain_float(q, depth)
            items.append((gain / cost, cost, gain))
    items.sort(reverse=True)
    costs = [0.0]
    gains = [0.0]
    for _, cost, gain in items:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
    log_rd = 0.5 * log(discriminant) + 0.25 * sum(
        log(q) for q in ideals[:t]
    )

    def envelope(target: float) -> float:
        index = bisect_left(costs, target)
        assert 0 < index < len(costs)
        fraction = (target - costs[index - 1]) / (
            costs[index] - costs[index - 1]
        )
        return gains[index - 1] + fraction * (
            gains[index] - gains[index - 1]
        )

    def rhs(w: float) -> float:
        exponent = 2 * (2 * ALPHA_FLOAT - 1) * w - log_rd
        return (
            log(PACKING_FLOAT)
            + log_rd
            + (2 - 4 * ALPHA_FLOAT) * w
            + log1p(exp(exponent) / PACKING_FLOAT)
        )

    def margin(w: float) -> float:
        return min(
            envelope(2 * ALPHA_FLOAT * w) - rhs(w),
            envelope(4 * ALPHA_FLOAT * w) - rhs(2 * w),
        )

    # The envelope is concave, rhs is convex, and a pointwise minimum of
    # concave functions is concave.  Golden search therefore sees the global
    # maximum of the two-endpoint lower envelope.
    low = 1e-12
    high = costs[-1] / (4 * ALPHA_FLOAT) * (1 - 1e-12)
    phi = (sqrt(5) - 1) / 2
    x = high - phi * (high - low)
    y = low + phi * (high - low)
    fx = margin(x)
    fy = margin(y)
    for _ in range(100):
        if fx < fy:
            low, x, fx = x, y, fy
            y = low + phi * (high - low)
            fy = margin(y)
        else:
            high, y, fy = y, x, fx
            x = high - phi * (high - low)
            fx = margin(x)
    w = (low + high) / 2
    return margin(w), w, d, useful


def decimal_top_certificate(
    discriminant: int, ideals: list[int], t: int, precision: int
):
    getcontext().prec = precision
    alpha = Decimal("0.49369313")
    packing = Decimal(PACKING_FRACTION.numerator) / Decimal(
        PACKING_FRACTION.denominator
    )
    d = t - 2
    useful = (d * d - 1) // 4 - (d + 1) - t
    items: list[tuple[Decimal, Decimal, Decimal]] = []
    maximum_fourth_slope = Decimal(0)
    for q_int in ideals[t : t + useful]:
        q = Decimal(q_int)
        cost = q.ln() / 2
        parameter = Decimal(1) / (q * q)
        power = Decimal(1)
        total = Decimal(1)
        for depth in range(1, 5):
            previous = total
            power *= parameter
            total += power
            ratio = (Decimal(depth + 1) / total) / (
                Decimal(depth) / previous
            )
            gain = ratio.ln() / 4
            slope = gain / cost
            if depth <= 3:
                items.append((slope, cost, gain))
            else:
                maximum_fourth_slope = max(maximum_fourth_slope, slope)
    items.sort(reverse=True)
    costs = [Decimal(0)]
    gains = [Decimal(0)]
    slopes = [Decimal(0)]
    for slope, cost, gain in items:
        costs.append(costs[-1] + cost)
        gains.append(gains[-1] + gain)
        slopes.append(slope)
    log_rd = Decimal(discriminant).ln() / 2 + sum(
        (Decimal(q).ln() / 4 for q in ideals[:t]), Decimal(0)
    )

    def envelope(target: Decimal):
        index = bisect_left(costs, target)
        assert 0 < index < len(costs)
        fraction = (target - costs[index - 1]) / (
            costs[index] - costs[index - 1]
        )
        value = gains[index - 1] + fraction * (
            gains[index] - gains[index - 1]
        )
        return value, slopes[index]

    coefficient = 2 * (2 * alpha - 1)

    def rhs(w: Decimal):
        exponential = (coefficient * w - log_rd).exp() / packing
        return (
            packing.ln()
            + log_rd
            + (2 - 4 * alpha) * w
            + (1 + exponential).ln()
        )

    def rhs_derivative(w: Decimal):
        exponential = (coefficient * w - log_rd).exp() / packing
        return (2 - 4 * alpha) + coefficient * exponential / (1 + exponential)

    def endpoints(w: Decimal):
        left_value, left_slope = envelope(2 * alpha * w)
        right_value, right_slope = envelope(4 * alpha * w)
        left = left_value - rhs(w)
        right = right_value - rhs(2 * w)
        left_derivative = 2 * alpha * left_slope - rhs_derivative(w)
        right_derivative = 4 * alpha * right_slope - 2 * rhs_derivative(2 * w)
        return left, right, left_derivative, right_derivative

    # Isolate the nonzero crossing of the endpoint margins.  At that crossing
    # the left branch is increasing and the right branch decreasing, which is
    # a global maximum certificate by concavity.
    low = Decimal("39000")
    high = Decimal("41000")
    assert (endpoints(low)[0] - endpoints(low)[1]) < 0
    assert (endpoints(high)[0] - endpoints(high)[1]) > 0
    for _ in range(4 * precision):
        middle = (low + high) / 2
        if endpoints(middle)[0] < endpoints(middle)[1]:
            low = middle
        else:
            high = middle
    w = (low + high) / 2
    left, right, left_derivative, right_derivative = endpoints(w)
    _, left_slope = envelope(2 * alpha * w)
    _, right_slope = envelope(4 * alpha * w)
    assert abs(left - right) < Decimal(10) ** (-(precision - 10))
    assert left_derivative > 0 and right_derivative < 0
    assert maximum_fourth_slope < min(left_slope, right_slope)
    return (
        w,
        min(left, right),
        left_derivative,
        right_derivative,
        maximum_fourth_slope,
        min(left_slope, right_slope),
    )


def main() -> None:
    sqrt_three_lower = Fraction(265, 153)
    assert sqrt_three_lower * sqrt_three_lower < 3
    x = Fraction(1, 5)
    atan_fifth_upper = sum(
        (-1) ** j * x ** (2 * j + 1) / (2 * j + 1) for j in range(5)
    )
    y = Fraction(1, 239)
    atan_239_lower = y - y**3 / 3
    pi_upper = 16 * atan_fifth_upper - 4 * atan_239_lower
    assert pi_upper < Fraction(355, 113)
    assert 2 * sqrt_three_lower / Fraction(355, 113) == PACKING_FRACTION

    metadata = exact_pari_metadata()
    assert set(metadata) == set(FIELDS)
    primes = prime_sieve(NORM_LIMIT)
    ideal_lists: dict[int, list[int]] = {}
    for discriminant, expected in FIELDS.items():
        leader_t, class_number, class_rank, narrow_rank, last_180, last_leader = expected
        # disc, cert, h, ordinary 2-rank, narrow 2-rank, S-class order,
        # S-class cyclic-factor count, S-unit columns, ray quotient rank,
        # image rank, last norm at 180, last norm at the genus-screen T.
        assert metadata[discriminant] == (
            discriminant,
            1,
            class_number,
            class_rank,
            narrow_rank,
            1,
            0,
            182,
            4,
            4,
            last_180,
            last_leader,
        )
        ideals = prime_ideal_norms(discriminant, primes)
        ideal_lists[discriminant] = ideals
        assert ideals[179] == last_180
        assert ideals[leader_t - 1] == last_leader

    # Cl_S is trivial already at T=180.  It remains trivial on enlarging S;
    # the 182 S-unit columns have surjective image in the four-dimensional
    # sign/mod-4 ray quotient.  Hence d=t+2-4=t-2 throughout this interval.
    endpoint_rows = {}
    for discriminant, ideals in ideal_lists.items():
        scores = [
            (all_useful_score(discriminant, ideals, t), t)
            for t in range(180, 281)
        ]
        score, best_t = max(scores)
        expected_t, expected_margin = EXPECTED_ENDPOINTS[discriminant]
        assert best_t == expected_t
        assert abs(score[0] - expected_margin) < 2e-10
        endpoint_rows[discriminant] = (best_t, *score)
    assert max(row[1] for row in endpoint_rows.values()) < -1.67

    outputs = [
        decimal_top_certificate(880_440, ideal_lists[880_440], 217, precision)
        for precision in (90, 150)
    ]
    assert abs(outputs[0][0] - outputs[1][0]) < Decimal("1e-70")
    assert abs(outputs[0][1] - outputs[1][1]) < Decimal("1e-70")
    assert outputs[1][1] < Decimal("-1.67")

    print("PARI BNF / S-class / ray audit: PASS")
    for discriminant in FIELDS:
        print("field metadata:", discriminant, metadata[discriminant])
    print("all-useful best rows (D,t,margin,w,d,N):")
    for discriminant, row in endpoint_rows.items():
        print(discriminant, *row)
    print("D=880440 90-digit cusp:", *outputs[0])
    print("D=880440 150-digit cusp:", *outputs[1])
    print("GENUS-BONUS LEADERS: EXACT-RANK / ALL-USEFUL NO-GO CERTIFIED")


if __name__ == "__main__":
    main()
