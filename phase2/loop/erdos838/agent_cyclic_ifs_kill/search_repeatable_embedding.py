#!/usr/bin/env python3
"""Search exact prefix embeddings in the fitted cyclic three-map IFS.

For a convex word set S at depth d and fixed prefix words u,v, test whether
uS union vS is again in convex position.  All coordinates and orientation
tests are exact Fractions.  This is a discovery script; the final report only
uses candidates that also admit a symbolic/invariant-cone proof.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LEX = ROOT / "agent_lex_minimizer_search"
RV = ROOT / "agent_root_variance"
sys.path.insert(0, str(LEX))
sys.path.insert(0, str(RV))
import triangular_ifs_probe as ifs  # noqa: E402
import cyclic_ifs_maxplus as mp  # noqa: E402


def setup():
    data = json.loads((LEX / "exact_realizable_n9.json").read_text())
    points = sorted(tuple(map(Fraction, p)) for p in data["coordinates_as_stored"])
    groups = ((0, 1, 5), (2, 3, 4), (6, 7, 8))
    clusters = [[points[i] for i in group] for group in groups]
    macro = [ifs.centroid(cluster) for cluster in clusters]
    permutations = ((0, 1, 2), (2, 0, 1), (0, 2, 1))
    maps, metadata = ifs.make_maps(macro, clusters, permutations, Fraction(1))
    return macro, maps, metadata


def point_for_word(macro, maps, word):
    p = macro[word[-1]]
    for digit in reversed(word[:-1]):
        p = maps[digit](p)
    return p


def orient(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def strict_convex(points):
    """Every supplied point is a vertex of its convex hull."""
    pts = sorted(points)
    if len(set(pts)) != len(pts):
        return False

    def chain(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = chain(pts)
    hi = chain(list(reversed(pts)))
    return len(lo) + len(hi) - 2 == len(pts)


def main():
    macro, maps, _ = setup()
    cert = json.loads((RV / "cyclic_ifs_maxplus_certificate.json").read_text())
    convex = {
        row["depth"]: [tuple(w) for w in row["convex_words"]]
        for row in cert["rows"]
    }
    for k in (1, 2, 3):
        prefixes = list(itertools.product(range(3), repeat=k))
        winners = []
        for u, v in itertools.combinations(prefixes, 2):
            good = []
            for d in range(1, 7-k):
                words = [u+s for s in convex[d]] + [v+s for s in convex[d]]
                good.append(strict_convex([point_for_word(macro, maps, w) for w in words]))
            if all(good):
                winners.append((u, v))
        print("prefix length", k, "all-depth winners", winners[:20], "count", len(winners))

    # Stronger and easier-to-prove target: a two-block regular language whose
    # 2^r points are all extreme for several iterations.
    for k in (1, 2, 3, 4):
        blocks = list(itertools.product(range(3), repeat=k))
        winners = []
        for u, v in itertools.combinations(blocks, 2):
            for tail in range(3):
                good = True
                sizes = []
                for r in range(1, 5):
                    words = [sum(bs, ()) + (tail,) for bs in itertools.product((u, v), repeat=r)]
                    ok = strict_convex([point_for_word(macro, maps, w) for w in words])
                    good &= ok
                    sizes.append((len(words), ok))
                    if not good:
                        break
                if good:
                    winners.append((u, v, tail))
        print("regular block length", k, "winners", winners[:20], "count", len(winners))


if __name__ == "__main__":
    main()
