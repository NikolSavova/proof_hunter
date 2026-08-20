#!/usr/bin/env python3
"""Verify shared-head/tail double closure for amplified #1208 channels."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_high_codegree_replacement_completion import add, subtract, tables
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def profile(points: list[Point]) -> Profile:
    edge_at_sum, _, anchor = tables(points)
    fibres = clean_start_fibres(points)
    fibre_sets = {q: set(starts) for q, starts in fibres.items()}
    by_head: dict[int, list[Point]] = defaultdict(list)
    by_tail: dict[int, list[Point]] = defaultdict(list)
    for q in fibres:
        head, tail = anchor[q]
        by_head[head].append(q)
        by_tail[tail].append(q)

    head_intersections = head_exceptions = 0
    tail_intersections = tail_clean = tail_boundary = 0
    maximum_pair_exception_union = 0

    for translations in by_head.values():
        for q_one in translations:
            head, _ = anchor[q_one]
            exceptions_at_start: dict[Point, set[Point]] = {}
            for start in fibres[q_one]:
                exceptional_q: set[Point] = set()
                for q_zero in translations:
                    if q_zero == q_one or start not in fibre_sets[q_zero]:
                        continue
                    difference = subtract(q_one, q_zero)
                    shifted = add(start, q_zero)
                    head_intersections += 1
                    if shifted not in fibre_sets.get(difference, set()):
                        exceptional_q.add(q_zero)
                        head_exceptions += 1
                        _, tail_one = anchor[q_one]
                        _, tail_zero = anchor[q_zero]
                        first = set(edge_at_sum[shifted])
                        second = set(edge_at_sum[add(start, q_one)])
                        assert tail_one in first
                        assert tail_zero in second
                        assert len(first & second) == 1
                # The two target endpoints of the q_one row give exactly
                # the two exceptional same-head translations.
                assert len(exceptional_q) == 2
                exceptions_at_start[start] = exceptional_q
            # A common source pair deletes the union of its two individual
            # exceptional translation sets, of size at most four.
            for first, second in combinations(fibres[q_one], 2):
                union = exceptions_at_start[first] | exceptions_at_start[second]
                maximum_pair_exception_union = max(
                    maximum_pair_exception_union, len(union)
                )
                assert len(union) <= 4

    boundary_witness: tuple[Point, Point, Point] | None = None
    for translations in by_tail.values():
        for q_one, q_zero in combinations(translations, 2):
            difference = subtract(q_one, q_zero)
            for start in fibre_sets[q_one] & fibre_sets[q_zero]:
                tail_intersections += 1
                shifted = add(start, q_zero)
                target = add(start, q_one)
                first_edge = set(edge_at_sum[shifted])
                second_edge = set(edge_at_sum[target])
                assert not (first_edge & second_edge)
                if shifted in fibre_sets.get(difference, set()):
                    tail_clean += 1
                else:
                    tail_boundary += 1
                    boundary_witness = boundary_witness or (q_one, q_zero, start)
                    head, tail = anchor[difference]
                    assert head in first_edge or tail in second_edge

    assert head_exceptions == 2 * sum(map(len, fibres.values()))
    assert tail_clean + tail_boundary == tail_intersections
    return (
        len(points),
        sum(map(len, fibres.values())),
        head_intersections,
        head_exceptions,
        tail_intersections,
        tail_boundary,
        maximum_pair_exception_union,
    )


def main() -> None:
    families = [
        ("closure-16", POINTS[:16]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-19", transformed_parabola_43()[:19]),
        ("ruler-40", ruler_points()),
    ]
    profiles = {name: profile(points) for name, points in families}
    for name, result in profiles.items():
        print(name, result)
    assert profiles["closure-16"][5] > 0
    print("amplified shared-anchor channel closure: PASS")


if __name__ == "__main__":
    main()
