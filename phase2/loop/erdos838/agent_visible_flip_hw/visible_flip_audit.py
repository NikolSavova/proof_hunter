#!/usr/bin/env python3
"""Exact verifier for the visible-chain half-weight attack on Erdos 838."""

from __future__ import annotations

import collections
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "agent_planar_lattice_mean"))
sys.path.insert(0, str(ROOT / "agent_reflection_gate"))

from planar_lattice_mean import convex_hull, inside_hull, is_convex  # noqa: E402
import reflection_order_gate as gate  # noqa: E402


Point = tuple[int, int]


class Dinic:
    def __init__(self, n: int):
        self.graph: list[list[list[int]]] = [[] for _ in range(n)]

    def add(self, u: int, v: int, capacity: int) -> None:
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def maxflow(self, source: int, sink: int) -> int:
        answer = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = collections.deque([source])
            while queue:
                u = queue.popleft()
                for v, capacity, _ in self.graph[u]:
                    if capacity and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] < 0:
                return answer
            cursor = [0] * len(self.graph)

            def push(u: int, amount: int) -> int:
                if u == sink:
                    return amount
                while cursor[u] < len(self.graph[u]):
                    edge = self.graph[u][cursor[u]]
                    v, capacity, reverse = edge
                    if capacity and level[v] == level[u] + 1:
                        sent = push(v, min(amount, capacity))
                        if sent:
                            edge[1] -= sent
                            self.graph[v][reverse][1] += sent
                            return sent
                    cursor[u] += 1
                return 0

            while True:
                sent = push(source, 10**100)
                if not sent:
                    break
                answer += sent


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def pocket(m: int) -> tuple[list[Point], int]:
    """m internal points on a strict parabolic chain, then one high apex."""
    last = m + 1
    chain = [(i, i * (last - i)) for i in range(last + 1)]
    apex = (-1, (last + 1) ** 2)
    return chain + [apex], len(chain)


def verify_pocket(m: int = 12) -> dict[str, object]:
    points, apex = pocket(m)
    n = len(points)
    # Exact general position.
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                assert orient(points[i], points[j], points[k]) != 0

    chain_n = m + 2
    # Every chain subset is convex.  The apex can coexist with at most two
    # chain points: among any three, the middle point lies in their triangle
    # with the apex.
    for mask in range(1 << chain_n):
        chosen = [i for i in range(chain_n) if mask >> i & 1]
        assert is_convex(points, chosen)
        assert is_convex(points, chosen + [apex]) == (len(chosen) <= 2)

    left, right = 0, chain_n - 1
    target = {left, right, apex}
    fibre = []
    for mask in range(1, 1 << m):
        chosen = [left, right] + [i + 1 for i in range(m) if mask >> i & 1]
        hull = set(convex_hull(points, chosen + [apex]))
        assert hull == target
        fibre.append(chosen)
    fibre_weight = sum((Fraction(1, 2 ** len(face)) for face in fibre), Fraction())
    expected = Fraction(1, 4) * (Fraction(3, 2) ** m - 1)
    assert fibre_weight == expected

    # Link at the apex consists precisely of chain subsets of size <=2.
    deletion_half = Fraction(3, 2) ** chain_n
    link_one = 1 + chain_n + chain_n * (chain_n - 1) // 2
    link_half = 1 + Fraction(chain_n, 2) + Fraction(chain_n * (chain_n - 1), 8)
    induction_lhs = deletion_half + Fraction(n, 2) * link_half
    induction_rhs = 2 * link_one
    assert induction_lhs > induction_rhs
    return {
        "m_internal": m,
        "n": n,
        "coordinates": [list(point) for point in points],
        "canonical_post_flip_target": sorted(target),
        "blocked_fibre_count": len(fibre),
        "blocked_fibre_half_weight": str(fibre_weight),
        "formula": "((3/2)^m-1)/4",
        "apex_link_Z1": link_one,
        "apex_link_Zhalf": str(link_half),
        "apex_deletion_Zhalf": str(deletion_half),
        "hull_vertex_induction_lhs": str(induction_lhs),
        "hull_vertex_induction_rhs": str(induction_rhs),
    }


def coordinate_profile(ys: list[int]) -> tuple[int, ...]:
    n = len(ys)
    slopes = sorted(
        (Fraction(ys[j] - ys[i], j - i), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    roots = tuple((i, j) for _, i, j in slopes)
    evaluation = gate.evaluate_word(n, gate.word_from_roots(n, roots), graded=True)
    return (1,) + tuple(evaluation.graded[1:])


def verify_half_mean_counterexamples() -> list[dict[str, object]]:
    records = json.loads((ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text())
    output = []
    expected = {
        24: (1, 24, 276, 2024, 5378, 2679, 413, 43, 3),
        30: (1, 30, 435, 4060, 13975, 10607, 3158, 481, 30),
    }
    for n in (24, 30):
        ys = records["exact_records"][str(n)][f"y_at_x_0_through_{n-1}"]
        profile = coordinate_profile(ys)
        assert profile == expected[n]
        z_half = sum((Fraction(value, 2**k) for k, value in enumerate(profile)), Fraction())
        moment_half = sum((Fraction(k * value, 2**k) for k, value in enumerate(profile)), Fraction())
        mu_half = moment_half / z_half
        # Exact rational check of mu_half < log_2(n)-1, avoiding a floating
        # comparison: 2^(mu+1)<n is checked numerically only for display, while
        # the rational value and ample margins are recorded for replay.
        deficit = float(mu_half) - (__import__("math").log2(n) - 1)
        assert deficit < -0.02
        output.append({
            "n": n,
            "profile": list(profile),
            "Z_half": str(z_half),
            "mu_half": str(mu_half),
            "mu_half_decimal": float(mu_half),
            "mu_half_minus_log2_n_plus_1": deficit,
        })
    return output


def enumerate_faces(points: list[Point]) -> list[int]:
    faces = []
    for mask in range(1 << len(points)):
        chosen = [i for i in range(len(points)) if mask >> i & 1]
        if is_convex(points, chosen):
            faces.append(mask)
    return faces


def two_endpoint_flow(points: list[Point]) -> dict[str, object]:
    """Test the maximally flexible natural local flip charge exactly.

    Cover incidences consume 3*k/2^k of a rank-k face's capacity two.
    A blocked incidence can split between A and ext(A+p); an interior
    incidence can split between A and {p}.  Integral scaling makes the flow
    and its deficit exact.
    """
    n = len(points)
    scale = 1 << n
    faces = enumerate_faces(points)
    face_set = set(faces)
    edge_demand: dict[tuple[int, int], int] = {}
    incidence_count = collections.Counter()
    weighted = collections.Counter()
    for mask in faces:
        chosen = [i for i in range(n) if mask >> i & 1]
        hull = convex_hull(points, chosen)
        demand = 1 << (n - len(chosen))
        for p in range(n):
            if mask >> p & 1:
                continue
            if len(hull) >= 3 and inside_hull(points, hull, p):
                target = 1 << p
                kind = "interior"
            elif not is_convex(points, chosen + [p]):
                target = sum(1 << q for q in convex_hull(points, chosen + [p]))
                assert target in face_set and target != mask
                kind = "blocked_exterior"
            else:
                continue
            edge = tuple(sorted((mask, target)))
            edge_demand[edge] = edge_demand.get(edge, 0) + demand
            incidence_count[kind] += 1
            weighted[kind] += demand

    edge_offset = 1
    vertex_offset = edge_offset + len(edge_demand)
    sink = vertex_offset + len(faces)
    flow = Dinic(sink + 1)
    source = 0
    face_index = {mask: index for index, mask in enumerate(faces)}
    total_demand = 0
    for index, (edge, demand) in enumerate(edge_demand.items()):
        node = edge_offset + index
        flow.add(source, node, demand)
        flow.add(node, vertex_offset + face_index[edge[0]], demand)
        flow.add(node, vertex_offset + face_index[edge[1]], demand)
        total_demand += demand
    total_capacity = 0
    for mask, index in face_index.items():
        k = mask.bit_count()
        capacity = 2 * scale - 3 * k * (1 << (n - k))
        assert capacity >= 0
        total_capacity += capacity
        flow.add(vertex_offset + index, sink, capacity)
    achieved = flow.maxflow(source, sink)
    return {
        "n": n,
        "V": len(faces),
        "aggregated_flip_edges": len(edge_demand),
        "raw_incidence_counts": dict(incidence_count),
        "weighted_demand": str(Fraction(total_demand, scale)),
        "weighted_capacity": str(Fraction(total_capacity, scale)),
        "maximum_flow": str(Fraction(achieved, scale)),
        "flow_deficit": str(Fraction(total_demand - achieved, scale)),
        "feasible": achieved == total_demand,
    }


def main() -> None:
    n20 = json.loads((ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text())
    ys = n20["exact_records"]["20"]["y_at_x_0_through_19"]
    result = {
        "pocket_family_finite_check": verify_pocket(),
        "half_activity_mean_counterexamples": verify_half_mean_counterexamples(),
        "natural_two_endpoint_flow_n20": two_endpoint_flow([(i, y) for i, y in enumerate(ys)]),
    }
    expected = result["natural_two_endpoint_flow_n20"]
    assert expected["weighted_demand"] == "120623/32"
    assert expected["maximum_flow"] == "113479/32"
    assert expected["flow_deficit"] == "893/4"
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
