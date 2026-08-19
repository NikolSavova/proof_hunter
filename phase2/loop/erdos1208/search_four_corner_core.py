#!/usr/bin/env python3
"""Search exact 2-regular fixed-endpoint four-corner relation cores.

The four corner projections with c_0 fixed pair the relation records in four
perfect matchings.  For a matching quadruple, the endpoint labels are the
connected components of the appropriate two-colour subgraphs.  The relation
equation then determines c_1 as a Gaussian-linear form.  We test whether the
resulting formal point set has a repeated squared-distance polynomial.  If it
does not, a generic integral specialization is a distance-Sidon realization
of a nonempty four-corner 2-core.
"""

from __future__ import annotations

import argparse
import math
import random
from collections.abc import Iterator
from itertools import combinations


Gaussian = tuple[int, int]
Form = tuple[Gaussian, ...]
Matching = tuple[int, ...]


def perfect_matchings(n: int) -> Iterator[Matching]:
    """Yield fixed-point-free involutions of range(n)."""

    mate = [-1] * n

    def rec() -> Iterator[Matching]:
        try:
            first = next(index for index, value in enumerate(mate) if value < 0)
        except StopIteration:
            yield tuple(mate)
            return
        for second in range(first + 1, n):
            if mate[second] >= 0:
                continue
            mate[first] = second
            mate[second] = first
            yield from rec()
            mate[first] = mate[second] = -1

    yield from rec()


def edge_set(matching: Matching) -> frozenset[tuple[int, int]]:
    return frozenset((i, matching[i]) for i in range(len(matching)) if i < matching[i])


def two_colour_components(first: Matching, second: Matching) -> tuple[int, ...]:
    """Return canonical component ids of the union of two matchings."""

    n = len(first)
    labels = [-1] * n
    component = 0
    for root in range(n):
        if labels[root] >= 0:
            continue
        stack = [root]
        labels[root] = component
        while stack:
            vertex = stack.pop()
            for neighbour in (first[vertex], second[vertex]):
                if labels[neighbour] < 0:
                    labels[neighbour] = component
                    stack.append(neighbour)
        component += 1
    return tuple(labels)


def add(*forms: Form) -> Form:
    return tuple(
        (sum(form[j][0] for form in forms), sum(form[j][1] for form in forms))
        for j in range(len(forms[0]))
    )


def negate(form: Form) -> Form:
    return tuple((-real, -imag) for real, imag in form)


def multiply_i(form: Form) -> Form:
    return tuple((-imag, real) for real, imag in form)


def basis_form(dimension: int, index: int) -> Form:
    return tuple((1, 0) if j == index else (0, 0) for j in range(dimension))


def difference(left: Form, right: Form) -> Form:
    return add(left, negate(right))


def norm_signature(form: Form) -> tuple[Gaussian, ...]:
    """Hermitian Gram coefficients of |sum_j form_j z_j|^2."""

    signature: list[Gaussian] = []
    for row, (ar, ai) in enumerate(form):
        for br, bi in form[row:]:
            # conjugate(a) * b
            signature.append((ar * br + ai * bi, ar * bi - ai * br))
    return tuple(signature)


def build_forms(matchings: tuple[Matching, Matching, Matching, Matching]) -> tuple[list[Form], list[tuple[int, ...]]]:
    """Build split-role point forms and relation point indices.

    Matching order is 00, 01, 10, 11.  Components encode a0, a1, b0,
    and b1 respectively; p is a further basis variable and every c_r is
    p+i(a0-a1-b0+b1).
    """

    m00, m01, m10, m11 = matchings
    component_maps = (
        two_colour_components(m00, m01),
        two_colour_components(m10, m11),
        two_colour_components(m00, m10),
        two_colour_components(m01, m11),
    )
    component_counts = [max(mapping) + 1 for mapping in component_maps]
    offsets: list[int] = []
    running = 0
    for count in component_counts:
        offsets.append(running)
        running += count
    p_index = running
    dimension = p_index + 1
    base_forms = [basis_form(dimension, index) for index in range(dimension)]
    points = list(base_forms)
    relations: list[tuple[int, ...]] = []

    for record in range(len(m00)):
        a0, a1, b0, b1 = (
            offsets[role] + component_maps[role][record] for role in range(4)
        )
        inside = add(
            base_forms[a0],
            negate(base_forms[a1]),
            negate(base_forms[b0]),
            base_forms[b1],
        )
        c_form = add(base_forms[p_index], multiply_i(inside))
        c_index = len(points)
        points.append(c_form)
        relations.append((a0, a1, b0, b1, p_index, c_index))

    return points, relations


def repeated_norms(points: list[Form]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    seen: dict[tuple[Gaussian, ...], tuple[int, int]] = {}
    repeats: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for first, second in combinations(range(len(points)), 2):
        signature = norm_signature(difference(points[first], points[second]))
        previous = seen.get(signature)
        if previous is None:
            seen[signature] = (first, second)
        else:
            repeats.append((previous, (first, second)))
    return repeats


def unit_normalize(form: Form) -> Form:
    rotations = []
    value = form
    for _ in range(4):
        rotations.append(value)
        value = multiply_i(value)
    return min(rotations)


def repeated_unit_edges(points: list[Form]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    seen: dict[Form, tuple[int, int]] = {}
    repeats: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for first, second in combinations(range(len(points)), 2):
        signature = unit_normalize(difference(points[first], points[second]))
        previous = seen.get(signature)
        if previous is None:
            seen[signature] = (first, second)
        else:
            repeats.append((previous, (first, second)))
    return repeats


def has_distinct_forms(points: list[Form]) -> bool:
    return len(set(points)) == len(points)


def search(n: int, limit: int | None = None) -> None:
    all_matchings = list(perfect_matchings(n))
    fixed = all_matchings[0]
    fixed_edges = edge_set(fixed)
    candidates = [matching for matching in all_matchings if edge_set(matching).isdisjoint(fixed_edges)]
    checked = 0
    best: tuple[int, tuple[Matching, ...], list[tuple[tuple[int, int], tuple[int, int]]]] | None = None

    for m01 in candidates:
        used01 = fixed_edges | edge_set(m01)
        for m10 in candidates:
            if not edge_set(m10).isdisjoint(used01):
                continue
            used10 = used01 | edge_set(m10)
            for m11 in candidates:
                if not edge_set(m11).isdisjoint(used10):
                    continue
                matchings = (fixed, m01, m10, m11)
                points, relations = build_forms(matchings)
                if not has_distinct_forms(points):
                    continue
                repeats = repeated_norms(points)
                checked += 1
                score = len(repeats)
                if best is None or score < best[0]:
                    best = score, matchings, repeats
                    print("best", n, "checked", checked, "repeats", score, "points", len(points))
                    print("matchings", matchings)
                    print("relations", relations)
                    print("first repeats", repeats[:10])
                if not repeats:
                    print("GENERIC COUNTEREXAMPLE", n, matchings)
                    return
                if limit is not None and checked >= limit:
                    print("limit", checked)
                    return

    print("complete", n, "checked", checked, "best", None if best is None else best[0])


def random_search(n: int, limit: int, seed: int) -> None:
    rng = random.Random(seed)
    fixed_list = list(range(n))
    fixed = tuple(index ^ 1 for index in range(n))
    fixed_edges = edge_set(fixed)
    checked = 0
    best = 10**9

    def random_matching(used: set[tuple[int, int]]) -> Matching | None:
        for _ in range(100):
            unmatched = fixed_list.copy()
            rng.shuffle(unmatched)
            mate = [-1] * n
            success = True
            while unmatched:
                first = unmatched.pop()
                choices = [
                    second
                    for second in unmatched
                    if (min(first, second), max(first, second)) not in used
                ]
                if not choices:
                    success = False
                    break
                second = rng.choice(choices)
                unmatched.remove(second)
                mate[first] = second
                mate[second] = first
            if success:
                return tuple(mate)
        return None

    for trial in range(limit):
        used = set(fixed_edges)
        chosen = [fixed]
        for _ in range(3):
            matching = random_matching(used)
            if matching is None:
                break
            chosen.append(matching)
            used.update(edge_set(matching))
        if len(chosen) != 4:
            continue
        points, relations = build_forms(tuple(chosen))  # type: ignore[arg-type]
        if not has_distinct_forms(points):
            continue
        repeats = repeated_unit_edges(points)
        checked += 1
        if len(repeats) < best:
            best = len(repeats)
            print("random best", n, "trial", trial, "checked", checked, "unit repeats", best)
            print("matchings", tuple(chosen))
            print("relations", relations)
        if not repeats:
            norm_repeats = repeated_norms(points)
            print("NO UNIT REPEATS", n, "norm repeats", len(norm_repeats))
            print("matchings", tuple(chosen))
            if not norm_repeats:
                print("GENERIC COUNTEREXAMPLE")
            return
    print("random complete", n, "checked", checked, "best", best)


def core_score(matchings: tuple[Matching, Matching, Matching, Matching]) -> tuple[int, int, int]:
    m00, m01, m10, m11 = matchings
    maps = (
        two_colour_components(m00, m01),
        two_colour_components(m10, m11),
        two_colour_components(m00, m10),
        two_colour_components(m01, m11),
    )
    base_tokens = sorted({(role, component) for role, mapping in enumerate(maps) for component in mapping})
    # A sparse form is a sorted tuple (role, component, real, imaginary).
    sparse_points: list[tuple[tuple[int, int, int, int], ...]] = [
        ((role, component, 1, 0),) for role, component in base_tokens
    ]
    p_form = ((4, 0, 1, 0),)
    sparse_points.append(p_form)
    for record in range(len(m00)):
        sparse_points.append(
            tuple(
                sorted(
                    (
                        (0, maps[0][record], 0, 1),
                        (1, maps[1][record], 0, -1),
                        (2, maps[2][record], 0, -1),
                        (3, maps[3][record], 0, 1),
                        (4, 0, 1, 0),
                    )
                )
            )
        )
    duplicate_points = len(sparse_points) - len(set(sparse_points))

    def sparse_difference(
        left: tuple[tuple[int, int, int, int], ...],
        right: tuple[tuple[int, int, int, int], ...],
    ) -> tuple[tuple[int, int, int, int], ...]:
        coefficients: dict[tuple[int, int], tuple[int, int]] = {}
        for sign, form in ((1, left), (-1, right)):
            for role, component, real, imag in form:
                key = role, component
                old_real, old_imag = coefficients.get(key, (0, 0))
                coefficients[key] = old_real + sign * real, old_imag + sign * imag
        return tuple(
            (role, component, real, imag)
            for (role, component), (real, imag) in sorted(coefficients.items())
            if real or imag
        )

    def sparse_unit_normalize(
        form: tuple[tuple[int, int, int, int], ...]
    ) -> tuple[tuple[int, int, int, int], ...]:
        rotations = []
        current = form
        for _ in range(4):
            rotations.append(current)
            current = tuple((role, component, -imag, real) for role, component, real, imag in current)
        return min(rotations)

    seen: set[tuple[tuple[int, int, int, int], ...]] = set()
    repeats = 0
    for first, second in combinations(range(len(sparse_points)), 2):
        signature = sparse_unit_normalize(
            sparse_difference(sparse_points[first], sparse_points[second])
        )
        if signature in seen:
            repeats += 1
        else:
            seen.add(signature)
    return 10_000 * duplicate_points + repeats, duplicate_points, repeats


def anneal(n: int, steps: int, seed: int) -> None:
    rng = random.Random(seed)
    fixed = tuple(index ^ 1 for index in range(n))

    def fresh_matching(used: set[tuple[int, int]]) -> Matching:
        while True:
            vertices = list(range(n))
            rng.shuffle(vertices)
            mate = [-1] * n
            okay = True
            while vertices:
                first = vertices.pop()
                choices = [
                    second
                    for second in vertices
                    if (min(first, second), max(first, second)) not in used
                ]
                if not choices:
                    okay = False
                    break
                second = rng.choice(choices)
                vertices.remove(second)
                mate[first] = second
                mate[second] = first
            if okay:
                return tuple(mate)

    matchings: list[Matching] = [fixed]
    used = set(edge_set(fixed))
    for _ in range(3):
        matching = fresh_matching(used)
        matchings.append(matching)
        used.update(edge_set(matching))

    current = core_score(tuple(matchings))  # type: ignore[arg-type]
    best = current
    best_matchings = tuple(matchings)
    print("anneal initial", n, current)

    for step in range(steps):
        colour = rng.randrange(1, 4)
        old = matchings[colour]
        old_edges = list(edge_set(old))
        (a, b), (c, d) = rng.sample(old_edges, 2)
        if rng.randrange(2):
            replacements = ((min(a, c), max(a, c)), (min(b, d), max(b, d)))
        else:
            replacements = ((min(a, d), max(a, d)), (min(b, c), max(b, c)))
        if replacements[0] == replacements[1]:
            continue
        other_edges = set().union(
            *(edge_set(matchings[index]) for index in range(4) if index != colour)
        )
        if any(edge in other_edges for edge in replacements):
            continue
        candidate_list = list(old)
        for x, y in ((a, b), (c, d)):
            candidate_list[x] = candidate_list[y] = -1
        for x, y in replacements:
            candidate_list[x] = y
            candidate_list[y] = x
        candidate = tuple(candidate_list)
        matchings[colour] = candidate
        candidate_score = core_score(tuple(matchings))  # type: ignore[arg-type]
        temperature = max(0.05, 4.0 * (1.0 - step / steps))
        delta = candidate_score[0] - current[0]
        if delta <= 0 or rng.random() < math.exp(-delta / temperature):
            current = candidate_score
        else:
            matchings[colour] = old
        if current < best:
            best = current
            best_matchings = tuple(matchings)
            print("anneal best", n, "step", step, best)
            print("matchings", best_matchings)
        if best == (0, 0, 0):
            points, relations = build_forms(best_matchings)  # type: ignore[arg-type]
            norm_repeats = repeated_norms(points)
            print("NO UNIT REPEATS", "norm repeats", len(norm_repeats))
            print("relations", relations)
            return
    print("anneal complete", n, "best", best)
    print("matchings", best_matchings)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--random", action="store_true")
    parser.add_argument("--anneal", action="store_true")
    parser.add_argument("--seed", type=int, default=1208)
    args = parser.parse_args()
    assert args.n >= 2 and args.n % 2 == 0
    if args.anneal:
        anneal(args.n, args.limit or 100_000, args.seed)
    elif args.random:
        random_search(args.n, args.limit or 10_000, args.seed)
    else:
        search(args.n, args.limit)


if __name__ == "__main__":
    main()
