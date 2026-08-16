#!/usr/bin/env python3
"""Exact and coefficientwise audits for the rankwise near-maximal target."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RANK = ROOT / "agent_apa_rank"
GRADED = ROOT / "agent_graded_supersat"
sys.path[:0] = [str(HERE), str(RANK), str(GRADED)]

from amplification_probe import cap_cup_profiles  # noqa: E402
from graded_balanced import pascal_row, vertical_iterate  # noqa: E402
from low_addable_audit import audit, guarded_template  # noqa: E402
from verify_apa_counterexample import matrix_profile  # noqa: E402


def add_rankwise(row: dict[str, object]) -> dict[str, object]:
    level = int(row["L"])
    value = int(row["V"])
    counts = list(map(int, row["low_addable_counts_below_L"]))
    terms = [Q(2 ** (level - rank) * count, value) for rank, count in enumerate(counts)]
    maximum = max(terms)
    rank = terms.index(maximum)
    return {
        **row,
        "rankwise_terms": [str(item) for item in terms],
        "K": str(maximum),
        "K_decimal": float(maximum),
        "maximizing_rank": rank,
    }


def exact_coordinate_record() -> dict[str, object]:
    data = json.loads((HERE / "planar_rnp_record.json").read_text())
    points = tuple((Q(x), Q(y)) for x, y in enumerate(data["y_coordinates"]))
    row = add_rankwise(audit(points, tuple(data["search_profile"])))
    assert Q(row["K"]) == Q(2_679, 2_516) > Q(17, 16)
    assert Q(row["K"]) < Q(16, 15)
    assert row["maximizing_rank"] == 4
    return row


def profile_upper(profile: list[int], n: int, value: int) -> dict[str, object]:
    """Use N_r<=v_r to upper-bound K without enumerating links."""
    level = math.ceil(math.log2(n))
    terms = [Q(2 ** (level - rank) * profile[rank], value) for rank in range(level)]
    maximum = max(terms)
    return {
        "n": n,
        "L": level,
        "profile_upper_terms": [str(item) for item in terms],
        "profile_upper_K": str(maximum),
        "profile_upper_K_decimal": float(maximum),
        "maximizing_rank": terms.index(maximum),
    }


def central_profile_bounds() -> list[dict[str, object]]:
    rows = []
    for m in range(4, 17):
        n, _, _, convex = pascal_row(m, m + 2)[m // 2]
        profile = [1] + list(convex[1:])
        value = sum(profile)
        rows.append({"m": m, **profile_upper(profile, n, value)})
    assert max(Q(row["profile_upper_K"]) for row in rows) < Q(2, 3)
    assert all(
        Q(rows[index + 1]["profile_upper_K"]) < Q(rows[index]["profile_upper_K"])
        for index in range(4, len(rows) - 1)
    )
    return rows


def scalar_values(template, depth: int) -> list[tuple[int, int]]:
    r, cap_profile, cup_profile, convex_profile = template
    n = cap = cup = convex = 1
    answer = []
    for _ in range(depth):
        cap_factor = sum(
            value * n ** (rank - 1)
            for rank, value in enumerate(cap_profile)
            if rank >= 1
        )
        cup_factor = sum(
            value * n ** (rank - 1)
            for rank, value in enumerate(cup_profile)
            if rank >= 1
        )
        cross_factor = sum(
            value * n ** (rank - 2)
            for rank, value in enumerate(convex_profile)
            if rank >= 2
        )
        convex = r * convex + cap * cup * cross_factor
        cap *= cap_factor
        cup *= cup_factor
        n *= r
        answer.append((n, 1 + convex))
    return answer


def vertical_profile_bounds() -> dict[str, list[dict[str, object]]]:
    families = {}
    for parameter in (3, 4, 5):
        points = guarded_template(parameter)
        profile = list(matrix_profile(points))
        caps, cups = cap_cup_profiles(points)
        template = (
            len(points),
            list(caps),
            list(cups),
            [0] + profile[1:],
        )
        rows = []
        for depth, (n, value) in enumerate(scalar_values(template, 8), 1):
            level = math.ceil(math.log2(n))
            _, _, _, truncated = vertical_iterate(template, depth, level - 1)
            row = profile_upper([1] + truncated[1:], n, value)
            rows.append({"depth": depth, **row})
        assert all(
            Q(rows[index + 1]["profile_upper_K"]) < Q(rows[index]["profile_upper_K"])
            for index in range(len(rows) - 1)
        )
        families[f"guarded_k{parameter}"] = rows
    return families


def saved_exact_rows() -> dict[str, object]:
    source = json.loads((HERE / "low_addable_certificate.json").read_text())
    rows = {name: add_rankwise(row) for name, row in source["records"].items()}
    assert max(Q(row["K"]) for row in rows.values()) < Q(17, 16)
    assert Q(rows["guarded_template_k3_depth2"]["K"]) < Q(1, 400)
    return rows


def main() -> None:
    output = {
        "description": "rankwise near-maximal Hall target audit",
        "definition": "K=max_(r<L) 2^(L-r) N_r / V, L=ceil(log2 n)",
        "exact_coordinate_record": exact_coordinate_record(),
        "saved_exact_records": saved_exact_rows(),
        "central_Pascal_profile_upper_bounds": central_profile_bounds(),
        "guarded_vertical_profile_upper_bounds": vertical_profile_bounds(),
    }
    (HERE / "rankwise_nearmax_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("rankwise near-maximal audit: PASS")
    print(
        "exact coordinate K=",
        output["exact_coordinate_record"]["K_decimal"],
    )
    central = output["central_Pascal_profile_upper_bounds"]
    print(
        "central profile-only upper: first/last=",
        central[0]["profile_upper_K_decimal"],
        central[-1]["profile_upper_K_decimal"],
    )
    for name, rows in output["guarded_vertical_profile_upper_bounds"].items():
        print(
            name,
            "profile-only upper depth 1/8=",
            rows[0]["profile_upper_K_decimal"],
            rows[-1]["profile_upper_K_decimal"],
        )


if __name__ == "__main__":
    main()
