#!/usr/bin/env python3
"""Exact checks for the size-biased eight-corner gate and boundary barrier."""

from __future__ import annotations

from collections import Counter

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import POINTS
from verify_transverse_eight_corner_gate import relation_corner_keys


Point = tuple[int, int]
RolePair = tuple[int, int]
Relation = tuple[RolePair, RolePair, RolePair]


EXPECTED = {
    30: (26_428, 5, 41_696),
    45: (107_720, 6, 191_272),
    60: (259_516, 8, 477_864),
    90: (1_009_116, 9, 2_018_332),
    120: (2_798_384, 12, 6_182_704),
}


INTERNAL_POINTS: list[Point] = [
    (-3384850, -177817),
    (6289502, -2263621),
    (-2746346, -4185887),
    (6551974, 3570361),
    (9413619, -630852),
    (-428433, -1006884),
    (2667312, 14619144),
    (-5643234, -5154018),
    (6126636, -5463210),
    (2205960, -1106490),
    (-3211086, -3360744),
    (4404780, 96360),
    (-1092186, -2489790),
    (5891610, 1924284),
    (5742870, -35220),
    (-25944, 440724),
    (5900448, -3775536),
    (5091552, -757434),
    (3823926, 3128556),
    (-1908894, 5300916),
    (-5511000, -1410732),
    (4172634, 856794),
]


BASE: Relation = ((0, 1), (2, 3), (4, 5))
COMPLETIONS: dict[int, tuple[Relation, Relation]] = {
    0: (
        ((0, 3), (2, 6), (4, 7)),
        ((0, 8), (2, 1), (4, 9)),
    ),
    3: (
        ((2, 1), (10, 3), (4, 11)),
        ((12, 1), (0, 3), (4, 13)),
    ),
    4: (
        ((0, 3), (2, 14), (15, 5)),
        ((0, 16), (2, 1), (17, 5)),
    ),
    7: (
        ((2, 1), (18, 3), (19, 5)),
        ((20, 1), (0, 3), (21, 5)),
    ),
}


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def rotate(value: Point) -> Point:
    return -value[1], value[0]


def relation_vectors(points: list[Point], relation: Relation) -> tuple[Point, Point, Point]:
    return tuple(
        subtract(points[first], points[second]) for first, second in relation
    )  # type: ignore[return-value]


def is_relation(points: list[Point], relation: Relation) -> bool:
    d, f, e = relation_vectors(points, relation)
    return d == add(f, rotate(e))


def is_transverse(points: list[Point], relation: Relation) -> bool:
    d, _, e = relation_vectors(points, relation)
    return e != (0, 0) and d[0] * e[0] + d[1] * e[1] != 0


def corner_data(relation: Relation, mask: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    bits = tuple((mask >> role) & 1 for role in range(3))
    selected = tuple(relation[role][bits[role]] for role in range(3))
    complement = tuple(relation[role][1 - bits[role]] for role in range(3))
    return selected, complement


def normalized_edge(points: list[Point], complement: tuple[int, ...], mask: int) -> tuple[Point, Point]:
    signs = tuple(2 * ((mask >> role) & 1) - 1 for role in range(3))
    q0 = points[complement[1]]
    r0 = points[complement[0]]
    q = signs[1] * q0[0], signs[1] * q0[1]
    r = signs[0] * r0[0], signs[0] * r0[1]
    return q, r


def verify_internal_barrier() -> None:
    assert len(INTERNAL_POINTS) == 22
    assert is_distance_sidon(INTERNAL_POINTS)
    assert is_relation(INTERNAL_POINTS, BASE)
    assert is_transverse(INTERNAL_POINTS, BASE)

    known = [BASE]
    for pair in COMPLETIONS.values():
        known.extend(pair)
    assert all(is_relation(INTERNAL_POINTS, relation) for relation in known)
    assert all(is_transverse(INTERNAL_POINTS, relation) for relation in known)

    for mask in (0, 3, 4, 7):
        base_key, base_complement = corner_data(BASE, mask)
        fibre = []
        for relation in known:
            key, complement = corner_data(relation, mask)
            if key == base_key:
                fibre.append(complement)

        assert len(fibre) == 3
        edges = [normalized_edge(INTERNAL_POINTS, complement, mask) for complement in fibre]
        tails = {tail for tail, _ in edges}
        heads = {head for _, head in edges}
        base_edge = normalized_edge(INTERNAL_POINTS, base_complement, mask)
        assert base_edge[0] in heads
        assert base_edge[1] in tails
        print("internal corner", mask, "fibre", len(fibre), "edge", base_edge)


def profile(points: list[Point]) -> tuple[int, int, int]:
    relations = relation_corner_keys(points)
    degrees = [Counter(keys[mask] for keys in relations) for mask in range(8)]
    adaptive = [
        min(degrees[mask][keys[mask]] for mask in range(8)) for keys in relations
    ]

    # Exact layer-cake identity C=sum_t |R_(>=t)|.
    layer_cake = sum(
        sum(value >= threshold for value in adaptive)
        for threshold in range(1, max(adaptive, default=0) + 1)
    )
    assert layer_cake == sum(adaptive)
    return len(relations), max(adaptive, default=0), sum(adaptive)


def verify_profiles() -> None:
    for size, expected in EXPECTED.items():
        actual = profile(list(POINTS[:size]))
        assert actual == expected, (size, actual, expected)
        relations, maximum, total = actual
        print(
            "size-biased corner",
            size,
            relations,
            maximum,
            total,
            total / size**3,
            total / relations,
        )


def main() -> None:
    verify_internal_barrier()
    verify_profiles()
    print("size-biased eight-corner gate: PASS")


if __name__ == "__main__":
    main()
