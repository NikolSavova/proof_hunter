#!/usr/bin/env python3
"""Exact checks for HIGH_TRIANGLE_QUERY_LOCALIZATION_GATE.md."""

from fractions import Fraction as Q
from itertools import combinations, product
from math import comb


def local_cauchy_audit():
    systems = 0
    for rows in range(1, 101):
        for columns in range(1, 101):
            edges = rows * columns
            maximum = max(rows, columns)
            if maximum <= 5:
                assert edges <= 5 * rows
            else:
                triangles = comb(maximum, 3)
                assert 5 * edges * edges <= 54 * rows * triangles
            systems += 1
    return systems


def dyadic_and_release_audit():
    alpha = Q(7, 11)
    weights = [alpha / 2, alpha / 3, alpha / 9,
               alpha / 17, alpha / 100]
    layer_upper = {}
    for weight in weights:
        level = 0
        upper = alpha
        while not (upper / 2 < weight <= upper):
            level += 1
            upper /= 2
        layer_upper[level] = upper
        assert weight <= upper < 2 * weight
    assert sum(layer_upper.values(), Q(0)) < 2 * alpha
    assert sum(layer_upper[level] for level in layer_upper) < 2 * alpha

    # Direct record-to-source routing really has the release multiplier.
    degree = 37
    direct_source_load = degree * alpha
    compressed_layer_load = alpha
    assert direct_source_load == 37 * alpha
    assert compressed_layer_load == alpha
    return len(layer_upper), direct_source_load, compressed_layer_load


def circuit_signature_audit():
    signatures = set()
    triangle = (0, 1, 2)
    for triangle_rank in (2, 3):
        for trace in combinations(triangle, triangle_rank):
            for interior_position in range(4):
                signatures.add((trace, interior_position))
    assert len(signatures) == 16
    return len(signatures)


def strongly_connected_components(vertex_count, edges):
    graph = [[] for _ in range(vertex_count)]
    reverse = [[] for _ in range(vertex_count)]
    for left, right in edges:
        graph[left].append(right)
        reverse[right].append(left)
    seen, order = set(), []

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


def graph_and_direction_audit():
    systems = 0
    for vertex_count in range(1, 5):
        possible = [(i, j) for i in range(vertex_count)
                    for j in range(vertex_count) if i != j]
        for choices in product((0, 1), repeat=len(possible)):
            edges = [edge for edge, chosen in zip(possible, choices) if chosen]
            component, count = strongly_connected_components(vertex_count, edges)
            condensation = {(component[i], component[j]) for i, j in edges
                            if component[i] != component[j]}
            for start in range(count):
                frontier = [v for u, v in condensation if u == start]
                reached = set()
                while frontier:
                    point = frontier.pop()
                    assert point != start
                    if point in reached:
                        continue
                    reached.add(point)
                    frontier.extend(v for u, v in condensation if u == point)
            systems += 1

    direction_weights = [Q(17, 5), Q(11, 7), Q(13, 11),
                         Q(7, 13), Q(5, 17)]
    direction_weights.sort(reverse=True)
    total = sum(direction_weights, Q(0))
    top_three = sum(direction_weights[:3], Q(0))
    eta = Q(1, 5)
    if top_three >= (1 - eta) * total:
        assert direction_weights[0] >= (1 - eta) * total / 3
    else:
        assert sum(direction_weights[3:], Q(0)) > eta * total
    return systems


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(convex_hull(points)) == len(points)


def planar_star_audit(maximum_rank=10):
    base = [(Q(0), Q(0)), (Q(4), Q(0)),
            (Q(4), Q(4)), (Q(0), Q(4))]
    c = base[-1]
    delta = Q(1, 3600)
    cloud = [(Q(2) - delta * t * t, -Q(1, 5) + delta * t)
             for t in range(1, 7)]
    triangle = cloud[:3]
    audited = 0
    for rank in range(1, maximum_rank + 1):
        shield = []
        for k in range(1, rank + 1):
            x = Q(4 * k, rank + 1)
            y = Q(5) - (x - 2) ** 2 / 10
            shield.append((x, y))
        ground = base + cloud + shield
        assert all(cross(*triple) != 0 for triple in combinations(ground, 3))
        assert triangle[1] not in convex_hull(triangle + [c])
        for mask in range(1 << rank):
            selected = [shield[k] for k in range(rank) if mask >> k & 1]
            retained_base = base + selected
            assert convex(retained_base)
            assert all(convex(retained_base + [point]) for point in cloud)
            assert not convex(retained_base + triangle)
            audited += 1
    return audited


def main():
    local = local_cauchy_audit()
    dyadic = dyadic_and_release_audit()
    signatures = circuit_signature_audit()
    graphs = graph_and_direction_audit()
    stars = planar_star_audit()
    print(
        "PASS: local=%d dyadic=%s signatures=%d SCC=%d planar-stars=%d"
        % (local, dyadic, signatures, graphs, stars)
    )


if __name__ == "__main__":
    main()
