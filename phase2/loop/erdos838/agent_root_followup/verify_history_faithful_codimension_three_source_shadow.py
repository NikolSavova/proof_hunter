#!/usr/bin/env python3
"""Exact verifier for HISTORY_FAITHFUL_CODIMENSION_THREE_SOURCE_SHADOW."""

from __future__ import annotations

import itertools
import math
import sys
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

from agent_outer_internal_product.verify_third_cyclic_merged_downface_history_load_gate import (  # noqa: E402
    add_common_ear,
    is_convex,
)
from agent_outer_internal_product.verify_two_sided_merged_downface_maximum_child_gate import (  # noqa: E402
    role_gadget,
)


def exact_geometry():
    (points, left_roles, right_roles, left_marks, right_marks,
     left_index, right_index, seam) = role_gadget(3, 2)
    points, third_roles, third_index = add_common_ear(
        points, seam, left_marks, right_marks, left_index, right_index
    )

    loads = Counter()
    incidences = 0
    for left_word in itertools.product(*left_roles):
        for right_word in itertools.product(*right_roles):
            for third_word in itertools.product(*third_roles):
                for i, j, k in itertools.product(range(3), repeat=3):
                    output = frozenset(
                        seam
                        | {left_index[left_word[r]] for r in range(3) if r != i}
                        | {right_index[right_word[r]] for r in range(3) if r != j}
                        | {third_index[third_word[r]] for r in range(3) if r != k}
                    )
                    assert is_convex([points[x] for x in output])
                    loads[output] += 1
                    incidences += 1

    assert incidences == 512 * 27 == 13_824
    assert len(loads) == 1_728
    assert set(loads.values()) == {8}
    return incidences, len(loads), min(loads.values()), max(loads.values())


def product_formulas():
    checked = 0
    for dims1 in ((2, 2), (2, 3, 2), (3, 4)):
        for dims2 in ((2, 2), (3, 2, 2)):
            for dims3 in ((2, 3), (2, 2, 2)):
                mass = math.prod(dims1) * math.prod(dims2) * math.prod(dims3)
                incidences = mass * len(dims1) * len(dims2) * len(dims3)
                outputs = 0
                for a in dims1:
                    for b in dims2:
                        for c in dims3:
                            outputs += mass // (a * b * c)
                weighted_formula = mass
                weighted_formula *= sum(1 / a for a in dims1)
                weighted_formula *= sum(1 / b for b in dims2)
                weighted_formula *= sum(1 / c for c in dims3)
                assert outputs == round(weighted_formula)
                assert incidences >= outputs
                checked += 1

    for q in range(2, 17):
        mass = 1 << (3 * q)
        incidences = mass * q**3
        outputs = mass * q**3 // 8
        assert incidences == 8 * outputs
        checked += 1
    return checked


def fixed_gap_ledger():
    rows = []
    for ell in (32, 40, 48, 64, 80, 96, 128):
        ambient = 1 << ell
        a = ell
        b = ell // 4
        alphabet = ambient // ell**6
        side = (1 << a) * alphabet**b
        mass = side * side * (1 << ell)
        bank = mass * ell**3 // 8
        assert bank * 8 == mass * ell**3
        assert abs(math.log2(bank / mass) - (3 * math.log2(ell) - 3)) < 1e-12
        rows.append((ell, alphabet, mass.bit_length(), bank.bit_length()))
    return rows


def main():
    geometry = exact_geometry()
    formulas = product_formulas()
    ledger = fixed_gap_ledger()
    print(
        "PASS: codim-three source shadow; geometry=%s; formulas=%d; "
        "fixed-gap L=%d..%d"
        % (geometry, formulas, ledger[0][0], ledger[-1][0])
    )


if __name__ == "__main__":
    main()
