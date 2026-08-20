#!/usr/bin/env python3
"""Verify dyadic reversibility and the indexed-graph quartic extremizer."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import ceil, comb


def finite_binomial_checks() -> None:
    # Pointwise inequalities used in (2.2)--(2.5).
    for codegree in range(4, 801):
        minimum_transverse = ceil(codegree / 2)
        assert 16 * comb(minimum_transverse, 2) >= codegree**2
        assert 2 * comb(codegree, 2) < codegree**2

    for K in range(4, 401):
        for codegree in range(K, 2 * K):
            minimum_transverse = ceil(codegree / 2)
            assert 16 * comb(minimum_transverse, 2) >= K**2
            assert comb(codegree, 2) < 2 * K**2

    # The determinant-cell estimate (3.5), with the subpolynomial cell
    # multiplicity factored out.
    for k in range(4, 121):
        for K in range(k, 4 * k + 1):
            for codegree in (K, 2 * K - 1):
                rich_base_upper = 2 * (k - 2) * codegree
                B_upper = comb(codegree, 2) * rich_base_upper
                assert B_upper < 8 * k * K**3


def graph_extremizer(M: int = 128) -> tuple[int, ...]:
    assert M >= 128
    k = M + 3
    translations = [(colour, index) for colour in range(3) for index in range(M)]
    codegree = len(translations)

    def leaf(index: int) -> int:
        return 3 + index % M

    def good(translation: tuple[int, int]) -> frozenset[int]:
        colour, index = translation
        return frozenset((colour, leaf(index)))

    def bad(translation: tuple[int, int]) -> frozenset[int]:
        colour, index = translation
        return frozenset((leaf(index), leaf(index + colour + 1)))

    def anchor(translation: tuple[int, int]) -> tuple[int, int]:
        colour, index = translation
        return leaf(index), leaf(index + colour + 4)

    good_edges = {translation: good(translation) for translation in translations}
    bad_edges = {translation: bad(translation) for translation in translations}
    anchors = {translation: anchor(translation) for translation in translations}

    assert len(set(good_edges.values())) == codegree
    assert len(set(bad_edges.values())) == codegree
    assert len(set(anchors.values())) == codegree
    assert all(len(edge) == 2 for edge in good_edges.values())
    assert all(len(edge) == 2 for edge in bad_edges.values())
    assert all(head != tail for head, tail in anchors.values())

    selected_bases: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for colour in range(3):
        colour_translations = [(colour, index) for index in range(M)]
        for left, right in combinations(colour_translations, 2):
            assert good_edges[left] & good_edges[right] == {colour}
            if bad_edges[left].isdisjoint(bad_edges[right]):
                selected_bases.append((left, right))

    expected_bases = 3 * (comb(M, 2) - M)
    assert len(selected_bases) == expected_bases

    rich_bases = 0
    anchor_disjoint_bases = 0
    B_2 = 0
    minimum_transverse = codegree
    maximum_transverse = 0
    pool_incidence = Counter({translation: 0 for translation in translations})

    for left, right in selected_bases:
        base_anchor_union = set(anchors[left] + anchors[right])
        base_good_union = good_edges[left] | good_edges[right]
        base_bad_union = bad_edges[left] | bad_edges[right]

        transverse = [
            translation
            for translation in translations
            if (
                set(anchors[translation]).isdisjoint(base_anchor_union)
                and good_edges[translation].isdisjoint(base_good_union)
                and bad_edges[translation].isdisjoint(base_bad_union)
            )
        ]
        transverse_count = len(transverse)
        minimum_transverse = min(minimum_transverse, transverse_count)
        maximum_transverse = max(maximum_transverse, transverse_count)
        assert transverse_count >= 2 * M - 52
        assert 2 * transverse_count >= codegree
        rich_bases += 1
        B_2 += comb(transverse_count, 2)
        for translation in transverse:
            pool_incidence[translation] += transverse_count - 1

        if set(anchors[left]).isdisjoint(anchors[right]):
            anchor_disjoint_bases += 1

    assert rich_bases == expected_bases
    assert 100 * anchor_disjoint_bases > 98 * rich_bases
    assert sum(pool_incidence.values()) == 2 * B_2
    assert min(pool_incidence.values()) > M**3 // 2
    assert max(pool_incidence.values()) < 8 * M**3

    lower_B = expected_bases * comb(2 * M - 52, 2)
    assert B_2 >= lower_B
    assert B_2 > k**4
    assert B_2 < 8 * k**4

    # Literal instance of (1.3), taking K=c for the one occupied band.
    K = codegree
    assert K >= k
    assert K**2 * rich_bases <= 16 * B_2
    assert B_2 < 2 * K**2 * rich_bases

    return (
        M,
        k,
        codegree,
        rich_bases,
        anchor_disjoint_bases,
        minimum_transverse,
        maximum_transverse,
        B_2,
        min(pool_incidence.values()),
        max(pool_incidence.values()),
    )


def main() -> None:
    finite_binomial_checks()
    profile = graph_extremizer()
    print("PASS", {"graph_profile": profile})


if __name__ == "__main__":
    main()
