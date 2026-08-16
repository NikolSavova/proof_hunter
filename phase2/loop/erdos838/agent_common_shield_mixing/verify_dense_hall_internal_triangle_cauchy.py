#!/usr/bin/env python3
"""Exact checks for DENSE_HALL_INTERNAL_TRIANGLE_CAUCHY.md."""

from fractions import Fraction as Q
from itertools import product
from math import comb


def local_algebra_audit():
    systems = 0
    for rows in range(1, 101):
        for columns in range(1, 101):
            edges = rows * columns
            hall_size = 2 * rows + 2 * columns + 1
            if min(rows, columns) <= 5:
                assert 2 * edges <= 5 * hall_size
            else:
                triangles = comb(rows, 3) + comb(columns, 3)
                assert 20 * edges * edges <= 27 * hall_size * triangles
            systems += 1
    return systems


def graph_audit():
    # Exhaust all small bipartite subgraphs after deleting isolated labels.
    systems = 0
    for rows in range(1, 5):
        for columns in range(1, 5):
            pairs = [(i, j) for i in range(rows) for j in range(columns)]
            for mask in range(1, 1 << len(pairs)):
                active_rows = {i for index, (i, _j) in enumerate(pairs)
                               if mask >> index & 1}
                active_columns = {j for index, (_i, j) in enumerate(pairs)
                                  if mask >> index & 1}
                edge_count = mask.bit_count()
                a, b = len(active_rows), len(active_columns)
                hall_size = 2 * a + 2 * b + 1
                if min(a, b) <= 5:
                    assert 2 * edge_count <= 5 * hall_size
                else:
                    triangles = comb(a, 3) + comb(b, 3)
                    assert 20 * edge_count * edge_count <= 27 * hall_size * triangles
                systems += 1
    return systems


def weighted_overlap_audit():
    # Actual output labels deliberately overlap across contexts.
    contexts = [
        {
            "weight": Q(2, 3),
            "edges": 36,
            "hall": {f"h{k}" for k in range(25)},
            "triangles": {f"t{k}" for k in range(40)},
            "thick": True,
        },
        {
            "weight": Q(5, 7),
            "edges": 42,
            # The exact 6-by-7 complete rectangle: h=2(6+7)+1=27,
            # i=C(6,3)+C(7,3)=55 and e=42.
            "hall": {f"h{k}" for k in range(10, 37)},
            "triangles": {f"t{k}" for k in range(20, 75)},
            "thick": True,
        },
        {
            "weight": Q(11, 13),
            "edges": 20,
            # The exact 4-by-5 complete thin rectangle: h=19 and e=20.
            "hall": {f"h{k}" for k in range(35, 54)},
            "triangles": set(),
            "thick": False,
        },
    ]

    hall_loads = {}
    triangle_loads = {}
    hall_mass = triangle_mass = Q(0)
    thin_demand = thick_demand = Q(0)
    for context in contexts:
        weight = context["weight"]
        hall_mass += weight * len(context["hall"])
        for face in context["hall"]:
            hall_loads[face] = hall_loads.get(face, Q(0)) + weight
        if context["thick"]:
            triangle_mass += weight * len(context["triangles"])
            thick_demand += weight * context["edges"]
            for face in context["triangles"]:
                triangle_loads[face] = triangle_loads.get(face, Q(0)) + weight
        else:
            thin_demand += weight * context["edges"]

    hall_load = max(hall_loads.values())
    triangle_load = max(triangle_loads.values())
    face_universe = set(hall_loads) | set(triangle_loads)
    face_count = len(face_universe)
    assert hall_mass <= hall_load * face_count
    assert triangle_mass <= triangle_load * face_count

    # Thin inequality and the squared thick Cauchy inequality.
    thin_hall_mass = sum(
        context["weight"] * len(context["hall"])
        for context in contexts if not context["thick"]
    )
    assert 2 * thin_demand <= 5 * thin_hall_mass
    thick_hall_mass = sum(
        context["weight"] * len(context["hall"])
        for context in contexts if context["thick"]
    )
    assert 20 * thick_demand * thick_demand <= (
        27 * thick_hall_mass * triangle_mass
    )
    return hall_load, triangle_load, face_count


def strongly_connected_components(vertex_count, edges):
    graph = [[] for _ in range(vertex_count)]
    reverse = [[] for _ in range(vertex_count)]
    for left, right in edges:
        graph[left].append(right)
        reverse[right].append(left)

    seen = set()
    order = []

    def visit(vertex):
        seen.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                visit(neighbor)
        order.append(vertex)

    for vertex in range(vertex_count):
        if vertex not in seen:
            visit(vertex)

    component = [-1] * vertex_count

    def assign(vertex, label):
        component[vertex] = label
        for neighbor in reverse[vertex]:
            if component[neighbor] == -1:
                assign(neighbor, label)

    label = 0
    for vertex in reversed(order):
        if component[vertex] == -1:
            assign(vertex, label)
            label += 1
    return component, label


def graph_decomposition_audit():
    systems = 0
    for vertex_count in range(1, 5):
        possible = [(i, j) for i in range(vertex_count)
                    for j in range(vertex_count) if i != j]
        for choices in product((0, 1), repeat=len(possible)):
            edges = [edge for edge, chosen in zip(possible, choices) if chosen]
            component, count = strongly_connected_components(vertex_count, edges)
            condensation = {(component[i], component[j]) for i, j in edges
                            if component[i] != component[j]}

            # Condensation is acyclic: a cycle would merge its components.
            for start in range(count):
                frontier = [right for left, right in condensation if left == start]
                reached = set()
                while frontier:
                    point = frontier.pop()
                    assert point != start
                    if point in reached:
                        continue
                    reached.add(point)
                    frontier.extend(right for left, right in condensation
                                    if left == point)

            # Every edge internal to a nontrivial SCC has a return path.
            for left, right in edges:
                if component[left] != component[right]:
                    continue
                frontier = [right]
                reached = set()
                while frontier and left not in reached:
                    point = frontier.pop()
                    if point in reached:
                        continue
                    reached.add(point)
                    frontier.extend(j for i, j in edges if i == point)
                assert left in reached
            systems += 1
    return systems


def main():
    local = local_algebra_audit()
    graphs = graph_audit()
    weighted = weighted_overlap_audit()
    decompositions = graph_decomposition_audit()
    print(
        "PASS: local=%d bipartite=%d weighted-loads=%s SCC-systems=%d"
        % (local, graphs, weighted, decompositions)
    )


if __name__ == "__main__":
    main()
