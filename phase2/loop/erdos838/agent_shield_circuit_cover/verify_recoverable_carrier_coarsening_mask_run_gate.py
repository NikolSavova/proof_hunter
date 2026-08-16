#!/usr/bin/env python3
"""Checks for RECOVERABLE_CARRIER_COARSENING_MASK_RUN_GATE."""

from itertools import combinations
from math import ceil, log2
from pathlib import Path
import runpy


def runs_and_gaps(mask, q):
    deleted = set(mask)
    retained = [i for i in range(q) if i not in deleted]
    if not deleted or len(retained) < 2:
        return [], []
    runs = []
    seen = set()
    for start in sorted(deleted):
        if start in seen or (start - 1) % q in deleted:
            continue
        run = []
        cur = start
        while cur in deleted:
            run.append(cur)
            seen.add(cur)
            cur = (cur + 1) % q
        runs.append(tuple(run))
    gaps = [((run[0] - 1) % q, (run[-1] + 1) % q) for run in runs]
    return runs, gaps


def maximum_disjoint_edges(edges):
    best = 0
    for r in range(len(edges) + 1):
        for chosen in combinations(edges, r):
            used = set()
            if all(not (set(e) & used) and not used.update(e) for e in chosen):
                best = max(best, r)
    return best


# Exhaustive cyclic masks.
mask_checks = 0
for q in range(4, 13):
    for bits in range(1, (1 << q) - 1):
        mask = [i for i in range(q) if bits >> i & 1]
        if q - len(mask) < 2:
            continue
        runs, gaps = runs_and_gaps(mask, q)
        assert len(runs) == len(gaps)
        assert max(map(len, runs)) >= ceil(len(mask) / len(runs))
        matching = maximum_disjoint_edges(gaps)
        assert matching >= ceil(len(gaps) / 3)
        mask_checks += 1

# Three-log scale and corrected-half deficit.
scale_rows = []
for L1 in (2**12, 2**14, 2**16):
    L2 = log2(L1)
    L3 = log2(L2)
    a = L3
    pure = L1 * a - a * a / 2
    C = 3
    corrected = (
        pure
        - C * (L1 * log2(L1) - (L1 - a) * log2(L1 - a))
    )
    assert pure > 0 and corrected > 0
    run_exp = L1 / L2
    assert run_exp < corrected
    scale_rows.append((int(L1), round(L2, 4), round(L3, 4),
                       round(corrected / L1, 4)))

# Many-gap threshold with beta=1/4, sigma=1/10.
beta = 1 / 4
sigma = 1 / 10
for L1 in (1000, 2000, 4000):
    L2 = log2(L1)
    g = ceil((3 * sigma / (2 * beta) + 0.1) * L2)
    log_bank = 2 * ceil(g / 3) * (beta * L1 - 3 * L2)
    assert log_bank >= sigma * L1 * L2

# Exact rational rooted modules and central-pair attachment obstruction.
here = Path(__file__).resolve().parent
runpy.run_path(
    str(here / "verify_high_transversal_common_pocket_endpoint_product.py")
)
barrier = runpy.run_path(
    str(here / "verify_almost_full_word_mixed_bank_barrier.py")
)
words, total_faces, star = barrier["check_geometry"]()
full_words, partial, one_sided = barrier["check_masks"]()
assert words == full_words == 4096
assert (total_faces, star, partial, one_sided) == (45, 7, 15625, 249)

print(
    "PASS: recoverable mask/run gate; masks=%d, scale_rows=%s, "
    "many-gap rooted threshold verified"
    % (mask_checks, scale_rows)
)
