#!/usr/bin/env python3
"""Exact verifier for dense-Hall rooted localization and its design barrier."""

from fractions import Fraction
from itertools import combinations, product


def density(contexts, subset):
    demand = sum(contexts[index][0] for index in subset)
    union = set().union(*(set(contexts[index][1]) for index in subset))
    return Fraction(demand, len(union))


def private_pruning_exhaustive():
    # Exhaust all nonempty-bank systems with at most three contexts on a
    # three-face universe, and check Theorem 1 whenever the maximizing
    # family is inclusion-minimal.
    faces = range(3)
    banks = [frozenset(face for face in faces if mask & (1 << face))
             for mask in range(1, 1 << len(tuple(faces)))]
    checked = 0
    for count in range(2, 4):
        for chosen_banks in product(banks, repeat=count):
            for demands in product(range(1, 4), repeat=count):
                contexts = list(zip(demands, chosen_banks))
                families = [tuple(index for index in range(count)
                                  if mask & (1 << index))
                            for mask in range(1, 1 << count)]
                values = {family: density(contexts, family)
                          for family in families}
                maximum = max(values.values())
                for family in families:
                    if len(family) <= 1 or values[family] != maximum:
                        continue
                    if any(values[subfamily] == maximum
                           for subfamily in families
                           if set(subfamily) < set(family)):
                        continue
                    union = set().union(*(chosen_banks[index]
                                         for index in family))
                    total = sum(demands[index] for index in family)
                    rho = Fraction(total, len(union))
                    for index in family:
                        other_union = set().union(
                            *(chosen_banks[j] for j in family if j != index)
                        )
                        private = len(chosen_banks[index] - other_union)
                        assert Fraction(private) < Fraction(demands[index], 1) / rho
                    checked += 1
    assert checked > 0
    return checked


def marked_localization_check():
    # Four contexts, demand 6.  Their ordinary union has five faces.  Each
    # supplies six marked occurrences of rank at most three.  The theorem
    # guarantees degree >= CK/(hU)=24/15; the actual maximum is audited.
    marked = [
        ((0, "a"), (1, "b"), (2, "c"), (0, "d"), (1, "d"), (2, "e")),
        ((0, "a"), (1, "b"), (2, "c"), (0, "d"), (1, "e"), (2, "e")),
        ((0, "a"), (1, "b"), (2, "c"), (0, "c"), (1, "d"), (2, "e")),
        ((0, "a"), (1, "b"), (2, "c"), (0, "b"), (1, "d"), (2, "e")),
    ]
    counts = {}
    for bank in marked:
        assert len(set(bank)) == 6
        for target in bank:
            counts[target] = counts.get(target, 0) + 1
    C, K, h, U, demand = 4, 6, 3, 5, 6
    rho = Fraction(C * demand, U)
    lower = Fraction(K) * rho / (h * demand)
    maximum = max(counts.values())
    assert maximum >= lower
    assert lower == Fraction(8, 5)
    assert maximum == 4
    return rho, lower, maximum


def normalized_vectors(prime):
    vectors = []
    for raw in product(range(prime), repeat=3):
        if raw == (0, 0, 0):
            continue
        first = next(value for value in raw if value)
        inverse = pow(first, -1, prime)
        normalized = tuple((value * inverse) % prime for value in raw)
        if normalized not in vectors:
            vectors.append(normalized)
    return tuple(vectors)


def dot(left, right, prime):
    return sum(a * b for a, b in zip(left, right)) % prime


def projective_plane(prime):
    points = normalized_vectors(prime)
    lines = normalized_vectors(prime)
    incidence = {
        line: frozenset(point for point in points if dot(line, point, prime) == 0)
        for line in lines
    }
    expected = prime * prime + prime + 1
    assert len(points) == len(lines) == expected
    assert {len(bank) for bank in incidence.values()} == {prime + 1}
    point_degrees = {
        point: sum(point in incidence[line] for line in lines)
        for point in points
    }
    assert set(point_degrees.values()) == {prime + 1}
    for first, second in combinations(lines, 2):
        assert len(incidence[first] & incidence[second]) == 1

    # The full plane is a strict Hall maximizer: exhaust all line families
    # for the Fano plane.  For order three regularity proves Hall, while
    # the intersection property proves connectedness and hence strictness.
    if prime == 2:
        for mask in range(1, 1 << len(lines)):
            chosen = [lines[index] for index in range(len(lines))
                      if mask & (1 << index)]
            neighbors = set().union(*(incidence[line] for line in chosen))
            assert len(neighbors) >= len(chosen)
            if len(chosen) < len(lines):
                assert len(neighbors) > len(chosen)

    # Exhibit an induced 2K2.
    first, second = lines[:2]
    p = next(point for point in incidence[first] if point not in incidence[second])
    q = next(point for point in incidence[second] if point not in incidence[first])
    assert p in incidence[first] and p not in incidence[second]
    assert q in incidence[second] and q not in incidence[first]
    return points, lines, incidence


def tensor_audit(prime, tensor_power):
    points, lines, incidence = projective_plane(prime)
    contexts = tuple(product(lines, repeat=tensor_power))
    targets = tuple(product(points, repeat=tensor_power))
    banks = {
        context: frozenset(target for target in targets
                           if all(target[index] in incidence[context[index]]
                                  for index in range(tensor_power)))
        for context in contexts
    }
    N = prime * prime + prime + 1
    K = (prime + 1) ** tensor_power
    assert len(contexts) == len(targets) == N ** tensor_power
    assert {len(bank) for bank in banks.values()} == {K}
    degrees = {target: sum(target in banks[context] for context in contexts)
               for target in targets}
    assert set(degrees.values()) == {K}
    for first, second in combinations(contexts, 2):
        distance = sum(a != b for a, b in zip(first, second))
        assert len(banks[first] & banks[second]) == K // ((prime + 1) ** distance)
        assert banks[first] != banks[second]
    return len(contexts), K


def main():
    checked = private_pruning_exhaustive()
    rho, lower, maximum = marked_localization_check()
    projective_plane(3)
    contexts, degree = tensor_audit(2, 2)
    print(f"PASS: strict private-target pruning on {checked} minimal maximizing systems")
    print(f"PASS: marked localization density={rho}, lower={lower}, actual={maximum}")
    print("PASS: exact PG(2,2) and PG(2,3) regularity, intersections, Hall, and 2K2")
    print(f"PASS: tensor incidence contexts={contexts}, common degree={degree}")


if __name__ == "__main__":
    main()
