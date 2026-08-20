#!/usr/bin/env python3
"""Verify the fifteen-channel third-translation dichotomy."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_high_codegree_replacement_completion import add, tables


Point = tuple[int, int]


def channel_profile(
    translations: list[Point],
    anchor: dict[Point, tuple[int, int]],
    first_edges: dict[Point, set[int]],
    second_edges: dict[Point, set[int]],
    q: Point,
    q_prime: Point,
    first_good: bool,
) -> tuple[int, int, int]:
    k = 1 + max(
        endpoint
        for edge in [*anchor.values(), *first_edges.values(), *second_edges.values()]
        for endpoint in edge
    )
    good_edges = first_edges if first_good else second_edges
    bad_edges = second_edges if first_good else first_edges
    good_union = good_edges[q] | good_edges[q_prime]
    bad_union = bad_edges[q] | bad_edges[q_prime]
    assert len(good_union) == 3
    assert len(bad_union) == 4

    q_head, q_tail = anchor[q]
    q_prime_head, q_prime_tail = anchor[q_prime]
    base_heads = (q_head, q_prime_head)
    base_tails = (q_tail, q_prime_tail)
    base_anchor_union = set(base_heads + base_tails)
    local = transverse = 0
    channels: Counter[tuple[str, int]] = Counter()
    for q_zero in translations:
        head, tail = anchor[q_zero]
        is_local = False
        for endpoint in base_heads:
            if head == endpoint:
                channels["shared-head", endpoint] += 1
                is_local = True
            if tail == endpoint:
                channels["cross-tail-head", endpoint] += 1
                is_local = True
        for endpoint in base_tails:
            if tail == endpoint:
                channels["shared-tail", endpoint] += 1
                is_local = True
            if head == endpoint:
                channels["cross-head-tail", endpoint] += 1
                is_local = True
        for endpoint in good_union:
            if endpoint in good_edges[q_zero]:
                channels["good-target", endpoint] += 1
                is_local = True
        for endpoint in bad_union:
            if endpoint in bad_edges[q_zero]:
                channels["bad-target", endpoint] += 1
                is_local = True

        direct_local = bool(set(anchor[q_zero]) & base_anchor_union) or bool(
            good_edges[q_zero] & good_union
        ) or bool(bad_edges[q_zero] & bad_union)
        assert direct_local == is_local
        local += is_local
        transverse += not is_local

    maximum_channel = max(channels.values(), default=0)
    M = len(translations)
    assert local + transverse == M
    assert local <= 15 * k - 36
    assert transverse * 2 >= M or maximum_channel * 30 >= M
    if M >= 30 * k:
        assert transverse * 2 >= M
    return local, transverse, maximum_channel


def abstract_checks() -> None:
    # A directed cycle at the literal edge/vertex threshold stresses the
    # cross-orientation anchor channels.  Target role zero is a star and
    # role one is a cycle, so every selected base pair is one-role.
    k = 12
    translations = [(index, 0) for index in range(k)]
    anchor = {
        q: (index, (index + 1) % k)
        for index, q in enumerate(translations)
    }
    all_edges = [set(edge) for edge in combinations(range(k), 2)]

    def edge_map(special: dict[int, set[int]]) -> dict[Point, set[int]]:
        used = {tuple(sorted(edge)) for edge in special.values()}
        remaining = [edge for edge in all_edges if tuple(sorted(edge)) not in used]
        output: dict[Point, set[int]] = {}
        for index, q in enumerate(translations):
            output[q] = special[index] if index in special else remaining.pop(0)
        assert len({tuple(sorted(edge)) for edge in output.values()}) == k
        return output

    first_edges = edge_map({1: {0, 1}, 5: {0, 2}})
    second_edges = edge_map({1: {3, 4}, 5: {5, 6}})
    # Use a pair whose second-role cycle edges are disjoint.
    result = channel_profile(
        translations,
        anchor,
        first_edges,
        second_edges,
        translations[1],
        translations[5],
        True,
    )
    assert result[0] + result[1] == k


def parabola_profile(limit: int = 24) -> tuple[int, ...]:
    points = transformed_parabola_43()
    k = len(points)
    edge_at_sum, label, anchor = tables(points)
    target_gaps = {
        first - second
        for first in label.values()
        for second in label.values()
    }
    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for q, starts in clean_start_fibres(points).items():
        for first in starts:
            for second in starts:
                if first == second:
                    continue
                gap = label[first] - label[second]
                if gap % 18 == 0 and -gap // 18 in target_gaps:
                    common[first, second].append(q)

    base_records = transverse_rich = local_rich = 0
    minimum_rich_channel = k
    replacement_direct = replacement_amplified = replacement_split = 0
    tested_pairs = 0
    for (first, second), translations in common.items():
        if second < first or len(translations) < k:
            continue
        tested_pairs += 1
        first_edges = {
            q: set(edge_at_sum[add(first, q)]) for q in translations
        }
        second_edges = {
            q: set(edge_at_sum[add(second, q)]) for q in translations
        }
        replacements = [
            q for q in translations if first_edges[q] & second_edges[q]
        ]
        rho = len(replacements)
        M = len(translations)
        replacement_direct += rho
        replacement_amplified += rho * M
        replacement_split += rho * rho + rho * (M - rho)
        assert rho * M == rho * rho + rho * (M - rho)

        for q, q_prime in combinations(sorted(translations), 2):
            first_good = bool(first_edges[q] & first_edges[q_prime])
            second_good = bool(second_edges[q] & second_edges[q_prime])
            if first_good == second_good:
                continue
            local, transverse, maximum_channel = channel_profile(
                translations,
                anchor,
                first_edges,
                second_edges,
                q,
                q_prime,
                first_good,
            )
            base_records += 1
            if transverse * 2 >= M:
                transverse_rich += 1
                assert k <= 2 * transverse
            else:
                local_rich += 1
                minimum_rich_channel = min(minimum_rich_channel, maximum_channel)
                assert k <= 30 * maximum_channel
        if tested_pairs >= limit:
            break

    assert tested_pairs == limit
    assert replacement_amplified == replacement_split
    assert k * replacement_direct <= replacement_amplified
    assert base_records == transverse_rich + local_rich
    return (
        tested_pairs,
        base_records,
        transverse_rich,
        local_rich,
        minimum_rich_channel,
        replacement_direct,
        replacement_amplified,
    )


def main() -> None:
    abstract_checks()
    result = parabola_profile()
    print("parabola-43 high aligned sample", result)
    print("amplified third-translation local/transverse dichotomy: PASS")


if __name__ == "__main__":
    main()
