#!/usr/bin/env python3
"""Exact verifier for arbitrary-child substitution in the E(7,7) reset.

The script checks the separated-composition face recurrence by rational
brute force, certifies the rank and coefficient-degree recurrences, and
evaluates the two-boundary max-plus Bellman state with exact Fractions.
No floating-point predicate is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb


Point = tuple[Q, Q]
Profile = tuple[int, int, int, int]  # n, caps, cups, ordinary faces
Rank = tuple[int, int, int, int]     # n, cap rank, cup rank, face rank
Matrix = tuple[tuple[Q, Q], tuple[Q, Q]]
Candidate = tuple[int, int]          # total singleton degree, path edges
CandidateMatrix = tuple[
    tuple[Candidate, Candidate], tuple[Candidate, Candidate]
]


def orient(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def normalize(points: tuple[Point, ...]) -> tuple[Point, ...]:
    if len(points) == 1:
        return ((Q(0), Q(0)),)
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    dx, dy = max(xs) - min(xs), max(ys) - min(ys)
    return tuple(((x - min(xs)) / dx if dx else Q(0),
                  (y - min(ys)) / dy if dy else Q(0))
                 for x, y in points)


def slope_bound(points: tuple[Point, ...]) -> Q:
    return max((abs((b[1] - a[1]) / (b[0] - a[0]))
                for a, b in combinations(points, 2)), default=Q(0))


def separated(left: tuple[Point, ...],
              right: tuple[Point, ...]) -> tuple[Point, ...]:
    """High-left/low-right rational separated composition."""
    a, b = normalize(left), normalize(right)
    height = int(3 * max(slope_bound(a), slope_bound(b)) + 6)
    out = (tuple((x, y + height) for x, y in a)
           + tuple((x + 2, y) for x, y in b))
    assert len({p[0] for p in out}) == len(out)
    # The two mixed sign rules used in the proof.
    n = len(a)
    for i, j in combinations(range(n), 2):
        for k in range(n, len(out)):
            assert orient(out[i], out[j], out[k]) < 0
    for i in range(n):
        for j, k in combinations(range(n, len(out)), 2):
            assert orient(out[i], out[j], out[k]) > 0
    return out


@lru_cache(None)
def cup_cap_set(r: int, s: int) -> tuple[Point, ...]:
    assert r >= 2 and s >= 2
    if r == 2 or s == 2:
        return ((Q(0), Q(0)),)
    return separated(cup_cap_set(r, s - 1), cup_cap_set(r - 1, s))


def convex_hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
    if len(points) <= 1:
        return points
    ordered = sorted(points)

    def half(seq):
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lower = half(ordered)
    upper = half(reversed(ordered))
    return tuple(lower[:-1] + upper[:-1])


def is_cup(points: tuple[Point, ...]) -> bool:
    points = tuple(sorted(points))
    return all(orient(points[i], points[i + 1], points[i + 2]) > 0
               for i in range(len(points) - 2))


def is_cap(points: tuple[Point, ...]) -> bool:
    points = tuple(sorted(points))
    return all(orient(points[i], points[i + 1], points[i + 2]) < 0
               for i in range(len(points) - 2))


def brute_profile(points: tuple[Point, ...]) -> Profile:
    cap = cup = face = 0
    for mask in range(1, 1 << len(points)):
        subset = tuple(points[i] for i in range(len(points))
                       if mask >> i & 1)
        cap += is_cap(subset)
        cup += is_cup(subset)
        face += len(convex_hull(subset)) == len(subset)
    return len(points), cap, cup, face


def compose_profile(a: Profile, b: Profile) -> Profile:
    na, ca, ua, wa = a
    nb, cb, ub, wb = b
    return (na + nb,
            ca * (1 + nb) + cb,
            ua + ub * (1 + na),
            wa + wb + ca * ub)


def compose_rank(a: Rank, b: Rank) -> Rank:
    na, ca, ua, wa = a
    nb, cb, ub, wb = b
    return (na + nb,
            max(ca + 1, cb),
            max(ua, ub + 1),
            max(wa, wb, ca + ub))


def e_operator(r: int, s: int, leaf, compose):
    cache = {}

    def go(rr: int, ss: int):
        if rr == 2 or ss == 2:
            return leaf
        key = rr, ss
        if key not in cache:
            cache[key] = compose(go(rr, ss - 1), go(rr - 1, ss))
        return cache[key]

    return go(r, s)


@dataclass(frozen=True)
class Degrees:
    """Leading degrees of flattened C_i, U_i, and K_ij coefficients."""

    c: tuple[int, ...]
    u: tuple[int, ...]
    edge: tuple[tuple[int, int, int], ...]


def compose_degrees(a: Degrees, b: Degrees) -> Degrees:
    na = len(a.c)
    c = tuple(z + 1 for z in a.c) + b.c
    u = a.u + tuple(z + 1 for z in b.u)
    edge = list(a.edge)
    edge.extend((na + i, na + j, d) for i, j, d in b.edge)
    edge.extend((i, na + j, a.c[i] + b.u[j])
                for i in range(na) for j in range(len(b.c)))
    return Degrees(c, u, tuple(edge))


def combine_matrix(a: Matrix, b: Matrix, q: Q) -> Matrix:
    """Two-boundary Bellman recurrence, indices are alpha,beta in {0,1}."""
    return tuple(tuple(max(a[alpha][beta] + beta,
                           b[alpha][beta] + alpha,
                           a[alpha][1] + b[1][beta] - q)
                       for beta in range(2))
                 for alpha in range(2))  # type: ignore[return-value]


def bellman_power(h: int, q: Q) -> Matrix:
    matrix: Matrix = ((Q(0), Q(0)), (Q(0), Q(0)))
    for _ in range(h):
        matrix = e_operator(7, 7, matrix,
                            lambda a, b: combine_matrix(a, b, q))
    return matrix


def candidate_value(p: Candidate, q: Q) -> Q:
    degree, edges = p
    return Q(degree) - edges * q


def candidate_root(p: Candidate, budget: Q) -> Q:
    degree, edges = p
    if edges == 0:
        return Q(-10**30)
    return Q(degree - budget, edges)


def choose_candidate(candidates: list[Candidate], q: Q,
                     budget: Q) -> Candidate:
    # The root tie-break makes the parametric envelope walk monotone.
    return max(candidates,
               key=lambda p: (candidate_value(p, q),
                              candidate_root(p, budget)))


def combine_candidates(a: CandidateMatrix, b: CandidateMatrix,
                       q: Q, budget: Q) -> CandidateMatrix:
    out = []
    for alpha in range(2):
        row = []
        for beta in range(2):
            row.append(choose_candidate([
                (a[alpha][beta][0] + beta, a[alpha][beta][1]),
                (b[alpha][beta][0] + alpha, b[alpha][beta][1]),
                (a[alpha][1][0] + b[1][beta][0],
                 a[alpha][1][1] + b[1][beta][1] + 1),
            ], q, budget))
        out.append(tuple(row))
    return tuple(out)  # type: ignore[return-value]


def candidate_power(h: int, q: Q, budget: Q) -> CandidateMatrix:
    zero: CandidateMatrix = (((0, 0), (0, 0)),
                             ((0, 0), (0, 0)))
    matrix = zero
    for _ in range(h):
        matrix = e_operator(
            7, 7, matrix,
            lambda a, b: combine_candidates(a, b, q, budget))
    return matrix


def exact_threshold(h: int, budget: Q) -> tuple[Q, Candidate, int]:
    """Least q with max_path(sum degree - q*edges) <= budget."""
    q = Q(0)
    for iteration in range(1, 1000):
        witness = candidate_power(h, q, budget)[0][0]
        if candidate_value(witness, q) <= budget:
            return q, witness, iteration
        next_q = candidate_root(witness, budget)
        assert next_q > q
        q = next_q
    raise AssertionError("parametric Bellman walk did not terminate")


def brute_bellman(degrees: Degrees, q: Q) -> Matrix:
    n = len(degrees.c)
    edge = {(i, j): d for i, j, d in degrees.edge}
    answer = [[None, None], [None, None]]
    for alpha in range(2):
        for beta in range(2):
            best = None
            for mask in range(1, 1 << n):
                path = [i for i in range(n) if mask >> i & 1]
                value = Q(alpha * degrees.u[path[0]]
                          + beta * degrees.c[path[-1]])
                for i, j in zip(path, path[1:]):
                    value += edge[i, j] - q
                best = value if best is None else max(best, value)
            answer[alpha][beta] = best
    return tuple(tuple(row) for row in answer)  # type: ignore[return-value]


def es_guaranteed_rank(population: int) -> int:
    """Largest r certified by the elementary cup--cap upper bound."""
    r = 3
    while population >= comb(2 * (r + 1) - 4, (r + 1) - 2) + 1:
        r += 1
    return r


def main() -> None:
    # Exact rational brute-force validation of the recurrence, including
    # genuinely heterogeneous children.
    expected = {
        (3, 3): (2, 3, 3, 3),
        (3, 4): (3, 7, 6, 7),
        (3, 5): (4, 15, 10, 15),
        (4, 3): (3, 6, 7, 7),
        (4, 4): (6, 31, 31, 50),
        (4, 5): (10, 170, 101, 375),
        (5, 3): (4, 10, 15, 15),
        (5, 4): (10, 101, 170, 375),
    }
    for rs, profile in expected.items():
        points = cup_cap_set(*rs)
        assert brute_profile(points) == profile
        recursive = e_operator(*rs, (1, 1, 1, 1), compose_profile)
        assert recursive == profile

    bad_child = tuple((Q(x), Q(y)) for x, y in
                      ((0, 0), (1, 3), (2, 1), (3, 0)))
    other_child = cup_cap_set(3, 4)
    heterogeneous = separated(bad_child, other_child)
    assert brute_profile(heterogeneous) == compose_profile(
        brute_profile(bad_child), brute_profile(other_child))

    # The exact additive, rather than multiplicative, rank recurrence.
    rank: Rank = (1, 1, 1, 1)
    rank_rows = []
    for h in range(1, 9):
        rank = e_operator(7, 7, rank, compose_rank)
        assert rank == (252 ** h, 5 * h + 1, 5 * h + 1, 10 * h)
        rank_rows.append((h, rank[1], rank[2], rank[3]))

    base_degrees = e_operator(
        7, 7, Degrees((0,), (0,), ()), compose_degrees)
    assert (len(base_degrees.c), max(base_degrees.c),
            max(base_degrees.u)) == (252, 5, 5)
    assert max(d for _, _, d in base_degrees.edge) == 8
    assert len(base_degrees.edge) == comb(252, 2)

    # Independent path enumeration on the six-leaf E(4,4) tree checks all
    # four boundary states, not only the ordinary 00 entry.
    small_degrees = e_operator(
        4, 4, Degrees((0,), (0,), ()), compose_degrees)
    q_probe = Q(3, 2)
    recursive_probe = e_operator(
        4, 4, ((Q(0), Q(0)), (Q(0), Q(0))),
        lambda a, b: combine_matrix(a, b, q_probe))
    assert recursive_probe == brute_bellman(small_degrees, q_probe)

    # At q=0 the ramp width has the closed form
    # 182*252^(h-1)-2; this is huge, even though any single edge has degree
    # only 10h-2.
    widths = []
    for h in range(1, 9):
        matrix = bellman_power(h, Q(0))
        r = 182 * 252 ** (h - 1) - 2
        assert matrix == ((Q(r), Q(r + 1)),
                          (Q(r + 1), Q(r + 2)))
        widths.append(r)

    # Exact half-coefficient scalar payments.  Here D=2^L, L=14^h,
    # and the local log-face budget is w=L^2/2.  theta is measured in
    # units of L, so the forced additive log payment is theta*L.
    expected_theta = {
        1: Q(33, 7),
        2: Q(174, 17),
        3: Q(14740, 1007),
        4: Q(248434, 12601),
        5: Q(6081464, 254015),
        6: Q(55420988, 1905121),
        7: Q(1067503776, 32006015),
        8: Q(18497721126, 480090241),
    }
    threshold_rows = []
    for h, expected_q in expected_theta.items():
        length_log = 14 ** h
        budget = Q(length_log, 2)
        theta, witness, iterations = exact_threshold(h, budget)
        assert theta == expected_q
        assert candidate_value(witness, theta) == budget
        threshold_rows.append((h, theta, witness, iterations))

    # With at most R identical numerical endpoint profiles, one profile
    # occupies M/R macro leaves.  The classical ES upper bound then gives
    # a same-profile convex support and hence a stationary K_ij monomial.
    es_rows = []
    for h in range(1, 9):
        macro = 252 ** h
        one = es_guaranteed_rank(macro)
        two = es_guaranteed_rank(macro // 2)
        assert one >= two >= 3
        es_rows.append((h, one, two, two - 2))

    print("PASS")
    print("  rational profile brute force:", expected)
    print("  heterogeneous profile:", brute_profile(heterogeneous))
    print("  additive rank rows (h,cap,cup,face):", rank_rows)
    print("  base flattened degrees: leaves=252, cap=5, cup=5, K=8")
    print("  q=0 ramp widths:", widths)
    print("  exact half-scale thresholds (h,theta,(degree,edges),iters):")
    for row in threshold_rows:
        print("   ", row)
    print("  ES finite-profile rows (h,rank R=1,rank R=2,K degree R=2):")
    for row in es_rows:
        print("   ", row)


if __name__ == "__main__":
    main()
