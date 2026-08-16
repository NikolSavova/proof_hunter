#!/usr/bin/env python3
"""Exact checks for TANGENT_MARKED_SHIELD_DESCENT.md."""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def configuration():
    outer = [
        (-3, -1), (-2, -3), (1, -4), (3, -2),
        (4, 1), (2, 3), (-1, 4), (-4, 2),
    ]
    outer = [(F(x), F(y)) for x, y in outer]
    inner = [
        (F(-5881, 2000), F(-2451, 2500)),
        (F(-4901, 2500), F(-147, 50)),
        (F(9797, 10000), F(-7839, 2000)),
        (F(29399, 10000), F(-19601, 10000)),
        (F(9801, 2500), F(4899, 5000)),
        (F(4901, 2500), F(5879, 2000)),
        (F(-2449, 2500), F(7841, 2000)),
        (F(-39203, 10000), F(19601, 10000)),
    ]
    blocks = [(outer[i], inner[i]) for i in range(8)]
    repairs = [
        (F(-177, 70), F(-141, 70)),
        (F(-2983, 1180), F(-1187, 590)),
        (F(-101, 40), F(-121, 60)),
        (F(-1619, 640), F(-641, 320)),
    ]
    points = sum((list(B) for B in blocks), []) + repairs
    return blocks, repairs, points


def completion_indices(bits):
    return tuple(2 * i + bits[i] for i in range(8))


def recover_cell(mark, output, points):
    """Recover the unoriented five-vertex cell from cyclic adjacency."""
    coords = [points[i] for i in output]
    boundary = hull(coords)
    assert len(boundary) == len(output)
    inverse = {points[i]: i for i in output}
    cycle = [inverse[x] for x in boundary]
    j = cycle.index(mark)
    return frozenset(cycle[(j + d) % len(cycle)] for d in (-2, -1, 0, 1, 2))


def check_geometry_and_decoder():
    blocks, repairs, points = configuration()
    assert all(cross(*triple) != 0 for triple in combinations(points, 3))

    bit_words = list(product(range(2), repeat=8))
    completions = [completion_indices(bits) for bits in bit_words]
    assert len(completions) == 256
    assert all(convex([points[i] for i in Q]) for Q in completions)

    # Local radial nesting is the circuit certificate for every completion
    # pair.  Audit all root choices exactly, then audit all pairs as well.
    for i in range(8):
        outer, inner = blocks[i]
        for left in blocks[(i - 1) % 8]:
            for right in blocks[(i + 1) % 8]:
                assert not convex([outer, inner, left, right])
    assert all(not convex([points[i] for i in sorted(set(Q) | set(R))])
               for Q, R in combinations(completions, 2))

    repair_indices = tuple(range(16, 20))
    stars = [Q + (p,) for Q in completions for p in repair_indices]
    assert len(stars) == 1024
    assert all(convex([points[i] for i in S]) for S in stars)
    assert all(not convex([points[i] for i in Q + pair])
               for Q in completions for pair in combinations(repair_indices, 2))
    assert all(all(i in S or not convex([points[j] for j in S + (i,)])
                   for i in range(len(points))) for S in stars)

    # The repair block has the arbitrary nonconvex four-point order type.
    assert not convex(repairs)
    assert all(convex(list(T)) for T in combinations(repairs, 3))

    # Fix blocks 7,0,1,2 to their outer points.  Blocks 3,4,5,6 carry the
    # four variable bits in one common tangent cell.
    fixed_words = [bits for bits in bit_words
                   if bits[7] == bits[0] == bits[1] == bits[2] == 0]
    fixed = [completion_indices(bits) for bits in fixed_words]
    assert len(fixed) == 16
    mark = 16
    expected_cell = frozenset((14, 0, mark, 2, 4))
    free_positions = (3, 4, 5, 6)
    shield = (16, 18, 19)
    assert convex([points[i] for i in shield])

    for Q in fixed:
        S = Q + (mark,)
        assert recover_cell(mark, S, points) == expected_cell
        assert not convex([points[i] for i in sorted(set(S) | set(shield))])

    level_data = []
    for t in range(5):
        loads = Counter()
        for Q in fixed:
            S = Q + (mark,)
            free = tuple(Q[i] for i in free_positions)
            for deleted in combinations(free, t):
                T = tuple(i for i in S if i not in deleted)
                assert convex([points[i] for i in T])
                assert recover_cell(mark, T, points) == expected_cell
                loads[frozenset(T)] += 1
        incidences = len(fixed) * comb(4, t)
        outputs = comb(4, t) * 2 ** (4 - t)
        assert sum(loads.values()) == incidences
        assert len(loads) == outputs
        assert set(loads.values()) == {2 ** t}
        level_data.append((t, incidences, outputs, 2 ** t))
    assert level_data[2] == (2, 96, 24, 4)

    # Now allow all sixteen tangent cells (the choices in blocks 7,0,1,2).
    # Guarded outputs from distinct cells cannot collide because the output
    # decoder recovers the cell.
    all_loads = Counter()
    cells = set()
    t = 2
    for Q in completions:
        S = Q + (mark,)
        cell = recover_cell(mark, S, points)
        cells.add(cell)
        free = tuple(i for i in Q if i not in cell)
        assert len(free) == 4
        for deleted in combinations(free, t):
            T = tuple(i for i in S if i not in deleted)
            assert recover_cell(mark, T, points) == cell
            all_loads[frozenset(T)] += 1
    assert len(cells) == 16
    assert sum(all_loads.values()) == 256 * 6 == 1536
    assert len(all_loads) == 16 * 24 == 384
    assert set(all_loads.values()) == {4}

    return len(completions), len(stars), len(cells), level_data, (
        sum(all_loads.values()), len(all_loads), max(all_loads.values()))


def check_guarded_carleson_weighted():
    # Abstract stars with recoverable cells.  An output is deliberately
    # shared only within its cell; the theorem should charge the maximum
    # total cell weight A, never the number of possible ambient cells.
    histories = []
    for cell in range(7):
        for j in range(cell % 4 + 1):
            histories.append((cell, F(j + 1, cell + 2)))
    B_t = 6
    outputs = Counter()
    total_weight = F(0)
    cell_weight = Counter()
    for serial, (cell, weight) in enumerate(histories):
        total_weight += weight
        cell_weight[cell] += weight
        # Six formal outputs.  Each history produces each output at most
        # once, and collisions occur only inside one recoverable cell.
        for j in range(B_t):
            outputs[(cell, j)] += weight
    lhs = total_weight * B_t
    assert lhs == sum(outputs.values(), F(0))
    Lambda = max(outputs.values())
    A = max(cell_weight.values())
    assert Lambda == A
    distinct_capacity = len(outputs)
    assert lhs <= Lambda * distinct_capacity
    return len(histories), total_weight, Lambda, A, distinct_capacity


def check_collision_cauchy():
    tests = 0
    for V in range(1, 8):
        for bins in range(1, min(V, 5) + 1):
            for degrees in product(range(5), repeat=bins):
                N = sum(degrees)
                if N == 0:
                    continue
                collision = sum(comb(d, 2) for d in degrees)
                for good in range(collision + 1):
                    L = ceil(F(good, V))
                    for theta in (F(1), F(1, 2), F(1, 3)):
                        for beta in range(3):
                            if F(good) < theta * collision - beta * N:
                                continue
                            x = F(N, V)
                            c = F(1) + F(2 * beta) / theta
                            assert x * x - c * x - F(2 * L) / theta <= 0
                            tests += 1
    return tests


def check_cross_petal_circuit():
    # A literal four-circuit with common prefix B={u,v}; both B+D and B+D'
    # are triangles, while their union is bad and meets both petals.
    points = [(F(-1), F(0)), (F(1), F(0)),
              (F(0), F(-2)), (F(0), F(-1))]
    B, D, E = (0, 1), (2,), (3,)
    assert convex([points[i] for i in B + D])
    assert convex([points[i] for i in B + E])
    assert not convex(points)
    circuit = set(range(4))
    assert circuit & (set(D) - set(E))
    assert circuit & (set(E) - set(D))
    return 1


def main():
    geometry = check_geometry_and_decoder()
    weighted = check_guarded_carleson_weighted()
    cauchy = check_collision_cauchy()
    cross = check_cross_petal_circuit()
    print(
        "tangent marked shield descent: PASS; "
        f"geometry={geometry}; weighted={weighted}; "
        f"collision_checks={cauchy}; cross_petals={cross}"
    )


if __name__ == "__main__":
    main()
