#!/usr/bin/env python3
"""Independent full scan of the provider's precomputed convex-k-gon files."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def scan(n: int, path: Path) -> dict:
    data = path.read_bytes()
    width = n - 2  # bytes for k=3,...,n
    if len(data) % width:
        raise ValueError("partial kgons record")
    best = None
    trace_count = lex_count = 0
    profile_histogram = Counter()
    best_index = None
    for index, offset in enumerate(range(0, len(data), width)):
        profile = tuple(data[offset : offset + width])
        trace = n + n * (n - 1) // 2 + sum(profile)  # nonempty
        moment = n + 2 * (n * (n - 1) // 2) + sum(
            (k + 3) * count for k, count in enumerate(profile)
        )
        pair = (trace, moment)
        if best is None or pair[0] < best[0]:
            best = pair
            trace_count = lex_count = 1
            profile_histogram = Counter({profile: 1})
            best_index = index
        elif pair[0] == best[0]:
            trace_count += 1
            profile_histogram[profile] += 1
            if pair[1] < best[1]:
                best = pair
                lex_count = 1
                best_index = index
            elif pair[1] == best[1]:
                lex_count += 1
    if best is None:
        raise ValueError("empty file")
    return {
        "n": n,
        "record_count": len(data) // width,
        "minimum_nonempty_count": best[0],
        "official_empty_inclusive_count": best[0] + 1,
        "lex_minimum_first_moment": best[1],
        "minimum_trace_record_count": trace_count,
        "lex_minimum_record_count": lex_count,
        "lex_minimum_record_index_zero_based": best_index,
        "minimum_profile_histogram_k3_onward": {
            ",".join(map(str, p)): count for p, count in sorted(profile_histogram.items())
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()
    result = {
        str(n): scan(n, args.data_dir / f"kgons{n:02}.b08") for n in (8, 9)
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
