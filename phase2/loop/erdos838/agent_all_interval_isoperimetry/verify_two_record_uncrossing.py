#!/usr/bin/env python3
"""Exact checks for TWO_RECORD_UNCROSSING.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import ceil, comb


Point = tuple[Fraction, Fraction]


def cross(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered
    lower: list[Point] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[Point] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def parabola_counterexample() -> None:
    source = [(Fraction(x), Fraction(x * x)) for x in range(-4, 5)]
    blocker = (Fraction(1, 10), Fraction(-3))
    ambient = source + [blocker]
    for a, b, c in combinations(ambient, 3):
        assert cross(a, b, c) != 0
    assert len(hull(source)) == 9
    repaired = set(hull(ambient))
    hidden = [point for point in source if point not in repaired]
    expected = [
        (Fraction(-1), Fraction(1)),
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(1)),
    ]
    assert hidden == expected
    assert repaired == set(source).difference(expected).union({blocker})
    assert len(hull(hidden + [blocker])) == 3 < 4
    assert (Fraction(0), Fraction(0)) not in hull(hidden + [blocker])
    print("exact parabola blocker+ear counterexample: PASS")


def insertion_poset_audit() -> None:
    base = [
        (Fraction(-2), Fraction(-1)),
        (Fraction(2), Fraction(-1)),
        (Fraction(2), Fraction(1)),
        (Fraction(-2), Fraction(1)),
    ]
    top = [
        (Fraction(-1, 2), Fraction(2)),
        (Fraction(1, 2), Fraction(2)),
        (Fraction(0), Fraction(3)),
    ]
    bottom = [
        (Fraction(-1, 2), Fraction(-2)),
        (Fraction(1, 2), Fraction(-2)),
    ]
    assert all(len(hull(base + [point])) == len(base) + 1 for point in top + bottom)

    # The first two top points are incomparable and both lie below the
    # third hull in the containment order.
    assert len(hull(base + [top[2], top[0]])) == len(base) + 1
    assert len(hull(base + [top[2], top[1]])) == len(base) + 1
    assert len(hull(base + top[:2])) == len(base) + 2
    assert len(hull(base + [top[0], top[2]])) == len(base) + 1
    assert len(hull(base + [top[1], top[2]])) == len(base) + 1
    # Antichain choices at the nonadjacent top and bottom edges coexist.
    combined = base + top[:2] + bottom
    assert len(hull(combined)) == len(combined)
    print("endpoint insertion poset and nonadjacent antichains: PASS")


def adjacent_deletion_counterexample() -> None:
    base = [
        (Fraction(-821887), Fraction(-595397)),
        (Fraction(-738882), Fraction(-762305)),
        (Fraction(365937), Fraction(-1123009)),
        (Fraction(1057493), Fraction(-478100)),
        (Fraction(1071435), Fraction(-332802)),
        (Fraction(1105222), Fraction(54013)),
        (Fraction(267072), Fraction(1065040)),
    ]
    left = [
        (Fraction(913819), Fraction(1914436)),
        (Fraction(1117441), Fraction(1400409)),
    ]
    right = [
        (Fraction(-2318987), Fraction(3222280)),
        (Fraction(-1770368), Fraction(2922150)),
    ]
    ambient = base + left + right
    for a, b, c in combinations(ambient, 3):
        assert cross(a, b, c) != 0
    assert len(hull(base)) == len(base)
    assert len(hull(base + left)) == len(base) + len(left)
    assert len(hull(base + right)) == len(base) + len(right)
    combined = base[:-1] + left + right
    assert len(hull(combined)) == len(combined) - 1
    assert right[1] not in hull(combined)
    print("adjacent-edge common-guard deletion counterexample: PASS")


def subsets_at_most_two(q: int) -> list[tuple[int, ...]]:
    return [item for size in range(3) for item in combinations(range(q), size)]


def balanced_code(q1: int, qb: int, y: int) -> int:
    domain = [(a, b, p, z) for a in range(q1) for b in range(qb) for p in range(y) for z in range(y)]
    codomain = [(left, right) for left in subsets_at_most_two(q1) for right in subsets_at_most_two(qb)]
    loads = Counter(codomain[index % len(codomain)] for index in range(len(domain)))
    maximum = max(loads.values())
    expected = ceil(len(domain) / len(codomain))
    assert maximum == expected
    return maximum


def product_count(core: int, blocks: tuple[int, ...], blockers: int) -> None:
    assert len(blocks) >= 2
    q1, qb = blocks[0], blocks[-1]
    middle = 1
    product = 1
    for value in blocks:
        product *= value
    for value in blocks[1:-1]:
        middle *= value
    s1 = sum(comb(q1, j) for j in range(3))
    sb = sum(comb(qb, j) for j in range(3))
    records = core * product * blockers
    sources = core * product
    two_ended = core * s1 * middle * sb
    fibre = ceil(q1 * qb * blockers * blockers / (s1 * sb))
    assert records * records <= fibre * sources * two_ended
    if q1 * qb * blockers * blockers <= 200_000:
        assert balanced_code(q1, qb, blockers) == fibre
    print(
        f"product core={core} blocks={blocks} y={blockers} "
        f"K={fibre} records^2/(A*D)={records*records/(sources*two_ended):.6f} PASS"
    )


def symmetric_product_count(
    core: int, blocks: tuple[int, ...], blockers: int, left: int, right: int
) -> None:
    product = 1
    for value in blocks:
        product *= value
    q_left, q_right = blocks[left], blocks[right]
    s_left = sum(comb(q_left, size) for size in range(3))
    s_right = sum(comb(q_right, size) for size in range(3))
    records = core * product * blockers
    face_left = core * (product // q_left) * s_left
    face_right = core * (product // q_right) * s_right
    fibre = ceil(q_left * q_right * blockers * blockers / (s_left * s_right))
    assert records * records <= fibre * face_left * face_right
    assert balanced_code(q_left, q_right, blockers) == fibre
    print(
        f"symmetric slots=({left},{right}) q=({q_left},{q_right}) "
        f"y={blockers} K={fibre} PASS"
    )


def hierarchy_audit() -> None:
    # Exact H1 example: linearly many low-coordinate resets are compatible
    # with only a linear-scale density increase.
    rank = 100
    rho = Fraction(rank)
    coordinate_entropy = Fraction(89)
    initial_log_mass = rho * (rank + 1)
    branch_loss = Fraction(0)
    for current_rank in range(rank, rank // 2, -1):
        assert coordinate_entropy < rho
        branch_loss += coordinate_entropy
        rho = (rho * (current_rank + 1) - coordinate_entropy) / current_rank
    assert rho < 2 * rank
    assert branch_loss > rank * rank / 3
    assert initial_log_mass == rank * (rank + 1)

    # Marked-downclosure Kraft audit.  Rotation targets are sliding rank-k
    # windows; every step has a fresh mark.  A marked face can be charged by
    # at most its number of labels, even though old marks persist for many
    # steps.
    ell = 20
    k = 12
    steps = 24
    targets: list[frozenset[int]] = []
    marks: list[int] = []
    for index in range(steps):
        target = frozenset(range(index, index + k))
        targets.append(target)
        marks.append(index + k - 1)
    loads: Counter[frozenset[int]] = Counter()
    for target, mark in zip(targets, marks):
        others = sorted(target.difference({mark}))
        for mask in range(1 << len(others)):
            face = frozenset(
                [mark] + [value for bit, value in enumerate(others) if mask >> bit & 1]
            )
            loads[face] += 1
    mu = max(loads.values())
    union_size = len(loads)
    cap = 1 << (ell - k)
    assert k >= ceil(ell / 2)
    assert mu <= k
    assert steps * (1 << (k - 1)) <= mu * union_size
    assert steps * cap <= 2 * mu * union_size
    print(
        f"hierarchy reset and marked Kraft: levels={rank//2} "
        f"final_density={float(rho):.6f} mu={mu} PASS"
    )


def guarded_shadow_and_coefficient_audit() -> None:
    # Abstract guarded histories: the first and last base labels are the
    # insertion-edge guards and may not be deleted.  Check the exact
    # incidence/right-degree inequality behind H10.
    k, t = 7, 2
    histories = [
        (0, tuple(range(0, 7))),
        (0, tuple(range(0, 6)) + (7,)),
        (1, tuple(range(1, 8))),
        (1, tuple(range(1, 7)) + (8,)),
    ]
    output_loads: Counter[tuple[int, frozenset[int]]] = Counter()
    for mark, base in histories:
        guards = {base[0], base[-1]}
        deletable = sorted(set(base).difference(guards))
        for deleted in combinations(deletable, t):
            prefix = frozenset(set(base).difference(deleted))
            output_loads[(mark, prefix)] += 1
    left_degree = comb(k - 2, t)
    total_incidences = len(histories) * left_degree
    assert total_incidences == sum(output_loads.values())
    marked_lambda = max(output_loads.values())
    assert len(output_loads) * marked_lambda >= total_incidences

    # H13 and H17: adjacent root transcripts are only 3^r, and the
    # first-heavy cross-prefix fibre is subquadratic in the rank exponent.
    for boundary_rank in (4, 8, 16):
        assert sum((2**steps) * comb(boundary_rank, steps) for steps in range(boundary_rank + 1)) == 3**boundary_rank
    ratios = []
    for rank in (100, 400, 1600):
        omitted = ceil(rank**0.5)
        exponent = (2 * omitted + 2) * rank
        ratios.append(exponent / (rank * rank))
    assert ratios[0] > ratios[1] > ratios[2]
    print(
        f"guarded shadow and coefficient reuse: degree={left_degree} "
        f"Lambda={marked_lambda} ratios={ratios} PASS"
    )


if __name__ == "__main__":
    parabola_counterexample()
    insertion_poset_audit()
    adjacent_deletion_counterexample()
    product_count(17, (3, 5), 4)
    product_count(11, (4, 3, 6), 5)
    product_count(7, (8, 5, 4, 9), 12)
    for size in (2, 3, 4, 8, 16, 32):
        product_count(13, (size, 3, size), size)
        symmetric_product_count(13, (size, 3, size), size, 0, 2)
        symmetric_product_count(13, (3, size, 5), size, 1, 1)
    hierarchy_audit()
    guarded_shadow_and_coefficient_audit()
