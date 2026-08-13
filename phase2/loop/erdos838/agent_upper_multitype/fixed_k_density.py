#!/usr/bin/env python3
"""Limiting convex-k density of an infinitely iterated vertical template.

For a fixed finite template S, all limits are obtained from triangular fixed
point equations for normalized cap, cup, and convex-set profiles.  Decimal
arithmetic avoids underflow at exp(-Theta(k^2)) densities.
"""

from __future__ import annotations

import argparse
import math
from decimal import Decimal, localcontext

from pascal_vk_probe import row


def D(x: int) -> Decimal:
    return Decimal(x)


def limiting_density(template, k: int, precision: int = 80):
    r, sc, su, sv = template
    facts = [math.factorial(i) for i in range(k + 1)]
    with localcontext() as ctx:
        ctx.prec = precision
        c = [Decimal(0)] * (k + 1)
        u = [Decimal(0)] * (k + 1)
        v = [Decimal(0)] * (k + 1)
        c[1] = u[1] = v[1] = Decimal(1)
        for size in range(2, k + 1):
            cap_sum = Decimal(0)
            cup_sum = Decimal(0)
            for j in range(2, min(size + 1, len(sc))):
                a = size - j + 1
                cap_sum += D(sc[j]) * c[a] / D(facts[a])
                cup_sum += D(su[j]) * u[a] / D(facts[a])
            factor = D(facts[size]) / (D(r) ** size)
            denominator = Decimal(1) - D(r) ** (1 - size)
            c[size] = factor * cap_sum / denominator
            u[size] = factor * cup_sum / denominator

            convex_sum = Decimal(0)
            for j in range(2, min(size + 1, len(sv))):
                if not sv[j]:
                    continue
                remaining = size - j + 2
                for a in range(1, remaining):
                    b = remaining - a
                    convex_sum += (
                        D(sv[j]) * c[a] * u[b]
                        / D(facts[a]) / D(facts[b])
                    )
            v[size] = factor * convex_sum / denominator
        return +c[k], +u[k], +v[k]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, nargs="+", default=[10, 15, 20, 25, 30, 40, 50])
    parser.add_argument("--max-template", type=int, default=40)
    parser.add_argument("--precision", type=int, default=100)
    args = parser.parse_args()
    for k in args.k:
        best = None
        for m in range(2, min(k, args.max_template + 1)):
            template = row(m, k)[m // 2]
            _, _, density = limiting_density(template, k, args.precision)
            gamma = -float(density.ln() / D(2).ln()) / (k * k)
            item = (gamma, m, template[0], density)
            if best is None or item[0] > best[0]:
                best = item
        assert best is not None
        gamma, m, r, density = best
        print(
            f"k={k} best_gamma={gamma:.10f} template_m={m} r={r} "
            f"log2density={-gamma*k*k:.10f} density={density:.8E}",
            flush=True,
        )


if __name__ == "__main__":
    main()
