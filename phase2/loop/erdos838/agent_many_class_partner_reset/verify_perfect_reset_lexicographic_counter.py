#!/usr/bin/env python3
"""Exact verifier for the perfect-reset lexicographic counter-regression.

The verifier constructs the rational cup--cap set E(7,7), deterministically
finds fourteen 18-point colour classes and pair-edge-disjoint perfect bad-
circuit matchings, certifies the cup/cap rank bound, and checks the symbolic
pair decoder in the second lexicographic power.  All geometry uses Fraction
arithmetic; the fixed-seed search is deterministic and its output is fully
rechecked independently of the search path.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, product
from math import ceil, comb, log
import random


Point = tuple[Q, Q]
Pair = tuple[int, int]


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


def internal_slope_bound(points: tuple[Point, ...]) -> Q:
    return max((abs((b[1] - a[1]) / (b[0] - a[0]))
                for a, b in combinations(points, 2)), default=Q(0))


@lru_cache(None)
def cup_cap_set(r: int, s: int) -> tuple[Point, ...]:
    """Rational ES lower construction: no r-cup and no s-cap."""
    assert r >= 2 and s >= 2
    if r == 2 or s == 2:
        return ((Q(0), Q(0)),)
    # High-left A kills a crossing cup with two A points; low-right B kills
    # a crossing cap with two B points.
    a = normalize(cup_cap_set(r, s - 1))
    b = normalize(cup_cap_set(r - 1, s))
    slope_bound = max(internal_slope_bound(a), internal_slope_bound(b))
    height = ceil(3 * slope_bound + 5)
    out = (tuple((x, y + height) for x, y in a)
           + tuple((x + 2, y) for x, y in b))
    assert len({p[0] for p in out}) == len(out)
    return out


def is_bad_quad(indices: tuple[int, int, int, int],
                points: tuple[Point, ...]) -> bool:
    """A GP four-set is bad iff one point is inside the other triangle."""
    pts = [points[z] for z in indices]
    for hidden in range(4):
        z = pts[hidden]
        tri = [pts[q] for q in range(4) if q != hidden]
        a, b, c = tri
        direction = orient(a, b, c)
        signs = (orient(a, b, z), orient(b, c, z), orient(c, a, z))
        if all(sign * direction > 0 for sign in signs):
            return True
    return False


def cup_cap_lengths(points: tuple[Point, ...]) -> tuple[int, int, int]:
    order = sorted(range(len(points)), key=lambda z: points[z][0])
    cup: dict[tuple[int, int], int] = {}
    cap: dict[tuple[int, int], int] = {}
    triple_checks = 0
    for j in range(1, len(order)):
        for k in range(j + 1, len(order)):
            cup[j, k] = cap[j, k] = 2
            for i in range(j):
                sign = orient(points[order[i]], points[order[j]],
                              points[order[k]])
                assert sign != 0
                triple_checks += 1
                if sign > 0:
                    cup[j, k] = max(cup[j, k], cup.get((i, j), 2) + 1)
                else:
                    cap[j, k] = max(cap[j, k], cap.get((i, j), 2) + 1)
    return max(cup.values()), max(cap.values()), triple_checks


def random_factor(vertices: list[int], forbidden: set[Pair],
                  rng: random.Random) -> list[Pair] | None:
    """Sample a perfect matching in the graph of unused physical pairs."""
    def recurse(unused: set[int], out: list[Pair]):
        if not unused:
            return list(out)
        v = min(unused, key=lambda z: sum(
            tuple(sorted((z, w))) not in forbidden
            for w in unused if w != z
        ))
        candidates = [w for w in unused if w != v
                      and tuple(sorted((v, w))) not in forbidden]
        rng.shuffle(candidates)
        for w in candidates:
            answer = recurse(unused - {v, w}, out + [(v, w)])
            if answer is not None:
                return answer
        return None
    return recurse(set(vertices), [])


def bipartite_perfect_matching(adjacency: list[list[int]],
                               rng: random.Random) -> list[int] | None:
    matched_right: dict[int, int] = {}

    def augment(left: int, seen: set[int]) -> bool:
        candidates = list(adjacency[left])
        rng.shuffle(candidates)
        for right in candidates:
            if right in seen:
                continue
            seen.add(right)
            if (right not in matched_right
                    or augment(matched_right[right], seen)):
                matched_right[right] = left
                return True
        return False

    for left in sorted(range(len(adjacency)),
                       key=lambda z: len(adjacency[z])):
        if not augment(left, set()):
            return None
    out = [-1] * len(adjacency)
    for right, left in matched_right.items():
        out[left] = right
    assert set(out) == set(range(len(adjacency)))
    return out


def class_rounds(n: int) -> list[list[tuple[int, int]]]:
    """The circle one-factorization of the class graph K_n."""
    assert n % 2 == 0
    return [
        [(n - 1, r)]
        + [((r + k) % (n - 1), (r - k) % (n - 1))
           for k in range(1, n // 2)]
        for r in range(n - 1)
    ]


def find_base_reset(points: tuple[Point, ...]):
    """Fixed-seed exact search; every returned circuit is recertified."""
    b, g, max_attempts = 14, 18, 400
    rng = random.Random(112358)
    for global_try in range(10):
        order = list(range(len(points)))
        rng.shuffle(order)
        classes = [order[g * i:g * (i + 1)] for i in range(b)]
        forbidden: list[set[Pair]] = [set() for _ in range(b)]
        solution = {}
        failed = False
        attempts = 0
        for round_pairs in class_rounds(b):
            for raw_i, raw_j in round_pairs:
                i, j = sorted((raw_i, raw_j))
                found = False
                for _attempt in range(max_attempts):
                    attempts += 1
                    pi = random_factor(classes[i], forbidden[i], rng)
                    pj = random_factor(classes[j], forbidden[j], rng)
                    if pi is None or pj is None:
                        break
                    adjacency = [
                        [right for right in range(g // 2)
                         if is_bad_quad(pi[left] + pj[right], points)]
                        for left in range(g // 2)
                    ]
                    matching = bipartite_perfect_matching(adjacency, rng)
                    if matching is None:
                        continue
                    solution[i, j] = (pi, pj, matching)
                    forbidden[i].update(tuple(sorted(pair)) for pair in pi)
                    forbidden[j].update(tuple(sorted(pair)) for pair in pj)
                    found = True
                    break
                if not found:
                    failed = True
                    break
            if failed:
                break
        if not failed:
            return classes, solution, global_try, attempts
    raise AssertionError("fixed-seed perfect-reset search did not terminate")


def certify_base(points: tuple[Point, ...], classes, solution):
    b, g, m = 14, 18, 9
    assert len(points) == b * g == comb(10, 5)
    assert len(solution) == comb(b, 2)
    assert {z for cls in classes for z in cls} == set(range(len(points)))
    pair_degree = Counter()
    label_load = Counter()
    circuit_edges = 0
    factors: dict[tuple[int, int], list[Pair]] = {}

    for i, j in combinations(range(b), 2):
        pi, pj, matching = solution[i, j]
        assert len(pi) == len(pj) == len(matching) == m
        assert {z for pair in pi for z in pair} == set(classes[i])
        assert {z for pair in pj for z in pair} == set(classes[j])
        factors[i, j] = pi
        factors[j, i] = pj
        for left, right in enumerate(matching):
            quad = pi[left] + pj[right]
            assert is_bad_quad(quad, points)
            pair_degree[i, tuple(sorted(pi[left]))] += 1
            pair_degree[j, tuple(sorted(pj[right]))] += 1
            label_load.update(quad)
            circuit_edges += 1

    assert set(pair_degree.values()) == {1}
    assert set(label_load.values()) == {b - 1}
    assert circuit_edges == m * comb(b, 2) == 819
    return factors, {
        "classes": b,
        "class_size": g,
        "matching_size": m,
        "circuit_edges": circuit_edges,
        "label_load": b - 1,
        "pair_node_degree": 1,
        "pair_node_triangles": 0,
    }


def digits(value: int, length: int, base: int) -> tuple[int, ...]:
    out = [0] * length
    for q in range(length - 1, -1, -1):
        out[q] = value % base
        value //= base
    assert value == 0
    return tuple(out)


def encode(word: tuple[int, ...], base: int) -> int:
    out = 0
    for z in word:
        out = base * out + z
    return out


def first_difference(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    return next(q for q in range(len(a)) if a[q] != b[q])


def symbolic_h2_pair_audit(classes, factors) -> dict[str, int]:
    """Exhaust pair-node freshness for one class in the h=2 power."""
    b, g, h = 14, 18, 2
    positions = [{z: q for q, z in enumerate(cls)} for cls in classes]
    central = (0, 0)
    seen = set()
    neighbours = 0
    for neighbour in product(range(b), repeat=h):
        if neighbour == central:
            continue
        ell = first_difference(central, neighbour)
        suffix_length = h - ell - 1
        modulus = g ** suffix_length
        shift = encode(neighbour[ell + 1:], b)
        assert 0 <= shift < b ** suffix_length <= modulus
        base_pairs = factors[central[ell], neighbour[ell]]
        for prefix in product(range(g), repeat=ell):
            for raw_u, raw_v in base_pairs:
                u = positions[central[ell]][raw_u]
                v = positions[central[ell]][raw_v]
                for suffix_index in range(modulus):
                    left = (prefix + (u,)
                            + digits(suffix_index, suffix_length, g))
                    right = (prefix + (v,)
                             + digits((suffix_index + shift) % modulus,
                                      suffix_length, g))
                    pair = tuple(sorted((left, right)))
                    assert pair not in seen
                    seen.add(pair)
        neighbours += 1
    expected = (b ** h - 1) * (g ** h // 2)
    assert len(seen) == expected
    return {
        "power_h": h,
        "neighbours_of_test_class": neighbours,
        "fresh_pair_nodes_at_test_class": len(seen),
        "expected_fresh_pair_nodes": expected,
    }


def asymptotic_and_padding_audit() -> dict[str, object]:
    b, g, rank_base = 14, 18, 10
    rho = log(rank_base) / log(b)
    assert rho < 1
    checks = 0
    for h in range(1, 9):
        t = b ** h
        class_size = g ** h
        matching_size = class_size // 2
        rank_bound = rank_base ** h
        assert 2 * matching_size == class_size
        assert rank_bound < t
        # Ten-percent near-perfect padding, rounded to physical labels.
        padding = ceil(class_size / 10)
        padded_size = class_size + padding
        average_load_numerator = class_size * (t - 1)
        assert average_load_numerator / padded_size <= t - 1
        cell_multiplicity = ceil(padded_size / class_size)
        assert cell_multiplicity == 2
        assert cell_multiplicity * rank_bound < 2 * t
        checks += 1
    return {
        "rho=log_14(10)": rho,
        "exact_power_checks": checks,
        "perfect_rank_ratio_h8": Q(10 ** 8, 14 ** 8),
        "ten_percent_padded_rank_ratio_h8": Q(2 * 10 ** 8, 14 ** 8),
    }


def main() -> None:
    points = cup_cap_set(7, 7)
    assert len(points) == 252
    longest_cup, longest_cap, triple_checks = cup_cap_lengths(points)
    assert (longest_cup, longest_cap) == (6, 6)
    # A convex x-ordered set is its lower cup plus upper cap, sharing the
    # two endpoints, hence rank <= 6+6-2=10.
    convex_rank_upper = longest_cup + longest_cap - 2
    assert convex_rank_upper == 10

    classes, solution, search_try, search_attempts = find_base_reset(points)
    factors, base = certify_base(points, classes, solution)
    symbolic = symbolic_h2_pair_audit(classes, factors)
    asymptotic = asymptotic_and_padding_audit()

    print("PASS")
    print("  ES base: points=252, cup/cap=(6,6), "
          f"convex_rank_upper={convex_rank_upper}, triples={triple_checks}")
    print(f"  perfect reset: {base}")
    print(f"  deterministic search: try={search_try}, attempts={search_attempts}")
    print(f"  lexicographic pair decoder: {symbolic}")
    print(f"  asymptotic/padding: {asymptotic}")


if __name__ == "__main__":
    main()
