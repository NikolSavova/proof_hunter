#!/usr/bin/env python3
"""Exact checks for WEIGHTED_SIDE_DELETION_PROFILE_DESCENT_BARRIER."""

from fractions import Fraction
from itertools import combinations, product
from math import comb, log2

from verify_critical_edge_dispersion_rechart_ledger import (
    configuration,
    convex,
    orient,
)


def one_role_kill_audit():
    left, right, ys, ws, lowers, roots = configuration()
    nonempty_root_subsets = [
        [roots[i] for i in range(len(roots)) if mask >> i & 1]
        for mask in range(1, 1 << len(roots))
    ]

    good_after_y = []
    good_after_w = []
    for subset in nonempty_root_subsets:
        if all(convex([left] + subset + [w, right, lower])
               for w, lower in product(ws, lowers)):
            good_after_y.append(tuple(subset))
        if all(convex([left, y] + subset + [right, lower])
               for y, lower in product(ys, lowers)):
            good_after_w.append(tuple(subset))
    assert {len(subset) for subset in good_after_y} == {1}
    assert {len(subset) for subset in good_after_w} == {1}
    assert len(good_after_y) == len(roots)
    assert len(good_after_w) == len(roots)
    return len(good_after_y), len(good_after_w)


def side_mask_and_pair_line_audit():
    left, right, ys, ws, lowers, roots = configuration()
    roles = [
        ("L", [left]),
        ("Y", ys),
        ("W", ws),
        ("R", [right]),
        ("T", lowers),
    ]
    left_side = {0, 1}
    right_side = {2, 3, 4}
    audited_masks = 0
    for root_pair in combinations(roots, 2):
        # The candidate common infinity line cuts every neighbour pair.
        assert all(orient(root_pair[0], root_pair[1], y)
                   * orient(root_pair[0], root_pair[1], w) < 0
                   for y, w in product(ys, ws))

        for mask in range(1 << len(roles)):
            selected_roles = {i for i in range(len(roles)) if mask >> i & 1}
            choices = [roles[i][1] for i in selected_roles]
            exists = any(convex(list(root_pair) + list(values))
                         for values in (product(*choices) if choices else [()]))
            if not exists:
                continue
            assert selected_roles <= left_side or selected_roles <= right_side
            audited_masks += 1
    assert audited_masks > 20
    return audited_masks


def square_root_and_load_audit():
    checked = 0
    # C*U >= V_Q and arbitrary complete side reservoirs.
    for c, u, r_left, r_right in product(range(1, 12), repeat=4):
        vq = c * u
        h = r_left * r_right
        bank = max(u * r_left, c * r_right)
        assert bank * bank >= vq * h

        # A retained right output forgets exactly the left word and at most
        # r_Q possible marked roots, plus genuine same-(B,z) multiplicity.
        rank, history = 5, 3
        right_load = r_left * rank * history
        left_load = r_right * rank * history
        assert right_load * left_load == h * rank * rank * history * history
        checked += 1
    return checked


def deletion_identity_and_mask_audit():
    rows = []
    for q in range(2, 22, 2):
        masks = list(combinations(range(q), q // 2))
        family = {frozenset(mask) for mask in masks}
        deletion_sum = sum(
            sum(i not in mask for mask in family) for i in range(q)
        )
        assert deletion_sum == len(family) * q // 2
        left_half = frozenset(range(q // 2))
        avoids_left = sum(not (mask & left_half) for mask in family)
        assert avoids_left == 1
        probability = Fraction(avoids_left, len(family))
        assert probability == Fraction(1, comb(q, q // 2))
        rows.append((q, len(family), probability))
    return rows


def coefficient_audit():
    # Quarter carrier plus half child gives only three eighths after the
    # valid square root, whereas the killed H/D splice suggested one half.
    h, child = Fraction(1, 4), Fraction(1, 2)
    valid = (h + child) / 2
    false_splice = h + child / 2
    assert valid == Fraction(3, 8)
    assert false_splice == Fraction(1, 2)
    assert abs(float(valid) - 0.375) < 1e-15
    return valid, false_splice


def main():
    y_good, w_good = one_role_kill_audit()
    masks = side_mask_and_pair_line_audit()
    loads = square_root_and_load_audit()
    rows = deletion_identity_and_mask_audit()
    valid, false_splice = coefficient_audit()
    print(
        "PASS: one-role survivors Y=%d W=%d side-masks=%d load-cases=%d "
        "coefficient=%s killed=%s central-q20=%d/%d"
        % (y_good, w_good, masks, loads, valid, false_splice,
           rows[-1][2].numerator, rows[-1][2].denominator)
    )


if __name__ == "__main__":
    main()
