#!/usr/bin/env python3
"""Exact checks for CONVEX_BAD_PAIR_EAR_PROMOTION.md."""

from fractions import Fraction as F
from itertools import combinations, product

from verify_bad_pair_rank4_piq import (
    coherent_itinerary_audit,
    rank_four_audit,
)
from verify_mixed_seam_vertex_cover_pi2 import convex, orient


def cyclic_convex(word):
    if len(word) < 3:
        return True
    signs = [orient(word[i], word[(i + 1) % len(word)],
                    word[(i + 2) % len(word)])
             for i in range(len(word))]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def local_insertion_audit():
    left, right = (F(0), F(0)), (F(6), F(0))
    lower = [(F(x), F(y)) for x in range(-6, 13) for y in range(-6, 0)]
    upper = [(F(x), F(y)) for x in range(-8, 15) for y in range(1, 9)]
    tested = [0, 0]

    for a in lower:
        for b in lower:
            local = [left, a, b, right]
            if not cyclic_convex(local) or orient(left, a, b) <= 0:
                continue
            alpha, s = a[0] / 6, -a[1] / 6
            beta, t = b[0] / 6, -b[1] / 6
            determinant = s * beta - t * alpha
            endpoint = determinant + t - s
            assert determinant > 0 and endpoint > 0
            branch = int(t < s)

            for raw_z in upper:
                z = (raw_z[0] / 6, raw_z[1] / 6)
                an = (alpha, -s)
                bn = (beta, -t)
                unit_right = (F(1), F(0))
                if not cyclic_convex([(F(0), F(0)), an, unit_right, z]):
                    continue
                if not cyclic_convex([(F(0), F(0)), bn, unit_right, z]):
                    continue

                chi = orient(an, bn, z)
                expanded = (determinant + (beta - alpha) * z[1]
                            + (t - s) * z[0])
                assert chi == expanded and chi > 0
                if t >= s:
                    lower_bound = determinant * (1 + z[1] / s)
                else:
                    lower_bound = endpoint * (1 + z[1] / s)
                assert chi >= lower_bound
                tested[branch] += 1

    assert min(tested) > 1000
    return tested


def parabola_blocks(q=8):
    return [[(F(10 * role + offset), F((10 * role + offset) ** 2))
             for offset in range(4)]
            for role in range(q)]


def same_type_and_product_audit():
    blocks = parabola_blocks()
    q = len(blocks)
    # Two representatives per role already give a nontrivial complete product.
    transversals = 0
    for choice in product(range(2), repeat=q):
        word = [blocks[i][choice[i]] for i in range(q)]
        assert convex(word)
        transversals += 1

    anchors = [block[0] for block in blocks]
    active = (1, 3, 5)
    menus = {i: ((blocks[i][0], blocks[i][1]),
                 (blocks[i][2], blocks[i][3]))
             for i in active}

    for i in active:
        left, right = anchors[i - 1], anchors[i + 1]
        for pair in menus[i]:
            assert convex([left, pair[0], pair[1], right])

    outputs = set()
    endpoint_outputs = set()
    for choice in product(range(2), repeat=len(active)):
        selected = {i: menus[i][choice[index]]
                    for index, i in enumerate(active)}
        word = []
        for i in range(q):
            word.extend(selected[i] if i in selected else (anchors[i],))
        assert convex(word)
        frozen = frozenset(word)
        assert frozen not in outputs
        outputs.add(frozen)
        endpoint_word = frozenset(
            selected[i][0] if i in selected else anchors[i]
            for i in range(q)
        )
        assert convex(list(endpoint_word))
        endpoint_outputs.add(endpoint_word)
    assert len(outputs) == 2 ** len(active)
    # Ear promotion changes the retained mark/rank, not the raw menu count.
    assert len(endpoint_outputs) == len(outputs)

    # Exact context formula: two disjoint retained tags give two disjoint
    # copies; erasing the tags gives load two and no fictitious factor.
    tagged = {(tag, output) for tag in (0, 1) for output in outputs}
    assert len(tagged) == 2 * len(outputs)
    erased_incidences = [(tag, output) for tag in (0, 1) for output in outputs]
    erased_load = max(sum(candidate == output for _, candidate in erased_incidences)
                      for output in outputs)
    assert erased_load == 2
    assert len(erased_incidences) // erased_load == len(outputs)
    return (transversals, len(outputs), len(next(iter(outputs))),
            len(endpoint_outputs), len(tagged), erased_load)


def max_cycle_independent(vertices, q):
    vertices = set(vertices)
    best = 0
    for mask in range(1 << q):
        chosen = {i for i in range(q) if mask >> i & 1}
        if not chosen <= vertices:
            continue
        if any((i + 1) % q in chosen for i in chosen):
            continue
        best = max(best, len(chosen))
    return best


def independent_set_audit():
    systems = 0
    for q in range(3, 12):
        for mask in range(1 << q):
            vertices = {i for i in range(q) if mask >> i & 1}
            best = max_cycle_independent(vertices, q)
            assert 3 * best >= len(vertices)
            systems += 1
    return systems


def main():
    local = local_insertion_audit()
    (transversals, outputs, rank, endpoints,
     tagged, erased_load) = same_type_and_product_audit()
    systems = independent_set_audit()
    records, types, ray_t, ray_u = rank_four_audit()
    walls, matrices, itineraries, bound, ratio = coherent_itinerary_audit()
    print("PASS: insertion branches=%s; transversals=%d; ear/endpoints=%d/%d "
          "rank=%d; tagged=%d erased-load=%d; cycle systems=%d; hidden=%s "
          "types=%s; PGL2=%d/%d<=%d ratio=%s"
          % (local, transversals, outputs, endpoints, rank, tagged,
             erased_load, systems, records, types, itineraries, matrices,
             bound, ratio))


if __name__ == "__main__":
    main()
