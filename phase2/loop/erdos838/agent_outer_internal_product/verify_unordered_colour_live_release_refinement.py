#!/usr/bin/env python3
"""Checks UNORDERED_COLOUR_LIVE_RELEASE_REFINEMENT.md."""

from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial, log2


def entropy(probabilities):
    return -sum(value * log2(value) for value in probabilities if value)


def check_weighted_colouring():
    for ground, rank in [(5, 2), (6, 3), (7, 3)]:
        words = list(combinations(range(ground), rank))
        weights = {
            word: Q(1 + (sum(word) + len(word)) % 5, 5)
            for word in words
        }
        total = sum(weights.values(), Q(0))
        retained_sum = Q(0)
        best = Q(0)
        colouring_count = rank**ground
        for colouring in product(range(rank), repeat=ground):
            retained = sum(
                (
                    weights[word]
                    for word in words
                    if len({colouring[label] for label in word}) == rank
                ),
                Q(0),
            )
            retained_sum += retained
            best = max(best, retained)
        expected = total * Q(factorial(rank), rank**rank)
        assert retained_sum == colouring_count * expected
        assert best >= expected


def check_unordered_entropy_decoder():
    # Physical sources are unordered pairs on four labels.  Fix one injective
    # colouring and coordinatize retained pairs by their colours; no geometric
    # order on the pair is used.
    colouring = (0, 1, 0, 1)
    sources = [
        word
        for word in combinations(range(4), 2)
        if {colouring[label] for label in word} == {0, 1}
    ]
    coordinate_word = {
        source: tuple(
            next(label for label in source if colouring[label] == role)
            for role in range(2)
        )
        for source in sources
    }
    raw_weights = {source: 1 + sum(source) % 2 for source in sources}
    faces = (0, 1)
    role_sizes = (2, 2)
    masks = (0, 1, 2, 3)

    # Exhaust all source-only adaptive masks and several fully adaptive maps.
    maps = []
    for source_masks in product(masks, repeat=len(sources)):
        maps.append(
            {
                (source, face): source_masks[index]
                for index, source in enumerate(sources)
                for face in faces
            }
        )
    maps.append(
        {
            (source, face): (sum(source) + face) % 4
            for source in sources
            for face in faces
        }
    )

    raw_total = sum(raw_weights.values())
    source_weight_total = Q(raw_total, 2)  # scale atoms to <=1
    for mask_map in maps:
        outputs = {}
        input_probabilities = []
        mean_sigma = 0.0
        for source in sources:
            word = coordinate_word[source]
            for face in faces:
                probability = raw_weights[source] / (raw_total * len(faces))
                mask = mask_map[(source, face)]
                retained = tuple(
                    word[role] if not (mask >> role & 1) else None
                    for role in range(2)
                )
                output = (face, mask, retained)
                outputs[output] = outputs.get(output, 0.0) + probability
                input_probabilities.append(probability)
                mean_sigma += probability * sum(
                    log2(role_sizes[role])
                    for role in range(2)
                    if mask >> role & 1
                )
        h_input = entropy(input_probabilities)
        h_output = entropy(outputs.values())
        redundancy = mean_sigma - (h_input - h_output)
        assert h_output + mean_sigma + 1e-12 >= h_input
        assert redundancy >= -1e-12
        assert abs(mean_sigma - (h_input - h_output + redundancy)) < 1e-10
        assert h_output + mean_sigma + 1e-12 >= log2(float(source_weight_total)) + 1


if __name__ == "__main__":
    check_weighted_colouring()
    check_unordered_entropy_decoder()
    print("UNORDERED_COLOUR_LIVE_RELEASE_REFINEMENT verifier: PASS")
