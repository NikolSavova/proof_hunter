#!/usr/bin/env python3
"""Exact and heuristic Gate-A search for the Erdős 838 reflection-order model.

A reduced word for the longest permutation in S_n is viewed as a sorting
network.  Its root sequence is the sequence of wire-label pairs that cross.
For a positive root (i,j), i<j, attach the transvection I+z E_(j,i).
The forward and reverse products enumerate increasing- and decreasing-slope
paths.  Their Frobenius product is the convex-subset partition function in a
stretchable (coordinate-realizable) reflection order.

The script supports:

* exact integer and graded-polynomial evaluation;
* exhaustive enumeration of every reduced word for w_0 (practical to n=6);
* randomized Coxeter-move/annealing search in higher ranks;
* a sufficient fixed-x stretchability LP, with exact rational verification;
* coordinate/root-sequence cross-checks against ../reflection_trace.py.

All certificates are plain JSON and can be checked with ``check``.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
import time
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Root = tuple[int, int]
Word = tuple[int, ...]
Poly = tuple[int, ...]


def bubble_word(n: int) -> Word:
    """The standard reduced word 0,1,0,2,1,0,... for w_0."""
    return tuple(i for top in range(1, n) for i in range(top - 1, -1, -1))


def root_sequence(n: int, word: Sequence[int], require_w0: bool = True) -> tuple[Root, ...]:
    """Return beta_k = prefix(alpha_{word[k]}) as unordered label pairs."""
    wires = list(range(n))
    roots: list[Root] = []
    for step, generator in enumerate(word):
        if not 0 <= generator < n - 1:
            raise ValueError(f"invalid generator s_{generator} at step {step}")
        a, b = wires[generator], wires[generator + 1]
        if a > b:
            raise ValueError(f"word is not reduced from identity at step {step}: {a}>{b}")
        roots.append((a, b))
        wires[generator], wires[generator + 1] = b, a
    if require_w0:
        expected_length = n * (n - 1) // 2
        if len(word) != expected_length or wires != list(reversed(range(n))):
            raise ValueError("word is reduced but does not represent w_0")
    return tuple(roots)


def word_from_roots(n: int, roots: Sequence[Root]) -> Word:
    """Recover the sorting-network word from a reflection root sequence."""
    wires = list(range(n))
    word: list[int] = []
    for step, raw_root in enumerate(roots):
        root = tuple(sorted(raw_root))
        try:
            p = wires.index(root[0])
            q = wires.index(root[1])
        except ValueError as exc:
            raise ValueError(f"bad root at step {step}: {root}") from exc
        if abs(p - q) != 1:
            raise ValueError(f"root {root} is not an adjacent crossing at step {step}")
        generator = min(p, q)
        if wires[generator] > wires[generator + 1]:
            raise ValueError(f"root {root} would decrease Coxeter length at step {step}")
        word.append(generator)
        wires[generator], wires[generator + 1] = (
            wires[generator + 1], wires[generator]
        )
    if wires != list(reversed(range(n))):
        raise ValueError("root sequence does not end at w_0")
    return tuple(word)


def _integer_product(n: int, roots: Sequence[Root]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        row_i = matrix[i]
        row_j = matrix[j]
        matrix[j] = [a + b for a, b in zip(row_j, row_i)]
    return matrix


def _value_derivative_product(
    n: int, roots: Sequence[Root]
) -> tuple[list[list[int]], list[list[int]]]:
    """Return a transvection product and its entrywise derivative at z=1."""
    values = [[int(i == j) for j in range(n)] for i in range(n)]
    derivatives = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in roots:
        # row_j(z) <- row_j(z) + z row_i(z)
        values_i = values[i]
        derivatives_i = derivatives[i]
        old_values_j = values[j]
        old_derivatives_j = derivatives[j]
        values[j] = [a + b for a, b in zip(old_values_j, values_i)]
        derivatives[j] = [
            a + b + c
            for a, b, c in zip(old_derivatives_j, values_i, derivatives_i)
        ]
    return values, derivatives


def _poly_add_shift(left: Poly, right: Poly) -> Poly:
    """Return left + z*right."""
    degree = max(len(left), len(right) + 1)
    out = [0] * degree
    for k, value in enumerate(left):
        out[k] += value
    for k, value in enumerate(right):
        out[k + 1] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def _poly_product(left: Poly, right: Poly) -> Poly:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return tuple(out)


def _poly_product_matrix(n: int, roots: Sequence[Root]) -> list[list[Poly]]:
    zero, one = (0,), (1,)
    matrix = [[one if i == j else zero for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [
            _poly_add_shift(matrix[j][column], matrix[i][column])
            for column in range(n)
        ]
    return matrix


@dataclass(frozen=True)
class Evaluation:
    n: int
    trace: int
    endpoint_max: int
    cup_total: int
    cap_total: int
    first_moment: int
    cups: tuple[tuple[int, ...], ...]
    caps: tuple[tuple[int, ...], ...]
    graded: tuple[int, ...] | None = None

    @property
    def normalized(self) -> float:
        return math.log2(self.trace) / math.log2(self.n) ** 2 if self.n > 1 else math.inf

    @property
    def mean_size(self) -> float:
        return self.first_moment / self.trace

    @property
    def mean_minus_log_n(self) -> float:
        return self.mean_size - math.log2(self.n)

    def summary(self) -> dict[str, object]:
        return {
            "n": self.n,
            "trace": self.trace,
            "endpoint_max": self.endpoint_max,
            "cup_total": self.cup_total,
            "cap_total": self.cap_total,
            "first_moment": self.first_moment,
            "mean_size": self.mean_size,
            "mean_minus_log2_n": self.mean_minus_log_n,
            "normalized_log_trace": self.normalized,
            "graded": list(self.graded) if self.graded is not None else None,
        }


def evaluate_roots(n: int, roots: Sequence[Root], graded: bool = False) -> Evaluation:
    if len(roots) != n * (n - 1) // 2 or set(roots) != {
        (i, j) for i in range(n) for j in range(i + 1, n)
    }:
        raise ValueError("roots must contain every positive root exactly once")
    cups_list, cup_derivatives = _value_derivative_product(n, roots)
    caps_list, cap_derivatives = _value_derivative_product(n, tuple(reversed(roots)))
    trace = sum(
        cups_list[i][j] * caps_list[i][j]
        for i in range(n)
        for j in range(n)
    )
    endpoint_max = max(
        [1]
        + [
            cups_list[i][j] * caps_list[i][j]
            for i in range(n)
            for j in range(i)
        ]
    )
    # Z(z)=Nz+<A(z),B(z)>-N.
    first_moment = n + sum(
        cup_derivatives[i][j] * caps_list[i][j]
        + cups_list[i][j] * cap_derivatives[i][j]
        for i in range(n)
        for j in range(n)
    )
    graded_result: tuple[int, ...] | None = None
    if graded:
        cup_polys = _poly_product_matrix(n, roots)
        cap_polys = _poly_product_matrix(n, tuple(reversed(roots)))
        # <A(z),B(z)> has N at degree zero.  Replace that by Nz.
        accumulator = [0]
        for i in range(n):
            for j in range(n):
                product = _poly_product(cup_polys[i][j], cap_polys[i][j])
                if len(accumulator) < len(product):
                    accumulator.extend([0] * (len(product) - len(accumulator)))
                for degree, coefficient in enumerate(product):
                    accumulator[degree] += coefficient
        accumulator[0] -= n
        if len(accumulator) < 2:
            accumulator.append(0)
        accumulator[1] += n
        while len(accumulator) > 1 and accumulator[-1] == 0:
            accumulator.pop()
        graded_result = tuple(accumulator)
        if sum(graded_result) != trace:
            raise AssertionError("graded specialization at z=1 disagrees with trace")
        if sum(k * value for k, value in enumerate(graded_result)) != first_moment:
            raise AssertionError("graded derivative at z=1 disagrees with first moment")
    return Evaluation(
        n=n,
        trace=trace,
        endpoint_max=endpoint_max,
        cup_total=sum(map(sum, cups_list)),
        cap_total=sum(map(sum, caps_list)),
        first_moment=first_moment,
        cups=tuple(map(tuple, cups_list)),
        caps=tuple(map(tuple, caps_list)),
        graded=graded_result,
    )


def evaluate_word(n: int, word: Sequence[int], graded: bool = False) -> Evaluation:
    return evaluate_roots(n, root_sequence(n, word), graded=graded)


def reduced_words(n: int) -> Iterator[Word]:
    """Generate every reduced decomposition of w_0 by ascent-only DFS."""
    target_length = n * (n - 1) // 2
    permutation = list(range(n))
    word: list[int] = []

    def visit() -> Iterator[Word]:
        if len(word) == target_length:
            yield tuple(word)
            return
        for i in range(n - 1):
            if permutation[i] < permutation[i + 1]:
                permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]
                word.append(i)
                yield from visit()
                word.pop()
                permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]

    yield from visit()


def random_reduced_word(n: int, rng: random.Random) -> Word:
    permutation = list(range(n))
    word: list[int] = []
    while permutation != list(reversed(range(n))):
        ascents = [i for i in range(n - 1) if permutation[i] < permutation[i + 1]]
        i = rng.choice(ascents)
        word.append(i)
        permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]
    return tuple(word)


def coxeter_moves(word: Sequence[int]) -> tuple[list[int], list[int]]:
    commuting = [i for i in range(len(word) - 1) if abs(word[i] - word[i + 1]) > 1]
    braids = [
        i
        for i in range(len(word) - 2)
        if word[i] == word[i + 2] and abs(word[i] - word[i + 1]) == 1
    ]
    return commuting, braids


def _heap_closures(word: Word) -> tuple[list[int], list[int]]:
    """Transitive predecessor/successor bitsets for the Coxeter heap."""
    length = len(word)
    predecessors = [0] * length
    for q in range(length):
        bits = 0
        for p in range(q):
            if abs(word[p] - word[q]) <= 1:
                bits |= (1 << p) | predecessors[p]
        predecessors[q] = bits
    successors = [0] * length
    for p in range(length - 1, -1, -1):
        bits = 0
        for q in range(p + 1, length):
            if abs(word[p] - word[q]) <= 1:
                bits |= (1 << q) | successors[q]
        successors[p] = bits
    return predecessors, successors


def _greedy_extension(word: Word, selected_bits: int | None = None) -> list[int]:
    """Lexicographically least linear extension of a heap-induced subposet."""
    predecessors, _ = _heap_closures(word)
    remaining = (
        (1 << len(word)) - 1 if selected_bits is None else selected_bits
    )
    placed = ((1 << len(word)) - 1) ^ remaining
    order: list[int] = []
    while remaining:
        available = [
            p
            for p in range(len(word))
            if (remaining >> p) & 1 and predecessors[p] & ~placed == 0
        ]
        if not available:
            raise AssertionError("heap has a cycle or selected set is not a downset")
        node = min(available, key=lambda p: (word[p], p))
        order.append(node)
        remaining ^= 1 << node
        placed |= 1 << node
    return order


def canonical_commutation_word(word: Word) -> Word:
    """Canonical key for a reduced word modulo short commutations."""
    return tuple(word[node] for node in _greedy_extension(word))


def braid_neighbors_mod_commutation(n: int, word: Word) -> set[Word]:
    """All commutation classes adjacent through one long braid.

    A triple of crossings can be exposed consecutively precisely when its
    three heap nodes form a convex three-element interval.  We construct an
    explicit linear extension containing the interval as a block, apply the
    long braid, and return the canonical representative of the new heap.
    """
    word = canonical_commutation_word(word)
    roots = root_sequence(n, word)
    root_position = {root: position for position, root in enumerate(roots)}
    predecessors, successors = _heap_closures(word)
    full_bits = (1 << len(word)) - 1
    neighbors: set[Word] = set()

    def topo_on_downset(bits: int) -> list[int]:
        remaining = bits
        placed = full_bits ^ bits
        order: list[int] = []
        while remaining:
            available = [
                p
                for p in range(len(word))
                if (remaining >> p) & 1 and predecessors[p] & ~placed == 0
            ]
            if not available:
                raise AssertionError("requested prefix is not a downset")
            node = min(available, key=lambda p: (word[p], p))
            order.append(node)
            remaining ^= 1 << node
            placed |= 1 << node
        return order

    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                triple_nodes = sorted(
                    (root_position[(a, b)], root_position[(a, c)], root_position[(b, c)])
                )
                first, middle, last = triple_nodes
                interval = 0
                for node in range(len(word)):
                    after_first = node == first or bool(successors[first] & (1 << node))
                    before_last = node == last or bool(successors[node] & (1 << last))
                    if after_first and before_last:
                        interval |= 1 << node
                triple_bits = sum(1 << node for node in triple_nodes)
                if interval != triple_bits:
                    continue

                prefix_bits = (
                    predecessors[first] | predecessors[middle] | predecessors[last]
                ) & ~triple_bits
                prefix = topo_on_downset(prefix_bits)
                used = prefix_bits | triple_bits
                placed = used
                suffix: list[int] = []
                remaining = full_bits & ~used
                while remaining:
                    available = [
                        p
                        for p in range(len(word))
                        if (remaining >> p) & 1 and predecessors[p] & ~placed == 0
                    ]
                    if not available:
                        raise AssertionError("failed to extend exposed braid block")
                    node = min(available, key=lambda p: (word[p], p))
                    suffix.append(node)
                    remaining ^= 1 << node
                    placed |= 1 << node
                node_order = prefix + triple_nodes + suffix
                exposed = tuple(word[node] for node in node_order)
                index = len(prefix)
                if not (
                    exposed[index] == exposed[index + 2]
                    and abs(exposed[index] - exposed[index + 1]) == 1
                ):
                    raise AssertionError("convex heap triple did not expose a Coxeter braid")
                neighbor = canonical_commutation_word(apply_braid(exposed, index))
                root_sequence(n, neighbor)  # validation
                if neighbor != word:
                    neighbors.add(neighbor)
    return neighbors


def apply_commutation(word: Word, index: int) -> Word:
    candidate = list(word)
    candidate[index], candidate[index + 1] = candidate[index + 1], candidate[index]
    return tuple(candidate)


def apply_braid(word: Word, index: int) -> Word:
    candidate = list(word)
    a, b = candidate[index], candidate[index + 1]
    candidate[index : index + 3] = [b, a, b]
    return tuple(candidate)


def fixed_x_realization(
    n: int, roots: Sequence[Root], denominator_limit: int = 10**8
) -> tuple[Fraction, ...] | None:
    """Find y_i with x_i=i realizing the order modulo disjoint commutations.

    Only pairs of roots sharing a vertex are constrained; disjoint
    transvections commute, so their relative slope order does not affect the
    products.  Strict homogeneous inequalities can be scaled to gap >= 1.
    Feasibility is solved numerically, but every returned point is converted to
    a rational and all inequalities are then rechecked exactly.
    """
    ordered_pairs: list[tuple[Root, Root]] = []
    root_list = list(roots)
    for a_pos, first in enumerate(root_list):
        for second in root_list[a_pos + 1 :]:
            if set(first) & set(second):
                ordered_pairs.append((first, second))

    # Each normal encodes slope(second)-slope(first) >= 1.  The scale 1 is
    # harmless because the original system is a homogeneous strict cone.
    exact_normals: list[list[Fraction]] = []
    for first, second in ordered_pairs:
        row = [Fraction(0) for _ in range(n)]
        i, j = first
        k, ell = second
        row[j] += Fraction(1, j - i)
        row[i] -= Fraction(1, j - i)
        row[ell] -= Fraction(1, ell - k)
        row[k] += Fraction(1, ell - k)
        exact_normals.append([-value for value in row])

    if not exact_normals:
        return tuple(Fraction(0) for _ in range(n))

    # A dependency-free cyclic projection solver.  It is only used to *find*
    # a sufficient realization: every success is rationally certified below,
    # while failure is reported as "not certified", never as infeasibility.
    normals = [[float(value) for value in row] for row in exact_normals]
    squared_norms = [sum(value * value for value in row) for row in normals]
    y = [0.0] * n
    for epoch in range(10_000):
        largest_violation = 0.0
        for normal, squared_norm in zip(normals, squared_norms):
            dot = sum(a * b for a, b in zip(normal, y))
            if dot < 1.0:
                correction = (1.0 - dot) / squared_norm
                for index in range(n):
                    y[index] += correction * normal[index]
                largest_violation = max(largest_violation, 1.0 - dot)
        # Translation is free; anchoring avoids needless coordinate drift.
        offset = y[0]
        y = [value - offset for value in y]
        if largest_violation < 1e-9:
            break
    else:
        return None

    # Scale once more before rational reconstruction to leave a large exact
    # safety margin against the walls.
    y = [1000.0 * value for value in y]
    rational_ys = tuple(
        Fraction(value).limit_denominator(denominator_limit) for value in y
    )

    def slope(root: Root, coordinates: Sequence[Fraction]) -> Fraction:
        i, j = root
        return (coordinates[j] - coordinates[i]) / (j - i)

    if not all(
        slope(first, rational_ys) < slope(second, rational_ys)
        for first, second in ordered_pairs
    ):
        # The LP margin makes this exceptional, but do not emit a float-only
        # certificate if rational reconstruction happened to cross a wall.
        return None
    integer_ys = tuple(Fraction(round(value)) for value in y)
    if all(
        slope(first, integer_ys) < slope(second, integer_ys)
        for first, second in ordered_pairs
    ):
        return integer_ys
    return rational_ys


def verify_fixed_x(n: int, roots: Sequence[Root], ys: Sequence[Fraction]) -> bool:
    if len(ys) != n:
        return False
    slopes = {
        root: (ys[root[1]] - ys[root[0]]) / (root[1] - root[0]) for root in roots
    }
    for a_pos, first in enumerate(roots):
        for second in roots[a_pos + 1 :]:
            if set(first) & set(second) and not slopes[first] < slopes[second]:
                return False
    return True


def make_certificate(n: int, word: Word, graded: bool = True) -> dict[str, object]:
    roots = root_sequence(n, word)
    evaluation = evaluate_roots(n, roots, graded=graded)
    ys = fixed_x_realization(n, roots) if n <= 10 else None
    return {
        "n": n,
        "word_zero_based": list(word),
        "root_sequence_zero_based": [list(root) for root in roots],
        "evaluation": evaluation.summary(),
        "cups": [list(row) for row in evaluation.cups],
        "caps": [list(row) for row in evaluation.caps],
        "fixed_x_rational_y": [str(value) for value in ys] if ys is not None else None,
        "fixed_x_status": (
            "rational_certificate"
            if ys is not None
            else ("not_attempted_large_n" if n > 10 else "not_certified")
        ),
    }


def exhaustive(n: int, output: Path | None = None) -> dict[str, object]:
    started = time.monotonic()
    count = 0
    trace_histogram: Counter[int] = Counter()
    minimum: int | None = None
    min_word: Word | None = None
    min_count = 0
    min_endpoint = None
    minimum_mean_eval: Evaluation | None = None
    minimum_mean_word: Word | None = None
    minimum_mean_count = 0
    for word in reduced_words(n):
        evaluation = evaluate_word(n, word)
        count += 1
        trace_histogram[evaluation.trace] += 1
        if minimum is None or evaluation.trace < minimum:
            minimum = evaluation.trace
            min_word = word
            min_count = 1
            min_endpoint = evaluation.endpoint_max
        elif evaluation.trace == minimum:
            min_count += 1
            if word < min_word:  # type: ignore[operator]
                min_word = word
            min_endpoint = min(min_endpoint, evaluation.endpoint_max)  # type: ignore[arg-type]
        if (
            minimum_mean_eval is None
            or evaluation.first_moment * minimum_mean_eval.trace
            < minimum_mean_eval.first_moment * evaluation.trace
        ):
            minimum_mean_eval = evaluation
            minimum_mean_word = word
            minimum_mean_count = 1
        elif (
            evaluation.first_moment * minimum_mean_eval.trace
            == minimum_mean_eval.first_moment * evaluation.trace
        ):
            minimum_mean_count += 1
            if word < minimum_mean_word:  # type: ignore[operator]
                minimum_mean_word = word
    if minimum is None or min_word is None or minimum_mean_eval is None or minimum_mean_word is None:
        raise AssertionError("empty exhaustive search")
    certificate = make_certificate(n, min_word)
    result: dict[str, object] = {
        "mode": "exhaustive_reduced_words",
        "n": n,
        "reduced_word_count": count,
        "distinct_trace_count": len(trace_histogram),
        "minimum_trace": minimum,
        "minimum_word_count": min_count,
        "minimum_normalized_log_trace": math.log2(minimum) / math.log2(n) ** 2,
        "minimum_endpoint_max_among_min_trace": min_endpoint,
        "minimum_mean_size": minimum_mean_eval.mean_size,
        "minimum_mean_minus_log2_n": minimum_mean_eval.mean_minus_log_n,
        "minimum_mean_word_count": minimum_mean_count,
        "elapsed_seconds": time.monotonic() - started,
        "trace_histogram": {str(k): v for k, v in sorted(trace_histogram.items())},
        "certificate": certificate,
        "minimum_mean_certificate": make_certificate(n, minimum_mean_word),
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def exhaustive_commutation_classes(
    n: int, output: Path | None = None
) -> dict[str, object]:
    """Enumerate every reduced-word commutation class through braid flips."""
    started = time.monotonic()
    initial = canonical_commutation_word(bubble_word(n))
    queue = [initial]
    seen = {initial}
    cursor = 0
    minimum_eval: Evaluation | None = None
    minimum_word: Word | None = None
    minimum_count = 0
    minimum_mean_eval: Evaluation | None = None
    minimum_mean_word: Word | None = None
    minimum_mean_count = 0
    trace_histogram: Counter[int] = Counter()
    degrees: Counter[int] = Counter()
    while cursor < len(queue):
        word = queue[cursor]
        cursor += 1
        evaluation = evaluate_word(n, word)
        trace_histogram[evaluation.trace] += 1
        if minimum_eval is None or evaluation.trace < minimum_eval.trace:
            minimum_eval, minimum_word, minimum_count = evaluation, word, 1
        elif evaluation.trace == minimum_eval.trace:
            minimum_count += 1
            if word < minimum_word:  # type: ignore[operator]
                minimum_word = word
        if (
            minimum_mean_eval is None
            or evaluation.first_moment * minimum_mean_eval.trace
            < minimum_mean_eval.first_moment * evaluation.trace
        ):
            minimum_mean_eval, minimum_mean_word, minimum_mean_count = evaluation, word, 1
        elif (
            evaluation.first_moment * minimum_mean_eval.trace
            == minimum_mean_eval.first_moment * evaluation.trace
        ):
            minimum_mean_count += 1
            if word < minimum_mean_word:  # type: ignore[operator]
                minimum_mean_word = word
        neighbors = braid_neighbors_mod_commutation(n, word)
        degrees[len(neighbors)] += 1
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    if (
        minimum_eval is None
        or minimum_word is None
        or minimum_mean_eval is None
        or minimum_mean_word is None
    ):
        raise AssertionError("empty class enumeration")
    result: dict[str, object] = {
        "mode": "exhaustive_commutation_classes",
        "n": n,
        "commutation_class_count": len(seen),
        "distinct_trace_count": len(trace_histogram),
        "minimum_trace": minimum_eval.trace,
        "minimum_class_count": minimum_count,
        "minimum_normalized_log_trace": minimum_eval.normalized,
        "minimum_mean_size": minimum_mean_eval.mean_size,
        "minimum_mean_minus_log2_n": minimum_mean_eval.mean_minus_log_n,
        "minimum_mean_class_count": minimum_mean_count,
        "elapsed_seconds": time.monotonic() - started,
        "trace_histogram": {str(k): v for k, v in sorted(trace_histogram.items())},
        "flip_degree_histogram": {str(k): v for k, v in sorted(degrees.items())},
        "certificate": make_certificate(n, minimum_word),
        "minimum_mean_certificate": make_certificate(n, minimum_mean_word),
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def heuristic(
    n: int,
    steps: int,
    restarts: int,
    seed: int,
    output: Path | None = None,
    objective: str = "trace",
) -> dict[str, object]:
    rng = random.Random(seed)
    started = time.monotonic()
    global_best_word: Word | None = None
    global_best_eval: Evaluation | None = None
    evaluated_braids = 0
    accepted_braids = 0
    commutations = 0
    distinct_words: set[Word] = set()
    restart_summaries: list[dict[str, object]] = []
    def score(evaluation: Evaluation) -> float:
        if objective == "trace":
            return math.log(evaluation.trace)
        if objective == "mean-deficit":
            return evaluation.mean_minus_log_n
        raise ValueError(f"unknown objective: {objective}")

    for restart in range(restarts):
        word = bubble_word(n) if restart == 0 else random_reduced_word(n, rng)
        current = evaluate_word(n, word)
        local_best_word, local_best = word, current
        for step in range(steps):
            commuting, braids = coxeter_moves(word)
            # Commutations are free objective-preserving moves and essential
            # for exposing different long braid moves.
            total_moves = len(commuting) + len(braids)
            if total_moves == 0:
                break
            choice = rng.randrange(total_moves)
            if choice < len(commuting):
                word = apply_commutation(word, commuting[choice])
                commutations += 1
                distinct_words.add(word)
                continue
            candidate_word = apply_braid(word, braids[choice - len(commuting)])
            candidate = evaluate_word(n, candidate_word)
            evaluated_braids += 1
            # Slowly cool from an O(1) log-temperature to near-greedy.  A
            # periodic reheat prevents early freezing in a commutation class.
            phase = (step % max(1000, steps // 5)) / max(999, steps // 5 - 1)
            temperature = 0.5 * (1.0 - phase) + 0.002
            score_difference = score(candidate) - score(current)
            if score_difference <= 0 or rng.random() < math.exp(-score_difference / temperature):
                word, current = candidate_word, candidate
                accepted_braids += 1
                distinct_words.add(word)
            if score(current) < score(local_best):
                local_best_word, local_best = word, current
            if global_best_eval is None or score(current) < score(global_best_eval):
                global_best_word, global_best_eval = word, current
        restart_summaries.append(
            {
                "restart": restart,
                "best_trace": local_best.trace,
                "best_normalized_log_trace": local_best.normalized,
                "best_word": list(local_best_word),
                "best_mean_size": local_best.mean_size,
                "best_mean_minus_log2_n": local_best.mean_minus_log_n,
            }
        )
    if global_best_word is None or global_best_eval is None:
        raise AssertionError("heuristic search produced no candidate")
    result: dict[str, object] = {
        "mode": "coxeter_annealing",
        "n": n,
        "steps_per_restart": steps,
        "restarts": restarts,
        "seed": seed,
        "objective": objective,
        "evaluated_braids": evaluated_braids,
        "accepted_braids": accepted_braids,
        "commutations": commutations,
        "distinct_total_words_seen": len(distinct_words),
        "elapsed_seconds": time.monotonic() - started,
        "best_trace": global_best_eval.trace,
        "best_normalized_log_trace": global_best_eval.normalized,
        "restarts_summary": restart_summaries,
        "certificate": make_certificate(n, global_best_word),
    }
    if output is not None:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def _parse_certificate(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text())
    return data.get("certificate", data)


def check_certificate(path: Path) -> dict[str, object]:
    certificate = _parse_certificate(path)
    n = int(certificate["n"])
    word = tuple(map(int, certificate["word_zero_based"]))
    rebuilt = make_certificate(n, word)
    claimed_eval = certificate.get("evaluation", {})
    if rebuilt["evaluation"] != claimed_eval:
        raise AssertionError("evaluation does not match certificate")
    raw_y = certificate.get("fixed_x_rational_y")
    if raw_y is not None:
        roots = root_sequence(n, word)
        ys = tuple(Fraction(value) for value in raw_y)
        if not verify_fixed_x(n, roots, ys):
            raise AssertionError("fixed-x realization does not verify exactly")
    return rebuilt


def read_coordinate_roots(path: Path) -> tuple[int, tuple[Root, ...]]:
    parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent))
    import reflection_trace  # type: ignore

    points = reflection_trace.read_points(path)
    roots = tuple((i, j) for _, i, j in reflection_trace.slope_order(points))
    return len(points), roots


def selftest() -> None:
    for n in range(2, 8):
        word = bubble_word(n)
        roots = root_sequence(n, word)
        assert word_from_roots(n, roots) == word
        value = evaluate_word(n, word, graded=True)
        assert value.graded is not None and sum(value.graded) == value.trace
    # Every 3-point set has exactly 2^3-1 nonempty convex subsets.
    for word in reduced_words(3):
        value = evaluate_word(3, word, graded=True)
        assert value.trace == 7
        assert value.graded == (0, 3, 3, 1)
    # Independent coordinate-path cross-check against the parent checker.
    parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(parent))
    import reflection_trace  # type: ignore

    cell = sorted(reflection_trace.pascal_cell(4, 2, Fraction(1, 97)))
    coordinate_roots = tuple(
        (i, j) for _, i, j in reflection_trace.slope_order(cell)
    )
    coordinate_word = word_from_roots(6, coordinate_roots)
    ours = evaluate_word(6, coordinate_word, graded=True)
    theirs = reflection_trace.evaluate(cell)
    assert (ours.cap_total, ours.cup_total, ours.trace, ours.endpoint_max) == theirs
    assert ours.graded == (0, 6, 15, 20, 9)

    epsilon = Fraction(1, 16384)
    composition = sorted(
        (
            macro_x + epsilon * epsilon * micro_x,
            macro_y + epsilon * micro_y,
        )
        for macro_x, macro_y in cell
        for micro_x, micro_y in cell
    )
    composition_roots = tuple(
        (i, j) for _, i, j in reflection_trace.slope_order(composition)
    )
    composition_word = word_from_roots(36, composition_roots)
    ours_composition = evaluate_word(36, composition_word)
    theirs_composition = reflection_trace.evaluate(composition)
    assert (
        ours_composition.cap_total,
        ours_composition.cup_total,
        ours_composition.trace,
        ours_composition.endpoint_max,
    ) == theirs_composition
    print("algebraic root/word/graded and coordinate cross-checks: PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("selftest")
    exact_parser = sub.add_parser("exhaustive")
    exact_parser.add_argument("n", type=int)
    exact_parser.add_argument("--output", type=Path)
    classes_parser = sub.add_parser("classes")
    classes_parser.add_argument("n", type=int)
    classes_parser.add_argument("--output", type=Path)
    heuristic_parser = sub.add_parser("heuristic")
    heuristic_parser.add_argument("n", type=int)
    heuristic_parser.add_argument("--steps", type=int, default=100_000)
    heuristic_parser.add_argument("--restarts", type=int, default=8)
    heuristic_parser.add_argument("--seed", type=int, default=838)
    heuristic_parser.add_argument("--output", type=Path)
    heuristic_parser.add_argument(
        "--objective", choices=("trace", "mean-deficit"), default="trace"
    )
    check_parser = sub.add_parser("check")
    check_parser.add_argument("certificate", type=Path)
    coordinate_parser = sub.add_parser("coordinates")
    coordinate_parser.add_argument("points", type=Path)

    args = parser.parse_args()
    if args.command == "selftest":
        selftest()
    elif args.command == "exhaustive":
        result = exhaustive(args.n, args.output)
        print(json.dumps({k: v for k, v in result.items() if k != "trace_histogram"}, indent=2))
    elif args.command == "heuristic":
        result = heuristic(
            args.n, args.steps, args.restarts, args.seed, args.output, args.objective
        )
        print(json.dumps({k: v for k, v in result.items() if k != "restarts_summary"}, indent=2))
    elif args.command == "classes":
        result = exhaustive_commutation_classes(args.n, args.output)
        print(json.dumps({k: v for k, v in result.items() if k != "trace_histogram"}, indent=2))
    elif args.command == "check":
        result = check_certificate(args.certificate)
        print(json.dumps(result["evaluation"], indent=2))
    elif args.command == "coordinates":
        n, roots = read_coordinate_roots(args.points)
        word = word_from_roots(n, roots)
        result = make_certificate(n, word)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
