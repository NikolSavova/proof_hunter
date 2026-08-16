#!/usr/bin/env python3
"""Generate the explicit 134-point W3 parent for sampled spectrum audits.

The two 44-point ingredients and their complete profile menu are exact.
The final strong-comb composition uses the same rational formula as the
certified glue, but deliberately omits its cubic exact top-split audit.
This is construction-side finite evidence, not a new proof certificate.
"""

from decimal import Decimal, getcontext
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import importlib.util
import sys


HERE = Path(__file__).resolve().parent
SHIELD = HERE.parent / "agent_shield_circuit_cover"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SHIELD))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cert = load("pareto_cert", SHIELD / "verify_pareto_two_level_recursive_menu.py")
explore = load("two_level_rechart", HERE / "explore_two_level_rechart.py")
glue = cert.glue

TARGETS = ((15121, 102449), (44728, 21566), (102449, 15121))


def strong_glue_unchecked(left, right):
    """The exact certified rational formula, without the O(n^3) audit."""
    left, right = glue.normalize(left), glue.normalize(right)
    slopes = []
    for block in (left, right):
        slopes.extend((b[1] - a[1]) / (b[0] - a[0])
                      for a, b in combinations(block, 2))
    if slopes:
        minimum = min(slopes)
        epsilon = min(Q(1, 4), minimum / (8 + 2 * minimum))
    else:
        epsilon = Q(1, 4)
    return ([(epsilon * x, y) for x, y in left]
            + [(1 + epsilon * x, 2 + y) for x, y in right])


def comb_unchecked(blocks):
    out = blocks[0]
    for block in blocks[1:]:
        out = strong_glue_unchecked(out, block)
    return out


def decimal(q):
    return Decimal(q.numerator) / Decimal(q.denominator)


def build_level3():
    parent = cert.build_parent()
    orders, profiles = cert.parent_spectrum(parent)
    blocks = [[(Q(0), Q(0))]]
    selected = []
    selected_orders = []
    for target in TARGETS:
        index = profiles.index(target)
        order = orders[index]
        selected.append(index)
        selected_orders.append(order)
        child = explore.rechart(parent, order)
        blocks.append(child)
    blocks.append([(Q(0), Q(0))])
    level3 = comb_unchecked(blocks)
    assert len(level3) == 134
    return parent, level3, selected, selected_orders


def main():
    _, level3, selected, _ = build_level3()

    getcontext().prec = 80
    print(len(level3))
    for x, y in level3:
        print(f"{decimal(x):.60E} {decimal(y):.60E}")
    print(
        "generated exact-rational W3 parent; "
        f"selected 44-point chambers={selected}; "
        "top-level split check intentionally omitted",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
