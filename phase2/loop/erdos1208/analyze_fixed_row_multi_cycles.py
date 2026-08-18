#!/usr/bin/env python3
"""Inspect relation four-sets that are C4s in multiple fixed-row projections."""

from __future__ import annotations

from collections import defaultdict

from verify_transverse_closure_witness import POINTS
from verify_transverse_fixed_row_c4 import (
    ROLE_PAIRS,
    fixed_row_relations,
    projection_cycles,
)


ROLE_NAMES = ("u", "v", "x", "y")


def partition_for_projection(relations, cycle, first, second):
    first_groups = defaultdict(list)
    second_groups = defaultdict(list)
    for index in cycle:
        relation = relations[index]
        first_groups[relation[first]].append(index)
        second_groups[relation[second]].append(index)
    return (
        tuple(sorted(tuple(sorted(group)) for group in first_groups.values())),
        tuple(sorted(tuple(sorted(group)) for group in second_groups.values())),
    )


def main():
    relations = fixed_row_relations(POINTS, (0, -1))
    families = {
        pair: projection_cycles(relations, *pair)
        for pair in ROLE_PAIRS
    }
    union = set().union(*families.values())
    multi = [
        cycle
        for cycle in union
        if sum(cycle in family for family in families.values()) > 1
    ]
    print("multi", len(multi))
    for cycle in multi:
        print("cycle", cycle)
        for pair, family in families.items():
            if cycle in family:
                names = ROLE_NAMES[pair[0]] + ROLE_NAMES[pair[1]]
                print(" projection", names, partition_for_projection(relations, cycle, *pair))
        for index in cycle:
            relation = relations[index]
            print(index, relation, tuple(POINTS[item] for item in relation))
        print()


if __name__ == "__main__":
    main()
