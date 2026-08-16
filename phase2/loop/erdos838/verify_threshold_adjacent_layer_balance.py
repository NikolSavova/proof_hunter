#!/usr/bin/env python3
"""Exact checks for THRESHOLD_ADJACENT_LAYER_BALANCE_GATE_20260816.md."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from math import comb, floor
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def audit_averaging() -> int:
    checks = 0
    for total in range(12, 41):
        for rank in range(3, min(9, total - 1)):
            for sample in range(rank + 1, total + 1):
                left_multiplicity = comb(total - rank, sample - rank)
                right_multiplicity = comb(
                    total - rank - 1, sample - rank - 1
                )
                assert Fraction(
                    left_multiplicity, right_multiplicity
                ) == Fraction(total - rank, sample - rank)

                # Normalizing v_(j+1)/v_j by the ambient binomial layers
                # cancels N-j exactly and leaves (j+1)/(q-j).
                assert (
                    Fraction(total - rank, sample - rank)
                    * Fraction(rank + 1, total - rank)
                    == Fraction(rank + 1, sample - rank)
                )
                checks += 1
    return checks


def audit_coefficient() -> int:
    checks = 0
    for lambda_numerator in range(0, 10):
        lam = Fraction(lambda_numerator, 10)
        c = 1 + lam
        assert c < 2
        for alpha_numerator in range(1, 10):
            alpha = Fraction(alpha_numerator, 10)
            eta = (1 - c / 2) * (1 - alpha * alpha)
            advertised = (1 - lam) * (1 - alpha * alpha) / 2
            assert eta == advertised > 0
            coefficient = Fraction(1, 4) + eta / 4
            assert coefficient == (
                Fraction(1, 4)
                + (1 - lam) * (1 - alpha * alpha) / 8
            )
            checks += 1
    return checks


def audit_double_chain() -> tuple[int, Fraction, Fraction]:
    density = load(
        "successive_density_for_threshold_balance",
        HERE / "verify_successive_rank_density_gain.py",
    )
    points = density.double_chain(8)
    v4 = density.face_count(points, 4)
    v5 = density.face_count(points, 5)
    assert (v4, v5) == (924, 112)
    normalized = Fraction(5 * v5, 12 * v4)
    assert normalized == Fraction(5, 99) < Fraction(1, 16)

    checks = 1
    maximum_threshold_ratio = Fraction()
    for rank in range(5, 21):
        m = 2 ** (rank - 1)
        v_rank = 2 * comb(m, rank)
        v_next = 2 * comb(m, rank + 1)
        ratio = Fraction(v_rank, v_next)
        assert ratio == Fraction(rank + 1, m - rank)
        assert ratio < 1
        maximum_threshold_ratio = max(maximum_threshold_ratio, ratio)
        checks += 1
    return checks, normalized, maximum_threshold_ratio


def audit_pascal() -> tuple[int, Fraction, Fraction]:
    graded = load(
        "graded_balanced_for_threshold_balance",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )
    checks = 0
    maximum = Fraction()
    last = Fraction()
    for h in (5, 6, 8, 10, 12, 16, 20, 30, 40, 50):
        size, _, _, profile = graded.central_template(h, 2 * h)
        rank = 2 * h - 5
        ratio = Fraction(profile[rank], profile[rank + 1])
        assert ratio < 3

        # The central binomial coefficient has threshold size 2^(j+o(j)).
        assert size <= 2 ** (2 * h - 4)
        assert size * (2 * h - 3) >= 2 ** (2 * h - 4)

        maximum = max(maximum, ratio)
        last = ratio
        checks += 1
    assert last < Fraction(3, 20)
    return checks, maximum, last


def glue_cells(left, right, cutoff: int):
    graded = load(
        "graded_balanced_for_promoted_pascal",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )
    na, ca, ua, va = left
    nb, cb, ub, vb = right
    return (
        na + nb,
        graded.add(graded.optional_point(ca, nb, cutoff), cb, cutoff),
        graded.add(ua, graded.optional_point(ub, na, cutoff), cutoff),
        graded.add(graded.add(va, vb, cutoff), graded.mul(ca, ub, cutoff), cutoff),
    )


def singleton_cell(cutoff: int):
    profile = [0, 1] + [0] * (cutoff - 1)
    return 1, profile[:], profile[:], profile[:]


def promoted_cap_cell(m: int, index: int, cutoff: int):
    """T(m,index) plus one root in a unique promoted maximum cap.

    Follow the right Pascal child until T(index+1,index), which is a
    strict cap, append one point on its cap side, and rebuild the seams.
    """
    graded = load(
        "graded_balanced_for_promoted_pascal_rows",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )
    current = graded.pascal_row(m, cutoff)[index]
    if m == index + 1:
        return glue_cells(current, singleton_cell(cutoff), cutoff)
    left = graded.pascal_row(m - 1, cutoff)[index - 1]
    return glue_cells(left, promoted_cap_cell(m - 1, index, cutoff), cutoff)


def top_cap_recurrence(maximum_m: int) -> list[list[int]]:
    """t(m,i): coefficient of degree i+1 in the cap profile of T(m,i)."""
    rows: list[list[int]] = []
    for m in range(maximum_m + 1):
        graded = load(
            "graded_balanced_for_top_cap_recurrence",
            HERE / "agent_graded_supersat" / "graded_balanced.py",
        )
        row = graded.pascal_row(m, maximum_m + 2)
        rows.append(
            [
                cell[1][i + 1] if i + 1 < len(cell[1]) else 0
                for i, cell in enumerate(row)
            ]
        )
        if m >= 2:
            for i in range(1, m):
                assert rows[m][i] == (
                    comb(m - 1, i) * rows[m - 1][i - 1]
                    + rows[m - 1][i]
                )
    return rows


def audit_promoted_pascal() -> tuple[int, int, Fraction]:
    graded = load(
        "graded_balanced_for_promoted_pascal_audit",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )
    rows = top_cap_recurrence(35)
    checks = 0
    last_ratio = Fraction()
    for h in range(4, 21):
        rank = 2 * h - 4
        cutoff = rank + 1
        split_row = graded.pascal_row(rank - 1, cutoff)
        left = split_row[h - 3]
        right = split_row[h - 2]
        promoted_left = promoted_cap_cell(rank - 1, h - 3, cutoff)
        parent = glue_cells(promoted_left, right, cutoff)

        one_sided = left[1][h - 2]
        assert one_sided == rows[rank - 1][h - 3]
        assert graded.central_template(h, cutoff)[3][rank] == one_sided**2
        assert parent[3][rank + 1] == one_sided
        assert parent[3][rank] >= one_sided**2
        assert parent[0] == comb(rank, rank // 2) + 1

        half_steps = floor((h - 3) / 2)
        if half_steps:
            # The first-summand path in the recurrence has each selected
            # binomial factor at least 2^(h-3-r).
            elementary_lower = 2 ** sum(
                (h - 3) - r for r in range(half_steps)
            )
            assert one_sided >= elementary_lower

        last_ratio = Fraction(parent[3][rank], parent[3][rank + 1])
        checks += 1

    assert rows[5][2] == 46
    assert rows[7][3] == 3421
    return checks, rows[35][16], last_ratio


def audit_promoted_pascal_geometry() -> int:
    sys.path.insert(0, str(HERE / "agent_graded_supersat"))
    graded_trace = load(
        "graded_trace_for_promoted_pascal_geometry",
        HERE / "agent_graded_supersat" / "graded_trace.py",
    )

    def glue_tagged(left, right, epsilon: Fraction):
        return [
            (epsilon * epsilon * x, epsilon * y, root)
            for x, y, root in left
        ] + [
            (1 + epsilon * epsilon * x, 1 + epsilon * y, root)
            for x, y, root in right
        ]

    def pascal_tagged(m: int, index: int, epsilon: Fraction):
        return [
            (x, y, False)
            for x, y in graded_trace.pascal_cell(m, index, epsilon)
        ]

    def promoted_tagged(m: int, index: int, epsilon: Fraction):
        if m == index + 1:
            return glue_tagged(
                pascal_tagged(m, index, epsilon),
                [(Fraction(), Fraction(), True)],
                epsilon,
            )
        return glue_tagged(
            pascal_tagged(m - 1, index - 1, epsilon),
            promoted_tagged(m - 1, index, epsilon),
            epsilon,
        )

    epsilon = Fraction(1, 97)
    expected = {
        4: ((0, 7, 21, 35, 21, 3), (0, 6, 15, 20, 9)),
        5: (
            (0, 21, 210, 1330, 3923, 5324, 2713, 46),
            (0, 20, 190, 1140, 3225, 4260, 2116),
        ),
    }
    for h, (full_expected, old_expected) in expected.items():
        rank = 2 * h - 4
        points = glue_tagged(
            promoted_tagged(rank - 1, h - 3, epsilon),
            pascal_tagged(rank - 1, h - 2, epsilon),
            epsilon,
        )
        full = sorted((x, y) for x, y, _ in points)
        old = sorted((x, y) for x, y, root in points if not root)
        assert graded_trace.graded_profile(full) == full_expected
        assert graded_trace.graded_profile(old) == old_expected
    return len(expected)


def audit_promoted_pascal_leaf_padding() -> tuple[int, Fraction]:
    """Check that a large recursive child repairs every tested cliff leaf.

    This is a finite regression, not a proof of the threshold conjecture.
    The immutable binary trees below retain every physical Pascal leaf, so
    the audit really tries every possible singleton substitution.
    """
    graded = load(
        "graded_balanced_for_promoted_pascal_padding",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )

    class Node:
        __slots__ = ("left", "right", "cell")

        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right
            self.cell = None

    def leaf():
        return Node()

    def pascal_tree(m: int, index: int):
        if index == 0 or index == m:
            return leaf()
        return Node(
            pascal_tree(m - 1, index - 1),
            pascal_tree(m - 1, index),
        )

    def promoted_tree(m: int, index: int):
        if m == index + 1:
            return Node(pascal_tree(m, index), leaf())
        return Node(
            pascal_tree(m - 1, index - 1),
            promoted_tree(m - 1, index),
        )

    def fast_glue(left, right, cutoff: int):
        na, ca, ua, va = left
        nb, cb, ub, vb = right
        return (
            na + nb,
            graded.add(graded.optional_point(ca, nb, cutoff), cb, cutoff),
            graded.add(ua, graded.optional_point(ub, na, cutoff), cutoff),
            graded.add(
                graded.add(va, vb, cutoff),
                graded.mul(ca, ub, cutoff),
                cutoff,
            ),
        )

    def baseline(node, cutoff: int):
        if node.cell is None:
            if node.left is None:
                node.cell = singleton_cell(cutoff)
            else:
                node.cell = fast_glue(
                    baseline(node.left, cutoff),
                    baseline(node.right, cutoff),
                    cutoff,
                )
        return node.cell

    def substitute_each_leaf(node, child, cutoff: int):
        if node.left is None:
            return [child]
        left = baseline(node.left, cutoff)
        right = baseline(node.right, cutoff)
        return [
            fast_glue(row, right, cutoff)
            for row in substitute_each_leaf(node.left, child, cutoff)
        ] + [
            fast_glue(left, row, cutoff)
            for row in substitute_each_leaf(node.right, child, cutoff)
        ]

    checks = 0
    maximum = Fraction()
    for h in range(4, 9):
        rank = 2 * h - 4
        cutoff = rank + 1
        root = Node(
            promoted_tree(rank - 1, h - 3),
            pascal_tree(rank - 1, h - 2),
        )
        assert baseline(root, cutoff)[0] == comb(rank, rank // 2) + 1

        # This child has logarithmic size rank+O(log rank), already on the
        # same 2^(rank+o(rank)) scale but on the oversaturated side of 2^rank.
        child = graded.central_template(h + 4, cutoff)
        assert child[0] > 2**rank
        for row in substitute_each_leaf(root, child, cutoff):
            ratio = Fraction(row[3][rank], row[3][rank + 1])
            assert ratio < 1
            maximum = max(maximum, ratio)
            checks += 1
    return checks, maximum


def audit_alternating_comb() -> tuple[int, Fraction, Fraction]:
    trees = load(
        "uniform_caterpillar_for_threshold_balance",
        HERE / "verify_uniform_growing_rank_caterpillar.py",
    )
    checks = 0
    first = None
    last = None
    previous = None
    for rank in range(4, 11):
        tree = trees.alternating_comb(2**rank)
        profile = trees.ordinary_profiles(tree)[2]
        ratio = Fraction(profile[rank], profile[rank + 1])
        assert ratio < 2
        if previous is not None:
            assert ratio < previous
        first = ratio if first is None else first
        last = ratio
        previous = ratio
        checks += 1
    assert first is not None and last is not None
    return checks, first, last


def audit_abstract_hereditary_barrier() -> int:
    checks = 0
    for rank in range(4, 13):
        size = 2**rank
        current = comb(size, rank)
        following = 1
        assert current // following > 2**rank
        checks += 1
    return checks


def main() -> None:
    averaging = audit_averaging()
    coefficient = audit_coefficient()
    double_checks, double_kill, double_threshold = audit_double_chain()
    pascal_checks, pascal_maximum, pascal_last = audit_pascal()
    promoted_checks, promoted_last_cap, promoted_last_ratio = audit_promoted_pascal()
    promoted_geometry = audit_promoted_pascal_geometry()
    padding_checks, padding_maximum = audit_promoted_pascal_leaf_padding()
    comb_checks, comb_first, comb_last = audit_alternating_comb()
    abstract_checks = audit_abstract_hereditary_barrier()
    print(
        "PASS: threshold adjacent-layer reduction and exact regressions; "
        f"averaging={averaging}; coefficient={coefficient}; "
        f"double_chain={double_checks}; Pascal={pascal_checks}; "
        f"promoted_Pascal={promoted_checks}/{promoted_geometry}; "
        f"promoted_padding={padding_checks}; "
        f"comb={comb_checks}; abstract={abstract_checks}; "
        f"double_kill={double_kill}; "
        f"double_threshold_max={float(double_threshold):.6f}; "
        f"Pascal_max={float(pascal_maximum):.6f}; "
        f"Pascal_h50={float(pascal_last):.6f}; "
        f"promoted_last_cap_bits={promoted_last_cap.bit_length()}; "
        f"promoted_last_ratio_bits={promoted_last_ratio.numerator.bit_length() - promoted_last_ratio.denominator.bit_length()}; "
        f"padding_max={float(padding_maximum):.6f}; "
        f"comb=({float(comb_first):.6f},{float(comb_last):.6f})"
    )


if __name__ == "__main__":
    main()
