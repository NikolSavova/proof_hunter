#!/usr/bin/env python3
"""Exact checks for the full external-alphabet energy trichotomy."""

from fractions import Fraction
from itertools import combinations, product
from math import comb


def energy(occurrences):
    """Occurrences are dicts with cell, completion, bank, weight, profile."""
    pair_weights = {}
    diagonal = Fraction(0)
    for occurrence in occurrences:
        bank = tuple(occurrence["bank"])
        weight = Fraction(occurrence["weight"], len(bank))
        diagonal += len(bank) * weight * weight
        for face in bank:
            key = (occurrence["completion"], face)
            pair_weights[key] = pair_weights.get(key, Fraction(0)) + weight
    total = sum((value * value for value in pair_weights.values()), Fraction(0))
    return total, diagonal, total - diagonal


def profiled_energy(occurrences):
    weights = {}
    diagonal = Fraction(0)
    for occurrence in occurrences:
        bank = tuple(occurrence["bank"])
        weight = Fraction(occurrence["weight"], len(bank))
        diagonal += len(bank) * weight * weight
        for face in bank:
            key = (occurrence["completion"], occurrence["profile"], face)
            weights[key] = weights.get(key, Fraction(0)) + weight
    total = sum((value * value for value in weights.values()), Fraction(0))
    return total, diagonal, total - diagonal


def abstract_alphabet_identity():
    # Every cell has two letters and different letters in one cell have
    # different completions, as in B union {x}.
    occurrences = [
        {"cell": 0, "letter": "a", "completion": "Y0",
         "bank": ("f0", "f1"), "weight": 2, "profile": ("a", "e0")},
        {"cell": 0, "letter": "b", "completion": "Y1",
         "bank": ("f1",), "weight": 2, "profile": ("b", "e1")},
        {"cell": 1, "letter": "c", "completion": "Y0",
         "bank": ("f0", "f2"), "weight": 3, "profile": ("a", "e0")},
        {"cell": 1, "letter": "d", "completion": "Y2",
         "bank": ("f1", "f2", "f3"), "weight": 3,
         "profile": ("d", "e2")},
        {"cell": 2, "letter": "e", "completion": "Y0",
         "bank": ("f0", "f1"), "weight": 5, "profile": ("e", "e3")},
        {"cell": 2, "letter": "f", "completion": "Y1",
         "bank": ("f1", "f3"), "weight": 5, "profile": ("b", "e1")},
    ]
    full, diagonal, collision = energy(occurrences)
    assert full == diagonal + collision

    by_cell = {}
    for occurrence in occurrences:
        by_cell.setdefault(occurrence["cell"], []).append(occurrence)
    assert {len(values) for values in by_cell.values()} == {2}
    energies = []
    for choice in product(*by_cell.values()):
        energies.append(energy(choice)[0])
    expected = sum(energies, Fraction(0)) / len(energies)
    D = 2
    assert expected == diagonal / D + collision / (D * D)
    assert full == D * D * expected - (D - 1) * diagonal

    refined, same_diagonal, refined_collision = profiled_energy(occurrences)
    assert same_diagonal == diagonal
    profiles_per_completion = {}
    for occurrence in occurrences:
        profiles_per_completion.setdefault(occurrence["completion"], set()).add(
            occurrence["profile"]
        )
    K = max(map(len, profiles_per_completion.values()))
    assert refined * K >= full
    assert refined_collision * K >= collision - (K - 1) * diagonal
    return full, diagonal, collision, expected, K


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def build(sequence):
        out = []
        for point in sequence:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    lower = build(points)
    upper = build(reversed(points))
    return lower[:-1] + upper[:-1]


def in_convex_position(points):
    return len(convex_hull(points)) == len(set(points))


def circle_point(parameter):
    parameter = Fraction(parameter)
    return ((1 - parameter * parameter) / (1 + parameter * parameter),
            2 * parameter / (1 + parameter * parameter))


def all_general_position(points):
    return all(orient(a, b, c) != 0 for a, b, c in combinations(points, 3))


def inside_root_triangle(x, u, v, z):
    return (orient(u, v, x) > 0 and orient(v, z, x) > 0
            and orient(z, u, x) > 0)


def choose_pocket_points(count, fixed_points, u, v, z, carriers, top):
    """Choose exact rational points in the stable open cell near (0,1/4)."""
    chosen = []
    denominator = 10000
    for index in range(1, 2000):
        x_coordinate = Fraction((index % 17) - 8, denominator)
        y_coordinate = Fraction(1, 4) + Fraction(index * index + 3 * index,
                                                  denominator * denominator)
        candidate = (x_coordinate, y_coordinate)
        trial = fixed_points + chosen + [candidate]
        if not all_general_position(trial):
            continue
        if not inside_root_triangle(candidate, u, v, z):
            continue
        if not all(in_convex_position(list(carrier) + [candidate])
                   for carrier in carriers):
            continue
        positive = [point for point in top if point != z
                    and orient(candidate, z, point) > 0]
        negative = [point for point in top if point != z
                    and orient(candidate, z, point) < 0]
        if not (len(positive) == 5 and len(negative) == 7):
            continue
        chosen.append(candidate)
        if len(chosen) == count:
            return chosen
    raise AssertionError("failed to find a stable rational pocket cluster")


def planar_full_alphabet_instance(a=2):
    assert a == 2, "the exhaustive coordinate verifier is specialized to a=2"
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    z = (Fraction(0), Fraction(1))
    lower_left = [circle_point(-j) for j in range(2, 2 * a + 2)]
    # Six right-half circle vertices, all with parameter strictly between -1 and 1.
    parameters = [Fraction(1, j) for j in range(2, 3 * a // 2 + 2)]
    parameters += [Fraction(-1, j) for j in range(2, 3 * a // 2 + 2)]
    upper_pool = [circle_point(parameter) for parameter in parameters]
    assert len(lower_left) == 2 * a
    assert len(upper_pool) == 3 * a
    top = [u, v, z] + lower_left + upper_pool
    assert len(top) == 5 * a + 3
    assert all_general_position(top)
    assert in_convex_position(top)

    carrier_sets = [frozenset({u, v}) | frozenset(chosen)
                    for chosen in combinations(lower_left, a)]
    D = 2 ** a
    pocket = choose_pocket_points(D, top, u, v, z, carrier_sets, top)
    assert all_general_position(top + pocket)

    source_rank = a + (3 * a) // 2 + 3
    middle_rank = (3 * a) // 2
    expected_k = comb(3 * a, middle_rank)
    sources = set()
    incidences = []
    completion_counts = {}
    selected_edges = set()
    halfplane_face_universe = set()

    for carrier in carrier_sets:
        chosen_lower = frozenset(carrier) - {u, v}
        local_sources = []
        for middle in combinations(upper_pool, middle_rank):
            source = frozenset({u, v, z}) | chosen_lower | frozenset(middle)
            assert len(source) == source_rank
            assert in_convex_position(list(source))
            assert source not in sources
            sources.add(source)
            local_sources.append(source)
        assert len(local_sources) == expected_k

        for x in pocket:
            completion = frozenset(carrier) | {x}
            assert in_convex_position(list(completion))
            completion_counts[completion] = completion_counts.get(completion, 0) + 1

            positive = tuple(point for point in top
                             if point != z and orient(x, z, point) > 0)
            negative = tuple(point for point in top
                             if point != z and orient(x, z, point) < 0)
            assert len(positive) == 2 * a + 1
            assert len(negative) == 3 * a + 1
            richer = negative
            bank = tuple(frozenset({x, z}) | frozenset(subset)
                         for size in range(len(richer) + 1)
                         for subset in combinations(richer, size))
            assert len(bank) == 2 ** (3 * a + 1)
            assert all(in_convex_position(list(face)) for face in bank)
            halfplane_face_universe.update(bank)
            incidences.append({
                "cell": carrier,
                "letter": x,
                "completion": completion,
                "bank": bank,
                "weight": expected_k,
                "profile": (x, frozenset({u, v})),
            })

            for source in local_sources:
                edge = (source, x)
                assert edge not in selected_edges
                selected_edges.add(edge)
                assert not in_convex_position(list(source | {x}))

    N = comb(2 * a, a)
    bank_size = 2 ** (3 * a + 1)
    assert len(sources) == N * expected_k
    assert len(selected_edges) == D * N * expected_k
    assert len(incidences) == D * N
    assert max(completion_counts.values()) == 1

    full_energy, diagonal, collision = energy(incidences)
    expected_energy = Fraction(D * N * expected_k * expected_k, bank_size)
    assert full_energy == diagonal == expected_energy
    assert collision == 0
    assert full_energy == 75
    assert full_energy > D * D

    # The selected alphabet itself is a detached ordinary-face bank.
    pocket_faces = set()
    for size in range(D + 1):
        for subset in combinations(pocket, size):
            if in_convex_position(list(subset)):
                pocket_faces.add(frozenset(subset))
    # This particular finite cluster is convex, so its whole Boolean complex
    # is an explicit detached bank.  The report's scalable conclusion uses
    # the universal f(D) bound and does not assume convex position.
    assert len(pocket_faces) == 2 ** D

    padded_n = D * (2 ** source_rank)
    existing_n = len(top) + len(pocket)
    assert padded_n >= existing_n
    assert padded_n // (2 ** source_rank) == D
    return {
        "sources": len(sources),
        "edges": len(selected_edges),
        "completions": len(completion_counts),
        "bank": bank_size,
        "energy": full_energy,
        "pocket_faces": len(pocket_faces),
        "padded_n": padded_n,
        "rank": source_rank,
    }


def asymptotic_and_discharge_checks():
    for a in range(2, 101):
        D = 2 ** a
        N = comb(2 * a, a)
        k = comb(3 * a, (3 * a) // 2)
        B = 2 ** (3 * a + 1)
        exact_energy = Fraction(D * N * k * k, B)
        lower = Fraction(2 ** (6 * a - 1),
                         (2 * a + 1) * (3 * a + 1) ** 2)
        assert exact_energy >= lower
        assert exact_energy > D * D
        source_support = N * k
        selected_mass = D * source_support
        assert source_support <= 2 ** (5 * a)
        assert selected_mass <= 2 ** (6 * a)

        rank = a + (3 * a) // 2 + 3
        padded_n = D * (2 ** rank)
        assert padded_n // (2 ** rank) == D

    # Exact abstract source--alphabet bound with a supplied detached-bank size.
    for source_support, D, detached_faces in [(7, 5, 100), (20, 4, 64), (3, 9, 11)]:
        selected_mass = source_support * D
        ambient_lower = max(source_support, detached_faces)
        ratio = Fraction(selected_mass, ambient_lower)
        assert ratio <= min(Fraction(D), Fraction(source_support * D, detached_faces))


def strictly_inside_triangle(point, a, b, c):
    signs = (orient(a, b, point), orient(b, c, point), orient(c, a, point))
    triangle_sign = orient(a, b, c)
    return all(value > 0 for value in signs) if triangle_sign > 0 else all(
        value < 0 for value in signs
    )


def carrier_root_rectangle_check():
    """Exact rational three-arc realization of Proposition 4."""
    left = [circle_point(Fraction(-3)), circle_point(Fraction(-4))]
    right = [circle_point(Fraction(-1, 3)), circle_point(Fraction(-1, 4))]
    roots = [circle_point(Fraction(3, 4)), circle_point(Fraction(1)),
             circle_point(Fraction(4, 3))]
    outer = left + right + roots
    origin = (Fraction(0), Fraction(0))
    assert all_general_position(outer + [origin])
    assert in_convex_position(outer)

    carriers = [(u, v) for u in left for v in right]
    triangles = [(u, v, z) for u, v in carriers for z in roots]
    assert all(strictly_inside_triangle(origin, *triangle) for triangle in triangles)

    # Add a second exact blocker in the common open intersection.
    second = None
    for index in range(1, 1000):
        candidate = (Fraction(index, 10**6),
                     Fraction(index * index + 1, 10**9))
        if not all_general_position(outer + [origin, candidate]):
            continue
        if all(strictly_inside_triangle(candidate, *triangle)
               for triangle in triangles):
            second = candidate
            break
    assert second is not None
    blockers = [origin, second]

    # Ferrers formula for x=(0,0), z=(0,1).  Every cross pair is an edge;
    # same-side pairs are not.
    top_root = circle_point(Fraction(1))
    for u in left:
        a = -u[0]
        assert a > 0
        for v in right:
            c = v[0]
            assert c > 0
            assert u[1] / a + v[1] / c < 0
            assert strictly_inside_triangle(origin, u, v, top_root)
    for side in (left, right):
        for u, v in combinations(side, 2):
            assert not strictly_inside_triangle(origin, u, v, top_root)

    # h=1, p=3.  Marked sources have exact root-mark load h+1=2.
    underlying_load = {}
    marked_count = 0
    pair_load = {}
    completion_set = set()
    for u, v in carriers:
        top = frozenset({u, v}) | frozenset(roots)
        assert in_convex_position(list(top))
        for z in roots:
            others = [w for w in roots if w != z]
            for middle in combinations(others, 1):
                source = frozenset({u, v, z}) | frozenset(middle)
                assert in_convex_position(list(source))
                underlying_load[source] = underlying_load.get(source, 0) + 1
                marked_count += 1

            for x in blockers:
                assert strictly_inside_triangle(x, u, v, z)
                completion = frozenset({u, v, x})
                assert in_convex_position(list(completion))
                completion_set.add(completion)

                positive = [w for w in others if orient(x, z, w) > 0]
                negative = [w for w in others if orient(x, z, w) < 0]
                richer = positive if len(positive) >= len(negative) else negative
                # Retain a canonical h=1 subset if the richer side has size 2.
                retained = [sorted(richer)[0]]
                bank = [frozenset({x, z}), frozenset({x, z, retained[0]})]
                assert all(in_convex_position(list(face)) for face in bank)
                for face in bank:
                    pair = (completion, face)
                    pair_load[pair] = pair_load.get(pair, 0) + 1

    assert marked_count == len(carriers) * len(roots) * 2
    assert set(underlying_load.values()) == {2}
    assert len(underlying_load) == len(carriers) * comb(3, 2)
    assert len(completion_set) == len(carriers) * len(blockers)
    assert max(pair_load.values()) <= len(roots)
    assert 2 ** len(outer) == 128
    return {
        "carriers": len(carriers),
        "roots": len(roots),
        "blockers": len(blockers),
        "marked": marked_count,
        "sources": len(underlying_load),
        "pair_load": max(pair_load.values()),
        "outer_shield": 2 ** len(outer),
    }


def main():
    full, diagonal, collision, expected, profiles = abstract_alphabet_identity()
    result = planar_full_alphabet_instance()
    rectangle = carrier_root_rectangle_check()
    asymptotic_and_discharge_checks()
    print("PASS: exact full-alphabet diagonal/collision and thinning identity")
    print(f"PASS: abstract energy={full}, diagonal={diagonal}, collision={collision}, "
          f"random-average={expected}, profile-count={profiles}")
    print("PASS: rational full-cap common-top instance "
          f"sources={result['sources']}, edges={result['edges']}, "
          f"completions={result['completions']}, bank={result['bank']}, "
          f"energy={result['energy']}, pocket-faces={result['pocket_faces']}")
    print(f"PASS: exact cap padding n={result['padded_n']}, rank={result['rank']}")
    print("PASS: planar Ferrers carrier-root rectangle "
          f"carriers={rectangle['carriers']}, roots={rectangle['roots']}, "
          f"blockers={rectangle['blockers']}, marked={rectangle['marked']}, "
          f"sources={rectangle['sources']}, pair-load={rectangle['pair_load']}, "
          f"outer-shield={rectangle['outer_shield']}")
    print("PASS: scalable formulas and source--alphabet discharge through a=100")


if __name__ == "__main__":
    main()
